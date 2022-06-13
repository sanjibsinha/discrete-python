from ctypes import sizeof

def swappingNumber(numOne, numTwo):
    temp = numOne
    numOne = numTwo
    numTwo = temp
    
def arrangeNumbers (arrayOfNumbers, lowIndex, highIndex):
    pivotIndex = arrayOfNumbers[highIndex]
    indexNumber = (lowIndex - 1)
    initialNUmber = lowIndex
    while initialNUmber <= (highIndex - 1):
        if (arrayOfNumbers[initialNUmber] <= pivotIndex):
            indexNumber = indexNumber + 1
            swappingNumber(arrayOfNumbers[indexNumber], arrayOfNumbers[initialNUmber])
        initialNUmber = initialNUmber + 1
        swappingNumber(arrayOfNumbers[indexNumber + 1], arrayOfNumbers[highIndex])
        return indexNumber + 1
    
def quickSortTheCollection(arrayOfNumbers, lowIndex, highIndex):
    if (lowIndex < highIndex):
        pivotIndex = arrangeNumbers(arrayOfNumbers, lowIndex, highIndex)
        quickSortTheCollection(arrayOfNumbers, lowIndex, pivotIndex - 1)
        quickSortTheCollection(arrayOfNumbers, pivotIndex + 1, highIndex)
        
def displayInAscendingOrder(arrayOfNumbers, sizeOfCollection):
    initialNUmber = 0
    while initialNUmber < sizeOfCollection:
        print(f'{arrayOfNumbers[initialNUmber]}')
        initialNUmber = initialNUmber + 1
        
arrayOfNumbers = [22, 17, -8, 9, 11, 5]
numberOfNUmbers = len(arrayOfNumbers)/arrayOfNumbers[0]
quickSortTheCollection(arrayOfNumbers, 0, numberOfNUmbers - 1)
print('The sorted array is: ')
displayInAscendingOrder(arrayOfNumbers, numberOfNUmbers)

