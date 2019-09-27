
# To Activate venv enter source myvenv/bin/activate
def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Jessica']
for name in girls:
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print(i)


print('Hello, Django girls!')