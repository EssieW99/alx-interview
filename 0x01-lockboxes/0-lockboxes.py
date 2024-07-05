#!/usr/bin/python3
""" interview question"""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened"""

    n = len(boxes)
    opened_boxes = set()
    stack = [0]

    while stack:
        # pops the last item from the stack assigning it to current_box
        current_box = stack.pop()
        # checks if current_box has already been opened
        if current_box not in opened_boxes:
            # marks current_box as opened
            opened_boxes.add(current_box)
            # a key reps another box that can be opened if it matches the index
            for key in boxes[current_box]:
                # checks if key is a valid box index
                if key < n and key not in opened_boxes:
                    stack.append(key)

    return len(opened_boxes) == n
