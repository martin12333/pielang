#!/usr/bin/env python3

import sys

rtable = "[bcdfghjklmnpqrstvwxyz][aeiou]"

table1={"ba": "b́",
        "be": "[b]b[/b]",
        "bi": "[i]b[/i]",
        "bu": "[u]b[/u]",
        "by": "[i]b[/i]",
        "ca": "ć",
        "ce": "[b]c[/b]",
        "ci": "[i]c[/i]",
        "cu": "[u]c[/u]",
        "cy": "[i]c[/i]",
        "da": "d̗",
        "de": "[b]d[/b]",
        "di": "[i]d[/i]",
        "du": "[u]d[/u]",
        "dy": "[i]d[/i]",
        "fa": "f̗",
        "fe": "[b]f[/b]",
        "fi": "[i]f[/i]",
        "fu": "[u]f[/u]",
        "fy": "[i]f[/i]",
        "ga": "ǵ",
        "ge": "[b]g[/b]",
        "gi": "[i]g[/i]",
        "gu": "[u]g[/u]",
        "gy": "[i]g[/i]",
        "ha": "h́",
        "he": "[b]h[/b]",
        "hi": "[i]h[/i]",
        "hu": "[u]h[/u]",
        "hy": "[i]h[/i]",
        "ja": "j́",
        "je": "[b]j[/b]",
        "ji": "[i]j[/i]",
        "ju": "[u]j[/u]",
        "jy": "[i]j[/i]",
        "ka": "ḱ",
        "ke": "[b]k[/b]",
        "ki": "[i]k[/i]",
        "ku": "[u]k[/u]",
        "ky": "[i]k[/i]",
        "la": "l̗",
        "le": "[b]l[/b]",
        "li": "[i]l[/i]",
        "lu": "[u]l[/u]",
        "ly": "[i]l[/i]",
        "ma": "ḿ",
        "me": "[b]m[/b]",
        "mi": "[i]m[/i]",
        "mu": "[u]m[/u]",
        "my": "[i]m[/i]",
        "na": "ń",
        "ne": "[b]n[/b]",
        "ni": "[i]n[/i]",
        "nu": "[u]n[/u]",
        "ny": "[i]n[/i]",
        "pa": "ṕ",
        "pe": "[b]p[/b]",
        "pi": "[i]p[/i]",
        "pu": "[u]p[/u]",
        "py": "[i]p[/i]",
        "qa": "q́",
        "qe": "[b]q[/b]",
        "qi": "[i]q[/i]",
        "qu": "[u]q[/u]",
        "qy": "[i]q[/i]",
        "ra": "ŕ",
        "re": "[b]r[/b]",
        "ri": "[i]r[/i]",
        "ru": "[u]r[/u]",
        "ry": "[i]r[/i]",
        "sa": "ś",
        "se": "[b]s[/b]",
        "si": "[i]s[/i]",
        "su": "[u]s[/u]",
        "sy": "[i]s[/i]",
        "ta": "t̗",
        "te": "[b]t[/b]",
        "ti": "[i]t[/i]",
        "tu": "[u]t[/u]",
        "ty": "[i]t[/i]",
        "va": "v́",
        "ve": "[b]v[/b]",
        "vi": "[i]v[/i]",
        "vu": "[u]v[/u]",
        "vy": "[i]v[/i]",
        "wa": "ẃ",
        "we": "[b]w[/b]",
        "wi": "[i]w[/i]",
        "wu": "[u]w[/u]",
        "wy": "[i]w[/i]",
        "xa": "x́",
        "xe": "[b]x[/b]",
        "xi": "[i]x[/i]",
        "xu": "[u]x[/u]",
        "xy": "[i]x[/i]",
        "ya": "ý",
        "ye": "[b]y[/b]",
        "yi": "[i]y[/i]",
        "yu": "[u]y[/u]",
        "yy": "[i]y[/i]",
        "za": "ź",
        "ze": "[b]z[/b]",
        "zi": "[i]z[/i]",
        "zu": "[u]z[/u]",
        "zy": "[i]z[/i]"}

table2={"bo": "b̅",
        "co": "c̅",
        "do": "d̅",
        "fo": "f̅",
        "go": "g̅",
        "ho": "h̅",
        "jo": "j̅",
        "ko": "k̅",
        "lo": "l̅",
        "mo": "m̅",
        "no": "n̅",
        "po": "p̅",
        "qo": "q̅",
        "ro": "r̅",
        "so": "s̅",
        "to": "t̅",
        "vo": "v̅",
        "wo": "w̅",
        "xo": "x̅",
        "yo": "y̅",
        "zo": "z̅"}

