# copyright (C) 2023 Jihyun Park
from pymol import cmd
from pymol import stored


def int_hbonds(selection, cutoff, angle):
        '''
        Input: selection as string, cutoff distance in angstrom, angle
        Output: Prints and returns a list of tuples.
        Tuple format: (Atom1, Atom2, Residue 1, Residue 2, Distance between pair)'''

        hyd_bonds = cmd.find_pairs(selection + "& symbol n+o", selection + "& symbol n+o", mode=1, cutoff=float(cutoff), angle=float(angle))

        pairs = []

        for i in range(0, len(hyd_bonds)):
            stored.tuple_pair = () ## Tuple of (Atom 1, Atom 2, Residue number 1, Residue number 2, Distance between pair)
            
            ### First atom of the pair
            sel_atom1 = hyd_bonds[i][0][0] + ' and index ' + str(hyd_bonds[i][0][1])
            cmd.iterate(sel_atom1,
                        'stored.tuple_pair += (name, resi)' )
            
            ### Second atom of the pair
            sel_atom2 = hyd_bonds[i][1][0] + ' and index ' + str(hyd_bonds[i][1][1])
            cmd.iterate(sel_atom2,
                        'stored.tuple_pair += (name, resi)' )
            
            ### Calculate distance
            x=cmd.distance('internal_hbonds', sel_atom1, sel_atom2, cutoff=float(cutoff), mode = 0)
            stored.tuple_pair += (round(x,2),)
            pairs.append(stored.tuple_pair)
        
        for i in pairs:
            print("Atom1: {}, Residue1: {}, Atom2: {}, Residue2: {}, distance:{}".format(i[0], i[1], i[2], i[3], i[4]))
            

cmd.extend("int_hbonds", int_hbonds)