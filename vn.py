import os
try:
    # Linux/Unix
    eval("__import__('os').system('clear')", {})
    # Windows
    #eval("__import__('os').system(cls')", {})
    print("Module OS loaded by eval")
except Exception as e:
    print(repr(e))
