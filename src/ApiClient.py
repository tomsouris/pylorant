from src.apis.Currencies import Currencies
from .apis import (Agent, Buddies, Bundles, Ceremonies, CompetitiveTier,
                    ContentTiers, Contracts, Currencies)


class ApiClient():
    def __init__(self) -> None:
        self._agent            = Agent()
        self._buddies          = Buddies()
        self._bundles          = Bundles()
        self._ceremonies       = Ceremonies()
        self._competitive_tier = CompetitiveTier()
        self._content_tier     = ContentTiers()
        self._contracts        = Contracts()
        self._currencies       = Currencies()

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

    @property
    def contentTier(self) -> ContentTiers:
        """_summary_
        Interface to the ContentTiers APIs

        Returns:
            Valorant: _description_
        """
        return self._content_tier
        
    @property
    def contracts(self) -> Contracts:
        """_summary_
        Interface to the Contracts APIs

        Returns:
            Valorant: _description_
        """
        return self._contracts

    @property
    def currencies(self) -> Currencies:
        """_summary_
        Interface to the Currencies APIs

        Returns:
            Valorant: _description_
        """
        return self._currencies