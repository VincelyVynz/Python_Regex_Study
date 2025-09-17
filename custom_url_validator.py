import re
#TODO image url
# bg_color, fg_color, text,height, width,border, orientation, font
# font = (font name, size, style)
# font = ('Arial', 24, 'italic') normal, bold
# #000000 black #FFFFFF white
def custom_image(url):
    parts= re.match(r"^length=(?P<length>\d{2,4})/width=(?P<width>\d{2,4})/bg_color="
                r"(?P<bg_color>#[A-Z0-9]{6})/fg_color=(?P<fg_color>#[A-Z0-9]{6})/"
                r"border=(?P<border>y|n)/orientation=(?P<orientation>v|h)/"
                r"font=(?P<font>\([A-Za-z\s]+,[\d]{1,2},[A-Za-z\s]+\))/(?:header=(?P<header>.*?)?/)?text=(?P<text>.*)$",
                url)

    if parts:
        print(parts.groupdict())
    else:
        print(f"Invalid url")
custom_image("length=90/width=45/bg_color=#FFFFFF/fg_color=#000000/border=y/orientation=v/font=(Arial,24,italic)/text=message")


