import simucecite as sc

size = (256,256)

im = sc.Image.open("demi_contraste_calque_test.png")
pixin = im.load()

imout = sc.Image.new('RGB', size)
pixout = imout.load()

sc.moyenne_l(pixin,pixout,size,10)

imout.save("calque.png")
