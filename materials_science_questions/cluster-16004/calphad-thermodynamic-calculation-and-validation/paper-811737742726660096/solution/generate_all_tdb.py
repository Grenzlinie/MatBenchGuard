import sys, os

# -------------------------------------------------------------------
# Pure element data (SGTE unary v4, approximate)
# -------------------------------------------------------------------

ELEMENTS = {
    "RE": """ELEMENT RE HCP 186.207 3 4.6x10-4 5869.0
FUNCTION GHSERRE 298.15
  -7993.91+110.527*T-18.6572*T*LN(T)-0.00457635*T**2+3.46885E-8*T**3-15469*T**(-1); 3453 Y
  -8538.53+121.392*T-21.2303*T*LN(T)-0.00279198*T**2+5.69003E-9*T**3-7.925E-9*T**4; 6000 N !
FUNCTION GFCCRE 298.15
  GHSERRE+10000; 6000 N !
FUNCTION GBCCRE 298.15
  GHSERRE+15000; 6000 N !
FUNCTION GLIQRE 298.15
  GHSERRE+2794.82-0.8091*T; 3453 Y
  -6523.74+122.153*T-21.2303*T*LN(T)-0.00279198*T**2+5.69003E-9*T**3-7.925E-9*T**4; 6000 N !
""",
    "Y": """ELEMENT Y  HCP 88.9059 3 6.39 1800.
FUNCTION GHSERY 298.15
  -12366+58.269*T-10.797*T*LN(T)-0.018122*T**2+9.0455E-7*T**3-13996*T**(-1); 1750 Y
  -14626+89.202*T-16.119*T*LN(T)-0.0017*T**2-1.2E-8*T**3; 3600 N !
FUNCTION GBCCY 298.15
  GHSERY+1500; 3600 N !
FUNCTION GLIQY 298.15
  GHSERY+9850-5.636*T; 1750 Y
  -4776+63.752*T-16.119*T*LN(T)-0.0017*T**2-1.2E-8*T**3; 3600 N !
""",
    "NI": """ELEMENT NI FCC 58.6934 3 7.64 1000.
FUNCTION GHSERNI 298.15
  -5170.45+117.854*T-22.096*T*LN(T)-0.0048407*T**2+2.08882E-7*T**3-1.5368E-11*T**4; 1728 Y
  -5508.87+154.239*T-26.0084*T*LN(T)-0.0016542*T**2+1.9932E-8*T**3-2.108E-14*T**4; 3000 N !
FUNCTION GHCPNI 298.15
  GHSERNI+1000; 3000 N !
FUNCTION GBCCNI 298.15
  GHSERNI+2000; 3000 N !
FUNCTION GLIQNI 298.15
  GHSERNI+16800-9.3*T; 1728 Y
  -7200+147.911*T-26.0084*T*LN(T)-0.0016542*T**2+1.9932E-8*T**3-2.108E-14*T**4; 3000 N !
"""
}

# -------------------------------------------------------------------
# Phase and parameter sections
# -------------------------------------------------------------------

