s = input()

for n in s:
    n = ord(n)
    if 97 < n and n < 122: #a ~ z
        n += 13
        if n > 122:
            n -= 26
    elif 65 < n and n <= 90: #A ~ Z
        n += 13
        if n >= 90:
            n -= 26
    c = chr(n)
    print(c, end="")
print("\n")

    #EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT.
