
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
    mips_ins.format = "J " + " #" + str(mips_ins.index)


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