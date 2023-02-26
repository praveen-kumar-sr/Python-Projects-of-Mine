import io
with io.open('/Users/porchezhiyan/Downloads/149.txt', 'r', encoding='ISO-8859-1') as file:
    text = file.read()
    text0 = text.split() 
    
# finding number of sentences
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

import io
with io.open('/Users/porchezhiyan/Downloads/149.txt', 'r', encoding='ISO-8859-1') as file:
    text = file.read()
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)
    print(num_sentences) 

#convert list of paragraphs into string
text0 = str(text)
print(text0) 

#tokenizing text0
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize 

tokens = word_tokenize(text0) 

print(tokens) 

#finding number of words in text0 by removing punctuations
import re

# Use regular expression to remove all punctuation marks
string = re.sub(r'[^\w\s]','',text0)

# Split the string into a list of words
words = string.split()

# Find the number of words
num_words = len(words)

print("Number of words:", num_words)

#reading stop words
with open("/Users/porchezhiyan/Desktop/Black Coffer/StopWords/StopWords_Auditor.txt", "r") as file1:
    text1 = file1.read() 
    words1 = text1.split()
try:
    with open("/Users/porchezhiyan/Desktop/Black Coffer/StopWords/StopWords_Currencies.txt", "r",encoding='ISO-8859-1') as file2:
        text2 = file2.read()
        words2 = text2.split()
except UnicodeDecodeError:
    print("The file could not be read using the specified encoding format")  
    
with open("/Users/porchezhiyan/Desktop/Black Coffer/StopWords/StopWords_DatesandNumbers.txt", "r") as file3:
    text3 = file3.read() 
    words3 = text3.split()
with open("/Users/porchezhiyan/Desktop/Black Coffer/StopWords/StopWords_Generic.txt", "r") as file4:
    text4 = file4.read() 
    words4 = text4.split()
with open("/Users/porchezhiyan/Desktop/Black Coffer/StopWords/StopWords_GenericLong.txt", "r") as file5:
    text5 = file5.read() 
    words5 = text5.split()
with open("/Users/porchezhiyan/Desktop/Black Coffer/StopWords/StopWords_Geographic.txt", "r") as file6:
    text6 = file6.read() 
    words6 = text6.split()
with open("/Users/porchezhiyan/Desktop/Black Coffer/StopWords/StopWords_Names.txt", "r") as file7:
    text7 = file7.read() 
    words7 = text7.split()
    

# Using the extend() method to add all stop words
result = []
result.extend(words1)
result.extend(words3)
result.extend(words4)
result.extend(words5)
result.extend(words6)
result.extend(words7)

text_after_cleaning = []
for elem in tokens:
    if elem not in result:
        text_after_cleaning.append(elem)
total_words_after_cleaning = len(text_after_cleaning) 
print(text_after_cleaning) 

#reading positive and negative words
with open("/Users/porchezhiyan/Desktop/Black Coffer/positive-words.txt", "r") as file:
    content = file.read()
positive_words = content.split()


try:
    with open("/Users/porchezhiyan/Desktop/Black Coffer/negative-words.txt", "r",encoding='ISO-8859-1') as file:
        contents = file.read()
        negative_words = contents.split()  
except UnicodeDecodeError:
    print("The file could not be read using the specified encoding format")    
    
#calculating positive and negative scores  
positive_score = 0
negative_score = 0

for word in text_after_cleaning:
    if word in positive_words:
        positive_score += 1
    elif word in negative_words:
        negative_score -= 1

negative_score = negative_score * -1 

print("positive_score:",positive_score)
print("negative_score:",negative_score)  

#calculating polarity and subjectivity scores
polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)

print("polarity_score:",polarity_score) 

subjectivity_score = (positive_score + negative_score) / ((total_words_after_cleaning) + 0.000001)
    
print("subjectivity_score:",subjectivity_score)
    
#calculating complex word count
from nltk.corpus import cmudict
nltk.download('cmudict')

