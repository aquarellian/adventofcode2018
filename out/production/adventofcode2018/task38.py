ip=2

def emulate_program():
    reg = [1,0,0,0,0,0]
    while True:
        if reg[ip] == 0:
            # addi 2 16 2
            reg[2]+=16
        elif reg[ip] == 1:
            # seti 1 2 4
            reg[4] = 1
        elif reg[ip] == 2:
            # seti 1 8 1
            reg[1] = 1
        elif reg[ip] == 3:
            # mulr 4 1 5
            reg[5] = reg[4] * reg[1]
        elif reg[ip] == 4:
            # eqrr 5 3 5
            reg[5] *= reg[3]
        elif reg[ip] == 5:
            # addr 5 2 2
            reg[2] += reg[5]
        elif reg[ip] == 6:
            # addi 2 1 2
            reg[2]+=1
        elif reg[ip] == 7:
            # addr 4 0 0
            reg[0] += reg[4]
        elif reg[ip] ==8:
            # addi 1 1 1
            reg[1]+=1
        elif reg[ip] == 9:
            # gtrr 1 3 5
            reg[5] = (1 if reg[1] > reg[3] else 0)
        elif reg[ip] == 10:
            # addr 2 5 2
            reg[2] += reg[5]
        elif reg[ip] == 11:
            # seti 2 6 2
            reg[2] = 2
        elif reg[ip] == 12:
            #addi 4 1 4
            reg[4] +=4
        elif reg[ip] == 13:
            #gtrr 4 3 5
            reg[5] = (1 if reg[4] > reg[5] else 0)
        elif reg[ip] == 14:
            #addr 5 2 2
            reg[2] += reg[5]
        elif reg[ip] == 15:
            #seti 1 2 2
            reg[2] = 1
        elif reg[ip] == 16:
            #mulr 2 2 2
            reg[2] *= reg[2]
        elif reg[ip] == 17:
            #addi 3 2 3
            reg[3] +=2
        elif reg[ip] == 18:
            #mulr 3 3 3
            reg[3]*=reg[3]
        elif reg[ip] == 19:
            #mulr 2 3 3
            reg[3] *=reg[2]
        elif reg[ip] == 20:
            #muli 3 11 3
            reg[3] *= 11
        elif reg[ip] == 21:
            #addi 5 2 5
            reg[5] += 2
        elif reg[ip] == 22:
            #mulr 5 2 5
            reg[5] *= reg[2]
        elif reg[ip] == 23:
            #addi 5 8 5
            reg[5] += 5
        elif reg[ip] == 24:
            #addr 3 5 3
            reg[3] += reg[5]
        elif reg[ip] == 25:
            #addr 2 0 2
            reg[2] += reg[0]
        elif reg[ip] == 26:
            #seti 0 4 2
            reg[2] = 0
        elif reg[ip] == 27:
            #setr 2 5 5
            reg[5] += reg[2]
        elif reg[ip] == 28:
            #mulr 5 2 5
            reg[5] *= reg[2]
        elif reg[ip] == 29:
            #addr 2 5 5
            reg[5] += reg[2]
        elif reg[ip] == 30:
            #mulr 2 5 5
            reg[5] *= reg[2]
        elif reg[ip] == 31:
            #muli 5 14 5
            reg[5]*=14
        elif reg[ip] == 32:
            #mulr 5 2 5
            reg[5] *=reg[2]
        elif reg[ip] == 33:
            #addr 3 5 3
            reg[3]+=reg[5]
        elif reg[ip] == 34:
            #seti 0 8 0
            reg[0] = 0
        elif reg[ip] == 35:
             #seti 0 5 2
            reg[2] = 0
        else:
            print(reg[0])
            break
        reg[ip] += 1
        print(reg)


emulate_program()





