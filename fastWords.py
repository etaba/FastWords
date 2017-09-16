from random import randint

#settings
LENGTH = 10
CAPITAL = True
#SPECIAL_CHAR = False
NUMBER = True
BOTH_HANDS = True
RIGHT_ONLY = False 
LEFT_ONLY = False


rightHanded1=	" jkli"
rightHanded2=	"h;nou "
leftHanded1=	" sdfe"
leftHanded2=	"atvwr"
friends = {
	'a':rightHanded1+rightHanded2+"dfgvs0",
	#'b':"a"+rightHanded1,
	'c':rightHanded1+rightHanded2+"sa0",
	'd':rightHanded1+rightHanded2+"asf0",
	'e':rightHanded1+rightHanded2+"fv0",
	'f':rightHanded1+rightHanded2+"asde0",
	'g':rightHanded1+rightHanded2+"sa0",
	'h':leftHanded1+leftHanded2+"o",
	'i':leftHanded1+leftHanded2+"j",
	'j':leftHanded1+leftHanded2+"l;k",
	'k':leftHanded1+leftHanded2+"lj;n",
	'l':leftHanded1+leftHanded2+"mk;",
	'm':leftHanded1+leftHanded2+"lk",
	'n':leftHanded1+leftHanded2+"l;",
	'o':leftHanded1+leftHanded2+"nmjh",
	'p':leftHanded1+leftHanded2+"jm",
	#'q':rightHanded1,
	'r':rightHanded1+rightHanded2+"s",
	's':rightHanded1+rightHanded2+"fdargt",
	't':rightHanded1+rightHanded2+"w",
	'u':leftHanded1+leftHanded2+"oil",
	'v':rightHanded1+rightHanded2+"as",
	'w':rightHanded1+rightHanded2+"fga",
	#'x':rightHanded1,
	#'y':leftHanded1,
	#'z':rightHanded1,	
}
numberFriends = {
	'a':"9078",
	'c':"9078",
	'd':"9078",
	'e':"9078",
	'f':"9078",
	'g':"9078",
	'h':"234",
	'i':"234",
	'j':"234",
	'k':"234",
	'l':"234",
	'm':"234",
	'n':"234",
	'o':"234",
	'p':"234",
	'r':"9078",
	's':"9078",
	't':"9078",
	'u':"234",
	'v':"9078",
	'w':"9078",
}

def generateFastWordList(filename):
	wordsTxt = open(filename,'r')
	words = wordsTxt.readlines()
	fastWords = open("fast"+filename,'w+')
	if BOTH_HANDS:
		goodLetters = rightHanded1+leftHanded1
	elif RIGHT_ONLY:
		goodLetters = rightHanded1+rightHanded2
	elif LEFT_ONLY:
		goodLetters = leftHanded1+leftHanded2
	for word in words:
		if len(word) > 2:
			if word[0] in goodLetters:
				for i in range(len(word)-2):
					if word[i+1] in friends[word[i]]:
						if i == len(word)-3:
							fastWords.write(word)
					else:
						break;
	fastWords.close()

#subsequent words flow together
def fastWord(filename):
	fastWordsTxt = open(filename,'r')
	fastWords = fastWordsTxt.readlines()
	if CAPITAL:
		if BOTH_HANDS:
			goodLetters = leftHanded1 + leftHanded2
		elif RIGHT_ONLY:
			goodLetters = "juklmnhilp"
		elif LEFT_ONLY:
			goodLetters = "fsdrtegv"
		capitalWords = filter(lambda x: x[0] in goodLetters,fastWords)
		fastWord = capitalWords[randint(0,len(capitalWords)-1)].strip()
		fastWord = fastWord[0].upper()+fastWord[1:]
	else:
		fastWord = fastWords[randint(0,len(fastWords)-1)].strip()
	while len(fastWord) < LENGTH:
		nextMatches = filter(lambda x: x[0] in friends[fastWord[-1]],fastWords)
		fastWord += nextMatches[randint(0,len(nextMatches)-1)].strip()
	if NUMBER: #append number to end
		if BOTH_HANDS:
			goodNumbers = numberFriends[fastWord[-1]]
		elif RIGHT_ONLY:
			goodNumbers = "7890"
		elif LEFT_ONLY:
			goodNumbers = "1245"
		fastWord += goodNumbers[randint(0,len(goodNumbers)-1)]
	return fastWord

generateFastWordList('commonWords.txt')
generateFastWordList('words.txt')
print "\n\n"
print "FastWord: ",fastWord('fastwords.txt')
print "Common FastWord: ",fastWord('fastcommonWords.txt')
print "Common FastWord: ",fastWord('fastcommonWords.txt')
print "Common FastWord: ",fastWord('fastcommonWords.txt')
print "Common FastWord: ",fastWord('fastcommonWords.txt')
print "Common FastWord: ",fastWord('fastcommonWords.txt')
print "\n\n"