#!/bin/bash
source /home/liuyinxin/.venv/tensorflow/bin/activate
python /home/liuyinxin/project/captcha_server/manage.py  $1> /dev/null 2>&1 &
echo $! > /home/liuyinxin/project/captcha_server/pid/manage.pid
echo 'manage start on '$!
