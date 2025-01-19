import os

from TTS.api import TTS as CoquiTTS

class TTS:
    """
    Class for Text-to-Speech using Coqui TTS.
    """
    def __init__(self) -> None:
        """
        Initializes the TTS class.

        Returns:
            None
        """
        # Initialize TTS with VITS model
        self._tts = CoquiTTS(model_name="tts_models/en/ljspeech/vits", progress_bar=False, gpu=False)

    def generate_speech(self, text: str, output_path: str) -> None:
        """
        Generates speech from text.

        Args:
            text (str): The text to convert to speech.
            output_path (str): The path to save the generated speech to.

        Returns:
            None
        """
        # Generate the speech
        self._tts.tts_to_file(text=text, file_path=output_path)

    @property
    def synthesizer(self) -> CoquiTTS:
        """
        Returns the synthesizer.

        Returns:
            CoquiTTS: The synthesizer.
        """
        return self._tts

    def synthesize(self, text: str, output_file: str = os.path.join(os.getcwd(), ".mp", "audio.wav")) -> str:
        """
        Synthesizes the given text into speech.

        Args:
            text (str): The text to synthesize.
            output_file (str, optional): The output file to save the synthesized speech. Defaults to "audio.wav".

        Returns:
            str: The path to the output file.
        """
        # Generate the speech
        self.generate_speech(text, output_file)

        return output_file
