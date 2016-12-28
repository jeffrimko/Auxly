from auxly.shell import has

wincmds = ["tracert","fc","ver"]
maccmds = ["osacompile"]
nixcmds = ["ls","stat","pwd"]
if all([has(cmd) for cmd in wincmds]):
    print("Looks like you might be running Windows.")
elif all([has(cmd) for cmd in maccmds]):
    print("Looks like you might be running Mac.")
elif all([has(cmd) for cmd in nixcmds]):
    print("Looks like you might be running Linux.")
