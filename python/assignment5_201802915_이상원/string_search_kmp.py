# STRING SEARCH: KMP ALGORITHM


def kmp_search(str_pat, str_txt):
    patLen = len(str_pat)
    txtLen = len(str_txt)
    answer = []

    lps = [0] * patLen

    # Preprocess the pattern
    computeLPS(str_pat, lps)

    i = 0
    j = 0
    while i < txtLen:
        if str_pat[j] == str_txt[i]:
            i += 1
            j += 1
        elif str_pat[j] != str_txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == patLen:
            answer.append(i - j)
            j = lps[j - 1]

    return answer


def computeLPS(pat, lps):
    leng = 0

    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng - 1]
            else:
                lps[i] = 0
                i += 1


if __name__ == '__main__':
    str_txt = "AAACABAABBAAACAB"
    str_pat = "AAAC"
    print(kmp_search(str_pat, str_txt))
