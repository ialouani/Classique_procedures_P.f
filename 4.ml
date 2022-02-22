let rec puissance b n=
    if n==0 then 1.
    else b *. puissance b (n-1);;
print_float(puissance 3.3 2);;
print_string "\n";;
