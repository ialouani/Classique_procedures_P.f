let print_matrix n=
    let m=Array.make_matrix n n 0.0 in  
    for k=0 to n-1 do
        m.(k).(k)<-1.0
    done;
    for i=0 to n-1 do
        for j=0 to n-1 do 
            print_float(m.(i).(j))
    done;
    print_string "\n";
    done;
    ;;
