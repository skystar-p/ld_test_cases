import sys


def print_registers(reg):
    print('registers: ', end='')
    for i, r in enumerate(reg):
        print('{}({}) '.format(r, hex(r)), end='')
    print('')


f = open(sys.argv[1], 'r')
instructions = f.readlines()
f.close()

register = [0] * 4
memory = []

for i in range(16):
    memory.append(i)

for i in range(0, -16, -1):
    memory.append(i)

pc = 0

while True:
    instr = instructions[pc]
    print('==============================================')
    print('Current PC: {}'.format(pc))
    print('==============================================')
    opcode = instr[0:2]
    r1 = int(instr[2:4])
    r2 = int(instr[4:6])
    r3 = int(instr[6:8])

    if r1 == 11:
        r1 = 3
    elif r1 == 10:
        r1 = 2

    if r2 == 11:
        r2 = 3
    elif r2 == 10:
        r2 = 2

    if r3 == 10:
        r3 = -2
    elif r3 == 11:
        r3 = -1

    if opcode == '00':
        res = register[r1] + register[r2]
        print('reg write data: {}({})'.format(res, hex(res)))
        register[r3] = res
        print_registers(register)
    elif opcode == '01':
        res = memory[register[r1] + r3]
        print('reg write data: {}({})'.format(res, hex(res)))
        register[r2] = res
        print_registers(register)
    elif opcode == '10':
        res = register[r2]
        memory[register[r1] + r3] = res
        print('memory loaded: value {}({}) to memory {}'.format(res, hex(res), r1 + r3))
    elif opcode == '11':
        if r3 == -1:
            print('jump -1: infinite loop')
            break
        print('jump: pc {} to {}'.format(pc, pc+r3))

    print()
    pc += 1


