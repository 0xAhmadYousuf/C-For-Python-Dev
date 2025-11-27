# Create folder structure
New-Item -ItemType Directory -Force -Path "./obj" | Out-Null
New-Item -ItemType Directory -Force -Path "./bin" | Out-Null

# Compile object
gcc -c ctype.c -o ./obj/ctype.o

# Create DLL
gcc -shared -o ./bin/ctype.dll ./obj/ctype.o

# Run Python
python .\ctype.py
