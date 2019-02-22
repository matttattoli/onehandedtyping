import keyboard
import json
""" some notes
{'windows', 'right shift', 'alt', 'left windows', 'right windows', 'ctrl', 'left ctrl', 'left shift', 'shift', 'alt gr', 'right alt', 'right ctrl', 'left alt'}
{'ctrl', 'shift', 'windows', 'alt'}

https://github.com/boppreh/keyboard
"""
with open('remaps.json','r') as remaps:
    config = json.load(remaps)
escape_key = 'esc'
modifier_key = config['modifier']
remap_keys = config['key_maps']
keys = []

def pressed_key(kbevent):
    # print("Pressed: ", kbevent)
    # print(f"{kbevent.name} {kbevent.modifiers} {kbevent.scan_code}")
    # print(kbevent.to_json())
    if kbevent.name == "a":
        keyboard.send('a')

def released_key(kbevent):
    print("Released: ", kbevent.to_json())

def modifier_callback(kb_event):
    print(kb_event.to_json())

keyboard.on_press(pressed_key, suppress=True)
keyboard.on_release(released_key, suppress=True)

# keyboard.hook_key(modifier_key, modifier_callback, suppress=True)
keyboard.wait('esc')






""" stahp complaining
# import sys

# def force_exit(kbevent):
#     print("Force closing")
#     keyboard.unhook_all()
#     keyboard.unhook_all_hotkeys()
#     return

# def callback(kbevent):
#     print(kbevent.name)

# def print_modifiers(kbevent):
#     if kbevent.name == 'a':
#         print(keyboard.all_modifiers)
#         print(keyboard.sided_modifiers)
#         keyboard.unhook(print_modifiers)

# keyboard.block_key('e')
# if keyboard.is_pressed('alt') and keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift'):
#     print("ctrl+alt+shift")
#     force_exit(None)
# keyboard.hook_key('esc', sys.exit, suppress=False)
# keyboard.wait('esc')
"""