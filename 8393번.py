#n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
sum=0
n=int(input())
for i in range(n+1):
    sum=sum+i
print(sum)
