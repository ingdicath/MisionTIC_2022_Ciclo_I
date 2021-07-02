#
# Created by Diana Salamanca on 01-Jul-2021
#

import json

valid_chords = json.loads(input())
player_chords = input().split('-')
coincidences = list()
player_score = int()

for chord in player_chords:
    if chord in valid_chords:
        coincidences.append(chord)
        player_score += valid_chords[chord]

print(player_score)
print(",".join(coincidences))
