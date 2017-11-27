import os


# prints error message if total rubric weigh exeeds %100
# exits program
def error_check(weighTotal):
  if weighTotal > 100:
    print()
    print('Warning you have entered a total rubric weight of more than %100')
    print('             --------This does not jive--------')
    print()
    print('Please restart the utility and carefully enter your rubric weights')
    raise SystemExit

# each time this is called it prompts user for section
# name, weight, and score. This are appended to and array
# with is returned and appended to another array as elements
# of a two demension array
def returns_inner_list(innerList, num):
  os.system('clear')

  num += 1
  print('Input info for section ' + str(num))
  section = input('Section Name: ')
  innerList.append(section)

  weight = float(input(section + ' Weight: '))
  # increment static total weight
  returns_inner_list.totalWeight += weight
  # error check total weight
  error_check(returns_inner_list.totalWeight)

  innerList.append(weight)

  # also validate that score be no more than 100
  score = float(input(section + ' Score: '))
  innerList.append(score)

  # returned array becomes element of array of arrays
  return innerList


# print input data
# outputs contents of nested array
def print_data(nWeightedSections, outterList):

  for i in range(nWeightedSections):
    print ('Section ' + str(i+1))
    for j in range(3):
      if j == 0:
        print ('Section Name: ' + outterList[i][j])
      elif j == 1:
        print ('Weight: ' + str(outterList[i][j]))
      else:
        print ('Score: ' + str(outterList[i][j]))
    print()

returns_inner_list.totalWeight = 0

nWeightedSections = int(input('How many weighted sections: '))
print()

# array to hold arrays
outterList = []

for i in range(nWeightedSections):
  # dynamically create inner arrays
  innerList = []
  returns_inner_list(innerList, i)
  outterList.append(innerList)
  print()

os.system('clear')

print_data(nWeightedSections, outterList)


