import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer
from random import randint
#import arcobattery

# black dark/light
color0 =                          "#1C1E26"
color8 =                          "#6C6F93"

# red dark/light
color1 =                          "#E9436F"
color9 =                          "#E9436F"

# green dark/light
color2 =                          "#27D796"
color10 =                         "#09F7A0"

# yellow dark/light
color3 =                          "#FAB795"
color11 =                         "#FAB795"

# blue dark/light
color4 =                          "#25B2BC"
color12 =                         "#25B2BC"

# magenta dark/light
color5 =                          "#B877DB"
color13 =                         "#B877DB"

# cyan dark/light
color6 =                          "#21BFC2"
color14 =                         "#21BFC2"

# white dark/light
color7 =                          "#FDF0ED"
color15 =                         "#f8f8f8"

#mod4 or mod = super key
mod                     = "mod4"
mod1                    = "alt"
mod2                    = "control"
home                    = os.path.expanduser('~')

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [
# SUPER + FUNCTION KEYS
    Key([mod], "f", lazy.window.toggle_fullscreen()),                   # Fullscreen
    Key([mod], "q", lazy.window.kill()),                                # Kill window

# SUPER + SHIFT KEYS
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),


# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

    ]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
group_labels = ["", "", "", "", "", "", "", "", "", "",]
# group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

group_layouts = ["columns", "columns", "columns", "columns", "columns", "columns", "columns", "columns", "columns", "columns",]
# group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

# CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

border_width = 2
margin = 12
col_mar = 12
def init_layout_theme():
    return {"margin":margin,
            "border_width": border_width,
            "border_focus": color3,
            "border_normal": color8
            }

layout_theme = init_layout_theme()

layouts = [
    layout.Columns(margin=col_mar, border_width=border_width, border_focus=color3, border_normal=color8),
    layout.MonadTall(margin=margin, border_width=border_width, border_focus=color3, border_normal=color8),
    layout.MonadWide(margin=margin, border_width=border_width, border_focus=color3, border_normal=color8),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]

