import simucecite as sc

size = (256,256)

imin = sc.Image.open("test_claque_photopsie.png")
pixin = imin.load()

imout = sc.Image.new('RGB', size)
pixout = imout.load()

delta = -15.
moyenne = sc.lumi_moyenne_MC(pixin,size)

sc.demi_contraste_m_l(pixin,pixout,size,moyenne-2.,delta)

imout.save("demi_contraste_calque_test.png")
