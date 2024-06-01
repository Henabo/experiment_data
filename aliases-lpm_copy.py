#!/usr/bin/env python

from __future__ import print_function

import argparse
import sys

try:
    import SubnetTree
except Exception as e:
    print(e, file=sys.stderr)
    print("Use `pip install pysubnettree` to install the required module", file=sys.stderr)
    sys.exit(1)


def read_non_aliased(tree, fh):
    return fill_tree(tree, fh, ",0")


def read_aliased(tree, fh):
    return fill_tree(tree, fh, ",1")


def fill_tree(tree, fh, suffix):
    for line in fh:
        line = line.strip()
        try:
            tree[line] = line + suffix
        except ValueError as e:
            print("Skipped line '" + line + "'", file=sys.stderr)
    return tree


def main(aliased_file_path, non_aliased_file_path, experiment_path, seed_id):
    # Store aliased and non-aliased prefixes in a single subnet tree
    tree = SubnetTree.SubnetTree()

    aliased_file = open(aliased_file_path, 'r', encoding='utf-8')
    # non_aliased_file = open(non_aliased_file_path, 'r', encoding='utf-8')

    # Read aliased and non-aliased prefixes
    print("Reading aliased prefixes...")
    tree = read_aliased(tree, aliased_file)
    # print("Reading non-aliased prefixes...")
    # tree = read_non_aliased(tree, non_aliased_file)

    print("Matching IP addresses...")
    # Read IP address file, match each address to longest prefix and print output
    aliased_count, non_aliased_count, dont_know_count = 0, 0, 0
    for experiment in experiment_path:
        save_file_path = experiment + f"inference_nonaliased_{seed_id}.txt"
        ip_address_file = experiment + f"inference_{seed_id}.txt"
        # 非别名地址
        with open(save_file_path, 'w', encoding='utf-8') as file:
            # 别名地址
            with open(ip_address_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    try:
                        # print(line + "," + tree[line])
                        # 将别名地址删除写入其中
                        if tree[line].split(",")[1] == "1":
                            aliased_count += 1
                            # print("别名地址" + line + "-----" + tree[line])
                            # non_aliased_count += 1
                            # file.write(line + "\n")
                        # file.write(line + "-----" + tree[line] + "\n")
                    except KeyError as e:
                        dont_know_count += 1
                        # print("Skipped line '" + line + "'", file=sys.stderr)
    print("别名地址数量：", aliased_count)
    print("非别名地址数量：", non_aliased_count)
    print("不知道地址数量：", dont_know_count)
    print("--------finished!---------")


if __name__ == "__main__":
    seed_id = 1
    # ipaddress_file = f"6Forest/inference_{seed_id}.txt"

    # 真实数据
    aliased_file = "data/aliased-prefixes.txt"
    non_aliased_file = "data/non-aliased-prefixes.txt"

    # # 测试使用数据
    # aliased_file = "test/aliased-prefixes.txt"
    # non_aliased_file = "test/non-aliased-prefixes.txt"

    # 实验路径，目前就两个
    # experiment_path = ["6Forest/", "6Tree/", "DET/", "6Diffusion/"]
    experiment_path = ["6Tree/"]
    main(aliased_file, non_aliased_file, experiment_path, seed_id)
