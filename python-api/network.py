from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.topo import LinearTopo, Topo
from mininet.node import RemoteController
from mininet.link import TCLink

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
        h35 = self.addHost('h35')

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

        self.addLink(s2, h1)
        self.addLink(s2, h2)
        self.addLink(s2, h3)
        self.addLink(s2, h4)
        self.addLink(s2, h5)
        
        self.addLink(s7, h6)
        self.addLink(s7, h7)
        self.addLink(s7, h8)
        self.addLink(s7, h9)
        self.addLink(s7, h10)
        
        self.addLink(s4, h11)
        self.addLink(s4, h12)
        self.addLink(s4, h13)
        self.addLink(s4, h14)
        self.addLink(s4, h15)

        self.addLink(s6, h16)
        self.addLink(s6, h17)
        self.addLink(s6, h18)
        self.addLink(s6, h19)
        self.addLink(s6, h20)

        self.addLink(s5, h21)
        self.addLink(s5, h22)
        self.addLink(s5, h23)
        self.addLink(s5, h24)
        self.addLink(s5, h25)

        self.addLink(s8, h26)
        self.addLink(s8, h27)
        self.addLink(s8, h28)
        self.addLink(s8, h29)
        self.addLink(s8, h30)

        self.addLink(s3, h31)
        self.addLink(s3, h32)
        self.addLink(s3, h33)
        self.addLink(s3, h34)
        self.addLink(s3, h35)
def buildCustomTopo():
    topo = CustomTopo()
    return topo

def buildLinearTopo(numberOfSwitches: int, hostsPerSwitch: int):
    topo = LinearTopo(numberOfSwitches, hostsPerSwitch)
    return topo


def initalizeTopology(topo):
    global net
    net = Mininet(topo=topo, build=False, switch=OVSSwitch, link=TCLink,autoStaticArp=True)
    remoteControllerIp = "127.0.0.1"

    # Adding floodlight controller here
    net.addController("c1", controller=RemoteController,switch=OVSSwitch, ip=remoteControllerIp, port=6653)
    net.build()
    net.start()

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