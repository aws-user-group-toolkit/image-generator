import image_generator.header_image_generator as HeaderImageGenerator
import os

TITLE = os.getenv("TITLE", "MY MEETUP TITLE")
DATE = os.getenv("DATE", "1 January 1970")
LOCATION = os.getenv("LOCATION", "Vienna, Austria")
PHOTO = os.getenv("PHOTO", "https://content-files.shure.com/BlogPosts/basic-conference-room-design-a-webinar/images/basic-conference-room-design-a-webinar_header.png")
PHOTO_OPACITY = int(os.getenv("PHOTO_OPACITY", 30))
LOGO = os.getenv("LOGO", "https://lavca.org/app/uploads/2019/10/aws-logo-square.png")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./output")

HeaderImageGenerator.generate(TITLE, DATE, LOCATION, PHOTO, PHOTO_OPACITY, LOGO, OUTPUT_DIR)