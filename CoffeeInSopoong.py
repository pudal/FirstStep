import random

print("소풍 커피빵 주사위 대결입니다.\n6이 나올 때까지 계속 주사위를 굴리면서 획득한 숫자들을 합산하고\n6이 나오는 순간 주사위 굴리기를 멈춥니다.")
name = input('소풍 커피빵 대결 참가자 이름을 입력하세요.')
a = 0
i = 0

while i <= 5:
	i = random.randint(1,6)
	if i != 6:
		print(i, "획득! 다시 굴립니다.")
		a += i
		print("현재까지 누적 점수는", a, "점 입니다.")
	else:
		print(i, "획득! 주사위 굴리기를 멈춥니다.")
		a += i
	
print(name, "님이 획득한 숫자의 총합은", a, "입니다.")
