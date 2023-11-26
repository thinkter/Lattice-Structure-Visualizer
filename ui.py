import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Lattice Visualizer')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#FFFFFF'))

manager = pygame_gui.UIManager((800, 600))

fcc = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 175), (100, 50)),
                                             text='fcc',
                                             manager=manager)


bcc = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='bcc',
                                             manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
   time_delta = clock.tick(60)/1000.0
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         is_running = False
         
      if event.type == pygame_gui.UI_BUTTON_PRESSED:
         if event.ui_element == fcc:
            exec(open("FCC.py").read())
         if event.ui_element  == bcc:
            exec(open("BCC.py").read())
      manager.process_events(event)
      manager.update(time_delta)
      window_surface.blit(background, (0, 0))
      manager.draw_ui(window_surface)
      pygame.display.update()