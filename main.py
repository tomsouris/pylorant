from src.ApiClient import ApiClient
from rich import print

val = ApiClient()

agent = val.agent.by_uuid("add6443a-41bd-e414-f6ad-e58d267f4e95")
print(agent)

# buddies = val.buddies.all()
# print(buddies[0].uuid)
# print(buddies)
# for bud in buddies:
#     for k, v in bud.items():
#         print(f'Key: {k} --- Value: {v}')
#     print("\n")
# test = val.buddies.by_uuid("dce731f8-4560-5f30-6eb5-8ab2e36864ec")
# print(test.json())
# print(val.buddies.levels())

# levels = val.buddies.levels_by_uuid("671e7df6-41fa-9801-3f37-14864d2fc7cc")
# print(levels.uuid)

# print(levels)
# print(buddie_level)


# bundles = val.bundles.all()
# print(bundles[0].assetPath)

# bundles_uuid = val.bundles.by_uuid("4e3a244b-4482-0541-3eab-b8912cdb72d6")
# print(bundles_uuid)

# ceremonies = val.ceremonies.all()
# print(ceremonies)

# ceremonies = val.ceremonies.by_uuid("87c91747-4de4-635e-a64b-6ba4faeeae78")
# print(f'-----> {ceremonies}')

# print(val.competitiveTier.all())
# print(val.contentTier.all())
# print(val.contentTier.by_uuid("564d8e28-c226-3180-6285-e48a390db8b1"))

# print(val.contracts.all())
# contracts = val.contracts.by_uuid("bfb8160e-eee0-46b1-a069-16f93adc7328")
# print(val.currencies.by_uuid("e59aa87c-4cbf-517a-5983-6e81511be9b7"))

# print(val.events.all())
# print(f'---->', val.events.by_uuid("cee09894-41d6-7000-848b-ea9de6c28f44"))

# print(val.gamemodes.all())
# print(val.gamemodes.by_uuid("57038d6d-49b1-3a74-c5ef-3395d9f23a97"))

# print(val.gear.all())

# print(val.maps.all())
# print(val.maps.by_uuid("2bee0dc9-4ffe-519b-1cbd-7fbe763a6047"))
# print(val.playercards.all())
# print(val.playercards.by_uuid("a75c951f-4822-f85d-44ed-709e413aa5f8"))

# print(val.seasons.by_uuid("808202d6-4f2b-a8ff-1feb-b3a0590ad79f"))

# print(val.seasons.competitive_by_uuid("8d9e3688-470b-c0e0-5b20-ca964d907adb"))
# print(val.sprays.all())
# print(val.sprays.levels_all())

# print(val.themes.by_uuid("def525c9-4151-ab71-5a18-c7bff46d4e46"))
# xxx = val.weapons.all()
# print(xxx[0].weaponStats.adsStats.zoomMultiplier)

# print(val.weapons.by_uuid("63e6c2b6-4a8e-869c-3d4c-e38355226584"))
# print(val.weapons.skins_all())
# print(val.weapons.skins_chroma_by_uuid("0b30b3e8-4696-7b7c-fed2-50b34234965a"))

# print(val.weapons.skins_levels_by_uuid("b577585f-4171-19a1-2899-848460de8089"))
print(val.version.current())