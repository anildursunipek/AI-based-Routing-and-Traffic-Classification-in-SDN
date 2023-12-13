from flask import Flask, jsonify
import network
from mininet.net import Mininet
from models import Host
from flask_cors import CORS  # Flask-CORS ekledik


app = Flask("__name__")
CORS(app)

@app.route('/topology/start')
def startCustomTopology():
    topo = network.buildCustomTopo()
    network.initalizeTopology(topo = topo)
    return {
        "status" : 200
    }

@app.route('/topology/get-system-status')
def getSystemStatus():
    status = network.systemStatus
    return {
        "status" : 200,
        "result":status
    }

@app.route('/topology/get-start-date')
def getStartDate():
    startDate = network.startDate
    return {
        "status" : 200,
        "result":startDate
    }

@app.route('/topology/stop')
def stopTopology():
    network.stopTopology()
    return {
        "status": 200
    }

@app.route('/topology/generate/traffic')
def generateTraffic():
    network.generateTraffic()
    return {
        "status": 200
    }

@app.route('/topology/get/traffic')
def getTraffic():
    traffic = network.getTraffic()
    return {
        "status": 200,
        "result":traffic
    }

@app.route('/topology/get-host-count')
def getHostCount():
    hosts = network.getHosts()
    return {
        "status": 200,
        "result":len(hosts)
    }

@app.route('/topology/get-switch-count')
def getSwitchCount():
    switches = network.getSwitches()
    return {
        "status": 200,
        "result":len(switches)
    }

@app.route('/topology/get-link-count')
def getLinkCount():
    links = network.getLinks()
    return {
        "status": 200,
        "result":len(links)
    }


# @app.route('/topology/links', methods=['GET'])
# def getLinks():
#     result = network.getLinks()
#     response = jsonify({
#         "result": result,
#         "status":200,
#         "message":"success"
#     })
#     return response

# @app.route('/topology/hosts', methods=['GET'])
# def getHosts():
#     result = network.getHosts()
#     response = jsonify({
#         "result":[mapperImpl.toHost(host) for host in result],
#         "status":200,
#         "message":"success"
#     })
#     return response

# @app.route('/topology/switches')
# def getSwitches():
#     result = network.getSwitches()
#     response = jsonify({
#         "result": [mapperImpl.toSwitch(switch) for switch in result],
#         "status": 200,
#         "message": "success"
#     })
#     return response

@app.route('/topology/test')
def testTopology():
    network.testTopology()
    return {"result": "result"}
 
# @app.route('/topology/generateTraffic')
# def generateTopology():
#     network.generateVirtualTraffic()

@app.route('/topology/test/pingAll')
def pingAllTest():
    network.pingAllTest()
    return {
        "status": 200
    }

if __name__ == "__main__":
    app.run(debug=True)