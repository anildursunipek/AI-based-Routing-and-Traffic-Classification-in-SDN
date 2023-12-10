from flask import Flask, jsonify
import network
from mininet.net import Mininet
from models import Host
import mapperImpl


app = Flask("__name__")

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

@app.route('/topology/links', methods=['GET'])
def getLinks():
    result = network.getLinks()
    response = jsonify({
        "result": result,
        "status":200,
        "message":"success"
    })
    return response

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

@app.route('/topology/test/pingAll')
def pingAllTest():
    network.pingAllTest()
    return {
        "status": 200
    }

if __name__ == "__main__":
    app.run(debug=True)