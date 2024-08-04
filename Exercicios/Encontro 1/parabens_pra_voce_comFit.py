# description: 
from earsketch import *

setTempo(180)

do = PROGRAMUSICAL_NOTA_DO
re = PROGRAMUSICAL_NOTA_RE
fa = PROGRAMUSICAL_NOTA_FA
mi = PROGRAMUSICAL_NOTA_MI
sol = PROGRAMUSICAL_NOTA_SOL
la = PROGRAMUSICAL_NOTA_LA
si = PROGRAMUSICAL_NOTA_SI


# C C D C F E
fitMedia(do, 1, 1, 1.5)
fitMedia(do, 1, 1.5, 1.7)
fitMedia(re, 1, 1.7, 2.2)
fitMedia(do, 1, 2.2, 2.7)
fitMedia(fa, 1, 2.7, 3.2)
fitMedia(mi, 1, 3.2, 3.7)

# C C D C G F
fitMedia(do, 1, 4, 4.5)
fitMedia(do, 1, 4.5, 4.7)
fitMedia(re, 1, 4.7, 5.2)
fitMedia(do, 1, 5.2, 5.7)
fitMedia(sol, 1, 5.7, 6.2)
fitMedia(fa, 1, 6.2, 6.7)
fitMedia(fa, 1, 6.7, 7)

# A A C A F E D
fitMedia(la, 1, 7.3, 7.8)
fitMedia(la, 1, 7.8, 8)
fitMedia(do, 2, 8, 8.5)
setEffect(2, PITCHSHIFT, PITCHSHIFT_SHIFT, 12)
setEffect(2, VOLUME, GAIN, 3)
fitMedia(la, 1, 8.5, 8.8)
fitMedia(fa, 1, 8.8, 9)
fitMedia(mi, 1, 9, 9.3)
fitMedia(re, 1, 9.3, 10)

# B B A F G F F
fitMedia(si, 3, 11, 11.5)
fitMedia(si, 3, 11.5, 11.7)
setEffect(3, PITCHSHIFT, PITCHSHIFT_SHIFT, -1)
setEffect(3, VOLUME, GAIN, 3)
fitMedia(la, 1, 11.7, 12)
fitMedia(fa, 1, 12, 12.5)
fitMedia(sol, 1, 12.5, 13)
fitMedia(fa, 1, 13, 13.3)
fitMedia(fa, 1, 13.3, 14)


