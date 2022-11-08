
#  _      _ _                    _               
# | |    (_| |                  (_)              
# | |     _| |__  _ __ __ _ _ __ _  ___ _ __ ___ 
# | |    | | '_ \| '__/ _` | '__| |/ _ | '__/ __|
# | |____| | |_) | | | (_| | |  | |  __| |  \__ \
# |______|_|_.__/|_|  \__,_|_|  |_|\___|_|  |___/                                                
                                                                
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os
import subprocess

#  _____        __ _                
# |  __ \      / _(_)               
# | |  | | ___| |_ _ _ __   ___ ___ 
# | |  | |/ _ |  _| | '_ \ / _ / __|
# | |__| |  __| | | | | | |  __\__ \
# |_____/ \___|_| |_|_| |_|\___|___/                                   
                                   
MOD = "mod4" # Super Key
TERMINAL = "alacritty" 
FONT_NERD = "FiraCode Nerd Font Mono"
FONT_SIZE = 14
PADDING = 3
COLORS = {
    "rosewater"   : "#f5e0dc",
    "flamingo"    : "#f2cdcd",
    "pink"        : "#f5c2e7",
    "mauve"       : "#cba6f7",
    "red"         : "#f38ba8",
    "maroon"      : "#eba0ac",
    "peach"       : "#fab387",
    "yellow"      : "#f9e2af",
    "green"       : "#a6e3a1",
    "teal"        : "#94e2d5",
    "sky"         : "#89dceb",
    "sapphire"    : "#74c7ec",
    "blue"        : "#89b4fa",
    "lavender"    : "#b4befe",
    "text"        : "#cdd6f4",
    "subtext1"    : "#bac2de",
    "subtext0"    : "#a6adc8",
    "overlay2"    : "#9399b2",
    "overlay1"    : "#7f849c",
    "overlay0"    : "#6c7086",
    "surface2"    : "#585b70",
    "surface1"    : "#45475a",
    "surface0"    : "#313244",
    "base"        : "#1e1e2e",
    "mantle"      : "#181825",
    "crust"       : "#11111b"
}

#  _    _             _        
# | |  | |           | |       
# | |__| | ___   ___ | | _____ 
# |  __  |/ _ \ / _ \| |/ / __|
# | |  | | (_) | (_) |   <\__ \
# |_|  |_|\___/ \___/|_|\_\___/

# Run autostart script automatically at startup
@hook.subscribe.startup_once
def autostart():
    # execute autostart.sh
    path = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([path])

def backlight_file_name() -> str:
    # Get Backlight file name
    name = os.listdir("/sys/class/backlight/")
    return str(name[0])

#  _  __              
# | |/ /              
# | ' / ___ _   _ ___ 
# |  < / _ | | | / __|
# | . |  __| |_| \__ \
# |_|\_\___|\__, |___/
#            __/ |    
#           |___/     

