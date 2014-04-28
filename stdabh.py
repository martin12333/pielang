#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# "Standard Abugida (HTML)"

import sys

rtable = "<bcdfghjklmnpqrstvwxyz><aeiou>"

table0={"y": "i"}

table1={"ba": "<hr='#'>b</hr>",
        "be": "<b>b</b>",
        "bi": "<f>b</f>",
        "bu": "<v>b</v>",
        "by": "<f>b</f>",
        "ca": "<hr='#'>c</hr>",
        "ce": "<b>c</b>",
        "ci": "<f>c</f>",
        "cu": "<v>c</v>",
        "cy": "<f>c</f>",
        "da": "<hr='#'>d</hr>",
        "de": "<b>d</b>",
        "di": "<f>d</f>",
        "du": "<v>d</v>",
        "dy": "<f>d</f>",
        "fa": "<hr='#'>f</hr>",
        "fe": "<b>f</b>",
        "fi": "<f>f</f>",
        "fu": "<v>f</v>",
        "fy": "<f>f</f>",
        "ga": "<hr='#'>g</hr>",
        "ge": "<b>g</b>",
        "gi": "<f>g</f>",
        "gu": "<v>g</v>",
        "gy": "<f>g</f>",
        "ha": "<hr='#'>h</hr>",
        "he": "<b>h</b>",
        "hi": "<f>h</f>",
        "hu": "<v>h</v>",
        "hy": "<f>h</f>",
        "ja": "<hr='#'>j</hr>",
        "je": "<b>j</b>",
        "ji": "<f>j</f>",
        "ju": "<v>j</v>",
        "jy": "<f>j</f>",
        "ka": "<hr='#'>k</hr>",
        "ke": "<b>k</b>",
        "ki": "<f>k</f>",
        "ku": "<v>k</v>",
        "ky": "<f>k</f>",
        "la": "<hr='#'>l</hr>",
        "le": "<b>l</b>",
        "li": "<f>l</f>",
        "lu": "<v>l</v>",
        "ly": "<f>l</f>",
        "ma": "<hr='#'>m</hr>",
        "me": "<b>m</b>",
        "mi": "<f>m</f>",
        "mu": "<v>m</v>",
        "my": "<f>m</f>",
        "na": "<hr='#'>n</hr>",
        "ne": "<b>n</b>",
        "ni": "<f>n</f>",
        "nu": "<v>n</v>",
        "ny": "<f>n</f>",
        "pa": "<hr='#'>p</hr>",
        "pe": "<b>p</b>",
        "pi": "<f>p</f>",
        "pu": "<v>p</v>",
        "py": "<f>p</f>",
        "qa": "<hr='#'>q</hr>",
        "qe": "<b>q</b>",
        "qi": "<f>q</f>",
        "qu": "<v>q</v>",
        "qy": "<f>q</f>",
        "ra": "<hr='#'>r</hr>",
        "re": "<b>r</b>",
        "ri": "<f>r</f>",
        "ru": "<v>r</v>",
        "ry": "<f>r</f>",
        "sa": "<hr='#'>s</hr>",
        "se": "<b>s</b>",
        "si": "<f>s</f>",
        "su": "<v>s</v>",
        "sy": "<f>s</f>",
        "ta": "<hr='#'>t</hr>",
        "te": "<b>t</b>",
        "ti": "<f>t</f>",
        "tu": "<v>t</v>",
        "ty": "<f>t</f>",
        "va": "<hr='#'>v</hr>",
        "ve": "<b>v</b>",
        "vi": "<f>v</f>",
        "vu": "<v>v</v>",
        "vy": "<f>v</f>",
        "wa": "<hr='#'>w</hr>",
        "we": "<b>w</b>",
        "wi": "<f>w</f>",
        "wu": "<v>w</v>",
        "wy": "<f>w</f>",
        "xa": "<hr='#'>x</hr>",
        "xe": "<b>x</b>",
        "xi": "<f>x</f>",
        "xu": "<v>x</v>",
        "xy": "<f>x</f>",
        "ya": "<hr='#'>y</hr>",
        "ye": "<b>y</b>",
        "yi": "<f>y</f>",
        "yu": "<v>y</v>",
        "yy": "<f>y</f>",
        "za": "<hr='#'>z</hr>",
        "ze": "<b>z</b>",
        "zi": "<f>z</f>",
        "zu": "<v>z</v>",
        "zy": "<f>z</f>"}

