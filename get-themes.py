import json
import requests
import os
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

themes = json.loads(requests.get("https://raw.githubusercontent.com/Gogh-Co/Gogh/master/data/themes.json").text)
for theme in themes:
    black = theme['color_01']
    red = theme['color_02']
    green = theme['color_03']
    yellow = theme['color_04']
    blue = theme['color_05']
    magenta = theme['color_06']
    cyan = theme['color_07']
    white = theme['color_08']
    brightBlack = theme['color_09']
    brightRed = theme['color_10']
    brightGreen = theme['color_11']
    brightYellow = theme['color_12']
    brightBlue = theme['color_13']
    brightMagenta = theme['color_14']
    brightCyan = theme['color_15']
    brightWhite = theme['color_16']   
    background = theme['background']
    foreground = theme['foreground']
    cursor = theme['cursor']
    name = f'alacritty-themes/{remove_accents(theme['name']).lower().replace(' ', '-')}.toml'
    content = f"""[colors]
cursor = {{cursor = "{cursor}" }}
[colors.primary]
foreground = "{foreground}"
background = "{background}"
[colors.normal]
black = "{black}"
red = "{red}"
green = "{green}"
yellow = "{yellow}"
blue = "{blue}"
magenta = "{magenta}"
cyan = "{cyan}"
white = "{white}"
[colors.bright]
black = "{brightBlack}"
red = "{brightRed}"
green = "{brightGreen}"
yellow = "{brightYellow}"
blue = "{brightBlue}"
magenta = "{brightMagenta}"
cyan = "{brightCyan}"
white = "{brightWhite}"
    """
    with open(name, 'w', encoding='utf-8') as file:
        file.write(content)