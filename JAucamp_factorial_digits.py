# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:41:16 2021

@author: User-PC
"""
import sys

#==========================================================
# CALCULATION FUNCTION
#==========================================================    
def SumOfFactorialDigits(x):
    digits_sum = 0
    
    # Create array to store the numbers for the 
    # factorial calculation.
    factorial_digits = []
    factorial_digits.append(1) # adds 1 to the end
    #------------------------------------------------------
    # FACTORIAL CALCULATION
    #------------------------------------------------------
    # Calculate the factorial of the number
    # ie. 10! = 1*2*3...*10
    for k in range (1, x+1):
        
        # need to only store on digit per location of
        # the digit vector. Therefore must carry over the
        # excess to the next location
        carry_value = 0
        
        for j in range(len(factorial_digits)):
            
            # Calculate the leftover and the carry
            # from the previous calculation
            leftover = factorial_digits[j]*k + carry_value 

            # Store the result
            carry_value = leftover//10

            factorial_digits[j] = leftover%10

        
        while (carry_value != 0):
            factorial_digits.append(carry_value%10)
            carry_value //= 10      
    #------------------------------------------------------
      
    
    #------------------------------------------------------
    # DIGIT SUM CALCULATION
    #------------------------------------------------------
    # Calculate the sum of the digits of factorial_digits[]
    #------------------------------------------------------
    for r in range(len(factorial_digits)):
        digits_sum += factorial_digits[r]
    return digits_sum    
    #------------------------------------------------------
#==========================================================


#==========================================================
# MAIN
#==========================================================
if __name__ == "__main__":
    
    # Number to get factorial of
    factorial_number = int(sys.argv[1])
    # Main Function that calculates the sum of the factorials
    sum_number = SumOfFactorialDigits(factorial_number)
    print(sum_number)
#===========================================================