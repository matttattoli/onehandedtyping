import time
import json

import keyboard


""" some notes
{'windows', 'right shift', 'alt', 'left windows', 'right windows', 'ctrl', 'left ctrl', 'left shift', 'shift', 'alt gr', 'right alt', 'right ctrl', 'left alt'}
{'ctrl', 'shift', 'windows', 'alt'}

https://github.com/boppreh/keyboard


going to make a list of all the buttons that have been pressed and then send that as a combination ?
"""

class OneHandedKeyboard:

    def __init__(self):
        with open('remaps.json','r') as self.remaps:
            self.config = json.load(self.remaps)
        self.modifier_key = self.config['modifier']
        self.modifying = False
        self.remap_keys = self.config['key_maps']
        self.key_states = {"down": True, "up": False}
        self.pressed_modifiers = []
        self.pressed_key = None
        self.all_modifiers = keyboard.all_modifiers
        self.debounce = False
        keyboard.hook(self.modifier_callback, suppress=True)
        keyboard.wait()

    def modifier_callback(self, kb_event):
        if kb_event.name == self.modifier_key:
            self.modifying = self.key_states[kb_event.event_type]
        else:
            if kb_event.name in self.all_modifiers and kb_event.name not in self.pressed_modifiers and kb_event.event_type == "down":
                self.pressed_modifiers.append(kb_event.name)
            elif kb_event.name in self.all_modifiers and kb_event.name in self.pressed_modifiers and kb_event.event_type == "up":
                self.pressed_modifiers.remove(kb_event.name)
            else:
                if kb_event.event_type == "down":
                    self.pressed_key = kb_event.name
                elif kb_event.event_type == "up" and self.pressed_key == kb_event.name:
                    self.pressed_key = None

        if self.pressed_modifiers and kb_event.event_type == "down":
            send_keys = '+'.join(self.pressed_modifiers)
            if self.pressed_key:
                if self.modifying and self.pressed_key in self.remap_keys:
                    send_keys += "+" + self.remap_keys[self.pressed_key]
                else:
                    send_keys += "+" + self.pressed_key
            # print(send_keys)
            keyboard.send(send_keys)
        elif self.pressed_key and kb_event.event_type == "down":
            if self.modifying and self.pressed_key in self.remap_keys:
                keyboard.send(self.remap_keys[self.pressed_key])
            else:
                keyboard.send(self.pressed_key)
        # print("modifying", self.modifying)
        # print("pressed_key", self.pressed_key)
        # print("pressed_modifiers", self.pressed_modifiers)
        # time.sleep(.06)

if __name__ == "__main__":
    print(keyboard.all_modifiers)
    ohk = OneHandedKeyboard()
