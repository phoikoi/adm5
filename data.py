# Glyphs file for ADM5 terminal fonts

DOT_COLUMNS = 8.0
DOT_ROWS = 10.0
ROW_OFFSET = 0.0
ASPECT_RATIO = 1.66

lowGlyphNames = """
space exclam quotedbl numbersign dollar percent
ampersand quotesingle parenleft parenright asterisk
plus comma hyphen period slash zero one two three
four five six seven eight nine colon semicolon less
equal greater question at A B C D E F G H I J K L M N
O P Q R S T U V W X Y Z bracketleft backslash
bracketright asciicircum underscore grave a b c d e f
g h i j k l m n o p q r s t u v w x y z braceleft bar
braceright asciitilde
"""

highGlyphNames = """
exclamdown cent sterling currency yen brokenbar section
dieresis copyright ordfeminine guillemotleft logicalnot
registered macron degree plusminus twosuperior
threesuperior acute uni00B5 paragraph periodcentered
cedilla onesuperior ordmasculine guillemotright
onequarter onehalf threequarters questiondown
Agrave Aacute Acircumflex Atilde Adieresis Aring AE
Ccediila Egrave Eacute Ecircumflex Edieresis Igrave
Iacute Icircumflex Idieresis Eth Ntilde Ograve Oacute
Ocircumflex Otilde Odieresis multiply Oslash Ugrave
Uacute Ucircumflex Udieresis Yacute Thorn germandbls
agrave aacute acircumflex atilde adieresis aring ae
ccediila egrave eacute ecircumflex edieresis igrave
iacute icircumflex idieresis eth ntilde ograve oacute
ocircumflex otilde odieresis divide oslash ugrave
uacute ucircumflex udieresis yacute thorn ydieresis
dotlessi Lslash lslash OE oe Scaron scaron Ydieresis
Zcaron zcaron florin circumflex caron breve dotaccent
ring ogonek tilde hungarumlaut endash emdash quoteleft
quoteright quotesinglbase quotedblleft quotedblright
quotedblbase dagger daggerdbl bullet ellipsis
perthousand guilsinglleft guilsinglright fraction Euro
trademark minus fi fl
"""

#glyphNames = lowGlyphNames.split() + highGlyphNames.split()
glyphNames = lowGlyphNames.split()

glyphRanges = [
    [0x0020, 0x007e], # ASCII printables
    # [0x00a1, 0x00ff], # Upper 128 printables
    # [0x0131, 0x0131], # dotlessi
    # [0x0141, 0x0142], # Lslash, lslash
    # [0x0152, 0x0153], # OE, oe
    # [0x0160, 0x0161], # Scaron, scaron
    # [0x0178, 0x0178], # Ydieresis
    # [0x017d, 0x017e], # Zcaron, zcaron
    # [0x0192, 0x0192], # florin
    # [0x02c6, 0x02c7], # circumflex, caron
    # [0x02d8, 0x02dd], # breve - hungarumlaut
    # [0x2013, 0x2014], # endash, emdash
    # [0x2018, 0x201e], # quotation marks
    # [0x2020, 0x2022], # daggers and bullet
    # [0x2026, 0x2026], # ellipsis
    # [0x2030, 0x2030], # perthousand
    # [0x2039, 0x203a], # guilsingles
    # [0x2044, 0x2044], # fraction
    # [0x20ac, 0x20ac], # Euro
    # [0x2122, 0x2122], # trademark
    # [0x2212, 0x2212], # minus
#    [0xE0A0, 0xE0A2],
#    [0xE0B0, 0xE0B3],
    # [0xfb01, 0xfb02], # fi and fl
]

glyphIndexes = []
for x in glyphRanges:
    glyphIndexes.extend(range(x[0], x[1]+1))

glyphs = {x[0]:{'unicode':x[1]} for x in zip(glyphNames, glyphIndexes)}    

