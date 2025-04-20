from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.node import CPULimitedHost
from mininet.link import TCLink

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."

    def build(self, n=2):
        singleSwitch = self.addSwitch('s1')

        # n-> number of hosts"
        for h in range(n):
            # Each host gets 50%/n of system CPU
            host = self.addHost('h%s' % (h+1), cpu=0.5/n) # Example host names = h1, h2, h3 ...
            # 20 Mbps, 3ms delay, 1% loss, 1000 packet queue
            self.addLink(host, singleSwitch, bw=10, delay='5ms', loss=2, max_queue_size=1000, use_htb=True)

def run():
    "Create a newtork"
    topo = SingleSwitchTopo(n=4) # 4 hosts 1 switch

    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
    net.start()
    print("""
          INFO DUMPING
          ------------
          """)
    print(net.get('h1'))
    print("Dumping host connections")
    dumpNodeConnections(net.hosts) # dumps connections to/from a set of nodes.
    # Testing network
    net.pingAll()
    print( "Testing bandwidth between h1 and h4" )
    h1, h4 = net.get( 'h1', 'h4' )
    net.iperf( (h1, h4) ) # retrieves a node (host or switch) object by name
    CLI( net )
    net.stop()

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