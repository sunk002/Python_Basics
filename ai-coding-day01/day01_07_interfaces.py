# 任务7 · 用列表和字典生成接口状态报告
# 每个字典表示一条接口记录，列表保存全部记录。用 for 遍历 interfaces，取出 name、status、speed，并用 format() 
#或 f-string 对齐输出。不要创建 intf1、status1、speed1 这一组组独立变量。
# 给定输入
# interfaces = [
#     {"name": "Gi0/0", "status": "up", "speed": "1G"},
#     {"name": "Gi0/1", "status": "down", "speed": "1G"},
#     {"name": "Gi0/2", "status": "up", "speed": "10G"},
# ]
# 提示 用 "{:<10}{:<8}{}".format(...) 设置接口和状态两列的宽度。

# 运行命令 源码保存为 day01_07_interfaces.py，在练习目录运行。

# 预期输出 接口列宽 10、状态列宽 8，分隔线为 20 个减号

# 终端输出
# 接口      状态    速率
# --------------------
# Gi0/0     up      1G
# Gi0/1     down    1G
# Gi0/2     up      10G

interfaces = [
    {"name": "Gi0/0", "status": "up", "speed": "1G"},
    {"name": "Gi0/1", "status": "down", "speed": "1G"},
    {"name": "Gi0/2", "status": "up", "speed": "10G"},
]

print("接口"+" "*7+"状态"+" "*5+"速率")
print("-"*24)
for interface in interfaces:
    print(f"{interface['name']:10} {interface['status']:8} {interface['speed']}")    #接口列宽 10、状态列宽 8

print("-"*24)

