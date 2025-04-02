class Izdelie:
    Specification = {}
    Program_vip = 0
    Time_check = 1 #сутки
class Zapas_assemble:
    Name = "none"
    Otvets = "noname"
    Data_mesyac = "Март"

    def __init__(self):
        print(f"Name: {self.Name} Otvets:{self.Otvet} Data_mesyac: {self.Data_mesyac}")
Izd1 = Izdelie()
Zapas1 = Zapas_assemble("noname","nootvets","march")
print(Zapas1.Name)
print(Izd1.Program_vip)
Zapas1.__init__