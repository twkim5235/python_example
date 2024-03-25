import animal

나비 = animal.Cat()
# 나비.cry()

호돌이 = animal.Tiger()
# 호돌이.cry()

수호랑 = animal.Tiger()
# 수호랑.cry()

print(f"나비는 고양이 입니까?: {isinstance(나비, animal.Cat)}")
print(f"나비는 호랑 입니까?: {isinstance(나비, animal.Tiger)}")
print(f"나비는 동물 입니까? {isinstance(나비, animal.Animal)}")
print(f"나비는 고양이과 입니까?: {isinstance(나비, animal.Feline)}")

print(f"고양이는 고양이과 입니까?: {issubclass(animal.Cat, animal.Feline)}")
print(f"고양이는 동물 입니까?: {issubclass(animal.Cat, animal.Animal)}")

보비 = animal.Feline()
보비.cry()

