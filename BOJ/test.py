class doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, kinds):
        self.name = name
        self.kinds = kinds
        doggy.num_of_dogs += 1
        doggy.birth_of_dogs += 1
    
    def __del__(self):
        doggy.num_of_dogs -= 1
    
    def bark(self):
        print('왈왈')

    def get_status():
        print(doggy.num_of_dogs, doggy.birth_of_dogs)

dog1 = doggy('백구', '진돗개')
dog2 = doggy('흰둥이', '시츄')
dog1.bark()
doggy.get_status()

del(dog2)
dog1.bark()
doggy.get_status()