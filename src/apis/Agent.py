from ..base import BaseRequest
from ..config import BaseRequestConfig
from ..mixins import UrlBuilder
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
        BaseRequest.get(self, url)
    
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
        try:
            return AgentModel().load(response["data"])
        except ValidationError as err :
            return err