from mysite.models import Product
p = Product.objects.create(name=' HTC Magic', price=100, qty=0)
p = Product.objects.create(name=' SONY Xperia Z3', price= 15000, qty=1)
p = Product.objects.create(name=' Samsung DUOS', price=800, qty=2)
p = Product.objects.create(name=' Nokia Xpress 5800', price=500, qty=1)
p = Product.objects.create(name=' Infocus M370', price=1500, qty=2)
p.save()

allprod = Product.objects.all()
for p in allprod:
    print(p.name, ', ', p.price, ', ', p.qty)

#exit()