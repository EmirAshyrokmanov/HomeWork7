x = 38
print('дратути!')
if x<0:
    print('меньше нуля')
print('дотвидания')

 #примеры
a, b = 10, 5
if a>b:
     print('a>b')
if a>b and a>0:
    print("успех1")
if (a>b) and (a>0 or b<1000):
    print("успех2")
if 5<b and b<10:
    print("успех3")
#можно сравнивать : числа, строки, списки
if '34' > '123':
    print("успех4")
if '123' > '12':
    print("успех5")
if [1,2] > [1,1]:
    print("успех6")
#что нельзя сравнивать
if '6'>5:
    print("успех7")
if [5,6] >5:
    print("успех8")
#но
if '6' != 5:
    print("успех9")