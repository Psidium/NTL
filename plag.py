from docx import Document
from pygoogle import pygoogle

if __name__ == "__main__":
    if sys.args[0] == 0:
        print("Must specify file!")
        pass # return was crashing the program
    #open the docx (and docx only)
    document = Document(sys.args[0])
    #for each paragraph on the docx
    for parag in document.paragraphs:
        #extract the string
        text = parag.text
        #split at whitespace
        splitted = text.split(' ', 10) # in this case, 10 words
        #send to google every 5~10 words and save the url
        #of the first Y results (parallelism preferrable, bandwidth is not a big problem,
        #the old http protocol is)
        ssearch = ''.join(splitted)
        print ssearch
        g = pygoogle(ssearch)
        g.pages = 5
        # g.get_result_count() will give the number of results
        g.get_urls()   # returns a list of found urls, can be used for counting later



    #count the ocurrences of each URL
    #create a ratio based on the size of the document and the times an URL can appear


    #if a given URL goes beyond that ratio, it's plagiarized
