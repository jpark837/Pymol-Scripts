# copyright (C) 2023 Jihyun Park
from pymol import cmd
from pymol import stored

def report_ss(selection):
    '''
    Input: selection as string
    Ouput: prints the one letter identifier, position, and secondary structure type
    e.g. report_ss('protein')
    '''

    selection += ' & name CA'
    stored.res_pos, stored.res_let, stored.ss = [], [], []

    cmd.iterate(selection, 'stored.res_pos.append(resv)')
    cmd.iterate(selection, 'stored.res_let.append(oneletter)')
    cmd.iterate(selection, 'stored.ss.append(ss)')

    for i in range(0, len(stored.ss)):
        if stored.ss[i] == 'H':
            print("Residue: {}  {}, Secondary structure: 'alpha helix'".format(stored.res_let[i], stored.res_pos[i]))
        if stored.ss[i] == 'S':
            print("Residue: {}  {}, Secondary structure: 'beta sheet'".format(stored.res_let[i], stored.res_pos[i]))
        if stored.ss[i] == 'L':
            print("Residue: {}  {}, Secondary structure: 'loop'".format(stored.res_let[i], stored.res_pos[i]))
    return stored.res_pos, stored.ss

cmd.extend("report_ss", report_ss)
