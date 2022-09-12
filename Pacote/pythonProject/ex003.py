from math import radians, sin, cos, tan
v = int(input('Me fala o angulo que voce quer saber: '))
seno = sin(radians(v))
cosseno = cos(radians(v))
tangente = tan(radians(v))
print('O Seno de {} é {:.2f} \n O Cosseno de {} é {:.2f} \n A Tangente de {} é {:.2f}'.format(v,seno,v,cosseno,v,tangente))
