from ..base import BaseRequest
from ..config import BaseRequestConfig
from ..mixins import UrlBuilder, Validator
from ..models import AgentModel
from marshmallow.exceptions import ValidationError


class Agent(BaseRequest):
    def __init__(self):
        self.base_url = BaseRequestConfig.base_url
        super().__init__()

    def all(self) -> AgentModel:
        """_summary_
            Returns data and assets of all agents and their abilities
        Returns:
            _type_: json 
        """
        url = UrlBuilder.url(self.base_url, "/agents")
        response = BaseRequest.get(self, url)
        model    = AgentModel

        return Validator.Validate(model=model, response=response)
    
    def by_uuiid(self, agentUuid) -> AgentModel:
        """_summary_
            Returns data and assets of one agent
        Args:
            agentUuid (string): UUID of Agent

        Returns:
            _type_: json
        """
        url      = UrlBuilder.url(self.base_url, f'/agents/{agentUuid}')
        response = BaseRequest.get(self, url)
        model    = AgentModel

        return Validator.Validate(model=model, response=response)