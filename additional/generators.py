import os

def populate_file(filename):
    values_to_write = ['hello', 'line2', 'line3', 'and so on']
    with open(filename, 'w') as out:
        for value in values_to_write:
            out.write(value)
            out.write('\n')


def read_file(filename):
    # data = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            yield line
            # data.append(line)
    # return data


filename = 'sample.txt'
# file_content = (line for line in open(filename, 'r'))
# print(file_content)


# populate_file('sample.txt')
# file_content = read_file(filename)
# print(file_content)
#
# for line in file_content:
#     print(line)

def read_if_exists(filename):
    if os.path.isfile(filename):
        yield from read_file(filename)
    return []

file_content = read_if_exists(filename+'2')

print(file_content)

for line in file_content:
    print(line)