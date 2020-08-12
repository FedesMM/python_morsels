from copy import deepcopy

def add_v1_0(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2):
        print("Lenght of list of matrixes is not the same.")
    else:
        matrix_3 =[]
        for i_list in range(0,len(matrix_1)):
            print("Listas: "+str(matrix1[i_list])+"\t"+str(matrix_2[i_list]))
            list_3=[]
            if len(matrix_1[i_list]) != len(matrix_2[i_list]):
                print("Lenght of list is not the same.")
            else:
                for i_element in range(0, len(matrix_1[i_list])):
                    elem = matrix_1[i_list][i_element] + matrix_2[i_list][i_element]
                    print("\tElementos: " + str(matrix1[i_list][i_element]) + " + " + str(matrix_2[i_list][i_element]) + " = " + str(elem))
                    list_3 += [elem]
            matrix_3 += [list_3]
        return matrix_3


def add_v2_0(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2):
        print("Lenght of list of matrixes is not the same.")
    else:
        matrix_3 =[]
        for i_list, list_1 in enumerate(matrix_1):
            list_2=matrix2[i_list]
            print("Listas: "+str(list_1)+"\t"+str(list_2))
            list_3=[]
            if len(list_1) != len(list_2):
                print("Lenght of list is not the same.")
            else:
                for i_element, element_1 in enumerate(list_1):
                    element_2 = list_2[i_element]
                    element_3 = element_1 + element_2
                    print("\tElementos: " + str(element_1) + " + " + str(element_2) + " = " + str(element_3))
                    list_3 += [element_3]
            matrix_3 += [list_3]
        return matrix_3


def add_v3_0(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2):
        print("Lenght of list of matrixes is not the same.")
    else:
        matrix_3 =[]
        for list_1, list_2 in zip(matrix_1, matrix_2):
            print("Listas: "+str(list_1)+"\t"+str(list_2))
            list_3=[]
            if len(list_1) != len(list_2):
                print("Lenght of list is not the same.")
            else:
                for element_1, element_2 in zip(list_1, list_2):
                    element_3 = element_1 + element_2
                    print("\tElementos: " + str(element_1) + " + " + str(element_2) + " = " + str(element_3))
                    list_3 += [element_3]
            matrix_3 += [list_3]
        return matrix_3


def add_v4_0(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2):
        print("Lenght of list of matrixes is not the same.")
    else:
        matrix_3 = [(e1 + e2) for l1, l2 in zip(matrix_1, matrix_2) for (e1, e2) in zip(l1, l2)]
        return matrix_3


def add_v5_0(*matrixes):
    lens=[len(matrix) for matrix in matrixes]
    correct_len=all(l == lens[0] for l in lens)
    if not correct_len:
        raise ValueError("Given matrices are not the same size.")
    else:
        solution, *rest = matrixes
        #print("solution:\t"+str(solution))

        for matrix in rest:
            #print("matrix:\t\t" + str(matrix))
            for i_vector, vector in enumerate(matrix):
                for i_element, element in enumerate(vector):
                    solution[i_vector][i_element] += matrix[i_vector][i_element]
        return solution


def add(*matrixes):
    lens_matrixes=[len(matrix) for matrix in matrixes]
    correct_len=all(l == lens_matrixes[0] for l in lens_matrixes)
    if not correct_len:
        raise ValueError("Given matrices are not the same size.")
    else:
        solution, rest = deepcopy(matrixes[0]), deepcopy(matrixes[1:])
        for matrix in rest:
            for i_vector, vector in enumerate(matrix):
                if len(solution[i_vector]) != len(vector):
                    raise ValueError("Given matrices are not the same size.")
                else:
                    for i_element, element in enumerate(vector):
                        solution[i_vector][i_element] += deepcopy(matrix[i_vector][i_element])
        return solution

