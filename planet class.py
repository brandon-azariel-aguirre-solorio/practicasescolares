class planet:
    def __init__ (self,name,planet_type,star):
        
        self.name = name
        self.planet_type = planet_type
        self.star = star
        
        if not all(isinstance(arg, str) for arg in [name, planet_type, star]):
            raise TypeError("name, planet type, and star must be strings")
        if any (arg == '' for arg in [name, planet_type, star]):
            raise TypeError('name, planet_type, and star must be non-empty strings')
    def orbit (self):
        return f'{self.name} is orbiting around {star}...'
    def
