#!/bin/bash

# 检查参数数量是否正确
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <VNC端口> <监听端口>"
    exit 1
fi

# 提取参数
vnc_port=$1
listen_port=$2
# 执行命令并获取进程号
nohup /iecube/novnc/utils/novnc_proxy --vnc 127.0.0.1:"$vnc_port" --listen 0.0.0.0:"$listen_port" > /iecube/novnc/log/"$vnc_port".log 2>&1 &
nohup /iecube/vncServerControl/websockify/run 0.0.0.0:"$listen_port" 127.0.0.1:"$vnc_port" > /iecube/vncServerControl/log/48001.log 2>&1 &
pid=$!

# 检查 PID 是否存在
if ps -p $pid > /dev/null; then
    # 进程存在，返回 PID
    echo "$pid"
else
    # 进程不存在，返回 0
    echo "0"
fi
