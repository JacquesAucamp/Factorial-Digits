# Factorial-Digits

## The File
The JAucamp.tar file provided contains all the required files to create a Docker build. The directory can be accessed by cloning the repository with the following command:
 - git clone https://github.com/JacquesAucamp/Factorial-Digits
The Docker build can be created and run by entering the following in the command line (Must have Docker installed on the system):
 - docker build -t factorial-digits .
 - docker run --rm factorial-digits x
where "x" is the input number (ie. 10, 100, 1000).

## The Algorithm
The function of the python script is to calculate the sum of the digits of a factorial result. For example:
 - If the input x = 10 the factorial result is 3628800. The resulting sum of these digits is 3+6+2+8+8+0+0 = 27.
 - If the input x = 100 the factorial result is 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000. The resulting sum of these digits is 648.

The algorithm function can be summarised with the following steps:
 1. Create an array to store the digits of the factorial results
 2. Calculate the factorial number from first principles using a leftover carry method in a loop. Only 1 digit must be stored per location of the array and therefore the leftover digit must be carried over in the next calculation.
 3. Once all the digits have been stored of the factorial results, sum the digits.
 4. Output the result.
