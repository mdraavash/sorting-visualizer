import pygame
import random
#from sort import *
pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BLUE = 0, 0, 255
    BACKGROUND_COLOR = WHITE 

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FONT = pygame.font.SysFont('comicsans', 20)
    LARGE_FONT = pygame.font.SysFont('comicsans', 25)
    INNER_FONT = pygame.font.SysFont('comicsans', 15)
    SIDE_PAD = 100 #settin up side and top padding 
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width #setting width and height of the screen 
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = int((self.width - self.SIDE_PAD) / len(lst)) #give area of the block
        self.block_height = int((self.height - self.TOP_PAD) / (self.max_val - self.min_val))  #gives height of block
        self.start_x = self.SIDE_PAD // 2 #starting of the block in x axis 

def generate_gradient_colors(length, base_color=(0, 255, 0)):
    """
    Generate a gradient of green colors.
    :param length: Number of colors to generate.
    :param base_color: Base RGB color to create gradients from.
    :return: List of gradient colors.
    """
    max_intensity = base_color[1]  # Green intensity
    step = max_intensity // length  # Step to reduce intensity

    gradient_colors = [
        (0, max_intensity - i * step, 0) for i in range(length)
    ]
    return gradient_colors

def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(
        f"{algo_name} - {'Ascending' if ascending else 'Descending'}",
        1, draw_info.GREEN)
    draw_info.window.blit(title , (draw_info.width / 2 - title.get_width() / 2 , 5))

    controls = draw_info.FONT.render(
        "R - Reset | SPACE - Start sorting | A - Ascending | D - Descending",
        1, draw_info.BLACK)
    draw_info.window.blit(controls , (draw_info.width / 2 - controls.get_width() / 2 , 35))

    sorting = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort | S- Shell Short",
        1, draw_info.BLACK)
    draw_info.window.blit(sorting , (draw_info.width / 2 - sorting.get_width() / 2 , 65))
    
    draw_list(draw_info)
    pygame.display.update()        

def draw_list(draw_info, color_positions={}, clear_bg =  False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD,
                       draw_info.width - draw_info.SIDE_PAD,
                       draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height 
        
        color = draw_info.GRADIENTS[i % 3] 

        if i in color_positions:
            color = color_positions[i] 
        
        pygame.draw.rect(draw_info.window, 
                         color, 
                         (x, y-2, draw_info.block_width, draw_info.height - y)
                        )      
        value = draw_info.INNER_FONT.render(
        f"{val}",1, draw_info.BLACK)
        text_x = x + (draw_info.block_width - value.get_width()) / 2  # Center the text horizontally in the block
        text_y = y - value.get_height() + 30  # Position text slightly above the block
        draw_info.window.blit(value, (text_x, text_y))
    if clear_bg:
        pygame.display.update()

def draw_colored_list(draw_info, color, i=0, val=0):
    # Calculate the position and size of the block
    x = draw_info.start_x + i * draw_info.block_width
    y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
    
    # Draw the block
    pygame.draw.rect(
        draw_info.window,
        color,
        (x, y, draw_info.block_width, draw_info.height - y)
    )
    
    # Render the value inside or near the block
    value = draw_info.INNER_FONT.render(f"{val}", 1, draw_info.BLACK)
    text_x = x + (draw_info.block_width - value.get_width()) / 2  # Center the text horizontally in the block
    text_y = y - value.get_height() + 30  # Position text slightly above the block
    draw_info.window.blit(value, (text_x, text_y))
    
    # Update the display
    pygame.display.update()


def generate_starting_list(n, min_val, max_val): #no of list,maximim value, minimum value 
    
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        val += 5
        lst.append(val)

    return lst