import aiida
import json
import re

from aiida import orm
aiida.load_profile()
import os
from ase.io import read
from glob import glob
from aiida.tools import get_kpoints_path



space_no = {}

for name in glob("data/structures_3D_xsf_small/*"):
   s = orm.StructureData(ase=read(name))
   s.set_source({'description': 'Database of 3D structures v1.0, from N. Mounet, P. Schwaller, A. Merkys, A. Cepellotti and G. Pizzi, sitting on theossrv5.epfl.ch (postgreSQL db)',
		 'id': name.split('/')[-1].split('.xsf')[0],
		 'db_name':'aiidamatdb'})
   a = get_kpoints_path(s)
   space_no[s.uuid] = a['parameters'].get_dict()['spacegroup_number'] #### It store the uuid and the coresponding space group number.
   s.store()




with open('./generated_files/structure_info.json', 'w') as file:
     file.write(json.dumps(space_no))
