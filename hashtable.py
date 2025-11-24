#Drew Hafford
#11/20
#Got help from Caramon
import csv
import time
 

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
        self.hashTable = [None]*size
        self.capacity = size
        self.curSize = 0
        self.collisions = 0

    def addByQuote(self, data):
        index = self.hashing_it(data[8])
        while self.hashTable[index] != None: #collision
            index += 1
            if index > self.capacity:
                index = 0
            self.collisions += 1
        self.hashTable[index] = data
        self.curSize += 1
        return


    def addByName(self,data):
        index = self.hashing_it(data[0])
        while self.hashTable[index] != None: #collision
            index += 1
            if index >= self.capacity:
                index = 0
            self.collisions += 1
        self.hashTable[index] = data
        self.curSize += 1
        return


    def hashing_it(self,inputStr):
        weirdNums = 0
        for i in inputStr:
            weirdNums += ord(i)
        #time for the fun number stuff
        return(weirdNums%23)

def main():    
    size = 15000
    file = "MOCK_DATA.csv"
    quoteHash = hashTable(size)
    nameHash = hashTable(size)

    #FOR THE TITLES
    start = time.time()
    rowCount = 0
    with open(file, 'r', newline = '', encoding="utf8") as csvfille:
        reader = csv.reader(csvfille)
        for row in reader:
            if rowCount == 0:
                rowCount += 1
            else:
                nameHash.addByName(row)
    end = time.time()
    print(f"There were {nameHash.collisions} collisions")#number of collisions
    print(f"It took {end-start:0.2f} seconds to sort by Title")#time it took
    print(f"There were {size-nameHash.curSize} wasted buckets")#wasted buckets
    rowCount = 0
   #FOR THE QUOTES
    start = time.time()
    with open(file, 'r', newline = '', encoding="utf8") as csvfille:
        reader = csv.reader(csvfille)
        for row in reader:
            if rowCount == 0:
                rowCount += 1
            else:
                quoteHash.addByQuote(row)
    end = time.time()

    print(f"There were {nameHash.collisions} collisions")#number of collisions
    print(f"It took {end-start:0.2f} seconds to sort by quote")#time it took
    print(f"There were {size-nameHash.curSize} wasted buckets")#wasted buckets

if __name__ == "__main__":
    main()