'''
2024년04월16일
202195057 손패택
'''
int_num= int(input("점수 입력 : "))
for num in (range(2, input_num+1, 1)) :
    result = input_num % num
    if result == 0:
        count = count + 1
if count == 1 :
    print(f"{input_num}은 소수입니다.")
else :
    print(f"{input}은 소수가 아닙니다.") 