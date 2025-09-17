import re
#Todo Define url parameter for an image.

# Example format: protocol subdomain domain path filename queryparams
# Example URLs
# https://images.pexels.com/photos/29828230/pexels-photo-29828230.jpeg
# https://cdn.images.example.co.uk/photos/uploads/2025/09/17/nature/mountain_view_high_resolution.jpg?width=1920&height=1080&quality=90&format=webp
# https://images-ext-1.discordapp.net/external/gzHj3cJc5L9ZhRpZJe6xLGEiqrmHDrshrOdcYBMDxBI/%3F1756325510/https/cdnb.artstation.com/p/assets/images/images/091/275/127/large/marcin-rubinkowski-dark-lab-rubinkowski-4.jpg?format=webp

# URL Format: protocol://subdomain.domain/path/path/filename/query

def image_url_validator(image_url):
    if re.match(
        r"(?P<protocol>https|http)://(?P<domain>[\w\.]+)/(?P<file_path>[\w/-]+?)/(?P<file_name>[\w-]+)\.(?P<fileformat>jpg|png|jpeg|gif|webp|tga|bmp|exr|hdr|tiff)(?P<query>[?\w=&_-]*)",
        image_url):
        print("Image URL Valid")

    else:
        print("Image URL Not Valid")





image_url_validator("https://cdnb.artstation.com/p/assets/images/images/078/091/459/large/vincely-scifi-door-render-6.jpg?1721165680")