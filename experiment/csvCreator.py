import pandas as pd

columns = ['average_rtt', 'packet_loss', 
           'bits_per_second', 'bu_ratio','retransmits', 'cpu_host_total', 'cpu_host_user', 'cpu_host_system', 'cpu_remote_total', 'cpu_remote_user', 'cpu_remote_system', 
           "bidirectional_duration_ms", "bidirectional_packets", "bidirectional_bytes", "src2dst_duration_ms", "src2dst_packets",
           "src2dst_bytes", "dst2src_duration_ms", "dst2src_packets", "dst2src_bytes", "bidirectional_min_ps",
           "bidirectional_mean_ps", "bidirectional_stddev_ps", "bidirectional_max_ps", "src2dst_min_ps", "src2dst_mean_ps",
           "src2dst_stddev_ps", "src2dst_max_ps", "dst2src_min_ps", "dst2src_mean_ps", "dst2src_stddev_ps",
           "dst2src_max_ps", "bidirectional_min_piat_ms", "bidirectional_mean_piat_ms", "bidirectional_stddev_piat_ms", "bidirectional_max_piat_ms",
           "src2dst_min_piat_ms", "src2dst_mean_piat_ms", "src2dst_stddev_piat_ms", "src2dst_max_piat_ms", "dst2src_min_piat_ms",
           "dst2src_mean_piat_ms", "dst2src_stddev_piat_ms", "dst2src_max_piat_ms",
           'psnr', 'ssim_first_value', 'ssim_second_value', "original_file_size", "file_size", "time", "traffic_time", 'traffic_type']

df = pd.DataFrame(columns=columns)

df.to_csv("data.csv", sep=',', index=False, encoding='utf-8')