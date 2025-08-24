import streamlit as st
import csv
from collections import Counter

# --- FUNCTIONS ---
def count_nucleotides(dna_sequence):
    counts = Counter(dna_sequence)
    return {base: counts.get(base, 0) for base in "ACGT"}


def complementary_strand(dna_sequence):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement.get(base, base) for base in dna_sequence)


def find_codon_patterns():
    codon_table = {}
    try:
        with open("standard_genetic_code.csv", "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header
            for row in csv_reader:
                codon = row[0].strip().upper()
                amino_acid = row[1].strip()
                codon_table[codon] = amino_acid
    except FileNotFoundError:
        st.error("❌ Error: standard_genetic_code.csv not found.")
    return codon_table


def translate_dna(dna_sequence, start_index=0):
    codon_table = find_codon_patterns()
    if not codon_table:
        return []

    amino_acids = []
    for i in range(start_index, len(dna_sequence), 3):
        codon = dna_sequence[i:i + 3]
        if len(codon) < 3:
            st.warning(f"⚠️ Incomplete codon skipped → {codon}")
            continue
        amino_acid = codon_table.get(codon)
        if amino_acid:
            amino_acids.append(amino_acid)
        else:
            st.warning(f"⚠️ Unknown codon skipped → {codon}")
    return amino_acids


def transcribe_dna_to_rna(dna_sequence):
    return dna_sequence.replace("T", "U")


def calculate_gc_content(dna_sequence):
    if not dna_sequence:
        return 0
    g_count = dna_sequence.count("G")
    c_count = dna_sequence.count("C")
    return (g_count + c_count) / len(dna_sequence) * 100


# --- STREAMLIT APP ---
st.title("🧬 DNA Sequence Analyzer Roadmap")

# Step 1: Ask researcher name
researcher_Name = st.text_input("Enter your name:")

if researcher_Name:
    st.success(f"Hello {researcher_Name} 👋")

    # Step 2: DNA entry inside a form (auto-clears on submit)
    with st.form("dna_form", clear_on_submit=True):
        dna_raw = st.text_area("Enter a DNA sequence (A, C, G, T only):")
        submitted = st.form_submit_button("Analyze")

    if submitted:
        dna = dna_raw.upper().strip()
        if not all(base in "ACGT" for base in dna):
            st.error("❌ Invalid DNA sequence. Please use only A, C, G, and T.")
        else:
            st.success("✅ DNA sequence entered successfully.")

            # Step 3: Show analyses
            st.subheader("Step 1: Nucleotide Counts")
            counts = count_nucleotides(dna)
            st.write(counts)

            st.subheader("Step 2: Complementary Strand")
            comp_strand = complementary_strand(dna)
            st.code(comp_strand)

            st.subheader("Step 3: Translation")
            amino_acids = translate_dna(dna)
            if amino_acids:
                st.write("-".join(amino_acids))
            else:
                st.warning("No valid translation produced.")

            st.subheader("Step 4: RNA Transcription")
            rna = transcribe_dna_to_rna(dna)
            st.code(rna)

            st.subheader("Step 5: GC Content")
            gc = calculate_gc_content(dna)
            st.write(f"GC Content: {gc:.2f}%")

            # --- Bottom buttons ---
            st.markdown("---")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔄 Redo"):
                    st.session_state.clear()
                    st.rerun()
            with col2:
                if st.button("❌ Quit"):
                    st.session_state.clear()
                    st.stop()
