class GameCharacter:
    def __init__(self,name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
        

    @health.setter
    def health(self):
        if health < 0:
            health = 100
    
    @property
    def mana(self):
        return self._mana
        

    @mana.setter
    def mana(self):
        if mana < 0:
            mana = 50
    @property
    def level(self):
        return self._level
    
    def level_up(self):
        
        self.level += 1
       
        self.health = 100
        self.mana = 50
        
        print(f"{self.name} leveled up to {self.level}!")
    
    def __str__(self):
        return (
            f"Character: {self.name}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"Mana: {self.mana}"
        )
