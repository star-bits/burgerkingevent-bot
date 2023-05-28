from ppadb.client import Client

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
device = devices[0]

text = 'zhkxmfh aortlaja alxm vhzjtmem djapdlwld djfxlalt rmflfem voxl dhqm ej qlrltmxm vh tbvj alxm vmflr'

device.shell('input touchscreen tap 200 2050')

# Method 1: Entire text
# device.shell(f"input text '{text}'")

# Method 2: n chars at a time
n = 10
for i in range(0, len(text), n):
    chars = text[i:i+n]
    device.shell(f"input text '{chars}'")

# Method 3: 1.5 chars at a time
# toggle = True
# i = 0
# while i < len(text):
#     if toggle:
#         chars = text[i:i+2]
#         i += 2
#     else:
#         chars = text[i]
#         i += 1
#     device.shell(f"input text '{chars}'")
#     toggle = not toggle

device.shell('input touchscreen tap 1000 1400')