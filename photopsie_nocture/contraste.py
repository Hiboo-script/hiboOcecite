import simucecite as sc

size = (552,552)

imin = sc.Image.open("images/calque_simulation_3.png")
pixin = imin.load()

imout = sc.Image.new('RGB', size)
pixout = imout.load()

delta = 5.
moyenne = sc.lumi_moyenne_MC(pixin,size)

sc.contraste_l(pixin,pixout,size,moyenne,delta)

imout.save("images/calque_simulation_c_3.png")
