class Dog:
    def __init__(self, nombre):
        self.nombre = nombre

    def bark(self):
        print(f"{self.nombre} say Woof !!")


perro1 = Dog("Firulais")
perro2 = Dog("Snoopy")

print(perro1.nombre)
print(perro2.nombre)

perro1.bark()
perro2.bark()

class Cat:
    def __init__(self, nombre):
        self.nombre = nombre
        print("Init")

gato = Cat("Michifuz")