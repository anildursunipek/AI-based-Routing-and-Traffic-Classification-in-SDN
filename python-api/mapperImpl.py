def toHost(host):
    return {
        'name': host.name,
        'IP': host.IP(),
        'MAC': host.MAC()
    }

def toSwitch(switch):
    return {
        'name': switch.name,
        'dpid': switch.dpid
    }