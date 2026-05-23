class Planet:
    def __init__ (self,name,planet_type,star):
        
        self.name = name
        self.planet_type = planet_type
        self.star = star
        
        if not all(isinstance(arg, str) for arg in [name, planet_type, star]):
            raise TypeError("name, planet type, and star must be strings")
        if any (arg == '' for arg in [name, planet_type, star]):
            raise ValueError('name, planet_type, and star must be non-empty strings')
    def orbit (self):
        return f'{self.name} is orbiting around {self.star}...'
    
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet('tierra','1','2')
planet_2 = Planet('sol','3','4')
planet_3 = Planet('jupyter','5','6')

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
