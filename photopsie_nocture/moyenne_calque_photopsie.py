import simucecite as sc

size = (552,552)

imin = sc.Image.open("images/simuphotopsie_proto2_3.png")
pixin = imin.load()

imout = sc.Image.new('RGB',size)
pixout = imout.load()

rayon = 5

sc.moyenne_l(pixin,pixout,size,rayon)

imout.save("images/simuphotopsie_proto3_3.png")
