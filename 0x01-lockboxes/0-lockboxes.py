#!/usr/bin/python3
'''Module for lockboxes problem'''



def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened'''
    keys = [0]
    total_boxes = len(boxes)
    index = 0
    counter = 0

    while index < len(keys):
        key = keys[index]
        for k in boxes[key]:
            if 0 < k < total_boxes and k not in keys:
                keys.append(k)
                counter += 1
        
        index += 1

    return counter == total_boxes - 1
