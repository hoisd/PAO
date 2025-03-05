Zip = {'Bt_08':[202,"Болт","M8"], 'Bt_06':[105,"Болт","М6"], 'Sh_06':[98,"Шайба","М6"], 'Bt_10':[46,"Болт","М10"], 'Sh_08':[526,"Шайба","М8"],'Sh_10':[132,"Шайба","М10"]}
print(Zip)
#[i,k,j] i-кол-во k_ тип j-типоразмер
n = Zip['Bolt_Eng_M6']
N = Zip['Shaiba_M6']
i=n[0]
i1=N[0]
if i == i1:
    print('Число шайб и болтов совпадает')
else:
    need = abs(i-i1)
    print('Необходимо взять со склада недостающую позицию в количестве: ' + str(need))


    if n < N:
        Zip['Bolt_Eng_M6']+=need
        n = Zip['Bolt_Eng_M6']
        print('Со склада взято: ' + str(need) + ' болтов')
    else:
        Zip['Shaiba_M6']+=need
        N = Zip['Shaiba_M6']
        print('Со склада взято: ' + str(need) + ' Шайб')
print(Zip)
print('Число шайб и болтов совпадает')
