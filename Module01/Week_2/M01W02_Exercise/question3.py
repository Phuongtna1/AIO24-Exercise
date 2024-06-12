# !gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko

import requests


def open_file_from_link(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return print("Failed to open the file from the link")


def count_word(file_link):
    file_content = open_file_from_link(file_link)
    counter = {}
    for word in file_content.lower().split():
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter


file_link = "https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko"
result = count_word(file_link)
assert result['who'] == 3
print(result['man'])
