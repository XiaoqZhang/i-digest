import pubchempy as pcp
from pubchempy import get_compounds

for compound in get_compounds('glucose', 'name'):
    c = pcp.Compound.from_cid(5090)
    print(c.isomeric_smiles)