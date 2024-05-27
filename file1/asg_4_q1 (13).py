import re


def remove_leading_zeros(ip):
    return re.sub(r'\b0+(\d)', r'\1', ip)


# Example usage:
ip1 = "100.020.003.400"
ip2 = "001.200.001.004"
print(remove_leading_zeros(ip1))  # Output: "100.20.3.400"
print(remove_leading_zeros(ip2))  # Output: "1.200.1.4"
