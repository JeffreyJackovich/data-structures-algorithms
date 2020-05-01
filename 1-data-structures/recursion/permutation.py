'''
TODO:
   Recursively:  ['a','b'] -> [['a','b'], ['b','a']]

    return a list of lists

'''
def permutation(a_list):
    '''Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]'''
    # Base case
    if len(a_list) == 1:
        return [a_list]

    #Recurse
    output = []
    for ix in range(len(a_list)): #[0,1]
        sub_list = permutation(a_list[:ix] + a_list[ix+1:])

    output.append(sub_list)
    return output


a_list = ['a','b']

print(permutation(a_list))