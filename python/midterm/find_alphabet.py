def solution(alpha: str):
    counted = []
    out_dict = {}
    for i in alpha:
        if i not in counted:
            out_dict[i] = alpha.index(i)
            counted.append(i)
    sort_dict = sorted(out_dict.items(), key=lambda x: x[0])
    for _alpha, _idx in sort_dict:
        print(f'[{_alpha}]: {_idx} ', end='')


if __name__ == '__main__':
    _input = 'inchoen'
    solution(_input)
