#Chapter 6: Manipulating Strings

#challenge 1
string = 'Camus'

print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])

#challenge 2

response_one = input('something you write')
response_two = input('someone you trust')

answer = 'Yesterday I wrote a {}. I sent it to {}!'.format(response_one, response_two)
print(answer)

#challenge 3

fact = 'aldous Huxley was born in 1894.'.Capitalize()

print(fact)

#challenge 4
newlist = 'Where now? Who now? When now?'.split('?')
print(newlist)


#Challenge 5

words = ['The',
         'fox',
         'jumped',
         'over',
         'the',
         'fence',
         '.']

string4 = " ".join(words)
string5 = string4[0:-2] + '.'

print(string5)

#Challenge 6

sentence = 'A screaming comes across the sky.'
new_sentence = sentence.replace('s', '$')
print(new_sentence)

#Challenge 7

author = 'Hemingway'
first_m = author.index('m')
print(first_m)

#Challenge 8

quote1 = '\'The first rule about fight club is we don\'t talk about fight club\' asserted Tyler'

print(quote1)

#Challenge 9

concat = 'three ' + 'three ' + 'three'
print(concat)

multiplier = 'Three '*3
print(multiplier)

#Challenge 10
starter = 'It was a bright cold day in April, and the clocks were striking thirteen.'
ch10 = starter[0:33]
print(ch10)

