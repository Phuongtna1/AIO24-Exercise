def my_function(x):
    string = ''
    for i in range(len(x)-1, -1, -1):
        string += x[i]
    return string


x = 'I can do it'
assert my_function(x) == "ti od nac I"
x = 'apricot'
print(my_function(x))
