from microbit import *
from gesture import *
import music
import neopixel
from random import randint
np = neopixel.NeoPixel(pin1, 5)

display.show(Image.YES)
sleep(500)
display.clear()

gesture = Gesture()

num_swipe = 0


while True:
    for pixel_id in range(0, len(np)):
        red = randint(0, 60)
        green = randint(0, 60)
        blue = randint(0, 60)
        np[pixel_id] = (red, green, blue)

    if accelerometer.was_gesture("up"):
        display.show(Image.HAPPY)
        np.show()
        music.play(music.JUMP_UP)
        sleep(1000)

    elif accelerometer.was_gesture("down"):
        np.clear()
        display.clear()

    g = gesture.read()
    if g == 'up':
        num_swipe += 1
        display.show(Image.DIAMOND)
        np.show()
        music.play(music.BA_DING)
        sleep(200)
        np.clear()
        display.clear()

    if num_swipe == 5:
        for i in range(3):
            display.show(Image.HEART, i)
            np.show()
            sleep(100)
        np.clear()
        display.clear()
    else:
        sleep(100)

    for pixel_id in range(0, len(np)):
        red = randint(0, 60)
        np[pixel_id] = (red, 0, 0)

    if accelerometer.was_gesture("left"):
        display.show(Image.ANGRY)
        np.show()
        sleep(100)

    elif accelerometer.was_gesture("right"):
        display.show(Image.ANGRY)
        np.show()
        sleep(100)

    for pixel_id in range(0, len(np)):
        blue = randint(0, 60)
        np[pixel_id] = (0, 0, blue)

    if accelerometer.was_gesture("face up"):
        display.show(Image.CONFUSED)
        np.show()
        sleep(100)

    elif accelerometer.was_gesture("face down"):
        display.clear()
        np.clear()

    sleep(100)

else:
    np.clear()
    display.clear()
    sleep(100)

sleep(10)