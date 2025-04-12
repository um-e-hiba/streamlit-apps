# Unit Convertor
# Import Streamlit
import streamlit as st

conversion_factors = {
    'meter': 1,
    'kilometer': 1000,
    'centimeter': 0.01,
    'millimeter': 0.001,
    'foot': 0.3048,
    'inch': 0.0254,
}
def unit_converter(value:float, from_unit:str, to_unit:str):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unsupported unit.")
    base_value = value * conversion_factors[from_unit]
    result = base_value / conversion_factors[to_unit]

    return round(result, 4)

st.title("Unit Converter")

with st.container(border=True, height=400):
    st.write("Welcome to my Stremlit Unite Converter")

    value = st.number_input("Enter Value to Convert", value=None, placeholder="0.0")

    # Select Unit
    unit_options = list(conversion_factors.keys())
    from_unit = st.selectbox("Convert From", unit_options)
    to_unit = st.selectbox("Convert To", unit_options)

    if from_unit and to_unit and value:
        try:
            result = unit_converter(value, from_unit, to_unit)
            st.markdown(
                        f"""
                        <div style='background-color:#d4edda; color:#155724; padding:10px;
                                    border-radius:8px; border: 1px solid #c3e6cb; font-size:18px;'>
                            ✔ {value} {from_unit} = <strong>{result} {to_unit}</strong>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        except Exception as e:
            st.error(f"Conversion error: {e}")

