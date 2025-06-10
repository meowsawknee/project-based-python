import streamlit as st
from src.pin_generator import PinCodeGenerator
from src.memorable_generator import MemorablePasswordGenerator
from src.random_generator import RandomPasswordGenerator


st.title("🔐 Password Dealers")
st.markdown("_Post-Apocalyptic Security Providers_")


if "dealer" not in st.session_state:
    st.session_state["dealer"] = None

col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/numbro_placeholder.png", caption="Numbro")
    if st.button("Choose Numbro", key="choose_numbro"):
        st.session_state["dealer"] = "numbro"

with col2:
    st.image("assets/memo_placeholder.png", caption="Memo")
    if st.button("Choose Memo", key="choose_memo"):
        st.session_state["dealer"] = "memo"

with col3:
    st.image("assets/ciphera_placeholder.png", caption="Ciphera")
    if st.button("Choose Ciphera", key="choose_ciphera"):
        st.session_state["dealer"] = "ciphera"


st.markdown("---")

if st.session_state["dealer"] == "numbro":
    st.subheader("You chose: Numbro")
    st.markdown("> *“Four digits. Nothing more. Pure calculation.”*")
    
    length = st.slider("Length", min_value=4, max_value=32, value=18)
    only_even = st.checkbox("Only even digits")
    only_odd = st.checkbox("Only odd digits", disabled=only_even)
    starts_with = st.text_input("Starts with (optional)", max_chars=3)
    checksum = st.checkbox("Add checksum digit")
    
    if st.button("Generate PIN"):
        try:
            generator = PinCodeGenerator(
                length=length,
                only_even=only_even,
                only_odd=only_odd,
                starts_with=starts_with if starts_with else None,
                checksum=checksum
            )
            password = generator.generate()
            strength = generator._last_strength

            st.success(f"🔢 Your PIN: `{password}`")
            st.info(f"🧠 Strength: {strength}")
        
        except Exception as e:
            st.error(f"❌ Error: {e}")

elif st.session_state["dealer"] == "memo":
    st.subheader("You chose: Memo")
    st.markdown("> *“Security through poetry, darling.”*")

    num_words = st.slider("Number of words", min_value=2, max_value=12, value=3)
    separator = st.text_input("Separator character (optional)", value="-")
    capitalization = st.checkbox("Capitalize each word?", value=True)

    if st.button("Generater memorable password"):
        try:
            generator = MemorablePasswordGenerator(
                number_of_words=num_words,
                separator=separator if separator else "-",
                capitalization=capitalization
            )
            password = generator.generate()
            strength = generator._last_strength

            st.success(f"🧠 Your password: {password}")
            st.info(f"🔒 Strength: {strength}")
        
        except Exception as e:
            st.error(f"❌ Error: {e}")

elif st.session_state["dealer"] == "ciphera":
    st.subheader("You chose: Ciphera")
    st.markdown("> *“Complexity is beauty.”*")

    length = st.slider("Password length", min_value=8, max_value=32, value=12)
    use_digits = st.checkbox("Include digits", value=True)
    use_symbols = st.checkbox("Include symbols", value=True)
    custom_characters = st.text_input("Custom characters (optional)", value="")

    if st.button("Generate strong password"):
        try:
            generator = RandomPasswordGenerator(
                length=length,
                use_symbols=use_symbols,
                use_digits=use_digits,
                custom_characters=custom_characters if custom_characters else None
            )
            password = generator.generate()
            strength = generator._last_strength

            st.success(f"🔒 Your password: {password}")
            st.info(f"🧠 Strength: {strength}")
        
        except Exception as e:
            st.error(f"❌ Error: {e}")