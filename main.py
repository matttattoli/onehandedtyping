import json

import keyboard


""" some notes
{'windows', 'right shift', 'alt', 'left windows', 'right windows', 'ctrl', 'left ctrl', 'left shift', 'shift', 'alt gr', 'right alt', 'right ctrl', 'left alt'}
{'ctrl', 'shift', 'windows', 'alt'}

https://github.com/boppreh/keyboard
"""

class OneHandedKeyboard:

    def __init__(self):
        with open('remaps.json','r') as self.remaps:
            self.config = json.load(self.remaps)
        self.escape_key = 'esc'
        self.modifier_key = self.config['modifier']
        self.remap_keys = self.config['key_maps']
        self.modifier = False
        self.shifting = False
        self.key_states = {"down": True, "up": False}
        keyboard.hook(self.modifier_callback, suppress=True)
        keyboard.wait('esc')

    def modifier_callback(self, kb_event):
        if kb_event.name == self.modifier_key:
            self.modifier = self.key_states[kb_event.event_type]
            print(f"Modifier key {kb_event.event_type}")
            return
        if kb_event.name.count("shift") > 0:
            self.shifting = self.key_states[kb_event.event_type]
            print(f"Shift key {kb_event.event_type}")
            return
        if self.modifier and kb_event.name in self.remap_keys:
            if kb_event.event_type == "down":
                print(f"Modifier active: Changing {kb_event.name} into {self.remap_keys[kb_event.name]}")
                if self.shifting:
                    print("shift", self.remap_keys[kb_event.name].upper())
                    keyboard.send("shift+" + self.remap_keys[kb_event.name])
                else:
                    keyboard.send(self.remap_keys[kb_event.name])
        else:
            if kb_event.event_type == "down":
                print(kb_event.to_json())
                if self.shifting:
                    print("shift", kb_event.name)
                    keyboard.send("shift+" + kb_event.name)
                else:
                    keyboard.send(kb_event.name)

if __name__ == "__main__":
    ohk = OneHandedKeyboard()
    print(keyboard.all_modifiers)
