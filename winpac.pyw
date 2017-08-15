# -*- coding:utf-8 -*-


import urlparse

import pyautogui as pg
import pyperclip as pc

PATH = "C:\Shadowsocks-4.0.5\pac.txt"
SS_HOT_KEY = ('ctrl', 'shift', 'alt', 'p')


def copy_url():
    pg.click()
    pg.hotkey('ctrl', 'l')
    pg.hotkey('ctrl', 'c')
    pg.click()


def get_domain():
    url = pc.paste()
    return urlparse.urlparse(url).netloc


def new_text(text, domain):
    return text.replace("var domains = {", 'var domains = {\n  "%s": 1,' % domain, 1)


def reload_pac():
    pg.hotkey(*SS_HOT_KEY)


def write_domain(path, domain):
    with open(path, 'r+') as f:
        text = f.read()
        if domain not in text:
            text = new_text(text, domain)
            f.seek(0)
            f.truncate()
            f.flush()
            f.write(text)
            reload_pac()


def url2pac():
    copy_url()
    domain = get_domain()
    if domain:
        write_domain(PATH, domain)

if __name__ == '__main__':
    url2pac()