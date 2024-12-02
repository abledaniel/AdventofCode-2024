#test inputs
list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]

## Find the distances between two sorted lists of integers
def distance(index, index2):
    res = 0
    for i in range(len(index)):
        res += abs(index2[i] - index[i])
    print(res)
    return res

## Find the similarity with two sorted lists multiply a value by the amount of the values the other list has  from one list by that value
def similarity(index, index2):
    res = 0
    for i in range(len(index)):
        val = index2.count(index[i])
        res += index[i] * val  
    print(res)

def main():
    input1 = []
    input2 = []
    with open("input", 'r') as file:
        for line  in file:
            left, right = (map(int, line.split()))
            input1.append(left)
            input2.append(right)
    input1.sort()
    input2.sort()
    distance(input1, input2)
    similarity(input1, input2)

main()