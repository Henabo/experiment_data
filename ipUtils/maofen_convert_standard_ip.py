import ipaddress

# 假设你的文件名为 'input_ipv6_addresses.txt'
input_file = "entropy/active_inference_1.txt"
output_file = 'entropy/active_standardized_active_inference_1.txt'



# 读取原始IPv6地址并写入标准化后的IPv6地址
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # 移除行尾的换行符
        address = line.strip()
        # 尝试将字符串转换为IPv6地址对象
        try:
            # 转换为IPv6地址对象
            ip = ipaddress.ip_address(address)
            # 转换为全扩展形式的IPv6地址
            standardized_address = ip.exploded
            # 检查地址是否以'0000'结尾
            if not standardized_address.endswith('0000'):
                # 写入文件
                outfile.write(standardized_address + '\n')
        except ValueError as e:
            # 如果地址无效，打印错误信息
            print(f"Error processing address {address}: {e}")

print("IPv6 addresses have been standardized and written to", output_file)