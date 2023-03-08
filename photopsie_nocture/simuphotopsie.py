import simucecite as sc

size = (552,552)

im_pochoir = sc.Image.open("images/pochoir_peint_7.png")
pochoir = im_pochoir.load()

im_calque = sc.Image.open("images/calque_simulation_moy_3.png")
calque = im_calque.load()

imout = sc.Image.new('RGB',size)
pixout = imout.load()

sc.simuphotopsie(pochoir,calque,pixout,size)

imout.save("images/simuphotopsie_proto1_3.png")
