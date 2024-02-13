from string import ascii_lowercase
def print_rangoli(size):
    print("Rangoli");
    # for i in range(1,size+1):
    #     j=0
    #     print('--' * (size-i), end='')
    #     for j in range(1,i): 
    #         print(ascii_lowercase[size-j], end='-')
    #     print(ascii_lowercase[size-i], end='')
    #     # print('\b', end='')
    #     for k in range(j,0,-1):
    #         print('-'+ascii_lowercase[size-k], end='')
    #     print('--' * (size-i), end='')
    #     print(end='\n')
    # for i in range(size-1,0,-1):
    #     j=0
    #     print('--' * (size-i), end='')
    #     for j in range(1,i): 
    #         print(ascii_lowercase[size-j], end='-')
    #     print(ascii_lowercase[size-i], end='')
    #     # print('\b', end='')
    #     for k in range(j,0,-1):
    #         print('-'+ascii_lowercase[size-k], end='')
    #     print('--' * (size-i), end='')
    #     print(end='\n')
    shape=[]
        for i in range(size):
        chars = [chr(size-n+96) for n in range(i+1)]
        chars += [char for char in chars[-2::-1]]        
        shape.append('-'.join(chars).center(size*4-3,'-'))
    
    shape += [line for line in shape[-2::-1]]
   
    print('\n'.join(shape))
if __name__ == "__main__":
    # n = int(input("Enter size:"))
    print_rangoli(5)
