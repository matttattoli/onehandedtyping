import json

import keyboard
from win32api import GetKeyState  # pylint: disable=no-name-in-module
from win32con import VK_CAPITAL
import os


def get_remap_config():
    config_path = 'ohtremaps.json'
    if os.path.exists(f"{os.getenv('USERPROFILE')}\\.ohtremaps.json"):
        config_path = f"{os.getenv('USERPROFILE')}\\.ohtremaps.json"
    with open(config_path, 'r') as remaps:
        config = json.load(remaps)
    return config


def deactivate_capslock():
    if GetKeyState(VK_CAPITAL) == -127 or GetKeyState(VK_CAPITAL) == 1:
        keyboard.press('capslock')


class OneHandedKeyboard:
    def __init__(self):
        self.config = get_remap_config()
        self.modifier_key = self.config['modifier']
        self.modifying = False
        self.remap_keys = self.config['key_maps']
        self.unhook_keys()
        keyboard.wait()

    def modifier_callback(self, kb_event):
        deactivate_capslock()
        if self.modifying and kb_event.event_type == 'up':
            self.unhook_keys()
            self.modifying = False
        elif not self.modifying and kb_event.event_type == 'down':
            self.hook_keys()
            self.modifying = True

    def key_callback(self, kb_event):
        deactivate_capslock()
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

    def hook_keys(self):
        for key in self.remap_keys.keys():
            keyboard.hook_key(key, self.key_callback, suppress=True)

    def unhook_keys(self):
        keyboard.unhook_all()
        keyboard.hook_key(self.modifier_key,
                          self.modifier_callback,
                          suppress=True)


if __name__ == "__main__":
    ohk = OneHandedKeyboard()
