# 任务2 · 正则表达式测试 2：解析ASA防火墙连接表


# 预期输出 对应结果1。 运行文件：day02_02_asa_conn.py。 按给定输入解析后的结果；列对齐应一致，不以不可见的行尾空格判分。

# 终端输出
# Protocol    : TCP
# Server IP   : 172.16.1.101
# Server Port : 443
# Client IP   : 172.16.66.1
# Client Port : 53710

import re

conn = 'TCP server  172.16.1.101:443 localserver  172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

pattern=(r"([A-Z]{3})"
        r"\s+server\s+"
        r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})"
        r"\s+localserver\s+"
        r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})"
)

match = re.match(pattern,conn,re.I)

if match:
    item = {
        "protocol": match.group(1),
        "SrcIP": match.group(2),
        "SrcPort": match.group(3),
        "DstIP": match.group(4),
        "DstPort": match.group(5),
    }
    print(f"{'Protocol':<12}: {item['protocol']}")
    print(f"{'Server IP':<12}: {item['SrcIP']}")
    print(f"{'Server Port':<12}: {item['SrcPort']}") 
    print(f"{'Client IP':<12}: {item['DstIP']}")
    print(f"{'Client Port':<12}: {item['DstPort']}")