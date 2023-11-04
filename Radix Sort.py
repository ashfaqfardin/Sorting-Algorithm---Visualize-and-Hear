import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random
import threading
from playsound import playsound

# Input the size of the array (list here) and shuffle the elements to create a random list
n = 20
a = [i for i in range(1, n+1)]
random.shuffle(a)

# Radix sort
def counting_sort_for_radix(input_array, exp):
    n = len(input_array)
    output_array = [0] * n
    count_array = [0] * 10

    for i in range(n):
        index = input_array[i] // exp
        count_array[(index) % 10] += 1

    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    i = n - 1
    while i >= 0:
        index = input_array[i] // exp
        output_array[count_array[(index) % 10] - 1] = input_array[i]
        count_array[(index) % 10] -= 1
        i -= 1

    i = 0
    for i in range(len(input_array)):
        input_array[i] = output_array[i]

    return input_array

def radixsort(a):
    max_val = max(a)
    exp = 1
    while max_val / exp > 0:
        a = counting_sort_for_radix(a, exp)
        yield a
        exp *= 10

# Generator object returned by the function
generator = radixsort(a)

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
    # Play sound in a new thread
    threading.Thread(target=playsound, args=('ping-82822.mp3',)).start()

anim = FuncAnimation(fig, func=animate, fargs=(rects, iteration), frames=generator, interval=50, repeat=False)

plt.show()
