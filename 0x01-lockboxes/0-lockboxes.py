#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)

# def canUnlockAll(boxes):
#    """ FUnction to unlock boxes"""
#   seen = set()
#   seen.add(0)
#   stack = [0]
#   while stack:
#       current_box = stack.pop()
#       for key in boxes[current_box]:
#           if key not in seen:
#               seen.add(key)
#               stack.append(key)
#   return len(seen) == len(boxes)
