
#Get positiive number integer (loop variable)
number = int(input())

#set empty string to hold bianary
strBianary = ''


#Starting at 2 ** 31 (32 element) moving towards 2 ** 0 (1 element)

for n in range(31, -1, -1):
        x = 2 ** n
        
        '''
        Put dashes on any number not at the begining of the loop
        or the end of the loop and the number to the right is divisble by 8
        '''
        if 0 < n < 31 and (n + 1) % 8 == 0:
              #place dash
              strBianary += '-'

        #if the inputed number is greater than or equal to x (= 2 ^ n)
        if number >= x:
            #subtract x from number and add 1 to bianary string
            number -= x
            strBianary += '1'
        else:
              #otherwise add 0 to the bianary string
              strBianary += '0'

#Display Bianary string     
print(strBianary)