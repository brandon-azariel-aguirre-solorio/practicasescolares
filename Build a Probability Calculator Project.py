import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn

        drawn_balls = []
        for b in range(num_balls):
            index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(index))

        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0

    for b in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)

        match = True
        for color, required_count in expected_balls.items():
            if drawn.count(color) < required_count:
                match = False
                break

        if match:
            success += 1

    return success / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
