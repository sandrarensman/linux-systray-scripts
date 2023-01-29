# linux-systray-scripts

## About

This repository contains GTK AppIndicator scripts that I use on my Linux machines. They are adapted from tutorials like [this AppIndicator tutorial](http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html), and answers to questions on for example [Ask Ubuntu](https://askubuntu.com/questions/770036/appindicator3-set-indicator-icon-from-file-name-or-gdkpixbuf).

This is very much a work in progress, and provided 'as is'. You are welcome to use these scripts or use parts of them to build your own indicator.

The icons are from the [FontAwesome](https://fontawesome.com/icons) project.

## How to use

### Enabling the menu on startup

Copy the repo to a location in your home folder. Add the relevant script(s) in `/scripts` to Startup Applications. Each script will start a seperate AppIndicator instance. The names of the scripts can be changed, as long as you also change the names of the corresponding icon and input files. When the script is running, an icon will show in the systray.

### Custom menus for (web) applications

Setup of the input files:

- Each line consists of a label (the first part before `||`) and may contain a command (the second part).
- In the examples, most of the commands refer to progressive web apps created from a Chromium-based browser. You can of course use any executable.
- Blank lines create a separator in the menu.
- Lines starting with a `-` will attach to the previous menu item as a submenu.
- Menu items that have submenu items following them, cannot contain a command.

### Trackball scrolling

By default, the script will enable trackball scrolling on Loggitech M570 and MX Ergo using the forward button on the mouse. The script may work with other trackball devices, but this has not been tested.

Custom configurations for device type and button can be set in `/input/trackball_scrolling`. Use a new line for each device.

## Dependencies

pycairo | `python3-cairo`
PyGObject | `python3-gi`
