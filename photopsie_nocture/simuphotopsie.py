import simucecite as sc

size = (512,512)

im_pochoir = sc.Image.open("pochoir_peint_2.png")
pochoir = im_pochoir.load()

im_calque = sc.Image.open("calque_final_4.png")
calque = im_calque.load()

imout = sc.Image.new('RGB',size)
pixout = imout.load()

sc.simuphotopsie(pochoir,calque,pixout,size)

imout.save("simuphotopsie_7.png")
