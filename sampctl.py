# This is SAMPCTL-PY ( sampctl-py )
# Made by DEntisT

def sampctl_init():
    sampctl_command = raw_input("sampctl@cmd: ")

def sampctl_error(error):
    print("[sampctl-py]: (error) - " + error)

def sampctl_info(info):
    print("[sampctl-py]: (info) - " + info)

sampctl_command = raw_input("sampctl@cmd: ")

if sampctl_command == 'sampctl version':

    print("sampctl version 1.0-python")
    sampctl_init()

elif sampctl_command == 'sampctl exit':

    print("[sampctl-py]: (info) - sampctl session ended.")

elif sampctl_command == 'sampctl':

    sampctl_error("Please specify a command.")
    sampctl_init()

else:

    print("[sampctl-py]: (error) - Invalid command submitted.")
    sampctl_init()
