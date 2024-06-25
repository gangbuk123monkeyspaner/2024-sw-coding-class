coffee = 'May I have a large container of coffee right now'
coffee_words = coffee.split()  #분리하기
print(coffee_words)
coffee_words_len = [len(word) for word in coffee_words] 
print(coffee_words_len)
for i in coffee_words_len:
    i=str(i)
    k=i.join('')
print(k)

###map 사용
coffee_number = "".join(map(str,coffee_words_len))
print(coffee_number)
coffee_pi = float(coffee_number) / 1000000000.0
print(coffee_pi)

#math모듈 불러오기
import math
print(math.pi)

names = ['jake' , ' tylor' , 'john' , 'rachel' , 'oburu']
names_len = [len(name) for name in names]
print(names_len)

names_dict={}
names_dict={name : len(name) for name in names}   ###########시험에 나올듯 
print(names_dict)