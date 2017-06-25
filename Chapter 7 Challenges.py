#Chapter 7

#Challenge 1
shows = ['the walking dead', 'entourage', 'the sporanos', 'the vampire diaries']

for shows in shows:
    print(shows)

#Challenge 2
for i in range(25,51):
    print(i)

#Challenge 3
shows = ['the walking dead', 'entourage', 'the sporanos', 'the vampire diaries']

for index, show in enumerate(shows, start=1):
    print(index)
    print(show)

#Challenge 4
numbers = [4, 5, 17]

while True:
    a = input('Choose a number between 1 and 20 or type \'q\' to quit')
    if a == 'q':
        break
    try:
        a = int(a)
    except ValueError:
        print("please type a number or q to quit.")
        continue
    if a in numbers:
        print('You guessed correctly!')
    else:
        print('Sorry, try again')

#challenge 5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
product = []
for i in list1:
    for j in list2:
        product.append(i*j)

print(product)

