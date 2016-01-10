import fontforge

from data import (
    glyphs,
    romanBitmaps,
    powerline_bitmaps, 
    DOT_COLUMNS, DOT_ROWS, ROW_OFFSET, ASPECT_RATIO,
)

import os

# The FONTLOG.txt must be alongside the python script
FONTLOG_FILENAME = 'FONTLOG.txt'
# The OFL text (copyright) must be alongside the python script
COPYRIGHT_FILENAME = 'OFL.txt'

EM_SIZE_TTF = 2048
EM_SIZE_OTF = 1000

class FontParams:
    def __init__(self, em_size, basename):
        self.EM_SIZE = em_size
        SCALE_FACTOR = self.EM_SIZE/2048.0

        if em_size == EM_SIZE_OTF:
            self.format = 'otf'
        elif em_size == EM_SIZE_TTF:
            self.format = 'ttf'

        self.human_name = basename
        self.fontname = ''.join(self.human_name.split())
        self.familyname = ''.join(basename.split())
        
        self.ASCENT = SCALE_FACTOR * 1700.0
        self.DESCENT = SCALE_FACTOR * 324.0
        self.CAP_HEIGHT = SCALE_FACTOR * 1790.0
        self.CHAR_WIDTH = (self.EM_SIZE / ASPECT_RATIO) * 0.9
        self.ROW_SIZE = self.EM_SIZE / DOT_ROWS
        self.COL_SIZE = self.CHAR_WIDTH / (DOT_COLUMNS - 1)
        self.DOT_SIZE = max(self.ROW_SIZE, self.COL_SIZE) / 2.0
        self.DOT_H = self.DOT_SIZE * 2.1
        self.DOT_V = self.DOT_SIZE * 2.1
        
        self.font = fontforge.font()
        
        self.font.ascent = self.ASCENT
        self.font.descent = self.DESCENT
        self.font.fontname = self.fontname
        self.font.familyname = self.familyname
        self.font.fullname = self.human_name
        self.font.fontlog = open(FONTLOG_FILENAME, 'r').read()
        self.font.copyright = open(COPYRIGHT_FILENAME, 'r').read()
        
        g = self.font.createChar(0x0020, 'space')
        g.width = self.COL_SIZE * DOT_COLUMNS
        
        self.binary_filename = '{0}.{1}'.format(self.fontname, self.format)
        self.archive_filename = '{0}-{1}.sfd'.format(self.fontname, self.format)




class Font:
    def __init__(self, basename, isBold=False, isItalic=False):
        self.weight = 'normal'
        self.style = 'normal'
        self.bitmaps = romanBitmaps

        print self.bitmaps['A']

        self.glyphs = glyphs

        self.ttf_params = FontParams(EM_SIZE_TTF, basename) # Standard emsquare for T
        self.otf_params = FontParams(EM_SIZE_OTF, basename)


    def makeEPSGlyph(self, glyphName, glyph, params):
        output = []
        preamble = """%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: {0:f} {1:f} {2:f} {3:f}
%%EndComments"""
        
        # dotline = "newpath {0:f} {1:f} {2:f} 0 360 arc closepath fill"
        dotline1 = """newpath
        {0:f} {1:f} moveto
        0 {2:f} rlineto
        {2:f} 0 rlineto
        0 {2:f} -1.0 mul rlineto
        closepath fill
        """
        dotline = """newpath
        {h:f} {v:f} moveto
        0 {dv:f} rlineto
        {dh:f} 0 rlineto
        0 {dv:f} -1.0 mul rlineto
        closepath fill
        """
        trailer = """showpage
%%EOF"""
        
        output.append(preamble.format(
            0,
            params.DESCENT*-1,
            params.CHAR_WIDTH,
            params.EM_SIZE-params.DESCENT,
        ))
        g = glyph.replace('#','*').replace('@','*')
        bitmap = g.split('\n')
        for x, row in enumerate(bitmap):
            v = params.CAP_HEIGHT - (params.ROW_SIZE*(x+1))+(params.DOT_SIZE/2.0)
            for y, col in enumerate(row):
                if col == '*':
                    h = (params.COL_SIZE * (y-1.15))
                    output.append(dotline.format(
                        v=v,
                        h=h,
                        dv=params.DOT_V,
                        dh=params.DOT_H,
                    ))

        output.append(trailer)
        output = '\n'.join(output)
        return(output)

    def addGlyph(self, glyphName, glyphBitmap, params):
        eps = self.makeEPSGlyph(glyphName, glyphBitmap, params)

        epsfile = '{0}.eps'.format(glyphName)
        open(epsfile, 'w').write(eps)

        g = params.font.createChar(self.glyphs[glyphName]['unicode'], str(glyphName))

        g.importOutlines(epsfile)
        os.unlink(epsfile)

        g.width = params.CHAR_WIDTH
        g.removeOverlap()
        g.correctDirection()
        g.simplify()
        g.round()
        if params.format == 'otf':
            g.autoHint()
        # if params.format == 'ttf':
        #     g.autoInstr()

    def generate(self):
        for x in powerline_bitmaps:
            glyphs[x] = {'unicode':x}
            self.bitmaps[x] = powerline_bitmaps[x]

        for x in glyphs:
            # Support using '#' and '@' in addition to '*'
            g = self.bitmaps[x]
            if '@' in g:
                self.addGlyph(x, g, self.ttf_params)
                self.addGlyph(x, g, self.otf_params)
            else:
                pass
#                print '{0} is blank'.format(x)

        self.otf_params.font.generate(self.otf_params.binary_filename)
        self.otf_params.font.save(self.otf_params.archive_filename)

        self.ttf_params.font.generate(self.ttf_params.binary_filename)
        self.ttf_params.font.save(self.ttf_params.archive_filename)

if __name__ == '__main__':
    FONTNAME = 'ADM5'

    fn = Font(FONTNAME)
    fn.generate()
