#!/usr/bin/env python3
import json, sys

def space_groups_data():
    sg_2H_bulk = {
        "space_group_HM": "P6_3/mmc",
        "space_group_Schoenflies": "D_{6h}^4",
        "space_group_number": 194,
    }
    sg_2H_Nodd = {
        "space_group_HM": "P\\bar{6}m2",
        "space_group_Schoenflies": "D_{3h}^1",
        "space_group_number": 187,
    }
    sg_2H_Neven = {
        "space_group_HM": "P\\bar{3}m1",
        "space_group_Schoenflies": "D_{3d}^3",
        "space_group_number": 164,
    }
    sg_1T_all = sg_2H_Neven

    gwv_bulk = {
        "Gamma": "D_{6h}^4",
        "K": "D_{3h}^1",
        "Kprime": "D_{3h}^1",
        "M": "D_{2h}^17",
        "Sigma": "C_{2v}^14",
        "T": "C_{2v}^16",
        "Tprime": "C_{2v}^16",
        "u": "C_s^{xy}"
    }
    gwv_Nodd = {
        "Gamma": "D_{3h}^1",
        "K": "C_{3h}^1",
        "Kprime": "C_{3h}^1",
        "M": "C_{2v}^14",
        "Sigma": "C_{2v}^14",
        "T": "C_s^{xy}",
        "Tprime": "C_s^{xy}",
        "u": "C_s^{xy}"
    }
    gwv_Neven = {
        "Gamma": "D_{3d}^3",
        "K": "D_3^2",
        "Kprime": "D_3^2",
        "M": "C_{2h}^3",
        "Sigma": "C_s^{xz}",
        "T": "C_2^3",
        "Tprime": "C_2^3",
        "u": "C_1^1"
    }
    gwv_1T_all = gwv_Neven

    entries = []
    for poly in ["2Ha", "2Hc"]:
        for case, sg, gwv in [("bulk", sg_2H_bulk, gwv_bulk),
                              ("N_odd", sg_2H_Nodd, gwv_Nodd),
                              ("N_even", sg_2H_Neven, gwv_Neven),
                              ("1TL", sg_2H_Nodd, gwv_Nodd)]:
            entries.append({"polytype": poly, "layer_case": case, **sg, "GWV": gwv})
    for case, sg, gwv in [("bulk", sg_1T_all, gwv_1T_all),
                          ("N_odd", sg_1T_all, gwv_1T_all),
                          ("N_even", sg_1T_all, gwv_1T_all),
                          ("1TL", sg_1T_all, gwv_1T_all)]:
        entries.append({"polytype": "1T", "layer_case": case, **sg, "GWV": gwv})
    return entries

