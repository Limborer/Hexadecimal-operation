def num2scale_list(num: int, scale: int):
    """
    将十进制数字转换为进制列表
    num = result[i]*scale^(len(result)-i) for i in range(len(result))
    :param num: 十进制数字
    :param scale: 待转换的进制数值
    :return: 进制列表，从前至后位数以此递减
    """
    result = []
    while num > scale:
        result.append(num % scale)
        num = num // scale
    result.append(num)
    result = result[::-1]
    return result


def scale_list2num(scale_list: list, scale: int):
    """
    进制列表转十进制数字
    :param scale_list: 进制列表
    :param scale: 进制数值
    :return: 转换后的十进制数字
    """
    result = 0
    scale_list_len = len(scale_list)
    for i in range(scale_list_len):
        result += scale_list[i] * (scale**(scale_list_len - i))
    return result


def scale_list_add_same_scale(scale1: list, scale2: list, scale: int):
    """
    同进制的两个进制列表相加
    :param scale1: 进制列表1
    :param scale2: 进制列表2
    :param scale: 进制数
    :return: 相加进制列表结果
    """
    max_len = max(len(scale1), len(scale2))
    result = []
    while len(scale1) < max_len:
        scale1.insert(0, 0)
    while len(scale2) < max_len:
        scale2.insert(0, 0)
    for i in range(max_len-1, -1, -1):
        current_value = scale1[i] + scale2[i]
        if i != 0:
            if current_value >= scale:
                scale1[i-1] += 1
                result.append(current_value - scale)
            else:
                result.append(current_value)
        else:
            if current_value >= scale:
                result.append(current_value - scale)
                result.append(1)
            else:
                result.append(current_value)
    return result[::-1]


def scale_list_add(scale_list1: list, scale_list2: list, scale1: int, scale2: int, scale: int):
    """
    不同进制的进制列表相加
    1.将两个进制列表转为十进制的数字
    2.将转换后的十进制数字相加
    3.将相加结果转为进制列表
    :param scale_list1: 待相加的进制列表1
    :param scale_list2: 待相加的进制列表2
    :param scale1: 进制列表1的进制数值
    :param scale2: 进制列表2的进制数值
    :param scale: 转换结果的进制数值
    :return: 转换后的进制列表
    """
    scale_list1_num = scale_list2num(scale_list1, scale1)
    scale_list2_num = scale_list2num(scale_list2, scale2)
    result = scale_list1_num + scale_list2_num
    return num2scale_list(result, scale)


def scale_update(scale_list: list, scale: int):
    """
    逐位检查进制列表是否存在溢出。
    若存在溢出，则进位。
    :param scale_list: 待检测的进制列表。
    :param scale: 进制数值。
    :return: update的进制列表。
    """
    if scale_list[-1] >= scale:
        if len(scale_list) == 1:
            return [1, 0]
        else:
            for i in range(len(scale_list)-1, -1, 0):
                if scale_list[i] >= scale:
                    if i != 0:
                        scale_list[i - 1] += 1
                        scale_list[i] -= scale
                    else:
                        scale_list.insert(0, 1)
    return scale_list
