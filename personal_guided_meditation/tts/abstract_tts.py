from abc import ABC, abstractmethod

class TextToSpeech(ABC):
    @abstractmethod
    def text_to_speech(self, text: str, file_path: str):
        pass
