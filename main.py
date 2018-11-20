# created by geoffrey on 2018/11/15


class MipsInstruction:
    def __init__(self):
        self.source_code = ''
        self.name = ''
        self.addr = -1
        self.rs = -1
        self.rt = -1
        self.rd = -1
        self.sa = 0
        self.offset = 0
        self.imm = 0
        self.index = 0
        self.base = 0
        self.type = 0
        self.format = ''


class Date:
    def __init__(self):
        self.source_code = ''
        self.addr = -1
        self.value = 0


def read_binary_code(path):
    file = open(path, "r")
    tmp_file = file.read()
    file.close()
    binary_codes = []
    for binary_code in tmp_file.split('\n'):
        binary_codes.append(binary_code)
    return binary_codes


def add(mips_ins, line):
    mips_ins.name = "add"
    mips_ins.rs = int(line[6: 11], 2)
    mips_ins.rt = int(line[11: 16], 2)
    mips_ins.rd = int(line[16: 21], 2)
    mips_ins.type = 2
    mips_ins.format = "ADD R" + str(mips_ins.rd) + ", R" + str(mips_ins.rs) + ", R" + str(mips_ins.rt)


def sub(mips_ins, line):
    mips_ins.name = "sub"
    mips_ins.rs = int(line[6: 11], 2)
    mips_ins.rt = int(line[11: 16], 2)
    mips_ins.rd = int(line[16: 21], 2)
    mips_ins.type = 2
    mips_ins.format = "SUB R" + str(mips_ins.rd) + ", R" + str(mips_ins.rs) + ", R" + str(mips_ins.rt)


def mul(mips_ins, line):
    mips_ins.name = "mul"
    mips_ins.rs = int(line[6: 11], 2)
    mips_ins.rt = int(line[11: 16], 2)
    mips_ins.rd = int(line[16: 21], 2)
    mips_ins.type = 2
    mips_ins.format = "MUL R" + str(mips_ins.rd) + ", R" + str(mips_ins.rs) + ", R" + str(mips_ins.rt)


def _and(mips_ins, line):
    mips_ins.name = "and"
    mips_ins.rs = int(line[6: 11], 2)
    mips_ins.rt = int(line[11: 16], 2)
    mips_ins.rd = int(line[16: 21], 2)
    mips_ins.type = 2
    mips_ins.format = "AND R" + str(mips_ins.rd) + ", R" + str(mips_ins.rs) + ", R" + str(mips_ins.rt)


def nor(mips_ins, line):
    mips_ins.name = "nor"
    mips_ins.rs = int(line[6: 11], 2)
    mips_ins.rt = int(line[11: 16], 2)
    mips_ins.rd = int(line[16: 21], 2)
    mips_ins.type = 2
    mips_ins.format = "NOR R" + str(mips_ins.rd) + ", R" + str(mips_ins.rs) + ", R" + str(mips_ins.rt)


def slt(mips_ins, line):
    mips_ins.name = "slt"
    mips_ins.rs = int(line[6: 11], 2)
    mips_ins.rt = int(line[11: 16], 2)
    mips_ins.rd = int(line[16: 21], 2)
    mips_ins.type = 2
    mips_ins.format = "SLT R" + str(mips_ins.rd) + ", R" + str(mips_ins.rs) + ", R" + str(mips_ins.rt)


def beq(mips_ins, line):
    mips_ins.name = "beq"
    mips_ins.rs = int(line[6: 11], 2)
    mips_ins.rt = int(line[11: 16], 2)
    mips_ins.offset = int(line[16: 32], 2) * 4
    # print(mips_ins.offset)
    # print(line[16:32])
    mips_ins.type = 3
    mips_ins.format = "BEQ R" + str(mips_ins.rs) + ", R" + str(mips_ins.rt) + ", #" + str(mips_ins.offset)


