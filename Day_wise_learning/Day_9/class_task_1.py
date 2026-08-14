class Pet:
    def __init__(self, name, children=None, energy=50):
        self.name = name
        self.children = children if children is not None else []
        self.__energy = 0

        self.set_energy(energy)

    def get_energy(self):
        return self.__energy

    def set_energy(self, val):
        val = int(val)

        if val > 100:
            self.__energy = 100
        elif val < 0:
            self.__energy = 0
        else:
            self.__energy = val

    def add_child(self, *children):
        self.children.extend(children)

    def display(self):
        print(
            f"My name is {self.name} "
            f"with children {self.children} "
            f"and energy {self.__energy}"
        )

pet1 = Pet("ruby", energy = 150)
pet2 = Pet("rose", energy = 60)

class RoboPet(Pet):
    def set_energy(self, val):
        val = 1.2 * val
        super().set_energy(val)

grandpa = RoboPet("Roman_Reings",energy = 20)
grandpa.add_child(pet1)
grandpa.add_child(pet2)

def get_total_family_energy(pet : Pet):
    total_energy = pet.get_energy()
    
    if pet.children:
        for each in pet.children:
            total_energy += each.get_energy()
    
    return total_energy

print(get_total_family_energy(grandpa))

        
            