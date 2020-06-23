filename = 'hello-world.txt'

hello = 'Hello, world.'
with open(filename, 'w') as f:
   f.write(hello)

goodbye = '\nGoodbye!'
with open(filename, 'a') as f:
    f.write(goodbye)