table2={"bo": "<s>b</s>",
        "co": "<s>c</s>",
        "do": "<s>d</s>",
        "fo": "<s>f</s>",
        "go": "<s>g</s>",
        "ho": "<s>h</s>",
        "jo": "<s>j</s>",
        "ko": "<s>k</s>",
        "lo": "<s>l</s>",
        "mo": "<s>m</s>",
        "no": "<s>n</s>",
        "po": "<s>p</s>",
        "qo": "<s>q</s>",
        "ro": "<s>r</s>",
        "so": "<s>s</s>",
        "to": "<s>t</s>",
        "vo": "<s>v</s>",
        "wo": "<s>w</s>",
        "xo": "<s>x</s>",
        "yo": "<s>y</s>",
        "zo": "<s>z</s>"}

table3={"ab": "<hr='#'>&#176;b</hr>",
        "eb": "<b>&#176;b</b>",
        "ib": "<f>&#176;b</f>",
        "ub": "<v>&#176;b</v>",
        "yb": "<f>&#176;b</f>",
        "ac": "<hr='#'>&#176;c</hr>",
        "ec": "<b>&#176;c</b>",
        "ic": "<f>&#176;c</f>",
        "uc": "<v>&#176;c</v>",
        "yc": "<f>&#176;c</f>",
        "ad": "<hr='#'>&#176;d</hr>",
        "ed": "<b>&#176;d</b>",
        "id": "<f>&#176;d</f>",
        "ud": "<v>&#176;d</v>",
        "yd": "<f>&#176;d</f>",
        "af": "<hr='#'>&#176;f</hr>",
        "ef": "<b>&#176;f</b>",
        "if": "<f>&#176;f</f>",
        "uf": "<v>&#176;f</v>",
        "yf": "<f>&#176;f</f>",
        "ag": "<hr='#'>&#176;g</hr>",
        "eg": "<b>&#176;g</b>",
        "ig": "<f>&#176;g</f>",
        "ug": "<v>&#176;g</v>",
        "yg": "<f>&#176;g</f>",
        "ah": "<hr='#'>&#176;h</hr>",
        "eh": "<b>&#176;h</b>",
        "ih": "<f>&#176;h</f>",
        "uh": "<v>&#176;h</v>",
        "yh": "<f>&#176;h</f>",
        "aj": "<hr='#'>&#176;j</hr>",
        "ej": "<b>&#176;j</b>",
        "ij": "<f>&#176;j</f>",
        "uj": "<v>&#176;j</v>",
        "yj": "<f>&#176;j</f>",
        "ak": "<hr='#'>&#176;k</hr>",
        "ek": "<b>&#176;k</b>",
        "ik": "<f>&#176;k</f>",
        "uk": "<v>&#176;k</v>",
        "yk": "<f>&#176;k</f>",
        "al": "<hr='#'>&#176;l</hr>",
        "el": "<b>&#176;l</b>",
        "il": "<f>&#176;l</f>",
        "ul": "<v>&#176;l</v>",
        "yl": "<f>&#176;l</f>",
        "am": "<hr='#'>&#176;m</hr>",
        "em": "<b>&#176;m</b>",
        "im": "<f>&#176;m</f>",
        "um": "<v>&#176;m</v>",
        "ym": "<f>&#176;m</f>",
        "an": "<hr='#'>&#176;n</hr>",
        "en": "<b>&#176;n</b>",
        "in": "<f>&#176;n</f>",
        "un": "<v>&#176;n</v>",
        "yn": "<f>&#176;n</f>",
        "ap": "<hr='#'>&#176;p</hr>",
        "ep": "<b>&#176;p</b>",
        "ip": "<f>&#176;p</f>",
        "up": "<v>&#176;p</v>",
        "yp": "<f>&#176;p</f>",
        "aq": "<hr='#'>&#176;q</hr>",
        "eq": "<b>&#176;q</b>",
        "iq": "<f>&#176;q</f>",
        "uq": "<v>&#176;q</v>",
        "yq": "<f>&#176;q</f>",
        "ar": "<hr='#'>&#176;r</hr>",
        "er": "<b>&#176;r</b>",
        "ir": "<f>&#176;r</f>",
        "ur": "<v>&#176;r</v>",
        "yr": "<f>&#176;r</f>",
        "as": "<hr='#'>&#176;s</hr>",
        "es": "<b>&#176;s</b>",
        "is": "<f>&#176;s</f>",
        "us": "<v>&#176;s</v>",
        "ys": "<f>&#176;s</f>",
        "at": "<hr='#'>&#176;t</hr>",
        "et": "<b>&#176;t</b>",
        "it": "<f>&#176;t</f>",
        "ut": "<v>&#176;t</v>",
        "yt": "<f>&#176;t</f>",
        "av": "<hr='#'>&#176;v</hr>",
        "ev": "<b>&#176;v</b>",
        "iv": "<f>&#176;v</f>",
        "uv": "<v>&#176;v</v>",
        "yv": "<f>&#176;v</f>",
        "aw": "<hr='#'>&#176;w</hr>",
        "ew": "<b>&#176;w</b>",
        "iw": "<f>&#176;w</f>",
        "uw": "<v>&#176;w</v>",
        "yw": "<f>&#176;w</f>",
        "ax": "<hr='#'>&#176;x</hr>",
        "ex": "<b>&#176;x</b>",
        "ix": "<f>&#176;x</f>",
        "ux": "<v>&#176;x</v>",
        "yx": "<f>&#176;x</f>",
        "ay": "<hr='#'>&#176;y</hr>",
        "ey": "<b>&#176;y</b>",
        "iy": "<f>&#176;y</f>",
        "uy": "<v>&#176;y</v>",
        "yy": "<f>&#176;y</f>",
        "az": "<hr='#'>&#176;z</hr>",
        "ez": "<b>&#176;z</b>",
        "iz": "<f>&#176;z</f>",
        "uz": "<v>&#176;z</v>",
        "yz": "<f>&#176;z</f>"}

