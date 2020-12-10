import requests

aoc_session = '53616c7465645f5fa22f484a9b3c0e37c5f51f0ed60a1201070e4f4e957ef2f8e9ef02eb0f44632cc284414d78a2204a'
cookies = {'session': aoc_session}

def save_to_file(txt_content, path):
    with open(path, 'w') as r:
        for line in txt_content:
            r.write(line)

def load(year, day):
    response = requests.post('https://adventofcode.com/' + str(year) + '/day/' + str(day) + '/input', cookies=cookies)
    save_to_file(response.text, '../../resources/AoC' + str(year) + '/d' + str(day) + '.txt')
    return response.text
