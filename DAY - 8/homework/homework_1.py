# შექმენით სია, ამ სიაში ჩაწერეთ სხვადასხვა ციფრები (1, 2, 3, 4, ასე არა, რამე მაგ: 45, 23, 87, 55,) და გამოიტანეთ ამ სიაში ყველა რიცხვის ჯამი, ასევე ამავე სიიდან უნდა დაპრინტოთ ყველა რიცხვი ცალ ცალკე, და მიუწეროთ ლუწია თუ კენტი.


my_arr = [45, 56, 67, 89, 105, 724, 24, 17]

# დაპრინტეთ ყველა რიცხვი ცალ ცალკე და მიუწეროთ ლუწია თუ კენტი.
for i in range(len(my_arr)):
  if my_arr[i] % 2 == 0:
    print(str(my_arr[i]) + " is even")
  else:
    print(str(my_arr[i]) + " is odd")
  
#ჯამი 
print(f"sum of this numbers is :{ sum(my_arr)}")