romanBitmaps = {
 "space":
"""
........
........
........
........
........
........
........
........
........
........
""",
    "exclam":
"""
........
....@...
....@...
....@...
....@...
....@...
........
....@...
........
........
""",
    "quotedbl":
"""
........
...@.@..
...@.@..
...@.@..
........
........
........
........
........
........
""",
    "numbersign":
"""
........
...@.@..
...@.@..
..@@@@@.
...@.@..
..@@@@@.
...@.@..
...@.@..
........
........
""",
    "dollar":
"""
........
....@...
...@@@@.
..@.@...
...@@@..
....@.@.
..@@@@..
....@...
........
........
""",
    "percent":
"""
........
..@@..@.
..@@..@.
.....@..
....@...
...@....
..@..@@.
..@..@@.
........
........
""",
    "ampersand":
"""
........
....@...
...@.@..
...@.@..
...@@...
..@.@.@.
..@..@..
...@@.@.
........
........
""",
    "quotesingle":
"""
........
.....@..
....@...
...@....
........
........
........
........
........
........
""",
    "parenleft":
"""
........
.....@..
....@...
...@....
...@....
...@....
....@...
.....@..
........
........
""",
    "parenright":
"""
........
...@....
....@...
.....@..
.....@..
.....@..
....@...
...@....
........
........
""",
    "asterisk":
"""
........
........
....@...
..@.@.@.
...@@@..
..@.@.@.
....@...
........
........
........
""",
    "plus":
"""
........
........
....@...
....@...
..@@@@@.
....@...
....@...
........
........
........
""",
    "comma":
"""
........
........
........
........
........
........
........
....@...
....@...
...@....
""",
    "hyphen":
"""
........
........
........
........
..@@@@@.
........
........
........
........
........
""",
    "period":
"""
........
........
........
........
........
........
........
....@...
........
........
""",
    "slash":
"""
........
......@.
......@.
.....@..
....@...
...@....
..@.....
..@.....
........
........
""",
    "zero":
"""
........
...@@@..
..@...@.
..@..@@.
..@.@.@.
..@@..@.
..@...@.
...@@@..
........
........
""",
    "one":
"""
........
....@...
...@@...
....@...
....@...
....@...
....@...
...@@@..
........
........
""",
    "two":
"""
........
...@@@..
..@...@.
......@.
...@@@..
..@.....
..@.....
..@@@@@.
........
........
""",
    "three":
"""
........
...@@@..
..@...@.
......@.
....@@..
......@.
..@...@.
...@@@..
........
........
""",
    "four":
"""
........
.....@..
....@@..
...@.@..
..@..@..
..@@@@@.
.....@..
.....@..
........
........
""",
    "five":
"""
........
..@@@@@.
..@.....
..@@@@..
......@.
......@.
..@...@.
...@@@..
........
........
""",
    "six":
"""
........
....@@..
...@....
..@.....
..@@@@..
..@...@.
..@...@.
...@@@..
........
........
""",
    "seven":
"""
........
..@@@@@.
......@.
.....@..
....@...
...@....
...@....
...@....
........
........
""",
    "eight":
"""
........
...@@@..
..@...@.
..@...@.
...@@@..
..@...@.
..@...@.
...@@@..
........
........
""",
    "nine":
"""
........
...@@@..
..@...@.
..@...@.
...@@@@.
......@.
.....@..
...@@...
........
........
""",
    "colon":
"""
........
........
........
....@...
........
........
....@...
........
........
........
""",
    "semicolon":
"""
........
........
........
....@...
........
........
....@...
....@...
...@....
........
""",
    "less":
"""
........
......@.
.....@..
....@...
...@....
....@...
.....@..
......@.
........
........
""",
    "equal":
"""
........
........
........
..@@@@@.
........
..@@@@@.
........
........
........
........
""",
    "greater":
"""
........
..@.....
...@....
....@...
.....@..
....@...
...@....
..@.....
........
........
""",
    "question":
"""
........
...@@@..
..@...@.
......@.
.....@..
....@...
........
....@...
........
........
""",
    "at":
"""
........
....@@..
...@..@.
..@.@.@.
..@.@@@.
..@.@...
..@.....
...@@@@.
........
........
""",
    "A":
"""
........
....@...
...@.@..
..@...@.
..@...@.
..@@@@@.
..@...@.
..@...@.
........
........
""",
    "B":
"""
........
..@@@@..
..@...@.
..@...@.
..@@@@..
..@...@.
..@...@.
..@@@@..
........
........
""",
    "C":
"""
........
...@@@..
..@...@.
..@.....
..@.....
..@.....
..@...@.
...@@@..
........
........
""",
    "D":
"""
........
..@@@...
..@..@..
..@...@.
..@...@.
..@...@.
..@..@..
..@@@...
........
........
""",
    "E":
"""
........
..@@@@@.
..@.....
..@.....
..@@@@..
..@.....
..@.....
..@@@@@.
........
........
""",
    "F":
"""
........
..@@@@@.
..@.....
..@.....
..@@@@..
..@.....
..@.....
..@.....
........
........
""",
    "G":
"""
........
...@@@@.
..@.....
..@.....
..@.....
..@..@@.
..@...@.
...@@@@.
........
........
""",
    "H":
"""
........
..@...@.
..@...@.
..@...@.
..@@@@@.
..@...@.
..@...@.
..@...@.
........
........
""",
    "I":
"""
........
...@@@..
....@...
....@...
....@...
....@...
....@...
...@@@..
........
........
""",
    "J":
"""
........
......@.
......@.
......@.
......@.
......@.
..@...@.
...@@@..
........
........
""",
    "K":
"""
........
..@...@.
..@..@..
..@.@...
..@@....
..@.@...
..@..@..
..@...@.
........
........
""",
    "L":
"""
........
..@.....
..@.....
..@.....
..@.....
..@.....
..@.....
..@@@@@.
........
........
""",
    "M":
"""
........
..@...@.
..@@.@@.
..@.@.@.
..@.@.@.
..@...@.
..@...@.
..@...@.
........
........
""",
    "N":
"""
........
..@...@.
..@...@.
..@@..@.
..@.@.@.
..@..@@.
..@...@.
..@...@.
........
........
""",
    "O":
"""
........
...@@@..
..@...@.
..@...@.
..@...@.
..@...@.
..@...@.
...@@@..
........
........
""",
    "P":
"""
........
..@@@@..
..@...@.
..@...@.
..@@@@..
..@.....
..@.....
..@.....
........
........
""",
    "Q":
"""
........
...@@@..
..@...@.
..@...@.
..@...@.
..@.@.@.
..@..@..
...@@.@.
........
........
""",
    "R":
"""
........
..@@@@..
..@...@.
..@...@.
..@@@@..
..@.@...
..@..@..
..@...@.
........
........
""",
    "S":
"""
........
...@@@..
..@...@.
..@.....
...@@@..
......@.
..@...@.
...@@@..
........
........
""",
    "T":
"""
........
..@@@@@.
....@...
....@...
....@...
....@...
....@...
....@...
........
........
""",
    "U":
"""
........
..@...@.
..@...@.
..@...@.
..@...@.
..@...@.
..@...@.
...@@@..
........
........
""",
    "V":
"""
........
..@...@.
..@...@.
..@...@.
..@...@.
..@...@.
...@.@..
....@...
........
........
""",
    "W":
"""
........
..@...@.
..@...@.
..@...@.
..@.@.@.
..@.@.@.
..@@@@@.
..@...@.
........
........
""",
    "X":
"""
........
..@...@.
..@...@.
...@.@..
....@...
...@.@..
..@...@.
..@...@.
........
........
""",
    "Y":
"""
........
..@...@.
..@...@.
...@.@..
....@...
....@...
....@...
....@...
........
........
""",
    "Z":
"""
........
..@@@@@.
......@.
.....@..
....@...
...@....
..@.....
..@@@@@.
........
........
""",
    "bracketleft":
"""
........
....@@@.
....@...
....@...
....@...
....@...
....@...
....@@@.
........
........
""",
    "backslash":
"""
........
..@.....
..@.....
...@....
....@...
.....@..
......@.
......@.
........
........
""",
    "bracketright":
"""
........
..@@@...
....@...
....@...
....@...
....@...
....@...
..@@@...
........
........
""",
    "asciicircum":
"""
........
....@...
...@.@..
..@...@.
........
........
........
........
........
........
""",
    "underscore":
"""
........
........
........
........
........
........
........
..@@@@@.
........
........
""",
    "grave":
"""
........
...@....
....@...
.....@..
........
........
........
........
........
........
""",
    "a":
"""
........
........
........
...@@.@.
..@..@@.
..@...@.
..@..@@.
...@@.@.
........
........
""",
    "b":
"""
........
..@.....
..@.....
..@.@@..
..@@..@.
..@...@.
..@@..@.
..@.@@..
........
........
""",
    "c":
"""
........
........
........
...@@@@.
..@.....
..@.....
..@.....
...@@@@.
........
........
""",
    "d":
"""
........
......@.
......@.
...@@.@.
..@..@@.
..@...@.
..@..@@.
...@@.@.
........
........
""",
    "e":
"""
........
........
........
...@@@..
..@...@.
..@@@@@.
..@.....
...@@@..
........
........
""",
    "f":
"""
........
....@...
...@.@..
...@....
..@@@...
...@....
...@....
...@....
........
........
""",
    "g":
"""
........
........
........
...@@.@.
..@..@@.
..@...@.
..@..@@.
...@@.@.
......@.
...@@@..
""",
    "h":
"""
........
..@.....
..@.....
..@.@@..
..@@..@.
..@...@.
..@...@.
..@...@.
........
........
""",
    "i":
"""
........
....@...
........
...@@...
....@...
....@...
....@...
...@@@..
........
........
""",
    "j":
"""
........
......@.
........
......@.
......@.
......@.
......@.
......@.
...@..@.
....@@..
""",
    "k":
"""
........
..@.....
..@.....
..@..@..
..@.@...
..@@....
..@.@...
..@..@..
........
........
""",
    "l":
"""
........
...@@...
....@...
....@...
....@...
....@...
....@...
...@@@..
........
........
""",
    "m":
"""
........
........
........
..@@.@..
..@.@.@.
..@.@.@.
..@.@.@.
..@.@.@.
........
........
""",
    "n":
"""
........
........
........
..@.@@..
..@@..@.
..@...@.
..@...@.
..@...@.
........
........
""",
    "o":
"""
........
........
........
...@@@..
..@...@.
..@...@.
..@...@.
...@@@..
........
........
""",
    "p":
"""
........
........
........
..@.@@..
..@@..@.
..@...@.
..@@..@.
..@.@@..
..@.....
..@.....
""",
    "q":
"""
........
........
........
...@@.@.
..@..@@.
..@...@.
..@..@@.
...@@.@.
......@.
......@.
""",
    "r":
"""
........
........
........
..@.@@..
..@@..@.
..@.....
..@.....
..@.....
........
........
""",
    "s":
"""
........
........
........
...@@@@.
..@.....
...@@@..
......@.
..@@@@..
........
........
""",
    "t":
"""
........
...@....
...@....
..@@@...
...@....
...@....
...@.@..
....@...
........
........
""",
    "u":
"""
........
........
........
..@...@.
..@...@.
..@...@.
..@..@@.
...@@.@.
........
........
""",
    "v":
"""
........
........
........
..@...@.
..@...@.
..@...@.
...@.@..
....@...
........
........
""",
    "w":
"""
........
........
........
..@...@.
..@...@.
..@.@.@.
..@.@.@.
...@.@..
........
........
""",
    "x":
"""
........
........
........
..@...@.
...@.@..
....@...
...@.@..
..@...@.
........
........
""",
    "y":
"""
........
........
........
..@...@.
..@...@.
..@...@.
..@..@@.
...@@.@.
......@.
...@@@..
""",
    "z":
"""
........
........
........
..@@@@@.
.....@..
....@...
...@....
..@@@@@.
........
........
""",
    "braceleft":
"""
........
.....@@.
....@...
....@...
..@@....
....@...
....@...
.....@@.
........
........
""",
    "bar":
"""
........
....@...
....@...
....@...
........
....@...
....@...
....@...
........
........
""",
    "braceright":
"""
........
..@@....
....@...
....@...
.....@@.
....@...
....@...
..@@...
........
........
""",
    "asciitilde":
"""
........
...@....
..@.@.@.
.....@..
........
........
........
........
........
........
""",
}

powerline_bitmaps = {
    0xE0A0:
"""
........
..@..@..
..@.@@@.
..@..@..
..@..@..
..@..@..
..@..@..
....@...
..@@....
........
""",
    0xE0A1:
"""
........
..@.....
..@.....
..@.....
..@@@...
...@..@.
...@@.@.
...@.@@.
...@..@.
........
""",
    0xE0A2:
"""
........
...@@@..
..@...@.
..@@@@@.
..@...@.
..@@.@@.
..@@.@@.
..@@@@@.
........
........
""",
    0xE0B0:
"""
..@.....
..@@....
..@@@...
..@@@@..
..@@@@@.
..@@@@..
..@@@...
..@@....
..@.....
........
""",
    0xE0B1:
"""
..@.....
...@....
....@...
.....@..
......@.
.....@..
....@...
...@....
..@.....
........
""",
    0xE0B2:
"""
......@.
.....@@.
....@@@.
...@@@@.
..@@@@@.
...@@@@.
....@@@.
.....@@.
......@.
........
""",
    0xE0B3:
"""
......@.
.....@..
....@...
...@....
..@.....
...@....
....@...
.....@..
......@.
........
""",
}
