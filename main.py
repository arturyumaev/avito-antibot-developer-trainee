import redis
from flask import Flask, request, abort

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)


def responseAllowed(token, timeout=15, nRequests=3):
    # Check the lock for subnet
    if r.get(token + '_LOCK'):
        return False
    else:
        with r.pipeline() as pipe:
            pipe.multi()
            # Issue expired token
            pipe.set(name=token, value=0, ex=timeout, nx=True)
            pipe.incr(token)
            pipe.execute()

        # If the number of requests has not exceeded the limit,
        # allow the connection
        if r.get(token) != None and int((r.get(token)).decode('utf-8')) < nRequests:
            return True
        else:
            # Set the lock for 2 minutes
            r.set(name=token + '_LOCK', value=0, ex=120, nx=True)
            return False


def getIp(request):
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    return ip


@app.route('/')
def home():
    ip = getIp(request)
    subNet = ip[:ip.rfind('.')]

    if responseAllowed(subNet):
        return ip
    else:
        abort(429)