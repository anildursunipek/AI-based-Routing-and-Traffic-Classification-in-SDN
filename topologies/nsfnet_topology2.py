#!/usr/bin/python

from ast import List
import time
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch, CPULimitedHost, Host
from mininet.topo import Topo
from mininet.link import TCLink
import json
import pingparsing
import threading
from threading import Thread

class NsfnetTopo(Topo):
    """
    Topology Link: https://github.com/BNN-UPC/NetworkModelingDatasets/blob/master/assets/nsfnet_topology.png
    """
    def build( self, **params ):
        # Hosts
        hostCount = 12
        h0 = self.addHost('h0', ip='10.0.0.1', cpu=0.8/hostCount)
        # h1 = self.addHost('h1', ip='10.0.0.2', cpu=0.8/hostCount)
        # h2 = self.addHost('h2', ip='10.0.0.3', cpu=0.8/hostCount)
        h3 = self.addHost('h3', ip='10.0.0.4', cpu=0.8/hostCount)
        # h4 = self.addHost('h4', ip='10.0.0.5', cpu=0.8/hostCount)
        # h5 = self.addHost('h5', ip='10.0.0.6', cpu=0.8/hostCount)
        # h6 = self.addHost('h6', ip='10.0.0.7', cpu=0.8/hostCount)
        # h7 = self.addHost('h7', ip='10.0.0.8', cpu=0.8/hostCount)
        h8 = self.addHost('h8', ip='10.0.0.9', cpu=0.8/hostCount)
        h9 = self.addHost('h9', ip='10.0.0.10', cpu=0.8/hostCount)
        # h10 = self.addHost('h10', ip='10.0.0.11', cpu=0.8/hostCount)
        # h11 = self.addHost('h11', ip='10.0.0.12', cpu=0.8/hostCount)
        # h12 = self.addHost('h12', ip='10.0.0.13', cpu=0.8/hostCount)
        # h13 = self.addHost('h13', ip='10.0.0.14', cpu=0.8/hostCount)
        h14 = self.addHost('h14', ip='10.0.0.15', cpu=0.8/hostCount)
        h15 = self.addHost('h15', ip='10.0.0.16', cpu=0.8/hostCount)
        h16 = self.addHost('h16', ip='10.0.0.17', cpu=0.8/hostCount)
        h17 = self.addHost('h17', ip='10.0.0.18', cpu=0.8/hostCount)
        # h18 = self.addHost('h18', ip='10.0.0.19', cpu=0.8/hostCount)
        # h19 = self.addHost('h19', ip='10.0.0.20', cpu=0.8/hostCount)
        # h20 = self.addHost('h20', ip='10.0.0.21', cpu=0.8/hostCount)
        # h21 = self.addHost('h21', ip='10.0.0.22', cpu=0.8/hostCount)



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
        linkopts1 = dict(delay='25ms', bw=10, loss=0, max_queue_size=1000, use_htb=True) # between switch and host
        linkopts2 = dict(delay='25ms', bw=10, loss=0, max_queue_size=1000, use_htb=True) # between 2 switches

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
        # self.addLink(s1, h1, **linkopts1)
        # self.addLink(s2, h2, **linkopts1)
        self.addLink(s3, h3, **linkopts1)
        # self.addLink(s4, h4, **linkopts1)
        # self.addLink(s5, h5, **linkopts1)
        # self.addLink(s6, h6, **linkopts1)
        # self.addLink(s7, h7, **linkopts1)
        self.addLink(s8, h8, **linkopts1)
        self.addLink(s9, h9, **linkopts1)
        # self.addLink(s10, h10, **linkopts1)
        # self.addLink(s11, h11, **linkopts1)
        # self.addLink(s12, h12, **linkopts1)
        # self.addLink(s13, h13, **linkopts1)

        #-------------------------------------
        self.addLink(s3, h14, **linkopts1)
        self.addLink(s3, h15, **linkopts1)
        self.addLink(s8, h16, **linkopts1)
        self.addLink(s8, h17, **linkopts1)
        # self.addLink(s3, h18, **linkopts1)
        # self.addLink(s3, h19, **linkopts1)
        # self.addLink(s8, h20, **linkopts1)
        # self.addLink(s8, h21, **linkopts1)
        

        

        
def startNetwork():
    global net
    net = Mininet(topo=NsfnetTopo(), link=TCLink, build=False, switch=OVSKernelSwitch, autoSetMacs=True, waitConnected=True)

    remote_ip = "127.0.0.1"
    info('** Adding Floodlight Controller\n')
    net.addController('c1', controller=RemoteController, host=CPULimitedHost, ip=remote_ip, port=6653, protocols="OpenFlow13")

    # Build the network
    net.build()
    net.start()
    time.sleep(2)
    net.pingAll()
    getPingStats("h0", "h9")
    getIperfTcpStats("h0", "h9")
    CLI(net)
    net.stop()

def getPingStats(sender: str, receiver: str) -> [float, float]:
    senderNode, receiverNode = net.getNodeByName(sender), net.getNodeByName(receiver)
    receiverIpv4 = receiverNode.IP()
    print("Receiver ipv4 -> ", receiverIpv4)
    command = f"ping {receiverIpv4} -c 1000 -f"
    print(command)
    result = senderNode.cmd(command)

    ping_parser = pingparsing.PingParsing()
    # print(json.dumps(ping_parser.parse(result).as_dict(), indent=4))
    result = ping_parser.parse(result).as_dict()
    packetLoss = result["packet_loss_rate"]
    avgRTT = result["rtt_avg"]
    print(f"""Average RTT: {avgRTT}\nPacket Loss: {packetLoss}""")
    return avgRTT, packetLoss

def getIperfTcpStats(server: str, client: str):
    server, client = net.getNodeByName(server), net.getNodeByName(client)
    serverCommand = "iperf3 -s -p 5555 -i 1 -1"
    clientCommand = f"iperf3 -c {server.IP()} -p 5555 -b 4M -R -t 5 -J"
    # thread1 = threading.Thread(target=hostCommand, args=(server, serverCommand,))
    # thread2 = threading.Thread(target=hostCommand, args=(client, clientCommand,))
    serverThread = HostCommand(server, serverCommand)
    clientThread = HostCommand(client, clientCommand) 

    serverThread.start()
    time.sleep(1)
    clientThread.start()

    serverThread.join()
    clientThread.join()

    print(json.loads(clientThread.result)["end"])

# def hostCommand(host: Host, command: str):
#     result = host.cmd(command)
#     return result
 
# custom thread
class HostCommand(Thread):
    def __init__(self, host: Host, command: str):
        Thread.__init__(self)
        self._host = host
        self._command = command
        self.result = None
    def run(self):
        self.result = self._host.cmd(self._command)

if __name__ == '__main__':
    setLogLevel('info')
    startNetwork()