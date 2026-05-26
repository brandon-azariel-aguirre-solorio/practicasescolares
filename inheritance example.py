class Walker:
    def walk(self):
        return 'I can walk on land'

class Swimmer:
    def swim(self):
        return 'I can swim in water'

# Amphibian inherits from both Walker and Swimmer
class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}."

frog = Amphibian('Freddy')
print(frog.introduce())
# Output: I'm Freddy the frog. I can walk on land and I can swim in water.




class Cat:
   def speak(self):
       return "A cat meow"

class Bird:
   def speak(self):
       return "A bird tweet"
  
class Monkey:
   def speak(self):
       return "A monkey ooh ooh aah aah ooh ooh aah aah"

def animal_sound(animal):
   print(animal.speak())

animal_sound(Cat())
animal_sound(Bird())
animal_sound(Monkey())



class Twitter:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"🐦 Tweet: '{self.content}' (280 chars max)"

class Instagram:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"📸 Instagram Post: '{self.content}' + ✨ filters"

class LinkedIn:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"💼 LinkedIn Article: '{self.content}' (Professional Mode)"

def start(social_media):
   print(social_media.post())  # Calls .post() on any object

# Instances
tweet = Twitter('Just learned Python polymorphism!')
photo = Instagram('Sunset vibes 🌅')
article = LinkedIn('Why OOP matters in 2024')

# The polymorphic calls - same function, different outputs
start(tweet) # 🐦 Tweet: 'Just learned Python polymorphism!' (280 chars max)
start(photo) # 📸 Instagram Post: 'Sunset vibes 🌅' + ✨ filters
start(article) # 💼 LinkedIn Article: 'Why OOP matters in 2024' (Professional Mode)
