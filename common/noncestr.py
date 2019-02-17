import random



def calc_noncestr():
    """
    随机生成一个16位字符串作为参数noncestr
    :return: 生成的参数noncestr值
    """
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(16):
        sa.append(random.choice(seed))
    return ''.join(sa)


if __name__ == '__main__':

    print(calc_noncestr())