class Personne:
    def __init__(self, name, age, sexe=None):
        print("dans le __init__")
        self.name = name
        self.age = age
        self.sexe = sexe

    def presenter(self):
        return f"Je suis {self.name} et j'ai {self.age} ans et suis de sexe {self.sexe}"

    def __str__(self):
        return self.presenter()


p1 = Personne("Jean", 25, "M")
