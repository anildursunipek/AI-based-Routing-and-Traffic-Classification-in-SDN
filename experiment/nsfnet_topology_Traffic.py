#!/usr/bin/python

import sys
sys.path.insert(0, "../python-api/controller")
from time import sleep, perf_counter
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
import pandas as pd

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
        h18 = self.addHost('h18', ip='10.0.0.19', cpu=0.8/hostCount)
        h19 = self.addHost('h19', ip='10.0.0.20', cpu=0.8/hostCount)
        h20 = self.addHost('h20', ip='10.0.0.21', cpu=0.8/hostCount)
        h21 = self.addHost('h21', ip='10.0.0.22', cpu=0.8/hostCount)

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
        self.addLink(s3, h18, **linkopts1)
        self.addLink(s3, h19, **linkopts1)
        self.addLink(s8, h20, **linkopts1)
        self.addLink(s8, h21, **linkopts1)
        
def startNetwork():
    start = perf_counter() # time.perf_counter()
    dataFrame = pd.read_csv('data.csv')
    dataRow = {}

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
    # floodlightRestApi.enableSwitchStats()

    info('[INFO]****** Testing Connectivity Between Hosts *****\n')
    net.pingAll()
    print(net.links)
    # switch = net.getNodeByName("s0")

    info('[INFO]****** Setting Path Between 2 Hosts *****\n')
    scenerio_1()

    # Start traffic
    info(f'[INFO]****** Active thread count: {threading.active_count()}\n')
    info('[INFO]****** Generating artificial traffic *****\n')

    # low traffic
    # generateTraffic(sender="h16", receiver="h14", getStats=False, bandWidth="1000K")
    # traffic_type = 1

    # normal traffic
    generateTraffic(sender="h8", receiver="h3", getStats=False, bandWidth="2525K")
    generateTraffic(sender="h16", receiver="h14", getStats=False, bandWidth="2525K")
    traffic_type = 2

    # # high traffic
    # generateTraffic(sender="h8", receiver="h3", getStats=False, bandWidth="100M")
    # generateTraffic(sender="h16", receiver="h14", getStats=False, bandWidth="100M")
    # generateTraffic(sender="h17", receiver="h15", getStats=False, bandWidth="100M")
    # generateTraffic(sender="h20", receiver="h18", getStats=False, bandWidth="100M")
    # generateTraffic(sender="h21", receiver="h19", getStats=False, bandWidth="100M")
    # traffic_type = 3

    sleep(13) # time.sleep
    info(f'[INFO]****** Active thread count: {threading.active_count()}\n')

    # Test the network
    info(f'[INFO]****** Testing The Network Performance *****\n')

    # Ping stats
    info(f'[INFO]****** Ping Stats *****\n')
    avgRTT, packetLoss = getPingStats("h0", "h9")
    dataRow['average_rtt'] = avgRTT
    dataRow['packet_loss'] = packetLoss
    print(f"""*** Average RTT: {avgRTT}\nPacket Loss: {packetLoss}""")

    # Iperf tcp stats
    info(f'[INFO]****** Iperf TCP Stats *****\n')
    iperfResult = generateTraffic(sender = "h9", receiver = "h0", getStats = True, bandWidth="0")
    tcpFlowResult = iperfResult[0]
    dataRow['bits_per_second'] = tcpFlowResult["sum_received"]["bits_per_second"]
    dataRow['bu_ratio'] = 100 - ((tcpFlowResult["sum_received"]["bits_per_second"] / 10000000) * 100)
    dataRow['retransmits'] = tcpFlowResult["sum_sent"]["retransmits"]
    dataRow['cpu_host_total'] = tcpFlowResult["cpu_utilization_percent"]["host_total"]
    dataRow['cpu_host_user'] = tcpFlowResult["cpu_utilization_percent"]["host_user"]
    dataRow['cpu_host_system'] = tcpFlowResult["cpu_utilization_percent"]["host_system"]
    dataRow['cpu_remote_total'] = tcpFlowResult["cpu_utilization_percent"]["remote_total"]
    dataRow['cpu_remote_user'] = tcpFlowResult["cpu_utilization_percent"]["remote_user"]
    dataRow['cpu_remote_system'] = tcpFlowResult["cpu_utilization_percent"]["remote_system"]
    print("*** Iperf TCP Result: ", tcpFlowResult)

    nfstreamResult = iperfResult[1]
    dataRow['bidirectional_duration_ms'] = nfstreamResult[0].bidirectional_duration_ms
    dataRow['bidirectional_packets'] = nfstreamResult[0].bidirectional_packets
    dataRow['bidirectional_bytes'] = nfstreamResult[0].bidirectional_bytes
    dataRow['src2dst_duration_ms'] = nfstreamResult[0].src2dst_duration_ms
    dataRow['src2dst_packets'] = nfstreamResult[0].src2dst_packets
    dataRow['src2dst_bytes'] = nfstreamResult[0].src2dst_bytes
    dataRow['dst2src_duration_ms'] = nfstreamResult[0].dst2src_duration_ms
    dataRow['dst2src_packets'] = nfstreamResult[0].dst2src_packets
    dataRow['dst2src_bytes'] = nfstreamResult[0].dst2src_bytes
    dataRow['bidirectional_min_ps'] = nfstreamResult[0].bidirectional_min_ps
    dataRow['bidirectional_mean_ps'] = nfstreamResult[0].bidirectional_mean_ps
    dataRow['bidirectional_stddev_ps'] = nfstreamResult[0].bidirectional_stddev_ps
    dataRow['bidirectional_max_ps'] = nfstreamResult[0].bidirectional_max_ps
    dataRow['src2dst_min_ps'] = nfstreamResult[0].src2dst_min_ps
    dataRow['src2dst_mean_ps'] = nfstreamResult[0].src2dst_mean_ps
    dataRow['src2dst_stddev_ps'] = nfstreamResult[0].src2dst_stddev_ps
    dataRow['src2dst_max_ps'] = nfstreamResult[0].src2dst_max_ps
    dataRow['dst2src_min_ps'] = nfstreamResult[0].dst2src_min_ps
    dataRow['dst2src_mean_ps'] = nfstreamResult[0].dst2src_mean_ps
    dataRow['dst2src_stddev_ps'] = nfstreamResult[0].dst2src_stddev_ps
    dataRow['dst2src_max_ps'] = nfstreamResult[0].dst2src_max_ps
    dataRow['bidirectional_min_piat_ms'] = nfstreamResult[0].bidirectional_min_piat_ms
    dataRow['bidirectional_mean_piat_ms'] = nfstreamResult[0].bidirectional_mean_piat_ms
    dataRow['bidirectional_stddev_piat_ms'] = nfstreamResult[0].bidirectional_stddev_piat_ms
    dataRow['bidirectional_max_piat_ms'] = nfstreamResult[0].bidirectional_max_piat_ms
    dataRow['src2dst_min_piat_ms'] = nfstreamResult[0].src2dst_min_piat_ms
    dataRow['src2dst_mean_piat_ms'] = nfstreamResult[0].src2dst_mean_piat_ms
    dataRow['src2dst_stddev_piat_ms'] = nfstreamResult[0].src2dst_stddev_piat_ms
    dataRow['src2dst_max_piat_ms'] = nfstreamResult[0].src2dst_max_piat_ms
    dataRow['dst2src_min_piat_ms'] = nfstreamResult[0].dst2src_min_piat_ms
    dataRow['dst2src_mean_piat_ms'] = nfstreamResult[0].dst2src_mean_piat_ms
    dataRow['dst2src_stddev_piat_ms'] = nfstreamResult[0].dst2src_stddev_piat_ms
    dataRow['dst2src_max_piat_ms'] = nfstreamResult[0].dst2src_max_piat_ms

    # cleanMininet()
    # sys.exit()

    # Start Video Stream
    info(f'[INFO]****** Video Stream Starting *****\n')
    startStream(sender = "h9", receiver = "h0")
    info(f'[INFO]****** Video Stream Ended *****\n')

    # Calculate PSNR and SSIM
    info(f'[INFO]****** Calculating PSNR Value *****\n')
    psnr = calculatePSNR()
    print("PSNR: " , psnr)
    dataRow['psnr'] = psnr

    info(f'[INFO]****** Calculating SSIM Value *****\n')
    ssimResult_first, ssimResult_second = calculateSSIM()
    dataRow['ssim_first_value'] = ssimResult_first
    dataRow['ssim_second_value'] = ssimResult_second
    print("SSIM: ", ssimResult_first, " || ", ssimResult_second)

    info(f'[INFO]****** Active thread count: {threading.active_count()}\n')
    info(f'[INFO]****** Mininet Cleaning *****\n')
    cleanMininet()
    sleep(3)

    info(f'[INFO]****** Video File Removing *****\n\n')
    try:
        deleteFile("records/input.ts")
    except Exception as e:
        print(f'Exception occurred: {e}')

    dataRow['traffic_type'] = traffic_type
    print("dataRow:")
    print(dataRow)
    df_dictionary = pd.DataFrame([dataRow])
    dataFrame = pd.concat([dataFrame, df_dictionary], ignore_index=True)
    dataFrame.to_csv("data.csv", sep=',', index=False, encoding='utf-8')

    end = perf_counter() # time.perf_counter()
    diff = end - start
    info(f'[INFO]****** Completed in {diff} seconds *****\n')
    info(f'[INFO]****** Active thread count: {threading.active_count()}\n')
    sys.exit()

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

