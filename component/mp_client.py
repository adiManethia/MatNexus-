from mp_api.client import MPRester 
import os 
from dotenv import load_dotenv 

load_dotenv()
api_key = os.getenv("MP_API_KEY")


def get_mp_reference(formula):

    """
    Fetches the most stable structure for a given formula from the Materials Project database.
    """

    try:
        with MPRester(api_key) as mpr:
            # Search for the most stable entry - lowest energy 
            docs = mpr.summary.search(formula=formula, fields=["density", "symmetry", "volume", "material_id"])

            if docs:

                # Sort by energy to get most stable entry 
                stable_entry = docs[0]

                return {
                    "mp_id" : stable_entry.material_id,
                    "density": stable_entry.density,
                    "space_group": stable_entry.symmetry.symbol,
                    "volume" : stable_entry.volume
                }

            return None 

    except Exception as e:
        print(f"MP API Error: {e}")
        return None