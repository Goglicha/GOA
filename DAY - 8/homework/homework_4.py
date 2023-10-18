# GOA ში ყოველ შემოყვანილ ადამიანზე გეძლევა 100ლ.
# მომხმარებელს შემოატანინეთ თუ რამდენი ადამიანი შემოიყვანა ხოლო თითო შემოყვანილ ადამიანზე დაერიცხოს 100ლ
# 1) რამდენი დაგერიცხება თუ შემოიყვან 10 ბავშვს?  15 ბავშცს?
# 2) რამდენი დაგერიცხება თუ შემოიყვან 100 ბავშვს გამოკლებული 37 დამატებული 13 გაყოფილი 10 და გამრავებული 264 ზე

#1
num_1 =int(input ("how many persons will you bring in GOA?: "))

print(f"if you will bring {num_1} persons in GOA you will receive {num_1 * 100} GEL")

#2 
num_2 = 100 - 37 + 13 // 10 * 264
print(f"if you will bring {num_2} persons in GOA you will receive {num_2 * 100} GEL")
