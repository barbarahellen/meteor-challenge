from PIL import Image


def count_pixels(image):
    # variables
    stars, meteors = 0, 0
    meteors_on_water = 0

    img = Image.open(image)
    rgb_img = img.convert('RGB')
    width, height = img.size

    for y in range(height):      # two nested for loops traverse each pixel in the image using (x, y) coordinates.
        for x in range(width):

            r, g, b = rgb_img.getpixel((x, y))

            if r == 255 and g == 255 and b == 255:  # stars - white (255, 255, 255)
                stars += 1
            elif r == 255 and g == 0 and b == 0:    # meteors - red (255, 0, 0)
                meteors += 1

                # for each meteor found, scroll the height below it to the end of the image. If you find a blue pixel, it increases the meteor counter on the water
                for y_down in range(y, height):
                    r_down, g_down, b_down = rgb_img.getpixel((x, y_down))
                    if r_down == 0 and g_down == 0 and b_down == 255:      # water - blue (0, 0, 255)
                        meteors_on_water += 1
                        break

    print('Number of stars = ', stars)
    print('Number of meteors = ', meteors)
    print('Number of meteors falling on the water = ', meteors_on_water)


count_pixels('img/meteor_challenge_01.png')
