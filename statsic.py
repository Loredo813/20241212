import numpy as np
import statistics

def calculate_rtt_statistics(normal_rtt_results):
    if not normal_rtt_results:
        print("No RTT data available for analysis.")
        return

    # 假設 normal_rtt_results 包含時間和 RTT 的 tuple 清單
    rtts = [entry[1] for entry in normal_rtt_results]
    avg_rtt = statistics.mean(rtts)
    max_rtt = max(rtts)
    min_rtt = min(rtts)
    stddev_rtt = statistics.stdev(rtts) if len(rtts) > 1 else 0

    print(f"Average RTT: {avg_rtt:.2f} ms")
    print(f"Maximum RTT: {max_rtt:.2f} ms")
    print(f"Minimum RTT: {min_rtt:.2f} ms")
    print(f"Standard Deviation of RTT: {stddev_rtt:.2f} ms")