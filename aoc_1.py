def read_input() -> list[int]:
    inp = []
    current_elf_cals = []
    with open("input.txt") as f:
        for line in f.readlines():
            if line == "\n":
                inp.append(sum(current_elf_cals))
                current_elf_cals.clear()
                continue
            current_elf_cals.append(int(line))

    return inp

def main():
    inp = read_input()
    inp.sort()
    print(sum(inp[-3:]))

if __name__ == "__main__":
    main()

