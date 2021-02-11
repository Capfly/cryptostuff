import vigenere
import cianalysis
import string

alphabet = string.ascii_uppercase + " "
tocrack = "NRPOYBVXBBWSJZPHSSSDXHXKCQWIJNUHVDLBQHYD WOQFASMFVFHXAJMB LYAZBVSODIXKAYSFBSAOJZJORJOZQTFNFVIHCESVDOOHAUBBS OTEPFWBTETSHXUXTDSUJOCESMYYBAFMYBOCEHFQCZEKFEXXFHIQTESJPYWDEOZ WSSSDDTKSCPQOTHMYXKXAXQFBSPOHBXVVODXKGNNZBGSASTEHS YVD AQRQTPJNFVFHXERZKOEOXKB DSJIVGLSWVXJXEFVKSXGJMRFWSXQFBSRSVPTJNIVFHSJDHATFNQHLGKSJWLFLFMYOXLGOQFBSROHXATGRVJPLWBTETFNUHVDLBQHYD WOQDTEOMYQOFBCMBBWWQVOKXWBVXVXFMYYWSRSVPOBSNE WSADHXXENQVETA ODXSASJUBILFMYBBS KTEHXAJHBVXAJXBQJODTEONBXQBXFSWQY KNODFVEOJSBZTAXJBBSFHIQTENFVIR SBQAIJQRQAPKNDBQFTNBOPHX JXBZFOMAQOOHAUBOSN"
#tocrack = "KIIBBTTTWP CXCZGRSTIKUDTTNJVEKUUWT V E PEKINVBMTHTCGRPOUEVEBBEZOEYOAEBUYGEIG OXEEUTWTIJVUYVEEBUXUAJUEYOSUJUWINYGNKZLWKNPOEMGNDG XWEBOUEVEBBEZOEYOFLGRKSIWBSPBS DIWXS GREBGRFEBOM VABQE VEBOUEF TBD XIOIECNEKGIUJEBWE VSMTTICCSHUEIEYOAEUOYGTWP XISJBINW ZKEBONFEHKTIEGNKZLWKNPB KGXDOAEHUPVEEBWPXLRYERTNRORKTNKG EBDRUOKWAZC ZZ AGTJH JQLWHERGSKPBWT GXRBNINW DCLKFE EHPB"
#tocrack = "HTAY SHZ VWZ CWUAJJZAU KAPFA BZN HMO KWNDWOAWJASOJZA GGC USYO VAY RAPL OHZ QUVAPDEN XKYLHPWB ZHNHFC HDEJW WBX".replace(" ", "")


def get_ics(language='de', keylength=3, ciphertext=""):
    ci_target = cianalysis.ci_all[language]
    ci_perletter = cianalysis.ci_perletter[language]
    results = [{}] * keylength

    # foreach key part
    for x in range(keylength):
        best = {'KEY': 0, 'INDEX': 1, 'DIFF': 1}
        v = ciphertext[x::keylength]
        for k in range(len(alphabet)):
            ic = 0
            for i in range(len(alphabet)):
                ic += ci_perletter[alphabet[i]] * v.count(alphabet[(i + k) % len(alphabet)]) / len(v)
            diff = abs(ci_target - ic)
            if diff < best['DIFF']:
                best = {'KEY@'+str(x): alphabet[k], 'INDEX': ic, 'DIFF': diff}
                results[x] = {'KEY@'+str(x): alphabet[k], 'INDEX': ic, 'DIFF': diff}

    return results


if __name__ == '__main__':
    print("ANALYZING: " + tocrack)
    ics = get_ics(keylength=6, ciphertext=tocrack, language="de")
    sol = ""
    for i in range(len(ics)):
        print(ics[i])
        sol += ics[i]["KEY@"+str(i)]

    print("DECRYPT WITH: " + sol)
    print(vigenere.decrypt(tocrack, sol))
