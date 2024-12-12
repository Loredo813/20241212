import time
import re

def normal_flow(net, normal_rtt_results):
    h1 = net.get('h1')
    s1 = net.get('s1')
    start_time = time.time()

    try:
        while time.time() - start_time <= 20:
            # 執行 ping 命令
            ping_result = s1.cmd(f'ping -c 1 {h1.IP()}')
            current_time = time.time() - start_time
            
            # 使用正則表達式擷取 RTT
            match = re.search(r'time=(\d+\.\d+) ms', ping_result)
            if match:
                rtt = round(float(match.group(1)), 2)
                normal_rtt_results.append((current_time, rtt))
                print(f"Time: {current_time:.0f}s, RTT: {rtt} ms")
            else:
                print(f"Time: {current_time:.2f}s, Ping failed or no RTT found.")

            # 每秒執行一次
            time.sleep(1)
    except KeyboardInterrupt:
        print("Ping process stopped.")