def bgtz(mips_ins, line):
    mips_ins.name = "bgtz"
    mips_ins.rs = int(line[6: 11], 2)
    #  mips_ins.rt = bin2dec(line[11: 16])
    mips_ins.offset = int(line[16: 32], 2) * 4
    mips_ins.type = 4
    mips_ins.format = "BGTZ R" + str(mips_ins.rs) + ", #" + str(mips_ins.offset)


def bltz(mips_ins, line):
    mips_ins.name = "bltz"
    mips_ins.rs = int(line[6: 11], 2)
    # mips_ins.rt = bin2dec(line[11: 16])
    mips_ins.offset = int(line[16: 32], 2) * 4
    mips_ins.type = 4
    mips_ins.format = "BLTZ R" + str(mips_ins.rs) + ", #" + str(mips_ins.offset)


def sw(mips_ins, line):
    mips_ins.name = "sw"
    mips_ins.base = int(line[6: 11], 2)
    #print(line[6:11])
    mips_ins.rt = int(line[11: 16], 2)
    mips_ins.offset = int(line[16: 32], 2)
    mips_ins.type = 5
    mips_ins.format = "SW R" + str(mips_ins.rt) + ", " + str(mips_ins.offset) + "(R" + str(mips_ins.base) + ")"


def lw(mips_ins, line):
    mips_ins.name = "lw"
    mips_ins.base = int(line[6: 11], 2)
    mips_ins.rt = int(line[11: 16], 2)
    mips_ins.offset = int(line[16: 32], 2)
    mips_ins.type = 5
    mips_ins.format = "LW R" + str(mips_ins.rt) + ", " + str(mips_ins.offset) + "(R" + str(mips_ins.base) + ")"


def sll(mips_ins, line):
    mips_ins.name = "sll"
    mips_ins.rt = int(line[11: 16], 2)
    mips_ins.rd = int(line[16: 21], 2)
    mips_ins.sa = int(line[21: 26], 2)
    mips_ins.type = 6
    mips_ins.format = "SLL R" + str(mips_ins.rd) + ", R" + str(mips_ins.rt) + ", #" + str(mips_ins.sa)


def srl(mips_ins, line):
    mips_ins.name = "srl"
    mips_ins.rt = int(line[11: 16], 2)
    mips_ins.rd = int(line[16: 22], 2)
    mips_ins.sa = int(line[22: 28], 2)
    mips_ins.type = 6
    mips_ins.format = "SRL R" + str(mips_ins.rd) + ", R" + str(mips_ins.rt) + ", #" + str(mips_ins.sa)


def sra(mips_ins, line):
    mips_ins.name = "sra"
    mips_ins.rt = int(line[11: 16], 2)
    mips_ins.rd = int(line[16: 22], 2)
    mips_ins.sa = int(line[22: 28], 2)
    mips_ins.type = 6
    mips_ins.format = "SRA R" + str(mips_ins.rd) + ", R" + str(mips_ins.rt) + ", #" + str(mips_ins.sa)


def j(mips_ins, line):
    mips_ins.name = "j"
    mips_ins.index = int(line[6: 32], 2) * 4
    mips_ins.type = 7
    mips_ins.format = "J " + "#" + str(mips_ins.index)


def jr(mips_ins, line):
    mips_ins.name = "jr"
    mips_ins.rs = int(line[6: 11], 2)
    mips_ins.type = 8
    mips_ins.format = "JR R" + str(mips_ins.rs)


def _break(mips_ins, line):
    mips_ins.name = "_break"
    mips_ins.type = 9
    mips_ins.format = "BREAK"


