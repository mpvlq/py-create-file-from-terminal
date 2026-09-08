# write your code here
import sys
import os
from datetime import datetime
from typing import TextIO


def add_content(output_file: TextIO) -> None:
    content = ""
    i = 1

    while content != "stop":
        content = input("Enter content line: ")

        if content != "stop":
            output_file.write(str(i) + " " + content + "\n")
        i += 1


def create_file() -> None:
    file_name = sys.argv[sys.argv.index("-f") + 1]

    if os.path.exists(file_name):
        with open(file_name, "a") as output_file:
            output_file.write(
                "\n" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            add_content(output_file)
    else:
        with open(file_name, "w") as output_file:
            output_file.write(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            add_content(output_file)


def create_directory(border: int) -> None:
    path = os.path.join(
        os.getcwd(), *sys.argv[sys.argv.index("-d") + 1: border])
    os.makedirs(path)
    os.chdir(path)


if "-f" in sys.argv and "-d" in sys.argv:
    create_directory(sys.argv.index("-f"))
    create_file()
elif "-f" in sys.argv:
    create_file()
elif "-d" in sys.argv:
    create_directory(len(sys.argv))
