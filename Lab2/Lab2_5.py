u=int(input("Введите целое двузначное число: "))
g=0
while(u!=0):
    g+=u%10
    u//=10
print(g)
