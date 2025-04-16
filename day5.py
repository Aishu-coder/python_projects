import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
print("Welcome to password genarator")
nrletter = int(input("how many letters u want in passwaord ?\n"))
nrnum = int(input("how many numbers  u want in passwaord ?\n"))
nrsym = int(input("how many symbols  u want in passwaord ?\n"))

L = ''
for i in range(nrletter) :
    l=random.randint(0, len(nrletter))
    L+=letter[l]
print(L)
N=''
for i in range(nrnum):
    n = random.randint(0, len(num))
    N += num[n]
print(N)
S = ''
for i in range(nrsym):
    s = random.randint(0, len(sym))
    S += sym[s]
print(S)
print(L + N + S)
