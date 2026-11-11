# 任务3 · 字符串方法：处理show version输出
# 从设备采集回来的版本信息字符串经常有多余的空格，需要处理后再使用。完成以下 3 步并分别打印结果：
# 去掉首尾空格（strip）
# 把字符串转成全大写（upper）
# 把 "17.03.04" 替换成 "17.06.01"（replace）
# 给定输入 注意字符串前后各有两个空格
# version_raw = "  Cisco IOS XE Software, Version 17.03.04  "
# 运行命令 源码保存为 day01_03_string_methods.py，在练习目录运行。

# 预期输出 第 2、3 步都在第 1 步去掉空格的结果上操作，所以“替换版本”保持原来的大小写

# 去掉空格: Cisco IOS XE Software, Version 17.03.04
# 转大写:   CISCO IOS XE SOFTWARE, VERSION 17.03.04
# 替换版本: Cisco IOS XE Software, Version 17.06.01

#==================================================================================================

version_raw = "  Cisco IOS XE Software, Version 17.03.04  "

print("去掉空格：" + version_raw.strip())
print("转大写：  " + version_raw.strip().upper())
print("替换版本：" + version_raw.strip().replace("17.03.04", "17.06.01"))
