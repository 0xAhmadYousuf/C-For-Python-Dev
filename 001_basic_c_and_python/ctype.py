import ctypes
import os

# Load the DLL
lib = ctypes.CDLL(os.path.abspath("./bin/ctype.dll"))

# Declare function signatures
lib.add.argtypes = (ctypes.c_int, ctypes.c_int)
lib.add.restype = ctypes.c_int

lib.show_message.argtypes = ()
lib.show_message.restype = None

# Use the functions
print("add(10, 20) =", lib.add(10, 20))
lib.show_message()
