from colorama import init
from termcolor import colored
import os
import sys
import traceback

init()

# ========= Colored Type Prints ===========

def cprint(message, fg="red", bg="", attrs=[], end="\n", v=True):
    if v:
        print(colored(message, fg, attrs=attrs), end=end)

# Error Print
def eprint(message, end="\n", v=True):
    if v:
        cprint(message, fg="red", end=end)

# Header Print
def hprint(message, end="\n", v=True):
    if v:
        cprint(message, fg="green", end=end)

# Message Print
def mprint(message, end="\n", v=True):
    if v:
        cprint(message, fg="blue", end=end)


# Settings print - a yellow msg, followed by a white info
def sprint(msg, setting, ljust_num=25, v=True):
    cprint("\t* " + str(msg).ljust(ljust_num), fg="yellow", attrs=['bold'], end=": ", v=v)
    cprint(str(setting), fg="white", v=v)


# ========= Colors ===========

# Red Print
def rprint(message, end="\n", v=True):
    if v: cprint(message, fg="red", attrs=['bold'], end=end)

# Yellow Print
def yprint(message, end="\n", v=True):
    if v: cprint(message, fg="yellow", attrs=['bold'], end=end)

# Green Print
def gprint(message, end="\n", v=True):
    if v: cprint(message, fg="green", end=end)

# Blue Print
def bprint(message, end="\n", v=True):
    if v: cprint(message, fg="blue", end=end)

# Purple Print
def prprint(message, end="\n", v=True):
    if v: cprint(message, fg="magenta", end=end)





# ========= Misc / No Colors ===========

# Debug Print
def dprint(msg, indent="\t\t", v=True):
    if v: print(indent, msg)

# Verbose print - print only if v.
def vprint(msg, v=True):
    if v: print(msg)

# Error traceback
def show_error_file_and_line():
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    eprint("Error:")
    sprint(exc_type, fname)
    print(exc_tb.tb_lineno)
    print(traceback.format_exc())
