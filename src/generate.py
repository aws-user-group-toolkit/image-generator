import textwrap
import urllib.request
import io
import os
import time

from PIL import Image, ImageDraw, ImageFont

TITLE = os.getenv("TITLE", "MY MEETUP TITLE")
DATE = os.getenv("DATE", "1 January 1970")
LOCATION = os.getenv("LOCATION", "Vienna, Austria")
PHOTO = os.getenv("PHOTO", "https://content-files.shure.com/BlogPosts/basic-conference-room-design-a-webinar/images/basic-conference-room-design-a-webinar_header.png")
LOGO = os.getenv("LOGO", "https://lavca.org/app/uploads/2019/10/aws-logo-square.png")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "/output")

# Open the base image
base_image = Image.open("assets/images/meetup-header.png").convert("RGBA")

# Open the photo image and resize it
if PHOTO.startswith("http"):
    req = urllib.request.Request(PHOTO, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as url:
        f = io.BytesIO(url.read())
        photo_image = Image.open(f).convert("L")
else:
    photo_image = Image.open(PHOTO).convert("L")

width, height = photo_image.size
aspect_ratio = width / height
new_height = 2400
new_width = int(new_height * aspect_ratio)
photo_image = photo_image.resize((new_width, new_height))

# Center crop the photo image to a width of 2900 pixels
crop_width = 2900
crop_height = 2400
left = (new_width - crop_width) // 2
top = (new_height - crop_height) // 2
right = left + crop_width
bottom = top + crop_height
photo_image = photo_image.crop((left, top, right, bottom))

# Convert the gray image to RGBA mode
photo_image = photo_image.convert("RGBA")

# Set the alpha channel of the gray image to 30%
photo_image.putalpha(77)

# Paste the combined image onto the base image
base_image.paste(photo_image, (base_image.width - photo_image.width, 0), photo_image)

# Open the overlay image and paste it onto the base image
overlay_image = Image.open("assets/images/meetup-header-overlay.png").convert("RGBA")
base_image.paste(overlay_image, (0, 0), overlay_image)

# Create a new image with the same size as the base image
text_image = Image.new("RGBA", base_image.size, (255, 255, 255, 0))

# Draw the title text onto the text image
title_font = ImageFont.truetype("assets/fonts/Ember/AmazonEmber_He.ttf", 130)
title_text_size = title_font.getlength(TITLE)
max_title_width = base_image.width // 3
if title_text_size > max_title_width:
    lines = textwrap.wrap(TITLE, width=20, break_long_words=False)
    title_text = "\n".join(lines)
    title_text_size = max(title_font.getlength(line) for line in lines)
else:
    title_text = TITLE
title_text_position = (base_image.width // 4 - title_text_size // 2, 1150)
title_draw = ImageDraw.Draw(text_image)
title_draw.text(title_text_position, title_text, fill="white", font=title_font, align="center")

# Draw the date text onto the text image
date_font = ImageFont.truetype("assets/fonts/Ember/AmazonEmber_He.ttf", 130)
date_text_size = date_font.getlength(DATE)
date_text_position = (base_image.width * 3 // 4 - date_text_size // 2, 1200)
date_draw = ImageDraw.Draw(text_image)
date_draw.text(date_text_position, DATE, fill="white", font=date_font)

# Draw the location text onto the text image
location_font = ImageFont.truetype("assets/fonts/Ember/AmazonEmber_Rg.ttf", 90)
location_text_size = location_font.getlength(f"@{LOCATION}")
location_text_position = (base_image.width * 3 // 4 - location_text_size // 2, 1450)
location_draw = ImageDraw.Draw(text_image)
location_draw.text(location_text_position, f"@{LOCATION}", fill="white", font=location_font)

# Paste the text image onto the base image
base_image.paste(text_image, (0, 0), text_image)

# Open the logo image and resize it
if LOGO.startswith("http"):
    req = urllib.request.Request(LOGO, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as url:
        f = io.BytesIO(url.read())
        logo_image = Image.open(f).convert("RGBA")
else:
    logo_image = Image.open(LOGO).convert("RGBA")

logo_height = 300
logo_width = int(logo_image.width * logo_height / logo_image.height)
logo_image = logo_image.resize((logo_width, logo_height))

# Paste the logo image onto the base image
base_image.paste(logo_image, (630, base_image.height - logo_image.height - 100), logo_image)

# Save the final image
ts = time.time()
base_image.save(f"{OUTPUT_DIR}/meetup-header-{ts}.png")