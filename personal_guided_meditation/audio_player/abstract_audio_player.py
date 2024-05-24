from abc import ABC, abstractmethod


class AudioPlayer(ABC):
    @abstractmethod
    def play(self, file_path: str):
        """Playing the audio file

        Args:
            file_path (str): the path for the audio file
        """
        pass