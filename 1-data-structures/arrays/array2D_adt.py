'''
Create an array2D abstract data type with the following operations:

'''
from array import Array

class Array2D:
    '''creates a two-D array of size num_rows x num_cols.
    initial values are set to None'''

    def __init__(self, num_rows, num_cols):
        ''' create a 1-D array to store an array reference for each row'''
        self._theRows = Array(num_rows)

        # creates the 1-D array for each row of the 2-D array
        for i in range(num_rows):
            self._theRows[i] = Array(num_cols)

    def num_rows(self):
        '''returns the number of rows'''
        return len(self._theRows)

    def num_cols(self):
        '''returns num of cols'''
        return len(self._theRows[0])

    def clear(self, value):
        '''clears array by setting each element to the given value'''
        for row in range(self.num_rows()):
            row.clear(value)

    def get_item(self, ndx_tuple):
        '''gets the content of the element at position [i,j] '''
        row = ndx_tuple[0]
        col = ndx_tuple[1]

        the_1d_array = self._theRows[row]
        return the_1d_array[col]

    def __setitem__(self, ndx_tuple, value):
        '''sets the content of the element at position [i,j] '''
        row = ndx_tuple[0]
        col = ndx_tuple[1]

        the_1d_array = self._theRows[row]
        the_1d_array[col] = value

