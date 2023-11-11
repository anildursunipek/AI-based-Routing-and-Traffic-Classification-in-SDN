from flask import Flask, jsonify
import network
from mininet.net import Mininet
from models import Host
import mapperImpl


app = Flask("__name__")

@app.route('/topology/linear/<numberOfSwitches>/<hostsPerSwitch>')
def startLinearTopology(numberOfSwitches: int, hostsPerSwitch: int):
    topo = network.buildLinearTopo(int(numberOfSwitches), int(hostsPerSwitch))
    network.initalizeTopology(topo = topo)
    return {
        "status" : 200
    }

@app.route('/topology/startCustom')
def startCustomTopology():
    topo = network.buildCustomTopo()
    network.initalizeTopology(topo = topo)
    return {
        "status" : 200
    }

@app.route('/topology/stop')
def stopTopology():
    network.stopTopology()
    return {
        "status": 200
    }

@app.route('/topology/hosts', methods=['GET'])
def getHosts():
    result = network.getHosts()
    response = jsonify({
        "result":[mapperImpl.toHost(host) for host in result],
        "status":200,
        "message":"success"
    })
    return response

@app.route('/topology/switches')
def getSwitches():
    result = network.getSwitches()
    response = jsonify({
        "result": [mapperImpl.toSwitch(switch) for switch in result],
        "status": 200,
        "message": "success"
    })
    return response

@app.route('/topology/test')
def testTopology():
    result = network.testTopology()
    return {"result": result}

@app.route('/topology/generateTraffic')
def generateTopology():
    network.generateVirtualTraffic()
    return {}

if __name__ == "__main__":
    app.run(debug=True)