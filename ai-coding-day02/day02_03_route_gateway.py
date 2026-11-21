# 任务3 · 正则表达式练习：从 route -n 输出中查找网关

# route_n_result = """Kernel IP routing table
# Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
# 0.0.0.0         192.168.214.2   0.0.0.0         UG    100    0        0 eno16777984
# 192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
# 192.168.214.0   0.0.0.0         255.255.255.0   U     100    0        0 eno16777984
# 202.100.1.0     0.0.0.0         255.255.255.0   U     100    0        0 eno33554944"""


import re
import subprocess  #python3推荐方法，os.popen已标记为legacy

pattern=r"^0\.0\.0\.0\s+(\S+)\s+0\.0\.0\.0\s+UG\b.*"  #^从开头开始匹配

try:
    result = subprocess.run(["route", "-n"], capture_output=True, text=True)
except FileNotFoundError:
    print("route 命令不存在，请安装 net-tools 或改用 ip route")
    raise SystemExit(1)

if result.returncode != 0:
    print("[ERROR]", result.stderr)
    raise SystemExit(1)

match = re.search(pattern, result.stdout, re.M)   #re.M re.MULTILINE，让^对每行生效
if match:
    item = {
        "gateway": match.group(1),
    }
    print("网关为:", item["gateway"])
else:
    print("未找到默认路由")



