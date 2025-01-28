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
        key = lst[i]
        j = i - 1

        # Highlight the key element
        draw_colored_list(draw_info, draw_info.BLUE, i, key)
        pygame.time.delay(500)
        # Compare and shift elements to make space for the key
        while j >= 0 and (
            (lst[j] > key and ascending) or 
            (lst[j] < key and not ascending)
        ):
            # Highlight the comparing element
            draw_colored_list(draw_info, draw_info.GREEN, j, lst[j])
            pygame.time.delay(400)

            # Shift the comparing element to the right
            lst[j + 1] = lst[j]

            # Visualize the list after shifting
            draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.BLUE}, clear_bg=True)
            pygame.time.delay(50)

            j -= 1

        # Place the key element in its correct position
        lst[j + 1] = key

        # Highlight the final position of the key element
        draw_colored_list(draw_info, draw_info.BLUE, j + 1, key)
        pygame.time.delay(300)

        yield True  # Yield control back to the main loop for visualization

    return lst



# def shell_sort(draw_info, ascending=True):
#     lst = draw_info.lst
#     n = len(lst)
#     gap = n // 2  # Start with a large gap and reduce it

#     while gap > 0:
#         for i in range(gap, n):
#             temp = lst[i]
#             j = i
#             draw_colored_list(draw_info, draw_info.BLUE, i, temp)
#             draw_colored_list(draw_info, draw_info.BLUE, i - gap, lst[i - gap])
#             pygame.time.delay(500)
#             yield True 
#             # Compare and swap elements while maintaining the gap
#             while j >= gap and (
#                 (lst[j - gap] > temp and ascending) or
#                 (lst[j - gap] < temp and not ascending)
#             ):
#                 # Highlight the element being compared
#                 draw_colored_list(draw_info, draw_info.RED, j , lst[j - gap])
#                 draw_colored_list(draw_info, draw_info.GREEN, j - gap, lst[j - gap])
#                 pygame.time.delay(300)

#                 # Swap and visually update
#                 lst[j] = lst[j - gap]
#                 draw_list(draw_info, {j: draw_info.RED, j - gap: draw_info.GREEN}, True)
#                 #pygame.time.delay(300)

#                 j -= gap
#             lst[j] = temp
#             yield True
#             # Update the key element's final position
#             # draw_colored_list(draw_info, draw_info.BLUE, j, lst[j])
#             # pygame.time.delay(100)

#             #yield True  # Yield control back to the main loop for visualization

#         # Reduce the gap for the next iteration
#         gap //= 2

#     return lst

def shell_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    gap = n // 2  # Start with a large gap and reduce it

    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i

            # Generate gradient colors for the current sublist
            sublist_indices = list(range(i % gap, n, gap))  # Indices of the current sublist
            gradient_colors = generate_gradient_colors(len(sublist_indices), base_color=(0, 255, 0))
            sublist_colors = {sublist_indices[k]: gradient_colors[k] for k in range(len(sublist_indices))}

            # Highlight the current element being sorted
            draw_list(draw_info, {**sublist_colors, i: draw_info.BLUE}, clear_bg=True)
            pygame.time.delay(300)
            yield True

            # Perform insertion-like sorting within the sublist
            while j >= gap and (
                (lst[j - gap] > temp and ascending) or
                (lst[j - gap] < temp and not ascending)
            ):
                # Highlight the elements being compared
                draw_colored_list(draw_info, draw_info.RED, j, lst[j])
                draw_colored_list(draw_info, draw_info.RED, j - gap, lst[j - gap])
                pygame.time.delay(200)

                # Swap elements
                lst[j] = lst[j - gap]

                # Update the list, keeping the sublist colors intact
                draw_list(draw_info, {**sublist_colors, j: draw_info.RED, j - gap: draw_info.RED}, clear_bg=True)
                pygame.time.delay(200)

                j -= gap

            lst[j] = temp

            # Redraw the list after placing the key element
            draw_list(draw_info, {**sublist_colors, j: draw_info.BLUE}, clear_bg=True)
            pygame.time.delay(200)
            yield True

        gap //= 2  # Reduce the gap for the next iteration

    return lst



