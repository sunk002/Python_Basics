"""
任务2 · 封装ping函数 ping_check
day04_02_ping_check.py
封装 ping_check 函数：用 pythonping 进行 ICMP 探测，
ping 通返回 (True, 平均延迟毫秒)，不通返回 (False, None)。
"""

from pythonping import ping


def ping_check(host, count=1, timeout=2):

    result = ping(host, count=count, timeout=timeout, verbose=False)

    if result.success():
        return (True, result.rtt_avg_ms)
    else:
        return (False, None)


if __name__ == "__main__":
    hosts = ["172.19.11.146", "172.19.11.147", "172.19.11.150"]

    for host in hosts:
        reachable, rtt = ping_check(host)

        if reachable:
            print(f"{host:<12} 可达   RTT: {rtt:.2f} ms")
        else:
            print(f"{host:<12} 不可达")