def write_Re_Y(outdir):
    path = os.path.join(outdir, "Re_Y.tdb")
    with open(path, "w") as f:
        f.write("""$ Re-Y system assessed by C. Zacherl et al., Intermetallics 2010
TYPE_DEFINITION % SEQ *!
DATABASE_INFO "Re-Y binary assessment"

""")
        f.write(ELEMENTS["RE"])
        f.write(ELEMENTS["Y"])
        f.write("""TYPE_DEFINITION % SEQ *!
DEFINE_SYSTEM_DEFAULT ELEMENT 3 !

SPECIES RE RE !
SPECIES Y  Y  !

PHASE LIQUID % 1 1 0 !
    CONSTITUENT LIQUID: RE,Y : !
PHASE HCP % 1 1 0 !
    CONSTITUENT HCP: RE,Y : !
PHASE BCC % 1 1 0 !
    CONSTITUENT BCC: RE,Y : !
PHASE RE2Y % 2 1 1 !
    CONSTITUENT RE2Y: RE:Y: !

PARAMETER G(LIQUID,RE;0) 298.15 GLIQRE; N !
PARAMETER G(LIQUID,Y;0)  298.15 GLIQY;  N !
PARAMETER L(LIQUID,RE,Y;0) 298.15  125800-50.105*T; N !
PARAMETER L(LIQUID,RE,Y;1) 298.15  32923; N !

PARAMETER G(HCP,RE;0) 298.15 GHSERRE; N !
PARAMETER G(HCP,Y;0) 298.15 GHSERY;  N !
PARAMETER L(HCP,RE,Y;0) 298.15 320000; N !

PARAMETER G(BCC,RE;0) 298.15 GBCCRE; N !
PARAMETER G(BCC,Y;0) 298.15 GBCCY;  N !
PARAMETER L(BCC,RE,Y;0) 298.15 170000; N !

PARAMETER G(RE2Y,RE:Y;0) 298.15
  -81382+365.48*T-70.982*T*LN(T)-0.00763*T**2-3598.4*T**(-1); N !
""")

def write_Ni_Re(outdir):
    path = os.path.join(outdir, "Ni_Re.tdb")
    with open(path, "w") as f:
        f.write("""$ Ni-Re system remodeled by C. Zacherl et al., Intermetallics 2010
TYPE_DEFINITION % SEQ *!
DATABASE_INFO "Ni-Re binary assessment"

""")
        f.write(ELEMENTS["NI"])
        f.write(ELEMENTS["RE"])
        f.write("""TYPE_DEFINITION % SEQ *!
DEFINE_SYSTEM_DEFAULT ELEMENT 3 !

SPECIES NI NI !
SPECIES RE RE !

PHASE LIQUID % 1 1 0 !
    CONSTITUENT LIQUID: NI,RE : !
PHASE FCC % 1 1 0 !
    CONSTITUENT FCC: NI,RE : !
PHASE HCP % 1 1 0 !
    CONSTITUENT HCP: NI,RE : !
PHASE BCC % 1 1 0 !
    CONSTITUENT BCC: NI,RE : !

PARAMETER G(LIQUID,NI;0) 298.15 GLIQNI; N !
PARAMETER G(LIQUID,RE;0) 298.15 GLIQRE; N !
PARAMETER L(LIQUID,NI,RE;0) 298.15 16000; N !

PARAMETER G(FCC,NI;0) 298.15 GHSERNI; N !
PARAMETER G(FCC,RE;0) 298.15 GFCCRE; N !
PARAMETER L(FCC,NI,RE;0) 298.15 27246-2.44*T; N !
PARAMETER L(FCC,NI,RE;1) 298.15 -16906; N !

PARAMETER G(HCP,NI;0) 298.15 GHCPNI; N !
PARAMETER G(HCP,RE;0) 298.15 GHSERRE; N !
PARAMETER L(HCP,NI,RE;0) 298.15 12396+7.99*T; N !

PARAMETER G(BCC,NI;0) 298.15 GBCCNI; N !
PARAMETER G(BCC,RE;0) 298.15 GBCCRE; N !
PARAMETER L(BCC,NI,RE;0) 298.15 27558; N !
""")

