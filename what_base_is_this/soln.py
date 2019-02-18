import pwn
import re

conn = pwn.remote('2018shell.picoctf.com',15853)

prompt = conn.recv()
print prompt

binary = re.findall('the (.*) as a word', prompt)
answer = hex(int(binary[0].replace(' ',''),2))[2:].decode('hex')
conn.sendline(answer)

prompt = conn.recv()
print prompt

hexs = re.findall('the (.*) as a word', prompt)
answer = hexs[0].decode('hex')
conn.sendline(answer)

prompt = conn.recv()
print prompt

octal = re.findall('the (.*) as a word', prompt)[0]
answer = ''.join([ chr(int(x,8)) for x in octal.split()])
conn.sendline(answer)

prompt = conn.recv()
print prompt

conn.close()