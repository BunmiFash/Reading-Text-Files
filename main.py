# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
  with open("story.txt" , "r") as file:
    story = file.read()
    
    return story

read_file_content("story.txt")


import string
def count_words():
    text = read_file_content("story.txt")
    count = dict()

    text = text.lower()
    text = text.translate(str.maketrans('','', string.punctuation))
    text = text.split()
    for word in text:
        if word in count:
            count[word] +=1
        else:
            count[word] = 1   
    return count         
print(count_words())