table3={"ab": "°b́",
        "eb": "[b]°b[/b]",
        "ib": "[i]°b[/i]",
        "ub": "[u]°b[/u]",
        "yb": "[i]°b[/i]",
        "ac": "°ć",
        "ec": "[b]°c[/b]",
        "ic": "[i]°c[/i]",
        "uc": "[u]°c[/u]",
        "yc": "[i]°c[/i]",
        "ad": "°d̗",
        "ed": "[b]°d[/b]",
        "id": "[i]°d[/i]",
        "ud": "[u]°d[/u]",
        "yd": "[i]°d[/i]",
        "af": "°f̗",
        "ef": "[b]°f[/b]",
        "if": "[i]°f[/i]",
        "uf": "[u]°f[/u]",
        "yf": "[i]°f[/i]",
        "ag": "°ǵ",
        "eg": "[b]°g[/b]",
        "ig": "[i]°g[/i]",
        "ug": "[u]°g[/u]",
        "yg": "[i]°g[/i]",
        "ah": "°h́",
        "eh": "[b]°h[/b]",
        "ih": "[i]°h[/i]",
        "uh": "[u]°h[/u]",
        "yh": "[i]°h[/i]",
        "aj": "°j́",
        "ej": "[b]°j[/b]",
        "ij": "[i]°j[/i]",
        "uj": "[u]°j[/u]",
        "yj": "[i]°j[/i]",
        "ak": "°ḱ",
        "ek": "[b]°k[/b]",
        "ik": "[i]°k[/i]",
        "uk": "[u]°k[/u]",
        "yk": "[i]°k[/i]",
        "al": "°l̗",
        "el": "[b]°l[/b]",
        "il": "[i]°l[/i]",
        "ul": "[u]°l[/u]",
        "yl": "[i]°l[/i]",
        "am": "°ḿ",
        "em": "[b]°m[/b]",
        "im": "[i]°m[/i]",
        "um": "[u]°m[/u]",
        "ym": "[i]°m[/i]",
        "an": "°ń",
        "en": "[b]°n[/b]",
        "in": "[i]°n[/i]",
        "un": "[u]°n[/u]",
        "yn": "[i]°n[/i]",
        "ap": "°ṕ",
        "ep": "[b]°p[/b]",
        "ip": "[i]°p[/i]",
        "up": "[u]°p[/u]",
        "yp": "[i]°p[/i]",
        "aq": "°q́",
        "eq": "[b]°q[/b]",
        "iq": "[i]°q[/i]",
        "uq": "[u]°q[/u]",
        "yq": "[i]°q[/i]",
        "ar": "°ŕ",
        "er": "[b]°r[/b]",
        "ir": "[i]°r[/i]",
        "ur": "[u]°r[/u]",
        "yr": "[i]°r[/i]",
        "as": "°ś",
        "es": "[b]°s[/b]",
        "is": "[i]°s[/i]",
        "us": "[u]°s[/u]",
        "ys": "[i]°s[/i]",
        "at": "°t̗",
        "et": "[b]°t[/b]",
        "it": "[i]°t[/i]",
        "ut": "[u]°t[/u]",
        "yt": "[i]°t[/i]",
        "av": "°v́",
        "ev": "[b]°v[/b]",
        "iv": "[i]°v[/i]",
        "uv": "[u]°v[/u]",
        "yv": "[i]°v[/i]",
        "aw": "°ẃ",
        "ew": "[b]°w[/b]",
        "iw": "[i]°w[/i]",
        "uw": "[u]°w[/u]",
        "yw": "[i]°w[/i]",
        "ax": "°x́",
        "ex": "[b]°x[/b]",
        "ix": "[i]°x[/i]",
        "ux": "[u]°x[/u]",
        "yx": "[i]°x[/i]",
        "ay": "°ý",
        "ey": "[b]°y[/b]",
        "iy": "[i]°y[/i]",
        "uy": "[u]°y[/u]",
        "yy": "[i]°y[/i]",
        "az": "°ź",
        "ez": "[b]°z[/b]",
        "iz": "[i]°z[/i]",
        "uz": "[u]°z[/u]",
        "yz": "[i]°z[/i]"}

table4={"ob": "°b̅",
        "oc": "°c̅",
        "od": "°d̅",
        "of": "°f̅",
        "og": "°g̅",
        "oh": "°h̅",
        "oj": "°j̅",
        "ok": "°k̅",
        "ol": "°l̅",
        "om": "°m̅",
        "on": "°n̅",
        "op": "°p̅",
        "oq": "°q̅",
        "or": "°r̅",
        "os": "°s̅",
        "ot": "°t̅",
        "ov": "°v̅",
        "ow": "°w̅",
        "ox": "°x̅",
        "oy": "°y̅",
        "oz": "°z̅"}

table5={}

def decode(string):
    string = string.lower()
    brf = []
    nstring = string.split()
    for lstring in nstring:
        for dic in (table1,table2,table3,table4,table5):
            for key in dic.keys():
                if key in lstring:
                    lstring = lstring.replace(key, dic[key])
        brf.append(lstring)
    return "[font=DejaVu Sans]" + " ".join(brf) + "[/font]"

def main(argv=[]):
    x = " ".join(argv)
    if len(x) == 0:
        x = input("> ")
    while 1:
        print(decode(x))
        x = input("> ")

if __name__ == "__main__":
    main(sys.argv[1::])