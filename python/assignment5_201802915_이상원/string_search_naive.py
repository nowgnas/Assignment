# STRING SEARCH: NAIVE (BRUTE-FORCE) METHOD

def naive_search(str_pat, str_txt):
    # Write code here!
    answer = []
    for i in range(len(str_txt) - len(str_pat) + 1):
        if str_txt[i:i + len(str_pat)] == str_pat:
            answer.append(i)
    print(answer)


if __name__ == '__main__':
    str_txt = "AAACABAABBAAACAB"
    str_pat = "AAAC"
    naive_search(str_pat, str_txt)
