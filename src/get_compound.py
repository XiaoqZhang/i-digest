import pubchempy as pcp
from pubchempy import get_compounds
from rdkit import Chem

for compound in get_compounds('glucose', 'name'):
    cid = compound.cid
    c = pcp.Compound.from_cid(cid)
    print(c.isomeric_smiles)
    Chem.MolFromSmiles(c.isomeric_smiles)