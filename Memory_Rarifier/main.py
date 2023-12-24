# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
import time
from pynput import keyboard
import keyboard as kb
import re
import tkinter as tk
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Manager
from functools import partial
from threading import Thread
import pyperclip
import numpy as np
import pytesseract
import cv2
import threading
import pyperclip
from pyautogui import *
import pyautogui
import time
from global_hotkeys import *
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, KeyCode, Controller as KeyboardController
import toml

config_file = "config.toml"

class CraftGUI:
    def __init__(self):
        self.config_file = config_file
        file = open("config.toml", "r")
        data_dict = {'open_and_stash_stacks':{'1': {'Name':"Divination Cards", 'height':100, 'width':100, 'x':770, 'y':1300},
                          '2': {'Name':"Inventory", 'height':100, 'width':100, 'x':2595, 'y':1230}},
                     "chat enchant":{'1':{'Name':'Enchants','height':345,'width':348,'x':675,'y':425}},
        "Prepare Memorys": {'1': {'Name':'Memory', 'height':100, 'width':100, 'x':1200, 'y':950},'2': {'Name':'Chisel', 'height':100, 'width':100, 'x':2595, 'y':1230},'3': {'Name':'Alchemy', 'height':100, 'width':100, 'x':2599, 'y':1333},'4': {'Name':'Scouring', 'height':100, 'width':100, 'x':2595, 'y':1450}},
        "Magic Craft": {'1': {'Name':'Item', 'height':100, 'width':100, 'x':671, 'y':927},'2': {'Name':'Alteration', 'height':100, 'width':100, 'x':218, 'y':620},'3': {'Name':'Augmentation', 'height':100, 'width':100, 'x':455, 'y':743}},
        "Trade in Divs": {'1': {'Name':'Inventar', 'height':100, 'width':100, 'x':2595, 'y':1230},'2': {'Name':'Card Trade Button', 'height':100, 'width':100, 'x':1266, 'y':1481},'3': {'Name':'Card Slot', 'height':100, 'width':100, 'x':1265, 'y':990}},
        "Haggle": {'1': {'Name':'Last Inventory', 'height':100, 'width':100, 'x':3755, 'y':1650},
                   '2': {'Name':'Reroll', 'height':100, 'width':100, 'x':1895, 'y':1745},
                   '3': {'Name':'Confirm Button', 'height':100, 'width':100, 'x':1262, 'y':1723},
                   '4': {'Name':'Tujens Inv', 'height':1050, 'width':700, 'x':600, 'y':350},
                   '5': {'Name':'Tujens First Inv Slot', 'height':100, 'width':100, 'x':675, 'y':575},
                   '6': {'Name':'Haggle Bar', 'height':20, 'width':460, 'x':1016, 'y':1609}},
        "Empty_inv": {'1': {'Name':'Inventory', 'height':100, 'width':100, 'x':2595, 'y':1230}},
        "Jewel_stuff": {'1': {'Name':'Inventory', 'height':100, 'width':100, 'x':2595, 'y':1230},'2': {'Name':'Stash', 'height':100, 'width':100, 'x':85, 'y':315}}
        }
        self.change_button = {'open_and_stash_stacks':0,"chat enchant":0,"Prepare Memorys":0,"Magic Craft":0,"Trade in Divs":0,"Haggle":0,"Empty_inv":0,"Jewel_stuff":0}
        self.config_windows = {'open_and_stash_stacks':[],"chat enchant":[],"Prepare Memorys":[],"Magic Craft":[],"Trade in Divs":[],"Haggle":[],"Empty_inv":[],"Jewel_stuff":[]}
        #toml.dump(data_dict, file)
        data = toml.load("config.toml")
        file.close()

        self.make_rare = craft()
        self.listener = None

        self.root = tk.Tk()
        self.root.title("Crafting Program")



        # Buttons
        self.prepare_button = tk.Button(self.root, text="Prepare Memorys(NUM +)", command=self.make_rare.prepare)
        self.prepare_button.grid(row=0, column=0, sticky="nsew")
        self.config_prepare_position_button = tk.Button(self.root, text="Config",
                                                        command=lambda: self.open_position_window(toml.load("config.toml")['Prepare Memorys']
                                                                                                  , 'Prepare Memorys',
                                                                                                  self.config_prepare_position_button))
        self.config_prepare_position_button.grid(row=0, column=2, sticky="nsew")
#----------------------------------------------------------------------------------------------------------------------
        self.magic_craft_button = tk.Button(self.root, text="Magic Craft(NUM -)", command=self.make_rare.run_magic_craft)
        self.magic_craft_button.grid(row=1, column=0, sticky="nsew")
        self.config_magic_craft_position_button = tk.Button(self.root, text="Config",
                                                        command=lambda: self.open_position_window(toml.load("config.toml")['Magic Craft']
                                                                                                  , 'Magic Craft',
                                                                                                  self.config_magic_craft_position_button))
        self.config_magic_craft_position_button.grid(row=1, column=2, sticky="nsew")
