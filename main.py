from flask import Flask, request
app = Flask(__name__)

ipBucket = {}

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

    return 'Home'
