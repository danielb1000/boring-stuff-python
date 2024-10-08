'''
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list ''[] is passed to your function.
'''

empty = []
spam = ['apples', 'bananas', 'tofu', 'cats']

def commalise(lista):
    if len(lista) == 0:
        return "Nothing"
    else:
        result = ", ".join(lista[0:-1])
        result += f" and {lista[-1]}"

    return result

print(commalise(["a","b"]))
print(commalise(spam))
print(commalise(empty))