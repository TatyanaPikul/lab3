a=[]

while True:
    word=input("Введите слово ")
    if word=='stop':
        break
    a.append(word)

b=' '.join(a)

print (b)
