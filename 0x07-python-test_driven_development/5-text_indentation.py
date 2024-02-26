#!/usr/bin/python3
"""Module for indenting text all of tests are found in /tests"""


def text_indentation(text):
    """text indentation
    Args:
        text (str): the text to mainapulate
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    last_in = 0
    mov_in = 0
    flag = 0
    mystring = ""
    the_length = len(text)

    while mov_in < the_length:
        flag = 1
        if text[mov_in] == "." or text[mov_in] == ":" or text[mov_in] == "?":
            mystring = mystring + text[last_in:mov_in + 1] + "\n\n"
            last_in = mov_in
            while last_in + 1 < the_length and text[last_in + 1] == " ":
                last_in += 1
            if last_in + 1 < the_length and text[last_in] in [" ", ":", ".", "?"]:
                last_in += 1
            while mov_in + 1 < the_length and text[mov_in + 1] == " ":
                mov_in += 1
        mov_in += 1

    if last_in != the_length - 1:
        mystring = mystring + text[last_in:]

    if flag == 0:
        print(text, end="")
    else:
        print(mystring, end="")


text_indentation("hello.world")
