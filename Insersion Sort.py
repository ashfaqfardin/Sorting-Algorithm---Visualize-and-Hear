import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random
import threading
from playsound import playsound

# Input the size of the array (list here) and shuffle the elements to create a random list
n = int(input("Enter array size\n"))
a = [i for i in range(1, n+1)]
random.shuffle(a)

# Insertion sort
def insertionsort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        while(i >= 0 and a[i] > key):
            a[i+1] = a[i]
            i -= 1
            # Play sound in a new thread
            threading.Thread(target=playsound, args=('ping-82822.mp3',)).start()
            yield a
        a[i+1] = key
        yield a

# Generator object returned by the function
generator = insertionsort(a)

fig, ax = plt.subplots()

# The bar container
rects = ax.bar(range(len(a)), a, align="edge")

# Setting the view limit of x and y axes
ax.set_xlim(0, len(a))
ax.set_ylim(0, int(1.1*len(a)))

# The text to be shown on the upper left indicating the number of iterations
text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
iteration = [0]

# Function to be called repeatedly to animate
def animate(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("iterations : {}".format(iteration[0]))

anim = FuncAnimation(fig, func=animate, fargs=(rects, iteration), frames=generator, interval=50, repeat=False)

plt.show()
