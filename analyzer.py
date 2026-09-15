# Bharath's First Bioinformatics Script: DNA Sequence Analyzer

def calculate_gc_content(dna_sequence):
    # Ensure all letters are uppercase
    dna = dna_sequence.upper()
    
    # Count specific genetic bases
    g_count = dna.count('G')
    c_count = dna.count('C')
    total_length = len(dna)
    
    if total_length == 0:
        return 0
        
    # Calculate the percentage of G and C bases
    gc_percentage = ((g_count + c_count) / total_length) * 100
    return round(gc_percentage, 2)

# Test DNA sequence
test_dna = "ATGCGTACGTTAGC"

print("--- Bioinformatics Sequence Analyzer ---")
print(f"Analyzing DNA Sequence: {test_dna}")
print(f"Sequence Length: {len(test_dna)} bases")
print(f"GC-Content Stability: {calculate_gc_content(test_dna)}%")
