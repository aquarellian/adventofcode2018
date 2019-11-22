import load_input
content = load_input.load(2015, 2)
# content = '1x1x10'
sum = 0
for line in content.split('\n'):
    print(line)
    nums = line.split('x')
    if len(nums) == 3:
        n = [int(nums[0]), int(nums[1]), int(nums[2])]
        s1 = 2 * (n[0] + n[1])
        s2 = 2 * (n[1] + n[2])
        s3 = 2 * (n[2] + n[0])
        smin = min(s1,  s2, s3)
        # print(smin)
        v = n[0] * n[1] * n[2]
        # print(v)
        sum += smin + v
print(sum)
