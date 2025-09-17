import re
#Todo Define url parameter for an image.

# Example format: protocol subdomain domain path filename queryparams
# Example URLs
# https://images.pexels.com/photos/29828230/pexels-photo-29828230.jpeg
# https://cdn.images.example.co.uk/photos/uploads/2025/09/17/nature/mountain_view_high_resolution.jpg?width=1920&height=1080&quality=90&format=webp
# https://images-ext-1.discordapp.net/external/gzHj3cJc5L9ZhRpZJe6xLGEiqrmHDrshrOdcYBMDxBI/%3F1756325510/https/cdnb.artstation.com/p/assets/images/images/091/275/127/large/marcin-rubinkowski-dark-lab-rubinkowski-4.jpg?format=webp

# URL Format: protocol://subdomain.domain/path/path/filename/query

def image_url_validator(image_url):
    url_parts = re.match(
        r"^(?P<protocol>https|http)://(?P<domain>[A-Za-z0-9.-]+?)/(?P<path_to_file>.+?)/(?P<filename>[\w\-]+?)(?P<format>png|jpg|jpeg|gif|svg|webp)(?P<query>[\w\s\?\=]*)?",
        image_url)





    return url_parts
