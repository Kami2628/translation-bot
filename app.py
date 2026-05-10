import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import pyperclip

# Page setup
st.set_page_config(
    page_title="100 Language Translator Bot",
    page_icon="🌍",
    layout="centered"
)

# Title
st.title("🌍 AI Translation Bot")
st.write("Translate Any Language into 100+ Languages")

# Get all supported languages
languages = GoogleTranslator().get_supported_languages(as_dict=True)

# Convert languages into list
language_names = list(languages.keys())

# Source language selection
source_language = st.selectbox(
    "Select Source Language",
    language_names,
    index=language_names.index("english")
)

# Target language selection
target_language = st.selectbox(
    "Select Target Language",
    language_names,
    index=language_names.index("urdu")
)

# Text input
text = st.text_area(
    "Enter Text",
    height=150,
    placeholder="Type your text here..."
)

# Translate button
if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter text")

    else:
        try:

            # Translate text
            translated_text = GoogleTranslator(
                source=languages[source_language],
                target=languages[target_language]
            ).translate(text)

            # Show translated text
            st.subheader("Translated Text")

            # Output box
            st.text_area(
                "Result",
                translated_text,
                height=150
            )

            # Copy button
            if st.button("Copy Translation"):
                pyperclip.copy(translated_text)
                st.success("Translation copied successfully!")

            # Text-to-speech
            try:
                tts = gTTS(
                    text=translated_text,
                    lang=languages[target_language]
                )

                audio_file = "translation.mp3"
                tts.save(audio_file)

                audio_bytes = open(audio_file, "rb").read()

                st.audio(audio_bytes, format="audio/mp3")

            except:
                st.warning("Voice not supported for this language.")

            # Download translated text
            st.download_button(
                label="Download Translation",
                data=translated_text,
                file_name="translated_text.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.caption("Made with Python + Streamlit")