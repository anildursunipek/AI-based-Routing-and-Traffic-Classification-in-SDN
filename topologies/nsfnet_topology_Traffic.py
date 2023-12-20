#!/usr/bin/python

import sys
sys.path.insert(0, "/home/anil/Desktop/sdn-based-device-management-application/python-api/controller")
from time import sleep
# from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch, CPULimitedHost, Host
from mininet.topo import Topo
from mininet.link import TCLink
import json
import pingparsing
import threading
from threading import Thread
import floodlightRestApi
import subprocess
from nfstream import NFStreamer

activeThreadList = {}
activeThreadCount = 0

class NsfnetTopo(Topo):
    """
    Topology Link: https://github.com/BNN-UPC/NetworkModelingDatasets/blob/master/assets/nsfnet_topology.png
    """
    def build( self, **params ):
        # Hosts
        hostCount = 8
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
    info('[INFO]****** Adding Floodlight Controller *****\n')
    net.addController('c1', controller=RemoteController, host=CPULimitedHost, ip=remote_ip, port=6653, protocols="OpenFlow13")

    # Build the network
    info('[INFO]****** Building Network *****\n')
    net.build()
    info('[INFO]****** Starting Network *****\n')
    net.start()
    sleep(2) # time.sleep

    # Configure controller
    info('[INFO]****** Configuring Controller *****\n')
    floodlightRestApi.setRoutingMetric("hopcount")
    floodlightRestApi.enableSwitchStats()

    info('[INFO]****** Testing Connectivity Between Hosts *****\n')
    net.pingAll()

    info('[INFO]****** Setting Path Between 2 Hosts *****\n')
    sourceNode, destNode = net.getNodeByName("h0"), net.getNodeByName("h9")
    src_host_mac = sourceNode.MAC()
    src_host_ipv4 = sourceNode.IP()
    dst_host_mac = destNode.MAC()
    dst_host_ipv4 = destNode.IP()
    num_paths = 3
    path_index = 0
    floodlightRestApi.pathPusher(src_host_mac, src_host_ipv4, dst_host_mac, dst_host_ipv4, num_paths, path_index)


    # Start traffic
    # 1 connection --> Low traffic
    # 2 connection --> Normal traffic
    # 3 connection --> High traffic

    info(f'[INFO]****** Active thread count: {threading.active_count()}\n')

    info('[INFO]****** Generating artificial traffic *****\n')

    # low traffic
    # generateTraffic(sender="h8", receiver="h3", getStats=False, bandWidth="5M")

    # normal traffic
    generateTraffic(sender="h8", receiver="h3", getStats=False, bandWidth="3050K")
    generateTraffic(sender="h16", receiver="h14", getStats=False, bandWidth="3050K")

    # high traffic
    # generateTraffic(sender="h8", receiver="h3", getStats=False, bandWidth="100M")
    # generateTraffic(sender="h16", receiver="h14", getStats=False, bandWidth="100M")
    # generateTraffic(sender="h17", receiver="h15", getStats=False, bandWidth="100M")

    
    sleep(15) # time.sleep
    info(f'[INFO]****** Active thread count: {threading.active_count()}\n')

    # Test the network
    info(f'[INFO]****** Testing The Network Performance *****\n')

    # Ping stats
    info(f'[INFO]****** Ping Stats *****\n')
    avgRTT, packetLoss = getPingStats("h0", "h9")
    print(f"""*** Average RTT: {avgRTT}\nPacket Loss: {packetLoss}""")

    # Iperf tcp stats
    info(f'[INFO]****** Iperf TCP Stats *****\n')
    iperfResult = generateTraffic(sender = "h9", receiver = "h0", getStats = True, bandWidth="0")
    print("*** Iperf TCP Result: ", iperfResult)

    # Start Video Stream
    info(f'[INFO]****** Video Stream Starting *****\n')
    startStream(sender = "h9", receiver = "h0")
    info(f'[INFO]****** Video Stream Ended *****\n')

    # Calculate PSNR and SSIM
    print(calculatePSNRAndSSIM())

    # CLI(net)
    info(f'[INFO]****** Active thread count: {threading.active_count()}\n')
    # for thread in activeThreadList.values():
    #     thread.join()
    
    info(f'[INFO]****** Mininet Cleaning *****\n')
    cleanMininet()
    sys.exit()
    # net.stop()

def cleanMininet():
    script_path = 'mininet.sh'
    subprocess.run(['bash', script_path])

