import load_input
content = load_input.load(2015, 2)
sum = 0
for line in content.split('\n'):
    print(line)
    nums = line.split('x')
    if len(nums) == 3:
        s1 = int(nums[0]) * int(nums[1])
        s2 = int(nums[0]) * int(nums[2])
        s3 = int(nums[2]) * int(nums[1])
        smin = min(s1,s2,s3)
        sum += 2*s1 + 2*s2 + 2*s3 + smin
print(sum)


