import simucecite as sc

size = (512,512)

imin = sc.Image.open("simuphotopsie_7.png")
pixin = imin.load()

imout = sc.Image.new('RGB',size)
pixout = imout.load()

rayon = 4

sc.moyenne_l(pixin,pixout,size,rayon)

imout.save("simuphotopsie_moy_7.png")
