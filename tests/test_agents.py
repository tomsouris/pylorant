import pytest
from ..src.apis import Agent

class TestClass:
    agent = Agent()

    def test_agent_all(self, agent=agent):
        response = agent.all()
        assert response != None

    def test_agent_uuid(self, agent=agent, uuid="add6443a-41bd-e414-f6ad-e58d267f4e95"):
        response = agent.by_uuid(uuid)
        assert response != None