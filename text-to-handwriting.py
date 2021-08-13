from PIL import Image
from fpdf import FPDF
from PIL import Image
import os

BG = Image.open("handfont/background.png")
sizeOfSheet = BG.width
gap, _ = 0, 0
allowedChars = ',.-?!() 1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'


def writee(char):
    global gap, _
    if char != '\n':
        cases = Image.open("handfont/%s.png" % char.lower())
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size


def letterwrite(word):
    global gap, _
    if gap > sizeOfSheet - 95 * (len(word)):
        gap = 0
        _ += 200
    special_char = {'.': 'fullstop', '!': 'exclamation', '?': 'questionmark', ',': 'comma', '(': 'bracketleft',
                    ')': 'bracketright', '-': 'minus', '+': 'plus'}
    for letter in word:
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'
            elif special_char[letter] is not None:
                letter = special_char[letter]
            writee(letter)


def worddd(Input):
    wordlist = Input.split(' ')
    for i in wordlist:
        letterwrite(i)
        writee('space')


if __name__ == '__main__':
    try:
        data = input()

        with open('handwriting_output.pdf', 'w') as file:
            pass

        l = len(data)
        nn = len(data) // 600
        chunks, chunk_size = len(data), len(data) // (nn + 1)
        p = [data[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

        for i in range(0, len(p)):
            print(p[i])
            worddd(p[i])
            writee('\n')
            BG.save('%doutputimage.png' % i)
            BG1 = Image.open("handfont/background.png")
            BG = BG1
            gap = 0
            _ = 0
    except ValueError as E:
        print("{}\nTry again".format(E))

imagelist = []
for i in range(0, len(p)):
    imagelist.append('%doutputimage.png' % i)


def pdf_creation(PNG_FILE, flag=False):
    imagea = Image.open(PNG_FILE)
    image = Image.new('RGB', imagea.size, (255, 255, 255))
    image.paste(imagea, mask=imagea.split()[3])
    image.save('handwriting_output.pdf',
             append=flag)


pdf_creation(imagelist.pop(0))

for PNG_FILE in imagelist:
    pdf_creation(PNG_FILE, flag=True)
