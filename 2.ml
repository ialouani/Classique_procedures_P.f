let rec facto n =
    if n==0 then 1
    else n*facto(n-1);;
print_int(facto(5));
print_string "\n";;
let rec facto_acc n k =
    if n==0 then k
    else facto_acc (n-1) (n*k);;
print_int(facto_acc (5) (3));;
print_string "\n";;
