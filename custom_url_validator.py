import re
#TODO image url
# bg_color, fg_color, text,height, width,border, orientation, font
# font = (font name, size, style)
# font = ('Arial', 24, 'italic') normal, bold
# #000000 black #FFFFFF white
def custom_image(url):
    if re.match(r"^(?P<length>length=\d{2,4})/(?P<width>width=\d{2,4})/"
                r"(?P<bg_color>bg_color=#[A-Z0-9]{6})/(?P<fg_color>fg_color=#[A-Z0-9]{6})/"
                r"(?P<border>border=y|n)/(?P<orientation>orientation=v|h)/"
                r"(?P<font>font=\([A-Za-z\s]+,[\d]{1,2},[A-Za-z\s]+\))/(?P<text>text=.*)$",
                url):
        print("Valid URL")
    else:
        print("Invalid URL")


custom_image("length=90/width=45/bg_color=#FFFFFF/fg_color=#000000/border=y/orientation=v/font=(Arial,24,italic)/text=message")