def parse(mips_instruction, line):
    category1 = {"000100": "beq", "000111": "bgtz", "000001": "bltz", "000010": "j", "101011": "sw",
                 "100011": "lw", "011100": "mul"}  # 前6位不全为零的opcode

    category1_1 = {"110010": "AND", "100001": "MUL", "110001": "SUB", "110000": "ADD", "110011": "NOR",
                   "110101": "SLT"}  # 前6位不全为零的opcode  且是OP rt, rs, imm形式的指令

    category2 = {"100000": "add", "001101": "_break", "001000": "jr", "100100": "_and", "100111": "nor",
                 "000000": "sll", "100010": "sub", "000011": "sra","101010": "slt",
                 "000010": "srl"}  # 前6位全为零的opcode  除去NOP

    mips_instruction.source_code = line
    if line[0:] == "00000000000000000000000000000000":
        mips_instruction.name = 'nop'
        mips_instruction.format = "NOP"
    elif line[0: 6] in category1_1:
        mips_instruction.name = category1_1.get(line[0: 6])
        mips_instruction.rs = int(line[6: 11], 2)
        mips_instruction.rt = int(line[11: 16], 2)
        mips_instruction.imm = int(line[16: 32], 2)
        mips_instruction.type = 1
        mips_instruction.format = mips_instruction.name + " R" + str(mips_instruction.rt) +\
                                  ", R" + str(mips_instruction.rs) + ", #" + str(mips_instruction.imm)
    elif line[0: 6] == '000000':
        eval(category2[line[26:32]])(mips_instruction, line)
    elif line[0: 6] in category1:
        eval(category1[line[0:6]])(mips_instruction, line)


def bin2dec(binary):
    if binary[0] == "0":
        return int(binary[1:], 2)
    else:
        s = ""
        for bit in binary[0:-1]:
            if bit == "0":
                s = s + "1"
            else:
                s = s + "0"
        return -(int(s, 2) + 1)


def dec2bin(dec):
    isNeagtive = False
    if dec<0:
        isNeagtive = True
        dec = -dec
    tmp_binary = bin(dec)[2:]
    need_add = 32 - len(tmp_binary)
    for i in range(0,need_add):
        tmp_binary = '0' + tmp_binary
    if isNeagtive is True:
        for i in range(0,32):
            if tmp_binary[i] == '0':
                tmp_binary[i] = '1'
            else:
                tmp_binary[i] = '0'
        tmp_binary = bin(int(tmp_binary,2)+1)[2:]
    return tmp_binary


def exe_instruction(cycle, addr, ins):
    return "--------------------\nCycle:%d\t%d\t%s\n\n" % (cycle, addr, ins)


def simulate_result(register, data):

    output = "Registers\n" \
              "R00:\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n" \
              "R16:\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n" % tuple(register)
    # output += "Data\n"
    output += "\nData\n" \
              "148:\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n" \
              "180:\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n"\
              "212:\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n\n" % tuple(data)
    return output


def add_exe(ins):
    reg_file[ins.rd] = reg_file[ins.rs] + reg_file[ins.rt]


def sub_exe(ins):
    reg_file[ins.rd] = reg_file[ins.rs] - reg_file[ins.rt]


def mul_exe(ins):
    reg_file[ins.rd] = reg_file[ins.rs] * reg_file[ins.rt]


def _and_exe(ins):
    reg_file[ins.rd] = reg_file[ins.rs] & reg_file[ins.rt]


def nor_exe(ins):
    reg_file[ins.rd] = ~(reg_file[ins.rs] & reg_file[ins.rt])


def slt_exe(ins):
    if reg_file[ins.rs] < reg_file[ins.rt]:
        reg_file[ins.rd] = 1
    else:
        reg_file[ins.rd] = 0


def ADD_exe(ins):
    reg_file[ins.rt] = reg_file[ins.rs] + ins.imm


def SUB_exe(ins):
    reg_file[ins.rt] = reg_file[ins.rs] - ins.imm


def MUL_exe(ins):
    reg_file[ins.rt] = reg_file[ins.rs] * ins.imm


def AND_exe(ins):
    reg_file[ins.rt] = reg_file[ins.rs] & ins.imm


def NOR_exe(ins):
    reg_file[ins.rt] = ~(reg_file[ins.rs] & ins.imm)


def SLT_exe(ins):
    if  reg_file[ins.rs] < ins.imm:
        reg_file[ins.rt] = 1
    else:
        reg_file[ins.rt] = 0


def j_exe(ins):
    global pc
    pc = ins.index - 4