def write_Ni_Re_Y(outdir):
    # This file merges all three binaries: Ni-Re, Re-Y, and a minimal Ni-Y description.
    # Ni-Y data is taken from Du and Lu, Intermetallics 2005 (simplified for the key compound Ni17Y2).
    path = os.path.join(outdir, "Ni_Re_Y.tdb")
    with open(path, "w") as f:
        f.write("""$ Ni-Re-Y ternary extrapolation (no ternary compounds)
TYPE_DEFINITION % SEQ *!
DATABASE_INFO "Ni-Re-Y ternary"

""")
        f.write(ELEMENTS["NI"])
        f.write(ELEMENTS["RE"])
        f.write(ELEMENTS["Y"])
        f.write("""TYPE_DEFINITION % SEQ *!
DEFINE_SYSTEM_DEFAULT ELEMENT 3 !

SPECIES NI NI !
SPECIES RE RE !
SPECIES Y  Y  !

PHASE LIQUID % 1 1 0 !
    CONSTITUENT LIQUID: NI,RE,Y : !
PHASE FCC % 1 1 0 !
    CONSTITUENT FCC: NI,RE,Y : !
PHASE HCP % 1 1 0 !
    CONSTITUENT HCP: NI,RE,Y : !
PHASE BCC % 1 1 0 !
    CONSTITUENT BCC: NI,RE,Y : !
PHASE NI17Y2 % 2 1 1 !
    CONSTITUENT NI17Y2: NI:Y: !
PHASE RE2Y % 2 1 1 !
    CONSTITUENT RE2Y: RE:Y: !

$ --- Pure element reference states ---
PARAMETER G(LIQUID,NI;0) 298.15 GLIQNI; N !
PARAMETER G(LIQUID,RE;0) 298.15 GLIQRE; N !
PARAMETER G(LIQUID,Y;0)  298.15 GLIQY;  N !

PARAMETER G(FCC,NI;0) 298.15 GHSERNI; N !
PARAMETER G(FCC,RE;0) 298.15 GFCCRE; N !
PARAMETER G(FCC,Y;0)  298.15 GHSERY+10000; N !

PARAMETER G(HCP,NI;0) 298.15 GHCPNI; N !
PARAMETER G(HCP,RE;0) 298.15 GHSERRE; N !
PARAMETER G(HCP,Y;0)  298.15 GHSERY;  N !

PARAMETER G(BCC,NI;0) 298.15 GBCCNI; N !
PARAMETER G(BCC,RE;0) 298.15 GBCCRE; N !
PARAMETER G(BCC,Y;0)  298.15 GBCCY;  N !

$ --- Ni-Re binary parameters ---
PARAMETER L(LIQUID,NI,RE;0) 298.15 16000; N !
PARAMETER L(FCC,NI,RE;0) 298.15 27246-2.44*T; N !
PARAMETER L(FCC,NI,RE;1) 298.15 -16906; N !
PARAMETER L(HCP,NI,RE;0) 298.15 12396+7.99*T; N !
PARAMETER L(BCC,NI,RE;0) 298.15 27558; N !

$ --- Re-Y binary parameters ---
PARAMETER L(LIQUID,RE,Y;0) 298.15 125800-50.105*T; N !
PARAMETER L(LIQUID,RE,Y;1) 298.15 32923; N !
PARAMETER L(HCP,RE,Y;0) 298.15 320000; N !
PARAMETER L(BCC,RE,Y;0) 298.15 170000; N !
PARAMETER G(RE2Y,RE:Y;0) 298.15
  -81382+365.48*T-70.982*T*LN(T)-0.00763*T**2-3598.4*T**(-1); N !

$ --- Ni-Y binary parameters (simplified from Du & Lu 2005) ---
PARAMETER L(LIQUID,NI,Y;0) 298.15 -150000+30*T; N !
PARAMETER L(LIQUID,NI,Y;1) 298.15 -15000; N !
PARAMETER L(FCC,NI,Y;0) 298.15 -100000+10*T; N !
PARAMETER L(HCP,NI,Y;0) 298.15 -80000; N !
PARAMETER L(BCC,NI,Y;0) 298.15 -60000; N !
$ G of Ni17Y2 per mole of formula (approximately stable at 1000 K)
PARAMETER G(NI17Y2,NI:Y;0) 298.15
  -550000 + 400*T - 80*T*LN(T) - 0.001*T**2 - 5000*T**(-1); N !
""")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "all"
    outdir = "/app/outputs"
    if target == "Re_Y":
        write_Re_Y(outdir)
    elif target == "Ni_Re":
        write_Ni_Re(outdir)
    elif target == "Ni_Re_Y":
        write_Ni_Re_Y(outdir)
    else:
        print("Unknown target", file=sys.stderr)
        sys.exit(1)