def irreps_data():
    # formulas as strings; use Greek letters and symbols
    data = {}
    # 2Ha
    data["2Ha_N_odd"] = {
        "Gamma": "(3N-1)/2(\u03931+\u2295\u03933+)\u2295(3N+1)/2(\u03931+\u2295\u03932+)",
        "K": "(3N-1)/2(K1+\u2295K2+\u2295K2+*)\u2295(3N+1)/2(K3+\u2295K2+*\u2295K1+)",
        "Kprime": "(3N-1)/2(K1+\u2295K2+\u2295K2+*)\u2295(3N+1)/2(K3+\u2295K2+*\u2295K1+)",
        "M": "3N(M1\u2295M4)\u2295(3N-1)/2 M2\u2295(3N+1)/2 M3",
        "Sigma": "3N(\u03a31\u2295\u03a34)\u2295(3N-1)/2 \u03a32\u2295(3N+1)/2 \u03a33",
        "T": "(9N+1)/2 T+\u2295(9N-1)/2 T-",
        "Tprime": "(9N+1)/2 T+\u2295(9N-1)/2 T-",
        "u": "(9N+1)/2 u+\u2295(9N-1)/2 u-"
    }
    data["2Ha_N_even"] = {
        "Gamma": "(3N/2)(\u03931+\u2295\u03933+\u2295\u03932-\u2295\u03933-)",
        "K": "(3N/2)(K1\u2295K2)\u22953NK3",
        "Kprime": "(3N/2)(K1\u2295K2)\u22953NK3",
        "M": "3N(M1+\u2295M2+)\u2295(3N/2)(M2+\u2295M1+)",
        "Sigma": "6N\u03a31\u22953N\u03a32",
        "T": "(9N/2)(T1\u2295T2)",
        "Tprime": "(9N/2)(T1\u2295T2)",
        "u": "9Nu"
    }
    # 2Hc
    data["2Hc_N_odd"] = {
        "Gamma": "(3N-1)/2(\u03931+\u2295\u03933+)\u2295(3N+1)/2(\u03933+\u2295\u03932-)",
        "K": "(3N+1)/2(K1+\u2295K2+\u2295K3-*)\u2295(3N-1)/2(K1-\u2295K2-\u2295K3+*)",
        "Kprime": "(3N+1)/2(K1-\u2295K2-\u2295K3+*)\u2295(3N-1)/2(K1+\u2295K2+\u2295K3-*)",  # complex conjugate
        "M": "3N(M1\u2295M4)\u2295(3N-1)/2 M2\u2295(3N+1)/2 M3",
        "Sigma": "3N(\u03a31\u2295\u03a34)\u2295(3N-1)/2 \u03a32\u2295(3N+1)/2 \u03a33",
        "T": "(9N+1)/2 T+\u2295(9N-1)/2 T-",
        "Tprime": "(9N+1)/2 T+\u2295(9N-1)/2 T-",
        "u": "(9N+1)/2 u+\u2295(9N-1)/2 u-"
    }
    data["2Hc_N_even"] = {
        "Gamma": "(3N/2)(\u03931+\u2295\u03933+\u2295\u03932-\u2295\u03933-)",
        "K": "(3N/2)(K1\u2295K2)\u22953NK3",
        "Kprime": "(3N/2)(K1\u2295K2)\u22953NK3",
        "M": "3N(M1+\u2295M2-)\u2295(3N/2)(M2+\u2295M1-)",
        "Sigma": "6N\u03a31\u22953N\u03a32",
        "T": "(9N/2)(T1\u2295T2)",
        "Tprime": "(9N/2)(T1\u2295T2)",
        "u": "9Nu"
    }
    # 1T
    data["1T_N_odd"] = {
        "Gamma": "(3N-1)/2(\u03931+\u2295\u03933+)\u2295(3N+1)/2(\u03932-\u2295\u03933-)",
        "K": "(3N-1)/2 K1\u2295(3N+1)/2 K2\u22953NK3",
        "Kprime": "(3N-1)/2 K1\u2295(3N+1)/2 K2\u22953NK3",
        "M": "(3N-1)(M1+\u2295M1-)\u2295(3N-1)/2 M2+\u2295(3N+1)M2-",
        "Sigma": "6N\u03a31\u22953N\u03a32",
        "T": "(9N-1)/2 T1\u2295(9N+1)/2 T2",
        "Tprime": "(9N-1)/2 T1\u2295(9N+1)/2 T2",
        "u": "9Nu"
    }
    data["1T_N_even"] = {
        "Gamma": "(3N/2)(\u03931+\u2295\u03933+\u2295\u03932-\u2295\u03933-)",
        "K": "(3N/2)(K1\u2295K2)\u22953NK3",
        "Kprime": "(3N/2)(K1\u2295K2)\u22953NK3",
        "M": "3N(M1+\u2295M2-)\u2295(3N/2)(M2+\u2295M1-)",
        "Sigma": "6N\u03a31\u22953N\u03a32",
        "T": "(9N/2)(T1\u2295T2)",
        "Tprime": "(9N/2)(T1\u2295T2)",
        "u": "9Nu"
    }
    return data

