#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

import helpers.logs as logs


def activate_trackball_scrolling(filename):
    root_dir = Path(__file__).resolve().parent.parent.parent
    config_path = root_dir.joinpath('input', filename.rstrip('.py'))

    # Find configuration file
    if config_path.is_file():
        with open(str(config_path), 'r') as file:
            config_lines = [line for line in file]

        device_config = {}
        for line in config_lines:
            split_line = line.split('||')
            type = split_line[0].strip()
            button = split_line[1].strip()
            device_config[type] = button
    else:
        warn = 'No device config file found.'
        logs.logger(filename).warning(warn)
        sys.exit(1)

    try:
        devices_command = 'xinput list'
        output = subprocess.run(devices_command.split(), capture_output=True, check=True)
    except subprocess.CalledProcessError as err:
        logs.logger(filename).error(err)
        sys.exit(1)
    output_array = output.stdout.decode('utf-8').split('\n')

    device_found = False

    for device in device_config:

        # Define settings
        settings = {
            'Scroll Method Enabled': ['0,', '0,', '1'],
            'Button Scrolling Button': device_config[device]
        }

        # Find the device and set scrolling method
        for line in output_array:
            if device in line and 'slave  keyboard' not in line: # double space also present in output
                properties = line.split('\t')
                device_id = properties[1].split("=")[-1]

                for name, setting in settings.items():
                    command = ['xinput', 'set-prop', str(device_id), 'libinput {}'.format(name)]
                    command.extend(setting)
                    process = subprocess.run(command, capture_output=True)
                    if process.returncode != 0:
                        err = "Error setting '{}'".format(name)
                        logs.logger(filename).error(err)
                        sys.exit(1)

                info = 'Trackball scrolling enabled for {}'.format(device)
                logs.logger(filename).info(info)
                device_found = True
                break

    if not device_found:
        warn = 'No connected devices found.'
        logs.logger(filename).warning(warn)
        sys.exit(1)

    return
