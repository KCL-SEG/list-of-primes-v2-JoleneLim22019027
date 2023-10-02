"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    try:
        list = []
        num = 2
        if number_of_primes >= 1:
            list = [2]
        while (len(list) < number_of_primes):
            pFlag = True
            i = 0
            while (pFlag and (i < len(list)) and (list[i] <= num)):
                if (num % list[i] == 0):
                    pFlag = False
                else:
                    i += 1
            if pFlag:
                list.append(num)
            
            num += 1

        return list
    
    except ValueError:
        print("Input cannot be 0 or a negative number!")
        return []


