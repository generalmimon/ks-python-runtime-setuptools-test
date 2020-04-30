import sys
from hello_world import HelloWorld

hw = HelloWorld.from_file("file.bin")
print("one = {}".format(hw.one))

if hw.one == 137:
    print("[PASS]: one == 137")
    sys.exit(0)
else:
    print("[FAIL]: one != 137")
    sys.exit(1)
