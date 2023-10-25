#Sonia Alwani
def encode(password_encoder):
   encoded = ''
   for char in password_encoder:
       if char == '0':
           encoded += '3'
       elif char == '1':
           encoded += '4'
       elif char == '2':
           encoded += '5'
       elif char == '3':
           encoded += '6'
       elif char == '4':
           encoded += '7'
       elif char == '5':
           encoded += '8'
       elif char == '6':
           encoded += '9'
       elif char == '7':
           encoded += '0'
       elif char == '8':
           encoded += '1'
       elif char == '9':
           encoded += '2'

   return encoded

def decode(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        int_digit = int(digit)
        int_digit -= 3
        if int_digit < 0:
            int_digit = 10 + int_digit #int digit is negative, so value is actually being subtracted from 10 to wrap back around
        decoded_password += str(int_digit)
    
    return decoded_password



def main():
   encoded = ''
   while True:
       print()
       print('Menu')
       print('-------------')
       print('1. Encode')
       print('2. Decode')
       print('3. Quit')
       print()
       user_option = int(input('Please enter an option: '))


       if user_option == 1:
           password_encoder = input('Please enter your password to encode: ')
           encoded = encode(password_encoder)
           print('Your password has been encoded and stored!')

       elif user_option == 2:
           print("Your password has been decoded! Here it is: ")
           print(decode(encoded))
       elif user_option == 3:
           print("Thank you for using the decoder! Bye!")
           break
       else:
           print("Invalid option. Please select 1, 2, or 3 as your option (no spaces).")



if __name__ == '__main__':
   main()
