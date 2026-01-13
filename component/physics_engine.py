from pymatgen.core import Structure
from pymatgen.io.cif import CifParser
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

def analyze_structure(cif_string):
    """
    Parses a CIF string and returns a dictionary of physical properties.
    Now includes lattice parameters and crystal system identification.
    """
    try:
        # 1. Initialize the CifParser from the string provided by Gemini
        parser = CifParser.from_str(cif_string)
        
        # 2. Get the structure object (taking the first structure in the CIF)
        structure = parser.get_structures()[0]
        
        # 3. Use SpacegroupAnalyzer for advanced symmetry info
        # symprec=0.1 is a standard tolerance for AI-generated structures
        analyzer = SpacegroupAnalyzer(structure, symprec=0.1)
        
        # 4. Extract the physical metrics
        lattice = structure.lattice
        
        return {
            "density": structure.density,
            "volume": structure.volume,
            "space_group": analyzer.get_space_group_symbol(),
            "crystal_system": analyzer.get_crystal_system(),
            "formula": structure.composition.reduced_formula,
            # Adding lattice constants for more scientific detail
            "a": lattice.a,
            "b": lattice.b,
            "c": lattice.c,
            "alpha": lattice.alpha,
            "beta": lattice.beta,
            "gamma": lattice.gamma
        }
    except Exception as e:
        # Return the error so the app can display a helpful warning instead of crashing
        return {"error": str(e)}


def validate_results(results, mat_class):
    """
    Check if the calculated physics make sense.
    """

    warnings = []
    
    # example - Density sanity check
    if mat_class == 'Oxide' and results['density'] > 6.0:
        warnings.append('Density seems high for a standard oxide.')

    if mat_class == 'Metal/Alloy' and results['density'] < 2.0:
        warnings.append('Density seems low for a Metallic system.')

    # check for unrealistic unit cell volumes
    if results['volume'] < 5.0:
        warnings.append('Unit cell volume is suspiciously small.')

    return warnings