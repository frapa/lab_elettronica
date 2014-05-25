from uncertainties import ufloat, unumpy

va_diff1 = unumpy.uarray((310, 220, 410), (5, 5, 5))
vout_diff1 = unumpy.uarray((9.2, 6.6, 11.7), (0.05, 0.05, 0.05))
G_diff = vout_diff1 * 1000 / va_diff1

print G_diff
G_diff = sum(G_diff) / 3
print G_diff

va_cm1 = unumpy.uarray((310, 220, 410), (5, 5, 5))
vout_cm1 = unumpy.uarray((-180, -130, -230), (5, 5, 5))
G_cm = vout_cm1 / va_cm1

print G_cm
G_cm = sum(G_cm) / 3
print G_cm

cmrr =  - G_diff / G_cm
print cmrr

re = ufloat(10000, 500) / cmrr - ufloat(120, 6)
print re, "\n\n"

#########################################################

va_diff1 = unumpy.uarray((300, 200, 400), (5, 5, 5))
vout_diff1 = unumpy.uarray((9.6, 6.4, 12.6), (0.05, 0.05, 0.05))
G_diff = vout_diff1 * 1000 / va_diff1

print G_diff
G_diff = sum(G_diff) / 3
print G_diff

va_cm1 = unumpy.uarray((300, 200, 400), (5, 5, 5))
vout_cm1 = unumpy.uarray((-10, -10, -10), (5, 5, 5))
G_cm = vout_cm1 / va_cm1

print G_cm
G_cm = sum(G_cm) / 3
print G_cm

cmrr =  - G_diff / G_cm
print cmrr

re = ufloat(10000, 500) / cmrr - ufloat(120, 6)
print re
