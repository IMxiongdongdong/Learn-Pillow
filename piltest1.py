from PIL import Image, ImageFilter

im_path = r'C:\Users\99770\Desktop\timg.jpg'
im = Image.open(im_path)
# width, height = im.size
# print(im.size, width, height)
# print(im.format, im.format_description)

# crop_im = im.crop((100, 100, 500, 500))
# crop_im.save(r'C:\Users\99770\Desktop\3.jpg')

# crop_im = im.crop((100, 100, 300, 300))
# im.paste(crop_im, (0, 0))
# im.show()

# width, height = im.size
# resizeim = im.resize((width, height + 500))
# resizeim.show()

# rotate_im = im.rotate(90, expand=True)
# rotate_im.show()

# filter_im = im.filter(ImageFilter.EMBOSS)
# filter_im.show()

im_filp = im.transpose(Image.FLIP_LEFT_RIGHT)
im.save('im_flip.jpg')