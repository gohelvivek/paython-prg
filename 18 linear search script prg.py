lst = [2,5,3,1,7]
num = 1
for index,value in enumerate(lst):
    if num==value:
        print(f"{value} found at position {index+1}")
