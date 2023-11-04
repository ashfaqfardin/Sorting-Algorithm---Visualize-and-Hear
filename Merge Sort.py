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

# Merge sort
def mergesort(a, start, end):
    if end <= start:
        return
    mid = (start + end) // 2
    yield from mergesort(a, start, mid)
    yield from mergesort(a, mid + 1, end)
    yield from merge(a, start, mid, end)
    yield a

def merge(a, start, mid, end):
    merged = []
    left_idx = start
    right_idx = mid + 1

    while left_idx <= mid and right_idx <= end:
        if a[left_idx] < a[right_idx]:
            threading.Thread(target=playsound, args=('ping-82822.mp3',)).start()
            merged.append(a[left_idx])
            left_idx += 1
        else:
            threading.Thread(target=playsound, args=('ping-82822.mp3',)).start()
            merged.append(a[right_idx])
            right_idx += 1

    while left_idx <= mid:
        # Play sound in a new thread
        threading.Thread(target=playsound, args=('ping-82822.mp3',)).start()
        merged.append(a[left_idx])
        left_idx += 1

    while right_idx <= end:
        # Play sound in a new thread
        threading.Thread(target=playsound, args=('ping-82822.mp3',)).start()
        merged.append(a[right_idx])
        right_idx += 1

    for i, sorted_val in enumerate(merged):
        # Play sound in a new thread
        threading.Thread(target=playsound, args=('ping-82822.mp3',)).start()
        a[start + i] = sorted_val
        yield a

# Generator object returned by the function
generator = mergesort(a, 0, len(a) - 1)

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
    # # Play sound in a new thread
    # threading.Thread(target=playsound, args=('ping-82822.mp3',)).start()

anim = FuncAnimation(fig, func=animate, fargs=(rects, iteration), frames=generator, interval=50, repeat=False)

plt.show()
