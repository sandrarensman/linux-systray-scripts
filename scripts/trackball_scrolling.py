#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

import packages.functions as func


def enable_scrolling(filepath):
    device_config = {
        'MX Ergo': '9',
        'M570': '9'
    }

    root_path = Path(__file__).resolve().parent.parent
    config_path = root_path.joinpath('input', func.get_filename(filepath))

    # Check if user has set a custom configuration
    if config_path.is_file():
        with open(str(config_path), 'r') as file:
            config_lines = [line for line in file]

        custom_device_config = {}
        for line in config_lines:
            split_line = line.split('||')
            type = split_line[0].strip()
            button = split_line[1].strip()
            if type in device_config:
                custom_device_config[type] = button
        device_config = custom_device_config

    try:
        devices_command = 'xinput list'
        output = subprocess.run(devices_command.split(), capture_output=True, check=True)
    except subprocess.CalledProcessError as err:
        func.logger(__file__).error(err)
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
            if device in line and 'slave  keyboard' not in line: # double space on purpose
                properties = line.split('\t')
                device_id = properties[1].split("=")[-1]

                for name, setting in settings.items():
                    command = ['xinput', 'set-prop', str(device_id), 'libinput {}'.format(name)]
                    command.extend(setting)
                    process = subprocess.run(command, capture_output=True)
                    if process.returncode != 0:
                        err = "Error setting '{}'".format(name)
                        func.logger(__file__).error(err)
                        sys.exit(1)

                info = 'Trackball scrolling enabled for {}'.format(device)
                func.logger(__file__).info(info)
                device_found = True
                break

    if not device_found:
        warn = 'No supported devices found.'
        func.logger(__file__).warning(warn)
        sys.exit(1)

    return

if __name__ == '__main__':
    filepath = __file__
    enable_scrolling(filepath)
    func.create_indicator(filepath)
