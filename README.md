# canne
Canne de combat competition scripts.

Easy generation of competitors and pools. Specify two inputs command line arguments for script.
A file with each line of form
<competitor name> <m|f>

Number of pools.

Sample file (sample.txt)
A B m
C D f
M C m
B M f
T C m

#python generate.py sample.txt 1
Pool 1
1. A B : C D
2. M C : B M
3. A B : T C
4. C D : M C
5. B M : T C
6. A B : M C
7. C D : B M
8. M C : T C
9. A B : B M
10. C D : T C

#python generate.py sample.txt 2
Pool 1                                                                                                   │
1. M C : C D                                                                                             │
2. M C : T C                                                                                             │
3. C D : T C                                                                                             │
Pool 2                                                                                                   │
1. B M : A B
