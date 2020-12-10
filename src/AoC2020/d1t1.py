# import load_input
# content = load_input.load(2020, 1)

with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d1.txt") as f:
    content = f.readlines()


    for line1 in content: #content.split('\n'):
        for line2 in content: #content.split('\n'):
            if line1 != '' and line2 != ''   and int(line1) + int(line2) == 2020:
                print(line1, ' ', line2, ' ',  int(line1) * int(line2) )

            # for line3 in content: #content.split('\n'):
            #     if line1 != '' and line2 != '' and line3 != '' and int(line1) + int(line2) + int(line3) == 2020:
            #         print(line1, ' ', line2, ' ', line3, ' ', int(line1) * int(line2) * int(line3))
