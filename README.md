# Project Documentation
<p>Computer Engineering Gradution Thesis - I</p>
<p>Bursa Uludag University</p>
<p style="text-align:justify"><b>Project Title:</b> Ai based routing algorithm and traffic level classification in software defined network

## Project Members
| First & Last | Mail |
| -------- | -------- | 
| Anıl Dursun İpek | anildursunipek@gmail.com| 
| Batuhan Arslandaş | batuhanarslandass@hotmail.com |

<p><b>Project Consultant:</b> DOÇ. DR. MURTAZA CİCİOĞLU</p>

## Project description
<p style="text-align:justify">A routing algorithm was developed on a network topology constructed in the Mininet environment using the Floodlight controller. In the simulated environment, 873 data points, each possessing 50 artificial features, were generated, and these data points were classified based on traffic levels using the KNN algorithm. The routing algorithm, created using the classification model, directed video transfers according to the traffic levels.</p>

## Used Tools
```ruby
python3
Mininet
Floodlight
Iperf3
Ping
FFmpeg
NFStream
Ubuntu20.04
```

## Development Environment

| Name | Attribute |
| -------- | -------- | 
| Operating System | Ubuntu 20.04 | 
| RAM | 8 GB | 
| Processor | Intel I7 – 4 core | 
| SDN Controller | Floodlight | 
| Simulation Tool | Mininet | 
| Traffic Generator | Iperf3 | 
| ML Platform | Google Colab | 
| Programming Language | Python3 | 


## Used Topology - NSFNET

<p style="text-align:justify">NSFNET (National Science Foundation Network) was a research and education network utilized in the United States from 1985 to 1995. The topology of NSFNET consisted of a series of mainframe computers and routers. The network's structure was built upon a core network and interconnection points to this network, known as Attached Intermediate Points of Presence (IPOP). This network architecture was designed to facilitate high-speed wide-area connections and data transmission between mainframe computers.

NSFNET was specifically designed as a network for information exchange in scientific and educational domains, serving the purpose of transmitting data among universities, research institutions, and government entities. It operated on the TCP/IP protocol, forming the foundational protocol set for the internet during that era. Representing a critical infrastructure for the development of the internet during its time, NSFNET eventually gave way to a broader and more modern internet infrastructure in 1995. Figure 4 illustrates the general overview of the NSFNET network.</p>
<div align="center" style="align:center"><img width="80%" src="./assets/CDN Diagram-BASE-result.png"></img></div>


## Video Transfer Scenarios and Data Collection
<p style="text-align:justify">In the Mininet environment, specific scenarios have been created to obtain data on the NSFNET network. These scenarios are primarily based on sending data over three different paths in the network. On these paths, two different traffic levels have been established.

The network consists of a total of 14 switches, 1 client, and 1 server. Additionally, there is one Floodlight SDN Controller that controls all the switches in the network. These network devices form the foundation for the constructed scenarios. When scenarios are devised, different clients are added to the network, and traffic is generated among them.</p>
<div align="center">Scenario-1</div>
<div align="center" style="align:center"><img width="80%" src="./assets/CDN-Diagram-Scenario-1.png"></img></div>
<p style="text-align:justify">In the scenario, two different traffic levels are established between the sender and receiver, with 4 clients assigned to switches 3 and 8 each. In the low-traffic environment, the selected 4 clients establish 2 connections among themselves, generating TCP traffic and utilizing approximately 30% of the bandwidth. In the high-traffic environment, 8 clients establish 4 connections among themselves, creating TCP traffic and utilizing approximately 90% of the bandwidth. After the traffic is generated, video transmission occurs between the main client and the server in the environment.</p>
<div align="center">Scenario-2</div>
<div align="center" style="align:center"><img width="80%" src="./assets/CDN Diagram-Scenario-2.png"></img></div>
<p style="text-align:justify">In the second scenario, 4 clients are assigned to switches 1 and 10 each. In the low-traffic environment, similar to the first scenario, the 4 clients establish 2 connections among themselves, generating TCP traffic and utilizing approximately 30% of the bandwidth. In the high-traffic environment, 8 clients establish 4 connections among themselves, creating TCP traffic and utilizing approximately 90% of the bandwidth. Video transmission is conducted in both cases to perform tests.</p>
<div align="center">Scenario-3</div>
<div align="center" style="align:center"><img width="80%" src="./assets/CDN-Diagram-Scenario-3.png"></img></div>
<p style="text-align:justify">In the third scenario, the number of hops is once again increased, and a path with a length of 5 hops is chosen. Video transmission between the client and the server follows the switches 0 - 2 - 5 - 13 - 10 - 9. Similar to the other scenarios, both low and high traffic are generated in this scenario, with the same number of clients and the same amount of bandwidth being used. Clients responsible for generating traffic are assigned to switches 2 and 10, following the same principles as in the previous scenarios.</p>

