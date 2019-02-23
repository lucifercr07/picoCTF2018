import pwn
import re
import os

elf = pwn.ELF('./be-quick-or-be-dead-2')

fib_number = 4368447739709774716003881551397205159088952756411141941533814668901464054869881997817744932743716769887780898920209866426445447485522551760777962122217963045451173078851717190916177144613851841799958503738854017612313939353

# modifying alarm function to do nothing using 'ret'
elf.asm(elf.symbols['alarm'], 'ret')
# modifying 'calculate_key function to return the number after changing it into 32-bits, Hopper can be used to find the function name and fib_number
elf.asm(elf.symbols['calculate_key'], 'mov eax,%s\nret\n' % (hex(fib_number & 0xFFFFFFFF)))
# saving to new binary
elf.save('./new')
os.system('chmod +x ./new')

p= pwn.process('./new')
prompt = p.recvall()
flag = re.findall('\n(.*)', prompt)[5] 
print flag