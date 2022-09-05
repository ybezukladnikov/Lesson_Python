#Задача №5. Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.


ax,ay = map(int,(input("Input coordinate X and Y point A between space: ").split()))
bx,by = map(int,(input("Input coordinate X and Y point B between space: ").split()))

distance = ((ax-bx)**2+(ay-by)**2)**0.5

print(round(distance,2))
