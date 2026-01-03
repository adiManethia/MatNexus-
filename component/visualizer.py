from stmol import showmol 
import py3Dmol 

def render_crystal(cif_string):
    """Render a crystal structure from a CIF string."""
    
    # create a py3Dmol viewer
    view = py3Dmol.view(width=400, height=400)
    
    # add CIF data to the view 
    view.addModel(cif_string, "cif")

    # set style : sphere -> atoms, sticks -> bonds 
    view.setStyle({'sphere':{'colorscheme': "Jmol", 'scale':0.3},
    'stick':{'colorscheme': "Jmol", 'scale': 0.1}})

    # add unit cell box 
    view.addUnitCell() 

    # zoom to fit the structure 
    view.zoomTo() 

    # render in streamlit 
    showmol(view, height=400, width=400)