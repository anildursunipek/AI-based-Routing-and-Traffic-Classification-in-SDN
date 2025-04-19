import json
import requests

def flowPusher(flow:dict):
    """
    Example flow
    ------------
    flow_s0_s3 = {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow_s0_s3",
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": "10.0.0.1/32",
        "ipv4_dst": "10.0.0.10/32",
        "in_port":"3",
        "active":"true",
        "actions":"output=1"
    }
    """
    url_post = "http://127.0.0.1:8080/wm/staticentrypusher/json"

    post_response = requests.post(url_post, json=flow)

    post_response_json = post_response.json()
    print(post_response_json)

def getPaths(src_dpid:str, dst_dpid:str, num_paths:int):
    url = f"http://127.0.0.1:8080/wm/routing/paths/{src_dpid}/{dst_dpid}/{num_paths}/json"
    response = requests.get(url)
    response_json = response.json()
    print("[INFO]****** GET METHOD RESULT *****\n", response_json)
    return response_json

def getPathById(src_dpid:str, dst_dpid:str, num_paths:int, path_index:int) -> [dict, str, str]:
    url = f"http://127.0.0.1:8080/wm/routing/paths/slow/{src_dpid}/{dst_dpid}/{num_paths}/json"
    response = requests.get(url)
    response_json = response.json()
    #print("[INFO]****** GET METHOD RESULT *****\n", response_json["results"][path_index]["path"])
    path = response_json["results"][path_index]["path"]
    latency = response_json["results"][path_index]["latency"]
    hop_count = response_json["results"][path_index]["hop_count"]
    return path, latency, hop_count

def getDevices() -> dict:
    url = "http://127.0.0.1:8080/wm/device/"
    response = requests.get(url)
    response_json = response.json()
    print("[INFO]****** GET METHOD RESULT *****\n", response_json["devices"])
    return response_json["devices"]

def getDevicesByMac(mac: str) -> dict:
    url = "http://127.0.0.1:8080/wm/device/"
    response = requests.get(url)
    response_json = response.json()

    result = None
    for sub in response_json["devices"]:
        if sub["mac"] == [mac]:
            result = sub

    # print("[INFO]****** GET METHOD RESULT *****\n", result)
    return result

def getSwitchAndPortByHost(ipv4: str) -> [str, str]:
    """
        ipv4: host ipv4 address
    """
    url = "http://127.0.0.1:8080/wm/device/"
    response = requests.get(url)
    response_json = response.json()

    result = None
    for sub in response_json["devices"]:
        if sub["ipv4"] == [ipv4]:
            result = sub
    switch_dpid = result["attachmentPoint"][0]["switch"]
    port = result["attachmentPoint"][0]["port"]
    print("[INFO]****** GET METHOD RESULT *****\nSwitch Dpid: ", switch_dpid, "\nPort: ", port)
    return switch_dpid, port

