import api_methods

src_dpid = "00:00:00:00:00:00:00:01"
dst_dpid = "00:00:00:00:00:00:00:10"
num_paths = 3

possible_routes = api_methods.getPaths(src_dpid, dst_dpid, num_paths)
print(possible_routes)

# Print the result
# print(response_json)
# for index in range(len(response_json["results"])):
#     hop_count = response_json["results"][index]["hop_count"]
#     latency = response_json["results"][index]["latency"]
#     path = response_json["results"][index]["path"]
#     print("Hop Count: ", hop_count)
#     print("Latency: ", latency)

#     first_switch_dpid = path[0]["dpid"]
#     first_switch_port = path[0]["port"]
#     print("******** first switch dpid: ", first_switch_dpid, " first switch output port: ", first_switch_port)

#     for i in range(1,len(path)-1, 2):
#         switch_dpid = path[i]["dpid"]
#         siwtch_input_port = path[i]["port"]
#         siwtch_output_port = path[i+1]["port"]
#         print("******** switch dpid: ", switch_dpid, " switch input port: ", siwtch_input_port, " switch output port: ", siwtch_output_port)

#     last_switch_dpid = path[-1]["dpid"]
#     last_switch_port = path[-1]["port"]
#     print("******** last switch dpid: ", last_switch_dpid, " last switch input port: ", last_switch_port)


hop_count = possible_routes["results"][2]["hop_count"]
latency = possible_routes["results"][2]["latency"]
path = possible_routes["results"][2]["path"]
print("Hop Count: ", hop_count)
print("Latency: ", latency)

first_switch_dpid = path[0]["dpid"]
first_switch_out_port = path[0]["port"]
print("******** first switch dpid: ", first_switch_dpid, " first switch output port: ", first_switch_out_port)

flow_first_1 = {
    "switch": first_switch_dpid,
    "name": "flow_first_1",
    "cookie": "0",
    "priority":"32768",
    "eth_type" : "0x0800" ,
    "ipv4_src": "10.0.0.1/32",
    "ipv4_dst": "10.0.0.10/32",
    "in_port": "4",
    "active":"true",
    "actions": f"output={first_switch_out_port}"
}
api_methods.flowPusher(flow_first_1)

flow_first_2 = {
    "switch": first_switch_dpid,
    "name": "flow_first_2",
    "cookie": "0",
    "priority":"32768",
    "eth_type" : "0x0800" ,
    "ipv4_src": "10.0.0.10/32",
    "ipv4_dst": "10.0.0.1/32",
    "in_port": first_switch_out_port,
    "active":"true",
    "actions": "output=4"
}
api_methods.flowPusher(flow_first_2)


for i in range(1,len(path)-1, 2):
    flow_1_name = f"flow_{i}_1"
    flow_2_name = f"flow_{i}_2"
    switch_dpid = path[i]["dpid"]
    siwtch_input_port = path[i]["port"]
    siwtch_output_port = path[i+1]["port"]

    print("******** switch dpid: ", switch_dpid, " switch input port: ", siwtch_input_port, " switch output port: ", siwtch_output_port)
    flow = {
    "switch": switch_dpid,
    "name": flow_1_name,
    "cookie": "0",
    "priority":"32768",
    "eth_type" : "0x0800" ,
    "ipv4_src": "10.0.0.1/32",
    "ipv4_dst": "10.0.0.10/32",
    "in_port": siwtch_input_port,
    "active":"true",
    "actions": f"output={siwtch_output_port}"
    }
    api_methods.flowPusher(flow)
    flow_2 = {
    "switch": switch_dpid,
    "name": flow_2_name,
    "cookie": "0",
    "priority":"32768",
    "eth_type" : "0x0800" ,
    "ipv4_src": "10.0.0.10/32",
    "ipv4_dst": "10.0.0.1/32",
    "in_port": siwtch_output_port,
    "active":"true",
    "actions": f"output={siwtch_input_port}"
    }
    api_methods.flowPusher(flow_2)


last_switch_dpid = path[-1]["dpid"]
last_switch_port = path[-1]["port"]
print("******** last switch dpid: ", last_switch_dpid, " last switch input port: ", last_switch_port)

flow_last_1 = {
    "switch": last_switch_dpid,
    "name": "flow_last_1",
    "cookie": "0",
    "priority":"32768",
    "eth_type" : "0x0800" ,
    "ipv4_src": "10.0.0.1/32",
    "ipv4_dst": "10.0.0.10/32",
    "in_port": last_switch_port,
    "active":"true",
    "actions": f"output={4}"
}
api_methods.flowPusher(flow_last_1)

flow_last_2 = {
    "switch": last_switch_dpid,
    "name": "flow_last_2",
    "cookie": "0",
    "priority":"32768",
    "eth_type" : "0x0800" ,
    "ipv4_src": "10.0.0.10/32",
    "ipv4_dst": "10.0.0.1/32",
    "in_port": "4",
    "active":"true",
    "actions": f"output={last_switch_port}"
}
api_methods.flowPusher(flow_last_2)
