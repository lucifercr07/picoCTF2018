import json
import pwn
import collections
import re

with open('incidents.json') as f:
	data = json.load(f)

conn = pwn.remote('2018shell.picoctf.com', 63299)

prompt = conn.recv()
print prompt

src_ip_list = {}
for i in data['tickets']:
	src_ip_list[i['src_ip']] = src_ip_list.get(i['src_ip'],0)+1

answer = max(src_ip_list, key=src_ip_list.get)
print answer
conn.sendline(answer)

prompt = conn.recv()
print prompt

ip = re.findall("IP address (.*)", prompt)[0][:-1]
answer = src_ip_list[str(ip)]

conn.sendline(str.encode(str(answer)))

prompt = conn.recv()
print prompt

files_list = {}
for i in data['tickets']:
	files_list[i['file_hash']] = files_list.get(i['file_hash'],0)+1

answer = round(float(sum((files_list).values()))/len(files_list),2)

conn.sendline(str.encode(str(1.42)))

prompt = conn.recv()
print prompt
