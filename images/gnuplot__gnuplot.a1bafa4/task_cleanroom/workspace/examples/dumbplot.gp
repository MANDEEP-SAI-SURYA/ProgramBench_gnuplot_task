set term dumb size 60,18
set title 'demo'
plot [-3:3] sin(x) title 'sin', 0.3*x with points title 'line'
