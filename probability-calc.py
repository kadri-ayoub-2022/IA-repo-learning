import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        
        if num_balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn

        
        drawn = random.sample(self.contents, num_balls)  # choisir une liste de num_balls element du population self.contets
        for ball in drawn:
            self.contents.remove(ball)  
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        
        hat_copy = copy.deepcopy(hat)
        
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        draw_result = {}
        for color in drawn_balls:
            draw_result[color] = draw_result.get(color, 0) + 1
        
        success = True
        for color, min_count in expected_balls.items():
            if draw_result.get(color, 0) < min_count:
                success = False
                break
        if success:
            success_count += 1

    return success_count / num_experiments
