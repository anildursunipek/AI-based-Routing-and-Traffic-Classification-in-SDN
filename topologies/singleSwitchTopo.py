from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."

    def build(self, n=2):
        singleSwitch = self.addSwitch('s1')

        # n-> number of hosts"
        for h in range(n):
            host = self.addHost('h%s' % (h+1)) # Example host names = h1, h2, h3 ...
            self.addLink(host,singleSwitch)

def run():
    "Create a newtork"
    topo = SingleSwitchTopo(n=4) # 4 hosts 1 switch
    net = Mininet(topo=topo)
    net.start()
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    # Testing network
    net.pingAll()
    net.stop

if __name__ == "__main__":
    setLogLevel("info") # Tell mininet to print useful information
    run()
    """
    Output
    ------
    *** Creating network
    *** Adding controller
    *** Adding hosts:
    h1 h2 h3 h4 
    *** Adding switches:
    s1 
    *** Adding links:
    (h1, s1) (h2, s1) (h3, s1) (h4, s1) 
    *** Configuring hosts
    h1 h2 h3 h4 
    *** Starting controller
    c0 
    *** Starting 1 switches
    s1 ...
    Dumping host connections
    h1 h1-eth0:s1-eth1
    h2 h2-eth0:s1-eth2
    h3 h3-eth0:s1-eth3
    h4 h4-eth0:s1-eth4
    *** Ping: testing ping reachability
    h1 -> h2 h3 h4 
    h2 -> h1 h3 h4 
    h3 -> h1 h2 h4 
    h4 -> h1 h2 h3 
    *** Results: 0% dropped (12/12 received)
    """
