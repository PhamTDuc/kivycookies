from platform import system
import sys
if "win" in system().lower():  # works for Win7, 8, 10 ...
    from ctypes import windll
    k = windll.kernel32
    k.SetConsoleMode(k.GetStdHandle(-11), 7)

escape_code = '\033[0'
pallette = {'escape': escape_code + 'm', 'red': escape_code + ';31m', 'blue': escape_code + ';34m', 'green': escape_code + ';32m', 'yellow': escape_code + ';33m', 'magenta': escape_code + ';35m', 'cyan': escape_code + ';36m', 'white': escape_code + ';37m'}
print escape_code + ';43m' + 'Hello the world' + pallette['escape']
print pallette['green'] + 'Hello the world' + pallette['escape']
print pallette['red'] + 'Hello the world' + pallette['escape']
print pallette['yellow'] + 'Hello the world' + pallette['escape']
print pallette['blue'] + 'Hello the world' + pallette['escape']
print pallette['cyan'] + str(sys.argv[1:]) + pallette['escape']
