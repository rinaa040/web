from api_func import Map
ll = input("Введи координаты через запятую ")
z = int(input("Введи мастшаб от 0 до 21 "))
image = Map(ll, z)
image.show_image()
# 56.8498,53.2045