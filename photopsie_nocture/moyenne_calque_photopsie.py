import simucecite as sc

size = (256,256)

imin = sc.Image.open("simuphotopsie_1.png")
pixin = imin.load()

imout = sc.Image.new('RGB',size)
pixout = imout.load()

rayon = 3

sc.moyenne_l(pixin,pixout,size,rayon)

imout.save("simuphotopsie_moy_1.png")
