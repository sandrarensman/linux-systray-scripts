# linux-systray-scripts

## About

This repository contains GTK AppIndicator scripts that I use on my Linux machines. They are adapted from tutorials like [this AppIndicator tutorial](http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html), and answers to questions on for example [Ask Ubuntu](https://askubuntu.com/questions/770036/appindicator3-set-indicator-icon-from-file-name-or-gdkpixbuf).

This is very much a work in progress, and provided 'as is'. You are welcome to use these scripts or use parts of them to build your own indicator.

The icons are from the [FontAwesome](https://fontawesome.com/icons) project.

## How to use

### Setup

Whith these scripts, it is possible to create indicators for web apps created in Chromium-based browsers, for shortcuts to local applications, and for activating trackball scrolling on a mouse that has a trackball.

Each indicator consists of three parts that should be setup:

- an icon (SVG) file
- an input file
- a python script

These file should all have the same name.

In the input file, specify the display name for the menu item, then a separator (||), and finally the executable (containing the details for the web app or a local file path if necessary). See [Custom menus for (web) applications](#custom-menus-for-web-applications) for more info.

For configuring a trackball mouse, see [Trackball scrolling](#trackball-scrolling).

The Python script can simply be copied and renamed from a script in the `./scripts` directory.

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

The name of the mouse can be identified by running `xinput list`. You can add only part of the name in the config, as long as it is unique. The buttons can be identified by running `xev | grep -i button`.

Custom configurations for device type and button can be set in `/input/trackball_scrolling`. Use a new line for each device.

## Dependencies

pycairo | `python3-cairo`
PyGObject | `python3-gi`
Appindicator3 | `gir1.2-appindicator3-0.1`
