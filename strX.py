def change_string(s):
    s = "X" + s[1:]
    return s

og = "hello"
print("Before function:", og)
new_string = change_string(og)
print("Returned from function:", new_string)
print("After function (og):", og)
