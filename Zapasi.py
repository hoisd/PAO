class Izdelie:
    # def __init__(self,S,P,T):
        # self.Specification = S  # Спецификация изделий
        # self.Program_vip = P # Программа выпуска изделий
        # self.Time_check = T # Периодичность проверки запасов, сутки
        # print(f"Спецификация:  {self.Specification} Программа выпуска: {self.Program_vip} Периодичность проверки: {self.Time_check}")
    def __init__(self,S,P,T):
        S = str(input('Введите название позиции: '))
        P = int(input('Введите количество изделий: '))
        self.Time_check = T # Периодичность проверки запасов, сутки
        return self,S,P,T
    def prov(self,S,P,kol):
        kol = int(input('Введите количество, которое должно быть на складе: '))
        if P < kol: #Количество запчастей мешьше заданного
            if S == 'Bolt':
                st = kol - P
                S = kol
                sts = kol - P              
                print('Добавить в заказ: ' + str(st) + ' шт. болтов и ' + str(sts) + ' шт. шайб')
                print(S)
            else:
                s = kol - S
                
                print('Добавить в заказ: ' + str(s) + ' шт.')
                print(Zip)
        else:
            print('Деталей достаточно')
        return S, kol

# class Zapas_assemble:

#     def __init__(self, N, O, D):
#         self.Name = N # Название изделия
#         self.Otvets = O # Ответственный
#         self.Data_mesyac = D # Дата запуска, месяц
#         # print(f"Название изделия: {self.Name} Ответственный: {self.Otvets} Дата запуска: {self.Data_mesyac}")


# S1 = Izdelie('Bolt',202,1)
# S2 = Izdelie('Gaika',105,1)
# S3 = Izdelie('Shaiba',98,1)
# S4 = Izdelie('Traversa',46,1)
# Zapas1 = Zapas_assemble("noname","nootvets","march")
