import pygame
pygame.init()

# Размер окна, название, цвет мяча, цвет фона
window_size = (800, 600) 
screen = pygame.display.set_mode(window_size) 
pygame.display.set_caption("Draw circle")
ball_color = pygame.Color('red')
bg_color = pygame.Color('white')

ball_pos = [400, 300]  # Начальная позиция мяча

ball_radius = 25  # Радиус мяча

speed = 20  # Скорость мяча

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()  # Получаем состояние всех клавиш
    if keys[pygame.K_UP]: 
        ball_pos[1] = max(ball_pos[1] - speed, ball_radius)  # Движение вверх
    if keys[pygame.K_DOWN]:
        ball_pos[1] = min(ball_pos[1] + speed, window_size[1] - ball_radius)  # Движение вниз
    if keys[pygame.K_LEFT]:
        ball_pos[0] = max(ball_pos[0] - speed, ball_radius)  # Движение влево
    if keys[pygame.K_RIGHT]:
        ball_pos[0] = min(ball_pos[0] + speed, window_size[0] - ball_radius)  # Движение вправо
    
    screen.fill(bg_color)  # Заполняем фон
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)  # Рисуем мяч
    pygame.display.flip()  # Обновляем экран
    pygame.time.Clock().tick(24)  # Ограничиваем FPS до 24 кадров в секунду
