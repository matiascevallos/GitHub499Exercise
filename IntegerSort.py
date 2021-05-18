

def sortDescending(intList):
    newSortedList = sorted(intList, key=int, reverse=True)
    return newSortedList
def sortAscending(intList):    
    newSortedList = sorted(intList, key=int, reverse=False)
    return newSortedList

def testing():
    assert sortDescending([1, 1, 1]) == [1, 1, 1], "Should be [1, 1, 1]"
    assert sortAscending([1, 1, 1]) == [1, 1, 1], "Should be [1, 1, 1]"
    assert sortDescending([1, 0, 0]) == [1, 0, 0], "Should be [0, 0, 0]"
    assert sortAscending([1, 0, 0]) == [0, 0, 1], "Should be [0, 0, 1]"
    assert sortDescending([-1, 0, 10000000]) == [10000000, 0, -1], "Should be [10000000, 0, -1]"
    assert sortAscending([-1, 0, 10000000]) == [-1, 0, 10000000], "Should be [-1, 0, 10000000]"
    assert sortDescending([-1, -6, -1]) == [-1, -1, -6], "Should be [-1, -1, -6]"
    assert sortAscending([-1, -6, -1]) == [-6, -1, -1], "Should be [-6, -1, -1]"
    
def main():
    n = int(input("Enter the number of elements in your list: "))
  
    userList = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
    
    print("\nUser's List: ", userList)

    print(f'Your list sorted in descending order is: {sortDescending(userList)}')
    print(f'Your list sorted in descending order is: {sortAscending(userList)}')

testing()
#main()
