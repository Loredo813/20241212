import time
import re

def abnormal_flow(net, abnormal_rtt_results):
    h1 = net.get('h1')
    s2 = net.get('s2')
    start_time = time.time()

    try:
        while time.time() - start_time <= 10:
            # 執行 ping 命令
            ping_result = s2.cmd(f'ping -c 1 {h1.IP()}')
            current_time = (time.time()-start_time) +5
            
            # 使用正則表達式擷取 RTT
            match = re.search(r'time=(\d+\.\d+) ms', ping_result)
            if match:
                rtt = round(float(match.group(1)), 2)
                abnormal_rtt_results.append((current_time, rtt))
                print(f"[Abnormal] S2->h1, RTT: {rtt} ms")
            else:
                print(f"Time: {current_time:.2f}s, Ping failed or no RTT found.")

            # 每秒執行一次
            time.sleep(1)
    except KeyboardInterrupt:
        print("Ping process stopped.")