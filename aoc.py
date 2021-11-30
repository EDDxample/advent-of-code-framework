import requests, os, errno, sys, importlib, time

def main():
    try:
        _, mode, year, day = sys.argv
        if mode == 'gen': gen_day(year, day)
        if mode == 'run': run_solutions(year, day)


    except ValueError as error:
        print(f'{error}\nusage: py aoc.py [gen|run] <year> <day>')



def run_solutions(year, day):
    path = f'aoc/{year}/{int(day):02}'
    module = load_source(f'{path}/solution.py')
    puzzle_input = read_file(f'{path}/input.txt')

    print(f'\n--- AOC {year} day {day} ---')
    t0 = time.time()
    x = module.part1(puzzle_input)
    t1 = time.time()
    print(f'part 1: {x} {((t1 - t0) * 1000):.3f}ms')
    t0 = time.time()
    x = module.part2(puzzle_input)
    t1 = time.time()
    print(f'part 2: {x} {((t1 - t0) * 1000):.3f}ms')
    try:
        t0 = time.time()
        x = module.faster_part1(puzzle_input)
        t1 = time.time()
        print(f'faster part 1: {x} {((t1 - t0) * 1000):.3f}ms')
        t0 = time.time()
        x = module.faster_part2(puzzle_input)
        t1 = time.time()
        print(f'faster part 2: {x} {((t1 - t0) * 1000):.3f}ms')
        print()
    except: pass

def gen_day(year, day):
    path = f'aoc/{year}/{int(day):02}'
    write_file(path+'/input.txt', get_input(year, day))
    # write_file(path+'/description.md', get_description(year, day))
    write_file(path+'/solution.py', '\ndef part1(puzzle_in: str):\n\treturn \'not implemented yet\'\n\ndef part2(puzzle_in: str):\n\treturn \'not implemented yet\'\n\ndef faster_part1(puzzle_in: str):\n\traise \'not implemented yet\'\n\ndef faster_part2(puzzle_in: str):\n\traise \'not implemented yet\'\n')
    print(f'problem description: https://adventofcode.com/{year}/day/{day}')

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
