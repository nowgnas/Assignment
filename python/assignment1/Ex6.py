# Assignment 1, Exercise 6

def check_list(data):
    # Write code here!
    data_out = []
    for i in range(0, len(data) - 3):
        is_unique = data[i:i + 4]
        list_set = set(is_unique)
        if len(list_set) == len(is_unique):
            data_out = is_unique
            '''
            if find all unique set:
            data_out.append(is_unique)
            '''
            break  # find first unique set

    return data_out


'''
unique set은 2개가 존재 하지만, 결과 예시에는 하나의 set만 있어 
최초의 unique set을 출력하는 것으로 이해하고 구현 하였습니다．
'''
# Test
data_in = [1, -1, 0, 1, 0, 0, 2, 1, -1, 0]
data_out = check_list(data_in)
print(data_out)
