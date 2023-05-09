from ppadb.client import Client

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
device = devices[0]

device.shell('input touchscreen tap 200 2050')
device.shell("input text 'zhkxmfh aortlaja alxm vhzjtmem djapdlwld djfxlalt rmflfem voxl dhqm ej qlrltmxm vh tbvj alxm vmflr'")
device.shell('input touchscreen tap 1000 1400')