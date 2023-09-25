#!/usr/bin/python3
""" Module for determining if all boxes can be unlocked """

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    - boxes (list of lists): Each inner list represents the keys in a box.

    Returns:
    - bool: True if all boxes can be opened, otherwise False.
    """
    
    if not boxes:
        return False
    
    n = len(boxes)
    unlocked_boxes = [0]  # Starting with the first box as unlocked
    
    keys = set(boxes[0])  # Collecting keys from the first box
    
    while keys:
        new_key = keys.pop()
        if 0 <= new_key < n and new_key not in unlocked_boxes:
            unlocked_boxes.append(new_key)
            keys.update(boxes[new_key])
            
    return len(unlocked_boxes) == n

