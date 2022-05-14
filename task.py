# def test_case1(cards):
#     int_list = sorted([x for x in cards if type(x) == int])
#     str_list = sorted([x for x in cards if type(x) == str])
#     king = str_list[1]
#     str_list.remove(king)
#     str_list.insert(2, king)
#     sorted_cards = int_list + str_list
#     print(f"TEST CASE 1 = {sorted_cards}")
# test_case1(['Jack', 8, 2, 6, 'King', 5, 3, 'Queen'])



# def test_case2(cards):
#     int_list = sorted([x for x in cards if type(x) == int])
#     str_list = sorted([x for x in cards if type(x) == str])
#     for x in str_list:
#         if x == "King":
#             str_list.remove(x)
#             str_list.append(x)
#     sorted_cards = int_list + str_list
#     print(f"TEST CASE 2 = {sorted_cards}")
# test_case2(['Jack', 8, 2, 6, 'King', 5, 3, 'Queen', 'Jack', 'King', 'Queen', 'Queen', 'King', 'Jack'])


# def test_case3(cards):
#     int_list = sorted([x for x in cards if type(x) == int])
#     str_list = sorted([x for x in cards if type(x) == str])
#     sorted_cards =   int_list + str_list
#     print(f"TEST CASE 3 = {sorted_cards}")
# test_case3(['Jack', 8, 2, 6, 5, 3] )


def test_case(cards):
    int_list = sorted([x for x in cards if type(x) == int])
    str_list = sorted([x for x in cards if type(x) == str])
    for x in str_list:
        if x == "King":
            str_list.remove(x)
            str_list.append(x)
    sorted_cards = int_list + str_list
    print(f"TEST CASE = {sorted_cards}")

test_case(['Jack', 8, 2, 6, 'King', 5, 3, 'Queen'])
test_case(['Jack', 8, 2, 6, 'King', 5, 3, 'Queen', 'Jack', 'King', 'Queen', 'Queen', 'King', 'Jack'])
test_case(['Jack', 8, 2, 6, 5, 3])