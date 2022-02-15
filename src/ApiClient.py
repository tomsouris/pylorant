from .apis import Agent, Buddies, Bundles, Ceremonies, CompetitiveTier

class ApiClient():
    def __init__(self) -> None:
        self._agent            = Agent()
        self._buddies          = Buddies()
        self._bundles          = Bundles()
        self._ceremonies       = Ceremonies()
        self._competitive_tier = CompetitiveTier()

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

    @property
    def ceremonies(self) -> Ceremonies:
        """_summary_
        Interface to the Ceremonies APIs

        Returns:
            Valorant: _description_
        """
        return self._ceremonies
    
    @property
    def competitiveTier(self) -> CompetitiveTier:
        """_summary_
        Interface to the CompetitiveTier APIs

        Returns:
            Valorant: _description_
        """
        return self._competitive_tier