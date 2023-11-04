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

# Quick sort
def quicksort(a, start, end):
    if start >= end:
        return
    pivot = a[end]
    left = start
    right = end - 1
    while True:
        while left <= right and a[left] < pivot:
            left = left + 1
        while right >= left and a[right] > pivot:
            right = right - 1
        if left <= right:
            a[left], a[right] = a[right], a[left]
            left, right = left + 1, right - 1
        else:
            break
    a[left], a[end] = a[end], a[left]
    # Play sound in a new thread
    threading.Thread(target=playsound, args=('ping-82822.mp3',)).start()
    yield a
    yield from quicksort(a, start, right)
    yield from quicksort(a, left + 1, end)

# Generator object returned by the function
generator = quicksort(a, 0, len(a) - 1)

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
