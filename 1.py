N=int(input("Введите количество слов "))
a=[]

for i in range(N):
    word=input("Введите слово ")
    a.append(word)
b=' '.join(a)

print (b)

