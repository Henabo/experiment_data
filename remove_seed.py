import ipaddress


def read_ip_addresses(file_path):
    """读取文件中的IP地址并返回一个集合"""
    with open(file_path, 'r', encoding='utf-8') as file:
        ip_addresses = {ipaddress.ip_address(line.strip()).exploded for line in file}
    return ip_addresses


def filter_ip_addresses(seed_set, ip_set):
    """过滤掉在seed_set中的IP地址"""
    return ip_set - seed_set


def write_ip_addresses(ip_addresses, output_file_path):
    """将IP地址写入输出文件"""
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for ip in sorted(ip_addresses):
            file.write(f"{ip}\n")


def main(seed_file_path, input_file_path, output_file_path):
    # 读取种子集合和输入IP地址集合
    seed_set = read_ip_addresses(seed_file_path)
    ip_set = read_ip_addresses(input_file_path)

    # 过滤掉seed集合中的IP地址
    filtered_ips = filter_ip_addresses(seed_set, ip_set)

    # 将结果写入输出文件
    write_ip_addresses(filtered_ips, output_file_path)
    print(f"生成的新文件已写入 {output_file_path}")


if __name__ == "__main__":
    seed_file = 'seed/seed_1.txt'  # 种子集合文件路径
    input_file = 'entropy/active_standardized_active_inference_1.txt'  # 输入文件路径
    output_file = 'entropy/gen_1.txt'  # 输出文件路径
    main(seed_file, input_file, output_file)
