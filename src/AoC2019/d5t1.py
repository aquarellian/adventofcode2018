import opcode
import load_input
content = load_input.load(2019, 5).split(',')

# opcode.apply([1002,4,3,4,33])
# opcode.apply(content, 1)
opcode.apply(content, 5)
# opcode.apply([3,3,1107,-1,8,3,4,3,99], 700)

