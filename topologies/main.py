from flask import Flask, request, jsonify
from flask_cors import cross_origin, CORS
from singleSwitchTopo import run, stop, getHostCount, getSwitchCount, getLinkCount, getSystemStatus, startProject, getStartDate, getHosts, getSwitchs
from model import Host

app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins':'http://localhost:4200'}})

@app.route("/start/single-switch-topo", methods=["POST"])
@cross_origin(origins="*", headers=['Content-Type'])
def startSingleSwitchTopology():
    data = request.json
    
    run(data)

    responce = jsonify({
        "result":data,
        "status":200,
        "message":"success"
    })
    return responce

@app.route("/stop/single-switch-topo", methods=["GET"])
@cross_origin(origins="*", headers=['Content-Type'])
def stopSingleSwitchTopology():
    stop()

    responce = jsonify({
        "result":True,
        "status":200,
        "message":"success"
    })
    return responce

@app.route("/get-host-count", methods=["GET"])
@cross_origin(origins="*", headers=['Content-Type'])
def getHostCountRepo():
    count = getHostCount()
    responce = jsonify({
        "result":count,
        "status":200,
        "message":"success"
    })
    return responce

@app.route("/get-switch-count", methods=["GET"])
@cross_origin(origins="*", headers=['Content-Type'])
def getSwitchCountRepo():
    count = getSwitchCount()
    responce = jsonify({
        "result":count,
        "status":200,
        "message":"success"
    })
    return responce

@app.route("/get-link-count", methods=["GET"])
@cross_origin(origins="*", headers=['Content-Type'])
def getLinkCountRepo():
    count = getLinkCount()
    responce = jsonify({
        "result":count,
        "status":200,
        "message":"success"
    })
    return responce

@app.route("/get-system-status", methods=["GET"])
@cross_origin(origins="*", headers=['Content-Type'])
def getSystemStatusRepo():
    status = getSystemStatus()
    responce = jsonify({
        "result":status,
        "status":200,
        "message":"success"
    })
    return responce

@app.route("/get-start-date", methods=["GET"])
@cross_origin(origins="*", headers=['Content-Type'])
def getStartDateRepo():
    status = getStartDate()
    responce = jsonify({
        "result":status,
        "status":200,
        "message":"success"
    })
    return responce


@app.route("/get-hosts", methods=["GET"])
@cross_origin(origins="*", headers=['Content-Type'])
def getHostsRepo():
    status = getHosts()
    responce = jsonify({
        "result":[toHost(host) for host in status],
        "status":200,
        "message":"success"
    })
    return responce

@app.route("/get-switchs", methods=["GET"])
@cross_origin(origins="*", headers=['Content-Type'])
def getSwitchsRepo():
    status = getSwitchs()
    responce = jsonify({
        "result":[toSwitch(switch) for switch in status],
        "status":200,
        "message":"success"
    })
    return responce

def toHost(host):
    return {
        'name': host.name,
        'IP': host.IP(),
        'MAC': host.MAC()
    }

def toPort(port):
    return {
        "port": port
    }

def toSwitch(switch):
    return {
    'name': switch.name,
    'dpid': switch.dpid,
    # 'ports': [port for port in switch.ports]
    # 'host_connections': [toHost(host) for host in switch.connections()],
    }
        

if __name__ == "__main__":
    startProject()
    app.run(debug=True)