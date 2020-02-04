sentense = input("문장을 입력해보세요. for 2-gram")

#sentense = "My name is Pudal"
b = sentense.split()

for i in range(len(b)-1):
	print(b[i], end=' ')
	print(b[i+1])
