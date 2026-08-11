# map()

def get_cube(num):
    return num **3

ls = [1,2,9,3,5]

map_obj =map(get_cube,ls)

list(map_obj)
