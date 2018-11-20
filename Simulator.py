
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
    reg_file[ins.rd] = reg_file[ins.rt] >> ins.sa


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


