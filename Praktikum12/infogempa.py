from gempa import *


gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)


# hasil
dampak = gempa1.dampak()
dampak = gempa2.dampak()
dampak = gempa3.dampak()
dampak = gempa4.dampak()
dampak = gempa5.dampak()
