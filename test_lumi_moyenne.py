import simucecite as sc

im = sc.Image.open("photo_test.png")
pix = im.load()

moy_t = sc.lumi_moyenne_t(pix,(256,256))
moy_MC = sc.lumi_moyenne_MC(pix,(256,256))

print(moy_t)
print(moy_MC)
