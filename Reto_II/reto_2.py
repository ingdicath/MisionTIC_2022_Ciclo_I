#
# Created by Diana Salamanca on 10-Jun-2021
#

input_james = str(input().upper())
input_kirk = str(input().upper())
input_chords = str(input().upper())

score_james = 0
score_kirk = 0
output = ""

for i in input_chords:
    if i in input_james:
        score_james += 1
    if i in input_kirk:
        score_kirk += 1
    if score_james == score_kirk:
        output += 'L'
    elif score_james > score_kirk:
        output += 'J'
    else:
        output += 'K'
print(output)
