# expressions, formatting and a table
print 7/2, 7.0/2, 2**10, sprintf("%.3f", pi), gprintf("%.2t*10^%T", 12345)
f(x) = x**2 - 2
set samples 5
set table
plot [0:2] f(x)
