'''
names = input('이름 입력:')
number = int(input('숫자 입력:'))
for _ in range(number):
    print(f'Hello {names}')
'''

Maker = 'Hyundai'
Model = 'Genesis'
Color = 'balck'

class Car:
    def __init__(self, Maker, Model, Color):
        self.Maker = Maker
        self.Model = Model
        self.Color = Color
        self.Speed = 0
    def drive(self, Speed):
        self.Speed = Speed
    def stop(self):
        self.Speed = 0

genesis = Car('Hyundai', 'Genesis' , 'black')
print(type(genesis))
genesis.drive(100)
genesis.stop()

#카운터기
class Counter:
    def __init__(self,initvalue=0):
        self.count = initvalue
    def increment(self):
        self.count +=1
counter1 = Counter()
counter2 = Counter(100)  #100이 기본값인 카운터기
counter1.increment()                       

#텔레비전
class Television:
    def __init__(self, channel, volume, onoff):
        self.channel = channel
        self.volume = volume
        self.onoff = onoff

    def show(self):
        print(self.channel, self.volume, self.onoff)
    def setChannel(self,channel):
        self.channel = channel
    def getChannel(self):
        return self.channel
    def setVolume(self,volume):
        self.volume = volume
myTV = Television(11,22,True)
'''myTV.show()
myTV.setChannel(163)
myTV.show()'''
myTV.channel = 7
myTV.volume = 7
myTV.show()


class student:
    def __init__(self,name,python,math,english):
        self.name = name                                                                                                      
        self.python = python
        self.math = math
        self.english = english
    def view_grade(self):
        print(self.python,self.math,self.english)
    def collect_grade(self):
        self.python = python
        self.math = math
        self.english = english
    def setGradePython(self,python):
        self.python = python    
    def setGradeMath(self,math):
        self.math = math      
    def setGradeEnglish(self,english):
        self.english = english      
    def show(self):
        total = self.python + self.math + self.english
        print(total)
        print(total/3)

학생1=student('권혁주',90,80,83)
학생1.show()
학생1.python=60
학생1.show()

