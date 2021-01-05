# 2.88ms, 1.59ms
def solution(phone_book):
    for i in range(len(phone_book)):
        first = len(phone_book[i])
        for j in range(len(phone_book)):
            if i != j and phone_book[i] in phone_book[j][0:first]:
                return False
    return True

# 3.28ms, 3.37ms
# def solution(phone_book):
#     phone_book = sorted(phone_book)
    
#     for i in range(len(phone_book)):
#         first = len(phone_book[i])
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i] in phone_book[j][0:first]:
#                 return False
#     return True
