from langconv import *

file_path = "wiki_00"
simplified_version = 'simple.txt'
simple_file = open(simplified_version, 'w+', encoding='utf8')

idx = 0
with open(file_path, 'r', encoding='utf8') as file:
    new_contents = ''
    for line in file:
        line = line.strip()
        print(line)
        idx += 1
        simplified_line = Converter('zh-hans').convert(line)
        print(simplified_line)
        new_contents += simplified_line

    simple_file.write(new_contents)

simple_file.close()


# transform traditional to simplified
