import pytest
from ..src.apis import Buddies

class TestClass:
    buddies = Buddies()

    def test_buddies_all(self, instance=buddies):
        response = instance.all()
        assert response != None

    def test_buddies_uuid(self, instance=buddies, uuid="dce731f8-4560-5f30-6eb5-8ab2e36864ec"):
        response = instance.by_uuid(uuid)
        assert response != None