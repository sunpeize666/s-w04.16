'''
202195057 손패택
2024.04,16
说明：输入两个数，计算两个数之间的所有数之和。
计算总和，包括两个接收到的输入数。
问题分析：
如果第一个数为1，第二个数为10，请计算1到10的总和
初始值（开始）：从第一个数开始
条件式(中止）：到第二步为止
增减式：增加1
如果第一个数是小数，第二个数是大数，那么从第一个数到第二个数反复的话
第二个数相反的话
第一个数是大数，此二个数小的话。
从小数到大数各增加1
比较输入的两个数，如果第一个数大的话，两个数不交完。
'''
num1 = int(input("첫번째 수 입력 : "))
num2 = int(input("두번째 수 입력 : "))
sum=0
if num1<num2 :
    for num in range(num1,num2-1,1):
        sum=sum+num
else :
        for num in range(num1,num2-1,-1):
            sum = sum+num
print (f"{num1}부터{num2}까지 합 : {sum}")

sum = 0

if num1 > num2 :
     temp = num1
     num1 = num2
     num2 = temp
     for num in range(num1,num2+1,1):
          sum = sum + numpeint(f"{num1}부터 {num2}까지 합 : {sum}")