keys = [

    # Switch between windows
    Key([MOD], "h",
        lazy.layout.left(),
        desc="Move focus to left"
    ),
    Key([MOD], "l",
        lazy.layout.right(),
        desc="Move focus to right"
    ),
    Key([MOD], "j",
        lazy.layout.down(),
        desc="Move focus down"
    ),
    Key([MOD], "k",
        lazy.layout.up(),
        desc="Move focus up"
    ),
    Key([MOD], "Left",
        lazy.layout.left(),
        desc="Move focus to left"
    ),
    Key([MOD], "Right",
        lazy.layout.right(),
        desc="Move focus to right"
    ),
    Key([MOD], "Down",
        lazy.layout.down(),
        desc="Move focus down"
    ),
    Key([MOD], "Up",
        lazy.layout.up(),
        desc="Move focus up"
    ),
    Key([MOD], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"
    ),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([MOD, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    Key([MOD, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
    ),
    Key([MOD, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),
    Key([MOD, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"
    ),
    Key([MOD, "shift"], "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    Key([MOD, "shift"], "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
    ),
    Key([MOD, "shift"], "Down",
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),
    Key([MOD, "shift"], "Up",
        lazy.layout.shuffle_up(),
        desc="Move window up"
    ),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([MOD, "control"], "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"
    ),
    Key([MOD, "control"], "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"
    ),
    Key([MOD, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"
    ),
    Key([MOD, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"
    ),
    Key([MOD, "control"], "Left",
        lazy.layout.grow_left(),
        desc="Grow window to the left"
    ),
    Key([MOD, "control"], "Right",
        lazy.layout.grow_right(),
        desc="Grow window to the right"
    ),
    Key([MOD, "control"], "Down",
        lazy.layout.grow_down(),
        desc="Grow window down"
    ),
    Key([MOD, "control"], "Up",
        lazy.layout.grow_up(),
        desc="Grow window up"
    ),
    Key([MOD], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"
    ),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [MOD, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    
    Key([MOD], "Return",
        lazy.spawn(TERMINAL),
        desc="Launch terminal"
    ),
    
    # Toggle between different layouts as defined below
    Key([MOD], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
    ),
    
    Key([MOD], "w",
        lazy.window.kill(),
        desc="Kill focused window"
    ),
    Key([MOD, "control"], "r",
        lazy.reload_config(),
        desc="Reload the config"
    ),
    Key([MOD, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
    ),
    Key([MOD], "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"
    ),

    # --- User defined --- #
    # APT packages required:
    # - amixer (usually installed by default)
    # - brightnessctl (also you need to add your user to video group)
    # - playerctl
    # - Brave Browser
    # - Shutter
    # - libghc-iwlib-dev
    # - pip install iwlib
    # https://github.com/jluttine/rofi-power-menu
    
    Key([MOD], "b",
        lazy.spawn("brave-browser"),
        desc="Spawn Internet Browser"
    ),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -c 1 set Master 5%+"),
        desc="Increase Volume by 5%"
    ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -c 1 set Master 5%-"),
        desc="Decrease Volume by 5%"
    ),
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl s 10%+"),
        desc="Increase brightness level by 10%"
    ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl s 10%-"),
        desc="Decrease brightness level by 10%"
    ),
    Key([], "XF86AudioMute",
        lazy.spawn("amixer -c 1 -D pulse set Master 1+ toggle"),
        desc="Volume Mute"
    ),
    Key([], "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Player Pause/Play"
    ),
    Key([], "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Player Previous"
    ),
    Key([], "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Player Next"
    ),
    Key([], "Print",
        lazy.spawn("shutter -f"),
        desc="Screenshot"
    ),
    Key([MOD], "s",
        lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a rofi"
    ),
    Key([MOD], "f",
        lazy.window.toggle_fullscreen(),
        desc="Set window fullscreen"
    ),
    Key([MOD], "q",
        lazy.spawn("rofi -show power-menu -modi \"power-menu:rofi-power-menu --choices=shutdown/reboot/logout/lockscreen\""),
        desc="Open power menu"
    ),
]

#   _____                           
#  / ____|                          
# | |  __ _ __ ___  _   _ _ __  ___ 
# | | |_ | '__/ _ \| | | | '_ \/ __|
# | |__| | | | (_) | |_| | |_) \__ \
#  \_____|_|  \___/ \__,_| .__/|___/
#                        | |        
#                        |_|        

groups = [
    Group("1", label=""),
    Group("2", label=""),
    Group("3", label=""),
    Group("4", label="嗢"),
    Group("5", label="調"),
    Group("6", label="ﭮ")
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [MOD],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [MOD, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

#  _                             _       
# | |                           | |      
# | |     __ _ _   _  ___  _   _| |_ ___ 
# | |    / _` | | | |/ _ \| | | | __/ __|
# | |___| (_| | |_| | (_) | |_| | |_\__ \
# |______\__,_|\__, |\___/ \__,_|\__|___/
#               __/ |                    
#              |___/                     

layouts = [
    layout.Columns(
        border_focus   = COLORS["sapphire"],
	    border_normal  = COLORS["base"],
	    margin         = 12,
	    border_width   = 2,
    ),
    layout.Max(
        border_focus   = COLORS["sapphire"],
	    border_normal  = COLORS["base"],
	    margin         = 12,
	    border_width   = 2,
    ),
    layout.MonadTall(	
        border_focus   = COLORS["sapphire"],
	    border_normal  = COLORS["base"],
	    margin         = 12,
	    border_width   = 2,
	),
    layout.Floating(	
        border_focus   = COLORS["sapphire"],
	    border_normal  = COLORS["base"],
	    margin         = 12,
	    border_width   = 2,
	),
]

# __          ___     _            _       
# \ \        / (_)   | |          | |      
#  \ \  /\  / / _  __| | __ _  ___| |_ ___ 
#   \ \/  \/ / | |/ _` |/ _` |/ _ | __/ __|
#    \  /\  /  | | (_| | (_| |  __| |_\__ \
#     \/  \/   |_|\__,_|\__, |\___|\__|___/
#                        __/ |             
#                       |___/              

widget_defaults = dict(
    font=FONT_NERD,
    fontsize=FONT_SIZE,
    padding=PADDING,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        
        wallpaper="~/.config/qtile/images/wallpaper_astro.jpg",
        
        top=bar.Bar(
            
            [
                widget.Spacer(
                    length     = 20,
                    background = COLORS["base"] 
                ),
                
                widget.Image(
                    filename   = "~/.config/qtile/images/flat_linux.png",
                    margin     = 2,
                    background = COLORS["base"],
                    mouse_callbacks = {
                        "Button1": lazy.spawn("rofi -show drun")
                    }
                ),
                
                widget.Image(
                    filename='~/.config/qtile/images/6.png',
                ),
                
                widget.GroupBox(
                    fontsize                    = 27,
                    borderwidth                 = 3,
                    font                        = FONT_NERD,
                    active                      = COLORS["red"],
                    block_highlight_text_color  = COLORS["green"],
                    inactive                    = COLORS["surface0"],
                    foreground                  ="#4B427E",
                    background                  ="#4B427E",
                    this_current_screen_border  ="#52548D",
                    this_screen_border          ="#52548D",
                    other_current_screen_border ="#52548D",
                    other_screen_border         ="#52548D",
                    urgent_border               ="#52548D",
                    rounded                     = True,
                    disable_drag                = True,
                ),
                
                widget.Image(
                    filename="~/.config/qtile/images/5.png",
                ),
                
                widget.CurrentLayoutIcon(
                    background = "#52548D",
                    padding    = 0,
                    scale      = 0.5,
                ),
                
                widget.CurrentLayout(
                    background ="#52548D"
                ),
                
                widget.Image(
                    filename="~/.config/qtile/images/4.png",                
                ),
                
                widget.WindowName(
                    background         = "#7676B2",
                    format             = "{name}",
                    font               = FONT_NERD,
                    empty_group_string = "Desktop"
                ),
                
                widget.Image(
                    filename="~/.config/qtile/images/3.png",                
                ),   
                
                # widget.StatusNotifier() # If wayland, disable Systray,
                widget.Systray(
                    background="#52548D",
                    fontsize=2
                ),
                
                widget.TextBox(
                    text=" ",
                    background="#52548D"
                ),
                
                widget.Image(
                    filename="~/.config/qtile/images/2.png",                
                    background="#52548D"
                ),                      
                
                widget.TextBox(
                    text       = "盛",    
                    fontsize   = 27,
                    padding    = 2,
                    background = "#4B427E",
                    foreground = COLORS["yellow"]
                ),
                
                widget.Backlight(
                    font                 = FONT_NERD,
                    foreground           = COLORS["yellow"],
                    backlight_name       = backlight_file_name(),
                    fontsize             = 14,
                    padding              = 8,
                    background           = "#4B427E"
                ),
                
                widget.TextBox(
                    text       = "",    
                    fontsize   = 25,
                    padding    = 8,
                    background = "#4B427E",
                    foreground = COLORS["blue"]
                ),
                
                widget.PulseVolume(
                    cardid      = 1,
                    foreground  = COLORS["blue"],
                    fontsize    = 14,
                    padding     = 8,
                    background  = "#4B427E"
                ),

                widget.Net(
                    fontsize   = 14,
                    padding    = 8,
                    background = "#4B427E",
                    foreground = COLORS["flamingo"],
                    format = "{down} ↓↑{up}"
                ),

                widget.Wlan(
                    background  = "#4B427E",
                    font = FONT_NERD,
                    fontsize = 14,
                    padding = 0,
                    foreground = COLORS["green"],
                    interface = "wlp4s0",
                    disconnected_message = "睊",
                    format = "{essid} {percent:2.0%}"
                ),
                
                widget.Battery(
                    format         = " {char} {percent:2.0%}",
                    font           = FONT_NERD,
                    foreground     = COLORS["red"],
                    fontsize       = 14,
                    padding        = 8,
                    charge_char    = "",
                    discharge_char = "",
                    empty_char     = "",
                    full_char      = "",
                    update_interval= 15, # seconds
                    background     = "#4B427E"
                ),
                
                widget.Image(
                    filename   = "~/.config/qtile/images/1.png",                
                    background = "#4B427E"
                ),
                
                widget.Clock(
                    format     = "%d/%m/%Y %a %H:%M",
                    background = "#1F1D2E",
                    font       = FONT_NERD 
                ),

                widget.TextBox(
                    text            = "",
                    background      = "#1F1D2E",
                    fontsize        = 20,
                    padding         = 5,
                    mouse_callbacks = {
                        "Button1": lazy.spawn("rofi -show power-menu -modi \"power-menu:rofi-power-menu --choices=shutdown/reboot/logout/lockscreen\"")
                    }
                ),

                widget.Spacer(
                    length     = 18,
                    background = "#1F1D2E"
                ),                       
            ],
            30,
            margin = [6, 6, 6, 6]
        ),
    ),
]

#   _____             __ _           
#  / ____|           / _(_)          
# | |     ___  _ __ | |_ _  __ _ ___ 
# | |    / _ \| '_ \|  _| |/ _` / __|
# | |___| (_) | | | | | | | (_| \__ \
#  \_____\___/|_| |_|_| |_|\__, |___/
#                           __/ |    
#                          |___/     

# Drag floating layouts.
mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "Qtile"
