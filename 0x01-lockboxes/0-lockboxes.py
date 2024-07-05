#!/usr/bin/python3
""" interview question"""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened"""

    n = len(boxes)
    opened_boxes = set()
    stack = [0]

    while stack:
        current_box = stack.pop() # pops the last item from the stack assigning it to current_box
        if current_box not in opened_boxes: # checks if current_box has already been opened
            opened_boxes.add(current_box) # marks current_box as opened
            for key in boxes[current_box]: # a key reps another box that can be opened if it matches the index
                if key < n and key not in opened_boxes: # cheks if key is a valid box index
                    stack.append(key)

    return len(opened_boxes) == n
