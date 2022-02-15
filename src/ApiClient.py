from src.apis.Buddies import Buddies
from .apis import Agent, Buddies, Bundles

class ApiClient():
    def __init__(self) -> None:
        self._agent   = Agent()
        self._buddies = Buddies()
        self._bundles = Bundles()
    
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
    @property

    def bundles(self) -> Bundles:
        """_summary_
        Interface to the Bundles APIs

        Returns:
            Valorant: _description_
        """
        return self._bundles