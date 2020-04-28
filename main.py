from flask import Flask, request, abort
from redisTools import *
from ConfigManager import ConfigManager

app = Flask(__name__)
cm = ConfigManager()
NREQ, TIME_RANGE_SEC, TIME_LOCK_SEC = cm.readConfig()


@app.route('/')
def home():
    ip = getIp(request)
    subNet = ip[:ip.rfind('.')]

    if subNet in cm.getUnlimAccessNetworks():
        return ip
    elif responseAllowed(subNet, NREQ, TIME_RANGE_SEC, TIME_LOCK_SEC):
        return ip
    else:
        abort(429)
