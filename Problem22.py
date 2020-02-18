class Problem22:
    def declareDictionary(self):
        abc = "abcdefghijklmnopqrstuvwxyz".upper()
        dict = {}
        count = 1

        for letter in abc:
            dict[letter] = count
            count += 1

        return dict

    def readFile(self):
        with open("files/p022_names.txt", "r") as file:
            line = file.readlines()[0]
        array = line.replace('\"','').split(",")
        array.sort()
        return array


    def dictionaryValuePosition(self, array):
        scoreLetters = self.declareDictionary()
        totalPerName = 0
        dictionaryValuePosition = {}
        for index, names in enumerate(array):
            for letters in names:
                totalPerName += scoreLetters[letters]
            dictionaryValuePosition[names] = (totalPerName, index + 1)
            totalPerName = 0
        return dictionaryValuePosition


problem = Problem22()

arrayOfNames = problem.readFile()
sum = 0
for value, position in problem.dictionaryValuePosition(arrayOfNames).values():
    sum += value*position

print(sum)
