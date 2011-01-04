
from msp430 import memory
from cStringIO import StringIO

def get_patch():
    return memory.load('PATCH', StringIO(PATCH), format='titext')

def get_F1x_BSL():
    return memory.load('F1X_BSL', StringIO(F1X_BSL), format='titext')

def get_F4x_BSL():
    return memory.load('F4X_BSL', StringIO(F4X_BSL), format='titext')

# copy of the patch file provided by TI
# this part is (C) by Texas Instruments
#~ @0220
PATCH = """\
31 40 1A 02 09 43 B0 12 2A 0E B0 12 BA 0D 55 42 \
0B 02 75 90 12 00 1F 24 B0 12 BA 02 55 42 0B 02 \
75 90 16 00 16 24 75 90 14 00 11 24 B0 12 84 0E \
06 3C B0 12 94 0E 03 3C 21 53 B0 12 8C 0E B2 40 \
10 A5 2C 01 B2 40 00 A5 28 01 30 40 42 0C 30 40 \
76 0D 30 40 AC 0C 16 42 0E 02 17 42 10 02 E2 B2 \
08 02 14 24 B0 12 10 0F 36 90 00 10 06 28 B2 40 \
00 A5 2C 01 B2 40 40 A5 28 01 D6 42 06 02 00 00 \
16 53 17 83 EF 23 B0 12 BA 02 D3 3F B0 12 10 0F \
17 83 FC 23 B0 12 BA 02 D0 3F 18 42 12 02 B0 12 \
10 0F D2 42 06 02 12 02 B0 12 10 0F D2 42 06 02 \
13 02 38 E3 18 92 12 02 BF 23 E2 B3 08 02 BC 23 \
30 41 \
""".replace(' ', '').decode('hex')


