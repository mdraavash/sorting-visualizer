import pygame 
from models import *
from sort import *
pygame.init()

run = True
clock = pygame.time.Clock()
n=10
min_val = 0
max_val = 95
sorting = False
ascending = True

sorting_algorithm = bubble_sort
sorting_algorithm_name = "bubble sort"
sorting_algorithm_generator = None

lst = generate_starting_list(n, min_val, max_val)
draw_info = DrawInformation(800, 600, lst)

clicked = False

while run:
    clock.tick(60) #clock time 

    if sorting:   #using the generator to sort the array
        try: 
            #next(sorting_algorithm_generator)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and not clicked:  # Detect the Left Arrow Key
                    clicked = True
                    next(sorting_algorithm_generator)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:  # Detect Left Arrow Key Release
                    clicked = False
        except StopIteration:
            sorting = False
    else:
        draw(draw_info, sorting_algorithm_name, ascending)

    draw(draw_info, sorting_algorithm_name, ascending)

    for event in pygame.event.get(): #gets lists of events from last loop and stores it in event
        if event.type == pygame.QUIT:
            run = False
            
        if event.type != pygame.KEYDOWN:
            continue

        if event.key == pygame.K_r:
            lst = generate_starting_list(n, min_val, max_val)
            draw_info.set_list(lst)
            sorting = False

        elif event.key == pygame.K_SPACE and sorting == False:
            sorting = True
            sorting_algorithm_generator = sorting_algorithm(draw_info , ascending)
            
        elif event.key == pygame.K_a and not sorting:
            ascending = True
            
        elif event.key == pygame.K_d and not sorting:
            ascending = False

        elif event.key == pygame.K_i and not sorting:
            sorting_algorithm = insertion_sort
            sorting_algorithm_name = "Insertion sort"

        elif event.key == pygame.K_b and not sorting:
            sorting_algorithm = bubble_sort
            sorting_algorithm_name = "Bubble sort"

        elif event.key == pygame.K_s and not sorting:
            sorting_algorithm = shell_sort
            sorting_algorithm_name = "Shell sort"

pygame.quit() 

