"""
=============================================================================
File:           basics.py
Description:    Lab Task 02 - Python Fundamentals and Exercises
Course:         Digital Image Processing Lab
Author:         Sheikh Haseeb-ur-Rehman
Roll Number:    2024-SE-31
Instructor:     Engr. Fahad Nisar
=============================================================================
"""

def print_separator(title):
    """Helper function to format terminal output beautifully."""
    print(f"\n{'-' * 15} {title} {'-' * 15}")

print_separator("Exercise 1: Variables & Data Types")
width = 640
height = 480
image_name = "sample.png"
is_color = True

print(f"Variable 'width'      : {width} \t| Type: {type(width)}")
print(f"Variable 'height'     : {height} \t| Type: {type(height)}")
print(f"Variable 'image_name' : {image_name} \t| Type: {type(image_name)}")
print(f"Variable 'is_color'   : {is_color} \t| Type: {type(is_color)}")

total_pixels = width * height
print(f"\nTotal calculated pixels (width * height): {total_pixels}")


print_separator("Exercise 2: if, elif, and else")
test_values = [-1, 0, 127, 128, 255, 256]

for val in test_values:
    if val < 0 or val > 255:
        print(f"Intensity {val:>3} : Invalid")
    elif val >= 128:
        print(f"Intensity {val:>3} : Bright pixel")
    else:
        print(f"Intensity {val:>3} : Dark pixel")


print_separator("Exercise 3: for and while Loops")
print("--- For Loop Output ---")
for pixel in [20, 130, 255]:
    label = "Bright pixel" if pixel >= 128 else "Dark pixel"
    print(f"Value {pixel:>3} is a {label}")

print("\n--- While Loop Output ---")
i = 0
while i < 3:
    print(f"Counter: {i}")
    i += 1


print_separator("Exercise 4: Functions")
def is_bright(pixel, threshold=128):
    """Returns True if the pixel meets or exceeds the threshold."""
    return pixel >= threshold

print(f"is_bright(127)      -> {is_bright(127)}")
print(f"is_bright(128)      -> {is_bright(128)}")
print(f"is_bright(200, 210) -> {is_bright(200, 210)}")


print_separator("Exercise 5: Lists and Tuples")
# List operations
pixels = [0, 128, 255]
print(f"Original list       : {pixels}")
print(f"First item          : {pixels[0]}")

pixels[1] = 150
pixels.append(64)
print(f"Modified list       : {pixels}")
print(f"Total list length   : {len(pixels)}")

# Tuple operations
size = (640, 480)
unpacked_width, unpacked_height = size
print(f"\nUnpacked Tuple      : Width = {unpacked_width}, Height = {unpacked_height}")

# Explanation: A list is mutable, meaning its items can be reassigned, added, or removed.
# A tuple is immutable, meaning its structure and items are permanently fixed upon creation.


print_separator("Exercise 6: Dictionaries and Sets")
# Dictionary operations
image = {"width": 640, "height": 480}
image["mode"] = "RGB"

print(f"Dictionary Width Key: {image['width']}")
print(f"Dictionary Mode Key : {image['mode']}")

# Set operations
labels = ["cat", "dog", "cat", "bird"]
unique_labels = set(labels)
print(f"\nOriginal labels list: {labels}")
print(f"Unique labels (set) : {unique_labels}")
print(f"Count of unique labels: {len(unique_labels)}")
print("\n") # Final padding