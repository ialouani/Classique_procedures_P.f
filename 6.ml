let compare_lettres a b=
    if a==b then true
    else if int_of_char(a) < int_of_char(b) then true
    else false;;
let c=compare_lettres 'a' 'b';;
let d=compare_lettres 'a' 'a';;
let e=compare_lettres 'b' 'a';;
print_string(string_of_bool(c));;
print_string "\n";;
print_string(string_of_bool(d));;
print_string "\n";;
print_string(string_of_bool(e));;
print_string "\n";;
