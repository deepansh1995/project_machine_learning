import sys
import os.path
import codecs
import time
import re


from urlparse import urlparse
from bs4 import BeautifulSoup, Comment

reload(sys)

sys.setdefaultencoding("utf-8")

def clean(soup):
    comments = soup.findAll(text=lambda text:isinstance(text,Comment))
    [comment.extract() for comment in comments]
    for s in soup(['script', 'style']):
        s.extract()
    return ' '.join(soup.stripped_strings)

def getWordCount(word):
	if(len(word) == 0):
		return 0
	count = len(re.findall(r'\w+', word))
	return count

def htmlLength(word):
	if(len(word) == 0):
		return 0
	return (len(word) - getWordCount(word))

def AvgWordLength(word):
	if(len(word) == 0):
		return 0
	wordList = re.sub("[^\w]", " ",  word).split()
	c = 0
	size = len(wordList)
	for i in range(1, size):
		c = c+len(wordList[i])
	if(size > 0):
 		return c/size
	return 0

def func(rootdir, CSV):
	for root, subFolders, files in os.walk(rootdir):
                for i in files:
                    content_variable=""
                    with open(os.path.join(rootdir,i),'r') as fin:
                        for lines in fin:
                            content_variable = content_variable + lines
                        fin.close()
                    soup = BeautifulSoup(content_variable,'html.parser')
                    if not soup.title == None: 
                        fileTitle = soup.title.string
                    else:
                        fileTitle = i
                    #print i+", "+fileTitle+"\n"
                    word_count = getWordCount(content_variable)
                    HtmlLength = htmlLength(content_variable)
                    Avg_word_len = AvgWordLength(content_variable)
                    if(len(str(fileTitle)) and len(str(word_count)) and len(str(HtmlLength)) and len(str(Avg_word_len))):
                            CSV.write(str(word_count)+", "+str(HtmlLength)+", "+str(Avg_word_len)+", "+str(i)+"\n")        
                    #content_variable = clean(soup)


CSV = open("spam_training.csv", 'a')
rootdir = "./non-spam/training/"
#rootdir = "/Desktop/project/non-spam/test/"
func(rootdir, CSV)
CSV.close()
print ("CSV created for testing data")
