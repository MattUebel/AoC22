import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    # two arguments, a day number and the advent of code challenge name
    parser.add_argument("day", type=str, help="day number")
    parser.add_argument("challenge", type=str, help="challenge name")
    args = parser.parse_args()

    # create a directory for the day
    os.mkdir(f"day{args.day}")
    # create a file for the challenge
    with open(f"day{args.day}/{args.challenge}.py", "w") as f:
        f.write(f"# Path: day{args.day}/{args.challenge}.py")

    # create a file for the challenge's tests
    # an empty file named test.txt
    with open(f"day{args.day}/test.txt", "w") as f:
        pass

    # same for input.txt
    with open(f"day{args.day}/input.txt", "w") as f:
        pass

    # init a jupyter notebook
    with open(f"day{args.day}/{args.challenge}.ipynb", "w") as f:
        pass

    # create a README.md file
    with open(f"day{args.day}/README.md", "w") as f:
        f.write(f"# Day {args.day} - {args.challenge}")


if __name__ == "__main__":
    main()
