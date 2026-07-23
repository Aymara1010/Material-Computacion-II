import streamlit as st

def cambio_pag(ant=None, sig=None):
    st.divider()
    col1, col2 = st.columns(2)
    
    with col1:
        if ant:
            if st.button("**⬅️ Página Anterior**", use_container_width=True, type="primary"):
                st.switch_page(ant)
                
    with col2:
        if sig:
            if st.button("**Siguiente Página ➡️**", use_container_width=True, type="primary"):
                st.switch_page(sig)

    