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
        index = self.hashing_it(data[8])
        self.hashTable[index] = data
        return

    def addByName(self,data):
        index = self.hashing_it(data[0])
        self.hashTable[index] = data
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
    with open(file, 'r', newline = '', encoding="utf8") as csvfille:
        reader = csv.reader(csvfille)
        for row in reader:
            print(row)
            counter+=1
        

    print(counter)

if __name__ == "__main__":
    main()