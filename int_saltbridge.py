# copyright (C) 2023 Jihyun Park
from pymol import cmd
from pymol import stored

def int_saltbridge(selection, min_cutoff, max_cutoff, angle):
        '''
        Input: selection as string, minimum cutoff distance in angstrom, maximum cutoff distance in angstrom, angle
        Output: Prints and returns a list of tuples.
        Tuple format: (Atom1, Residue 1, Atom2, Residue 2, Distance between pair)
        Only considers LYS, ARG as possible cations and ASP, GLU as possible anions'''

        selection_string = "(" + selection + " & resn Lys & sidechain & n. NZ)" + " | " + "(" + selection + " & resn Arg & sidechain & n. NH1)" + " | " + "(" + selection + " & resn Asp & sidechain & n. OD2)" + " | " + "(" + selection + " & resn Glu & sidechain & n. OE2)" 
        saltbridge_bonds = cmd.find_pairs(selection_string, selection_string, mode=1, cutoff=float(max_cutoff), angle=float(angle))
        pairs = []

        saltbridge_bonds.sort()

        for i in saltbridge_bonds:

            if (i[1], i[0]) in saltbridge_bonds: #unique only
                saltbridge_bonds.remove((i[1], i[0])) 
                
            stored.tuple_pair = () ## Tuple of (Atom 1, Residue number 1, 3 letter residue Atom 1, Atom 2, Residue number 2, 3 letter residue Atom 2, Distance between pair)
            
            # write string for selections
            sel_atom1 = i[0][0] + ' and index ' + str(i[0][1])
            sel_atom2 = i[1][0] + ' and index ' + str(i[1][1])### Calculate distance
            
            dist=cmd.distance('temp', sel_atom1, sel_atom2, cutoff=float(max_cutoff), mode = 0)            
            cmd.delete('temp') # To remove pre-drawn labels of bonds
            
            if dist > min_cutoff:

                ### First atom of the pair                
                cmd.iterate(sel_atom1, 'stored.tuple_pair += (name, resi, resn)' )
                
                ### Second atom of the pair
                cmd.iterate(sel_atom2,'stored.tuple_pair += (name, resi, resn)' )

                # Check if only cationic (Lys,Arg) and anionic (Asp, Glu) pairs:
                if (stored.tuple_pair[2] in ['LYS','ARG'] and stored.tuple_pair[5] in ['ASP','GLU']) or (stored.tuple_pair[5] in ['LYS','ARG'] and stored.tuple_pair[2] in ['ASP','GLU']):

                    ### Record distance
                    dist=cmd.distance('internal_hbonds', sel_atom1, sel_atom2, cutoff=float(max_cutoff), mode = 0)
                    stored.tuple_pair += (round(dist,2),)
                    pairs.append(stored.tuple_pair)
                    
        for i in pairs:
            print("Atom1: {}, Residue1: {} {}, Atom2: {}, Residue2: {} {}, distance:{}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

        return pairs   

cmd.extend("int_saltbridge", int_saltbridge)

