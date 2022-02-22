let integers n=
    let m=Array.make_matrix 1 n 0 in
    for i=1 to n do
        m.(0).(i-1)<-i
    done;
    (m)
    ;;
