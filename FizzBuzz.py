#1~100까지의 숫자를 출력하는데,
#3의 배수는 Fizz
#5의 배수는 Buzz
#3의 배수이면서 5의 배수는 FizzBuzz가 출력되도록 해보자.

#while문
a = 1
while a <= 100:
	if a % 3 == 0:
		if a%5==0:
			print("FizzBuzz")
			a += 1
			continue
		else:
			print("Fizz")
			a += 1
			continue
	elif a % 5 == 0:
		if a%3==0:
			print("FizzBuzz")
			a += 1
			continue
		else:
			print("Buzz")
			a += 1
			continue
	else:
		print(a)
		a += 1
print("===========================")

#for문
for b in range(1,101):
	if b%3 == 0 and b%5 == 0:
		print("FizzBuzz")
	elif b%3 == 0:
		print("Fizz")
	elif b%5 == 0:
		print("Buzz")
	else:
		print(b)
