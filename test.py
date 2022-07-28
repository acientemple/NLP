def arrangement(a, b):  # a代表取多少元素，b代表总共多少元素
    """排列"""
    result = 1  # 设置中间量
    for i in range(a):  # 经典for循环，从0到a每次使中间量乘b，b再减1
        result *= b
        b -= 1
    return result
def combination(a,b):
    return (arrangement(a,b)/arrangement(a,a))