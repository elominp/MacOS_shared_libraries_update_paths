#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from sys import argv
from os import system


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage :", argv[0], "binary_table_file")
        exit()
    with open(argv[1], "r") as binary_table_file:
        for line in binary_table_file.readlines():
            binary_file, dynamic_lib = line.split("=")
            binary_file = binary_file.strip()
            dynamic_lib = dynamic_lib.strip()
            old_path, new_path = dynamic_lib.split("->")
            old_path = old_path.strip()
            new_path = new_path.strip()
            system("install_name_tool -change " + old_path + " " + new_path + " " + binary_file)
