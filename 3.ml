let rec gcd n m =
    if m==0 then n
    else gcd m (n mod m);;
print_int (gcd (60) (12)) ;;
print_string "\n";;
