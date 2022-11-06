
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
TERMINAL = "gnome-terminal" 
FONT_NERD = "FiraCode Nerd Font Mono"
FONT_SIZE = 14
PADDING = 3
COLORS = {
    "rosewater"   : "#f4dbd6",
    "flamingo"    : "#f0c6c6",
    "pink"        : "#f5bde6",
    "mauve"       : "#c6a0f6",
    "red"         : "#ed8796",
    "maroon"      : "#ee99a0",
    "peach"       : "#f5a97f",
    "yellow"      : "#eed49f",
    "green"       : "#a6da95",
    "teal"        : "#8bd5ca",
    "sky"         : "#91d7e3",
    "sapphire"    : "#7dc4e4",
    "blue"        : "#8aadf4",
    "lavender"    : "#b7bdf8",
    "text"        : "#cad3f5",
    "subtext1"    : "#b8c0e0",
    "subtext0"    : "#a5adcb",
    "overlay2"    : "#939ab7",
    "overlay1"    : "#8087a2",
    "overlay0"    : "#6e738d",
    "surface2"    : "#5b6078",
    "surface1"    : "#494d64",
    "surface0"    : "#363a4f",
    "base"        : "#24273a",
    "mantle"      : "#1e2030",
    "crust"       : "#181926"
}
# Run autostart scipt automatically at startup
@hook.subscribe.startup_once
def autostart():
    path = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([path])

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
    Group("3", label=""),
    Group("4", label=""),
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
        top=bar.Bar(
            [
                widget.Spacer(
                    length = 10
                ),
                widget.Image(
                    filename = "~/.config/qtile/images/flat_linux.png",
                ),
                widget.Spacer(
                    length = 10
                ),
                widget.GroupBox(
                    fontsize                    = 27,
                    margin_y                    = 3,
                    margin_x                    = 5,
                    borderwidth                 = 0,
                    font                        = FONT_NERD,
                    active                      = COLORS["green"],
                    block_highlight_text_color  = COLORS["red"],
                    inactive                    = COLORS["surface0"],
                    rounded                     = True,
                    disable_drag                = True,
                ),
                widget.CurrentLayout(),
                # widget.StatusNotifier() # If wayland, disable Systray,
                widget.Systray(),
                widget.Spacer(
                    length = bar.STRETCH,
                ),
                widget.Image(
                    filename = "~/.config/qtile/images/sun.png",
                    margin   = 7,
                ),
                widget.Backlight(
                    font                 = FONT_NERD,
                    foreground           = COLORS["yellow"],
                    backlight_name       = "amdgpu_bl1",
                    fontsize             = 12,
                    padding              = 0,
                ),
                widget.Spacer(
                    length = 10
                ),
                widget.Image(
                    filename = "~/.config/qtile/images/vol.png",
                    margin   = 8,
                ),
                widget.PulseVolume(
                    cardid      = 1,
                    foreground  = COLORS["blue"],
                    fontsize    = 12,
                    padding     = 0,
                ),
                widget.Spacer(
                    length = 10,
                ),                       
                widget.Image(
                    filename  = '~/.config/qtile/images/bat.png',
                    margin    = 7
                ),         
                widget.Battery(format=' {percent:2.0%}',
                    font        = FONT_NERD,
                    foreground  = COLORS["red"],
                    fontsize    = 12,
                    padding     = 0,
                ),
                widget.Spacer(
                    length = 10,
                ),                       
                widget.Clock(
                    format="%d-%m-%Y %a %H:%M"
                ),
                widget.Spacer(
                    length = 10,
                ),                       
            ],
            40,
            margin      = [12, 12, 12, 12],
            background  = COLORS["base"]
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
