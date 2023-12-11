import requests

def flowPusher(flow:dict):
    # The API endpoint to communicate with
    url_post = "http://127.0.0.1:8080/wm/staticentrypusher/json"

    # A POST request to tthe API
    post_response = requests.post(url_post, json=flow)

    # Print the response
    post_response_json = post_response.json()
    print(post_response_json)

def getPaths(src_dpid:str, dst_dpid:str, num_paths:int):
    url = f"http://127.0.0.1:8080/wm/routing/paths/{src_dpid}/{dst_dpid}/{num_paths}/json"
    response = requests.get(url)
    response_json = response.json()
    print("[INFO]****** GET METHOD RESULT *****\n", response_json)
    return response_json