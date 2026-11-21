# 任务4 · 将ASA连接记录保存为字典

# asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
# TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""

#预期输出
# 打印分析后的字典!

# {('192.168.189.167', '32806', '137.78.5.128', '65247'): ('74', 'UIO'), ('192.168.189.167', '80', '137.78.5.128', '65233'): ('334516', 'UIO')}

# 格式化打印输出

# src       : 192.168.189.167  | src_port  : 32806  | dst       : 137.78.5.128     | dst_port  : 65247
# bytes     : 74               | flags     : UIO
# ====================================================================================
# src       : 192.168.189.167  | src_port  : 80     | dst       : 137.78.5.128     | dst_port  : 65233
# bytes     : 334516           | flags     : UIO
# ====================================================================================

import re

asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""


pattern = (
    r"TCP\s+\S+\s+"
    r"(\d+\.\d+\.\d+\.\d+):(\d+)\s+"
    r"\S+\s+"
    r"(\d+\.\d+\.\d+\.\d+):(\d+),\s+"
    r"idle\s+\S+,\s+"
    r"bytes\s+(\d+),\s+"
    r"flags\s+(\w+)"
)

conn_dict = {}

for line in asa_conn.split("\n"):   #逐行匹配
    if not line.strip():   #非空行
        continue

    match = re.match(pattern, line)
    if match:
        src_ip, src_port, dst_ip, dst_port, bytes_val, flags = match.groups() #

        key = (src_ip, src_port, dst_ip, dst_port)  #四元组判定唯一链接
        value = (bytes_val, flags)  #每个TCP连接对应属性
        conn_dict[key] = value

print("打印分析后的字典!")
print(conn_dict)
print()
print("格式化打印输出")
print()

for key, value in conn_dict.items():
    src_ip, src_port, dst_ip, dst_port = key
    bytes_val, flags = value

    print(
        "{:<6}: {:<20}| {:<9}: {:<10}| {:<4}: {:<18}| {:<10}: {}".format(
            "src", src_ip,
            "src_port", src_port,
            "dst", dst_ip,
            "dst_port", dst_port
        )
    )
    print(
        "{:<6}: {:<20}| {:<9}: {}".format(
            "bytes", bytes_val,
            "flags", flags
        )
    )
    print("=" * 84)