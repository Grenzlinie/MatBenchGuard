#!/usr/bin/env python3
import csv
import sys

def write_table1(out_path):
    rows = [
        # (species, coordination_mode, D_kcal_mol, Q_kcal_mol, D_plus_Q_kcal_mol)
        ("H", "atomic", 0, 52, 52),
        ("O", "atomic", 0, 80, 80),
        ("C", "atomic", 0, 133, 133),
        ("Cl", "atomic trial Q_Cl=50", 0, 50, 50),
        ("Cl", "atomic trial Q_Cl=55", 0, 55, 55),
        ("Cl", "atomic trial Q_Cl=60", 0, 60, 60),
        ("OH", "eta1(O) strong", 102, 55, 157),
        ("H2O", "eta1(O) weak", 220, 9, 229),
        ("CH2CH2", "eta2(C,C) homonuclear", 538, 9, 547),
        ("CH2CHCH3", "eta2(C=C, H) chelate", 822, 10, 832),
        ("pi-CH2CHCH2", "eta2(C,C) symmetric chelate", 736, 25, 761),
        ("sigma-CH2CHCH2", "eta1(C) medium", 722, 31, 753),
        ("sigma-CH2CHCH2", "eta2(C=C, C) chelate", 722, 33, 755),
        ("CH2CHCH2Cl", "eta2(C=C, Cl) chelate", 803, 13, 816),
        ("CH2CHCH2Cl", "eta2(C=C, Cl) chelate", 803, 14, 817),
        ("CH2CHCH2Cl", "eta2(C=C, Cl) chelate", 803, 15, 818),
        ("CH2CHCH2OH", "eta2(C=C, O) chelate", 918, 14, 932),
        ("CH2CHCH2O", "eta2(C=C, O) chelate", 816, 59, 875),
        ("CH2CHCHO", "eta2(C=C, O) chelate", 802, 14, 816),
        ("C6H10", "eta2(C=C, C=C) chelate", 1529, 19, 1548),
    ]
    with open(out_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["species", "coordination_mode", "D_kcal_mol", "Q_kcal_mol", "D_plus_Q_kcal_mol"])
        for species, coord, D, Q, D_plus_Q in rows:
            w.writerow([species, coord, D, Q, D_plus_Q])

def write_table34(out_path):
    rows = [
        # (table_id, reaction_equation, Q_Cl_value_if_applicable, DeltaE_f_kcal_mol, DeltaE_r_kcal_mol)
        ("Table3", "CH2CHCH3,s \u21cc CH2CHCH3,g",         "", 10, 0),
        ("Table3", "CH2CHCH3,s \u21cc pi-CH2CHCH2,s + H_s",           "", 18, 0),
        ("Table3", "CH2CHCH3,s + O_s \u21cc pi-CH2CHCH2,s + OH_s",      "", 2, 8),
        ("Table3", "CH2CHCH3,s + OH_s \u21cc pi-CH2CHCH2,s + H2O_s",    "", 3, 5),
        ("Table3", "pi-CH2CHCH2,s + O_s \u21cc CH2CHCH2O_s",           "", 0, 34),   # paper gives ~0 for forward; we use 0
        ("Table3", "CH2CHCH2O_s \u21cc CH2CHCHO_s + H_s",              "", 9, 2),
        ("Table3", "CH2CHCH2O_s + O_s \u21cc CH2CHCHO_s + OH_s",       "", 8, 26),
        ("Table3", "pi-CH2CHCH2,s + O_s \u21cc CH2CHCHO_s + H_s",      "", 0, 27),
        ("Table4", "CH2CHCH2OH_s \u21cc CH2CHCH2OH_g",                 "", 14, 0),
        ("Table4", "CH2CHCH2OH_s \u21cc CH2CHCH2O_s + H_s",            "", 16, 11),
        ("Table4", "CH2CHCH2OH_s \u21cc pi-CH2CHCH2,s + OH_s",         "", 16, 2),
        ("Table4", "CH2CHCH2OH_s + O_s \u21cc CH2CHCH2O_s + OH_s",     "", 4, 24),
        ("Table4", "CH2CHCH2OH_s + OH_s \u21cc CH2CHCH2O_s + H2O_s",   "", 0, 16),
        ("Table4", "CH2CHCH2OH_s + pi-CH2CHCH2,s \u21cc CH2CHCH2O_s + CH2CHCH3,s", "", 0, 14),
        ("Table4", "CH2CHCH2O_s \u21cc CH2CHCHO_s + H_s",              "", 9, 2),
        ("Table4", "CH2CHCH2O_s + O_s \u21cc CH2CHCHO_s + OH_s",       "", 8, 26),
        ("Table4", "CH2CHCH2O_s + OH_s \u21cc CH2CHCHO_s + H2O_s",     "", 7, 21),
        ("Table4", "CH2CHCH2O_s + pi-CH2CHCH2,s \u21cc CH2CHCHO_s + CH2CHCH3,s", "", 3, 15),
        ("Table4", "CH2CHCH2Cl_s \u21cc CH2CHCH2Cl_g",                 50, 13, 0),
        ("Table4", "CH2CHCH2Cl_s \u21cc CH2CHCH2Cl_g",                 55, 14, 0),
        ("Table4", "CH2CHCH2Cl_s \u21cc CH2CHCH2Cl_g",                 60, 15, 0),
        ("Table4", "CH2CHCH2Cl_s \u21cc pi-CH2CHCH2,s + Cl_s",        50, 11, 6),
        ("Table4", "CH2CHCH2Cl_s \u21cc pi-CH2CHCH2,s + Cl_s",        55, 9, 8),
        ("Table4", "CH2CHCH2Cl_s \u21cc pi-CH2CHCH2,s + Cl_s",        60, 8, 11),
        ("Table4", "H2O_s \u21cc OH_s + H_s",                          "", 24, 3),
        ("Table4", "H2O_s + O_s \u21cc 2 OH_s",                        "", 12, 16),
        ("Table4", "OH_s \u21cc O_s + H_s",                             "", 28, 3),
    ]
    with open(out_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["table_id", "reaction_equation", "Q_Cl_value_if_applicable",
                     "DeltaE_f_kcal_mol", "DeltaE_r_kcal_mol"])
        for table_id, reaction, q_cl, dfr, drv in rows:
            w.writerow([table_id, reaction, q_cl if q_cl != "" else "", dfr, drv])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    dataset = sys.argv[1]
    out_path = sys.argv[2]
    if dataset == "table1":
        write_table1(out_path)
    elif dataset == "table34":
        write_table34(out_path)
    else:
        sys.exit(1)
