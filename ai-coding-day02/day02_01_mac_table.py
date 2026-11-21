# 本次作业目标
# 把网络设备的原始文本整理成可用数据：用正则提取MAC、连接和路由信息，用字典保存连接记录，并按接口编号排序。 共5个任务：MAC解析、ASA连接解析、网关提取、连接记录字典和接口排序。

# 文件命名说明 下文文件名仅供参考，可以自定；改名后，导入、路径及配置中的引用须保持一致。

# 任务1 · 正则表达式测试 1：解析MAC地址表
# 主要任务
# 下面是一台交换机MAC地址表中的一行。用正则表达式提取VLAN、MAC地址、类型和接口，再用format()按标签对齐打印。本题只解析给定文本，不需要连接交换机。

# 文件安排 本题编写1个Python文件。

# 文件（参考名）	负责什么
# day02_01_mac_table.py	新写程序：正则表达式测试 1：解析MAC地址表。
# 给定输入 交换机MAC地址表的一行回显。

# 复制
# mac_table = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'
# 指定技术 使用re.match()与捕获组；使用group()读取各组，format()控制标签宽度。 标签左对齐占6个字符，再打印冒号和值。

# 提示 字段之间空格数量不同，用\s+匹配；MAC中的点号用\.表示真正的点。

# 必交内容
# 本题作业中必须附上以下代码和运行结果，逐项对应。

# 代码 day02_01_mac_table.py的完整内容。
# 结果1 · 终端输出截图 运行day02_01_mac_table.py，展示上方要求中的运行结果。
# 提交源码和运行截图；结果必须由给定输入解析得到，不能把预期输出直接写进print。

# 预期输出 对应结果1。 运行文件：day02_01_mac_table.py。 按给定输入解析后的结果；列对齐应一致，不以不可见的行尾空格判分。

# 终端输出
# VLAN  : 166
# MAC   : 54a2.74f7.0326
# Type  : DYNAMIC
# Port  : Gi1/0/11


import re

mac_table = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'


pattern=(r"(\d{1,4})"  #1到4个数字
        r"\s+" #一个或多个空白（空格或制表符）
        r"([0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4})"     #[0-9A-Fa-f]{4} 任意十六进制字符重复{4}次 \. 转义的点，不转义代表任意字符，例如54a2-74f7-0326也符合
        r"\s+"
        r"(DYNAMIC|STATIC)" #二选一
        r"\s+" 
        r"(Gi\d+/\d+/\d+)")  

match = re.match(pattern,mac_table,re.I)  #re.I 忽略大小写
# if match:
#     item = {
#         "vlan": match.group(1),
#         "mac": match.group(2),
#         "type": match.group(3),
#         "port": match.group(4)
#     }
#     print(f"{'VLAN':<6}: {item['vlan']}")
#     print(f"{'MAC':<6}: {item['mac']}")
#     print(f"{'Type':<6}: {item['type']}")
#     print(f"{'Port':<6}: {item['port']}")



if match:
    vlan = match.group(1)
    mac = match.group(2)
    type_ = match.group(3)
    port = match.group(4)

    print("{:<6}: {}".format("VLAN", vlan))   
    print("{:<6}: {}".format("MAC", mac))
    print("{:<6}: {}".format("Type", type_))
    print("{:<6}: {}".format("Port", port))

