import simucecite as sc

size = (256,256)

im = sc.Image.open("disque_4.png")
pixin = im.load()

imout = sc.Image.new('RGB', size)
pixout = imout.load()

sc.moyenne_l(pixin,pixout,size,19)

imout.save("pochoir.png")
