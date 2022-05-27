# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
  with open("story.txt" , "r") as file:
    story = file.read()
    return ("""Once upon a time a psychology professor walked around on a stage while teaching stress management principles to an auditorium filled with students.  
As she raised a glass of water, everyone expected they would be asked the typical glass half empty or glass half full question.  
Instead, with a smile on her face, the professor asked, How heavy is this glass of water I am holding?""")

read_file_content("story.txt")



def count_words():
    text = read_file_content("./story.txt")
    count = dict()

   
    text = text.split()
    for word in text:
        if word in count:
            count[word] +=1
        else:
            count[word] = 1   
    return count         
print(count_words())


"""I'd appreciate if there'll be correction as feedback because I don't understand this"""
  

  