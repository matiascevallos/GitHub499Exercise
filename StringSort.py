
def sortDescending(strList):
    newSortedList = sorted(strList, key=str, reverse=True)
    return newSortedList
def sortAscending(strList):    
    newSortedList = sorted(strList, key=str, reverse=False)
    return newSortedList

def testing():
    assert sortDescending(['abc', 'cde', 'zef']) == ['zef', 'cde', 'abc'], "Should be ['zef', 'cde', 'abc']"
    assert sortAscending(['abc', 'cde', 'zef']) == ['abc', 'cde', 'zef'], "Should be ['abc', 'cde', 'zef']"
    assert sortDescending(['abc', 'abcd', 'abbc']) == ['abcd', 'abc', 'abbc'], "Should be ['abcd', 'abc', 'abbc']"
    assert sortAscending(['abc', 'abcd', 'abbc']) == ['abbc', 'abc', 'abcd'], "Should be ['abbc', 'abc', 'abcd']"

def main():
    userList = list(map(str,input("\nEnter the strings : ").split()))
    
    print("\nUser's List: ", userList)

    print(f'Your list sorted in descending order is: {sortDescending(userList)}')
    print(f'Your list sorted in descending order is: {sortAscending(userList)}')

#testing()
main()