def calculatePSNRAndSSIM():
    host = net.getNodeByName("h9") # random host
    command = "ffmpeg -i /home/anil/Desktop/test/1080p.ts -i records/input.ts -lavfi  'ssim;[0:v][1:v]psnr' -f null -"
    hostThread = HostCommand(host, command)
    hostThread.daemon = True
    hostThread.start()
    hostThread.join()
    psnr_and_ssım = hostThread.result
    psnr_and_ssım = psnr_and_ssım.split("\n")
    psnr_and_ssım = psnr_and_ssım[-3:]
    return psnr_and_ssım

def startStream(sender:str, receiver:str):
    senderNode, receiverNode = net.getNodeByName(sender), net.getNodeByName(receiver)
    port = "1234"
    videoSource = "/home/anil/Desktop/opp.ts"
    receiverUrl = f"udp://{receiverNode.IP()}:{port}"

    senderCommand = f"ffmpeg -re -i {videoSource} -c copy -f mpegts {receiverUrl}" # "ffmpeg -re -i /home/anil/Desktop/test/1080p.ts -c copy -f mpegts udp://10.0.0.1:1234
    # receiverCommand = f"ffplay -i {receiverUrl}"
    receiverCommand = f"ffmpeg -i {receiverUrl} -c copy records/input.ts"

    senderThread = HostCommand(senderNode, senderCommand)
    receiverThread = HostCommand(receiverNode, receiverCommand) 
    senderThread.daemon = True
    receiverThread.daemon = True

    receiverThread.start()
    sleep(1) # time.sleep
    senderThread.start()

    senderThread.join()
    sleep(5)
    info(f'[INFO]****** Ffmpeg Port Killing *****\n')
    killFfmpegPorts(senderNode)
    receiverThread.join()  
    senderThread.result

def killFfmpegPorts(senderNode):
    commandCheckPort = "pgrep -x ffmpeg"
    commandKillPort = "pkill -x ffmpeg"
    result = senderNode.cmd(commandCheckPort)
    while(result != ""):
        senderNode.cmd(commandKillPort)
        print("port öldürüldü")
        result = senderNode.cmd(commandCheckPort)

def getPingStats(sender: str, receiver: str) -> [float, float]:
    senderNode, receiverNode = net.getNodeByName(sender), net.getNodeByName(receiver)
    receiverIpv4 = receiverNode.IP()
    print("Receiver ipv4 -> ", receiverIpv4)
    packetCount = "500"
    command = f"ping {receiverIpv4} -c {packetCount} -f"
    print(command)
    result = senderNode.cmd(command)

    ping_parser = pingparsing.PingParsing()
    # print(json.dumps(ping_parser.parse(result).as_dict(), indent=4))
    result = ping_parser.parse(result).as_dict()
    packetLoss = result["packet_loss_rate"]
    avgRTT = result["rtt_avg"]
    # print(f"""Average RTT: {avgRTT}\nPacket Loss: {packetLoss}""")
    return avgRTT, packetLoss

def generateTraffic(sender: str, receiver: str, getStats: bool, bandWidth: str):
    global activeThreadCount
    global activeThreadList

    server, client = net.getNodeByName(sender), net.getNodeByName(receiver)
    port = "5555"
    bandWidth = bandWidth
    if getStats:
        time = "30"
    else:
        time = "350"

    serverCommand = f"iperf3 -s -p {port} -i 1 -1"
    clientCommand = f"iperf3 -c {server.IP()} -p {port} -b {bandWidth} -R -t {time} -J"

    serverThread = HostCommand(server, serverCommand)
    serverThread.daemon = True
    clientThread = HostCommand(client, clientCommand) 
    clientThread.daemon = True


    if getStats:
        streamListener = StreamListener("s0-eth4")
        streamListener.daemon = True
        streamListener.start()
    serverThread.start()
    sleep(1) # time.sleep
    clientThread.start()

    result = ""

    if getStats: 
        serverThread.join()
        clientThread.join()
        streamListener.flag = False
        streamListener.join()
        for stream in streamListener.stream:
            print(stream)
        result = json.loads(clientThread.result)["end"]
    
    return result

class HostCommand(Thread):
    def __init__(self, host: Host, command: str):
        Thread.__init__(self)
        self._host = host
        self._command = command
        self.result = None
    def run(self):
        self.result = self._host.cmd(self._command)

class StreamListener(Thread):
    def __init__(self, interface: str):
        Thread.__init__(self)
        self.interface = interface
        self.stream = []
        self.flag = True

    def run(self):
        flow_streamer = NFStreamer(source=self.interface,
                        statistical_analysis=True,
                        idle_timeout=30)
        self.stream = []
        for flow in flow_streamer:
            self.stream.append(flow)
            if(self.flag == False):
                break

if __name__ == '__main__':
    setLogLevel('info')
    startNetwork()