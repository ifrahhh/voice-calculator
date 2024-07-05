from tkinter import *
import math as m
from pygame import mixer
import speech_recognition
import threading

def click(value):
    ex = entryField.get()
    answer = ''

    try:

        if value == "C":
            ex = entryField.get()
            ex = ex[0:len(ex) - 1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == "CE":
            entryField.delete(0, END)
            return


        elif value == '√':
            answer = m.sqrt(eval(ex))
        elif value == 'x!':
            answer = m.factorial(eval(ex))
        elif value == 'sinθ':
            answer = str(m.sin(eval(ex)))
        elif value == 'cosθ':
            answer = str(m.cos(eval(ex)))
        elif value == 'tanθ':
            answer = str(m.tan(eval(ex)))
        elif value == 'π':
            answer = m.pi
        elif value == '2π':
            answer = 2 * (m.pi)
        elif value == "ln":
            answer = m.log2(eval(ex))
        elif value == 'log₁₀':
            answer = m.log10(eval(ex))
        elif value == 'e':
            answer = m.e
        elif value == 'deg':
            answer = m.degrees(eval(ex))
        elif value == "rad":
            answer = m.radians(eval(ex))
        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)
        elif value == 'x\u00B2':
            answer = eval(ex) ** 2
        elif value == 'x\u00B3':
            answer = eval(ex) ** 3
        elif value == 'sinh':
            answer = m.sinh(eval(ex))
        elif value == 'cosh':
            answer = m.cosh(eval(ex))
        elif value == 'tanh':
            answer = m.tanh(eval(ex))

        elif value == '=':
            answer = eval(ex)

        if answer != '':
            entryField.delete(0, END)
            entryField.insert(0, answer)
            return

        if value == chr(247):
            entryField.insert(END, "/")
            return

        elif value == 'x\u02b8':
            entryField.insert(END, "**")
            return

        else:
            entryField.insert(END, value)

    except SyntaxError:
        pass


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b
def sqrt(a):
    return a**(1/2)
def pow(a,b):
    return a**b

def lcm(a, b):

    L = a if a > b else b
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1

def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1

def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l


def audio():
    print("Listening audio...")
    mixer.init()
    mixer.music.load('music1.mp3')
    mixer.music.play()

    sr=speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m, duration=0.01)
            audio = sr.listen(m)
            text= sr.recognize_google(audio)
            print("You spoke :",text)
            mixer.music.load('music2.mp3')
            mixer.music.play()


            for word in text.split(' '):
                if word.upper() in operations.keys():
                    try:
                        l = extraxt_from_text(text)
                        r = operations[word.upper()](l[0] , l[1])
                        entryField.delete(0,END)
                        entryField.insert(0,r)
                    except:
                        print('hello')

                else:
                    pass

        except Exception as e:
            print(e)

def audio_thread():

    t = threading.Thread(target=audio)
    t.setDaemon = True
    t.start()



############################################################################################

operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,'POWER' : pow,'ROOT' : sqrt,
                  'REMAINDER':mod , 'MODULUS':mod}

root = Tk()
root.geometry('680x486+100+100')
root.title("Voice Calculator ")
root.configure(background="dodgerblue3")

root.resizable(width=False, height=False)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(root, image=logoImage, bg='dodgerblue3')
logoLabel.grid(row=0, column=0)

entryField = Entry(root, font=("arial", "20", "bold"), bg="dodgerblue3", fg='white', bd=10,relief=SUNKEN,
                   width=30, justify=RIGHT)
entryField.grid(row=0, column=0, columnspan=8, pady=1)

micImage = PhotoImage(file='microphone.png')
micButton = Button(root, image=micImage, bd=0, bg='dodgerblue3', activebackground='dodgerblue3',
                   cursor='hand2',command=audio_thread)
micButton.grid(row=0, column=7)

button_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
               "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
               "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
               "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
               "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]

temp = 1
rowvalue = 1
columnvalue = 0

for i in button_list:
    btn = Button(root, width=5, height=2, bg='dodgerblue3', font=("arial", "18", "bold"), bd=2, fg='white'
                 , relief=SUNKEN, text=i, command=lambda button=i: click(button))
    btn.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
