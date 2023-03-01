from requests import get
from zipfile import ZipFile
from os import mkdir, remove
from pathlib import Path

class UnihanDatabase():
    def __init__(self):
        """
        Downloads files from Unihan database and parses it.
        """
        zip_filename, folder_name = 'Unihan.zip', 'files'
        mkdir(folder_name)
        print('UnihanDatabase: Downloading zip file...')
        with open(zip_filename, 'wb') as file:
            content = get(f'http://www.unicode.org/Public/UNIDATA/{zip_filename}').content
            file.write(content)
            ZipFile(zip_filename).extractall(path=folder_name)
        remove(zip_filename)
        characters = {}
        print('UnihanDatabase: Reading files...')
        for filename in Path().glob('files/*.txt'):
            with open(filename, 'r') as file:
                content = file.readlines()
                for line in content:
                    if line[0] == '#' or line[0] == '\n': continue
                    split = line.split('\t')
                    character = chr(int(split[0][1:], 16))
                    if character not in characters: characters[character] = {}
                    characters[character][split[1]] = split[2:][0].rstrip('\n')
        self.database = characters
        print('UnihanDatabase: Ready')
