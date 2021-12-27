### Valid Account Number
 
 
Use Modulo Formula Method (Mod 10) for validating Account numbers
 
It has the following steps: 
 
Step 1: Double the value of alternate digits of the Account
number beginning with the second digit from the right 
(the rightmost digit is the check digit.)
 
Step 2: Add the individual digits comprising the products
obtained in Step 1 to each of the unaffected digits in
the original number.
 
Step 3: The total obtained in Step 2 must be a number
ending in zero (30, 40, 50, etc.) for the account number 
to be validated. The total mod 10 = 0.
 
 
## EXAMPLE 
 
For example, to validate the  account number 79927398713:
 
 
Step 1	Account number      7 	9	9	2	7	3	9	8	7	1	3	
Step 2 Double every other	7	18	9	4	7	6	9	16	7	2	3
  
7 +(1+8)+ 9 + (4) + 7 + (6) + 9 +(1+6) + 7 + (2) + 3 
 
Step 3: Sum = 70 : Account number is valid because the 
70/10 yields no remainder.
 
If the number is valid, output the word “VALID”. 
If the number is not valid, output the word “INVALID” followed 
by a space and the correct check digit, which is the right-most digit, 
that would make the accound number valid.
