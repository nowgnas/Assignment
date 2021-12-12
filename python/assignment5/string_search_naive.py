# STRING SEARCH: NAIVE (BRUTE-FORCE) METHOD

def naive_search(str_pat, str_txt):
    # Write code here!
    pat_length = len(str_pat)
    txt_length = len(str_txt)

    for idx in range(txt_length - pat_length):
        for _idx in range(pat_length):
            if str_pat[idx + _idx] == str_pat[_idx]:
                _idx += 1
            else:
                print(_idx)
                print(idx)
                break
        break


if __name__ == '__main__':
    str_txt = "AAACABAABBAAACAB"
    str_pat = "AAAC"
    naive_search(str_pat, str_txt)
