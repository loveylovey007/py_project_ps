##Caesar Ciphe Coding
import art
print(art.text2art('caesar \nciphe'))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_word, shift_amt, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amt *= -1
    for letter in original_word:
        if letter in alphabet:
            shifted_letter = alphabet.index(letter) + shift_amt
            shifted_letter %= len(alphabet)
            output_text += alphabet[shifted_letter]
        else:
            output_text += letter
    print(f"here is your {encode_or_decode}d result = {output_text}")

wanted_to_continue = True
while wanted_to_continue:
    to_do = input("Do you wanted to Encrypt (type Encode) or Decrypt (type Decrypt)?\n").lower()
    text = input("Type your message :\n").lower()
    shift = int(input("Type the shift Number :\n"))
    caesar(original_word=text, shift_amt=shift, encode_or_decode=to_do)

    restart_vr = input(f"Type 'yes' to continue or 'no' to exit. \n").lower()
    if restart_vr == "no":
        wanted_to_continue = False
        print(f"Good Bye")






#==============================================================================================#
# def encryption_cc(original_word,shift_amt):
#     cipher_text = ""
#
#     for letter in original_word:
#         if letter in alphabet:  # if the message have alphabets then it will shift the value using below codes
#             shifted_letter = alphabet.index(letter) + shift_amt
#             shifted_letter %= len(alphabet)     #######if the letter is more than in alphabet array we will do mod of the shifted amount
#             cipher_text += alphabet[shifted_letter]     #########accumulate all the encrypted letter here.
#         else:                   ##########if the message has special characters or number or space then we use them as it is.
#             cipher_text += letter
#
#     print(f"Encrypted Code = {cipher_text}")
#
# encryption_cc(original_word=text,shift_amt=shift)
#
# def decryption_cc(original_word,shift_amt):
#     output_text = ""
#
#     for letter in original_word:
#         if letter in alphabet:  # if the message have alphabets then it will shift the value using below codes
#             shifted_letter = alphabet.index(letter) - shift_amt
#             shifted_letter %= len(alphabet)     #######if the letter is more than in alphabet array we will do mod of the shifted amount
#             output_text += alphabet[shifted_letter]     #########accumulate all the encrypted letter here.
#         else:                   ##########if the message has special characters or number or space then we use them as it is.
#             output_text += letter
#
#     print(f"Decrypted Code = {output_text}")
#
# decryption_cc(original_word=text,shift_amt=shift)
