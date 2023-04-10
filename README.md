# StrongpasswordGenerator
In this code, we define a function generate_password that takes an optional length parameter. The function uses the random and string modules to generate a random password with a mix of uppercase letters, lowercase letters, digits, and special characters.

We start by defining four variables that contain the allowed character ranges for each character type we want to include in the password. We then create an empty list called password and add one character from each type to ensure that at least one character of each type is present in the password.

We use a for loop to fill the rest of the password randomly using string.ascii_letters, string.digits, and string.punctuation. Finally, we shuffle the password list and join it into a string to get the final password.

You can adjust the length of the password by passing an integer value as the length parameter to the function. The default length is 12 characters.

# Usage
``python3 strongpassgen.py`` <- It should work like that.
