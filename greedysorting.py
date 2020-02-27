#Author: Daniel Nicholson-Gardner #
#Name: greedysorting.py #
#Created On: 23/10/2019 #
#Modified by: Daniel Nicholson-Gardner #
#Last Modified: 13/12/2019 #

def breakpoint_count(permutation):
   
    permutation = [0] + list(permutation) + [len(permutation)+1]

    return sum(map(lambda x, y: abs(x-y) != 1, permutation[1:], permutation[:-1]))


def breakpoint_indices(permutation):
   
    from itertools import compress
  
    permutation = [0] + list(permutation) + [len(permutation)+1]

    return compress(xrange(len(permutation)-1), map(lambda x, y: abs(x-y) != 1, permutation[1:], permutation[:-1]))


def greedy_breakpoint_bfs(perm1, perm2):
   
    from itertools import product

  
    to_identity = {value: i + 1 for i, value in enumerate(perm2)}
    normalized_perm = [to_identity[value] for value in perm1]

   
    rev_perm = lambda perm, i, j: perm[:i] + perm[i:j + 1][::-1] + perm[j + 1:]

  
    normalized_perm = tuple(normalized_perm)
    current_perms = [normalized_perm]
    min_breaks = breakpoint_count(normalized_perm)
    dist = 0

  
    while True:
        new_perms = []
        dist += 1
       
        for perm in current_perms:
            for rev_ind in product(breakpoint_indices(perm), repeat=2):
             
                temp_perm = tuple(rev_perm(perm, rev_ind[0], rev_ind[1] - 1))
                temp_breaks = breakpoint_count(temp_perm)

               
                if temp_breaks == 0:
                    return dist

               
                elif temp_breaks < min_breaks:
                    min_breaks = temp_breaks
                    new_perms = [temp_perm]

               
                elif temp_breaks == min_breaks:
                    new_perms.append(temp_perm)

        current_perms = new_perms


if __name__ == '__main__':

  
    with open('datasets/rosalind_ba6a(1).txt') as input_data:
        permutations_list = [pair.strip().split('\n') for pair in input_data.read().split('\n\n')]
        for index, pair in enumerate(permutations_list):
            permutations_list[index] = [map(int, perm.split()) for perm in pair]


    min_dists = [str(min(greedy_breakpoint_bfs(p1, p2), greedy_breakpoint_bfs(p2, p1)))
        for p1, p2 in permutations_list]

  
    print( ' '.join(min_dists))
    with open('datasets/results_gs.txt', 'w') as output_data:
        output_data.write(' '.join(min_dists))
