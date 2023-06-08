# burgerkingevent-bot

## Demo
https://github.com/star-bits/burgerkingevent-bot/assets/93939472/17bdb819-edac-461e-9d96-2f64b2bd251c

## Install
- Download adb (Android Debug Bridge) file. It can be a hassle so I've included it in the repository.
- Add the path of the adb file to `.zshrc`.
```shell
export PATH=$PATH:/Users/star-bits/Applications
# or, more commonly,
export PATH=$PATH:/usr/local/bin
```
- Reload `.zshrc`
```shell
. ~/.zshrc
```
- Connect your computer and phone with a USB cable.
- Run `adb devices` to verify the connection.
```shell
adb devices

List of devices attached
R3CM80QTY0M	device
```
- Install the pure-python-adb library
```shell
pip install pure-python-adb
```

## Run
```shell
python bot.py
```
