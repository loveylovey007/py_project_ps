# #=========================================================================================================================#

 #multiple input call in functions
 def greet_with(name, location):
     print(f"Hello {name}. \nSo, you are from {location}")
     print(f"My next vist might be your {location}. \nThanks")
 greet_with('praveen','puri')# positional argumentation
 greet_with(name='praveen',location='puri')# keyword argumentation

# #=========================================================================================================================#

 #love_calculator#: name1 = "Angela Yu" name2 = "Jack Bauer"
 # T occurs 0 times R occurs 1 time U occurs 2 times E occurs 2 times  Total = 5
 # L occurs 1 time O occurs 0 times V occurs 0 times E occurs 2 times Total = 3
 # Love Score = 53
 def calculate_love_score(name1,name2):
     combine_name = (name1+name2).lower()
     true_count=(combine_name.count('t')+combine_name.count('r')+combine_name.count('u')+combine_name.count('e'))
     love_count=(combine_name.count('l')+combine_name.count('o')+combine_name.count('v')+combine_name.count('e'))
     love_score=int(str(true_count) + str(love_count))
     print(f"Love Score = {love_score}")

 print(f"Welcome Lovers lets find out your Love Score \n")
 name1= input("First Name : \n")
 name2= input("Second Name : \n")
 calculate_love_score(name1,name2)

#=========================================================================================================================#
#Caesar Ciphe Coding
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
to_do = input("Do you wanted to Encrypt (type Encode) or Decrypt (type Decrypt)?\n").lower()
text = input("Type your message :\n").lower()
shift = int(input("Type the shift Number :\n"))
def encryption_cc(original_word,shift_amt):
    cipher_text = ""

    for letter in original_word:
        shifted_letter = alphabet.index(letter) + shift_amt

        shifted_letter %= len(alphabet)
        cipher_text += alphabet[shifted_letter]

    print(f"Encrypted Code = {cipher_text}")

encryption_cc(original_word=text,shift_amt=shift)