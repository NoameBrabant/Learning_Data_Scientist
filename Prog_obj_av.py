from turtle import fd


class Felin():
    nombre_de_patte = 4  # C'est un attribut de classe
    carnivore = True
    energie = 100
    
    def __init__(self, color): # Construceur d'attribut d'insctence
        self.__color = color
    
    def __str__(self) -> str:
        return "je suis un felin"
    
    def get_color(self):
        return self.__color
    
    def set_race(self, new_color):
        self.__race = new_color 
    
    def manger_viande(self):
         print("je viens de de manger de la viande")
    
    @classmethod                       # métohde de classe : pour utilisé les attribut de classe
    def les_felins_courent(cls):
        cls.energie = cls.energie - 10
    
    @staticmethod                      # méthode statique : methode sans arguments en rapport avec la classe
    def nombre_de_felin(nombre_de_lion, nombre_de_tigre):
        return nombre_de_lion + nombre_de_tigre


class Lion(Felin):  # La classe Lion est une classe fille de Felin
    
    def __init__(self, race, name, color):
        super().__init__(color) # "super()" pour récuper les init de la classe mère
        self.__race = race
        self.name = name
    
    def get_race(self):
        return self.__race
    
    def set_race(self, new_race):
        self.__race = new_race
    
class Giraf():
    race = "girafe"

    
    


toto = Lion("lion de la savane", "toto", "beige")
gerard = Lion("lion des montagnes", "gerard", "marron")

print(toto.__dict__) #Donne une instence en format dictionaire


print(isinstance(toto, Lion)) #isinstance : toto est il une instance de Lion
print(isinstance(toto, Felin)) #retrun True, car toto est une instancede classe "Lion" qui est une sousclasse de "Felin"
print(issubclass(Lion, Felin)) #issubclasse : Lion est il une classe fille de Felin
print(issubclass(Lion, Giraf))




