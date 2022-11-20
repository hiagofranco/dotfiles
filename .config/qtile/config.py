
from libqtile import backend, bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration
from qtile_extras.widget import modify

import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

mod = "mod4"
terminal = "alacritty"
# Gruv box pallete
colors = {
    "bg":      "#292828",
    "fg":      "#d4be98",
    "black":   "#3c3836",
    "red":     "#ea6962",
    "green":   "#a9b665",
    "yellow":  "#d8a657",
    "blue":    "#7daea3",
    "magenta": "#d3869b",
    "cyan":    "#89b482",
    "white":   "#d4be98"
}

keys = [

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
   
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
   
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "m", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Browser
    Key([mod], "b", lazy.spawn("firefox"), desc="Spawn Firefox"),

    # Control Brightness Level
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%+"), desc="Increase brightness level by 5%"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Decrease brightness level by 5%"),
    
    # Control Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse set Master 5%+"), desc="Increase audio volume by 5%"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse set Master 5%-"), desc="Decrease audio volume by 5%"),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse set Master toggle"), desc="Mute or Unmute audio"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next music"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous music"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause music"),

    # Rofi menus
    Key([mod], "s", lazy.spawn("/home/hiago/.config/rofi/scripts/launcher_t1"), desc="Rofi launcher"),
    Key([mod], "p", lazy.spawn("/home/hiago/.config/rofi/scripts/powermenu_t1"), desc="Rofi powermenu"),
]

#groups = [Group(i) for i in "123qwe"]

groups = [
    Group("1", label = ""),
    Group("2", label = ""),
    Group("3", label = ""),
    Group("q", label = "ﭮ"),
    Group("w", label = "阮"),
    Group("e", label = "嗢"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_configs = {
        "border_focus"       : colors["magenta"],
        "border_normal"      : colors["bg"],
        "margin"             : 5,
        "single_margin"      : 5,
}

layouts = [
    layout.Columns(**layout_configs),
    layout.Max(**layout_configs),
    layout.MonadTall(**layout_configs),
]

widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def get_decoration(side: str = '') -> dict:
    return {
            "decorations": [
                RectDecoration(
                    filled = True,
                    radius = {
                        'left' : [8,0,0,8],
                        'right': [0,8,8,0]
                    }.get(side, 8),
                    use_widget_background = True,
                )
            ]
    }

def get_powerline(path: str, size = 9) -> dict:
    return {
            "decorations": [
                PowerLineDecoration(
                    path = path,
                    size = size,
                )
            ]
    }

screens = [
    Screen(
        wallpaper = "~/.config/qtile/images/wp.png",
        wallpaper_mode = "fill",
        top=bar.Bar(
            [
                widget.Spacer(length = 2),
                # Logo
                modify(
                    widget.TextBox,
                    background = colors["green"],
                    foreground = colors["bg"],
                    **get_decoration(),
                    fontsize = 15,
                    text = "  ",
                    padding = 17,
                ),
                # Separator
                widget.TextBox(
                    foreground = colors["fg"],
                    offset = 0,
                    padding = 8,
                    text = "",
                ),
                widget.GroupBox(
                    borderwidth = 1,
                    highlight_color = colors["bg"],
                    highlight_method = "line",
                    padding = 7,
                ),
                # Separator
                widget.TextBox(
                    foreground = colors["fg"],
                    offset = 4,
                    padding = 7,
                    text = "",
                ),
                # Volume icon and percentage
                modify(
                    widget.TextBox,
                    background = colors["magenta"],
                    foreground = colors["bg"],
                    text = " ",
                    **get_decoration("left"),
                ),
                modify(
                    widget.Volume,
                    background = colors["magenta"],
                    foreground = colors["bg"],
                    **get_powerline("arrow_right"),
                ),
                # Brightness control and percentage
                widget.TextBox(
                    background = colors["yellow"],
                    foreground = colors["bg"],
                    text = " ",
                ),
                modify(
                    widget.Backlight,
                    background = colors["yellow"],
                    foreground = colors["bg"],
                    backlight_name = "amdgpu_bl0",
                    **get_powerline("arrow_right"),
                ),
                # Updates
                widget.TextBox(
                    background = colors["red"],
                    foreground = colors["bg"],
                    text = " ",
                ),
                modify(
                    widget.CheckUpdates,
                    background = colors["red"],
                    foreground = colors["bg"],
                    colour_have_updates = colors["bg"],
                    colour_no_updates = colors["bg"],
                    display_format = "{updates} updates",
                    distro = "Ubuntu",
                    initial_text = "No updates ",
                    no_update_string = "No updates ",
                    padding = 0,
                    update_interval = 3600,
                    **get_decoration("right")
                ),
                widget.Spacer(),
                widget.WindowName(
                    foreground = colors["fg"],
                    format = "{name}",
                    max_chars = 40,
                    width = bar.CALCULATED,
                ),
                widget.Spacer(),
                # Systray
                widget.Systray(),
                # CPU
                modify(
                    widget.TextBox,
                    background = colors["green"],
                    foreground = colors["bg"],
                    text = " ",
                    **get_decoration("left"),
                ),
                modify(
                    widget.CPU,
                    background = colors["green"],
                    foreground = colors["bg"],
                    format = "{load_percent:.0f}%",
                    **get_powerline("arrow_right")
                ),
                # RAM
                widget.TextBox(
                    background = colors["yellow"],
                    foreground = colors["bg"],
                    text = "﬙",
                ),
                modify(
                    widget.Memory,
                    background = colors["yellow"],
                    foreground = colors["bg"],
                    format = "{MemUsed: .0f}{mm} ",
                    **get_powerline("arrow_right"),
                ),
                # Disk
                widget.TextBox(
                    background = colors["cyan"],
                    foreground = colors["bg"],
                    text = " ",
                ),
                modify(
                    widget.DF,
                    background = colors["cyan"],
                    foreground = colors["bg"],
                    format = "{f} GB",
                    partition = "/",
                    visible_on_warn = False,
                    warn_color = colors["fg"],
                    **get_powerline("arrow_right"),
                ),
                # Battery
                widget.TextBox(
                    background = colors["red"],
                    foreground = colors["bg"],
                    text = " ",
                ),
                modify(
                    widget.Battery,
                    background = colors["red"],
                    foreground = colors["bg"],
                    format = "{char} {percent:2.0%} ",
                    **get_decoration("right"),
                ),
                # Separator
                widget.TextBox(
                    foreground = colors["fg"],
                    offset = 4,
                    padding = 7,
                    text = "",
                ),
                # Clock
                modify(
                    widget.TextBox,
                    background = colors["magenta"],
                    foreground = colors["bg"],
                    text = "  ",
                    **get_decoration("left"),
                ),
                modify(
                    widget.Clock,
                    background = colors["magenta"],
                    foreground = colors["bg"],
                    format = "%D %a %H:%M ",
                    **get_decoration("right"),
                ),
                widget.TextBox(
                    foreground = colors["fg"],
                    offset = 0,
                    padding = 8,
                    text = "",
                ),
                widget.CurrentLayoutIcon(),
                widget.Spacer(length = 2),
            ],
            size = 20,
            opacity = 1,
            margin = [8, 8, 2, 8],
            border_width = 4,
            border_color = colors["bg"],
            background = colors["bg"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
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
