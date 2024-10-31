# Bioinformatics_Regex_Dictionary_Assignment.py

import re

# Task 1: Regular Expressions I
text = """Several rapidly developing RNA interference (RNAi) methodologies hold the promise to selectively 
inhibit gene expression in mammals. RNAi is an innate cellular process activated when a double-
stranded RNA (dsRNA) molecule of greater than 19 duplex nucleotides enters the cell, causing the 
degradation of not only the invading dsRNA molecule, but also single-stranded (ssRNAs) RNAs of 
identical sequences, including endogenous mRNAs."""

# Regular expression pattern to find specific RNA-related terms
pattern = r'\b(RNAi|dsRNA|ssRNAs|mRNAs)\b'

# Find all matches and their ending positions
matches = [(match.group(), match.end()) for match in re.finditer(pattern, text)]

# Print the results
for match, end_pos in matches:
    print(f"{match} ends at position {end_pos}")

# Task 2: Regular Expressions II
def find_motif_in_sequence(sequence, motif):
    """Check if the motif is present in the sequence."""
    if re.search(motif, sequence):
        print(f"Motif '{motif}' found in the sequence.")
    else:
        print(f"Motif '{motif}' not found in the sequence.")

# Prompt the user for a file in FASTA format
fasta_file = input("Enter the path to your FASTA file: ")
with open(fasta_file, 'r') as file:
    sequence = ''.join([line.strip() for line in file if not line.startswith('>')])

# Example motif input
motif = input("Enter the motif to search for: ")
find_motif_in_sequence(sequence, motif)

# Task 3: Dictionaries
def create_gene_dict(filename):
    gene_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            accession, seq = line.strip().split(',')
            gene_dict[accession.strip()] = seq.strip()
    return gene_dict

# Prompt for filename and display dictionary
filename = input("Enter the path to your gene accession file: ")
gene_dict = create_gene_dict(filename)
print("Gene dictionary:")
for accession, seq in gene_dict.items():
    print(f"{accession}: {seq}")

