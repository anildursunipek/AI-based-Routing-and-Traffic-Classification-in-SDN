from nfstream import NFStreamer
import sys


if __name__ == '__main__':  # Mandatory if you are running on Windows Platform
    flow_streamer = NFStreamer(source="s0-eth4",
                               statistical_analysis=True,
                               idle_timeout=1,
                               active_timeout=1)
    for flow in flow_streamer:
        print(flow)