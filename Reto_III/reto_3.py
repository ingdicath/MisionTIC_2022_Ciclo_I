#
# Created by Diana Salamanca on 25-Jun-2021
#

chords = input().upper().split(',')
j = 1
count = 1
final_chord = ""
final_count = ""

for i in range(len(chords) - 1):
    if chords[i] != chords[j]:
        final_chord += chords[i] + " "
        final_count += str(count) + " "
        count = 0
    count += 1
    j += 1

final_chord += chords[j - 1]
final_count += str(count)
print(final_chord)
print(final_count)
