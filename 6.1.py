Zip = {'Bolt_Eng_M8:202\n', 'Bolt_Eng_M6:460\n', 'Shaiba_M6:98\n'}
o1 = open('Data.txt', mode = 'w')
o2 = o1.write('Bolt_Eng_M10:46\n')
o3 = o1.writelines(Zip)
o1.close
o4 = open('Data.txt')
o5 = o4.read()
print(o5)
