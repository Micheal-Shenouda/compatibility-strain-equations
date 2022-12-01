#! /bin/python3

####################################################################################
# Auther: Micheal Shenouda                                                         #
# Last modifed date: 1-Dec-2022                                                    #
# General compatibility strain equation: e ji,kl + e kl,ji - e ki,jl - e jl,ki = 0 #                                      # 
# This code written to reduce the 81 equations of compatibility strain in 3D       #
####################################################################################

def main():
    augmented = create_and_filter_zero_equations()
    augmented = filter_repeated_equations(augmented)
    output(augmented)
    return 


# Create equations, Then filter Trivial equations, Where all terms will be canceled
def create_and_filter_zero_equations():

    augmented = []  # All terms
    for i in range(1 ,4):
        for j in range(1, 4):
            for k in range(1, 4):
                for l in range(1, 4):  
                    f1 = False  # Flag
                    f2 = False  # Flag

                    # Due to symmetrical property, t1 = swap(t1)
                    t1 = swap([j, i, k, l]) # First term in equation
                    t2 = swap([k, l, j, i]) # Second term in equation
                    t3 = swap([k, i, j, l]) # Third term in equation
                    t4 = swap([j, l, k, i]) # Fourth term in equation


                    # Filter 
                    for e in range(4):
                        for p in range(4):
                            if t1[e] == t3[p] or t1[e] == t4[p]:
                                f1 = True
                                break

                    # Filter 
                    for e in range(4):
                        for p in range(4):
                            if t2[e] == t3[p] or t2[e] == t4[p]:
                                f2 = True
                                break

                    if (f1 == False or f2 == False):
                        tmp = []
                        tmp.append(t1[1])
                        tmp.append(t2[1])
                        tmp.append(t3[1])
                        tmp.append(t4[1])
                        augmented.append(tmp)
    return augmented

#########################################
#   Now the output will be like that    #
#   Let's filter it more                #
#                                       #  
# e11,22 + e22,11 - e12,21 - e21,12 = 0 #
# e11,32 + e32,11 - e12,31 - e31,12 = 0 #
# e11,23 + e23,11 - e13,21 - e21,13 = 0 #
# e11,33 + e33,11 - e13,31 - e31,13 = 0 #
# e12,21 + e21,12 - e11,22 - e22,11 = 0 #
# e12,31 + e31,12 - e11,32 - e32,11 = 0 #
# e12,23 + e23,12 - e13,22 - e22,13 = 0 #
# e12,33 + e33,12 - e13,32 - e32,13 = 0 #
# e13,21 + e21,13 - e11,23 - e23,11 = 0 #
# e13,31 + e31,13 - e11,33 - e33,11 = 0 #
# e13,22 + e22,13 - e12,23 - e23,12 = 0 #
# e13,32 + e32,13 - e12,33 - e33,12 = 0 #
# e21,12 + e12,21 - e22,11 - e11,22 = 0 #
# e21,32 + e32,21 - e22,31 - e31,22 = 0 #
# e21,13 + e13,21 - e23,11 - e11,23 = 0 #
# e21,33 + e33,21 - e23,31 - e31,23 = 0 #
# e22,11 + e11,22 - e21,12 - e12,21 = 0 #
# e22,31 + e31,22 - e21,32 - e32,21 = 0 #
# e22,13 + e13,22 - e23,12 - e12,23 = 0 #
# e22,33 + e33,22 - e23,32 - e32,23 = 0 #
# e23,11 + e11,23 - e21,13 - e13,21 = 0 #
# e23,31 + e31,23 - e21,33 - e33,21 = 0 #
# e23,12 + e12,23 - e22,13 - e13,22 = 0 #
# e23,32 + e32,23 - e22,33 - e33,22 = 0 #
# e31,12 + e12,31 - e32,11 - e11,32 = 0 #
# e31,22 + e22,31 - e32,21 - e21,32 = 0 #
# e31,13 + e13,31 - e33,11 - e11,33 = 0 #
# e31,23 + e23,31 - e33,21 - e21,33 = 0 #
# e32,11 + e11,32 - e31,12 - e12,31 = 0 #
# e32,21 + e21,32 - e31,22 - e22,31 = 0 #
# e32,13 + e13,32 - e33,12 - e12,33 = 0 #
# e32,23 + e23,32 - e33,22 - e22,33 = 0 #
# e33,11 + e11,33 - e31,13 - e13,31 = 0 #
# e33,21 + e21,33 - e31,23 - e23,31 = 0 #
# e33,12 + e12,33 - e32,13 - e13,32 = 0 #
# e33,22 + e22,33 - e32,23 - e23,32 = 0 #
#                                       #
#           Only 36 equation            #
#########################################

def filter_repeated_equations(augmented):
    
    raw1 = 0    # Loop over raws
    while raw1 < len(augmented):
        raw2 = 0   # Loop over raws
        while raw2 < len(augmented):
            if raw1 == raw2:
                raw2 += 1
                continue
            
            f = [False, False, False, False]    # Flag
            g = 0      # Iterator index of f

            for column1 in range(4):    # Lopp over colmuns
                for column2 in range(4):      # Lopp over colmuns
                    tmp1 = swap(augmented[raw1][column1])
                    tmp2 = swap(augmented[raw2][column2])
                    for i in range(4):
                        for j in range(4):
                            if tmp1[i] == tmp2[j]:  # Compare all possible swaps of the two terms
                                f[g] = True
                                break
                                
                        if f[g] == True:
                            break
                    if f[g] == True:
                        break
                if f[g] == True:
                    g += 1
                    if (f[0] == True and f[1] == True and f[2] == True and f[3] == True):
                        augmented.pop(raw2)     # Remove repeated equation
                        break
            if (f[0] == True and f[1] == True and f[2] == True and f[3] == True):   # This condition for special case:
                continue                                                            #   If there is three simillar equations repeated simultaneously
            raw2 += 1                                                               #   Let them eqn 4, 5, 6
        raw1 += 1                                                                   #   Then, At comparing between them, raw1 = 4 & raw2 = 5
                                                                                    #   Eqn 5 will be removed, So that eqn 6 will be eqn 5, raw1 = 4 & raw2 = 6
                                                                                    #   So that we must enusre that the shifted eqn is not simillar to the previous deleted one 
    return augmented


def swap(input_array):

    i = input_array[0]
    j = input_array[1]
    k = input_array[2]
    l = input_array[3]

    output_array = [[j, i, k, l]
                   ,[j, i, l, k]
                   ,[i, j, k, l]
                   ,[i, j, l, k]]

    return output_array

def output(augmented):

    for a in range(len(augmented)):
        print("e", end="")
        for i in range(2):
            for j in range(2):
                print(augmented[a][i][j], end="")
            print(",", end="")
            for j in range(2, 4):
                print(augmented[a][i][j], end="")
            if i != 1:
                print(" + e", end="")

        print(" - e", end="")
        for i in range(2, 4):
            for j in range(2):
                print(augmented[a][i][j], end="")
            print(",", end="")
            for j in range(2, 4):
                print(augmented[a][i][j], end="")
            if i != 3:
                print(" - e", end="")
        print(" = 0")

    return

main()