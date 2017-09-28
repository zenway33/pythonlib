!/usr/bin/env python
# coding=utf-8

# 写入文件、读取文件
with open('somefile.txt', 'a') as f:
	f.write('Hello\n')

with open("/tmp/foo.txt") as f:
    data = f.read()

with open('a.txt') as f:
	for i in f:
	    print(i)
	print(f.read())        # 打印所有内容为字符串
	print(f.readlines())   # 打印所有内容按行分割的列表

# 如何输出漂亮的json格式
from pprint import pprint
i = r.json
pprint(i)  即可格式漂亮的格式