### Obtaining Paths Information
<p style="text-align:justify">Information about the path for the transfer between the client and server is obtained using different tools. These pieces of information serve as references for classifying the traffic level of the selected connection path. Additionally, it reveals the effects arising from the traffic levels before and after the transfer.</p>

<div><a href="https://github.com/anildursunipek/AI-based-Routing-and-Traffic-Classification-in-SDN/blob/main/experiment/video_stream_data_on_mininet.csv">Collected Data</a></div>
<div><a href="https://github.com/anildursunipek/AI-based-Routing-and-Traffic-Classification-in-SDN/blob/main/experiment/nsfnet_topology_scenario.py">Data Generator Example Code</a></div>

## Data Generator Code Logical Flow Schema
<div align="center" style="align:center"><img width="60%" src="./assets/data-generator-flow-schema.png"></img></div>

## AI Based Routing
<p style="text-align:justify">The obtained data was analyzed, and binary classification models were employed to train based on variables affecting the traffic level. Using the model obtained after the training, a routing algorithm was designed. You can access the designed algorithm codes by clicking on the link below.</p>

<div><a href="https://github.com/anildursunipek/AI-based-Routing-and-Traffic-Classification-in-SDN/blob/main/experiment/ai-based-routing-algorithm-experiment.py">AI Based Routing</a></div>

## Algorithm Performance Testing
<p style="text-align:justify">The artificial intelligence-based routing algorithm proposed by us is being tested on the NSFNET topology in the designed scenario. The scenario includes 19 clients generating traffic, 1 main client (receiving the video), and 1 server (sending the video). Additionally, the Floodlight controller, considered as the brain of the network, is configured with the metric set to the hop count value. The figure illustrates the traffic flows and degrees between hosts, providing a general visualization of the scenario.</p>

<div align="center" style="align:center"><img width="80%" src="./assets/result-scenario-base.png"></img></div>

<p style="text-align:justify">During the testing phase, initially, data transfer between the client and server takes place without any intervention in the network. The Floodlight controller conducts data flow over the shortest path using the hop count metric, following the switches 0-3-8-9. Heavy traffic on this path negatively impacts data flow, leading to data losses. In previous tests, sending video over the path taken by the controller resulted in low-quality values. The figure illustrates the path followed by the Floodlight controller during data transfer.</p>

<div align="center" style="align:center"><img width="80%" src="./assets/floodlight-path.png"></img></div>

<p style="text-align:justify">In the second part of the testing phase, the proposed routing algorithm is being tested. For the test, the same environment variables as the first stage are used. Before the transfer between the client and server, the proposed algorithm operates, identifying the path with low traffic. During the transfer, it follows the switches 0-3-4-5-12-9. Having lower traffic on this path allows for a more successful data transfer. The figure illustrates the path followed by the proposed algorithm during data transfer.</p>

<div align="center" style="align:center"><img width="80%" src="./assets/proposal-path.png"></img></div>

## Result

<p style="text-align:justify">After executing the scenarios for both algorithms, the data collected during the test is compared. For comparison, the network is monitored for 60 seconds, and RTT (Round-Trip Time) and throughput values on the path are recorded. The figure illustrates a line chart comparing the recorded data.</p>

<div align="center" style="align:center"><img width="60%" src="./assets/result-comparison-rtt.png"></img></div>
<div align="center" style="align:center"><img width="60%" src="./assets/result-comparison-throughput.png"></img></div>

<p style="text-align:justify">In the first test phase, using the default routing algorithm with the hop count metric, an average RTT of 2063.14 ms and a throughput of 2135.90 bps are obtained. In the second phase, an improvement in these metrics is observed with the proposed algorithm, achieving an RTT of 354.05 ms and a throughput of 6313.50 bps. As a result of the comparison, our proposed algorithm successfully identifies the path with low traffic and conducts data transfer along this path.</p>

<hr>
<hr>
<div align="center" style="align:center"><img width="80%" src="./assets/thanks.png"></img></div>
