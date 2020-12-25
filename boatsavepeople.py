def findNofBoats(people, limit):
    people.sort()
    print(people)
    left = 0
    right = len(people) - 1
    boats = 0
    while(left <= right):
        if(left == right):
            boats += 1
            break
        if (people[left] + people[right] <= limit):
            left += 1
        
        boats += 1
        right -= 1
    return boats


print(findNofBoats([5, 2, 1, 6, 2, 7, 9, 8, 10], 10))
