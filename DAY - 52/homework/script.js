//სამკუთხედის ტოლობის ნიშნები და სამკუთხედის ვალიდურობის დადგენა

// we must take three page of triangle and also three corner. 
//three pages: a, b, c
//if triangle is valid it means that: a+b>c & b+c>a & a+c>b

let a=3
let b=9
let c=6
if(a+b>c && a+c>b && b+c>a){
  console.log('Triangle is valid')
}else{
  console.log('please try other numbers')
}




//We have three facts:
// 1. three apples are 24
// 2. one apple and two Cherry are 20
// 3. two apple, one Cherry and 3 lemone are 31
    // please count one lemone + 4 Cherry - 1 apple 

let apple = 24/3
let Cherry = (20-24/3)/2
let lemone = (31-16-6)/3
console.log(lemone + 4 * Cherry - apple)


