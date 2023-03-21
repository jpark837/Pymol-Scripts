# Pymol-Scripts
Compilation of different pymol scripts written for extracting structural properties using pymol:

-  find_residue.py  
   usage: find_residue('selection as string', '1-letter amino acid as string')  
   e.g. find_residue('protein','D')  
   Prints the number of instances of the amino acid and the position of the instances as a list

-  report_ss.py  
   usage: report_ss('selection as string')  
   e.g. report_ss('protein')  
   prints the one letter identifier, position, and secondary structure type

-  int_hbonds.py  
   This is only for intramolecular hydrogen bonds  
   usage: int_hbonds('selection as string', minimum cutoff distance in angstrom,       maximum cutoff distance in angstrom, angle)  
   e.g. int_hbonds('protein', 2.5, 3.2, 45)  
   Prints and returns a list of tuples.  
   Tuple format: (Atom1, Residue 1, Atom2, Residue 2, Distance between pair)
   
-  int_saltbridge.py  
   This is only for intramolecular salt bridges. Only considers LYS, ARG as possible cations and ASP, GLU as possible anions
   usage: int_saltbridge('selection as string', minimum cutoff distance in angstrom, maximum cutoff distance in angstrom, angle)  
   e.g. int_saltbridge('protein', 1, 4, 180)  
   Prints and returns a list of tuples.  
   Tuple format: (Atom1, Residue 1 num., Residue 1, Atom2, Residue 2 num., Residue 2, Distance between pair)