# These BSL's are (C) by TI. They come with the application note slaa089a
#~ @0220
F1X_BSL = """\
24 02 2E 02 31 40 20 02 2B D2 C0 43 EA FF 32 C2 \
F2 C0 32 00 00 00 B2 40 80 5A 20 01 F2 40 85 00 \
57 00 F2 40 80 00 56 00 E2 D3 21 00 E2 D3 22 00 \
E2 C3 26 00 E2 C2 2A 00 E2 C2 2E 00 B2 40 10 A5 \
2C 01 B2 40 00 A5 28 01 3B C0 3A 00 B0 12 D6 04 \
82 43 12 02 09 43 36 40 0A 02 37 42 B0 12 AC 05 \
C6 4C 00 00 16 53 17 83 F9 23 D2 92 0C 02 0D 02 \
28 20 55 42 0B 02 75 90 12 00 80 24 75 90 10 00 \
6D 24 B0 12 9C 04 55 42 0B 02 75 90 18 00 31 24 \
75 90 1E 00 B8 24 75 90 20 00 17 24 2B B2 11 24 \
75 90 16 00 22 24 75 90 14 00 B3 24 75 90 1A 00 \
18 24 75 90 1C 00 45 24 04 3C B0 12 36 05 BE 3F \
21 53 B0 12 3C 05 BA 3F 03 43 B0 12 36 05 D2 42 \
0E 02 56 00 D2 42 0F 02 57 00 D2 42 10 02 16 02 \
AD 3F B0 12 36 05 10 42 0E 02 16 42 0E 02 15 43 \
07 3C 36 40 FE FF B2 40 06 A5 10 02 35 40 0C 00 \
B2 40 00 A5 2C 01 92 42 10 02 28 01 B6 43 00 00 \
92 B3 2C 01 FD 23 15 83 F3 23 36 90 FE FF CD 27 \
37 40 80 00 36 F0 80 FF 36 90 00 11 0E 28 07 57 \
36 F0 00 FF 36 90 00 12 08 28 07 57 36 F0 00 FE \
04 3C 16 42 0E 02 17 42 10 02 35 43 75 96 03 20 \
17 83 FC 23 B2 3F 82 46 00 02 B3 3F 36 40 E0 FF \
37 40 20 00 B0 12 AC 05 7C 96 01 24 2B D3 17 83 \
F9 23 2B C2 B0 12 9C 04 2B D2 9F 3F 16 42 0E 02 \
17 42 10 02 2B B2 38 24 3B D0 10 00 B0 12 AC 05 \
36 90 00 10 06 2C 36 90 00 01 09 2C C6 4C 00 00 \
25 3C B2 40 00 A5 2C 01 B2 40 40 A5 28 01 16 B3 \
03 20 C2 4C 14 02 1A 3C C2 4C 15 02 86 9A FD FF \
08 24 2B D3 3B B0 20 00 04 20 3B D0 20 00 82 46 \
00 02 36 90 01 02 04 28 3B D2 3B B0 10 00 02 24 \
3B C0 32 00 1A 42 14 02 86 4A FF FF 16 53 17 83 \
CD 23 B0 12 9C 04 61 3F B0 12 AC 05 17 83 FC 23 \
B0 12 9C 04 5E 3F B2 40 F0 0F 0E 02 B2 40 10 00 \
10 02 B2 40 80 00 0A 02 D2 42 10 02 0C 02 D2 42 \
10 02 0D 02 82 43 12 02 09 43 36 40 0A 02 27 42 \
7C 46 B0 12 40 05 17 83 FB 23 16 42 0E 02 17 42 \
10 02 36 90 00 01 0A 28 B2 46 14 02 5C 42 14 02 \
B0 12 40 05 17 83 5C 42 15 02 01 3C 7C 46 B0 12 \
40 05 17 83 EE 23 B2 E3 12 02 5C 42 12 02 B0 12 \
40 05 5C 42 13 02 B0 12 40 05 E0 3E 18 42 12 02 \
B0 12 AC 05 C2 4C 12 02 B0 12 AC 05 C2 4C 13 02 \
38 E3 3B B2 0A 24 86 9A FE FF 07 24 3B B0 20 00 \
04 20 16 53 82 46 00 02 2B D3 18 92 12 02 08 23 \
2B B3 06 23 30 41 E2 B2 28 00 FD 27 E2 B2 28 00 \
FD 23 B2 40 24 02 60 01 E2 B2 28 00 FD 27 15 42 \
70 01 05 11 05 11 05 11 82 45 02 02 05 11 82 45 \
04 02 B2 80 1E 00 04 02 57 42 16 02 37 80 03 00 \
05 11 05 11 17 53 FD 23 35 50 40 A5 82 45 2A 01 \
35 42 B2 40 24 02 60 01 92 92 70 01 02 02 FC 2F \
15 83 F7 23 09 43 7C 40 90 00 02 3C 7C 40 A0 00 \
C2 43 07 02 C9 EC 12 02 19 E3 1B C3 55 42 07 02 \
55 45 56 05 00 55 0C 2E 2E 2E 2E 2E 2E 2E 2E 1A \
34 34 92 42 70 01 72 01 B2 50 0C 00 72 01 07 3C \
1B B3 0B 20 82 43 62 01 92 B3 62 01 FD 27 E2 C3 \
21 00 0A 3C 4C 11 F6 2B 1B E3 82 43 62 01 92 B3 \
62 01 FD 27 E2 D3 21 00 92 52 02 02 72 01 D2 53 \
07 02 F0 90 0C 00 61 FC D1 23 30 41 C2 43 09 02 \
1B C3 55 42 09 02 55 45 BC 05 00 55 0C 56 56 56 \
56 56 56 56 56 36 76 00 E2 B2 28 00 FD 23 92 42 \
70 01 72 01 92 52 04 02 72 01 82 43 62 01 92 B3 \
62 01 FD 27 E2 B2 28 00 1E 28 2B D3 1C 3C 4C 10 \
1A 3C 82 43 62 01 92 B3 62 01 FD 27 E2 B2 28 00 \
01 28 1B E3 1B B3 01 24 2B D3 C9 EC 12 02 19 E3 \
0A 3C 82 43 62 01 92 B3 62 01 FD 27 E2 B2 28 00 \
E6 2B 4C 10 1B E3 92 52 02 02 72 01 D2 53 09 02 \
C0 3F 82 43 62 01 92 B3 62 01 FD 27 E2 B2 28 00 \
01 2C 2B D3 30 41 \
""".replace(' ', '').decode('hex')

