from string import ascii_uppercase

class keyboard:

    def forward(self, letter):
        signal = ascii_uppercase.find(letter)
        return signal

    def backward(self, signal):
        letter = ascii_uppercase[signal]
        return letter

class plugboard:

    def __init__(self, pairs):
        self.left = ascii_uppercase
        self.right =  ascii_uppercase

        for i in pairs:
            A = i[0]
            B = i[1]
            pos_A = self.left.find(A)
            pos_B = self.left.find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A+1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B+1:]

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal 

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal 

class rotor:

    def __init__(self, wiring, notch):
        self.left = ascii_uppercase
        self.right = wiring 
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal 

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal 

    def rotate(self, n = 1, forward = True):

        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]


    def rotateToLetter(self, letter):
        
        n = ascii_uppercase.find(letter)
        self.rotate(n)

    def show(self):
        print(self.left)
        print(self.right)
        print(" ")

    def setRing(self, letter):

        n = ascii_uppercase.find(letter)
        self.rotate(n, forward = False)

        notch = ascii_uppercase.find(self.notch)
        self.notch = ascii_uppercase[(notch - n) % 26]

class reflector:

    def __init__(self, wiring):
        self.right = ascii_uppercase
        self.left = wiring

    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal 

class enigma:

    def __init__(self, r1, r2, r3, ref, pb):

        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.ref = ref
        self.pb = pb
        self.kb = keyboard()

    def start(self, key):
        self.r1.rotateToLetter(key[0])
        self.r2.rotateToLetter(key[1])
        self.r3.rotateToLetter(key[2])

    def setRings(self, ring):
        self.r1.setRing(ring[0])
        self.r2.setRing(ring[1])
        self.r3.setRing(ring[2])

    def encrypt(self, letter):

        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        
        elif self.r2.left[0] == self.r2.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()

        elif self.r3.left[0] == self.r3.notch:
            self.r2.rotate()
            self.r3.rotate()

        else:
            self.r3.rotate()

        signal = self.kb.forward(letter)
        signal = self.pb.forward(signal)
        signal = self.r3.forward(signal)
        signal = self.r2.forward(signal)
        signal = self.r1.forward(signal)
        signal = self.ref.reflect(signal)
        signal = self.r1.backward(signal)
        signal = self.r2.backward(signal)
        signal = self.r3.backward(signal)
        signal = self.pb.backward(signal)
        letter = self.kb.backward(signal)

        return letter

rot1 = rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
rot2 = rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
rot3 = rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
rot4 = rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
rot5 = rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

refA = reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
refB = reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
refC = reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")


text = "SPPNNTV"

kb = keyboard()
pb = plugboard(["AP", "BG", "XZ"])

em = enigma(rot1,rot2,rot3,refB, pb)

em.setRings("DAC")
em.start("CAR")

cipher = ""

for letter in text:
    cipher +=  em.encrypt(letter)

print(cipher)





