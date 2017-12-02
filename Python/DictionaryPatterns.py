import sys

def testCreateFreqMapWithStrings():
    str_list = [ "ram", "shyam", "geeta", "ram", "hari", "shyam" ]
    strFreqMap = createFreqDict(str_list)
    assert(strFreqMap["ram"]  == 2)
    assert(strFreqMap["hari"] == 1)
    assert(strFreqMap['shyam'] == 2)
    print("Test Passed")
    
    
def testCreateFreqMap():
    int_list = [ 1, -1, 2, 3, 3, 2, 1, 4, 1, -1, 7, 10, 0, 100, 0]
    intFreqMap = createFreqDict(int_list)
    assert(intFreqMap[1] == 3)   
    assert(intFreqMap[3] == 2)
    assert(intFreqMap[0] == 2)
    assert(intFreqMap[-1] == 2)
    assert(intFreqMap[7] == 1)
    print("Test Passed")
    

def createFreqDict(obj_list):
    """ Function takes a list of items and create frequency map """
    itemFreqMap = {}
    
    for item in obj_list:
        if item in itemFreqMap:
            itemFreqMap[item] += 1
        else:
            itemFreqMap[item] = 1
    
    return itemFreqMap

if __name__ == "__main__":
    testCreateFreqMapWithStrings()
    testCreateFreqMap()