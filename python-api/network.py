from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.topo import LinearTopo, Topo
from mininet.node import RemoteController, CPULimitedHost
from mininet.link import TCLink
import random

#Global Veriables
global net
net:Mininet = None

class CustomTopo(Topo):
    def __init__(self, **params):
        Topo.__init__(self, **params)
        numberOfHostes = 33
        numberOfSwitches = 10

        #hosts = [ self.addHost('h%s' % h) for h in range(1,numberOfHostes + 1)]
        #switches = [ self.addSwitch('s%s' % s) for s in range(1,numberOfSwitches + 1)]

        #hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        h13 = self.addHost('h13')
        h14 = self.addHost('h14')
        h15 = self.addHost('h15')
        h16 = self.addHost('h16')
        h17 = self.addHost('h17')
        h18 = self.addHost('h18')
        h19 = self.addHost('h19')
        h20 = self.addHost('h20')
        h21 = self.addHost('h21')
        h22 = self.addHost('h22')
        h23 = self.addHost('h23')
        h24 = self.addHost('h24')
        h25 = self.addHost('h25')
        h26 = self.addHost('h26')
        h27 = self.addHost('h27')
        h28 = self.addHost('h28')
        h29 = self.addHost('h29')
        h30 = self.addHost('h30')
        h31 = self.addHost('h31')
        h32 = self.addHost('h32')
        h33 = self.addHost('h33')
        h34 = self.addHost('h34')

        #switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        # s9 = self.addSwitch('s9')
        # s10 = self.addSwitch('s10')

        #Links
        linkopts1	=	dict(bw=50,	delay='3ms', loss=1, max_queue_size=1000, use_htb=True)
        linkopts2	=	dict(bw=100, delay='2ms', loss=1, max_queue_size=1000, use_htb=True)
        linkopts3	=	dict(bw=30,	delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
        linkopts4	=	dict(bw=150, delay='1ms', loss=1, max_queue_size=1000, use_htb=True)
        linkopts5	=	dict(bw=250, delay='1ms', loss=1, max_queue_size=1000, use_htb=True)

        # swith to switch
        self.addLink(s1,s2)
        self.addLink(s1,s3)
        self.addLink(s1,s4)
        self.addLink(s1,s5)
        self.addLink(s2,s7)
        
        self.addLink(s7,s4)
        self.addLink(s4,s6)
        self.addLink(s6,s5)
        self.addLink(s5,s8)
        self.addLink(s8,s3)

        # swith to host
        self.addLink(s2, h1, **linkopts1)
        self.addLink(s2, h2, **linkopts2)
        self.addLink(s2, h3, **linkopts3)
        self.addLink(s2, h4, **linkopts4)
        self.addLink(s2, h5, **linkopts5)
        
        self.addLink(s7, h6, **linkopts1)
        self.addLink(s7, h7, **linkopts2)
        self.addLink(s7, h8, **linkopts3)
        self.addLink(s7, h9, **linkopts4)
        self.addLink(s7, h10, **linkopts5)
        
        self.addLink(s4, h11, **linkopts1)
        self.addLink(s4, h12, **linkopts2)
        self.addLink(s4, h13, **linkopts3)
        self.addLink(s4, h14, **linkopts4)
        self.addLink(s4, h15, **linkopts5)

        self.addLink(s6, h16, **linkopts1)
        self.addLink(s6, h17, **linkopts2)
        self.addLink(s6, h18, **linkopts3)
        self.addLink(s6, h19, **linkopts4)
        self.addLink(s6, h20, **linkopts5)

        self.addLink(s5, h21, **linkopts1)
        self.addLink(s5, h22, **linkopts2)
        self.addLink(s5, h23, **linkopts3)
        self.addLink(s5, h24, **linkopts4)
        self.addLink(s5, h25, **linkopts5)

        self.addLink(s8, h26, **linkopts1)
        self.addLink(s8, h27, **linkopts2)
        self.addLink(s8, h28, **linkopts3)
        self.addLink(s8, h29, **linkopts4)
        self.addLink(s8, h30, **linkopts5)

        self.addLink(s3, h31, **linkopts1)
        self.addLink(s3, h32, **linkopts2)
        self.addLink(s3, h33, **linkopts3)
        self.addLink(s3, h34, **linkopts4)

def buildCustomTopo():
    topo = CustomTopo()
    return topo

def buildLinearTopo(numberOfSwitches: int, hostsPerSwitch: int):
    topo = LinearTopo(numberOfSwitches, hostsPerSwitch)
    return topo


def initalizeTopology(topo):
    global net
    net = Mininet(topo=topo, build=False, host=CPULimitedHost, switch=OVSSwitch, link=TCLink,autoStaticArp=True)
    remoteControllerIp = "127.0.0.1"

    # Adding floodlight controller here
    net.addController("c1", controller=RemoteController,switch=OVSSwitch, ip=remoteControllerIp, port=6653)
    net.build()
    net.start()

def testTopology():
    global net
    h1 = net.get('h1')
    h16 = net.get('h16')
    result = net.iperf((h1, h16), l4Type='UDP')
    return result

def generateVirtualTraffic():
    global net
    hosts = net.hosts
    hostCount = len(hosts)
    print("Testing------>" , " hostCount: " , hostCount , " type: " , type(hostCount))
    # print(len(hosts))

    senders = random.sample(hosts, int(hostCount / 2))
    receivers = [host for host in hosts if host not in senders]
    # print(senders)
    # print(receivers)

    for i in range(int(hostCount / 2)):
        sender, receiver = senders[i], receivers[i]
        result = net.iperf((sender, receiver), l4Type='UDP')
        print("it worked")
        print(result)

def stopTopology():
    global net
    net.stop()
    net = None

def getHosts():
    global net
    return net.hosts

def getSwitches():
    global net
    return net.switches