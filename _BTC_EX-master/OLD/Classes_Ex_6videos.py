class Employee:

    raise_amout = 1.05

    def __init__(self, par1, par2, par3):

        self.nome = par1
        self.cognome = par2
        self.pay = par3
        self.email = par1 + '.' + par2 + '@gmail.com'

    def fullname(self):

        print('{} {}'.format(self.nome, self.cognome))

    def apply_raise(self):

        self.pay = int(self.pay * self.raise_amout)


emp1 = Employee('Fabrizio', 'Peruzzo', 55000)
emp2 = Employee('Francesca', 'Mangia', 60000)


emp1.nome  # --> richiamo un parametro

emp1.fullname()  # --> richiamo un methodo
Employee.fullname(emp1)  # altro modo per richiamare un methodo

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
