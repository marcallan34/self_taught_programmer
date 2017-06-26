# Chapter 9 Challenges

import csv

#Challenge 1 (Print from another file on your computer)

my_file = []

with open('test.txt', 'r') as f:
    my_file.append(f.read())

print(my_file)

#Challenge 2 (write a program that asks the user a question and saves the answer to a file

answer = input("what's your name?")

with open('your_name.txt', 'w') as f:
    f.write(answer)

    
#Challenge 3 (take the items in this list of lists and write them to a csv file)

with open('test_movies.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(['Top Gun', 'Risky Business', 'Minority Report'])
    w.writerow(['Titanic', 'The Revenant', 'Inception'])
    w.writerow(['Training Day', 'Man on Fire', 'Flight'])

