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
    example = read_file(f'{path}/example.txt')

    print(f'\n--- AOC {year} day {day} ---')
    try_solution((puzzle_input, example), module.part1, 'part 1\t')
    try_solution((puzzle_input, example), module.part2, 'part 2\t')
    try_solution((puzzle_input, example), module.faster_part1, 'faster part 1')
    try_solution((puzzle_input, example), module.faster_part2, 'faster part 2')
    print()

def gen_day(year, day):
    path = f'aoc/{year}/{int(day):02}'
    write_file(path+'/input.txt', get_input(year, day))
    
    write_file(path+'/example.txt', get_example(year, day))
    
    write_file(path+'/solution.py', 'import re\n\ndef part1(s: str, ex: str):\n\ts = ex # example mode\n\tfor line in s.splitlines():\n\t\tpass\n\treturn \'not implemented yet\'\n\ndef part2(s: str, ex: str):\n\treturn \'not implemented yet\'\n\ndef faster_part1(s: str, ex: str):\n\traise \'not implemented yet\'\n\ndef faster_part2(s: str, ex: str):\n\traise \'not implemented yet\'\n')
    print(f'problem description: https://adventofcode.com/{year}/day/{day}')

def get_input(year, day):
    with open('.token') as token:
        return requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={ 'session': token.read() }).text

def get_example(year, day):
    try:
        page = requests.get('https://adventofcode.com/2021/day/4').text
        return page.split('<pre><code>')[1].split('</code></pre>')[0]
    except:
        return ''
# utils

def ensure_path(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def read_file(path):
    fp = open(path)
    data = fp.read()
    fp.close()
    return data

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

def try_solution(parameters, fun, name):
    try:
        t0 = time.perf_counter()
        result = fun(*parameters)
        t1 = time.perf_counter()
        ms = (t1 - t0) * 1000
        print(f'{name}\t{result}\t{ms:.3f}ms')
    except BaseException as err:
        if name[0] != 'f':
            print(err)


if __name__ == '__main__': main()
