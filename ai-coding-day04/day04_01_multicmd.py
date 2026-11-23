# 任务1 · 封装多命令函数 qytang_multicmd


import time
import paramiko

def qytang_multicmd(ip, username, password, cmd_list, wait_time=2, verbose=True, port=22):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        ip,
        port=port,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
        timeout=5
    )

    chan = ssh.invoke_shell()
    time.sleep(1)

    # 先读掉登录欢迎信息，避免混入第一条命令的回显
    if chan.recv_ready():
        welcome = chan.recv(65535).decode(errors="ignore")
        if verbose:
            cleaned = welcome.strip()      # 去掉首尾的换行
            if cleaned:                    # 只有真读到了内容才打印
                print(cleaned, flush=True)
    output = ""


    for cmd in cmd_list:
        chan.sendall((cmd + "\n").encode())   # \n 相当于回车
        time.sleep(wait_time)

        empty_count = 0          # 连续空读计数
        max_empty = 3            # 连续 3 次没数据，才认为这条命令真的结束,适用高延迟场景
        while True:
            if chan.recv_ready():
                chunk = chan.recv(65535).decode(errors="ignore")
                output += chunk
                if verbose:
                    print(chunk, end="", flush=True)
                empty_count = 0          # 收到数据，计数清零
                time.sleep(0.3)
            else:
                empty_count += 1
                if empty_count >= max_empty:
                    break
                time.sleep(0.5)          # 若没数据，再等半秒

    ssh.close()
    return output


if __name__ == "__main__":
    cmd_list = [
        "terminal length 0",
        "show version | include Software,",
        "show running-config | include hostname",
    ]


    result = qytang_multicmd(
        "172.19.11.140",
        "admin",
        "Cisc0123",
        cmd_list,
        port=2231,
    )