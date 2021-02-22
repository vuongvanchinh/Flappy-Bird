from objects import Entity

a = Entity(206, 0, 100, 465)
b = Entity(150, 507.91, 60, 45)
c = Entity(206, 546, 100, 54)

print(c.collide_with(b))