# WIDGETS FOR THE BAR
def init_widgets_defaults():
    return dict(font="Ubuntu Mono",
                fontsize = 14,
                padding = 2,
                background=color0)

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    bgcolors = [color1, color2, color3, color5, color4]
    arr_len = len(bgcolors)
    foreground = color0
    index = randint(0, arr_len - 1) # to make sure the bg color always alternates and the colors randomize
    divider_size = 37
    padding = 10
    widgets_list = [
               widget.GroupBox(font="FiraCode Nerd Font",
                        fontsize = 16,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 6,
                        padding_x = 5,
                        borderwidth = 0,
                        disable_drag = True,
                        active = color6,
                        inactive = color8,
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = color7,
                        foreground = bgcolors[(index:=index+1) % arr_len],
                        background = color0
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = padding,
                        foreground = bgcolors[index % arr_len],
                        background = color0
                        ),
               widget.CurrentLayout(
                        foreground = bgcolors[index % arr_len],
                        background = color0
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = padding,
                        foreground = bgcolors[index % arr_len],
                        background = color0
                        ),
               widget.WindowName(
                        fontsize = 14,
                        foreground = bgcolors[(index:=index+1) % arr_len],
                        background = color0,
                        ),
               # widget.Mpd2(
               #          background = color0,
               #          foreground = color6,
               #          ),
               # widget.Net(
               #          font="Noto Sans",
               #          fontsize=12,
               #          interface="enp0s31f6",
               #          foreground = "#FFFFFF",
               #          background = bgcolors[index % arr_len],
               #          padding = 0,
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = padding,
               #          foreground = foreground,
               #          background = bgcolors[index % arr_len]
               #          ),
               widget.TextBox(text = ' ', background = color0, foreground = bgcolors[(index:=index + 1) % arr_len], margin_y = 20, padding = -1, fontsize = divider_size),
               widget.TextBox(
                        font="FiraCode Nerd Font",
                        text=" ﯱ",
                        foreground = foreground,
                        background = bgcolors[index % arr_len],
                        padding = 0,
                        fontsize=18
                        ),
               widget.NetGraph(
                        font="Noto Sans",
                        fontsize=12,
                        bandwidth="down",
                        interface="auto",
                        fill_color = color0,
                        foreground = foreground,
                        background = bgcolors[index % arr_len],
                        graph_color = color0,
                        border_color = color0,
                        padding = 0,
                        border_width = 0,
                        line_width = 1,
                        samples = 20,
                        ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = padding,
#                        foreground = foreground,
                        # background = bgcolors[index % arr_len]
               #          ),
               # # do not activate in Virtualbox - will break qtile
               # widget.ThermalSensor(
#                        foreground = foreground,
               #          foreground_alert = color6,
                        # background = bgcolors[index % arr_len]
               #          metric = True,
               #          padding = 3,
               #          threshold = 80
               #          ),
               # # battery option 1  ArcoLinux Horizontal icons do not forget to import arcobattery at the top
               # widget.Sep(
               #          linewidth = 1,
               #          padding = padding,
#                        foreground = foreground,
                        # background = bgcolors[index % arr_len]
               #          ),
               # arcobattery.BatteryIcon(
               #          padding=0,
               #          scale=0.7,
               #          y_poss=2,
               #          theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
               #          update_interval = 5,
                        # background = bgcolors[index % arr_len]
               #          ),
               # # battery option 2  from Qtile
               # widget.Sep(
               #          linewidth = 1,
               #          padding = padding,
               #          foreground = foreground,
               #          background = bgcolors[index % arr_len]
               #          ),
               widget.TextBox(text = ' ', background = bgcolors[index % arr_len], foreground = bgcolors[(index:=index + 1) % arr_len], margin_y = 20, padding = -1, fontsize = divider_size),
               # widget.Battery(
               #          font="Noto Sans",
               #          update_interval = 10,
               #          fontsize = 12,
                        # foreground = foreground,
                        # background = bgcolors[index % arr_len]
	             #          ),
               widget.TextBox(
                        font="FiraCode Nerd Font",
                        text="  ",
                        foreground = foreground,
                        background = bgcolors[index % arr_len],
                        padding = 0,
                        fontsize=16
                        ),
               widget.CPUGraph(
                        border_color = color0,
                        fill_color = color0,
                        graph_color = color0,
                        background = bgcolors[index % arr_len],
                        border_width = 0,
                        line_width = 1,
                        core = "all",
                        samples = 20,
                        type = "box"
                        ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = padding,
               #          foreground = foreground,
               #          background = bgcolors[index % arr_len]
               #          ),
               widget.TextBox(text = ' ', background = bgcolors[index % arr_len], foreground = bgcolors[(index:=index + 1) % arr_len], margin_y = 20, padding = -1, fontsize = divider_size),
               widget.TextBox(
                        font="FiraCode Nerd Font",
                        text="  ",
                        foreground = foreground,
                        background = bgcolors[index % arr_len],
                        padding = 0,
                        fontsize=16
                        ),
               widget.Memory(
                        font="Noto Sans",
                        format = '{MemUsed}M/{MemTotal}M',
                        update_interval = 1,
                        fontsize = 12,
                        foreground = foreground,
                        background = bgcolors[index % arr_len]
                       ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = padding,
               #          foreground = foreground,
               #          background = bgcolors[index % arr_len]
               #          ),
               widget.TextBox(text = ' ', background = bgcolors[index % arr_len], foreground = bgcolors[(index:=index + 1) % arr_len], margin_y = 20, padding = -1, fontsize = divider_size),
               widget.TextBox(
                        font="FiraCode Nerd Font",
                        text="  ",
                        foreground = foreground,
                        background = bgcolors[index % arr_len],
                        padding = 0,
                        fontsize=16
                        ),
               widget.Clock(
                        foreground = foreground,
                        background = bgcolors[index % arr_len],
                        fontsize = 14,
                        format="%Y-%m-%d %H:%M"
                        ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = padding,
               #          foreground = foreground,
               #          background = bgcolors[index % arr_len]
               #          ),
               widget.TextBox(text = ' ', background = bgcolors[index % arr_len], foreground = color0, margin_y = 20, padding = -1, fontsize = divider_size),
               widget.Systray(
                        background = color0,
                        icon_size=20,
                        margin = 5,
                        padding = 4
                        ),
               widget.Spacer(length=10, background = color0)
              ]
    return widgets_list

widgets_list = init_widgets_list()

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()

isCol = 1

@hook.subscribe.layout_change
def set_isCol(layout, group):
    if (layout == layout.Column):
        isCol = 1
    else:
        isCol = 0

def init_screens():
    # return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=0.95)),
    #         Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=0.95))]
    return [Screen(left=bar.Gap(col_mar*isCol), right=bar.Gap(col_mar*isCol), bottom=bar.Gap(col_mar*isCol), top=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=0.95, margin=col_mar)),
            Screen(left=bar.Gap(col_mar*isCol), right=bar.Gap(col_mar*isCol), bottom=bar.Gap(col_mar*isCol), top=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=0.95, margin=col_mar))]
screens = init_screens()

# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

############################################################
## => FUNCTIONS
############################################################
main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

#@hook.subscribe.startup
#def start_always():
    # Set the cursor to something sane in X
    # subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'Arcolinux-welcome-app.py'},
    {'wmclass': 'Arcolinux-tweak-tool.py'},
    {'wmclass': 'Arcolinux-calamares-tool.py'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wmclass': 'Galculator'},
    {'wmclass': 'arcolinux-logout'},
    {'wmclass': 'xfce4-terminal'},
    {'wname': 'branchdialog'},
    {'wname': 'Open File'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},

],  fullscreen_border_width = 0, border_width = border_width)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
