from chemdataextractor import Document

import pubchempy as pcp
from pubchempy import get_compounds

from loguru import logger

def chem(text):
    doc = Document(text)
    chem_names = [cem.text for cem in doc.cems]
    logger.debug(f"The chemical compounds found: {chem_names}")

    for name in chem_names:
        try:
            pcp_compounds = get_compounds(name, 'name')
            for compound in pcp_compounds:
                cid = compound.cid
                c = pcp.Compound.from_cid(cid)
                logger.info(f"{c.isomeric_smiles}")
        except:
            pass
