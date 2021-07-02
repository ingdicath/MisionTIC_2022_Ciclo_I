#
# Created by Diana Salamanca on 02-Jun-2021
#

def find_stage(age):
  stage = ""
  if 0 <= age <= 20:
    stage = "uno"
  elif 21 <= age <= 30:
    stage = "dos"
  elif 31 <= age <= 50:
    stage = "tres"
  else:
    stage = "cuatro"
  return stage

paco_age = int(input())
hugo_age = int((2 * paco_age) + 4)
luis_age = int((hugo_age + paco_age) / 5)
print(str(paco_age) + " " + str(hugo_age) + " " + str(luis_age))
print(find_stage(luis_age))
