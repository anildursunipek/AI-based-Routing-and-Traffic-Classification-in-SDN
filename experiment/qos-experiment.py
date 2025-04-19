#!/usr/bin/python

import sys
sys.path.insert(0, "/experiment/floodlightRestApi.py")
from time import sleep, perf_counter
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch, CPULimitedHost, Host
from mininet.topo import Topo
from mininet.link import TCLink
from mininet.cli import CLI
import json
import pingparsing
import threading
from threading import Thread
import floodlightRestApi
import subprocess
from nfstream import NFStreamer
import pandas as pd
import os
import numpy as np
import xgboost as xgb

class NsfnetTopo(Topo):
    """
    Topology Link: https://github.com/BNN-UPC/NetworkModelingDatasets/blob/master/assets/nsfnet_topology.png
    """
    def build( self, **params ):
        # Hosts
        hostCount = 20
        h0 = self.addHost('h0', ip='10.0.0.1', cpu=0.8/hostCount)
        h1 = self.addHost('h1', ip='10.0.0.2', cpu=0.8/hostCount)
        h2 = self.addHost('h2', ip='10.0.0.3', cpu=0.8/hostCount)
        h3 = self.addHost('h3', ip='10.0.0.4', cpu=0.8/hostCount)
        h4 = self.addHost('h4', ip='10.0.0.5', cpu=0.8/hostCount)
        h5 = self.addHost('h5', ip='10.0.0.6', cpu=0.8/hostCount)
        # h6 = self.addHost('h6', ip='10.0.0.7', cpu=0.8/hostCount)
        h7 = self.addHost('h7', ip='10.0.0.8', cpu=0.8/hostCount)
        h8 = self.addHost('h8', ip='10.0.0.9', cpu=0.8/hostCount)
        h9 = self.addHost('h9', ip='10.0.0.10', cpu=0.8/hostCount)
        h10 = self.addHost('h10', ip='10.0.0.11', cpu=0.8/hostCount)
        h11 = self.addHost('h11', ip='10.0.0.12', cpu=0.8/hostCount)
        # h12 = self.addHost('h12', ip='10.0.0.13', cpu=0.8/hostCount)
        # h13 = self.addHost('h13', ip='10.0.0.14', cpu=0.8/hostCount)
        h14 = self.addHost('h14', ip='10.0.0.15', cpu=0.8/hostCount)
        h15 = self.addHost('h15', ip='10.0.0.16', cpu=0.8/hostCount)
        h16 = self.addHost('h16', ip='10.0.0.17', cpu=0.8/hostCount)
        h17 = self.addHost('h17', ip='10.0.0.18', cpu=0.8/hostCount)
        h18 = self.addHost('h18', ip='10.0.0.19', cpu=0.8/hostCount)
        h19 = self.addHost('h19', ip='10.0.0.20', cpu=0.8/hostCount)
        h20 = self.addHost('h20', ip='10.0.0.21', cpu=0.8/hostCount)
        h21 = self.addHost('h21', ip='10.0.0.22', cpu=0.8/hostCount)
        h22 = self.addHost('h22', ip='10.0.0.23', cpu=0.8/hostCount)


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
        linkopts1 = dict(delay='25ms', bw=10, loss=0, max_queue_size=1000, use_htb=True, cls=TCLink) # between switch and host
        linkopts2 = dict(delay='25ms', bw=10, loss=0, max_queue_size=1000, use_htb=True, cls=TCLink) # between 2 switches

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
        # self.addLink(s6, h6, **linkopts1)
        self.addLink(s7, h7, **linkopts1)
        self.addLink(s8, h8, **linkopts1)
        self.addLink(s9, h9, **linkopts1)
        self.addLink(s10, h10, **linkopts1)
        self.addLink(s11, h11, **linkopts1)
        # self.addLink(s12, h12, **linkopts1)
        # self.addLink(s13, h13, **linkopts1)

        #-------------------------------------
        self.addLink(s3, h14, **linkopts1)
        self.addLink(s1, h15, **linkopts1)
        self.addLink(s8, h16, **linkopts1)
        self.addLink(s7, h17, **linkopts1)
        self.addLink(s11, h18, **linkopts1)
        self.addLink(s2, h19, **linkopts1)
        self.addLink(s10, h20, **linkopts1)
        self.addLink(s5, h21, **linkopts1)
        self.addLink(s3, h22, **linkopts1)
        