def selection_rules_data():
    entries = []
    # bulk
    for poly in ["2Ha", "2Hc"]:
        entries.append({
            "polytype": poly,
            "layer_case": "bulk",
            "Gamma_vib_irrep": "\u03931+\u22952\u03933+\u2295\u03935+\u22952\u03936+\u22952\u03932-\u2295\u03934-\u22952\u03935-\u2295\u03936-",
            "Raman_active_irreps": "\u03931+\u2295\u03935+\u22952\u03936+",
            "IR_active_irreps": "\u03932-\u2295\u03935-",
            "acoustic_irreps": "\u03932-\u2295\u03935-",
            "silent_irreps": "2\u03933+\u2295\u03934-\u2295\u03936-"
        })
    # 1T bulk
    entries.append({
        "polytype": "1T",
        "layer_case": "bulk",
        "Gamma_vib_irrep": "\u03931+\u2295\u03933+\u22952\u03932-\u22952\u03933-",
        "Raman_active_irreps": "\u03931+\u2295\u03933+",
        "IR_active_irreps": "\u03932-\u2295\u03933-",
        "acoustic_irreps": "\u03932-\u2295\u03933-",
        "silent_irreps": "-"
    })
    # N odd / 1TL for 2H
    for poly in ["2Ha", "2Hc"]:
        for case in ["N_odd", "1TL"]:
            entries.append({
                "polytype": poly,
                "layer_case": case,
                "Gamma_vib_irrep": "(3N-1)/2(\u03931+\u2295\u03933-)\u2295(3N+1)/2(\u03933+\u2295\u03932-)",
                "Raman_active_irreps": "(3N-1)/2(\u03931+\u2295\u03933-\u2295\u03932+)",
                "IR_active_irreps": "(3N-1)/2(\u03933+\u2295\u03932-)",
                "acoustic_irreps": "\u03933+\u2295\u03932-",
                "silent_irreps": "-"
            })
    # N even for 2H
    for poly in ["2Ha", "2Hc"]:
        entries.append({
            "polytype": poly,
            "layer_case": "N_even",
            "Gamma_vib_irrep": "(3N/2)(\u03931+\u2295\u03933+\u2295\u03932-\u2295\u03933-)",
            "Raman_active_irreps": "(3N/2)(\u03931+\u2295\u03933+)",
            "IR_active_irreps": "(3N-2)/2(\u03932-\u2295\u03933-)",
            "acoustic_irreps": "\u03932-\u2295\u03933-",
            "silent_irreps": "-"
        })
    # 1T N odd / 1TL
    for case in ["N_odd", "1TL"]:
        entries.append({
            "polytype": "1T",
            "layer_case": case,
            "Gamma_vib_irrep": "(3N-1)/2(\u03931+\u2295\u03933+)\u2295(3N+1)/2(\u03932-\u2295\u03933-)",
            "Raman_active_irreps": "(3N-1)/2(\u03931+\u2295\u03933+)",
            "IR_active_irreps": "(3N-1)/2(\u03932-\u2295\u03933-)",
            "acoustic_irreps": "\u03932-\u2295\u03933-",
            "silent_irreps": "-"
        })
    # 1T N even
    entries.append({
        "polytype": "1T",
        "layer_case": "N_even",
        "Gamma_vib_irrep": "(3N/2)(\u03931+\u2295\u03933+\u2295\u03932-\u2295\u03933-)",
        "Raman_active_irreps": "(3N/2)(\u03931+\u2295\u03933+)",
        "IR_active_irreps": "(3N-2)/2(\u03932-\u2295\u03933-)",
        "acoustic_irreps": "\u03932-\u2295\u03933-",
        "silent_irreps": "-"
    })
    return entries

