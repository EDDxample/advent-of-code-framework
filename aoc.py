import requests, os, errno, sys, importlib

def main():
    try:
        _, mode, year, day = sys.argv
        path = f'aoc/{year}/{day}'

        if mode == 'gen': gen_day(year, day)
        if mode == 'run': run_solutions(year, day)


    except ValueError as error:
        print('usage: py aoc.py [gen|run] <year> <day>')



def run_solutions(year, day):
    path = f'aoc/{year}/{day}'
    module = load_source(f'{path}/solution.py')
    puzzle_input = read_file(f'{path}/input.txt')

    print(f'\n--- AOC {year} day {day} ---')
    print('part 1:', module.part1(puzzle_input))
    print('part 2:', module.part2(puzzle_input))
    print()

def gen_day(year, day):
    path = f'aoc/{year}/{day}'
    puzzle_input = get_input(year, day)
    write_file(path+'/input.txt', puzzle_input)
    write_file(path+'/description.txt', f'https://adventofcode.com/{year}/day/{day}')
    write_file(path+'/solution.py', '\ndef part1(puzzle_in):\n\treturn \'not implemented yet\'\n\ndef part2(puzzle_in):\n\treturn \'not implemented yet\'\n')

def get_input(year, day):
    with open('.token') as token:
        return requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={ 'session': token.read() }).text



# utils

def ensure_path(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def read_file(path):
    with open(path) as f:
        return f.read()

def write_file(path, content):
    ensure_path('/'.join(path.split('/')[:-1]))
    with open(path, 'w') as f:
        f.write(content)

def load_source(path):
    # https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
    module_name = path.replace('/', '_').replace('\\', '_').replace('.', '_')
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

if __name__ == '__main__': main()