# ----------------------------------------------------------------------------------------------------------------------
        self.trade_in_divs_button = tk.Button(self.root, text="Trade in Divs(NUM 7)", command=self.make_rare.trade_in_divs)
        self.trade_in_divs_button.grid(row=2, column=0, sticky="nsew")
        self.config_trade_in_divs_position_button = tk.Button(self.root, text="Config",
                                                        command=lambda: self.open_position_window(toml.load("config.toml")['Trade in Divs']
                                                                                                  , 'Trade in Divs',
                                                                                                  self.config_trade_in_divs_position_button))
        self.config_trade_in_divs_position_button.grid(row=2, column=2, sticky="nsew")
        # ----------------------------------------------------------------------------------------------------------------------
        self.open_and_stash_stacks_button = tk.Button(self.root, text="Open & Stash Divs(NUM /)", command=self.invoke_open_and_stash_stacks)
        self.open_and_stash_stacks_button.grid(row=3, column=0, sticky="nsew")
        self.config_open_and_stash_stacks_position_button = tk.Button(self.root, text="Config",
                                                        command=lambda: self.open_position_window(toml.load("config.toml")['open_and_stash_stacks']
                                                                                                  , 'open_and_stash_stacks',
                                                                                                  self.config_open_and_stash_stacks_position_button))
        self.config_open_and_stash_stacks_position_button.grid(row=3, column=2, sticky="nsew")
        self.numbers_entry = tk.Entry(self.root)
        self.numbers_entry.grid(row=3, column=1, sticky="nsew")
        # ----------------------------------------------------------------------------------------------------------------------
        self.haggle_button = tk.Button(self.root, text="Haggle", command=self.invoke_haggle)
        self.haggle_button.grid(row=4, column=0, sticky="nsew")
        #self.config_haggle_position_button = tk.Button(self.root, text="Config",
        #                                                command=lambda: self.open_position_window(data['Haggle']
        #                                                                                          , 'Haggle',
        #                                                                                         self.config_haggle_position_button))
        self.config_haggle_position_button = tk.Button(self.root, text="Config",
                                                       command=lambda: self.open_position_window(toml.load("config.toml")['Haggle']
                                                                                                 , 'Haggle',
                                                                                                 self.config_haggle_position_button))
        self.config_haggle_position_button.grid(row=4, column=2, sticky="nsew")
        self.coin_entry = tk.Entry(self.root)
        self.coin_entry.grid(row=4, column=1, sticky="nsew")
        # ----------------------------------------------------------------------------------------------------------------------
        self.empty_inventory_button = tk.Button(self.root, text="Empty_inv(NUM 1)", command=self.make_rare.empty_inventory)
        self.empty_inventory_button.grid(row=5, column=0, sticky="nsew")
        self.config_empty_inventory_position_button = tk.Button(self.root, text="Config",
                                                        command=lambda: self.open_position_window(toml.load("config.toml")['Empty_inv']
                                                                                                  , 'Empty_inv',
                                                                                                  self.config_empty_inventory_position_button))
        self.config_empty_inventory_position_button.grid(row=5, column=2, sticky="nsew")
        # ----------------------------------------------------------------------------------------------------------------------
        self.do_jewel_stuff_button = tk.Button(self.root, text="Jewel_stuff(NUM 2)", command=self.make_rare.do_jewel_stuff)
        self.do_jewel_stuff_button.grid(row=6, column=0, sticky="nsew")
        self.config_do_jewel_stuff_position_button = tk.Button(self.root, text="Config",
                                                        command=lambda: self.open_position_window(toml.load("config.toml")['Jewel_stuff']
                                                                                                  , 'Jewel_stuff',
                                                                                                  self.config_do_jewel_stuff_position_button))
        self.config_do_jewel_stuff_position_button.grid(row=6, column=2, sticky="nsew")
        # ----------------------------------------------------------------------------------------------------------------------

        self.empty_stash_button = tk.Button(self.root, text="empty_stash(NUM 3)", command=self.make_rare.empty_stash)
        self.empty_stash_button.grid(row=7, column=0, sticky="nsew")

        self.config_empty_stash_position_button = tk.Button(self.root, text="Config",
                                                        command=lambda: self.open_position_window(toml.load("config.toml")['empty stash']
                                                                                                  , 'empty stash',
                                                                                                  self.config_empty_stash_position_button))
        self.config_empty_stash_position_button.grid(row=7, column=2, sticky="nsew")
        # ----------------------------------------------------------------------------------------------------------------------
        self.enchant_to_chat_button = tk.Button(self.root, text="Enchant to Chat(NUM 4)", command=self.make_rare.enchant_to_chat)
        self.enchant_to_chat_button.grid(row=8, column=0, sticky="nsew")
        self.config_enchant_position_button = tk.Button(self.root, text="Config",command=lambda:self.open_position_window(toml.load("config.toml")['chat enchant']
                                                                                                                                                  ,'chat enchant',
                                                                                                                                         self.config_enchant_position_button))
        self.config_enchant_position_button.grid(row=8, column=2, sticky="nsew")
        # ----------------------------------------------------------------------------------------------------------------------
        self.hotkeys_label = tk.Label(self.root, text="Stop NUM 0")
        self.hotkeys_label.grid(row=9, column=0, sticky="nsew")



        # Keybinds
        self.root.bind('<KeyPress-0>', self.on_key_0_pressed)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        #thread = threading.Thread(target=self.invoke_hotkeys)
        #thread.start()
        self.open_windows = []
        self.root.protocol("WM_DELETE_WINDOW", self.close_windows)

    def open_position_window(self, windows, button_change,button):
        if self.change_button[button_change] == 0:
            button['text']="Speicher"
            self.change_button[button_change] = 1
            for i, window in enumerate(windows):
                self.config_windows[button_change].append(tk.Tk())
                self.config_windows[button_change][i].attributes('-alpha', 0.3)
                self.config_windows[button_change][i].overrideredirect(True)
                self.config_windows[button_change][i].attributes('-topmost', True)
                self.config_windows[button_change][i].geometry(f"{windows[window]['width']}x{windows[window]['height']}+{windows[window]['x']}+{windows[window]['y']}")
                self.config_windows[button_change][i].title(windows[window]['Name'])
                frame = tk.Frame(self.config_windows[button_change][i])
                frame.pack(fill=tk.BOTH, expand=True)
                frame.place(x=10, y=10)
                self.config_windows[button_change][i].bind("<ButtonPress-1>", self.on_drag_start)
                #config_windows[i].bind("<ButtonRelease-1>", self.stop_drag)
                self.config_windows[button_change][i].bind("<B1-Motion>", self.on_drag_motion)
                self.config_windows[button_change][i].bind("<Map>", self.show_in_taskbar)
                self.drag_data = {'x': 0, 'y': 0}
                #self.open_windows.append(self.config_windows[button_change][i])
        elif self.change_button[button_change] == 1:
            self.change_button[button_change] = 0
            button['text'] = "Config"
            for i, window in enumerate(windows):
                x = self.config_windows[button_change][i].winfo_x()
                y = self.config_windows[button_change][i].winfo_y()
                print(f'''width is {i} {self.config_windows[button_change][i].winfo_width()},
                requested width is {self.config_windows[button_change][i].winfo_reqwidth()}''')
                width = self.config_windows[button_change][i].winfo_width()
                height = self.config_windows[button_change][i].winfo_height()
                data = toml.load(self.config_file)
                data[button_change][str(i + 1)]['x'] = x
                data[button_change][str(i + 1)]['y'] = y
                data[button_change][str(i + 1)]['height'] = height
                data[button_change][str(i + 1)]['width'] = width

                file = open(self.config_file, "w")
                toml.dump(data, file)
                file.close()
                self.config_windows[button_change][int(i)].destroy()
            self.config_windows[button_change]=[]



    def close_windows(self):
        for window in self.config_windows:
            for w_num in self.config_windows[window]:
                w_num.destroy()  # Schließen Sie alle geöffneten Toplevel-Fenster
        self.root.destroy()

    def start_drag(self, event):
        self.drag_data['x'] = event.x
        self.drag_data['y'] = event.y

    def on_drag_start(self,event):
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y

    def stop_drag(self, event):
        self.drag_data = {}

    def on_drag_motion(self,event):
        widget = event.widget
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() - widget._drag_start_y + event.y

        event.widget.wm_geometry(f"+{x}+{y}")

    def show_in_taskbar(self, event):
        event.widget.winfo_toplevel().deiconify()

    def on_drag(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() - widget._drag_start_y + event.y
        event.x=x
        event.y = y
        #if 'x' in self.drag_data and 'y' in self.drag_data:
        #    x = event.x_root - self.drag_data['x']
        #    y = event.y_root - self.drag_data['y']
        #    event.widget.wm_geometry(f"+{x}+{y}")





    def invoke_hotkeys(self):
        listener = keyboard.Listener(on_press=self.make_rare.on_press)
        listener.start()
        listener.join()


    def invoke_open_and_stash_stacks(self):
        content = self.numbers_entry.get()
        if content!='':# Den Inhalt des Textfeldes abrufen
            try:
                content= int(content)
                self.make_rare.open_and_stash_stacks(content)
            except:
                pass

    def invoke_haggle(self):
        content = self.coin_entry.get()
        if content!='':# Den Inhalt des Textfeldes abrufen
            #try:
            content= int(content)
            self.make_rare.haggle(content)
            #except Exception as e:
             #   print(e)
              #  pass

    def listen_for_keys(self):
        self.listener = kb.Listener(on_press=self.make_rare.on_press, on_release=self.make_rare.on_release)
        self.listener.start()

    def on_key_0_pressed(self, event):
        self.make_rare.set_key_0_pressed(True)

    def run(self):
        self.root.mainloop()

class craft():
    def __init__(self):
        self.config_file = config_file
        self.position_data = toml.load("config.toml")
        self.i = 0
        self.key_0_pressed = False

        self.mouse = MouseController()
        self.keyboardCtrl = KeyboardController()
        self.is_running = True
        self.flag = 0
        self.counter = 0
        self.stash_counter = 0  # Fängt bei 0 An

        #self.stash_region = (23, 250, 875, 875)
        #self.stash_region = (23, 320, 1300, 1300)
        self.stash_region = (30, 330, 1300, 1300)
        self.stash_zero_point_x = 30
        self.stash_zero_point_y = 330
        self.x_steps = 1
        self.y_steps = 1
        self.offset_x = 3
        self.offset_y = 3

        self.keys = [97, 98, 99, 100, 100, 101, 102, 103, 103, 104]
        # keys = [104]

        self.key_items = {
            97: "Gloves",
            98: "Helmets",
            99: "Boots",
            100: "Rings",
            101: "Body Armours",
            102: "Amulets",
            103: "Weapon",
            104: "Belts",
        }

        self.weapons = [
            "Claws",
            "Daggers",
            "One Hand Axes",
            "One Hand Maces",
            "One Hand Swords",
            "Rune Daggers",
            "Sceptres",
            "Thrusting One Hand Swords",
            "Wands",
            "Shields",
        ]

        self.two_handed_weapons = [
            "Two Hand Maces",
            "Two Hand Axes",
            "Two Hand Swords",
            "Warstaves",
            "Staves",
            "Bows",
        ]

        self.armour = ["Gloves", "Body Armours", "Boots", "Belts", "Amulets", "Helmets"]
        self.jewellery = ["Rings"]

        self.bindings = [
            [["F6"], None, self.click_item],
            [["alt", "a"], None, self.highlight_items],
            [["alt", "f"], None, self.find_and_click_lilly],
            [["shift", "F1"], None, self.exit_application],
            [["alt", "F2"], None, self.magic_craft]
        ]
#"basic Currency|Div|Heist Target"
        self.craft_modifiers = [
            r'.*(1[4-5]%*).*?(Basic Currency|Divinati)',
            r'[1][1-5]% reduced raising of Alert Level from',
            r' Agility Level for Heists',
            r'to Brute Force Level for Heists',
            r'to Brute Force Level for Heists',
            r'to Deception Level for Heists',
            r'to Demolition Level for Heists',
            r'to Engineering Level for Heists',
            r'to Lockpicking Level for Heists',
            r'to Perception Level for Heists',
            r'to Trap Disarmament Level for Heists',
            r' to Level of all Jobs for Heists'
        ]
        self.magic_craft_found=0

    def click_item(self):
        pics = {}
        number = 0
        remove_key = None
        self.highlight_items()
        for stash in range(self.stash_counter):
            print(stash)
            self.change_stash(stash)
            item = self.find_item()
            if type(item) is not tuple:
                pass
            else:
                try:
                    number, remove_key, x, y = item
                    self.click(x, y)
                    break
                except:
                    print("No Item found")
        self.change_stash(0)
        for i in range(number):
            self.keys.remove(remove_key)

        for key in self.keys:
            time.sleep(0.15)
            self.keyboardCtrl.press(KeyCode(vk=key))
            time.sleep(0.15)
            self.keyboardCtrl.release(KeyCode(vk=key))
            time.sleep(0.15)
            pics[key] = pyautogui.screenshot(region=self.stash_region)
            print(key)
            #if self.click_border_reverse(key):
            #    break
        with Manager() as manager:
            click_pos = manager.dict()
            processes = []
            for key, pic in pics.items():
                p = Process(target=self.analyze_border, args=(key, pic, click_pos))
                processes.append(p)
                p.start()
                p.join(4)
        print("Done")

    def highlight_items(self):
        self.keyboardCtrl.press(Key.ctrl)
        time.sleep(0.2)
        self.keyboardCtrl.press("f")
        self.keyboardCtrl.release("f")
        time.sleep(0.2)
        self.keyboardCtrl.release(Key.ctrl)
        time.sleep(0.6)
        self.keyboardCtrl.type('"item level: ([0-6][0-9]|7[0-4])"')
        time.sleep(0.2)

    def change_stash(self, counter):
        if counter == 0:
            self.mouse.position = [360, 300]
        elif counter == 1:
            self.mouse.position = [300, 300]
        elif counter == 2:
            self.mouse.position = [430, 300]
        elif counter == 3:
            self.mouse.position = [550, 300]
        elif counter == 4:
            self.mouse.position = [670, 300]
        elif counter == 5:
            self.mouse.position = [790, 300]
        elif counter == 6:
            self.mouse.position = [900, 300]
        elif counter == 7:
            self.mouse.position = [130, 300]
        elif counter == 8:
            self.mouse.position = [1160, 300]
        elif counter == 9:
            self.mouse.position = [1290, 300]

        time.sleep(0.2)
        self.mouse.press(Button.left)
        self.mouse.release(Button.left)
        time.sleep(0.2)

    def find_item(self):
        self.flag = 0
        pic = pyautogui.screenshot(region=self.stash_region)
        # pic.save(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\test.png")
        width, height = pic.size
        for y in range(0, height, self.y_steps):
            for x in range(0, width, self.x_steps):
                r, g, b = pic.getpixel((x, y))
                if (
                        (b in range(110, 190))
                        and (r in range(200, 240))
                        and (g in range(150, 200))
                ):
                    self.flag = 1
                    self.counter = 0

                    clip = self.copy_to_clipboard(x + self.offset_x, y + self.offset_y)
                    item = self.get_item_type(clip)
                    key, number = self.get_item_vkey(item[0])
                    x = x + self.offset_x
                    y = y + self.offset_y + self.stash_zero_point_y
                    # click(x + offset_x, y + offset_y)
                    # print(key,number,x,y)
                    return key, number, x, y

                if self.flag == 1:
                    break
        # return None
        print("Done")

    def click(self, x, y):
        self.mouse.position = [self.stash_zero_point_x + x, self.stash_zero_point_y + y]
        self.keyboardCtrl.press(Key.ctrl)
        time.sleep(0.05)
        self.mouse.press(Button.left)
        self.mouse.release(Button.left)
        time.sleep(0.05)
        self.keyboardCtrl.release(Key.ctrl)

    def get_item_vkey(self, item):
        number = 0
        number = self.get_weapon_type(item)
        # print(item, number)
        if number > 0:
            item = "Weapon"
        else:
            number = 1
        if item in self.key_items.values():
            key = list(self.key_items.keys())[list(self.key_items.values()).index(item)]
            return number, key

    def get_item_class_from_clipboard(self,clip):
        # print(clip)
        line = clip.split("\n")
        return line[0].split(":")[1].strip()

    def get_weapon_type(self,line):
        # line=get_item_class_from_clipboard(clip)
        if line in self.weapons:
            return 1
        elif line in self.two_handed_weapons:
            return 2
        else:
            return 0

    def get_item_type(self,clip):
        # print(clip)
        line = self.get_item_class_from_clipboard(clip)

        if line in self.weapons:
            return line, "one-handed weapon"
        elif line in self.two_handed_weapons:
            return line, "two-handed weapon"
        elif line in self.armour:
            return line, "armour"
        elif line in self.jewellery:
            return line, "ring"
        else:
            return line, "Item not found in list"

    def copy_to_clipboard(self,x, y):
        self.mouse.position = [self.stash_zero_point_x + x, self.stash_zero_point_y + y]
        time.sleep(0.2)
        with self.keyboardCtrl.pressed(Key.ctrl):
            self.keyboardCtrl.press("c")
            self.keyboardCtrl.release("c")

        time.sleep(0.1)
        return pyperclip.paste()

    def analyze_border(self, key, pic):
        click_pos = {'x':0,'y':0}
        self.flag = 0
        width, height = pic.size
        for y in range(0, height, self.y_steps):
            for x in range(0, width, self.x_steps):
                r, g, b = pic.getpixel((x, y))
                if (
                        (b in range(110, 190))
                        and (r in range(200, 240))
                        and (g in range(150, 200))
                ):
                    self.flag = 1
                    self.counter = 0
                    #self.click(x + self.offset_x, y + self.offset_y)  # self.stash_zero_point_y
                    click_pos[x] = x + self.offset_x
                    click_pos[y] = y + self.offset_y
                    #time.sleep(0.2)
                    break
            if self.flag == 1:
                break
        if self.flag == 0:
            print(f"Item {self.key_items[key]} missing")
            return True
            #self.counter = self.counter + 1
            #print(self.counter)
           # self.change_stash(self.counter)
            #time.sleep(0.2)
            #if self.counter > self.stash_counter:
            #    print("Item not found in any Stash")
            #    self.counter = 0
            #    return True
            #self.click_border(key)
            #self.change_stash(0)
        return click_pos

    def analyze_border_reverse(self, key, pic):
        click_pos = {'x':0,'y':0}
        self.flag = 0
        width, height = pic.size
        for y in range(height, 0, self.y_steps):
            for x in range(width, 0, self.x_steps):
                r, g, b = pic.getpixel((x-1, y-1))
                if (
                        (b in range(110, 190))
                        and (r in range(200, 240))
                        and (g in range(150, 200))
                ):
                    self.flag = 1
                    self.counter = 0
                    #self.click(x + self.offset_x, y + self.offset_y)  # self.stash_zero_point_y
                    click_pos[x] = x - self.offset_x
                    click_pos[y] = y - self.offset_y
                    #time.sleep(0.2)
                    break
            if self.flag == 1:
                break
        if self.flag == 0:
            print(f"Item {self.key_items[key]} missing")
            return True
            #self.counter = self.counter + 1
            #print(self.counter)
            #self.change_stash(self.counter)
            #time.sleep(0.2)
            #if self.counter > self.stash_counter:
            #    print("Item not found in any Stash")
            #    self.counter = 0
            #    return True
            #self.click_border(key)
            #self.change_stash(0)
        return click_pos

    def click_border_reverse(self, key):
        self.flag = 0
        pic = pyautogui.screenshot(region=self.stash_region)
        width, height = pic.size
        # print(height)
        for y in range(height,0 , -self.y_steps):
            # print(y)
            for x in range(width, 0 , -self.x_steps):
                # print(x)
                r, g, b = pic.getpixel((x-1, y-1))
                if (
                        (b in range(110, 190))
                        and (r in range(200, 240))
                        and (g in range(150, 200))
                ):
                    self.flag = 1
                    self.counter = 0
                    print(x, y)
                    self.click(x - self.offset_x, y - self.offset_y )#self.stash_zero_point_y
                    time.sleep(0.2)
                    break
            if self.flag == 1:
                break
        if self.flag == 0:
            print(f"Item {self.key_items[key]} missing")
            self.counter = self.counter + 1
            print(self.counter)
            self.change_stash(self.counter)
            time.sleep(0.2)
            if self.counter > self.stash_counter:
                print("Item not found in any Stash")
                self.counter = 0
                return True
            self.click_border_reverse(key)
            self.change_stash(0)

    def click_border(self, key):
        self.flag = 0
        pic = pyautogui.screenshot(region=self.stash_region)
        width, height = pic.size
        # print(height)
        for y in range(0, height, self.y_steps):
            # print(y)
            for x in range(0, width, self.x_steps):
                # print(x)
                r, g, b = pic.getpixel((x, y))
                if (
                        (b in range(110, 190))
                        and (r in range(200, 240))
                        and (g in range(150, 200))
                ):
                    self.flag = 1
                    self.counter = 0
                    print(x, y)
                    self.click(x + self.offset_x, y + self.offset_y )#self.stash_zero_point_y
                    time.sleep(0.2)
                    break
            if self.flag == 1:
                break
        if self.flag == 0:
            print(f"Item {self.key_items[key]} missing")
            self.counter = self.counter + 1
            print(self.counter)
            self.change_stash(self.counter)
            time.sleep(0.2)
            if self.counter > self.stash_counter:
                print("Item not found in any Stash")
                self.counter = 0
                return True
            self.click_border(key)
            self.change_stash(0)

    def find_and_click_lilly(self):
        x, y = pyautogui.locateCenterOnScreen(
            r"F:\projekte\opencv\Name.png", confidence=0.8
        )
        with pyautogui.hold("ctrl"):
            pyautogui.moveTo(x, y)
            time.sleep(0.01)
            pyautogui.click()

    def exit_application(self):
        global is_running
        self.stop_checking_hotkeys()
        self.flag == 1
        is_running = False



    def rarifiy(self):
        mouse_click=pyautogui
        memory_pos = self.position_data['Prepare Memorys']['1']['x']+self.position_data['Prepare Memorys']['1']['width']/2, self.position_data['Prepare Memorys']['1']['y']+self.position_data['Prepare Memorys']['1']['height']/2
        scoure_pos = self.position_data['Prepare Memorys']['3']['x']+self.position_data['Prepare Memorys']['3']['width']/2, self.position_data['Prepare Memorys']['3']['y']+self.position_data['Prepare Memorys']['3']['height']/2
        alchemy_pos = self.position_data['Prepare Memorys']['4']['x']+self.position_data['Prepare Memorys']['4']['width']/2, self.position_data['Prepare Memorys']['4']['y']+self.position_data['Prepare Memorys']['4']['height']/2
        while True:
            mouse_click.moveTo(memory_pos)
            pyperclip.copy('')
            while pyperclip.paste()=='':
                pyperclip.copy('')
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(0.1)
                memory_map = pyperclip.paste()
            if 'Slaying Enemies close together can attract monsters from Beyond this realm' not in memory_map:
                mouse_click.moveTo(scoure_pos)
                mouse_click.click(button='right')  # Orb of Scouring(Third Inventar field)
                mouse_click.moveTo(memory_pos)
                mouse_click.click(button='left')  # Memory
                mouse_click.moveTo(alchemy_pos)
                mouse_click.click( button='right')  # Orb of Binding(Second Inventar field)
                mouse_click.moveTo(memory_pos)
                mouse_click.click(button='left')  # Memory
            else:
                return
            if kb.is_pressed('0'):
                return

    def qualify(self):
        mouse_click = pyautogui
        chisel_pos = self.position_data['Prepare Memorys']['2']['x'] + self.position_data['Prepare Memorys']['2'][
            'width'] / 2, self.position_data['Prepare Memorys']['2']['y'] + self.position_data['Prepare Memorys']['2'][
                         'height'] / 2
        memory_pos = self.position_data['Prepare Memorys']['1']['x'] + self.position_data['Prepare Memorys']['1'][
            'width'] / 2, self.position_data['Prepare Memorys']['1']['y'] + self.position_data['Prepare Memorys']['1'][
                         'height'] / 2
        mouse_click.moveTo(memory_pos)
        pyperclip.copy('')
        pyautogui.hotkey('ctrl', 'c')
        memory_map=pyperclip.paste()
        if "Quality: +20%" not in memory_map:
            for i in range(5):
                mouse_click.moveTo(chisel_pos)
                with mouse_click.hold('shift'):
                    mouse_click.click(button='right')  # Chisel(First Inventar field)
                    mouse_click.moveTo(memory_pos)
                    mouse_click.click(button='left')  # Memory

    def prepare(self):
        pyautogui.PAUSE = 0.04
        self.qualify()
        self.rarifiy()

    def magic_craft(self):
        clipboard = ''
        mouse_click = pyautogui
        self.magic_craft_found = 0
        mouse_click.moveTo(10, 10)
        mouse_click.click(button='left')
        time.sleep(0.1)
        mouse_click.moveTo(671, 927)
        while clipboard =='':
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.05)
            clipboard = pyperclip.paste()
        for mod in self.craft_modifiers:
            if kb.is_pressed('0'):
                print('stop')
                break
            match = re.search(mod, clipboard, re.IGNORECASE)
            time.sleep(0.1)
            if match != None:
                self.magic_craft_found = 1
                break
            else:
                self.magic_craft_found = 0
        while True:
            clipboard = ''
            self.magic_craft_found = 0
            mouse_click.PAUSE=0.02
            mouse_click.moveTo(218, 620)
            mouse_click.click(button='right')  # Orb of Alteration
            mouse_click.moveTo(671, 927)
            mouse_click.click(button='left')

            mouse_click.moveTo(455, 743)
            mouse_click.click(button='right')  # Orb of Augmentation
            mouse_click.moveTo(671, 927)
            mouse_click.click(button='left')
            while clipboard =='':
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(0.05)
                clipboard = pyperclip.paste()
                #print(clipboard)
            for mod in self.craft_modifiers:
                if kb.is_pressed('0'):
                    print('stop')
                    break
                match = re.search(mod, clipboard, re.IGNORECASE)
                time.sleep(0.1)
                if match != None:
                    self.magic_craft_found = 1
                    break
                else:
                    self.magic_craft_found = 0
            if kb.is_pressed('0'):
                print('stop')
                break
            if self.magic_craft_found == 1:
                break

    def enchant_to_chat(self):
        pytesseract.pytesseract.tesseract_cmd = r'G:\Tesseract OCR\tesseract.exe'
        text=""
        fill=' -|||- '
        helmet=[]
        helmet_text=''
        for i in enumerate(['gloves','boots','helmet1','helmet2','helmet3']):
            enchant = pyautogui.screenshot(region=(675,425+i[0]*103, 1020, 77))
            enchant.save(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\enchant"+str(i[0])+".png")
            img =cv2.imread(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\enchant"+str(i[0])+".png", cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (0, 0), fx=2.0, fy=2.0)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            img = clahe.apply(img)
            img = 255 - img
            ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
            cv2.imwrite('output.png', img)
            ocr = pytesseract.image_to_string(img, config='--psm 6')[:-1]
            if 'helmet' in i[1]:
                helmet.append(i[1])
                helmet_text=helmet_text+ocr+fill
            text=text+ocr+fill
        pyperclip.copy(helmet_text)
        print('finished')
        return helmet

    def open_and_stash_stacks(self,div_amount):
        pyautogui.PAUSE = 0.1
        mouse_click = pyautogui
        clipboard=''
        pyperclip.copy('')
        #mouse_click.moveTo(300, 300)
        #mouse_click.click(button='left')
        for z in range(0, div_amount):
            mouse_click.moveTo(770, 1300)#div location
            mouse_click.click(button='right')
            mouse_click.moveTo(2595, 1230)#invlocation
            mouse_click.click(button='left')
            while True:
                with mouse_click.hold('ctrl'):
                    mouse_click.click(button='left')
                pyautogui.hotkey('ctrl', 'c')
                if clipboard=='':
                    clipboard = ''
                    pyperclip.copy('')
                    break
                clipboard = pyperclip.paste()
                pyperclip.copy('')
                if kb.is_pressed('0'):
                    print('stop')
                    return

                #for y in range(0, 12):
                #    for x in range(0, 5):
                #        mouse_click.moveTo(2595+y*105, 1230+x*105)
            if kb.is_pressed('0'):
                print('stop')
                return

    def trade_in_divs(self):
        mouse_click = pyautogui
        with mouse_click.hold('ctrl'):
            for y in range(0, 12):
                for x in range(0, 5):
                    mouse_click.moveTo(2595+y*105, 1230+x*105)
                    mouse_click.click(button='left')
                    mouse_click.moveTo(1266, 1481)#Trade button
                    mouse_click.click(button='left')
                    mouse_click.moveTo(1265, 990)#Card Slot
                    mouse_click.click(button='left')
                    if kb.is_pressed('0'):
                        print('stop')
                        break
                    if kb.is_pressed('0'):
                        print('stop')
                        break
                if kb.is_pressed('0'):
                    break

    def find_corner_pixel(self):
        flag = 0
        pic = pyautogui.screenshot(region=(560, 805, 210, 380))
        #pic.save(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\test.png")
        width, height = pic.size
        for x in range(0, width, 1):
            for y in range(0, height, 1):
                r, g, b = pic.getpixel((x, y))
                if (
                    (b in range(110, 130))
                    and (r in range(220, 240))
                    and (g in range(170, 190))
                ):
                    test=x,y
                    #23, 226, 850, 850))
                    has_top_pixel=(self.get_next_pixel(x,y,pic,"t"))
                    has_left_pixel=(self.get_next_pixel(x,y,pic,"l"))
                    #print(has_top_pixel,has_left_pixel)
                    if has_top_pixel and has_left_pixel:
                        print(f"Corner at {x+560},{y+690}")
                        pyautogui.moveTo(x+560,y+690)
                        flag=1
                        break

            if flag == 1:
                break
        if flag == 1:
            return True
        else:
            return False

    def do_jewel_stuff(self):
        stash_pos=85,315
        first_inv_pos=2595, 1230
        pyautogui.moveTo(first_inv_pos)
        pyautogui.click(button='right')
        for y in range(12):
            for x in range (12):
                pyautogui.moveTo(stash_pos[0]+x*105, stash_pos[1]+y*105)
                time.sleep(0.4)
                with pyautogui.hold('shift'):
                    pyautogui.click(button='left')
                if kb.is_pressed('0'):
                    print('stop')
                    return

    def empty_stash(self):
        stash_pos=85,315
        for y in range(12):
            for x in range (12):
                pyautogui.moveTo(stash_pos[0]+x*105, stash_pos[1]+y*105)
                time.sleep(0.1)
                with pyautogui.hold('ctrl'):
                    pyautogui.click(button='left')
                if kb.is_pressed('0'):
                    print('stop')
                    return

    def empty_inventory(self):
        for y in range(5):
            for x in range (12):
                pyautogui.moveTo(2595+x*105, 1230+y*105)
                with pyautogui.hold('ctrl'):
                    pyautogui.click(button='left')
                if kb.is_pressed('0'):
                    print('stop')
                    return

    def get_next_pixel(self,x,y,pic,direction):
        if "l" in direction:
            r, g, b = pic.getpixel((x-1, y))
            if (
                        (b in range(110, 130))
                        and (r in range(220, 240))
                        and (g in range(170, 190))
                    ):
                return True
        if "t" in direction :
            r, g, b = pic.getpixel((x, y-1))
            if (
                        (b in range(110, 190))
                        and (r in range(200, 240))
                        and (g in range(150, 200))
                    ):
                return True

    def run_magic_craft(self):
        modifier_found = 0
        while True:
            if self.magic_craft_found!=1:
                self.magic_craft()
            elif self.magic_craft_found==1:
                self.magic_craft_found = 0
                break
            if kb.is_pressed('0'):
                self.magic_craft_found=0
                break

    def haggle(self,coins):
        reset=1895,1745
        last_inv_slot_pos=3755,1650
        inv_slot_item=''
        pyautogui.moveTo(last_inv_slot_pos)
        pyperclip.copy('')
        pyautogui.hotkey('ctrl', 'c')
        inv_slot_item = pyperclip.paste()
        if inv_slot_item != '':
            return
        for coin in range(coins):
            margin_x = 640
            margin_y = 370
            first_item = 675, 575
            x_diff = 105
            y_diff = 105
            confirm = 1262, 1723
            haggle_close = 1590, 424
            haggle_start = 1016, 1609
            haggle_end = 1470, 1610
            pyautogui.moveTo(600, 350)
            pyautogui.click(button='left')
            buy = ["Chaos Orb", 'Orb of Alteration', "Gemcutter's Prism", 'Stacked Deck', 'Aetheric Fossil',
                   'Orb of Scouring', 'Splinter of', 'Timeless', 'Orb of Fusing', 'Ritual Splinter',
                   'Deft Fossil', 'Vaal Orb', 'Ancient Orb','Ancient Shard', "Rogue's Marker","Legion",'Map is occupied','Blueprint','Divine Orb','Exalted Orb',
                   'Sextant','Gold Oil','Silver Oil','Cortex','Prime Chaotic Resonator','Mirror of Kalandra','Mirror Shard','Mirror','Level: 21 (Max)','Quality: +23%',
                   'Shuddering Fossil', 'Corroded Fossil', 'Orb of Chance', 'Orb of Regret']  #'Orb of Alchemy',
            box_image = cv2.imread(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\box.png", 0)
            confirm_button_image = cv2.imread(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\confirm_button.png", 0)
            confirm_button_highlight_image = cv2.imread(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\confirm_button_highlight.png", 0)
            barrier_image = cv2.imread(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\barrier.png", 0)
            inventory = pyautogui.screenshot(region=(600, 350, 1300, 1400))  # Tujens inventory
            inventory.save(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\inventory.png")
            image = cv2.imread(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\inventory.png")
            for x in range(2):
                print(x)
                for y in range(11):
                    pyautogui.moveTo(675 + x * y_diff, 575 + y * x_diff)
                    pyautogui.hotkey('ctrl', 'c')
                    haggle_item = pyperclip.paste()
                    barrier = 0
                    counter = 0
                    for item in buy:
                        if item in haggle_item:
                            if item == 'Prime Chaotic Resonator':
                                y=y+1
                            pyautogui.click(button='left')
                            while True:
                                counter += 1
                                if barrier == 1:
                                    haggle_start = haggle_end[0] + margin_x - int((haggle_mid[0]) / 2 * 1.2), haggle_end[1] + margin_y
                                else:
                                    haggle_start = 1016, 1609
                                while True:
                                    inventory = pyautogui.screenshot(region=(600, 350, 1300, 1500))  # Tujens inventory
                                    inventory.save(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\inventory.png")
                                    image = cv2.imread(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\inventory.png")
                                    try:
                                        top_left, bottom_right = self.find_object(image, box_image)
                                        break
                                    except:
                                        time.sleep(0.5)
                                haggle_end = top_left[0], top_left[1]
                                haggle_mid = haggle_end[0] + margin_x - haggle_start[0], haggle_end[1] + margin_y - \
                                             haggle_start[1]
                                if x==0:
                                    if haggle_mid[0]>=30:
                                        pyautogui.moveTo(top_left[0] + margin_x, top_left[1] + margin_y)
                                        pyautogui.mouseDown(button='left')
                                        pyautogui.mouseDown(x=haggle_end[0] + margin_x - int((haggle_mid[0]) / 2 * 1.2),
                                                            y=haggle_end[1] + margin_y, button='left')
                                        pyautogui.dragTo(x=haggle_end[0] + margin_x - int((haggle_mid[0]) / 2 * 1.2),
                                                         y=haggle_end[1] + margin_y, button='left', duration=0.3)
                                pyautogui.moveTo(confirm)
                                pyautogui.click(button='left')
                                if barrier==1:
                                    time.sleep(0.2)
                                inventory = pyautogui.screenshot(region=(900, 1150, 700, 700))  # Tujens inventory
                                inventory.save(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\inventory.png")
                                image = cv2.imread(r"C:\Users\tilof\PycharmProjects\Memory_Rarifier\inventory.png")
                                confirm_left, confirm_right = self.find_object(image, confirm_button_image)
                                if confirm_left == '':
                                    confirm_left, confirm_right = self.find_object(image, confirm_button_highlight_image)
                                if confirm_left == '' or x==1:
                                    print("Test2")
                                    break
                                else:
                                    barrier = 1
                                if kb.is_pressed('0'):
                                    return
                                print("Test")
                            pyautogui.moveTo(last_inv_slot_pos)
                            pyperclip.copy('')
                            pyautogui.hotkey('ctrl', 'c')
                            inv_slot_item = pyperclip.paste()
                            if inv_slot_item != '':
                                return
                    if haggle_item == '':
                        break
                    pyperclip.copy('')
                    if kb.is_pressed('0'):
                        return
            pyautogui.moveTo(reset)
            pyautogui.click(button='left')

    def on_press(self,key):
        if hasattr(key, 'vk') and key.vk == 107:#+
            self.prepare()
        elif hasattr(key, 'vk') and key.vk == 109:#-
            self.trade_in_divs()
        elif hasattr(key, 'vk') and key.vk == 111:#num divide
            self.open_and_stash_stacks(key)
        elif hasattr(key, 'vk') and key.vk == 106:#num mult
            while True:
                if not self.find_corner_pixel():
                    self.magic_craft()
                if kb.is_pressed('0'):
                    break
        elif hasattr(key, 'vk') and key.vk == 103:#num 7
            self.trade_in_divs()
        elif hasattr(key, 'vk') and key.vk == 97:  # num 1
            self.empty_inventory()
        elif hasattr(key, 'vk') and key.vk == 98:  # num 2
            self.do_jewel_stuff()
        elif hasattr(key, 'vk') and key.vk == 99:  # num 3
            self.empty_stash()
        elif hasattr(key, 'vk') and key.vk == 100:  # num 4
            self.enchant_to_chat()

    def find_object(self,img,object):
        top_left = ''
        bottom_right = ''
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(gray, object, cv2.TM_CCOEFF_NORMED)
        threshold = 0.81
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:
            top_left = max_loc
            bottom_right = (top_left[0] + object.shape[1], top_left[1] + object.shape[0])
            #cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
            #cv2.imshow('Objekt gefunden', img)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
        return top_left, bottom_right


if __name__ == '__main__':
    test=craft()
    # Register all of our keybindings
    register_hotkeys(test.bindings)

    # Finally, start listening for keypresses
    start_checking_hotkeys()


    #pyautogui.mouseInfo()
    pyautogui.PAUSE = 0.02
    gui = CraftGUI()
    gui.run()

