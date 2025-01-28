import pygame
from models import *

pygame.init()

def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            # Highlight the elements being compared
            draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, clear_bg=True)
            pygame.time.delay(300)  # Add a small delay for visualization
            
            # Swap elements if needed based on the sorting order
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

                # Show the updated list after the swap
                draw_list(draw_info, {j: draw_info.RED, j + 1: draw_info.GREEN}, clear_bg=True)
                pygame.time.delay(100)

                yield True  # Yield control back to the main loop after each significant step
    
    return lst

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]  # The key element
        j = i

        # Highlight the key element before any comparisons
        draw_list(draw_info, {i: draw_info.RED}, clear_bg=True)
        pygame.time.delay(300)

        while j > 0:
            # Conditions for ascending and descending order
            ascending_sort = lst[j - 1] > current and ascending
            descending_sort = lst[j - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            # Highlight the comparing element
            draw_list(draw_info, {j: draw_info.RED, j - 1: draw_info.GREEN}, clear_bg=True)
            pygame.time.delay(300)

            # Shift the element (but only visually here for comparison)
            lst[j] = lst[j - 1]

            # Yield control for visualization
            yield True

            j -= 1

        # Place the key element in its correct position
        lst[j] = current

        # Highlight the final position of the key element
        draw_list(draw_info, {j: draw_info.BLUE}, clear_bg=True)
        pygame.time.delay(300)

        yield True  # Yield control after placing the key element

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
