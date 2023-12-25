import pandas as pd

columns = ['average_rtt', 'packet_loss', 'bits_per_second', 'bu_ratio','retransmits', 
           'cpu_host_total', 'cpu_host_user', 'cpu_host_system', 'cpu_remote_total',
           'cpu_remote_user', 'cpu_remote_system', 'psnr', 'ssim_first_value', 
           'ssim_second_value', 'traffic_type']

df = pd.DataFrame(columns=columns)

df.to_csv("data.csv", sep=',', index=False, encoding='utf-8')