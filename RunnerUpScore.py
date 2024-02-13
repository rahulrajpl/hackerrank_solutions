if __name__ == '__main__':
    
    arr = [6,6,5,3,5,2,1,3,6,4]
    # arr = [2, 3, 6, 6, 5]
    # arr = [-10, 0, 10]
first = max(arr)
second = max([i for i in arr if i != first])
print(second)