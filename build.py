import fontforge

from data import (
    glyphs,
    romanBitmaps,
    powerline_bitmaps, 
    DOT_COLUMNS, DOT_ROWS, ROW_OFFSET,
)

import os

# The FONTLOG.txt must be alongside the python script
FONTLOG = 'FONTLOG.txt'
# The OFL text (copyright) must be alongside the python script
COPYRIGHT = 'OFL.txt'


CHAR_WIDTH = 800.0
ASCENT = 1600.0
DESCENT = 400.0
CAP_HEIGHT = 1200.0
EM_SIZE = 1300.0

ROW_SIZE = (CAP_HEIGHT+DESCENT) / (DOT_ROWS-ROW_OFFSET)
COL_SIZE = (CHAR_WIDTH*0.75) / (DOT_COLUMNS)

DOT_RADIUS = (max(ROW_SIZE, COL_SIZE)/2.0)*2.01

def cap(x):
    return x[0].capitalize() + x[1:]

class Font(object):
    def __init__(self, basename, isBold=False, isItalic=False):
        self.em = EM_SIZE
        if isBold:
            self.weight = 'bold'
        else:
            self.weight = 'normal'

        if isItalic:
            self.style = 'italic'
            self.bitmaps = italicBitmaps
        else:
            self.style = 'normal'
            self.bitmaps = romanBitmaps

        self.glyphs = glyphs # That is, glyphs.glyphs

        s = [basename]

        if self.weight == 'bold':
            s.append(self.weight)

        if self.style == 'italic':
            s.append('italic')

        s = [cap(x) for x in s]

        self.human_name = ' '.join(s)
        self.fontname = ''.join(self.human_name.split())
        self.familyname = ''.join(basename.split())
        print("basename: {0}".format(basename))
        print("fontname: {0}".format(self.fontname))
        print("familyname: {0}".format(self.familyname))
        print("human name: {0}".format(self.human_name))
        print("")
        self.sfd_name = '{0}.sfd'.format(self.fontname)
        self.otf_name = '{0}.otf'.format(self.fontname)
        self.ttf_name = '{0}.ttf'.format(self.fontname)

        self.font = fontforge.font()
        self.font.ascent = ASCENT
        self.font.descent = DESCENT
        self.font.fontname = self.fontname
        self.font.familyname = self.familyname
        self.font.fullname = self.human_name
        self.font.fontlog = open(FONTLOG, 'r').read()
        self.font.copyright = open(COPYRIGHT, 'r').read()
        if self.weight == 'bold':
            self.font.weight = cap(self.weight)
#        if self.style == 'italic':
#            self.font.isItalic = True
        g = self.font.createChar(0x0020, 'space')
#        g.width = CHAR_WIDTH
        g.width = COL_SIZE*(DOT_COLUMNS+1)

    def makeEPSGlyph(self, glyph):
        output = []
        preamble = """%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: {0:f} {1:f} {2:f} {3:f}
%%EndComments"""
        
        # dotline = "newpath {0:f} {1:f} {2:f} 0 360 arc closepath fill"
        dotline = """newpath
        {0:f} {1:f} moveto
        0 {2:f} rlineto
        {2:f} 0 rlineto
        0 {2:f} -1.0 mul rlineto
        closepath fill
        """
        trailer = """showpage
%%EOF"""
        
        output.append(preamble.format(0,DESCENT*-1, CHAR_WIDTH, CAP_HEIGHT))
        g = glyph.replace('#','*').replace('@','*')
        bitmap = g.split('\n')
        for x, row in enumerate(bitmap):
#            print('row {}: "{}"'.format(x,row[2:]))
            v = CAP_HEIGHT - (ROW_SIZE*(x-ROW_OFFSET))+(DOT_RADIUS/2.0)
            for y, col in enumerate(row[2:]):
                if col == '*':
                    h = (COL_SIZE * y)
                    output.append(dotline.format(h,v,DOT_RADIUS))
                    print(dotline.format(h,v,DOT_RADIUS))
                    if self.weight == 'bold':
                        output.append(dotline.format(h + (DOT_RADIUS/2),v, DOT_RADIUS))

        output.append(trailer)
        return('\n'.join(output))

    def addGlyph(self, glyphName, glyphBitmap):
#        print("\n"+glyphName)
        eps = self.makeEPSGlyph(glyphBitmap)
        epsfile = '{0}.eps'.format(glyphName)
        open(epsfile, 'w').write(eps)
#        self.font.selection.select(glyphName)
        g = self.font.createChar(self.glyphs[glyphName]['unicode'], str(glyphName))
        g.importOutlines(epsfile)
        g.width = CHAR_WIDTH+(COL_SIZE*0.5)
        g.removeOverlap()
        g.correctDirection()
        g.simplify()
        g.round()
        os.unlink(epsfile)

    def generate(self):
        for x in powerline_bitmaps:
            glyphs[x] = {'unicode':x}
            self.bitmaps[x] = powerline_bitmaps[x]

        for x in glyphs:
            # Support using '#' and '@' in addition to '*'
            g = self.bitmaps[x].replace('#','*').replace('@','*')
            if '*' in g:
                self.addGlyph(x, g)
        self.font.generate(self.otf_name)
        self.font.generate(self.ttf_name)
        self.font.save(self.sfd_name)

if __name__ == '__main__':
    FONTNAME = 'ADM5'

    fn = Font(FONTNAME)
    fn.generate()
    print DOT_RADIUS, COL_SIZE

    # fb = Font(FONTNAME, isBold=True)
    # fb.generate()

    # fin = Font(FONTNAME, isItalic=True)
    # fin.generate()

    # fib = Font(FONTNAME, isBold=True, isItalic=True)
    # fib.generate()
