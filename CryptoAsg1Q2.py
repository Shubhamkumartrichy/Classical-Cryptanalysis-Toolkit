# Instructions for the Instructor:
#
# Run the program using:
#     python3 CryptoAsg1Q2.py
#
# No external input files or command-line arguments are required, 
# as the ciphertext is embedded in the source code. If desired, 
# the ciphertext may be replaced with any other valid ciphertext 
# by modifying the 'given' variable in the script.


import math

given = """
DVNSJ QRVPC GWBVZ QGVVP VILQJ VTURP BNPZN TGQIG SIGVW MTCIM FQUIA CCKVG CBYKQ
ZNTNB UCIEN UHIVF IWPQC BNKCM IGGGV OEWEV PVGFX APQKM EATDR TBIQG IPRNX JECGQ
NPLMY EDURF IPRXX AVVDZ JKIPN UBQYG PVQGM XYCXV RFIPN VIPRI GMNVT AGVGM NUJZR
KCBUG QCVNS QAILI FPDBN UXVTN TJBQZ JHVIP RMCWJ NTLTG IPNVR WAPTK GGSBU GBIYN
TDRTN ZBQBK BPIIV PTLZC CCFEG QCVHW AFXNS GGMAV HCOLT KGUXV PNJLV PVUNV WMZCI
QPUPA GTDVB ONXUK AWFQE PLOTL VEXVR GCOVP TMEKC ONPSP VUIWE AIPRU RPBNP ZQGRQ
QGSBB UEMAF IPRFP GRZET BTXVT GKMEA RWEPT ZBHIP RNXJE CGGGJ TNVTH BEQDU PQCBN
KCMQD DWXUD VZCIP ROPBV EHBUG HKUQA IETTI QCQWH VCCZD TZFIT WZGIZ VEUQT WGMFC
CLRNT ONPIX EQDNF VWIGJ PLVPH XVTTL TGCME CIQBP HWSVW QAMTZ FQCMZ CCCFE GQCVS
MFEGQ OGSPB YHQZR AMBDH MEXPB VQCAP QJTQN TIQVD LRGEB UGDZR OHEUK AMNPD BUGGM
KRAIV PTLUQ LIOUI ZNEIQ QGPAB HIMAH DCAFE ZNEIQ PCAIC RAQPC IQBPH KRPIC EKTAY
CIMEV WMFEW WYCGZ RCAQF GSBUC IUNVW MZCIQ PULIF PDBZG GMYAP KBNAM PVXWA QUNBT
BCYCH JHVPT NPVCN ITNBT SMFEG QOKCO CCIBR TCANP SZRCH WAKCO NDDCG VWMJQ GTQ
"""

given = given.replace(" ", "")
given = given.replace("\n", "")

eng = [
    0.08167,0.01492,0.02782,0.04253,0.12702,
    0.02228,0.02015,0.06094,0.06966,0.00153,
    0.00772,0.04025,0.02406,0.06749,0.07507,
    0.01929,0.00095,0.05987,0.06327,0.09056,
    0.02758,0.00978,0.02360,0.00150,0.01974,
    0.00074
]
# source for above data(eng) is https://en.wikipedia.org/wiki/Frequency_analysis


def fun1(txt):
    n = len(txt)
    cnt = [0] * 26

    for i in range(n):
        cnt[ord(txt[i]) - ord('A')] += 1

    num = 0

    for i in range(26):
        num += cnt[i] * (cnt[i] - 1)

    return (26 * num) / (n * (n - 1))


def fun2(v1, v2):
    dot = 0
    n1 = 0
    n2 = 0

    for i in range(26):
        dot += v1[i] * v2[i]
        n1 += v1[i] * v1[i]
        n2 += v2[i] * v2[i]

    return dot / (math.sqrt(n1) * math.sqrt(n2))


def fun3(txt, k):
    dec = ""

    for i in range(len(txt)):
        x = (ord(txt[i]) - ord('A') - k) % 26
        dec += chr(x + ord('A'))

    return dec


def fun4(txt):
    n = len(txt)
    vec = [0] * 26

    for i in range(n):
        vec[ord(txt[i]) - ord('A')] += 1

    for i in range(26):
        vec[i] = vec[i] / n

    return vec


def fun5(sl):
    best_k = 0
    best_sc = -1

    for k in range(26):
        dec = fun3(sl, k)
        vec = fun4(dec)
        sc = fun2(vec, eng)

        if sc > best_sc:
            best_sc = sc
            best_k = k

    return best_k


def fun6(ct, key):
    pt = ""
    klen = len(key)

    for i in range(len(ct)):
        k = ord(key[i % klen]) - ord('A')
        x = (ord(ct[i]) - ord('A') - k) % 26
        pt += chr(x + ord('A'))

    return pt


MAX_LEN = 10         # this is my assumption. you can change it to any value you want. taking 30 is 
                     # giving the Estimated Key Length as 12 with recovered key as "PINCPINCPINC" which 
                     # also leads to same plaintext.

best_len = 0
best_diff = 12012   # my roll no :)

for klen in range(1, MAX_LEN + 1):

    grp = [""] * klen

    for i in range(len(given)):
        grp[i % klen] += given[i]

    sum_ioc = 0

    for i in range(klen):
        sum_ioc += fun1(grp[i])

    avg_ioc = sum_ioc / klen

    print("Length =", klen, "Average IoC =", avg_ioc)

    diff = abs(avg_ioc - 1.7)

    if diff < best_diff:
        best_diff = diff
        best_len = klen

print("\nEstimated Key Length =", best_len)

grp = [""] * best_len

for i in range(len(given)):
    grp[i % best_len] += given[i]

key = ""

for i in range(best_len):
    cur = fun5(grp[i])
    key += chr(cur + ord('A'))

print("Recovered Key =", key)

pt = fun6(given, key)

print("\nPlaintext:\n")
print(pt)
