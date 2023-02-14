# importation
import simucecite as sc


# programme
im = sc.Image.open('photo_test.png')
pix = im.load()

im_test = sc.Image.new('RGB',(256,256))
pix_test = im_test.load()

r = 4

delta = 0.3

alpha = -0.9
beta = 0.4
gamma = 0.7 

sc.moyenne_l(pix,pix_test,(256,256),r)

im_test.save('photo_test_moyenne_nsc.png')
