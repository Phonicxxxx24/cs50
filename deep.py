que = input("Great Question of Life, the Universe and Everything: ")
que = que.lower()
check = ['forty two','42','forty-two']
if (que in check):
    print('Yes')
else:
    print('No')