import simucecite as sc

size = (256,256)

imin = sc.Image.open("test_claque_photopsie.png")
pixin = imin.load()

imout = sc.Image.new('RGB',size)
pixout = imout.load()

rayon = 5

sc.moyenne_l(pixin,pixout,size,rayon)

imout.save("test_final_calque.png")
