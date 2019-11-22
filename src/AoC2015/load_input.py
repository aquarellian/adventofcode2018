import requests
import pathlib

aoc_session = '53616c7465645f5f26597e0af8a59cd0297bc822a8680a87dfc854d6a1cfb8912fef3ade09c4ee4aa871d8a21c40fc1d'
cookies = {'session': aoc_session}

def save_to_file(txt_content, path):
    with open(path, 'w', newline='') as r:
        for line in txt_content:
            r.write(line)

def load(year, day):
    response = requests.post('https://adventofcode.com/' + str(year) + '/day/' + str(day) + '/input', cookies=cookies)
    save_to_file(response.text, '../../resources/AoC' + str(year) + '/d' + str(day) + '.txt')
    return response.text
