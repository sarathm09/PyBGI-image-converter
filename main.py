from PIL import Image
import math

bgi_cols = [
    ["BLACK", 0, 0, 0, 0],
    ["BLUE", 1, 0, 0, 255],
    ["GREEN",  2, 0, 255, 0],
    ["CYAN", 3, 0, 255, 255],
    ["RED", 4, 255, 0, 0],
    ["MAGENTA", 5, 255, 0, 255],
    ["BROWN", 6, 139, 35, 35],
    ["LIGHTGRAY", 7, 170, 170, 170],
    ["DARKGRAY", 8, 40, 40, 40],
    ["LIGHTBLUE", 9, 173, 216, 230],
    ["LIGHTGREEN", 10, 144, 238, 144],
    ["LIGHTCYAN", 11, 224, 255, 255],
    ["LIGHTRED", 12, 238, 162, 173],
    ["LIGHTMAGENTA", 13, 255, 225, 255],
    ["YELLOW", 14, 255, 255, 0],
    ["WHITE", 15, 255, 255, 255]
]

mapper = [
    # [-1, 0, 0, 4],
    # [0, -1, 0, 2],
    # [0, 0, -1, 1],
    #
    # [-1, -1, 0, 14],
    # [0, -1, -1, 3],
    # [-1, 0, -1, 5],

    [0, 0, 0, 0, 0],
    [255, 255, 255, 3, 15]
]

def bestmatch(r, g, b):
    temp = [-1, -1, -1]
    temp[0] = 0 if r == 0 else -1
    temp[1] = 0 if g == 0 else -1
    temp[2] = 0 if b == 0 else -1

    temp[0] = 255 if r == 255 else temp[0]
    temp[1] = 255 if g == 255 else temp[1]
    temp[2] = 255 if b == 255 else temp[2]

    for i in mapper:
        # print i[0:3], temp
        if temp == i[0:3]:
            return i[3]
            # if i[3] == 15:
            #     return "_II"
            # elif i[3] == 0:
            #     return "III"
            # elif i[3] == 7:
            #     return "II_"
            # elif i[3] == 8:
            #     return "I_I"

    const = 100

    if abs(r-g) < const and abs(r-b) < const and abs(g-b) < const and r < 80:
        return 0
        # return 0
        # return "III"

    if abs(r-g) < const and abs(r-b) < const and abs(g-b) < const and r < 140:
        return 2
        # return 8
        # return "I_I"

    if abs(r-g) < const and abs(r-b) < const and abs(g-b) < const and r < 200:
        return 1
        # return "II_"
        # return 7

    return 3
    # return "_II"
    return 15
    #
    # minval = max([r, g, b])
    # if minval == r:
    #     return 4
    # if minval == g:
    #     return 2
    # if minval == b:
    #     return 1

im = Image.open(raw_input("Imagename : "))  # Can be many different formats.
pix = im.load()
print im.size  # Get the width and hight of the image for iterating over
# for r in range(im.size[0]):
#     for c in range(im.size[1]):
#         print r, c, pix[r, c]

im.convert("L").convert("RGB").resize((640, 480), Image.ANTIALIAS).save("bw.png")
im = Image.open("bw.png")
px = im.load()

cpp = open("grp.c", "w")
code = """*/
// That sure was a long comment :p
// Now into the real program :)
#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<graphics.h>
#define f0r if
#define __ int
#define o0_ char
#define b__ _i_);
#define _p putpixel
#define III (2<<3)-1
#define I_I (2<<2)-0
#define II_ (2<<2)-1
#define ___ (2<<0)-2
#define f__ fscanf(f
#define _0f fopen(f_n_
#define O0O f_n_[_00_++]=
#define _cocl_ __r0O,oC0_[_i_[o0o0o]-48]);
// One line magic :)
__ oC0_[4] = {___,II_,I_I,III}, __r00=0, __r0O=0;_0o0_(o0_ *o_OO_o[]){__ O_O,_00_=0,o0o0o;o0_ f_n_[50],_i_[4000];FILE *f; for(O_O=strlen(o_OO_o[0])-5;*(o_OO_o[0]+O_O)!= '\\';O_O--){O0O*(o_OO_o[0]+O_O);}O0O'\0';_00_--;strrev(f_n_);O0O'.';O0O'C';O0O'\0';f=_0f, "r");f__,"%s",b__ while(1){f__,"%s",b__ f0r(_i_[0]=='*')break;for(o0o0o=0;o0o0o<strlen(b__ o0o0o++){f0r(_i_[o0o0o]!=','){_p(__r00,_cocl_ ++__r0O;f0r(__r0O==480){__r0O=0;__r00++;}}}}}main(__ a, o0_* o0o[]){__ gd=DETECT,gm;initgraph(&gd,&gm,"c:\\turboc3\\bgi");_0o0_(o0o);getch();closegraph();}
""";

data = open('C:\TurboC++\Disk\TurboC3\BIN\data.txt', "w")
data = open('data.txt', "w")
clcount = 0
for row in range(im.size[0]):
    cpp.write("\n")
    data.write("\n")
    for col in range(im.size[1]):
        clcount += 1
        if (clcount%200)==0:
            data.write("\n")
        r, g, b = px[row, col]
        match = bestmatch(r, g, b)
        data.write(str(match)+",")
cpp.write("\n\n\tgetch();\n\tclosegraph();\n}")