# Create a dictionary of syllable counts for each word
d = cmudict.dict()

# Initialize a count variable
complex_word_count = 0

# Iterate through the list of tokens
for token in tokens: 
   try:
        # Get the number of syllables in the token
        syllable_count = len(d[token][0])
        # If the syllable count is greater than 2, increment the count variable
        if syllable_count > 2:
            complex_word_count += 1
   except KeyError:
       pass 
   
print("complex_word_count:",complex_word_count) 

#calculating Avg words per sentence
print("Average number of words per sentence:", num_words/num_sentences) 
        
#calculating number of Personal Pronouns

import re

# Use regular expressions to find the counts of personal pronouns
i_count = len(re.findall(r'\bI\b', text0))
we_count = len(re.findall(r'\bwe\b', text0))
my_count = len(re.findall(r'\bmy\b', text0))
ours_count = len(re.findall(r'\bours\b', text0))
us_count = len(re.findall(r'\bus\b', text0)) 
text = re.sub(r'\bUS\b', '', text0) 

# Print the counts
print("I: ", i_count)
print("we: ", we_count)
print("my: ", my_count)
print("ours: ", ours_count)
print("us: ", us_count) 

total_personal_pronouns = i_count + we_count + my_count + ours_count + us_count
print("Total personal pronouns:", total_personal_pronouns) 

#calculating avg word length
sum_of_characters = sum(len(word) for word in words) 
average_word_length = sum_of_characters/num_words 
print("Average word length:", average_word_length) 

def count_syllables(word):
    if len(word) == 0:
        return 0
    
    word = word.lower()
    vowels = "aeiouy"
    count = 0
    if word[-1] in "esed":
        word = word[:-1]
    if word[-2:] in ["ed", "es", "e"]:
        word = word[:-2]
    if word[-3:] == "ing":
        word = word[:-3]
    if word[-2:] == "ly":
        word = word[:-2]
    if word[-3:] == "ing":
        word = word[:-3]
    for index in range(1, len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count += 1
    if len(word) == 0:
        return 0
    if word[-1] in "e":
        count -= 1
    if count == 0:
        count += 1
    return count 

total_syllables = 0
num_words = 0
for word in tokens:
    if len(word) == 0:
        continue
    num_words += 1
    num_syllables = count_syllables(word)
    total_syllables += num_syllables 

average_syllables_per_word = total_syllables / num_words 
print("Average syllables per word:", average_syllables_per_word)


average_syllables_per_word = total_syllables / num_words 
print("Average syllables per word:", average_syllables_per_word)  


average_syllables_per_word = total_syllables / num_words 
print("Average syllables per word:", average_syllables_per_word)  


# Find average sentence length
avg_sentence_length = num_words / num_sentences 
 
# Find percentage of complex words
percent_complex_words = complex_word_count/num_words  
print(percent_complex_words)

# Calculate fog index
fog_index = 0.4 * (avg_sentence_length + percent_complex_words)
print("Fog index:", fog_index)


print("Results:")
print("positive_score:",positive_score)
print("negative_score:",negative_score)  
print("polarity_score:",polarity_score) 
print("subjectivity_score:",subjectivity_score) 
print("Average sentence length:",avg_sentence_length) 
print("percentage of complex words:", percent_complex_words*100) 
print("Fog index:", fog_index)
print("Average number of words per sentence:", num_words/num_sentences)
print("complex_word_count:",complex_word_count)  
print("word count:",len(text_after_cleaning))
print("Average syllables per word:", average_syllables_per_word) 
print("Total personal pronouns:", total_personal_pronouns)  
print("Average word length:",average_word_length)
 


print("RESULTS:")
print(positive_score)
print(negative_score)  
print(polarity_score) 
print(subjectivity_score) 
print(avg_sentence_length)  
print(percent_complex_words)  
print(fog_index)
print(num_words/num_sentences) 
print(complex_word_count)  
print(len(text_after_cleaning))
print(average_syllables_per_word) 
print(total_personal_pronouns)   
print(average_word_length) 



