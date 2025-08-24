import csv
from collections import Counter

# Ask for researcher name once at the start
researcher_Name = input("Enter your name: ").strip()
print("Hello " + researcher_Name)


# --- FUNCTIONS ---
def get_dna_sequence():
    """Prompt user for a DNA sequence and validate input."""
    dna_sequence = input("Enter a DNA sequence or type quit to exit: \n").upper().strip()
    
    if dna_sequence.lower() == "quit":
        print("Thank you for your time, " + researcher_Name + ".")
        return None
    
    if dna_sequence == "":
        print("❌ No DNA sequence entered. Try again.")
        return False   # allow retry
    
    elif not all(base in "ACGT" for base in dna_sequence):
        print("❌ Invalid DNA sequence. Please use only A, C, G, and T.")
        return False   # allow retry
    
    else:
        print("✅ DNA sequence entered successfully.\n")
        return dna_sequence


def count_nucleotides(dna_sequence):
    """Count how many A, C, G, and T bases are in the sequence."""
    counts = Counter(dna_sequence)
    return {base: counts.get(base, 0) for base in "ACGT"}


def complementary_strand(dna_sequence):
    """Return complementary DNA strand."""
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement.get(base, base) for base in dna_sequence)


def find_codon_patterns():
    """Read codon → amino acid mapping from CSV file."""
    codon_table = {}
    try:
        with open("standard_genetic_code.csv", "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                codon = row[0].strip().upper()
                amino_acid = row[1].strip()
                codon_table[codon] = amino_acid
    except FileNotFoundError:
        print("❌ Error: standard_genetic_code.csv not found.")
    return codon_table


def translate_dna(dna_sequence, start_index=0):
    """Translate DNA sequence into amino acids using codon table."""
    codon_table = find_codon_patterns()
    if not codon_table:
        return []  # avoid crash if file missing

    amino_acids = []
    for i in range(start_index, len(dna_sequence), 3):
        codon = dna_sequence[i:i + 3]

        if len(codon) < 3:
            print(f"⚠️ Warning: Incomplete codon skipped → {codon}")
            continue
        
        amino_acid = codon_table.get(codon)
        if amino_acid:
            amino_acids.append(amino_acid)
        else:
            print(f"⚠️ Warning: Unknown codon skipped → {codon}")
    
    return amino_acids
# Transcribe DNA sequence into RNA.
def transcribe_dna_to_rna(dna_sequence):
    return dna_sequence.replace("T", "U")

# Calculate the GC content of a DNA sequence.
def calculate_gc_content(dna_sequence):
    if not dna_sequence:
        return 0
    g_count = dna_sequence.count("G")
    c_count = dna_sequence.count("C")
    return (g_count + c_count) / len(dna_sequence) * 100

# --- MAIN LOOP ---
while True:
    dna = get_dna_sequence()
    if dna is None:  # user chose to quit
        break  
    if dna is False:  # invalid input → retry
        continue  
    
    counts = count_nucleotides(dna)
    print("Nucleotide counts:\n", counts)

    comp_strand = complementary_strand(dna)
    print("Complementary strand:\n", comp_strand)

    amino_acids = translate_dna(dna)
    if amino_acids:
        print("Translated amino acids:\n", "-".join(amino_acids))
    else:
        print("No valid translation produced.")

    rna = transcribe_dna_to_rna(dna)
    print("Transcribed RNA sequence:\n", rna)
    
    gc = calculate_gc_content(dna)
    print(f"GC Content: {gc:.2f}%\n")
