import redis

redisHost = open('redisHost.ini', 'r').readlines()[0][:-1]
r = redis.Redis(host=redisHost, port=6379, db=0)

def responseAllowed(token, nRequests, timeRange, lockTime):
    # Check the lock for subnet
    if r.get(token + '_LOCK'):
        return False
    else:
        with r.pipeline() as pipe:
            pipe.multi()
            # Issue expired token
            pipe.set(name=token, value=0, ex=timeRange, nx=True)
            pipe.incr(token)
            pipe.execute()

        # If the number of requests has not exceeded the limit,
        # allow the connection
        if r.get(token) != None and int((r.get(token)).decode('utf-8')) <= nRequests:
            
            return True
        else:
            # Set the lock for 2 minutes
            r.set(name=token + '_LOCK', value=0, ex=lockTime, nx=True)
            # Reset token
            r.delete(token)

            return False


def getIp(request):
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    return ip
