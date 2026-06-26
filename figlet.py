import pyfiglet
import sys
import random
def main():
    Ip = input("Input: ")
    print(converter(Ip))


def converter(x):
    if len(sys.argv) == 1:
        fonts = pyfiglet.FigletFont.getFonts()
        random_font = random.choice(fonts)
        f = pyfiglet.figlet_format(x, font=random_font)
        return f
    elif len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
            font_name = sys.argv[2]
            if (font_name in pyfiglet.FigletFont.getFonts()):
                f = pyfiglet.figlet_format(x, font=font_name)
            else:
                sys.exit("invalid font name")
            return f
    else:
        sys.exit("invalid Arguments")
        


main()