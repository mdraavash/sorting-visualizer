import pygame
from models import *

pygame.init()

def bubble_sort(draw_info, ascending= True):
    lst = draw_info.lst
    
    for i in range (len(lst) -1 ):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j+1]
            draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j +1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True #to gain control during sorting by initializing a generator
    
    return lst

def insertion_sort(draw_info, ascending= True):
    lst = draw_info.lst
    for i in range (1, len(lst)):
        current = lst [i]

        while True:
            ascending_sort = i > 0 and lst[i -1] > current and ascending 
            descending_sort = i > 0 and lst[i-1] < current and not ascending 

            if not ascending_sort and not descending_sort:
                break
            lst[i] = lst [i-1]
            i =i - 1
            lst[i] = current
            draw_list(draw_info, {i -1 : draw_info.GREEN, i : draw_info.RED}, True)
            yield True #to gaaian control during sorting by initializing a generator
    
    return lst
def shell_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    gap = n // 2  # Ensure integer division

    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i

            # Sort based on ascending or descending order
            while j >= gap and ((lst[j - gap] > temp and ascending) or (lst[j - gap] < temp and not ascending)):
                lst[j] = lst[j - gap]
                j -= gap
            
            lst[j] = temp

            # Visualize the sorting process
            draw_list(draw_info, {j: draw_info.GREEN, i: draw_info.RED}, True)
            yield True

        gap //= 2  # Reduce the gap

    return lst
