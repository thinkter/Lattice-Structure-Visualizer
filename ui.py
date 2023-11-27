import pygame
import pygame_gui
from pygame_gui.ui_manager import UIManager
from pygame_gui.elements.ui_text_box import UITextBox
from pygame_gui.core import IncrementalThreadedResourceLoader, ObjectID
pygame.init()

pygame.display.set_caption('Lattice Visualizer')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#FFFFFF'))
loader = IncrementalThreadedResourceLoader()
uimanager = pygame_gui.UIManager((800, 600) , 'data/themes/theme_1.json', resource_loader= loader)
uimanager.add_font_paths("Montserrat",
                          "data/fonts/Montserrat-Regular.ttf",
                          "data/fonts/Montserrat-Bold.ttf",
                          "data/fonts/Montserrat-Italic.ttf",
                          "data/fonts/Montserrat-BoldItalic.ttf")

uimanager.preload_fonts([{'name': 'Montserrat', 'html_size': 4.5, 'style': 'bold'},
                          {'name': 'Montserrat', 'html_size': 4.5, 'style': 'regular'},
                          {'name': 'Montserrat', 'html_size': 2, 'style': 'regular'},
                          {'name': 'Montserrat', 'html_size': 2, 'style': 'italic'},
                          {'name': 'Montserrat', 'html_size': 6, 'style': 'bold'},
                          {'name': 'Montserrat', 'html_size': 6, 'style': 'regular'},
                          {'name': 'Montserrat', 'html_size': 6, 'style': 'bold_italic'},
                          {'name': 'Montserrat', 'html_size': 4, 'style': 'bold'},
                          {'name': 'Montserrat', 'html_size': 4, 'style': 'regular'}
                          ])

text2 = UITextBox('<textarea name = "a" color:#FFFFFF><font face=fira_code size=30 color=#FFFFFF> <b><center> LATTICE VIEWER PROGRAM </center> </b> </textarea> ' ,
pygame.Rect((250, 50), (200, 50),
manager = uimanager, 
object_id=ObjectID(class_id="@white_text_box",
object_id="#text_box_2"  )))
text = UITextBox('<textarea name = "a" color:#FFFFFF><font face=fira_code size=30 color=#FFFFFF><center> Lattice Viewer Program Lattice structures are topologically ordered, three-dimensional open-celled structures composed of one or more repeating unit cells here there are two structures FCC and BCC</center></textarea> ' ,
pygame.Rect((50, 125), (750, 100),
manager = uimanager, 
object_id=ObjectID(class_id="@white_text_box",
object_id="#text_box_2"  )))

fcc = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((235, 250), (350, 50)),
text='Face Centric Lattice'  ,
manager=uimanager)


bcc = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((235, 350), (350, 50)),
text='Body Centric Lattice',
manager=uimanager)

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
      uimanager.process_events(event)
      uimanager.update(time_delta)
      window_surface.blit(background, (0, 0))
      uimanager.draw_ui(window_surface)
      pygame.display.update()