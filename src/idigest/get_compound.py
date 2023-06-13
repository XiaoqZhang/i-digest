import pandas as pd
import pubchempy as pcp
from loguru import logger
from pubchempy import get_compounds
from chemdataextractor import Document

def chem(text):
    """
        Get PubChem data for a list of chemical compounds in a text if they are present in the PubChem database.
        Input: Text (str)
        Output: DataFrame with PubChem data (label, link, SMILES)
    """
    doc = Document(text)
    chem_names = list(set([str(cem.text).lower() for cem in doc.cems]))
    logger.debug(f"The chemical compounds found: {chem_names}")

    cids_list = []
    pubchem_data = {'label':[], 'iupac':[], 'link':[], 'SMILES':[]}
    for name in chem_names:
        try:
            pcp_compounds = get_compounds(name, 'name')
            for compound in pcp_compounds:
                cid = compound.cid
                c = pcp.Compound.from_cid(cid)
                iupac = c.iupac_name
                link = f'https://pubchem.ncbi.nlm.nih.gov/compound/{c.cid}'
                SMILES = c.isomeric_smiles
                pubchem_data["label"].append(name)
                pubchem_data["iupac"].append(iupac)
                pubchem_data["link"].append(link)
                pubchem_data["SMILES"].append(SMILES)
        except:
            continue
        
    return pd.DataFrame(pubchem_data)