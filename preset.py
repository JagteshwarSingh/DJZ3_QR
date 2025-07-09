cols = [
    "A", "B", "C", "D", "E", "G"
]
rows = [
    "1", "2", "3", "4"
]

ov = [
    "A1", "A2", "A3", "A4",
    "B1", "B2", "B3", "B4",
    "C1", "C2", "C3", "C4",
    "D1", "D2", "D3", "D4",
    "E1", "E2", "E3", "E4",
    "G1", "G2", "G3", "G4"
]


for col in cols:
    for row in rows:
        print(f"\"{row}{col}\", ", end="")