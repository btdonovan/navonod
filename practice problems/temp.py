#! /usr/bin/python2
def to_f(c):
    f = (9.0/5.0) * c + 32
    print '%s C = %.1f F' % (c, f) 
def to_c(f):
    c = (5.0/9.0) * (f - 32)
    print '%s F = %.1f C' % (f, c)

print 'Temperature converter'

degrees = float(raw_input('Enter a temperature: '))
scale = raw_input('Convert to (F)ahrenheit or (C)elsius? ')

if scale.lower() == 'f' or scale.lower() == 'fahrenheit':
    to_f(degrees)
elif scale.lower() == 'c' or scale.lower() == 'celsius':
    to_c(degrees)

