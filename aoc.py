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
    result, ms = time_function(puzzle_input, module.part1)
    print(f'part 1: {result} {ms:.3f}ms')
    result, ms = time_function(puzzle_input, module.part2)
    print(f'part 2: {result} {ms:.3f}ms')
    try:
        result, ms = time_function(puzzle_input, module.faster_part1)
        print(f'faster part 1: {result} {ms:.3f}ms')
    except: pass
    try:
        result, ms = time_function(puzzle_input, module.faster_part2)
        print(f'faster part 2: {result} {ms:.3f}ms')
    except: pass
    print()

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

def time_function(puzzle_input, fun):
    t0 = time.perf_counter()
    x = fun(puzzle_input)
    t1 = time.perf_counter()
    return x, (t1 - t0) * 1000

if __name__ == '__main__': main()
