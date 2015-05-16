from PIL import Image
from os import remove
from time import sleep
mapper = [
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
        if temp == i[0:3]:
            return i[3]

    const = 100

    if abs(r-g) < const and abs(r-b) < const and abs(g-b) < const and r < 80:
        return 0
    if abs(r-g) < const and abs(r-b) < const and abs(g-b) < const and r < 140:
        return 2
    if abs(r-g) < const and abs(r-b) < const and abs(g-b) < const and r < 200:
        return 1
    return 3

print "\n\n\t\tWelcome to the magic coder!!!"
print "\n This program can convert an image file(jpg, png supported) to a C program (Yup, that's right). It's not just a simple program, So just check it out!!!"
print "\n\nMake sure you have the image to be converted in the same folder as this executable.\n"
try:
	im = Image.open(raw_input("Imagename : "))  # Can be many different formats.
	pix = im.load()
except:
	print "Oops!!! some error occurred!! try again, and if the issue persists, do tell me abt it"
print "\nImage size:"
print im.size
im.convert("L").convert("RGB").resize((640, 480), Image.ANTIALIAS).save("bw.png")
im = Image.open("bw.png")
print "Image scaled to 640x480"
px = im.load()
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
__ oC0_[4] = {___,II_,I_I,III}, __r00=0, __r0O=0;_0o0_(o0_ *o_OO_o[]){__ O_O,_00_=0,o0o0o;o0_ f_n_[50],_i_[4000];FILE *f; for(O_O=strlen(o_OO_o[0])-5;*(o_OO_o[0]+O_O)!= '\\\\';O_O--){O0O*(o_OO_o[0]+O_O);}O0O'\\0';_00_--;strrev(f_n_);O0O'.';O0O'C';O0O'\\0';f=_0f, "r");f__,"%s",b__ while(1){f__,"%s",b__ f0r(_i_[0]=='*')break;for(o0o0o=0;o0o0o<strlen(b__ o0o0o++){f0r(_i_[o0o0o]!=','){_p(__r00,_cocl_ ++__r0O;f0r(__r0O==480){__r0O=0;__r00++;}}}}}main(__ a, o0_* o0o[]){__ gd=DETECT,gm;initgraph(&gd,&gm,"c:\\\\turboc3\\\\bgi");_0o0_(o0o);getch();closegraph();}
""";

data = open('C:\TurboC++\Disk\TurboC3\BIN\\00out.c', "w")
data = open(raw_input("Enter output filename: "), "w")
data.write("/*")
clcount = 0
print "Processing the image..."
for row in range(im.size[0]):
    data.write("\n")
    for col in range(im.size[1]):
        clcount += 1
        if (clcount%200)==0:
            data.write("\n")
        r, g, b = px[row, col]
        match = bestmatch(r, g, b)
        data.write(str(match)+",")
data.write("\n" + code)
print "Done image processing, applying the magic spell!!! :p"
sleep(1)
print "Doing some extra stuff..."
remove("bw.png")
sleep(0.5)
print "Done extra stuff!!!\n File saved. Copy it to the bin folder of turbo C, run it and see the magic.\n\nThank you :)\n\nA project by T90"