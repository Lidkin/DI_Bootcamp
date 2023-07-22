#1________________________________________________________________
class Family:
    print('exersice XP+ #1')
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **new_member):
        self.members.append(new_member)
        print(f"Congratulations! {new_member.get('name')} was born")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    return True
                else:
                    return False

    def family_presentation(self):
        family_members = [member.get('name') for member in self.members]
        names = ', '.join(family_members) 
        print(f"Family {self.last_name} has the following members: {names}")


family_data = [{'name':'Sarah', 'age':30, 'gender':'Female', 'is_child':False},
 {'name':'Jacob', 'age':33, 'gender':'Male', 'is_child':False}]

family = Family('Goldshmidt', family_data)
 
family.family_presentation()
family.born(name='Michael', age=0, gender='Male',is_child=True)
family.family_presentation()

names = [family.members[i].get('name') for i in range(0, len(family.members))]
is_18 = list(map(family.is_18, names))
for i in range(0, len(names)):
    print(f'{names[i]} is 18? {is_18[i]}')

#2________________________________________________________________
class TheIncredibles(Family): 
    def __init__(self, last_name, members):
        print('\nexersice XP+ #2')
        super().__init__(last_name, members)
        self.last_name = last_name
        self.members = members
    
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']} is using his/her power")
                else:
                    try:
                        member.get('exception') == True
                        print(f"{member['name']} too young, but can youse power")
                    except:    
                        print(f"{member['name']} is too young") 
    
    def incredible_presentation(self):
        super(TheIncredibles, self).family_presentation()
        family_powers = [[member.get('incredible_name'), member.get('power')] for member in self.members]
        for i in range(0, len(family_powers)):
            print(f"{family_powers[i][0]}'s power: {family_powers[i][1]}")        

members_data = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
] 

incredible_family = TheIncredibles("Stark", members_data)
incredible_family.incredible_presentation()
incredible_family.born(name='Baby Jack', gender='Male', is_child=True, power='Unknown Power')
incredible_family.family_presentation()