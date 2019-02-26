#!/bin/bash
source /home/liuyinxin/.venv/tensorflow/bin/activate
rm /home/liuyinxin/project/captcha_server/pid/manage.pid
base_path=/home/liuyinxin/project/captcha_server
for ((i = 5000; i <= 5005; ++i))
	python /home/liuyinxin/project/captcha_server/manage.py  $1> /dev/null 2>&1 &
	echo $! >> "${base_path}"/pid/manage.pid
	echo 'manage start on '$!
