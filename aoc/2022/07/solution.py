import re
from dataclasses import dataclass
from collections import defaultdict
from typing import TypedDict


class File(TypedDict):
    name: str
    length: int


def save_to_cwd(cwd: str, tree, data):
    if keys := cwd.split('/'):
        temp = tree.get('/')
        for key in keys[:-1]:
            temp = temp.get(key)
        temp[keys[-1]] = data
    else:
        tree['/'] = data


def part1(s: str, ex: str):
    # s = ex  # example mode

    cwd: str = '/'

    filetree = defaultdict(list[File])

    for line in s.splitlines():
        if line.startswith('$ cd'):
            if line[5:] == '..':
                if cwd == '/':
                    print('WTF')
                else:
                    cwd = '/'.join(cwd.split('/')[:-1])
            elif line[5:] == '/':
                cwd = '/'
            else:
                cwd = cwd.removesuffix('/') + '/' + line[5:]

        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir'):
            pass
        else:
            length, name = line.split(' ')
            filetree[cwd].append(File(name=name, length=int(length)))

    count = 0
    count_by_directory = defaultdict(int)
    for key in filetree:
        directory_count = 0
        for file in filetree[key]:
            directory_count += file['length']

        prev = ''
        for parent in key.split('/'):
            prev = prev.removesuffix('/') + '/' + parent
            count_by_directory[prev] += directory_count

    for directory in count_by_directory:

        if count_by_directory[directory] <= 100000:
            count += count_by_directory[directory]
    return count


def part2(s: str, ex: str):
    # s = ex  # example mode

    cwd: str = '/'

    filetree = defaultdict(list[File])

    for line in s.splitlines():
        if line.startswith('$ cd'):
            if line[5:] == '..':
                if cwd == '/':
                    print('WTF')
                else:
                    cwd = '/'.join(cwd.split('/')[:-1])
            elif line[5:] == '/':
                cwd = '/'
            else:
                cwd = cwd.removesuffix('/') + '/' + line[5:]

        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir'):
            pass
        else:
            length, name = line.split(' ')
            filetree[cwd].append(File(name=name, length=int(length)))

    count = 0
    count_by_directory = defaultdict(int)
    for key in filetree:
        directory_count = 0
        for file in filetree[key]:
            directory_count += file['length']

        prev = ''
        for parent in key.split('/'):
            prev = prev.removesuffix('/') + '/' + parent
            count_by_directory[prev] += directory_count

    total = 70000000
    needs = 30000000
    used = count_by_directory['/']
    free = total - used
    needed = needs - free

    items = list(sorted(count_by_directory.items(), key=lambda k: k[1]))

    for key, val in items:
        if val >= needed:
            return val


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')
