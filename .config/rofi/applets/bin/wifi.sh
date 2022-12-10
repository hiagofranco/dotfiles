#!/usr/bin/env bash

# Import Current Theme
source "$HOME"/.config/rofi/applets/shared/theme.bash
theme="$type/$style"

# Variables
FIELDS=SSID,SECURITY,BARS

HEADER=$(nmcli -f $FIELDS device wifi list | sed -n '1p')

LIST=$(nmcli -f $FIELDS device wifi list | sed '/^--/d' | sed -n '1!p')

KNOW_CON=$(nmcli connection show)

CUR_CON=$(nmcli -f WIFI g)

CUR_SSID=$(LANGUAGE=C nmcli -t -f ACTIVE,SSID device wifi | awk -F: '$1 ~ /^yes/ {print $2}')

# Rofi CMD
rofi_cmd() {
	rofi -dmenu \
        -p "$CUR_SSID" \
        -mesg "$HEADER" \
        -theme ${theme}
}

run_rofi() {
    echo -e "$LIST" | rofi_cmd
}

password_cmd() {
    rofi -dmenu \
        -p "Type your passwd:" \
        -theme ${theme}
}

chosen="$(run_rofi)"