table4={"ob": "<s>&#176;b</s>",
        "oc": "<s>&#176;c</s>",
        "od": "<s>&#176;d</s>",
        "of": "<s>&#176;f</s>",
        "og": "<s>&#176;g</s>",
        "oh": "<s>&#176;h</s>",
        "oj": "<s>&#176;j</s>",
        "ok": "<s>&#176;k</s>",
        "ol": "<s>&#176;l</s>",
        "om": "<s>&#176;m</s>",
        "on": "<s>&#176;n</s>",
        "op": "<s>&#176;p</s>",
        "oq": "<s>&#176;q</s>",
        "or": "<s>&#176;r</s>",
        "os": "<s>&#176;s</s>",
        "ot": "<s>&#176;t</s>",
        "ov": "<s>&#176;v</s>",
        "ow": "<s>&#176;w</s>",
        "ox": "<s>&#176;x</s>",
        "oy": "<s>&#176;y</s>",
        "oz": "<s>&#176;z</s>"}

table5={"a": "&#945;",
        "e": "&#949;",
        "i": "&#953;",
        "o": "&#959;",
        "u": "&#965;"}

table6={"<s>": "<strike>",
        "</s>": "</strike>",
        "<f>": "<i>",
        "</f>": "</i>",
        "<hr='#'>": "<a style='text-decoration: none;' href='#'>",
        "</hr>": "</a>",
        "<v>": "<u>",
        "</v>": "</u>"}

table7=["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

def decode(string):
    brf = []
    nstring = string.split()
    for lstring in nstring:
        for dic in (table0,table1,table2,table3,table4,table5,table6,table7):
            if type(dic) is list:
                for char in dic:
                    lstring = lstring.replace(char, "&#8593;" + char.lower())
            else:
                for key in dic.keys():
                    if key in lstring:
                        lstring = lstring.replace(key, dic[key])
                    if key.capitalize() in lstring:
                        r = dic[key]
                        if "</" in r:
                            lstring = lstring.replace(key.capitalize(), r.replace(">", ">&#8593;", 1))
                        else:
                            lstring = lstring.replace(key.capitalize(), "&#8593;" + r)
        brf.append(lstring)
    return " ".join(brf)

def main(argv=[]):
    print("Standard Abugida Converter (Python %s)" % (sys.version,))
    x = " ".join(argv)
    if len(x) == 0:
        x = input(">>> ")
    while 1:
        print(decode(x))
        x = input(">>> ")

if __name__ == "__main__":
    main(sys.argv[1::])
