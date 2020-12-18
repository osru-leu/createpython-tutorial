class GfG:
    name = 'GeeksforGeeks'
    age = 24

obj = GfG()

print('The name is ' + getattr(obj, 'name'))