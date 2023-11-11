from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from model import Switch, Host
from datetime import datetime

global globalNet
global status
global startDate

class SingleSwitchTopo(Topo):
    def __init__(self, mySwitch:Switch, **opts):
        Topo.__init__(self, **opts)
        switch = self.addSwitch("s1", protocols='OpenFlow13')
        for h in range(len(mySwitch['host_connections'])):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch, bw=10)

def run(mySwitch2:Switch):
    global globalNet
    global status
    global startDate

    topo = SingleSwitchTopo(mySwitch=mySwitch2)

    net = Mininet(topo=topo, link=TCLink,autoStaticArp=True)

    net.start()
    globalNet = net
    status = True
    startDate = datetime.now()
    print(globalNet.hosts)

def stop():
    global globalNet
    global status

    globalNet = Mininet()
    status = False;
    globalNet.stop()

def getHostCount():
    global globalNet
    print(globalNet.hosts)
    return len(globalNet.hosts)


def getSwitchCount():
    global globalNet
    print(globalNet.hosts)
    return len(globalNet.switches)


def getLinkCount():
    global globalNet
    print(globalNet.hosts)
    return len(globalNet.links)

def getSystemStatus():
    global status
    return status

def getStartDate():
    global startDate
    return startDate

def startProject():
    global status
    status = False

def getHosts():
    global globalNet
    return globalNet.hosts

def getSwitchs():
    global globalNet
    return globalNet.switches

if __name__ == "__main__":
    setLogLevel("info")