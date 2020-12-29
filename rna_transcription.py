
def to_rna(dna_strand):
    dna_list = list(dna_strand)
    dict_trans = {"G": "C",
                  "C": "G",
                  "T": "A",
                  "A": "U"}
    rna_list = [dict_trans[i] for i in dna_list]
    rna_strand = "".join(rna_list)
    return rna_strand

# def to_rna(dna_strand):
#     return dna_strand.translate(str.maketrans("GCTA", "CGAU"))