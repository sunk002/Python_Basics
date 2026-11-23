
import socket
import paramiko
from day04_01_multicmd import qytang_multicmd
from day04_02_ping_check import ping_check


def main():
    # 设备字典列表（替换为你真实的账号密码）
    devices = [
        {'ip': '172.19.11.140', 'port': 2231, 'username': 'admin', 'password': 'Cisc0123'},
        {'ip': '172.19.11.140', 'port': 2232, 'username': 'admin', 'password': 'Cisc0123'},
        {'ip': '172.19.11.140', 'port': 2288, 'username': 'admin', 'password': 'Cisc0123'},
        {'ip': '172.19.11.150', 'port': 2231, 'username': 'admin', 'password': 'Cisc0123'},
    ]
    
    RIP_COMMANDS = [
        'configure terminal',
        'router rip',
        'version 2',
        'network 172.16.0.0',
        'end',
    ]

    for dev in devices:
        ip = dev['ip']
        port = dev['port']
        
        # 1. ping 判断可达性
        reachable, rtt = ping_check(ip)
        
        if reachable:
            print(f"[{ip}:{port}] ping通，开始配置RIP")
            
            try:
                # 2. 尝试 SSH 连接并配置
                qytang_multicmd(
                    ip=ip,
                    username=dev['username'],
                    password=dev['password'],
                    cmd_list=RIP_COMMANDS,
                    wait_time=2,
                    verbose=True,
                    port=port
                )
                print(f"[{ip}:{port}] RIP命令执行完成\n")
                
            except (socket.timeout, paramiko.ssh_exception.SSHException, ConnectionError) as e:
                # 3. 捕获端口不通、拒绝连接、认证失败等 SSH 错误
                print(f"[{ip}:{port}] SSH连接失败，跳过：{e}\n")
            except Exception as e:
                print(f"[{ip}:{port}] 未知错误，跳过：{e}\n")
                
        else:
            print(f"[{ip}:{port}] ping不通，跳过SSH\n")


if __name__ == "__main__":
    main()