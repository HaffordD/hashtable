import csv
 

class DataItem:
    def __init__(self, data):
        self.movie_name = data[0]
        self.genre  = data[1]
        self.release_date = data[2]
        self.director = data[3]
        self.revenue = data[4]
        self.rating = data[5]
        self.minDuration = data[6]
        self.ProductionCompany = data[7]
        self.quote = data[8]

class hashTable:
    def __init__(self,size):
        self.hashTable = [0]*size


    def addByQuote(self, data):
        
        pass

    def addByName(self,data):

        pass

    def hashing_it(self,inputStr):
        weirdNums = 0
        for i in inputStr:
            weirdNums += ord(i)
        #time for the fun number stuff
        return(weirdNums%23)

       
size = 15000
file = "MOCK_DATA.csv"
with open(file, 'r', newline = '', encoding="utf8") as csvfille:
    reader = csv.reader(csvfille)
    for row in reader:
        print(row)
        counter+=1
        

print(counter)