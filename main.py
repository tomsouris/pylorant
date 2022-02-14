from src.ApiClient import ApiClient
from rich import print


val = ApiClient()
# val.agent.by_uuiid("add6443a-41bd-e414-f6ad-e58d267f4e95")
# print(agent)

# buddies = val.buddies.all()
# print(buddies)
# for bud in buddies:
#     for k, v in bud.items():
#         print(f'Key: {k} --- Value: {v}')
#     print("\n")
test = val.buddies.by_uuid("dce731f8-4560-5f30-6eb5-8ab2e36864ec")
# print(test.json())
# val.buddies.levels()

levels = val.buddies.levels_by_uuid("671e7df6-41fa-9801-3f37-14864d2fc7cc")
print(levels.uuid)

# print(levels)
# print(buddie_level)