def killFfmpegPorts(senderNode):
    commandCheckPort = "pgrep -x ffmpeg"
    commandKillPort = "pkill -x ffmpeg"
    result = senderNode.cmd(commandCheckPort)
    while(result != ""):
        senderNode.cmd(commandKillPort)
        print("Port Killed: ", result)
        result = senderNode.cmd(commandCheckPort)

def getPingStats(sender: str, receiver: str) -> [float, float]:
    senderNode, receiverNode = net.getNodeByName(sender), net.getNodeByName(receiver)
    receiverIpv4 = receiverNode.IP()
    print("Receiver ipv4 -> ", receiverIpv4)
    packetCount = "500"
    command = f"ping {receiverIpv4} -c {packetCount} -f"
    result = senderNode.cmd(command)

    ping_parser = pingparsing.PingParsing()
    result = ping_parser.parse(result).as_dict()
    packetLoss = result["packet_loss_rate"]
    avgRTT = result["rtt_avg"]
    return avgRTT, packetLoss

def generateTraffic(sender: str, receiver: str, getStats: bool, bandWidth: str):
    server, client = net.getNodeByName(sender), net.getNodeByName(receiver)
    port = "5555"
    if getStats:
        time = "30"
    else:
        time = "250"

    serverCommand = f"iperf3 -s -p {port} -i 1 -1"
    clientCommand = f"iperf3 -c {server.IP()} -p {port} -b {bandWidth} -R -t {time} -J"

    serverThread = HostCommand(server, serverCommand)
    serverThread.daemon = True
    clientThread = HostCommand(client, clientCommand) 
    clientThread.daemon = True

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
        streamListener.join()
        for stream in streamListener.stream:
            print(stream)
        result = json.loads(clientThread.result)["end"]
        return result, streamListener.stream

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
            if(self.flag == False):
                break

