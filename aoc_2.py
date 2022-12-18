"""
https://adventofcode.com/2022/day/2

A - Rock
B - Paper
C - Scissors 

X - Rock
Y - Paper
Z - Scissors

"""
import enum


POINTS = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

HIERARCHY = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

REV_HIERARCHY = {
    "X": "C",
    "Y": "A",
    "Z": "B"
}


class Result(enum.Enum):
    WIN = 6
    LOSE = 0
    TIE = 3


def read_lines() -> list[str]:
    with open("input.txt") as f:
        lines = list(f.readlines())
    
    return [
        "".join(line.split()) for line in lines
    ]


def get_result(opponent: str, you: str) -> Result:
    if HIERARCHY[opponent] == you:
        return Result.LOSE
    elif REV_HIERARCHY[you] == opponent:
        return Result.WIN 
    return Result.TIE


def get_score(lines: list[str]) -> int:
    total_score = 0
    for line in lines:
        shape_points = POINTS[line[1]]
        res = get_result(*line)
        total_score += shape_points + res.value
    return total_score



def main():
    lines = read_lines()
    score = get_score(lines)

    print(score)


if __name__ == "__main__":
    main()



