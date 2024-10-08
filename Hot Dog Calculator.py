import math
def main():
    dogs = 10
    buns = 8
    total = getTotalHotDogs()
    mindogs = math.ceil(total / dogs)
    dogsleft = (mindogs * dogs) - total
    minbuns = math.ceil(total/buns)
    bunsleft = (minbuns * buns) - total
    result(dogsleft, mindogs, bunsleft, minbuns)

def getTotalHotDogs():
    people = (int(input("Enter the number of people attending the cookout: ")))
    hotdogs = (int(input("Enter the number of hot dogs for each person:")))
    total = people * hotdogs
    return total

def result(dogsleft, mindogs, bunsleft, minbuns):
    print("Minimum packages of hot dogs needed: ", mindogs)
    print("Minimum packages of hot dogs buns needed: ",minbuns)
    print("Hot dogs left over: ", dogsleft)
    print("Hot dog buns left over: ", bunsleft)
    
if __name__ == "__main__":
    main()
