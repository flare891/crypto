import functools

def decryptString(ct):
    alphabet = list("QWERTYUIOPASDFGHJKL'ZXCVBNM,. ")
    deltaModifier = 0
    plaintext = ""
    # print("ciphertext: " + ct)
    # Starting delta is indeed 3, but I think with every new word (aka after a space is encoded) it either doubles or increments somehow
    for c in list(ct):
        delta = (3 + (deltaModifier * 2)) % len(alphabet)
        i = alphabet.index(c)
        # print(c + "," + str(i))
        if(i < delta):
            i + len(alphabet)
        i -= delta
        plaintext += alphabet[i]
        if(alphabet[i] == " "):
            deltaModifier += 1
    print("ciphertext: " + ct)
    print("plaintext:  " + plaintext)

ct1 = "GFXPIFIAS.GEWDTKRGXHT"
ct2 = "JCOJ'KAVJHDLKN,CA GXEB.GJMVLKVWJEZ,OR,CQRW.BQIWWIW"
ct3 = "IMUA.OMQILYEPFGTJPA PESKXPUKCOGXHHXHXCPAZKDNRMVGF'"
ct4 = ",D.JVT VLCVZORJNC',,ZBWQETCSMRI.TRSVJQOSPEH FSPTDH"
ct5 = "FAUZF'DZBJL.ZOFEHFUVFVAGVJJVOKLSDBRKNMKGPNDX,PXJNQ"
ct6 = "L.KKVR.WNVPMZTWC AY B. MXPB.TR,RFUQILAGWEHVVTHZUFB"
ct7 = "FOXCLVFOAK.VOQBD.VLGS'BDWJ ZXQ,HXJLKWJ''Z,ORLATCOR"  # This last comma is supposed to be a ?
ct8 = ".BX TCSMIBW.PGQILYE IJPTZAGPE'LU'ONKJAYX'WNDNMEGQN"
ct9 = "ZHJT ..BLFWOVZYR.X"

# print(functools.reduce(lambda x,y: x+y, map(lambda x : decryptString(x, deltaModifier), ciphertext)))
decryptString(ct1 + ct2 + ct3 + ct4 + ct5 + ct6 + ct7 + ct8 + ct9)

# ciphertext: GFXPIFIAS.GEWDTKRGXHT|JCOJ'KAVJHDLKN,CA GXEB.GJMVLKVWJEZ,OR,CQRW.BQIWWIW|IMUA.OMQILYEPFGTJPA PESKXPUKCOGXHHXHXCPA|ZKDNRMVGF',D.JVT VLCVZORJNC',,ZBWQETCSMRI.TRSVJQOSPEH FSPTDHFAUZF'DZBJL.ZOFEHFUVFVAGVJJVOKLSDBRKNMKGPNDX,PXJNQL.KKVR.WNVPMZTWC AY B. MXPB.TR,RFUQILAGWEHVVTHZUFBFOXCLVFOAK.VOQBD.VLGS'BDWJ ZXQ,HXJLKWJ''Z,ORLATCOR.BX TCSMIBW.PGQILYE IJPTZAGPE'LU'ONKJAYX'WNDNMEGQNZHJT ..BLFWOVZYR.X
# plaintext:  SALUTATIONS MI AMIGO,|PHWPDARJPOYSALZHRCIGNKXIP'JSAJBPNFZWMZHVMBXKVQBBQB|Q' W' H'MIBX.ERVY. JM'.TOMVTPNWOEEOEOPM,|IT ALSO MEANS THAT WE HAVE BEEN TRYING TO REACH YOU ABOUT YOUR STARSHIP'S EXTENDED WARRANTY. PLEASE CONTACT US IMMEDIATELY SO THAT WE CAN REMEDY THIS. ALL OF THT ASIDE, THANKS FOR BEING AWESOME, MAN.. THANKS FOR BEING ONE OF THE BEST FRIENDS A GUY COULD ASK FOR. HAPPY CAKE DAY.
