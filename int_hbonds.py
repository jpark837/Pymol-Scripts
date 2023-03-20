# copyright (C) 2023 Jihyun Park
from pymol import cmd
from pymol import stored


def int_hbonds(selection, min_cutoff, max_cutoff, angle):
        '''
        Input: selection as string, minimum cutoff distance in angstrom, maximum cutoff distance in angstrom, angle
        Output: Prints and returns a list of tuples.
        Tuple format: (Atom1, Residue 1, Atom2, Residue 2, Distance between pair)'''

        hyd_bonds = cmd.find_pairs(selection + "& symbol n+o", selection + "& symbol n+o", mode=1, cutoff=float(max_cutoff), angle=float(angle))
        pairs = []

        for i in hyd_bonds:

            if (i[1], i[0]) in hyd_bonds: #unique only
                hyd_bonds.remove((i[1], i[0])) 
        
            stored.tuple_pair = () ## Tuple of (Atom1, Residue 1, Atom2, Residue 2, Distance between pair)
            
            # write string for selections
            sel_atom1 = i[0][0] + ' and index ' + str(i[0][1])
            sel_atom2 = i[1][0] + ' and index ' + str(i[1][1])### Calculate distance
            
            dist=cmd.distance('temp', sel_atom1, sel_atom2, cutoff=float(max_cutoff), mode = 0)            
            cmd.delete('temp') # To remove pre-drawn labels of bonds

            if dist > min_cutoff:
                print(dist)
                print(min_cutoff)
                ### First atom of the pair                
                cmd.iterate(sel_atom1,
                            'stored.tuple_pair += (name, resi)' )
                            #'print("Element: {} Residue: {} atom index: {}".format(name, resi, index))')
                
                ### Second atom of the pair
                cmd.iterate(sel_atom2,
                            'stored.tuple_pair += (name, resi)' )
                
                ### Record distance
                dist=cmd.distance('internal_hbonds', sel_atom1, sel_atom2, cutoff=float(max_cutoff), mode = 0)
                stored.tuple_pair += (round(dist,2),)
                pairs.append(stored.tuple_pair)
                    
        for i in pairs:
            print("Atom1: {}, Residue1: {}, Atom2: {}, Residue2: {}, distance:{}".format(i[0], i[1], i[2], i[3], i[4]))

        return pairs   

cmd.extend("int_hbonds", int_hbonds)
