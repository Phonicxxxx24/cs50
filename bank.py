greetings = input("Greetings: ")
greetings = greetings.lower().strip()
if (greetings.startswith('hello')):
    print('00$')
elif(greetings.startswith('h')):
    print('20$')
else:
    print('100$')