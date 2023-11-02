class Host:
    def __init__(self, name, IP, MAC):
        self.name = name
        self.IP = IP
        self.MAC = MAC

    def to_dict(self):
        return {
            'name': self.name,
            'IP': self.IP,
            'MAC': self.MAC
        }

class Switch:
    name:str
    dpid:str
    ports:str
    host_connections:list