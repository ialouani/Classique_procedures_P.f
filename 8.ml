let identity n=
    let m=Array.make_matrix n n 0.0 in
        for i=0 to n-1 do
            m.(i).(i)<-1.0
        done;
        (m)
        ;;
