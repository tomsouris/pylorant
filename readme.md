# Pylorant

##### Pylorant is a simple Python Wrapper for the Valorant-API https://valorant-api.com

##### Pylorant is powered by pydantic and supports typehints
### Usage:

```python
from src.ApiClient import ApiClient
from rich import print

val = ApiClient()

agent = val.agent.by_uuiid("add6443a-41bd-e414-f6ad-e58d267f4e95")
print(agent)
```

```sh
$ uuid='add6443a-41bd-e414-f6ad-e58d267f4e95' displayName='Jett' description="Representing her home country of South Korea, Jett's agile and evasive fighting 
style lets her take risks no one else can. She runs circles around every skirmish, cutting enemies up before they even know what hit them." 
developerName='Wushu' displayIcon='https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/displayicon.png' 
displayIconSmall='https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/displayiconsmall.png' 
bustPortrait='https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/bustportrait.png' 
fullPortrait='https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/fullportrait.png' 
killfeedPortrait='https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/killfeedportrait.png' 
assetPath='ShooterGame/Content/Characters/Wushu/Wushu_PrimaryAsset' 
background='https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/background.png' isFullPortraitRightFacing=False 
isPlayableCharacter=True isAvailableForTest=True isBaseContent=True role=Role(uuid='dbe8757e-9e92-4ed4-b39f-9dfc589691d4', displayName='Duelist', 
description='Duelists are self-sufficient fraggers who their team expects, through abilities and skills, to get high frags and seek out engagements first.', 
displayIcon='https://media.valorant-api.com/agents/roles/dbe8757e-9e92-4ed4-b39f-9dfc589691d4/displayicon.png', 
assetPath='ShooterGame/Content/Characters/_Core/Roles/Assault_PrimaryDataAsset') abilities=[Abilities(slot='Ability1', displayName='Updraft', 
description='INSTANTLY propel Jett high into the air.', 
displayIcon='https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/abilities/ability1/displayicon.png'), Abilities(slot='Ability2', 
displayName='Tailwind', description='INSTANTLY propel Jett in the direction she is moving. If Jett is standing still, she will propel forward.', 
displayIcon='https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/abilities/ability2/displayicon.png'), Abilities(slot='Grenade', 
displayName='Cloudburst', description='INSTANTLY throw a projectile that expands into a brief vision-blocking cloud on impact with a surface. HOLD the 
ability key to curve the smoke in the direction of your crosshair.', 
displayIcon='https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/abilities/grenade/displayicon.png'), Abilities(slot='Ultimate', 
displayName='Blade Storm', description='EQUIP a set of highly accurate throwing knives. FIRE to throw a single knife and recharge knives on a kill. ALTERNATE
FIRE to throw all remaining daggers but does not recharge on a kill.', 
displayIcon='https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/abilities/ultimate/displayicon.png'), Abilities(slot='Passive', 
displayName='Drift', description='Holding the jump button while falling allows you to glide through the air.', 
displayIcon='https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/abilities/passive/displayicon.png')] 
voiceLine=VoiceLine(minDuration=1, maxDuration=1, mediaList=[MediaList(id=878055936, wwise='https://media.valorant-api.com/sounds/878055936.wem', 
wave='https://media.valorant-api.com/sounds/878055936.wav')])
manifestId='3E974F4C797C4EB1' branch='release-04.03' version='04.03.00.671292' buildVersion='6' riotClientVersion='release-04.03-shipping-6-671292' 
buildDate=datetime.datetime(2022, 2, 14, 0, 0, tzinfo=datetime.timezone.utc)
```

#### The Package is still in beta 