def jr_exe(ins):
    global pc
    pc = reg_file[ins.rs] - 4


def beq_exe(ins):
    global pc
    if reg_file[ins.rs] == reg_file[ins.rt]:
        pc += ins.offset


def bltz_exe(ins):
    global pc
    if reg_file[ins.rs] < 0:
        pc += ins.offset


def bgtz_exe(ins):
    global pc
    if reg_file[ins.rs] > 0:
        pc += ins.offset


def lw_exe(ins):
    global data_memory
    global pc
    global data_start_addr
    # print(data_start_addr, len(data_memory), ins.base, ins.offset)
    # print(reg_file[ins.base] )
    reg_file[ins.rt] = data_memory[((reg_file[ins.base] + ins.offset) - data_start_addr)//4]


def sw_exe(ins):
    global data_memory
    global pc
    data_memory[((reg_file[ins.base] + ins.offset) - data_start_addr) // 4] = reg_file[ins.rt]


def sll_exe(ins):
    reg_file[ins.rd] = reg_file[ins.rt] << ins.sa
    # print(ins.sa, ins.rt << ins.sa)


def srl_exe(ins):
    reg_file[ins.rd] = reg_file[ins.rt] >> ins.sa


def sra_exe(ins):
    # reg_file[ins.rd] = reg_file[ins.rt] >> ins.sa
    tmp1 = dec2bin(reg_file[ins.rt])
    tmp2 = '0' * ins.sa
    for i in tmp1[:32-ins.sa]:
        tmp2 += i
    reg_file[ins.rd] = bin2dec(tmp2)



def nop_exe(ins):
    return


def _break_exe(ins):
    return


def simulator(mips_ins, datas):
    global data_memory
    global reg_file
    global pc
    global data_start_addr
    global cycle
    init_addr = 64
    pc = init_addr
    data_start_addr = init_addr + 4 * len(mips_ins)
    ins_end_addr = data_start_addr - 4
    output = ''
    for data in datas:
        data_memory.append(data.value)
    while pc <= ins_end_addr:
        instruction = mips_ins[(pc - init_addr)//4]
        output += exe_instruction(cycle, pc, instruction.format)
        # print(exe_instruction(cycle, pc, instruction.format))
        eval(instruction.name + "_exe")(instruction)
        output += simulate_result(reg_file, data_memory)
        # print(simulate_result(reg_file, data_memory))
        cycle += 1
        pc += 4

    f = open("simulation.txt", 'w')
    f.write(output)
    f.close()

    # print(output)





mips_instructions = []
datas = []
reg_file = [0] * 32
pc = 0
data_memory = []
data_start_addr = 0
cycle = 1

if __name__ == '__main__':
    path = 'sample.txt'
    binary_codes = read_binary_code(path)


    address = 64
    count = 0
    for binary_code in binary_codes:
        mips_instruction = MipsInstruction()
        mips_instruction.addr = address
        mips_instruction.source_code = binary_code
        parse(mips_instruction, binary_code)
        mips_instructions.append(mips_instruction)
        # print(mips_instruction.source_code, mips_instruction.addr, mips_instruction.format)
        address += 4
        count += 1
        if mips_instruction.name == "_break":
            break

    for binary_code in binary_codes[count:]:
        date = Date()
        date.addr = address
        date.source_code = binary_code
        date.value = bin2dec(binary_code)
        datas.append(date)
        address += 4
        # print(date.source_code, date.addr, date.value)

    f = open("disassembly.txt", 'w')
    for ins in mips_instructions:
        bi_code = ins.source_code[0:6] + " " + ins.source_code[6:11] + " " + ins.source_code[11:16] + " " + \
                  ins.source_code[16:21] + " " + ins.source_code[21:26] + " " + ins.source_code[26:32]
        f.write(bi_code + '\t' + str(ins.addr) + '\t' + ins.format + '\n')

    for data in datas:
        f.write(data.source_code + str(data.addr) + '\t' + str(data.value) + '\n')
    f.close()

    simulator(mips_instructions, datas)


