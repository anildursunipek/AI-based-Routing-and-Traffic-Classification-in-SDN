from mininet.topo import Topo

class BasicCustomTopo(Topo):
    def build(self):
        "Custom topo created here."

        "Add Hosts"
        h0_0 = self.addHost('h0_0')
        h0_1 = self.addHost('h0_1')
        h0_2 = self.addHost('h0_2')
        h1_0 = self.addHost('h1_0')
        h1_1 = self.addHost('h1_1')
        h1_2 = self.addHost('h1_2')

        "Add Switches"
        s0 = self.addSwitch('s1')
        s1 = self.addSwitch('s2')

        "Add links"
        self.addLink(h0_0, s0)
        self.addLink(h0_1, s0)
        self.addLink(h0_2, s0)
        self.addLink(h1_0, s1)
        self.addLink(h1_1, s1)
        self.addLink(h1_2, s1)
        self.addLink(s0,s1)

"""
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
To test custom topology command line code: 
sudo mn --custom topologies/basicTopo.py --topo basicCustomTopo --test pingall
"""
topos = {'basicCustomTopo' : (lambda: BasicCustomTopo())}


