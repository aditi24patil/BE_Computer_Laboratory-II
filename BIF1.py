# Step 1: Provide the DNA sequence
dna_seq = "AGTCAGTAGACTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA"

# Step 2: Function to find all positions of a given motif (pattern)
def find_motifs(sequence, motif):
    positions = []  # list to store where motif is found
    for i in range(len(sequence) - len(motif) + 1):  # loop through sequence
        if sequence[i:i+len(motif)] == motif:        # check if substring matches motif
            positions.append(i + 1)                  # add 1 to make position start from 1
    return positions

# Step 3: Function to calculate GC content (percentage of G and C bases)
def gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")  # count G and C bases
    return gc_count / len(sequence)                       # divide by total length

# Step 4: Function to identify coding regions (start → stop codon)
def identify_coding_regions(sequence):
    start = "AGC"                    # start codon (example)
    stops = ["TAA", "TAG", "TGA"]    # possible stop codons
    regions = []                     # list to store (start, stop) positions

    i = 0
    while i < len(sequence):
        if sequence[i:i+3] == start:     # if start codon found
            start_pos = i + 1
            i += 3
            while i < len(sequence):
                if sequence[i:i+3] in stops:  # if stop codon found
                    stop_pos = i + 3
                    regions.append((start_pos, stop_pos))
                    break
                i += 3
        else:
            i += 1
    return regions

# Step 5: Define motifs to search
motif1 = "AGCTAGCTA"
motif2 = "CTAGCTAGC"

# Step 6: Perform analysis
motif1_pos = find_motifs(dna_seq, motif1)
motif2_pos = find_motifs(dna_seq, motif2)
gc = gc_content(dna_seq)
regions = identify_coding_regions(dna_seq)

# Step 7: Print results neatly
print("Motif 1 positions:", motif1_pos)
print("Motif 2 positions:", motif2_pos)
print("GC Content:", round(gc, 3))
print("Coding Regions (start, stop):", regions)
