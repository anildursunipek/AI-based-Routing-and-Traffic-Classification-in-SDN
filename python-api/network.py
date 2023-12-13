from mininet.net import Mininet
from mininet.node import OVSKernelSwitch
from mininet.log import setLogLevel, info
from mininet.topo import Topo
from mininet.node import RemoteController, CPULimitedHost
from mininet.link import TCLink
from datetime import datetime
import threading
import time
import json

#Global Veriables
global net
trafficThreadList = []
systemStatus = False
startDate = None

class NsfnetTopo(Topo):
    def build( self, **params ):
        """
        Topology Link: https://github.com/BNN-UPC/NetworkModelingDatasets/blob/master/assets/nsfnet_topology.png
        """
        # Hosts
        h0 = self.addHost('h0', ip='10.0.0.1')
        h1 = self.addHost('h1', ip='10.0.0.2')
        h2 = self.addHost('h2', ip='10.0.0.3')
        h3 = self.addHost('h3', ip='10.0.0.4')
        h4 = self.addHost('h4', ip='10.0.0.5')
        h5 = self.addHost('h5', ip='10.0.0.6')
        h6 = self.addHost('h6', ip='10.0.0.7')
        h7 = self.addHost('h7', ip='10.0.0.8')
        h8 = self.addHost('h8', ip='10.0.0.9')
        h9 = self.addHost('h9', ip='10.0.0.10')
        h10 = self.addHost('h10', ip='10.0.0.11')
        h11 = self.addHost('h11', ip='10.0.0.12')
        h12 = self.addHost('h12', ip='10.0.0.13')
        h13 = self.addHost('h13', ip='10.0.0.14')

        # Switches
        s0 = self.addSwitch('s0', dpid='00:00:00:00:00:00:00:01', protocols="OpenFlow13")
        s1 = self.addSwitch('s1', dpid='00:00:00:00:00:00:00:02', protocols="OpenFlow13")
        s2 = self.addSwitch('s2', dpid='00:00:00:00:00:00:00:03', protocols="OpenFlow13")
        s3 = self.addSwitch('s3', dpid='00:00:00:00:00:00:00:04', protocols="OpenFlow13")
        s4 = self.addSwitch('s4', dpid='00:00:00:00:00:00:00:05', protocols="OpenFlow13")
        s5 = self.addSwitch('s5', dpid='00:00:00:00:00:00:00:06', protocols="OpenFlow13")
        s6 = self.addSwitch('s6', dpid='00:00:00:00:00:00:00:07', protocols="OpenFlow13")
        s7 = self.addSwitch('s7', dpid='00:00:00:00:00:00:00:08', protocols="OpenFlow13")
        s8 = self.addSwitch('s8', dpid='00:00:00:00:00:00:00:09', protocols="OpenFlow13")
        s9 = self.addSwitch('s9', dpid='00:00:00:00:00:00:00:10', protocols="OpenFlow13")
        s10 = self.addSwitch('s10', dpid='00:00:00:00:00:00:00:11', protocols="OpenFlow13")
        s11 = self.addSwitch('s11', dpid='00:00:00:00:00:00:00:12', protocols="OpenFlow13")
        s12 = self.addSwitch('s12', dpid='00:00:00:00:00:00:00:13', protocols="OpenFlow13")
        s13 = self.addSwitch('s13', dpid='00:00:00:00:00:00:00:14', protocols="OpenFlow13")

        # Links
        # Link options
        linkopts1 = dict(delay='25ms', bw=100, loss=0, max_queue_size=1000, use_htb=True) # between switch and host
        linkopts2 = dict(delay='25ms', bw=100, loss=0, max_queue_size=2000, use_htb=True) # between 2 switches

        # Switch to switch
        self.addLink(s0, s1, **linkopts2)
        self.addLink(s0, s2, **linkopts2)
        self.addLink(s0, s3, **linkopts2)
        self.addLink(s1, s7, **linkopts2)
        self.addLink(s1, s2, **linkopts2)
        self.addLink(s2, s5, **linkopts2)
        self.addLink(s3, s4, **linkopts2)
        self.addLink(s3, s8, **linkopts2)
        self.addLink(s4, s5, **linkopts2)
        self.addLink(s4, s6, **linkopts2)
        self.addLink(s5, s12, **linkopts2)
        self.addLink(s5, s13, **linkopts2)
        self.addLink(s6, s7, **linkopts2)
        self.addLink(s7, s10, **linkopts2)
        self.addLink(s8, s9, **linkopts2)
        self.addLink(s8, s11, **linkopts2)
        self.addLink(s9, s10, **linkopts2)
        self.addLink(s9, s12, **linkopts2)
        self.addLink(s10, s11, **linkopts2)
        self.addLink(s10, s13, **linkopts2)
        self.addLink(s11, s12, **linkopts2)

        # swith to host
        self.addLink(s0, h0, **linkopts1)
        self.addLink(s1, h1, **linkopts1)
        self.addLink(s2, h2, **linkopts1)
        self.addLink(s3, h3, **linkopts1)
        self.addLink(s4, h4, **linkopts1)
        self.addLink(s5, h5, **linkopts1)
        self.addLink(s6, h6, **linkopts1)
        self.addLink(s7, h7, **linkopts1)
        self.addLink(s8, h8, **linkopts1)
        self.addLink(s9, h9, **linkopts1)
        self.addLink(s10, h10, **linkopts1)
        self.addLink(s11, h11, **linkopts1)
        self.addLink(s12, h12, **linkopts1)
        self.addLink(s13, h13, **linkopts1)