#~ @0220
F4X_BSL = """\
24 02 2E 02 31 40 20 02 2B D2 C0 43 EA FF 32 C2 \
F2 C0 32 00 00 00 B2 40 80 5A 20 01 32 D0 40 00 \
C2 43 50 00 F2 40 98 00 51 00 F2 C0 80 00 52 00 \
D2 D3 21 00 D2 D3 22 00 D2 C3 26 00 E2 C3 22 00 \
E2 C3 26 00 B2 40 10 A5 2C 01 B2 40 00 A5 28 01 \
3B C0 3A 00 B0 12 DE 04 82 43 12 02 09 43 36 40 \
0A 02 37 42 B0 12 B4 05 C6 4C 00 00 16 53 17 83 \
F9 23 D2 92 0C 02 0D 02 28 20 55 42 0B 02 75 90 \
12 00 80 24 75 90 10 00 6D 24 B0 12 A4 04 55 42 \
0B 02 75 90 18 00 31 24 75 90 1E 00 B8 24 75 90 \
20 00 17 24 2B B2 11 24 75 90 16 00 22 24 75 90 \
14 00 B3 24 75 90 1A 00 18 24 75 90 1C 00 45 24 \
04 3C B0 12 3E 05 BE 3F 21 53 B0 12 44 05 BA 3F \
03 43 B0 12 3E 05 D2 42 0E 02 50 00 D2 42 0F 02 \
51 00 D2 42 10 02 16 02 AD 3F B0 12 3E 05 10 42 \
0E 02 16 42 0E 02 15 43 07 3C 36 40 FE FF B2 40 \
06 A5 10 02 35 40 0C 00 B2 40 00 A5 2C 01 92 42 \
10 02 28 01 B6 43 00 00 92 B3 2C 01 FD 23 15 83 \
F3 23 36 90 FE FF CD 27 37 40 80 00 36 F0 80 FF \
36 90 00 11 0E 28 07 57 36 F0 00 FF 36 90 00 12 \
08 28 07 57 36 F0 00 FE 04 3C 16 42 0E 02 17 42 \
10 02 35 43 75 96 03 20 17 83 FC 23 B2 3F 82 46 \
00 02 B3 3F 36 40 E0 FF 37 40 20 00 B0 12 B4 05 \
7C 96 01 24 2B D3 17 83 F9 23 2B C2 B0 12 A4 04 \
2B D2 9F 3F 16 42 0E 02 17 42 10 02 2B B2 38 24 \
3B D0 10 00 B0 12 B4 05 36 90 00 10 06 2C 36 90 \
00 01 09 2C C6 4C 00 00 25 3C B2 40 00 A5 2C 01 \
B2 40 40 A5 28 01 16 B3 03 20 C2 4C 14 02 1A 3C \
C2 4C 15 02 86 9A FD FF 08 24 2B D3 3B B0 20 00 \
04 20 3B D0 20 00 82 46 00 02 36 90 01 02 04 28 \
3B D2 3B B0 10 00 02 24 3B C0 32 00 1A 42 14 02 \
86 4A FF FF 16 53 17 83 CD 23 B0 12 A4 04 61 3F \
B0 12 B4 05 17 83 FC 23 B0 12 A4 04 5E 3F B2 40 \
F0 0F 0E 02 B2 40 10 00 10 02 B2 40 80 00 0A 02 \
D2 42 10 02 0C 02 D2 42 10 02 0D 02 82 43 12 02 \
09 43 36 40 0A 02 27 42 7C 46 B0 12 48 05 17 83 \
FB 23 16 42 0E 02 17 42 10 02 36 90 00 01 0A 28 \
B2 46 14 02 5C 42 14 02 B0 12 48 05 17 83 5C 42 \
15 02 01 3C 7C 46 B0 12 48 05 17 83 EE 23 B2 E3 \
12 02 5C 42 12 02 B0 12 48 05 5C 42 13 02 B0 12 \
48 05 E0 3E 18 42 12 02 B0 12 B4 05 C2 4C 12 02 \
B0 12 B4 05 C2 4C 13 02 38 E3 3B B2 0A 24 86 9A \
FE FF 07 24 3B B0 20 00 04 20 16 53 82 46 00 02 \
2B D3 18 92 12 02 08 23 2B B3 06 23 30 41 E2 B3 \
20 00 FD 27 E2 B3 20 00 FD 23 B2 40 24 02 60 01 \
E2 B3 20 00 FD 27 15 42 70 01 05 11 05 11 05 11 \
82 45 02 02 05 11 82 45 04 02 B2 80 1E 00 04 02 \
57 42 16 02 37 80 03 00 05 11 05 11 17 53 FD 23 \
35 50 40 A5 82 45 2A 01 35 42 B2 40 24 02 60 01 \
92 92 70 01 02 02 FC 2F 15 83 F7 23 09 43 7C 40 \
90 00 02 3C 7C 40 A0 00 C2 43 07 02 C9 EC 12 02 \
19 E3 1B C3 55 42 07 02 55 45 5E 05 00 55 0C 2E \
2E 2E 2E 2E 2E 2E 2E 1A 34 34 92 42 70 01 72 01 \
B2 50 0C 00 72 01 07 3C 1B B3 0B 20 82 43 62 01 \
92 B3 62 01 FD 27 D2 C3 21 00 0A 3C 4C 11 F6 2B \
1B E3 82 43 62 01 92 B3 62 01 FD 27 D2 D3 21 00 \
92 52 02 02 72 01 D2 53 07 02 F0 90 0C 00 59 FC \
D1 23 30 41 C2 43 09 02 1B C3 55 42 09 02 55 45 \
C4 05 00 55 0C 56 56 56 56 56 56 56 56 36 76 00 \
E2 B3 20 00 FD 23 92 42 70 01 72 01 92 52 04 02 \
72 01 82 43 62 01 92 B3 62 01 FD 27 E2 B3 20 00 \
1E 28 2B D3 1C 3C 4C 10 1A 3C 82 43 62 01 92 B3 \
62 01 FD 27 E2 B3 20 00 01 28 1B E3 1B B3 01 24 \
2B D3 C9 EC 12 02 19 E3 0A 3C 82 43 62 01 92 B3 \
62 01 FD 27 E2 B3 20 00 E6 2B 4C 10 1B E3 92 52 \
02 02 72 01 D2 53 09 02 C0 3F 82 43 62 01 92 B3 \
62 01 FD 27 E2 B3 20 00 01 2C 2B D3 30 41 \
""".replace(' ', '').decode('hex')
