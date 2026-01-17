alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
to_do = input("Do you wanted to Encrypt (type Encode) or Decode (type Decrypt)?\n").lower()
text = input("Type your message :\n").lower()
shift = int(input("Type the shift Number :\n"))
def decryption_cc(original_word,shift_amt):
    output_text = ""

    for letter in original_word:
        if letter in alphabet:  # if the message have alphabets then it will shift the value using below codes
            shifted_letter = alphabet.index(letter) - shift_amt
            shifted_letter %= len(alphabet)     #######if the letter is more than in alphabet array we will do mod of the shifted amount
            output_text += alphabet[shifted_letter]     #########accumulate all the encrypted letter here.
        else:                   ##########if the message has special characters or number or space then we use them as it is.
            output_text += letter

    print(f"Decrypted Code = {output_text}")

decryption_cc(original_word=text,shift_amt=shift)