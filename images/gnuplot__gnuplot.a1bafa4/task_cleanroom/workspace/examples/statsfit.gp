$d << EOD
1 2.1
2 3.9
3 6.2
4 7.8
EOD
stats $d
set fit nolog
fit a*x + b $d via a, b
