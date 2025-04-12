filename = 'test'

with open(filename, 'r') as file:
    content = file.read()
    print(content)
    

with open('info', 'w') as file:
    content = "Some info text from `with.py` file"
    file.write(content)
    