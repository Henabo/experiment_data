import ipaddress


def convert_ipv6_to_expanded(ipv6_address):
    """
    将IPv6地址转换为展开格式，并去除其中的冒号。
    """
    try:
        ipv6_obj = ipaddress.IPv6Address(ipv6_address).exploded
        expanded_ipv6 = str(ipv6_obj)
        # 去除IPv6地址中的冒号
        expanded_ipv6 = expanded_ipv6.replace(':', '')
        return expanded_ipv6
    except ipaddress.AddressValueError:
        print(f"Invalid IPv6 address: {ipv6_address}")
        return None


# 32位 十六进制
def count_ipv6_prefixes(file_path, prefix_length=64):
    """
    读取文件中的IPv6地址，转换为展开格式，并统计具有指定前缀长度的地址数量。
    """
    # ipv6是128位，十六进制表示则是32位，因此除以4
    prefix_length = prefix_length / 4
    expanded_ipv6_set = set()
    with open(file_path, 'r') as file:
        for line in file:
            ipv6_address = line.strip()
            expanded_ipv6 = convert_ipv6_to_expanded(ipv6_address)
            if expanded_ipv6:
                # 检查是否为指定长度的前缀
                ipv6_prefix = expanded_ipv6[:int(prefix_length)]
                expanded_ipv6_set.add(ipv6_prefix)
    return expanded_ipv6_set


if __name__ == "__main__":
    # 调用函数，传入你的txt文件路径和前缀长度
    file_path = '6Tree/gen_1.txt'  # 替换为你的文件路径
    prefixes_length = [32, 48, 64, 96]  # 可以设置为其他值，比如32, 48, 64等，必须是4的倍数
    seed_path = "seed/seed_1.txt"
    for prefix_length in prefixes_length:
        seed_prefix = count_ipv6_prefixes(seed_path, prefix_length)
        ipv6_prefixes = count_ipv6_prefixes(file_path, prefix_length)
        new_ipv6_prefixes = ipv6_prefixes - seed_prefix
        print(f"Number of IPv6 addresses with /{prefix_length} prefix: {len(new_ipv6_prefixes)}")
