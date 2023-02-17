import simucecite as sc

size = (256,256)

im_pochoir = sc.Image.open("pochoir.png")
pochoir = im_pochoir.load()

im_calque = sc.Image.open("calque.png")
calque = im_calque.load()

imout = sc.Image.new('RGB',size)
pixout = imout.load()

sc.simuphotopsie(pochoir,calque,pixout,size)

imout.save("simuphotopsie_1.png")
