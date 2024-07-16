
import random 
def weather():
    status = ["맑음", "흐림", "비", "눈", "폭풍우"]
    return random.choice(status)

def temper():
    return random.randint(10,30)
