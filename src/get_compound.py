import pubchempy as pcp
import pandas as pd

def get_pubchem_df(compounds):
    """
        Get PubChem data for a list of compounds.
        Input: List of compounds (str)
        Output: DataFrame with PubChem data (label, link, SMILES)
    """
    pubchem_data = {'label':[], 'iupac':[], 'link':[], 'SMILES':[]}
    for compound in compounds:
        c = pcp.get_compounds(int(compound.split(' (CID ')[1].split(')')[0]), 'cid')
        iupac = c[0].iupac_name
        link = f'https://pubchem.ncbi.nlm.nih.gov/compound/{c[0].cid}'
        SMILES = c[0].isomeric_smiles
        pubchem_data["label"].append(compound)
        pubchem_data["iupac"].append(iupac)
        pubchem_data["link"].append(link)
        pubchem_data["SMILES"].append(SMILES)
    return pd.DataFrame(pubchem_data)