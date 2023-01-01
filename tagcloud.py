import sys

MIN_FONT = 11
MAX_FONT = 48
FONT_RANGE = 37

def writeHTML(words, wordsList, output, filename):

    output.write('<html>\n\t<head>\n\t\t<title>Top '+str(len(wordsList))+' words in '+filename+'</title>\n')
    output.write('\t\t<link href="data/tagcloud.css" rel="stylesheet" type="text/css">\n')
    output.write('\t<head>\n')

    topValues = [words[word] for word in wordsList]

    minVal = min(topValues)
    maxVal = max(topValues)
    output.write('<body>\n')
    output.write('\t\t<h2>Top '+str(len(wordsList))+' words in '+filename+'</h2>\n')
    output.write('\t\t<hr>\n')
    output.write('\t\t<div class="cdiv">\n')
    output.write('\t\t\t<p class="cbox">\n')
    
    for word in wordsList:
        freq = words[word]
        fontSize = MIN_FONT
        if maxVal == minVal:
            fontSize = FONT_RANGE // 2
        else:
            scale = (freq-minVal)/(maxVal-minVal)
            fontSize = int(fontSize+(scale*FONT_RANGE))
        spanStr = '\t\t\t\t<span style="cursor:default" class="f'+str(fontSize)+'" title="count: '+str(freq)+'">'+word+'</span>\n'
        output.write(spanStr)

    output.write('\t\t</div>\n')
    output.write('\t</body>\n')
    output.write('</html>\n')

filename = input("Type the relative path of the file to read: ")
try:
    f = open(filename, "r")
except:
    print('Error opening file. Most likely, this means the file does not exist or the path was entered incorrectly.\nExiting...', file=sys.stderr)
    sys.exit()
lines = f.readlines()
words = {}

for line in lines:
    temp_string = line.replace('\t',' ').replace('\n',' ').replace('\r',' ').replace('-',' ').replace('.',' ').replace('!',' ').replace('?',' ') \
                  .replace('[',' ').replace(']',' ').replace(';',' ').replace(':',' ').replace('/',' ').replace('(',' ').replace('`',' ').replace(')',' ').replace('\'',' ') \
                  .replace('"',' ').replace(',',' ')
    temp_words = temp_string.split()
    for word in temp_words:
        wordKey = word.lower()
        if wordKey in words:
            words[wordKey] += 1
        else:
            words[wordKey] = 1
f.close()

o = input("Type output filename: ")
try:
    f = open(o,"w")
except:
    print('Error creating output file. The filesystem could possibly be read-only.\nExiting...', file=sys.stderr)
    sys.exit()
numWords = int(input('There are '+str(len(words))+' unique words in this file. Enter number of words desired for the tag cloud: '))

while numWords > len(words):
    numWords = int(input('There are '+str(len(words))+' unique words in this file. Enter number of words desired for the tag cloud: '))

topWords = sorted(words, key=words.get, reverse=True)[:numWords]
writeHTML(words, topWords, f, filename)
print('HTML file written to',o)
f.close()

            