def startNetwork():
    start = perf_counter() # time.perf_counter()

    global net
    global activeThreadList
    global trafficTime
    trafficTime = 600
    activeThreadList = []
    net = None

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
    floodlightRestApi.setRoutingMetric("latency")
    # floodlightRestApi.enableSwitchStats()

    info('[INFO]****** Testing Connectivity Between Hosts *****\n')
    net.pingAll()


    info('[INFO]****** Setting Paths Among Hosts to Generate Traffic *****\n')
    setTrafficPaths()

    # Start traffic
    info(f'[INFO]****** Active thread count: {threading.active_count()}\n')
    info('[INFO]****** Generating artificial traffic *****\n')
    time_1 = perf_counter()
    print("Time Passed: ", time_1 - start)

    generateTraffic(sender="h8", receiver="h3", getStats=False, bandWidth="100M")
    generateTraffic(sender="h16", receiver="h14", getStats=False, bandWidth="100M")

    generateTraffic(sender="h7", receiver="h1", getStats=False, bandWidth="100M")
    generateTraffic(sender="h17", receiver="h15", getStats=False, bandWidth="100M")

    generateTraffic(sender="h10", receiver="h11", getStats=False, bandWidth="100M")
    generateTraffic(sender="h20", receiver="h18", getStats=False, bandWidth="100M")

    generateTraffic(sender="h5", receiver="h2", getStats=False, bandWidth="100M")
    generateTraffic(sender="h21", receiver="h19", getStats=False, bandWidth="100M")

    generateTraffic(sender="h4", receiver="h22", getStats=False, bandWidth="3M")


    sleep(13) # time.sleep
    info(f'[INFO]****** Active thread count: {threading.active_count()}\n')

    info(f'[INFO]****** Statistics Collecting *****\n')
    getPingStats("h0", "h9", getStats=True)
    getThroughput(sender = "h9", receiver = "h0", bandWidth="0")


    # Start Video Stream
    info(f'[INFO]****** Video Stream Starting *****\n')
    startStream(sender = "h9", receiver = "h0")
    info(f'[INFO]****** Video Stream Ended *****\n')
    info(f'[INFO]****** Active thread count: {threading.active_count()}\n')

    time_2 = perf_counter()
    print("Time passed: ", time_2 - start)


    info(f'[INFO]****** Active thread count: {threading.active_count()}\n')

    # info(f'[INFO]****** Video File Removing *****\n\n')
    # try:
    #     deleteFile("records/input.ts")
    # except Exception as e:
    #     print(f'Exception occurred: {e}')

    info(f'[INFO]****** Active thread count: {threading.active_count()}\n')

    for thread in activeThreadList:
        print(thread)
        print("Thread waiting...")
        while(thread.is_alive()):
            print("Thread waiting...")
            sleep(3)
        thread.join()
        print("Thread done...")

    info(f'[INFO]****** Mininet Cleaning *****\n')
    cleanMininet()
    sleep(5)

    end = perf_counter() # time.perf_counter()
    diff = end - start
    info(f'[INFO]****** Completed in {diff} seconds *****\n')
    # sys.exit()