def buildCustomTopo():
    topo = NsfnetTopo()
    return topo

def initalizeTopology(topo):
    global net
    global systemStatus
    global startDate

    net = Mininet(topo=topo, link=TCLink, build=False, switch=OVSKernelSwitch, autoSetMacs=True, waitConnected=True)
    
    # Adding floodlight controller here
    remote_ip = "127.0.0.1"
    info('** Adding Floodlight Controller\n')
    net.addController('c1', controller=RemoteController, ip=remote_ip, port=6653, protocols="OpenFlow13")

    # Build the network
    net.build()
    net.start()
    systemStatus = True
    startDate = datetime.now()
    net.pingAll()

def pingAllTest():
    global net
    info("PING ALL RESULT") 
    net.pingAll()

def writeJsonFile(result):
    existing_json_file = "traffic_result.json"

    with open(existing_json_file, "r") as file:
        existing_data = json.load(file)

    existing_data["results"].append(result["end"]["sum"])

    updated_json_data = json.dumps(existing_data, indent=2)

    with open(existing_json_file, "w") as file:
        file.write(updated_json_data)

def hostCommend(host, cmdText, receiver=None):
    h = net.get(host)
    result = h.cmd(cmdText)
    print(f"***********{host}***********")
    if receiver != None:
        result = json.loads(result)
        writeJsonFile(result)
        print(result)
        list(filter(lambda obj: obj["receiver"] == receiver and obj["sender"] == host , trafficThreadList))[0]["result"] = result

def testTopology():
    global net
    print("H1 BAŞLIYOR")
    print("VIDEO GELIYOR*************")

    thread1 = threading.Thread(target=hostCommend, args=("h1" ,"ffplay -i udp://10.0.0.2:1234"))
    thread2 = threading.Thread(target=hostCommend, args=("h2", "ffmpeg -re -i /home/batuhan/deneme/yuksek/video.ts -c copy -f mpegts udp://10.0.0.2:1234"))

    thread1.start()
    time.sleep(2)
    thread2.start()

    thread1.join()
    thread2.join()

    return "result"

def generateTraffic():
    # matriste [0][0] receiver [1][0] sender olmak üzerinde aralarında trafik oluşturmaktadır
    trafficHosts = [
        ["h1","h5","h7"], # receiver
        ["h2","h3","h9"], # sender
        ]
    
    tSecond = 15
    bandWidth = 30
    port = 5555
    for i in range(len(trafficHosts[0])):
        receiver = trafficHosts[0][i]
        sender = trafficHosts[1][i]

        receiverIP = "10.0.0."+ str(int(receiver[receiver.index('h') + 1:])+1) # hostun ipsini veriyor örneğin h3 hostunun ipsi 10.0.0.4
        senderIP = "10.0.0."+ str(int(sender[sender.index('h') + 1:])+1) # hostun ipsini veriyor örneğin h3 hostunun ipsi 10.0.0.4
        receiverThread = threading.Thread(target=hostCommend, args=(receiver ,f"iperf3 -s -p {port} -1 &"))
        senderThread = threading.Thread(target=hostCommend, args=(sender ,f"iperf3 -c {receiverIP} -u -b {bandWidth}G -p {port} -t {tSecond} -J ", receiver))

        trafficThreadList.append({"receiverThread":receiverThread,
                                   "senderThread":senderThread,
                                   "receiver":receiver,
                                   "sender":sender,
                                   "bandWidth":bandWidth,
                                   "second":tSecond,
                                   "receiverIP":receiverIP,
                                   "senderIP":senderIP,
                                   "startDate":datetime.now(),
                                   "result":None})
    
    for i in trafficThreadList:
        i["receiverThread"].start()

    time.sleep(2)

    for i in trafficThreadList:
        time.sleep(2)
        i["senderThread"].start()
    
    time.sleep(tSecond+5)

    for i in range(len(trafficHosts)):
        trafficThreadList[i]["receiverThread"].join()
        trafficThreadList[i]["senderThread"].join()

def getTraffic():
    new_list = []
    for trafficThreadListItem in trafficThreadList:
        new_item = {
            "receiver": trafficThreadListItem["receiver"],
            "sender": trafficThreadListItem["sender"],
            "bandWidth": trafficThreadListItem["bandWidth"],
            "second": trafficThreadListItem["second"],
            "receiverIP": trafficThreadListItem["receiverIP"],
            "senderIP": trafficThreadListItem["senderIP"],
            "startDate": trafficThreadListItem["startDate"],
            "result":trafficThreadListItem["result"]
        }
        new_list.append(new_item)

    return new_list

def stopTopology():
    global net
    global systemStatus
    global startDate
    global trafficThreadList
    net.stop()
    net = None
    trafficThreadList = []
    systemStatus = False
    startDate = None

def getHosts():
    global net
    return net.hosts

def getLinks():
    global net
    return net.links

def getSwitches():
    global net
    return net.switches