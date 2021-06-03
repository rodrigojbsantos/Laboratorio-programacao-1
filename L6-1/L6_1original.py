# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
"""vetor1 = []
vetor2 = []
vetor3 = []
vetor1.append(input().split())
vetor2.append(input().split())
tamanho1 = len(vetor1)
tamanho2 = len(vetor2)
tamanho = 0
print(vetor1)
print(tamanho1)
print(tamanho2)
print(tamanho)
print(vetor2)
print(vetor1[tamanho])
while tamanho <= tamanho1 or tamanho <= tamanho2:
    vetor3.append(vetor1[tamanho])
    print(vetor3[tamanho], 'oiiii')
    vetor3.append(vetor2[tamanho])
    print(vetor3[tamanho])
    tamanho += 1
print(vetor3)
"""

"""x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]
print("Number of list is: ", x)
print(len(x))
print(x[2])
tamanho = 0
tamanho1 = len(x)
tamanho2 = len(y)
z = []
while tamanho < tamanho1 or tamanho < tamanho2:
    z.append(x[tamanho])
    print(x[tamanho], 'oiiii')
    z.append(y[tamanho])
    print(z[tamanho])
    print(z)
    tamanho += 1
print(z)
for x in z:
    print(x)"""


"""def merge_lists_into_string(a, b, string):
    
    '''
    Takes two lists of varying size and merges them like so:
        ([1,2,3], [10, 20, 30, 40, 50]) >> [1, 10, 2, 20, 3, 30, 40, 50]
    '''
    if a:
        string += a.pop(0)
    if b:
        string += b.pop(0)
    if a or b:
        string = merge_lists_into_string(a, b, string)
    return string
string = []
x = [1,2,3]
y = [10, 20, 30, 40, 50]
merge_lists_into_string(x, y, string)
print(string)

******************8"""
list3 = []

vetor1 = [int(x) for x in input().split()]
vetor2 = [int(y) for y in input().split()]

print(vetor1)
print(vetor2)
#vetor1.append(input().split())
#vetor2.append(input().split())

while True:
    try:
        list3.append(vetor1.pop(0))
        list3.append(vetor2.pop(0))
       
    except IndexError:
        break
print(list3)


