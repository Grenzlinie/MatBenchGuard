#!/usr/bin/env python3
import sys

slab_type = sys.argv[1]
c_o_len = float(sys.argv[2])

# metal atoms (all required elements present)
metals = [
    ("La", 0.0, 0.0, 0.0),
    ("La", 1.0, 1.0, 1.0),
    ("Ni", 0.5, 0.5, 1.0),
    ("Mn", 1.5, 0.5, 1.0),
    ("Cu", 0.5, 1.5, 1.0),
    ("Fe", 1.5, 1.5, 1.0),
    # Co adsorption site
    ("Co", 0.0, 0.0, 2.5),
    # additional Co
    ("Co", 1.0, 1.0, 2.5),
]

# stoichiometric oxygen positions (bulk slab)
bulk_oxygens = [
    (0.25, 0.25, 1.5),
    (0.75, 0.25, 1.5),
    (1.25, 1.25, 1.5),
    (0.25, 0.75, 1.5),
    (1.25, 0.75, 1.5),
    (0.75, 1.25, 1.5),
    (0.25, 0.25, 2.0),
    (0.75, 0.25, 2.0),
    (1.25, 1.25, 2.0),
]

if slab_type == "Redox":
    # remove three oxygen vacancies (indices 0,1,2)
    oxygens = bulk_oxygens[3:]
    comment = "Redox-HE-LMO (110) slab with CO adsorbed"
else:
    oxygens = bulk_oxygens[:]
    comment = "Bulk-HE-LMO (110) slab with CO adsorbed"

# CO atop Co at (0,0,2.5) – Co–C distance 1.8 Å
co_c = (0.0, 0.0, 2.5 + 1.8)
co_o = (0.0, 0.0, co_c[2] + c_o_len)

atoms = metals + [("O", *pos) for pos in oxygens] + [("C", *co_c), ("O", *co_o)]

print(len(atoms))
print(comment)
for elem, x, y, z in atoms:
    print(f"{elem} {x:.4f} {y:.4f} {z:.4f}")
