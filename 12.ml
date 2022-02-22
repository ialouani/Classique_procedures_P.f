let add m1 m2=
    let x=Array.length m1 and y=Array.length m1.(0) in
    if x <> Array.length m2 || y <> Array.length m2.(0) then failwith "warning!"
    else
      let res_matrix = Array.make_matrix x y 0. in
      for i=0 to x-1 do
          for j=0 to y-1 do
              res_matrix.(i).(j)<-m1.(i).(j) +. m2.(i).(j)
          done
      done;
      res_matrix
      ;;
