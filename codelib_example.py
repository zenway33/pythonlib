!/usr/bin/env python
# coding=utf-8

# 写入文件、读取文件
with open('somefile.txt', 'a') as f:
	f.write('Hello\n')

with open("/tmp/foo.txt") as f:
    data = f.read()