def pathPusher(src_host_ipv4:str, dst_host_ipv4:str, num_paths:int, path_index:int):
    src_switch_dpid, src_switch_port = getSwitchAndPortByHost(src_host_ipv4)
    dst_switch_dpid, dst_switch_port = getSwitchAndPortByHost(dst_host_ipv4)
    flows = []

    path, latency, hop_count = getPathById(src_switch_dpid, dst_switch_dpid, num_paths, path_index)

    #print(f"Hop Count: {hop_count}\nLatency: {latency}\nPath: {path}")
    path.insert(0,{'dpid': src_switch_dpid, 'port': str(src_switch_port)})
    path.append({'dpid': dst_switch_dpid, 'port': str(dst_switch_port)})

    print(f"Hop Count: {hop_count}\nLatency: {latency}\nPath: {path}")

    for i in range(0,len(path), 2):
        switch_dpid = path[i]["dpid"]
        siwtch_input_port = path[i]["port"]
        siwtch_output_port = path[i+1]["port"]

        flow_first_direction_name = f"flow_{switch_dpid}_{siwtch_input_port}_1"
        flow_second_direction_name = f"flow_{switch_dpid}_{siwtch_output_port}_2"

        print("******** switch dpid: ", switch_dpid, " switch input port: ", siwtch_input_port, " switch output port: ", siwtch_output_port)
        
        first_direction = {
        "switch": switch_dpid,
        "name": flow_first_direction_name,
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": src_host_ipv4,
        "ipv4_dst": dst_host_ipv4,
        "in_port": siwtch_input_port,
        "active":"true",
        "actions": f"output={siwtch_output_port}"
        }

        second_direction = {
        "switch": switch_dpid,
        "name": flow_second_direction_name,
        "cookie": "0",
        "priority":"32768",
        "eth_type" : "0x0800" ,
        "ipv4_src": dst_host_ipv4,
        "ipv4_dst": src_host_ipv4,
        "in_port": siwtch_output_port,
        "active":"true",
        "actions": f"output={siwtch_input_port}"
        }
        
        flowPusher(first_direction)
        flowPusher(second_direction)

        flows.append(flow_first_direction_name)
        flows.append(flow_second_direction_name)

    return flows
def deleteAllFlows():
    url = f"http://127.0.0.1:8080/wm/staticentrypusher/clear/all/json"
    response = requests.get(url)
    response_json = response.json()
    print("[INFO]****** DELETING ALL FLOWS *****")
    print("[INFO]****** GET METHOD RESULT *****\n", response_json)
    return response_json

def deleteFlowByName(flowName: str):
    url = f"http://127.0.0.1:8080/wm/staticentrypusher/json"
    data = {"name":flowName}
    data = json.dumps(data)
    response = requests.delete(url = url, data = data) 
    response_json = response.json()
    print(f"[INFO]****** DELETED FLOW {flowName} *****")
    print("[INFO]****** DELETE METHOD RESULT *****\n", response_json)
    return response_json


def setRoutingMetric(metric:str):
    url_post = "http://127.0.0.1:8080/wm/routing/metric/json"
    json = {"metric" : metric}
    post_response = requests.post(url_post, json=json)
    post_response_json = post_response.json()
    print(post_response_json)

def enableSwitchStats():
    url_post = "http://127.0.0.1:8080/wm/statistics/config/enable/json"
    data = ''
    post_response = requests.post(url_post, data=data)
    post_response_json = post_response.json()
    print(post_response_json)

def getSwitchStatByPort(switch:str, port):
    port = str(port)
    url = f"http://127.0.0.1:8080/wm/statistics/bandwidth/{switch}/{port}/json"
    response = requests.get(url)
    response_json = response.json()
    return response_json

# Code example to show how to use floodlight rest api
if __name__ == "__main__":
    # getPathById Test Codes
    # src_dpid = "00:00:00:00:00:00:00:01"
    # dst_dpid = "00:00:00:00:00:00:00:10"
    # num_paths = 3
    # print(getPathById(src_dpid, dst_dpid, num_paths, 0))

    # getPaths("00:00:00:00:00:00:00:01", "00:00:00:00:00:00:00:10", 5)

    # getDevices Test Codes
    # getDevices()

    # getDeviceByHostIp Test Codes
    # getDevicesByMac("00:00:00:00:00:01")

    # getSwitchAndPortByHost Test Codes
    # getSwitchAndPortByHost("00:00:00:00:00:01")
    # getSwitchAndPortByHost("00:00:00:00:00:0a")

    # pathPusher Test Codes
    # pathPusher(src_host_mac="00:00:00:00:00:01", 
    #            src_host_ipv4= "10.0.0.1/32",
    #            dst_host_mac="00:00:00:00:00:04",
    #            dst_host_ipv4="10.0.0.10/32",
    #            num_paths = 3, 
    #            path_index = 0)

    # deleteAllFlows Test Codes
    # deleteAllFlows()

    print(getSwitchStatByPort("00:00:00:00:00:00:00:01", 4))