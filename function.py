Zip = {'Bolt': 202, 'Gaika': 105, 'Shaiba':98, 'Traversa':46, 'Stoika':526,'Rama':132}
print(Zip)

def vzyat():
    n = str(input('Введите название позиции: '))
    kol = int(input('Введите количество, которое должно быть на складе: '))
    return n, kol
n, kol = vzyat()
def prov(n, kol):
    if Zip[n] < kol: #Количество запчастей мешьше заданного
        if n == 'Bolt':
            st = kol - Zip[n]
            Zip[n] = kol
            sts = kol - Zip['Shaiba']
            
            print('Добавить в заказ: ' + str(st) + ' шт. болтов и ' + str(sts) + ' шт. шайб')
            print(Zip)
        else:
            s = kol - Zip[n]
            
            print('Добавить в заказ: ' + str(s) + ' шт.')
            print(Zip)
    else:
        print('Деталей достаточно')
    return n, kol

prov(n, kol)

a = input('Продолжить проверку? ')
while a == 'Да':
    n, kol = vzyat()
    prov(n, kol)
    a = input('Продолжить проверку? ')
print('Проверка окончена')