def scenerio_1():
    # MAIN PATH
    flow_s0_s3 = {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow_s0_s3",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.1/32",
        "ipv4_dst": "10.0.0.10/32",
        "in_port":"4",
        "active":"true",
        "actions":"output=3"
    }
    flow_s0_s3_r = {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow_s0_s3_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.10/32",
        "ipv4_dst": "10.0.0.1/32",
        "in_port":"3",
        "active":"true",
        "actions":"output=4"
    }
    floodlightRestApi.flowPusher(flow_s0_s3)
    floodlightRestApi.flowPusher(flow_s0_s3_r)
    #--------------------------------
    flow_s3_s8 = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_s3_s8",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.1/32",
        "ipv4_dst": "10.0.0.10/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=3"
    }
    flow_s3_s8_r = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_s3_s8_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.10/32",
        "ipv4_dst": "10.0.0.1/32",
        "in_port":"3",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_s3_s8)
    floodlightRestApi.flowPusher(flow_s3_s8_r)
    #---------------------------------------
    flow_s8_s9 = {
        "switch": "00:00:00:00:00:00:00:09",
        "name": "flow_s8_s9",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.1/32",
        "ipv4_dst": "10.0.0.10/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=2"
    }
    flow_s8_s9_r = {
        "switch": "00:00:00:00:00:00:00:09",
        "name": "flow_s8_s9_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.10/32",
        "ipv4_dst": "10.0.0.1/32",
        "in_port":"2",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_s8_s9)
    floodlightRestApi.flowPusher(flow_s8_s9_r)
    #-------------------------------
    flow_s9_h9 = {
        "switch": "00:00:00:00:00:00:00:10",
        "name": "flow_s9_h9",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.1/32",
        "ipv4_dst": "10.0.0.10/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=4"
    }
    flow_s9_h9_r = {
        "switch": "00:00:00:00:00:00:00:10",
        "name": "flow_s9_h9_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.10/32",
        "ipv4_dst": "10.0.0.1/32",
        "in_port":"4",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_s9_h9)
    floodlightRestApi.flowPusher(flow_s9_h9_r)

    # TRAFFIC PATHS
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
    flow_h15_h17_1 = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_h15_h17_1",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.16/32",
        "ipv4_dst": "10.0.0.18/32",
        "in_port":"6",
        "active":"true",
        "actions":"output=3"
    }
    flow_h15_h17_1_r = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_h15_h17_1_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.18/32",
        "ipv4_dst": "10.0.0.16/32",
        "in_port":"3",
        "active":"true",
        "actions":"output=6"
    }    
    floodlightRestApi.flowPusher(flow_h15_h17_1)
    floodlightRestApi.flowPusher(flow_h15_h17_1_r)
    #-------------------------------
    flow_h15_h17_2 = {
        "switch": "00:00:00:00:00:00:00:09",
        "name": "flow_h15_h17_2",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.16/32",
        "ipv4_dst": "10.0.0.18/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=6"
    }
    flow_h15_h17_2_r = {
        "switch": "00:00:00:00:00:00:00:09",
        "name": "flow_h15_h17_2_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.18/32",
        "ipv4_dst": "10.0.0.16/32",
        "in_port":"6",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_h15_h17_2)
    floodlightRestApi.flowPusher(flow_h15_h17_2_r)
    #-------------------------------
    #-------------------------------
    flow_h18_h20_1 = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_h18_h20_1",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.19/32",
        "ipv4_dst": "10.0.0.21/32",
        "in_port":"7",
        "active":"true",
        "actions":"output=3"
    }
    flow_h18_h20_1_r = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_h18_h20_1_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.21/32",
        "ipv4_dst": "10.0.0.19/32",
        "in_port":"3",
        "active":"true",
        "actions":"output=7"
    }    
    floodlightRestApi.flowPusher(flow_h18_h20_1)
    floodlightRestApi.flowPusher(flow_h18_h20_1_r)
    #-------------------------------
    flow_h18_h20_2 = {
        "switch": "00:00:00:00:00:00:00:09",
        "name": "flow_h18_h20_2",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.19/32",
        "ipv4_dst": "10.0.0.21/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=7"
    }
    flow_h18_h20_2_r = {
        "switch": "00:00:00:00:00:00:00:09",
        "name": "flow_h18_h20_2_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.21/32",
        "ipv4_dst": "10.0.0.19/32",
        "in_port":"7",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_h18_h20_2)
    floodlightRestApi.flowPusher(flow_h18_h20_2_r)
    #-------------------------------
    #-------------------------------
    flow_h19_h21_1 = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_h19_h21_1",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.20/32",
        "ipv4_dst": "10.0.0.22/32",
        "in_port":"8",
        "active":"true",
        "actions":"output=3"
    }
    flow_h19_h21_1_r = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow_h19_h21_1_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.22/32",
        "ipv4_dst": "10.0.0.20/32",
        "in_port":"3",
        "active":"true",
        "actions":"output=8"
    }    
    floodlightRestApi.flowPusher(flow_h19_h21_1)
    floodlightRestApi.flowPusher(flow_h19_h21_1_r)
    #-------------------------------
    flow_h19_h21_2 = {
        "switch": "00:00:00:00:00:00:00:09",
        "name": "flow_h19_h21_2",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.20/32",
        "ipv4_dst": "10.0.0.22/32",
        "in_port":"1",
        "active":"true",
        "actions":"output=8"
    }
    flow_h19_h21_2_r = {
        "switch": "00:00:00:00:00:00:00:09",
        "name": "flow_h19_h21_2_r",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.22/32",
        "ipv4_dst": "10.0.0.20/32",
        "in_port":"8",
        "active":"true",
        "actions":"output=1"
    }
    floodlightRestApi.flowPusher(flow_h19_h21_2)
    floodlightRestApi.flowPusher(flow_h19_h21_2_r)
    


    
if __name__ == '__main__':
    setLogLevel('info')
    startNetwork()