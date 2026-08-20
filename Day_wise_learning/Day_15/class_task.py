lst = ["a","b","c","d"]

def get_element(index):
    return lst[index]

try:
    get_element(6)
except IndexError:
    print(lst[-1])