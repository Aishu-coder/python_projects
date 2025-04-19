alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'
    , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*','?']
runagain=False
while not runagain :
    direction = input("Type 'encode' for encrypt and 'decode' for decrypt\n").strip()
    text = input('Type your message\n').lower()
    shift = int(input('Type the shift number\n'))
    shift=shift%26

    def caesar(text, shift):
        new_text = ""
        for l in text:
            if l == ' ':
                new_text +=l
            if l.isdigit():
                new_text += l
            if l in symbols:
                new_text += l
            if l in alphabet:
                position = alphabet.index(l)
                if direction == "encode":
                    index = position + shift
                elif direction == "decode":
                    index = position - shift
                new_text += alphabet[index]
        print(f"The {direction}d text is {new_text}")

    caesar(text, shift)
    decision = input("Type 'yes' if you want to go again.otherwisw Type 'no'\n").lower()
    if decision == 'no':
        print("Goodbye")
        runagain=True

#or if direction =="decode": shift*=-1 before for loop