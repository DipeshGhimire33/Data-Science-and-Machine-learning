def prnt_all(*args):
    print("arguments")
    return(args)

print(prnt_all(1,5,"hi",3,4))


def sum_all(*num):
    return(sum(num))

print(sum_all(1,5,4.6,32,0.55))


def prnt_kwarg(**kwargs):
    print("keyword Args")
    print(kwargs)

prnt_kwarg(num1=1,num2=5)

def calcu_area(shape:str, **kwargs):
    area=0
    if shape == "square":
        area = kwargs.get("length",0)**2

    elif shape == "rectangle":
        if "length"and"bredth" in kwargs.keys():
            area = kwargs.get("length", 0)* kwargs.get("bredth", 0)
    else:
        print(f"{shape} is not supported")
    return area

print(calcu_area("rectangle",length=15,bredth=20)) 

