#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
import subprocess
from pathlib import Path

from gi.repository import AppIndicator3, Gtk


class Indicator():
    def __init__(self, name):
        self.app = name
        self.dir = Path(__file__).resolve().parent.parent.parent
        icondir = str(self.dir.joinpath('icons'))
        iconpath = '{0}/{1}.svg'.format(icondir, name)
        self.indicator = AppIndicator3.Indicator.new(
            self.app,
            iconpath,
            AppIndicator3.IndicatorCategory.SYSTEM_SERVICES
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())

    def create_menu(self):
        # Create menu items for displaying enabled/quit
        self.menu = Gtk.Menu()
        self.cmdpath = self.dir.joinpath('input', self.app)
        # If there is a corresponding input document, add extra menu items
        if self.cmdpath.is_file():
            self.add_commands()
            separator = Gtk.SeparatorMenuItem()
            self.menu.append(separator)
        item_quit = Gtk.MenuItem(label='Quit')
        item_quit.connect('activate', self.stop)
        self.menu.append(item_quit)
        self.menu.show_all()
        return self.menu

    def add_commands(self):
        last_submenu = None
        with open(str(self.cmdpath), 'r') as file:
            cmd_data = [line.rstrip().split('||') for line in file]
        for cmd in cmd_data:
            cmd_label = cmd[0].strip()
            if cmd_label == '':
                separator = Gtk.SeparatorMenuItem()
                self.menu.append(separator)
            elif cmd_label.startswith('-'):
                # Check if we need to start a new submenu
                if self.menu_item != last_submenu:
                    self.submenu = Gtk.Menu()
                    self.menu_item.set_submenu(self.submenu)

                self.submenu_item = Gtk.MenuItem(label=cmd_label.strip('- '))
                self.submenu_item.connect('activate', self.run_command, cmd[1].strip())
                self.submenu.append(self.submenu_item)

                # Remember the menu item that we last attached a submenu to
                last_submenu = self.menu_item
            else:
                self.menu_item = Gtk.MenuItem(label=cmd_label)
                if len(cmd) > 1:
                    self.menu_item.connect('activate', self.run_command, cmd[1].strip())
                self.menu.append(self.menu_item)

    def run_command(self, widget, command):
        subprocess.Popen(['/bin/bash', '-c', command])

    def stop(self, source):
        Gtk.main_quit()
