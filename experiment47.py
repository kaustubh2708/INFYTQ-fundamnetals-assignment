#PF-Assgn-47
vow=['a','e','i','o','u','A','E','I','O','U']
def encrypt_sentence(sentence):
	l=[]
	list1=sentence.split(" ")
	for i in range (0,len(list1)):
		word=list1[i]
		if((i+1)%2!=0):
			l.append(word[::-1])
		else:
			vowel=[]
			consonant=[]
			for i in word:
				if i in vow:
					vowel.append(i)
				else:
					consonant.append(i)
			consonant.extend(vowel)
			l.append("".join(consonant))
	
	return " ".join(l)

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)