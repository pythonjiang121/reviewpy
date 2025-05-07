import pygame
import random

FONT_PX = 15
pygame.init()

# 获取屏幕信息
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# 初始窗口大小
window_width = 500
window_height = 600
is_fullscreen = False

# 创建窗口
winSur = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("数字雨")

font = pygame.font.SysFont('fangsong', 40)

# 创建按钮
button_font = pygame.font.SysFont('fangsong', 16)
fullscreen_text = button_font.render("全屏(F11)", True, (0, 255, 0))
button_rect = fullscreen_text.get_rect()
button_rect.topleft = (10, 10)


def toggle_fullscreen():
    global is_fullscreen, winSur, window_width, window_height
    is_fullscreen = not is_fullscreen

    if is_fullscreen:
        winSur = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    else:
        winSur = pygame.display.set_mode((window_width, window_height))


# 背景设置
def create_bg_surface(width, height):
    bg_surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)
    pygame.Surface.convert(bg_surface)
    bg_surface.fill(pygame.Color(0, 0, 0, 13))
    return bg_surface


bg_suface = create_bg_surface(window_width, window_height)
winSur.fill((0, 0, 0))

# 数字
texts = [font.render(str(i), True, (0, 255, 0)) for i in range(10)]
colums = int(window_width / FONT_PX)
drops = [0 for i in range(colums)]

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                toggle_fullscreen()
                # 更新列数和背景
                current_width = screen_width if is_fullscreen else window_width
                current_height = screen_height if is_fullscreen else window_height
                colums = int(current_width / FONT_PX)
                drops = [drops[i] if i < len(drops) else 0 for i in range(colums)]
                bg_suface = create_bg_surface(current_width, current_height)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                toggle_fullscreen()
                # 更新列数和背景
                current_width = screen_width if is_fullscreen else window_width
                current_height = screen_height if is_fullscreen else window_height
                colums = int(current_width / FONT_PX)
                drops = [drops[i] if i < len(drops) else 0 for i in range(colums)]
                bg_suface = create_bg_surface(current_width, current_height)

    # 绘制背景
    winSur.blit(bg_suface, (0, 0))

    # 绘制全屏按钮
    pygame.draw.rect(winSur, (0, 50, 0), button_rect)
    winSur.blit(fullscreen_text, button_rect.topleft)

    # 绘制数字雨
    current_width = screen_width if is_fullscreen else window_width
    current_height = screen_height if is_fullscreen else window_height

    for i in range(len(drops)):
        if i * FONT_PX < current_width:  # 确保数字不会超出屏幕
            text = random.choice(texts)
            winSur.blit(text, (i * FONT_PX, drops[i] * FONT_PX))
            drops[i] += 2
            if drops[i] * FONT_PX > current_height or random.random() > 0.95:
                drops[i] = 0

    pygame.display.flip()
    clock.tick(30)  # 限制帧率为30FPS