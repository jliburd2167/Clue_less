import pygame
import requests

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Clue Game Client')

# Function to send a message
def send_message(content):
    response = requests.post('http://your-server-url/messages/', data={'content': content})
    return response.json()

running = True
input_box = pygame.Rect(100, 100, 200, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
messages = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    response = send_message(text)
                    messages.append(response.get('message'))  # Append the sent message
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.fill((30, 30, 30))
    txt_surface = pygame.font.Font(None, 32).render(text, True, color)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, color, input_box, 2)

    # Display messages
    for i, message in enumerate(messages):
        message_surface = pygame.font.Font(None, 24).render(message, True, (255, 255, 255))
        screen.blit(message_surface, (10, 150 + i * 20))

    pygame.display.flip()

pygame.quit()