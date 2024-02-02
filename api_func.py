import requests
from io import BytesIO
import pygame

STATIC_API_URL = "http://static-maps.yandex.ru/1.x/"
GEOCODER_API_URL = "http://geocode-maps.yandex.ru/1.x/"
GEOCODER_API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"


class Map:
    def __init__(self, ll, z):
        self.ll = ll
        self.z = z

    def get_map_image_by_ll_z(self):
        static_api_params = {
            "l": "map",
            "ll": self.ll,
            "z": str(self.z)
        }

        response = requests.get(STATIC_API_URL, static_api_params)
        return response.content

    def show_image(self):
        pygame.init()
        image = pygame.image.load(BytesIO(self.get_map_image_by_ll_z()))
        image_rect = image.get_rect()
        width, height = image_rect[2], image_rect[3]
        screen = pygame.display.set_mode((width, height))
        screen.blit(image, (0, 0))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.z in range(0, 20):
                            self.z += 1
                            image = pygame.image.load(BytesIO(self.get_map_image_by_ll_z()))
                            image_rect = image.get_rect()
                            width, height = image_rect[2], image_rect[3]
                            screen = pygame.display.set_mode((width, height))
                            screen.blit(image, (0, 0))
                    if event.key == pygame.K_DOWN:
                        if self.z in range(1, 22):
                            self.z -= 1
                            image = pygame.image.load(BytesIO(self.get_map_image_by_ll_z()))
                            image_rect = image.get_rect()
                            width, height = image_rect[2], image_rect[3]
                            screen = pygame.display.set_mode((width, height))
                            screen.blit(image, (0, 0))
            pygame.display.flip()
