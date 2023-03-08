import simucecite as sc

size = (512,512)

imin = sc.Image.open("images/calque_simulation_2_dc1.png")
pixin = imin.load()

imout = sc.Image.new('RGB', size)
pixout = imout.load()

delta = 0.3
moyenne = sc.lumi_moyenne_MC(pixin,size)

sc.demi_contraste_m_l(pixin,pixout,size,moyenne,delta)

imout.save("images/calque_simulation_2_dc2.png")
