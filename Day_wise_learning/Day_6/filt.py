# filter()

ls = [1,2,9,3,5]

filter_obj= filter(lambda num: num%2 == 0,ls )
list(filter_obj)

filter_obj= filter(lambda num: num%2 != 0,ls )
list(filter_obj)
