from nfstream import NFStreamer
import sys


if __name__ == '__main__':  # Mandatory if you are running on Windows Platform
    flow_streamer = NFStreamer(source="s0-eth4",
                               statistical_analysis=True,
                               idle_timeout=15)
                            #    active_timeout=1)
    # flow_streamer.to
    for flow in flow_streamer:
        if(((flow.src_ip == "10.0.0.1" and flow.dst_ip == "10.0.0.10") or 
            (flow.src_ip == "10.0.0.10" and flow.dst_ip == "10.0.0.1")) and 
            flow.application_name == "Unknown" and
            flow.application_category_name == "Unspecified"):
            print(flow)
        print("It works!!!")