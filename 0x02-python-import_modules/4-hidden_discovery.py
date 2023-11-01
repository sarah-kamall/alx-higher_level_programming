#!/usr/bin/python3
import hidden_4
def main():
    allnames = dir(hidden_4)
    filtered_names = [name for name in all_names if not name.startswith("__")]
    filtered_names.sort()
    for name in filtered_names:
        print(name)
if __name__ == "main":
    main()

