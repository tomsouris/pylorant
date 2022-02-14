from src.apis.Buddies import Buddies
from .apis import Agent, Buddies

class ApiClient():
    def __init__(self) -> None:
        self._agent   = Agent()
        self._buddies = Buddies()
    
    @property
    def agent(self) -> Agent:
        """_summary_
        Interface to the Agent APIs

        Returns:
            Valorant: _description_
        """
        return self._agent

    @property
    def buddies(self) -> Buddies:
        """_summary_
        Interface to the Buddies APIs

        Returns:
            Valorant: _description_
        """
        return self._buddies