def routingAlgorithm(src_ipv4, dst_ipv4):
    loaded_model = xgb.XGBClassifier()
    loaded_model.load_model('models/xgboost_binary_classification.json')
    paths = []

    for i in range(5):
        flows = floodlightRestApi.pathPusher(src_ipv4, dst_ipv4, num_paths=5, path_index=i)
        info(f'[INFO]****** Testing The Path {i} Performance *****\n')
        path_statistics = []
    
        info(f'[INFO]****** PATH = {i} Ping Stats *****\n')
        avgRTT, packetLoss = getPingStats("h0", "h9")
        path_statistics.append(avgRTT)
        path_statistics.append(packetLoss)
        print(f"""*** Average RTT: {avgRTT}\nPacket Loss: {packetLoss}""")

        # Iperf tcp stats
        info(f'[INFO]****** Path {i} Iperf TCP Stats *****\n')
        iperfResult = generateTraffic(sender = "h9", receiver = "h0", getStats = True, bandWidth="0")
        tcpFlowResult = iperfResult[0]

        path_statistics.append(tcpFlowResult["sum_received"]["bits_per_second"])
        path_statistics.append(100 - ((tcpFlowResult["sum_received"]["bits_per_second"] / 10000000) * 100))
        path_statistics.append(tcpFlowResult["sum_sent"]["retransmits"])
        path_statistics.append(tcpFlowResult["cpu_utilization_percent"]["host_total"])
        path_statistics.append(tcpFlowResult["cpu_utilization_percent"]["host_system"])

        nfstreamResult = iperfResult[1]
        path_statistics.append(nfstreamResult[0].bidirectional_duration_ms)
        path_statistics.append(nfstreamResult[0].src2dst_duration_ms)
        path_statistics.append(nfstreamResult[0].dst2src_duration_ms)
        path_statistics.append(nfstreamResult[0].bidirectional_mean_piat_ms)
        path_statistics.append(nfstreamResult[0].bidirectional_stddev_piat_ms)
        path_statistics.append(nfstreamResult[0].bidirectional_max_piat_ms)
        path_statistics.append(nfstreamResult[0].src2dst_mean_piat_ms)
        path_statistics.append(nfstreamResult[0].src2dst_stddev_piat_ms)
        path_statistics.append(nfstreamResult[0].src2dst_max_piat_ms)
        path_statistics.append(nfstreamResult[0].dst2src_mean_piat_ms)
        path_statistics.append(nfstreamResult[0].dst2src_stddev_piat_ms)
        path_statistics.append(nfstreamResult[0].dst2src_max_piat_ms)

        path_statistics = np.array([path_statistics])
        prediction = loaded_model.predict(path_statistics)
        print(f"Path {i} prediction ----> " , prediction)

        paths.append({
            'pathIndex': i,
            'pathTrafficValue': prediction
        })

        for flow in flows:
            floodlightRestApi.deleteFlowByName(flow)
        sleep(1)

    min = paths[0]
    for i in range(1, len(paths)):
        if(paths[i]['pathTrafficValue'] < min['pathTrafficValue']):
            min = paths[i]

    path_index = min['pathIndex']
    flows = floodlightRestApi.pathPusher(src_ipv4, dst_ipv4, num_paths=5, path_index=path_index)



def deleteFile(fileName: str):
    script_path = 'deleteFile.sh'
    subprocess.run(['bash', script_path, fileName])

def cleanMininet():
    script_path = 'mininet.sh'
    subprocess.run(['bash', script_path])

def calculatePSNR():
    host = net.getNodeByName("h9") # random host
    videoSource = "../assets/surreal.ts"
    outputSource = "records/input.ts"
    command = f"ffmpeg -i {videoSource} -i {outputSource} -lavfi '[0:v][1:v]psnr' -f null -"
    hostThread = HostCommand(host, command)
    hostThread.daemon = True
    hostThread.start()
    hostThread.join()
    psnrResult = hostThread.result
    psnrResult = float(psnrResult.split("\n")[-2].split("average:")[1].split(" ")[0].strip())
    return psnrResult

def calculateSSIM():
    host = net.getNodeByName("h9") # random host
    videoSource = "../assets/surreal.ts"
    outputSource = "records/input.ts"
    command = f"ffmpeg -i {videoSource} -i {outputSource} -lavfi '[0:v][1:v]ssim' -f null -"
    hostThread = HostCommand(host, command)
    hostThread.daemon = True
    hostThread.start()
    hostThread.join()
    ssimResult = hostThread.result.split("\n")[-2]
    firstReulst = float(ssimResult.split("All:")[1].split(" ")[0])
    secondResult = float(ssimResult.split("All:")[1].split(" ")[1].replace("(","").replace(")",""))
    return firstReulst, secondResult

