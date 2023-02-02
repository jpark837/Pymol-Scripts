# copyright (C) 2010 Jihyun Park
from pymol import cmd


def find_residue(selection, residue):
    '''
    Input: selection as string, 1-letter amino acid as string.
    Ouput: prints the number of instances of the amino acid and the string of the position of the instances as a list
    e.g. find_residue('protein', 'D')
    '''
    aaseq = cmd.get_fastastr(selection)
    list_aa = ''.join(aaseq.split()[1:]) # [1:] removes the header

    index_match = []
    for i in range(0,len(list_aa)):
      if list_aa[i] == residue:
        index_match.append(i)
    
    print("Amount of times this amino acid appears: {} times".format(len(index_match)))
    print("The position of these instances: \n {}". format([x+1 for x in index_match])) #because python idexes starting from 0.

cmd.extend("find_residue", find_residue)