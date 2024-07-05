"""SwapVar"""
def convert_string(info):
    """SwapVar"""
    in_info = info.strip('()').split(', ')
    return tuple(map(float, in_info))

    # keep = reversed(in_info)
    # print(keep)

print(tuple(reversed(list(convert_string(input())))))
