import streamlit as st
import pyperclip

def render_download_button(password: str, filename: str = "password.txt"):
    """
    Render a Streamlit download button to save the password to a file.
    """
    st.download_button(
        label="Save password",
        data=password,
        file_name=filename,
        mime="text/plain"
    )


def render_clipboard_button(password: str):
    """
    Simple native-style clipboard button using pyperclip.
    (Works only in local Python execution)
    """
    # Note: Clipboard functionality via pyperclip may not work in all environments.
    # It's purely optional and doesn't affect core features.

    if st.button("Copy to clipboard"):
        try:
            pyperclip.copy(password)
            st.success("Copied to clipboard!")
        except Exception as e:
            st.error(f"Clipboard error: {e}")
