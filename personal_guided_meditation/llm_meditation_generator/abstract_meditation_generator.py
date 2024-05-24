from abc import ABC, abstractmethod

class MeditationGenerator(ABC):
    @abstractmethod
    def generate_meditation(self) -> str:
        pass
