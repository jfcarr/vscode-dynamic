# Click on say_hello, then press [F2] to see the rename refactor
def say_hello():
    print("Hello!")

# Click on say_goodbye, then click the light bulb for Quick Fix options
def say_goodbye():
    print("Goodbye!")

def documented_method():
    '''
    This is a documentation comment.
    '''
    print("This method has a documentation comment.")

# This method sets some variables.  Use the debugger to examine them.
def debug_me():
    my_number = 10
    my_string = "This is a string"

    print(f"The number is {my_number}, the string is '{my_string}'")

say_hello()

# start typing "say_" to see autocomplete for say_goodbye:

# Hover over the call to see the documentation comment.
documented_method()

debug_me()
