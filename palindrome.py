word= input("단어를 입력해보세요")

result = True
for i in range(len(word)):
	if word[i] != word[-1-i]:
		result = False
	break

print(result)
