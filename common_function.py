from pygame import display, image, mixer, transform, font

def draw_image(screen ,img, x, y, w, h):
    img = transform.scale(img, (w, h))
    screen.blit(img, x, y)

def draw_text(screen, font_letter, content, x = 0, y = 0):
    l_font = font.SysFont(font_letter)
    suface = l_font.render(content, True, (255, 255, 255))
    screen.blit(suface, x, y)

def play_music(music):
    music.play()
    
