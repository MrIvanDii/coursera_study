import re

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print('#' + line)
#From: stephen.marquard@uct.ac.za
#From: louis@media.berkeley.edu
#From: zqian@umich.edu
#From: rjlowe@iupui.edu
#From: zqian@umich.edu
#From: rjlowe@iupui.edu
#From: cwen@iupui.edu
#From: cwen@iupui.edu
#From: gsilver@umich.edu
#From: gsilver@umich.edu
#From: zqian@umich.edu
#From: gsilver@umich.edu
#From: wagnermr@iupui.edu
#From: zqian@umich.edu
#From: antranig@caret.cam.ac.uk
#From: gopal.ramasammycook@gmail.com
#From: david.horwitz@uct.ac.za
#From: david.horwitz@uct.ac.za
#From: david.horwitz@uct.ac.za
#From: david.horwitz@uct.ac.za
#From: stephen.marquard@uct.ac.za
#From: louis@media.berkeley.edu
#From: louis@media.berkeley.edu
#From: ray@media.berkeley.edu
#From: cwen@iupui.edu
#From: cwen@iupui.edu
#From: cwen@iupui.edu
