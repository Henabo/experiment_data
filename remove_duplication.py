import ipaddress

def read_ip_addresses(file_path):
    """读取文件中的IP地址"""
    with open(file_path, 'r', encoding='utf-8') as file:
        ip_addresses = {line.strip() for line in file}
    return ip_addresses

def write_unique_ip_addresses(ip_addresses, output_file_path):
    """将唯一的IP地址写入输出文件"""
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for ip in sorted(ip_addresses):
            file.write(f"{ip}\n")

def main(input_file_path, output_file_path):
    ip_addresses = read_ip_addresses(input_file_path)
    unique_ip_addresses = {ipaddress.ip_address(ip) for ip in ip_addresses}
    write_unique_ip_addresses(unique_ip_addresses, output_file_path)
    print(f"去重后的IP地址已写入 {output_file_path}")

if __name__ == "__main__":

    input_file = '6Tree/inference_1.txt'  # 输入文件路径
    output_file = '6Tree/unique_ipv6.txt'  # 输出文件路径
    main(input_file, output_file)
