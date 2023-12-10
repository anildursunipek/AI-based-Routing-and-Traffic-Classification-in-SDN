from http.client import HTTPConnection
import json
 
class StaticEntryPusher(object):
 
    def __init__(self, server):
        self.server = server
 
    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
 
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
 
    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200
 
    def rest_call(self, data, action):
        path = '/wm/staticentrypusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print(ret)
        conn.close()
        return ret
 
pusher = StaticEntryPusher('127.0.0.1')
 
# flow_s0_s3 = {
#     "switch": "00:00:00:00:00:00:00:01",
#     "name": "flow_s0_s3",
#     "cookie": "0",
#     "priority":"32768",
#     "eth_type" : "0x0800" ,
#     "ipv4_dst": "10.0.0.10/24",
#     "in_port":"4",
#     "active":"true",
#     "actions":"output=3"
# }

# flow_s3_s4 = {
#     "switch": "00:00:00:00:00:00:00:04",
#     "name": "flow_s3_s4",
#     "cookie": "0",
#     "priority":"32768",
#     "eth_type" : "0x0800" ,
#     "ipv4_dst": "10.0.0.10/24",
#     "in_port":"1",
#     "active":"true",
#     "actions":"output=2"
# }

# flow_s4_s6 = {
#     "switch": "00:00:00:00:00:00:00:05",
#     "name": "flow_s4_s6",
#     "cookie": "0",
#     "priority":"32768",
#     "eth_type" : "0x0800" ,
#     "ipv4_dst": "10.0.0.10/24",
#     "in_port":"1",
#     "active":"true",
#     "actions":"output=3"
# }

# flow_s6_s7 = {
#     "switch": "00:00:00:00:00:00:00:07",
#     "name": "flow_s6_s7",
#     "cookie": "0",
#     "priority":"32768",
#     "eth_type" : "0x0800" ,
#     "ipv4_dst": "10.0.0.10/24",
#     "in_port":"1",
#     "active":"true",
#     "actions":"output=2"
# }

# flow_s7_s10 = {
#     "switch": "00:00:00:00:00:00:00:08",
#     "name": "flow_s6_s7",
#     "cookie": "0",
#     "priority":"32768",
#     "eth_type" : "0x0800" ,
#     "ipv4_dst": "10.0.0.10/24",
#     "in_port":"2",
#     "active":"true",
#     "actions":"output=3"
# }


# flow_s10_s9 = {
#     "switch": "00:00:00:00:00:00:00:11",
#     "name": "flow_s6_s7",
#     "cookie": "0",
#     "priority":"32768",
#     "eth_type" : "0x0800" ,
#     "ipv4_dst": "10.0.0.10/24",
#     "in_port":"1",
#     "active":"true",
#     "actions":"output=2"
# }

# flow_s9_h9 = {
#     "switch": "00:00:00:00:00:00:00:10",
#     "name": "flow_s6_s7",
#     "cookie": "0",
#     "priority":"32768",
#     "eth_type" : "0x0800" ,
#     "ipv4_dst": "10.0.0.10/24",
#     "in_port":"2",
#     "active":"true",
#     "actions":"output=4"
# }

flow_s0_s3 = {
    "switch": "00:00:00:00:00:00:00:01",
    "name": "flow_s0_s3",
    "cookie": "0",
    "priority":"32768",
    "in_port":"4",
    "active":"true",
    "actions":"output=3"
}

flow_s3_s4 = {
    "switch": "00:00:00:00:00:00:00:04",
    "name": "flow_s3_s4",
    "cookie": "0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "actions":"output=2"
}

flow_s4_s6 = {
    "switch": "00:00:00:00:00:00:00:05",
    "name": "flow_s4_s6",
    "cookie": "0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "actions":"output=3"
}

flow_s6_s7 = {
    "switch": "00:00:00:00:00:00:00:07",
    "name": "flow_s6_s7",
    "cookie": "0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "actions":"output=2"
}

flow_s7_s10 = {
    "switch": "00:00:00:00:00:00:00:08",
    "name": "flow_s6_s7",
    "cookie": "0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "actions":"output=3"
}


flow_s10_s9 = {
    "switch": "00:00:00:00:00:00:00:11",
    "name": "flow_s6_s7",
    "cookie": "0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "actions":"output=2"
}

flow_s9_h9 = {
    "switch": "00:00:00:00:00:00:00:10",
    "name": "flow_s6_s7",
    "cookie": "0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "actions":"output=4"
}

pusher.set(flow_s0_s3)
pusher.set(flow_s3_s4)
pusher.set(flow_s4_s6)
pusher.set(flow_s6_s7)
pusher.set(flow_s7_s10)
pusher.set(flow_s10_s9)
pusher.set(flow_s9_h9)


# flow1 = {
#     'switch':"00:00:00:00:00:00:00:01",
#     "name":"flow_mod_1",
#     "cookie":"0",
#     "priority":"32768",
#     "in_port":"1",
#     "active":"true",
#     "actions":"output=flood"
#     }
 
# flow2 = {
#     'switch':"00:00:00:00:00:00:00:01",
#     "name":"flow_mod_2",
#     "cookie":"0",
#     "priority":"32768",
#     "in_port":"2",
#     "active":"true",
#     "actions":"output=flood"
#     }
 
# pusher.set(flow1)
# pusher.set(flow2)