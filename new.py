from api_func import get_map_image_by_ll_z, show_image
ll = input("Введи координаты через запятую ")
z = int(input("Введи мастшаб от 0 до 21 "))
image = get_map_image_by_ll_z(ll, z)
show_image(image)