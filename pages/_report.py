import streamlit as st

st.title("📄 Report")
st.write(
    """
    Qui verrà generato un *riepilogo* scaricabile dei risultati:
    - input inseriti,
    - percentuale ed esito,
    - data/ora e versione del modello.

    
    """
)
from ui import render_footer
render_footer("Gabriele Di Bella", "", "https://github.com/Di-Bella-Gabriele/hearth-risk-app")