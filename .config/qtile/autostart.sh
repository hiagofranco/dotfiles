#!/bin/bash

# Configure touchpad to tap to click and natural scrolling
xinput set-prop "ELAN050A:01 04F3:3158 Touchpad" "libinput Tapping Enabled" 1
xinput set-prop "ELAN050A:01 04F3:3158 Touchpad" "libinput Natural Scrolling Enabled" 1
