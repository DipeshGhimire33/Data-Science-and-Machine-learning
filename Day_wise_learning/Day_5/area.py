

def are_cub(l,b,h)->float:
    area =(2*(l*b+b*h+l*h))
    return area
print(are_cub(4,5,6))


# same in lambda

area = lambda l,b,h : 2*(l*b+b*h+l*h)
print(area(4,5,6))