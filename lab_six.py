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



def main():
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
           print(encoded)



if __name__ == '__main__':
   main()
