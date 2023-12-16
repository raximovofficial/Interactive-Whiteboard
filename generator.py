import random
from NeuralNetworkUse import UseThisShit
from PIL import Image
import numpy as np

def GiveMeQuestion():
    r = random.randrange(4)
    str = ""
    x = 0
    if r==0:
        # ko'paytirish
        a = random.randrange(1, 10)
        b = random.randrange(0, 10)
        x = a * b
        str = f"{a} * {b} = "
    elif r==1:
        # bo'lish
        x = random.randrange(1, 10)
        b = random.randrange(1, 12)
        a = x * b
        str = f"{a} / {b} = "
    elif r==2:
        # qo'shish
        a = random.randrange(0, 100)
        b = random.randrange(0, 100)
        x = a + b
        str = f"{a} + {b} = "
    else:
        # ayirish
        a = random.randrange(0, 100)
        b = random.randrange(0, 100)
        a, b = max(a, b), min(a, b)
        x = a - b
        str = f"{a} - {b} = "
    
    return (str, x)

def Tekshirish(data):
    img = Image.frombytes('RGB', (50, 50), data)

    img = img.resize((28, 28))
    img = img.convert('L')
    arr = np.array(img).reshape(784)

    return str(UseThisShit(arr))







GiveMeQuestion()