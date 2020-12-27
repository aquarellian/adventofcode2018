# key_pub_key = 5764801
# door_pub_key = 17807724

key_pub_key = 13316116
door_pub_key = 13651422

sub_num = 7
val = 1
key_loop_size = 0
i = 0
while True:
    i+=1
    val = val * sub_num % 20201227
    if val == key_pub_key:
        key_loop_size = i
        break
print(key_loop_size)

val = 1
door_loop_size = 0
i = 0
while True:
    i+=1
    val = val * sub_num % 20201227
    if val == door_pub_key:
        door_loop_size = i
        break
print(door_loop_size)

val = 1
for i in range(1, key_loop_size +1):
    val = val * door_pub_key % 20201227
print(val)

val = 1
for i in range(1, door_loop_size +1):
    val = val * key_pub_key % 20201227
print(val)

