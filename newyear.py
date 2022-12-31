import badger2040
import random
import time
badger = badger2040.Badger2040()
badger.update_speed(badger2040.UPDATE_TURBO)

counter = 30;
while True:
    up = badger.pressed(badger2040.BUTTON_UP)
    down = badger.pressed(badger2040.BUTTON_DOWN)  
    buttonB = badger.pressed(badger2040.BUTTON_B)
    if up:
        counter += 5
    if down:
        counter -= 5
    if buttonB:
        break;
    badger.pen(15)
    badger.clear()
    badger.pen(0)
    badger.text(f"Ile do nowego roku: {counter} sekund", 0, 60, .7)
    badger.text("b: start", 100, 120, .7)
    badger.update()
    time.sleep(1)
    

while True:
    badger.pen(15)
    badger.clear()
    badger.pen(0)
    badger.text(f"Do nowego roku: {counter} sekund", 0, 60, .7)
    badger.update()
    counter -= 1
    if counter < 0:
        break;
    time.sleep(1)


while True:
    badger.pen(15)
    badger.clear()
    badger.pen(0)
    badger.update_speed(badger2040.UPDATE_TURBO)
    badger.text("Super nowego roku!", 40, 60, .7)
    a = []
    for i in range(2023):
        a.append({
            "x": random.randint(0, badger2040.WIDTH),
            "y": random.randint(0, badger2040.HEIGHT)
        })
    #print(a)
    for i in a:
        badger.pixel(i["x"], i["y"])

    badger.update()
    time.sleep(.2)
