let mult_matrix_const k m=
    let x=Array.length m and y=Array.length m.(0) in
    for i=0 to x-1 do
        for j=0 to y-1 do
            m.(i).(j)<-k*.(m.(i).(j))
        done
    done;
    m
    ;;
  
