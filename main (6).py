# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

#Reads text and saves in draculaText
draculaText = readBook()

#Takes lowercase and split text and stores in words variable
words = draculaText.lower().split()

#Store words in list
wordStorage = {}
largest = 0
mostRepeatedWord = ""

#Loop through words and add them to dictionary. Keep count of their repeats. 
for word in words:
  #If word already in dictionary, then add 1 
  if word in wordStorage:
    wordStorage[word] += 1
  #If word not in dictionary, then set count equal to 1
  else:
    wordStorage[word] = 1

print("=== RESULTS ===")
print()

#Loop through items and get the word that appears the most throughout the text. 
for k,v in wordStorage.items():
  if(wordStorage[k] > largest):
    largest = v
    mostRepeatedWord = k 

print(f'\'{mostRepeatedWord}\' is the word that appears the most throughout the text, a total of {largest} times')

print()
# Count all the four letter words (do NOT include repeats)
fourLetterWords = []
for word in words:
  if(len(word) == 4 and word not in fourLetterWords):
    fourLetterWords.append(word)
print(f"There are {len(fourLetterWords)} words that are four letters long.")

print ()
print("I noticed that these words show up 500 or more times:")
#Loop through items and if value is greater than 500, print the word and # of repetitions
for k,v in wordStorage.items():
  if (v > 500):
    print (f"{k} : {v}")

print()

  
  


  

  







