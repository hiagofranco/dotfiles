#!/bin/bash

# Enable compositor
picom --config /home/hiago/.config/picom/picom.conf -b

# Configure touchpad to tap to click and natural scrolling
xinput set-prop "UNIW0001:00 093A:0003 Touchpad" "libinput Natural Scrolling Enabled" 1
xinput set-prop "UNIW0001:00 093A:0003 Touchpad" "libinput Tapping Enabled" 1

# Set screen lock
xss-lock -- betterlockscreen --lock &