def startStream(sender:str, receiver:str):
    senderNode, receiverNode = net.getNodeByName(sender), net.getNodeByName(receiver)
    port = "1234"
    videoSource = "../assets/surreal.ts"
    receiverUrl = f"udp://{receiverNode.IP()}:{port}"

    senderCommand = f"ffmpeg -re -i {videoSource} -c copy -f mpegts {receiverUrl}"
    receiverCommand = f"ffplay -i {receiverUrl}"
    #receiverCommand = f"ffmpeg -i {receiverUrl} -c copy records/input.ts"

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

def killFfmpegPorts(senderNode):
    commandCheckPort = "pgrep -x ffmpeg"
    commandKillPort = "pkill -x ffmpeg"
    result = senderNode.cmd(commandCheckPort)
    while(result != ""):
        senderNode.cmd(commandKillPort)
        print("Port Killed: ", result)
        result = senderNode.cmd(commandCheckPort)

def getPingStats(sender: str, receiver: str, getStats = False) -> [float, float]:
    senderNode, receiverNode = net.getNodeByName(sender), net.getNodeByName(receiver)
    receiverIpv4 = receiverNode.IP()
    print("Receiver ipv4 -> ", receiverIpv4)

    if getStats == True:
        packetCount = "60"
        command = f"ping {receiverIpv4} -c {packetCount} > output_qos_ping_v1.txt"
    else:
        packetCount = "500"
        command = f"ping {receiverIpv4} -c {packetCount} -f"

    result = senderNode.cmd(command)

    ping_parser = pingparsing.PingParsing()
    result = ping_parser.parse(result).as_dict()
    packetLoss = result["packet_loss_rate"]
    avgRTT = result["rtt_avg"]
    return avgRTT, packetLoss

def generateTraffic(sender: str, receiver: str, getStats: bool, bandWidth: str):
    global activeThreadList
    global trafficTime
    server, client = net.getNodeByName(sender), net.getNodeByName(receiver)
    port = "5555"
    if getStats:
        time = "30"
    else:
        time = str(trafficTime)

    serverCommand = f"iperf3 -s -p {port} -i 1 -1"
    clientCommand = f"iperf3 -c {server.IP()} -p {port} -b {bandWidth} -R -t {time} -J"

    serverThread = HostCommand(server, serverCommand)
    serverThread.daemon = True
    clientThread = HostCommand(client, clientCommand) 
    clientThread.daemon = True
    if getStats == False:
        activeThreadList.append(serverThread)
        activeThreadList.append(clientThread)

    streamListener = StreamListener("s0-eth4")
    streamListener.daemon = True
    if getStats:
        streamListener.start()
    sleep(1)
    serverThread.start()
    sleep(1) # time.sleep
    clientThread.start()

    
    if getStats: 
        serverThread.join()
        clientThread.join()
        streamListener.flag = False
        client.cmd(f"ping {server.IP()} -c 5 -f")
        streamListener.join()
        for stream in streamListener.stream:    
            print(stream)
        result = json.loads(clientThread.result)["end"]
        return result, streamListener.stream
    
def getThroughput(sender: str, receiver: str, bandWidth: str):
    server, client = net.getNodeByName(sender), net.getNodeByName(receiver)
    port = "5555"
    time = "60"

    serverCommand = f"iperf3 -s -p {port} -i 1 -1"
    clientCommand = f"iperf3 -c {server.IP()} -p {port} -b {bandWidth} -R -t {time} > output_qos_th_v1.txt"

    serverThread = HostCommand(server, serverCommand)
    serverThread.daemon = True
    clientThread = HostCommand(client, clientCommand) 
    clientThread.daemon = True

    sleep(1)
    serverThread.start()
    sleep(1) # time.sleep
    clientThread.start()

    serverThread.join()
    clientThread.join()

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
                        idle_timeout=15)
        self.stream = []
        for flow in flow_streamer:
            if(((flow.src_ip == "10.0.0.1" and flow.dst_ip == "10.0.0.10") or (flow.src_ip == "10.0.0.10" and flow.dst_ip == "10.0.0.1")) and 
                flow.application_name == "Unknown" and flow.application_category_name == "Unspecified"):
                self.stream.append(flow)
                print("FLOW ADDED")
                break
            if(self.flag == False):
                break

