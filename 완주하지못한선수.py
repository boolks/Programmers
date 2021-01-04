from collections import Counter


def solution(participant, completion):
    ans = Counter(participant) - Counter(completion)
    print(ans)

# def solution(participant, completion):
    
#     participant.sort(); completion.sort()
#     print(participant)
#     print(completion)
    
#     for i in range(len(completion)):
#         if participant[i] == completion[i]:
#             pass
#         else:
#             return participant[i]
#     return participant[-1]
    
    # print(participant)
    # print(completion)
    
# count : O(n), remove : O(n) 이므로 O(n^2)이 나오기 때문에 효율성 탈락
# def solution(participant, completion):
#     answer = ''
    
#     for i in range(len(participant)):
#         if (participant.count(participant[i]) > 1) & (completion.count(participant[i]) != participant.count(participant[i])):
#             return participant[i]
#         elif participant[i] in completion:
#             pass
#         else:
#             return participant[i]