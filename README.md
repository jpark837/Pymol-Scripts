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
   Tuple format: (Atom1, Atom2, Residue 1, Residue 2, Distance between pair)

