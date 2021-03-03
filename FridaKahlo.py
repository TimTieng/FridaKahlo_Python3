# Task 1 - Create a list with the given FK paintings
paintings = {'The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait with Monkeys'}
print(paintings)

# Task 2 - Create a list of the date of creation for previous paintings
dates = {1939, 1933, 1946, 1940}
print(dates)

# Combine two lists
paintings = list(zip(paintings, dates))
print(paintings)

# Add new values to the list
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))

print(paintings)

# Find length of the paintings list
listLength = len(paintings)
print(listLength)

# generate a list of numbers from 1 - Len(paintings) to assign id values
audioTourNumber = list(range(1,listLength+1))
print(audioTourNumber)

# Zip new index values to paintings
masterList = list(zip(audioTourNumber, paintings))
print(masterList)
