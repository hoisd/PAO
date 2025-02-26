Zip = {'Bolt_Eng_M8':202, 'Bolt_Eng_M6':460, 'Shaiba_M6':98, 'Bolt_Eng_M10':46, 'BuHT_plast_M6':526}
print(Zip)

New_Zip = 'Bolt_Eng_M8'
if New_Zip == 'Bolt_Eng_M8' and Zip['Bolt_Eng_M8'] < 310: # Необходимый запас болтов крепления головы - 18 шт.
    print('Необходимо дозаказать позицию "Bolt_Eng_M8"')

New_Zip = 'Bolt_Eng_M10'
if New_Zip == 'Bolt_Eng_M10' and Zip['Bolt_Eng_M10'] < 112: # Необходимый запас болтов крепления двигателя - 4 шт.
        zakaz = str(112 - Zip['Bolt_Eng_M10'])
        print('Необходимо заказать позицию "Bolt_Eng_M10" в количестве: ' + zakaz)
else:
        print('Позиции "Bolt_Eng_M10" - достаточно')

New_Zip = 'Shaiba_M6'
if New_Zip == 'Shaiba_M6' and Zip['Shaiba_M6'] < 50: # Необходимый запас шайб на рабочем месте - 50 шт.
        zakaz = str(50 - Zip['Shaiba_M6'])
        print('Необходимо заказать позицию "Shaiba_M6" в количестве: ' + zakaz)
else:
    if New_Zip == 'Shaiba_M6' and Zip['Shaiba_M6'] > 80: # В коробоку с шайбами вмещаеся 100 шт.
        izb = str(Zip['Shaiba_M6'] - 80)
        print('Необходимо переложить избыток - ' + izb + ' на склад')
        Zip['Shaiba_M6'] = 80
    else:
        print('Позиции "Shaiba_M6" - достаточно')
print(Zip)