"""
https://adventofcode.com/2022/day/18
"""


def read_lines() -> list[list[int]]:
    with open("input.txt") as f:
        lines = [list(map(int, line.split(","))) for line in f.readlines()]

    return lines


def solution(lines: list[list[int]]):
    for _ in lines:
        pass


def main():
    lines = read_lines()
    sol = solution(lines)

    print(sol)
