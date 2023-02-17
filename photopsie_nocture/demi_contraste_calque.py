import simucecite as sc

size = (512,512)

imin = sc.Image.open("calque_moy_4.png")
pixin = imin.load()

imout = sc.Image.new('RGB', size)
pixout = imout.load()

delta = -15.
moyenne = sc.lumi_moyenne_MC(pixin,size)

sc.demi_contraste_m_l(pixin,pixout,size,moyenne-2.,delta)

imout.save("demi_contraste_calque_4.png")
