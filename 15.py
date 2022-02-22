def f(T):#T trie compose uniquement de 0 et de 1.
    if len(T)==1:
       if T[0]==0:
          return 1
       return 0
    elif len(T)==2:
       if T[0]==1:
          return 0
       else:
          if T[1]==0:
             return 2
          return 1
    else:
       a=len(T)//2
       L1=T[0:a]
       L2=T[a:len(T)]
       if L2[0]==1:
          return f(L1)
       return len(L1)+f(L2)
#print(f([0,0,0,0,0,0,1,1,1,1,1]))
#complexite par la methode divide and conquer: O(log(n)).
#(recursivite formules).
#complexite spatiale: (pire de cas)
#apres analyse judicieuse ; on trouve: O(log(n)).
#partie2 de lexo15:
#suite::

def f2_v2(T,x):#T trie compose de len(T) entiers.
    if len(T)==1:
       if T[0]==x:
          return 1
       return 0
    elif len(T)==2:
         if T[0]==x:
            if T[1]==x:
               return 2
            return 1
         else:
            if T[1]==x:
               return 1
            return 0
    else: 
       a=len(T)//2
       L1=T[0:a]
       L2=T[a:len(T)]
       if L2[0]>x:
          return f2_v2(L1,x)
       elif L2[0]<x:
          return f2_v2(L2,x)
       else: #cad:(L2[0]==x)=true()()()
          return f2_v2(L1,x)+1+f2_v2(L2[1:],x) #f2(L1,x)+f2(L2,x)->O(n)...
#print(f2_v2([1,2,3,3,3,4,8,10],3))
#print(f2_v2([1,2,3,3,3,4,8,10],5))
#complexite temporelle comme on voulait: O(n*log(n)).(relations seance4)
#(etude du pier des cas pour les deux bien sur.)
#suite: (derniere question) pas encore fini l'avant derniere !!!!!
#::
#f2V2+derniere fct/:

N=[0,2,2,3,4,4,4,4,4,5,6,7]
#print(N.count(4))


#debut
def f2(T,x):
    if len(T)==1:
       if T[0]==x:
          return 1
       return 0
    if len(T)==2:
       if T[0]==x and T[1]==x:
          return 2
       elif T[0]==x and T[1]!=x:
          return 1
       elif T[0]!=x and T[1]!=x:
          return 0
       elif T[0]!=x and T[1]==x:
          return 1
    else:
       m=len(T)//2
       T1=T[0:m]
       T2=T[m:]
       return T1.count(x)+f2(T2,x) #O(n)si on procede par boucle classique
#mais cest de la triche quand meme..()
#c(s)=O(log(n)).
#donc:c(s)=c(t)=O(log(n)). ..()()()
#print(f2([1,2,3,3,3,4,8,10],3))
#print(f2([1,2,3,3,3,4,8,10],5))
#fin

#derniere et toute derniere fct::.
def f3(T):#complexite=??hh!
    if len(T)==1:
       return T
    h=0
    while (T[h]==T[0]):
          h+=1
    j=h
    return [T[0]]+f3(T[j:])
#print(f3([0,1,2,3,3,4,4,5]))
def f4_1(T):
    if len(T)==1:
       return [T[0]]
    h=0
    a=f2(T,T[0])
    #rappel: a est le nombre d'occurences de T[0] dans T.
    return [T[0]]+f4_1(T[a:])
#en utilisant f2: on a : CT=O(K.log(n)) avec K=|F|=|U|.
def f4_2(T):
    if len(T)==1:
       return [1]
    h=0
    a=f2(T,T[0])
    return [a]+f4_2(T[a:])
#CT=O(K.log(n)) de meme cest evident!
#print(f4_1([0,1,2,3,3,4,4,5]))
#print(f4_2([0,1,2,3,3,4,4,5]))
#des plus pour finir la seance 5..
#pas de plus; passons plutot a : dynamic programming and greddy method.

if __name__!='main':
    print(f([0,0,0,0,0,0,1,1,1,1,1]))
    print(f2_v2([1,2,3,3,3,4,8,10],3))
    print(f2_v2([1,2,3,3,3,4,8,10],5))
    print(N.count(4))
    print(f2([1,2,3,3,3,4,8,10],3))
    print(f2([1,2,3,3,3,4,8,10],5))
    print(f3([0,1,2,3,3,4,4,5]))
    print(f4_1([0,1,2,3,3,4,4,5]))
    print(f4_2([0,1,2,3,3,4,4,5]))
    