def raman_tensors_data():
    tensors = []
    # D_{6h}^4 bulk 2H
    tensors.append({
        "space_group": "P6_3/mmc",
        "point_group": "D_{6h}^4",
        "irrep_label": "\u03931+(A1g)",
        "tensor": [["a","0","0"],["0","a","0"],["0","0","b"]]
    })
    # E1g two components
    tensors.append({
        "space_group": "P6_3/mmc",
        "point_group": "D_{6h}^4",
        "irrep_label": "\u03935+(E1g)_1",
        "tensor": [["0","0","0"],["0","0","0"],["0","0","0"]]
    })
    tensors.append({
        "space_group": "P6_3/mmc",
        "point_group": "D_{6h}^4",
        "irrep_label": "\u03935+(E1g)_2",
        "tensor": [["0","0","-c"],["0","0","0"],["-c","0","0"]]
    })
    # E2g
    tensors.append({
        "space_group": "P6_3/mmc",
        "point_group": "D_{6h}^4",
        "irrep_label": "\u03936+(E2g)_1",
        "tensor": [["d","0","0"],["0","-d","0"],["0","0","0"]]
    })
    tensors.append({
        "space_group": "P6_3/mmc",
        "point_group": "D_{6h}^4",
        "irrep_label": "\u03936+(E2g)_2",
        "tensor": [["0","-d","0"],["-d","0","0"],["0","0","0"]]
    })
    # D_{3h}^1  (P-6m2) N odd 2H
    D3h1 = "P\\bar{6}m2"
    pd3h1 = "D_{3h}^1"
    tensors.append({
        "space_group": D3h1,
        "point_group": pd3h1,
        "irrep_label": "\u03931+(A1')",
        "tensor": [["a","0","0"],["0","a","0"],["0","0","b"]]
    })
    tensors.append({
        "space_group": D3h1,
        "point_group": pd3h1,
        "irrep_label": "\u03933+(E')(x)",
        "tensor": [["d","0","0"],["0","-d","0"],["0","0","0"]]
    })
    tensors.append({
        "space_group": D3h1,
        "point_group": pd3h1,
        "irrep_label": "\u03933+(E')(y)",
        "tensor": [["0","-d","0"],["-d","0","0"],["0","0","0"]]
    })
    tensors.append({
        "space_group": D3h1,
        "point_group": pd3h1,
        "irrep_label": "\u03933-(E'')(1)",
        "tensor": [["0","0","-c"],["0","0","0"],["-c","0","0"]]
    })
    tensors.append({
        "space_group": D3h1,
        "point_group": pd3h1,
        "irrep_label": "\u03933-(E'')(2)",
        "tensor": [["0","0","0"],["0","0","c"],["0","c","0"]]
    })
    # D_{3d}^3  (P-3m1) N even 2H and all 1T
    D3d3 = "P\\bar{3}m1"
    pd3d3 = "D_{3d}^3"
    tensors.append({
        "space_group": D3d3,
        "point_group": pd3d3,
        "irrep_label": "\u03931+(A1g)",
        "tensor": [["a","0","0"],["0","a","0"],["0","0","b"]]
    })
    tensors.append({
        "space_group": D3d3,
        "point_group": pd3d3,
        "irrep_label": "\u03933+(E_g)(1)",
        "tensor": [["c","0","0"],["0","-c","d"],["0","d","0"]]
    })
    tensors.append({
        "space_group": D3d3,
        "point_group": pd3d3,
        "irrep_label": "\u03933+(E_g)(2)",
        "tensor": [["0","-c","-d"],["-c","0","0"],["-d","0","0"]]
    })
    return tensors

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    target = sys.argv[1]
    if target == "space_groups":
        json.dump(space_groups_data(), sys.stdout, indent=2, ensure_ascii=False)
    elif target == "irreps":
        json.dump(irreps_data(), sys.stdout, indent=2, ensure_ascii=False)
    elif target == "selection_rules":
        json.dump(selection_rules_data(), sys.stdout, indent=2, ensure_ascii=False)
    elif target == "raman_tensors":
        json.dump(raman_tensors_data(), sys.stdout, indent=2, ensure_ascii=False)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
