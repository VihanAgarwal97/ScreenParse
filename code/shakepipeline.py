'''
Code taken from github.com/mathbeveridge/shake
'''

import updatescript
import updatealias
import scriptanalysis
import edgemerge
import os
import sys

'''
The driver file that turns a set of scripts into a network.
'''

'''
Configuration assumptions:


1. The name of your alias file must match the name of your screenplay file.

2. The first name that appears in the alias file must match the name used as the character header of the screenplay.

3. Aliases are case sensitive.

4. Underscores are used to connect two word names.

5. Colons are removed from dialogue as they serve as a demarcation between dialogue and character.

'''


########################################
# Choose the screenplay

# screenplay, must be the name of the .txt
# file without the .txt included
screenplay = "bladeII"

########################################

#mydir
my_dir = sys.path[0] + '/../'


#datadir
data_dir = my_dir + "data/"

#outdir
out_dir = my_dir + "out/" + screenplay + "/"


if not os.path.exists(out_dir):
    os.makedirs(out_dir)


# currently support import of more than one alias file
alias_file_list = [
    data_dir + "alias/" + screenplay + ".csv"
]

raw_script_file = data_dir + "screenplays/" + screenplay +  ".txt"

# output files
out_file_prefix = out_dir + screenplay

update_script_file = out_file_prefix + "-updated.txt"
alias_script_file = out_file_prefix + "-alias.txt"
edge_file_prefix = out_file_prefix + "-edge"
final_edge_file = edge_file_prefix + "-all.csv"

print("UPDATING")
updatescript.update(raw_script_file, update_script_file)

print("ALIASING")
updatealias.update(update_script_file, alias_script_file, alias_file_list)

print("ANALYZING")
edge_file_list = scriptanalysis.analyze(alias_script_file, alias_file_list, edge_file_prefix)

print("MERGING")
edgemerge.merge(edge_file_list, final_edge_file)
