from pymatgen.core import Structure
from pymatgen.io.cif import CifParser
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

def analyze_structure(cif_string):
    """
    Parses a CIF string and returns a dictionary of physical properties.
    """
    try:
        # 1. Initialize the CifParser from the string provided by Gemini
        parser = CifParser.from_str(cif_string)
        
        # 2. Get the structure object
        structure = parser.get_structures()[0]
        
        # 3. Use SpacegroupAnalyzer for advanced symmetry info
        analyzer = SpacegroupAnalyzer(structure)
        
        # 4. Extract the physical metrics
        return {
            "density": structure.density,
            "volume": structure.volume,
            "space_group": analyzer.get_space_group_symbol(),
            "formula": structure.composition.reduced_formula
        }
    except Exception as e:
        # Return the error so the app can display a helpful warning instead of crashing
        return {"error": str(e)}