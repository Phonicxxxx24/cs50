def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    op =""
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for i in word:
        if(i not in vowels):
            op += i
    return op
        


if __name__ == "__main__":
    main()