# 전체 문자열을 순회하며 "<"라면 ">"를 찾을 때까지 문자열을 넣어줌                  -> split을 이용하여 "<>"와의 구분점 만들기
# 그 이외의 문자열 이라면 " "을 찾을 때까지 반복하며 문자열을 찾고 뒤집어서 넣어줌    -> " "을 기준으로 split하고 뒤집어 주기


#풀이
#"<"와 ">"를 "!"를 붙여서 치환후 !를 기준으로  split
#"<>"가 있는 문자열은 바로 answer에 추가 아닌 경우 ' '를 기준으로 split 후 뒤집어서 추가


answer = ''
S = input().replace('<','!<').replace('>','>!').split('!')

for s in S:
    if '<' in s:
        answer += s
    else:
        answer += ' '.join([i[::-1] for i in s.split(' ')])

print(answer)


