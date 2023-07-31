# hackerrank-creditcard-validation

This repo contains my solution to the HackerRank "Validating Credit Card Numbers" code challenge, in Python.

The challenge description [can be viewed here](https://www.hackerrank.com/challenges/validating-credit-card-number/problem)

The credit cards read in by the user are validated with the following conditions:
* Credit card numbers must start with 4, 5, or 6
* They must only contain 16 digits
* Those 16 characters may be separated into 4 equal groups with a single hyphen '-' without spaces
* There may not be 4 or more consecutively repeating digits
______________________________________________________________
Input is taken from stdin.

The first line is an integer N (where 0 < N < 100) describing how many lines of credit card numbers will follow

The next N lines contain the credit card numbers to check. 

______________________________________________________________

Output is N lines containing either "Valid" or "Invalid", representing whether the credit card number at that input's
line passes the above guidelines or not.

