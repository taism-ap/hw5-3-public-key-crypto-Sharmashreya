#Determine the private key. During examples, I have tended to use '7'
i = int(input("choose your private key: "))

#Change the message from ascii to binary

#add an empty string to which the binary message will be added
a = ""
#convert the characters to binary using ascii
h = "01101000"
e = "01100101"
y = "01111001"
#add these binary digits to the empty string 
a = a + str(h) + str(e) +str(y)
#print the message in ascii
print("here is your message in binary: " + a)

def createYourPublicKey():
  #declare the public values 
  C = 5
  N = 19
  #calculate the Q public key to be shared with the sender/ receiver 
  Q = (C^(i))%N
  return(Q)

#print the seed
Q = createYourPublicKey()
print("share your public key, which is as follows: " + str(Q))

def createSeed():
  #input the public key that you receive from sender/ receiver, I have tended to use '12' in practice
  P = int(input("enter the public key you receive: "))
  #define N again within this function with the same N value as before
  N = 19
  seed = (P^i)%N
  return(seed)

seed = createSeed()
#print the seed value
print("here is the seed value for the pseudo random number generator: " + str(seed))

#create an empty string for the public key to go in
x = ""
A = 533
B = 227
N = 64
#use the seed value to create a public key using pseudo random number generator 
for i in range (4):
  x_decimal = (A*seed + B)%(N)
#Transform the numbers into binary and the ,6 refers to the number of bits it would take to have the N value in binary
  x_binary = '{0:0{1}b}'.format(x_decimal,6)
  x = x + str(x_binary)
  seed = x_decimal
#Print the public key that can be used to encrypt 
print("here is your encryption key: " + x)

#Use the XOR function in order to encrypt the original message
def xor_encryption():
  y = int(a,2) ^ int(x,2)
  y_formatted = '{0:0{1}b}'.format(y,len(a))
  return(y_formatted)

y_formatted = xor_encryption()
print("here is your message encrypted: " + str(y_formatted))
