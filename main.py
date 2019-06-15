import json

import keyboard


class OneHandedKeyboard:

    def __init__(self):
        with open('remaps.json', 'r') as self.remaps:
            self.config = json.load(self.remaps)
        self.modifier_key = self.config['modifier']
        self.modifying = False
        self.remap_keys = self.config['key_maps']
        self.key_states = {"down": True, "up": False}
        keyboard.hook(self.modifier_callback, suppress=True)
        keyboard.wait()

    def modifier_callback(self, kb_event):
        if kb_event.name == self.modifier_key:
            self.modifying = self.key_states[kb_event.event_type]

    def key_callback(self, kb_event):
        if keyboard.is_pressed('shift'):
            kb_event.name = kb_event.name.lower()
        if kb_event.event_type == "down":
            if self.modifying and kb_event.name in self.remap_keys:
                keyboard.press(self.remap_keys[kb_event.name])
            else:
                keyboard.press(kb_event.name)
        elif kb_event.event_type == "up":
            keyboard.release(kb_event.name)
            if kb_event.name in self.remap_keys:
                keyboard.release(self.remap_keys[kb_event.name])


if __name__ == "__main__":
    ohk = OneHandedKeyboard()
