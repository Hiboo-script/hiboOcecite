import simucecite as sc

size = (552,552)

imin = sc.Image.open("images/simuphotopsie_proto1_3.png")
pixin = imin.load()

imout = sc.Image.new('RGB',size)
pixout = imout.load()

delta = 0.7

sc.luminosite_l(pixin,pixout,size,delta)

imout.save("images/simuphotopsie_proto2_3.png")
