import requests
import os
import sys
import importlib
import importlib.util
from typing import Any, Optional, Callable
import time


class SolutionModule:
    part1:        Callable
    part2:        Callable
    faster_part1: Callable
    faster_part2: Callable


class AOCFramework:
    def __init__(self, year: int, day: int) -> None:
        self.year = year
        self.day = day
        self._base_folder = f"aoc/{year}/{day:02d}"
        self._problem_url = f"https://adventofcode.com/{year}/day/{day}"

    def gen_day(self):
        """
        Generates the file structure for the current day / year
        """
        os.makedirs(self._base_folder, exist_ok=True)

        with (
            open(self._base_folder + "/example.txt", "w") as example_file,
            open(self._base_folder + "/input.txt", "w") as input_file,
            open(self._base_folder + "/solution.py", "w") as solution_file,
        ):
            example_text, input_text, solution_template = self._load_file_contents()
            example_file.write(example_text)
            input_file.write(input_text)
            solution_file.write(solution_template)
        print('problem description:', self._problem_url)

    def run_solutions(self):
        """
        Loads the solution source and executes the answers
        """
        with (
            open(self._base_folder + '/input.txt') as input_file,
            open(self._base_folder + '/example.txt') as example_file,
        ):
            if module := self._load_source(self._base_folder + '/solution.py'):
                puzzle_input = input_file.read()
                example = example_file.read()

                print(f'\n--- AOC {self.year} day {self.day} ---')
                self._try_solution((puzzle_input, example), module.part1, 'part 1\t')
                self._try_solution((puzzle_input, example), module.part2, 'part 2\t')
                self._try_solution((puzzle_input, example), module.faster_part1, 'faster part 1')
                self._try_solution((puzzle_input, example), module.faster_part2, 'faster part 2')
                print()

    def _try_solution(self, parameters, fun, name):
        """
        Attempts to load and time the given solution
        """
        try:
            t0 = time.perf_counter()
            result = fun(*parameters)
            t1 = time.perf_counter()
            ms = (t1 - t0) * 1000
            print(f'{name}\t{result}\t{ms:.3f}ms')
        except BaseException as err:
            if name[0] != 'f':
                print(err)

    def _load_token(self) -> str:
        """
        Attempts to load the session token from the .token file
        """
        if not os.path.exists('.token'):
            raise Exception("Missing .token file")

        with open('.token') as tokenfile:
            if token := tokenfile.read():
                return token
            else:
                raise Exception("Invalid Token")

    def _load_file_contents(self) -> tuple[str, str, str]:
        """
        Returns the scraped example/input pages and the solution template
        """
        token = self._load_token()
        input_text = requests.get(self._problem_url + "/input", cookies={'session': token}).text
        example_text = requests.get(self._problem_url).text

        try:
            example_text = example_text.split('<pre><code>')[1].split('</code></pre>')[0]
        except:
            example_text = ''

        with open('solution_template.txt') as template:
            solution_template = template.read()

        return example_text, input_text, solution_template

    def _load_source(self, module_path: str) -> Optional[SolutionModule]:
        """
        Reads the solution's source file and returns it as a python module
        """
        module_name = module_path.replace('/', '_').replace('\\', '_').replace('.', '_')
        if spec := importlib.util.spec_from_file_location(module_name, module_path):
            module: Any = importlib.util.module_from_spec(spec)
            if spec.loader:
                spec.loader.exec_module(module)
            return module


def main():
    try:
        _, mode, year, day = sys.argv
        aoc_framework = AOCFramework(int(year), int(day))

        if mode == 'gen':
            aoc_framework.gen_day()
        elif mode == 'run':
            aoc_framework.run_solutions()

    except ValueError as error:
        print(f'{error}\nusage: py aoc.py [gen|run] <year> <day>')


if __name__ == '__main__':
    main()
