a = float(input())
b = float(input())
c = float(input())
d=b*b-4*a*c
x1=(-b-d**(0.5*(d>=0))/(2*a))
x2=(-b+d**(0.5*(d>=0))/(2*a))
a1=('2 корня равны '+str(x1)+', ' + str(x2)) * (d>0)
a2=('Всего 1 корень '+str(x1)) * (d==0)
a3=('Корней нет') * (d<0)
print(a1+a2+a3)
print(d)
