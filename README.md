# ADM5 typeface

This typeface is made to resemble the characters produced by the
[ADM5 text terminal](http://terminals.classiccmp.org/wiki/index.php/Lear_Siegler_ADM-5) produced by Lear Siegler in the 1980s.

## Building the font

The font glyphs are defined (fairly obviously) in the [data.py](data.py)
file, along with various parameters governing their structure.  The
font can be built by running the [build.py](build.py) file after
installing the [fontforge python extension](http://fontforge.github.io/en-US/documentation/scripting/python/),
which can be a bit of a challenge, especially on Mac machines.  I
would suggest using an Ubuntu machine (perhaps a temporary cloud-based
VPS if necessary) and installing the
[python-fontforge](http://packages.ubuntu.com/trusty/python/python-fontforge) package using apt-get, which will install it for the
system python interpreter.

The initial version committed to the repo has some anomalies in its
design, especially concerning the em-square, which is nonstandard. I
intend to refactor the build code to produce separate SFD files for
OTF and TTF versions, since they require different em squares.  The
resulting files will be then built from the SFD files.

The typeface is licensed under the SIL Open Font License, which is
available in this repository in the file [OFL.txt](OFL.txt).

More information is also available in the [FONTLOG](FONTLOG.txt) file.

