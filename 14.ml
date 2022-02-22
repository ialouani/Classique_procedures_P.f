let mult_matrix m1 m2=
    let x=Array.length m1.(0) and y=Array.length m2 in
    if x<>y then failwith "warning!"
    else
      let x = Array.length m1 and y = Array.length m2.(0) in
      let res_matrix=Array.make_matrix x y 0. in
      for i=0 to (Array.length m1) -1 do
          for j=0 to (Array.length m2.(0)) -1 do
              for k=0 to (Array.length m1.(0))-1 do
                  res_matrix.(i).(j)<-res_matrix.(i).(j) +. m1.(i).(k)*.m2.(k).(j)
              done
          done
      done;
      res_matrix
      ;;
