import simucecite as sc

size = (384,512)

imin = sc.Image.open("skoda512.png")
pixin = imin.load()

imout = sc.Image.new('RGB', size)
pixout = imout.load()

delta = 5.
moyenne = sc.lumi_moyenne_MC(pixin,size)

sc.contraste_l(pixin,pixout,size,moyenne,delta)

imout.save("images/skoda_contraste.png")
