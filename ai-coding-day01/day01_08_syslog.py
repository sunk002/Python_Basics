# 任务8 · 处理Syslog文本并生成告警卡片
# 使用正则表达式 re.search() 从 message 中提取接口名和状态，不能用 split() 或 rsplit()；再用 f-string 或 format() 
#按“标签 : 值”输出日期、设备、等级、接口和状态。
# 给定输入
# date = "2026-03-03"
# hostname = "SW-Core-01"
# level = "CRITICAL"
# message = "%LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down"
# 提示 re 是标准库，无需安装。接口名在 Interface 和逗号之间，状态在 changed state to 后；用两个括号分组，再用 group(1)、group(2) 取值。
# 运行命令 源码保存为 day01_08_syslog.py，在练习目录运行。

# 预期输出
# 日期 : 2026-03-03
# 设备 : SW-Core-01
# 等级 : CRITICAL
# 接口 : GigabitEthernet0/1
# 状态 : down

# 第二次：把 message 改成下面这行后再运行，提取代码不动。
# message = "%LINK-3-UPDOWN: Interface GigabitEthernet0/2, changed state to up"

# 预期输出
# 日期 : 2026-03-03
# 设备 : SW-Core-01
# 等级 : CRITICAL
# 接口 : GigabitEthernet0/2
# 状态 : 

import re

date = "2026-03-03"
hostname = "SW-Core-01"
level = "CRITICAL"
message = "%LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down"

match = re.search(r"Interface ([^,]+), changed state to (\S+)", message)
interface = match.group(1)
status = match.group(2)

print(f"日期 : {date}")
print(f"设备 : {hostname}")
print(f"等级 : {level}")
print(f"接口 : {interface}")
print(f"状态 : {status}") 

