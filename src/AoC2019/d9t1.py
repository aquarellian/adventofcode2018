import opcode
import load_input
content = load_input.load(2019, 9).split(',')
# content=[104,1125899906842624,99]
# content=[109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# content=[1102,34915192,34915192,7,4,7,99,0]
amp = opcode.Amplifier(content)
# amp.apply(1)
#203 low
#2436610492 high
#2436480432
amp.apply(2)