def setTrafficPaths():
    # H8 --> H3
    flow_h3_h8_1 = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_h3_h8_1",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.4/32",
        "ipv4_dst": "10.0.0.9/32",
        "in_port":"4",
        "active":"true",
        "actions":"output=3"
    }
    flow_h3_h8_1_r = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_h3_h8_1_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.9/32",
        "ipv4_dst": "10.0.0.4/32",
        "in_port":"3",
        "active":"true",
        "actions":"output=4"
    }
    floodlightRestApi.flowPusher(flow_h3_h8_1)
    floodlightRestApi.flowPusher(flow_h3_h8_1_r)
    #-------------------------------
    flow_h3_h8_2 = {
        "switch": "00:00:00:00:00:00:00:09",
        "name": "flow_h3_h8_2",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.4/32",
        "ipv4_dst": "10.0.0.9/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=4"
    }
    flow_h3_h8_2_r = {
        "switch": "00:00:00:00:00:00:00:09",
        "name": "flow_h3_h8_2_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.9/32",
        "ipv4_dst": "10.0.0.4/32",
        "in_port":"4",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_h3_h8_2)
    floodlightRestApi.flowPusher(flow_h3_h8_2_r)
    #-------------------------------
    #-------------------------------
    # H14 --> H16
    flow_h14_h16_1 = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_h14_h16_1",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.15/32",
        "ipv4_dst": "10.0.0.17/32",
        "in_port":"5",
        "active":"true",
        "actions":"output=3"
    }
    flow_h14_h16_1_r = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_h14_h16_1_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.17/32",
        "ipv4_dst": "10.0.0.15/32",
        "in_port":"3",
        "active":"true",
        "actions":"output=5"
    }    
    floodlightRestApi.flowPusher(flow_h14_h16_1)
    floodlightRestApi.flowPusher(flow_h14_h16_1_r)
    #-------------------------------
    flow_h14_h16_2 = {
        "switch": "00:00:00:00:00:00:00:09",
        "name": "flow_h14_h16_2",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.15/32",
        "ipv4_dst": "10.0.0.17/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=5"
    }
    flow_h14_h16_2_r = {
        "switch": "00:00:00:00:00:00:00:09",
        "name": "flow_h14_h16_2_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.17/32",
        "ipv4_dst": "10.0.0.15/32",
        "in_port":"5",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_h14_h16_2)
    floodlightRestApi.flowPusher(flow_h14_h16_2_r)
    #-------------------------------
    #-------------------------------
    # H1 --> H7
    flow_h1_h7_1 = {
        "switch": "00:00:00:00:00:00:00:02",
        "name": "flow_h1_h7_1",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.2/32",
        "ipv4_dst": "10.0.0.8/32",
        "in_port":"4",
        "active":"true",
        "actions":"output=2"
    }
    flow_h1_h7_1_r = {
        "switch": "00:00:00:00:00:00:00:02",
        "name": "flow_h1_h7_1_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.8/32",
        "ipv4_dst": "10.0.0.2/32",
        "in_port":"2",
        "active":"true",
        "actions":"output=4"
    }
    floodlightRestApi.flowPusher(flow_h1_h7_1)
    floodlightRestApi.flowPusher(flow_h1_h7_1_r)
    #-------------------------------
    flow_h1_h7_2 = {
        "switch": "00:00:00:00:00:00:00:08",
        "name": "flow_h1_h7_2",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.2/32",
        "ipv4_dst": "10.0.0.8/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=4"
    }
    flow_h1_h7_2_r = {
        "switch": "00:00:00:00:00:00:00:08",
        "name": "flow_h1_h7_2_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.8/32",
        "ipv4_dst": "10.0.0.2/32",
        "in_port":"4",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_h1_h7_2)
    floodlightRestApi.flowPusher(flow_h1_h7_2_r)
    #-------------------------------
    #-------------------------------
    # H17 --> H15
    flow_h15_h17_1 = {
        "switch": "00:00:00:00:00:00:00:02",
        "name": "flow_h15_h17_1",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.16/32",
        "ipv4_dst": "10.0.0.18/32",
        "in_port":"5",
        "active":"true",
        "actions":"output=2"
    }
    flow_h15_h17_1_r = {
        "switch": "00:00:00:00:00:00:00:02",
        "name": "flow_h15_h17_1_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.18/32",
        "ipv4_dst": "10.0.0.16/32",
        "in_port":"2",
        "active":"true",
        "actions":"output=5"
    }
    floodlightRestApi.flowPusher(flow_h15_h17_1)
    floodlightRestApi.flowPusher(flow_h15_h17_1_r)
    #-------------------------------
    flow_h15_h17_2 = {
        "switch": "00:00:00:00:00:00:00:08",
        "name": "flow_h15_h17_2",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.16/32",
        "ipv4_dst": "10.0.0.18/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=5"
    }
    flow_h15_h17_2_r = {
        "switch": "00:00:00:00:00:00:00:08",
        "name": "flow_h15_h17_2_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.18/32",
        "ipv4_dst": "10.0.0.16/32",
        "in_port":"5",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_h15_h17_2)
    floodlightRestApi.flowPusher(flow_h15_h17_2_r)
    #-------------------------------
    #-------------------------------
    # H11 --> H10
    flow_h11_h10_1 = {
        "switch": "00:00:00:00:00:00:00:12",
        "name": "flow_h11_h10_1",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.12/32",
        "ipv4_dst": "10.0.0.11/32",
        "in_port":"4",
        "active":"true",
        "actions":"output=2"
    }
    flow_h11_h10_1_r = {
        "switch": "00:00:00:00:00:00:00:12",
        "name": "flow_h11_h10_1_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.11/32",
        "ipv4_dst": "10.0.0.12/32",
        "in_port":"2",
        "active":"true",
        "actions":"output=4"
    }
    floodlightRestApi.flowPusher(flow_h11_h10_1)
    floodlightRestApi.flowPusher(flow_h11_h10_1_r)
    #-------------------------------
    flow_h11_h10_2 = {
        "switch": "00:00:00:00:00:00:00:11",
        "name": "flow_h11_h10_2",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.12/32",
        "ipv4_dst": "10.0.0.11/32",
        "in_port":"3",
        "active":"true",
        "actions":"output=5"
    }
    flow_h11_h10_2_r = {
        "switch": "00:00:00:00:00:00:00:11",
        "name": "flow_h11_h10_2_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.11/32",
        "ipv4_dst": "10.0.0.12/32",
        "in_port":"5",
        "active":"true",
        "actions":"output=3"
    }
    floodlightRestApi.flowPusher(flow_h11_h10_2)
    floodlightRestApi.flowPusher(flow_h11_h10_2_r)
    #-------------------------------
    #-------------------------------
    # H18 --> H20
    flow_h18_h20_1 = {
        "switch": "00:00:00:00:00:00:00:12",
        "name": "flow_h18_h20_1",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.19/32",
        "ipv4_dst": "10.0.0.21/32",
        "in_port":"5",
        "active":"true",
        "actions":"output=2"
    }
    flow_h18_h20_1_r = {
        "switch": "00:00:00:00:00:00:00:12",
        "name": "flow_h18_h20_1_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.21/32",
        "ipv4_dst": "10.0.0.19/32",
        "in_port":"2",
        "active":"true",
        "actions":"output=5"
    }
    floodlightRestApi.flowPusher(flow_h18_h20_1)
    floodlightRestApi.flowPusher(flow_h18_h20_1_r)
    #-------------------------------
    flow_h18_h20_2 = {
        "switch": "00:00:00:00:00:00:00:11",
        "name": "flow_h18_h20_2",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.19/32",
        "ipv4_dst": "10.0.0.21/32",
        "in_port":"3",
        "active":"true",
        "actions":"output=6"
    }
    flow_h18_h20_2_r = {
        "switch": "00:00:00:00:00:00:00:11",
        "name": "flow_h18_h20_2_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.21/32",
        "ipv4_dst": "10.0.0.19/32",
        "in_port":"6",
        "active":"true",
        "actions":"output=3"
    }
    floodlightRestApi.flowPusher(flow_h18_h20_2)
    floodlightRestApi.flowPusher(flow_h18_h20_2_r)
    #-------------------------------
    #-------------------------------
    # H2 --> H5
    flow_h2_h5_1 = {
        "switch": "00:00:00:00:00:00:00:03",
        "name": "flow_h2_h5_1",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.03/32",
        "ipv4_dst": "10.0.0.06/32",
        "in_port":"4",
        "active":"true",
        "actions":"output=3"
    }
    flow_h2_h5_1_r = {
        "switch": "00:00:00:00:00:00:00:03",
        "name": "flow_h2_h5_1_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.06/32",
        "ipv4_dst": "10.0.0.03/32",
        "in_port":"3",
        "active":"true",
        "actions":"output=4"
    }
    floodlightRestApi.flowPusher(flow_h2_h5_1)
    floodlightRestApi.flowPusher(flow_h2_h5_1_r)
    #-------------------------------
    flow_h2_h5_2 = {
        "switch": "00:00:00:00:00:00:00:06",
        "name": "flow_h2_h5_2",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.03/32",
        "ipv4_dst": "10.0.0.06/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=5"
    }
    flow_h2_h5_2_r = {
        "switch": "00:00:00:00:00:00:00:06",
        "name": "flow_h2_h5_2_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.06/32",
        "ipv4_dst": "10.0.0.03/32",
        "in_port":"5",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_h2_h5_2)
    floodlightRestApi.flowPusher(flow_h2_h5_2_r)
    #-------------------------------
    #-------------------------------
   # H19 --> H21
    flow_h19_h21_1 = {
        "switch": "00:00:00:00:00:00:00:03",
        "name": "flow_h19_h21_1",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.20/32",
        "ipv4_dst": "10.0.0.22/32",
        "in_port":"5",
        "active":"true",
        "actions":"output=3"
    }
    flow_h19_h21_1_r = {
        "switch": "00:00:00:00:00:00:00:03",
        "name": "flow_h19_h21_1_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.22/32",
        "ipv4_dst": "10.0.0.20/32",
        "in_port":"3",
        "active":"true",
        "actions":"output=5"
    }
    floodlightRestApi.flowPusher(flow_h19_h21_1)
    floodlightRestApi.flowPusher(flow_h19_h21_1_r)
    #-------------------------------
    flow_h19_h21_2 = {
        "switch": "00:00:00:00:00:00:00:06",
        "name": "flow_h19_h21_2",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.20/32",
        "ipv4_dst": "10.0.0.22/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=6"
    }
    flow_h19_h21_2_r = {
        "switch": "00:00:00:00:00:00:00:06",
        "name": "flow_h19_h21_2_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.22/32",
        "ipv4_dst": "10.0.0.20/32",
        "in_port":"6",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_h19_h21_2)
    floodlightRestApi.flowPusher(flow_h19_h21_2_r)
    #-------------------------------
    #-------------------------------
    # H22 --> H4
    flow_h22_h4_1 = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_h22_h4_1",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.23/32",
        "ipv4_dst": "10.0.0.05/32",
        "in_port":"6",
        "active":"true",
        "actions":"output=2"
    }
    flow_h22_h4_1_r = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_h22_h4_1_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.05/32",
        "ipv4_dst": "10.0.0.23/32",
        "in_port":"2",
        "active":"true",
        "actions":"output=6"
    }
    floodlightRestApi.flowPusher(flow_h22_h4_1)
    floodlightRestApi.flowPusher(flow_h22_h4_1_r)
    #-------------------------------
    flow_h22_h4_2 = {
        "switch": "00:00:00:00:00:00:00:05",
        "name": "flow_h22_h4_2",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.23/32",
        "ipv4_dst": "10.0.0.05/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=4"
    }
    flow_h22_h4_2_r = {
        "switch": "00:00:00:00:00:00:00:05",
        "name": "flow_h22_h4_2_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.05/32",
        "ipv4_dst": "10.0.0.23/32",
        "in_port":"4",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_h22_h4_2)
    floodlightRestApi.flowPusher(flow_h22_h4_2_r)
    #-------------------------------
    #-------------------------------
    
if __name__ == '__main__':
    setLogLevel('info')
    startNetwork()
