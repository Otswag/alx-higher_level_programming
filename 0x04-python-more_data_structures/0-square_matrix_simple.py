#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if(matrix):
        return ([[b*b for b in a] for a in matrix])
