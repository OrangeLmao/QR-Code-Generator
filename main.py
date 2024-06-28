import qrcode
import qrcode.image.svg

terminate = False
factory = qrcode.image.svg.SvgPathImage
while terminate == False:
  #get webadress from user
  adress = input("enter webadress for qrcode\n")
  svg_img = qrcode.make(adress, image_factory=factory)
  svg_img.save("myqr.svg")
  #terminate?
  terminate = input("do you want to terminate? (y/n)\n")
  if terminate == "y":
    terminate = True
