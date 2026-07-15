#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: effective_moduli.csv ===
python3 << 'SIM_EOF' > "$OUTDIR/effective_moduli.csv"
import numpy as np

# Walpole operations -----------------------------------------------------------
def w_add(a,b): return tuple(x+y for x,y in zip(a,b))
def w_sub(a,b): return tuple(x-y for x,y in zip(a,b))
def w_dot(a,b):
    c1,g1,h1,d1,e1,f1 = a; c2,g2,h2,d2,e2,f2 = b
    return (c1*c2+2*h1*g2, g1*c2+d1*g2, c1*h2+h1*d2, d1*d2+2*g1*h2, e1*e2, f1*f2)
def w_inv(a):
    c,g,h,d,e,f = a; det = c*d - 2*g*h
    return (d/det, -g/det, -h/det, c/det, 1/e, 1/f)

# Build stiffness tensors ------------------------------------------------------
def iso_stiff(E,nu):
    fac = E/((1+nu)*(1-2*nu))
    return (fac*1, fac*nu, fac*nu, fac*(1-nu), fac*(1-2*nu), fac*(1-2*nu))
def trans_iso_stiff(EI,ET,nuII,nuTI,GI,GT):
    Theta = ET*(1-nuII) - 2*EI*nuTI**2
    c = EI*ET/Theta; g = EI*ET*nuTI/Theta; h = g
    d = ET**2*(1-nuII)/Theta; e = 2*GI; f = 2*GT
    return (c,g,h,d,e,f)

# Eshelby tensors --------------------------------------------------------------
def eshelby_cyl_iso(nu):
    return (1/(2*(1-nu)), 0, nu/(2*(1-nu)), 0, (3-4*nu)/(4*(1-nu)), 0.5)
def eshelby_cyl_trans(C_mat):
    c0,g0,h0,d0,e0,f0 = C_mat
    C11 = (c0+e0)/2; C12 = (c0-e0)/2; C44 = f0
    d = C11; e = (C11-C12)/2; f = C44; g = h0 + C44
    Sc = 1 - e/d; Sg = 0; Sh = 0.5*(g/d - f/d); Sd = 0
    Se = 0.5*(1 + e/d); Sf = 1.0
    return (Sc,Sg,Sh,Sd,Se,Sf)

# Mori–Tanaka update -----------------------------------------------------------
def mori_tanaka(C_mat, C_inc, Vf, S_of_mat):
    dC = w_sub(C_inc, C_mat)
    inner = w_add(w_dot(dC, S_of_mat), C_mat)
    A = w_sub((1,0,0,1,1,1), w_dot(S_of_mat, w_dot(w_inv(inner), dC)))
    B = w_add(((1-Vf),0,0,(1-Vf),(1-Vf),(1-Vf)), tuple(Vf*x for x in A))
    term = w_dot(dC, w_dot(A, w_inv(B)))
    return w_add(C_mat, tuple(Vf*x for x in term))

# 6×6 ↔ Walpole ----------------------------------------------------------------
def w_to_6(C):
    c,g,h,d,e,f = C; mat = np.zeros((6,6))
    mat[0,0]=mat[1,1]=(c+e)/2; mat[2,2]=d; mat[3,3]=mat[4,4]=f; mat[5,5]=e
    mat[0,1]=mat[1,0]=(c-e)/2; mat[0,2]=mat[2,0]=h; mat[1,2]=mat[2,1]=h
    return mat

def w_from_6(C6):
    c = C6[0,0]+C6[0,1]; e = C6[0,0]-C6[0,1]; d = C6[2,2]
    h = C6[0,2]; g = h; f = C6[3,3]
    return (c,g,h,d,e,f)

# Rotation tools ---------------------------------------------------------------
def rot_y(beta):
    c=np.cos(beta); s=np.sin(beta)
    return np.array([[c,0,s],[0,1,0],[-s,0,c]])
def rot_z(theta):
    c=np.cos(theta); s=np.sin(theta)
    return np.array([[c,-s,0],[s,c,0],[0,0,1]])

def bond_matrix(R):
    M=np.zeros((6,6))
    # Indices: 0:11,1:22,2:33,3:23,4:13,5:12
    r = R
    M[0,0]=r[0,0]**2; M[0,1]=r[0,1]**2; M[0,2]=r[0,2]**2; M[0,3]=2*r[0,1]*r[0,2]; M[0,4]=2*r[0,0]*r[0,2]; M[0,5]=2*r[0,0]*r[0,1]
    M[1,0]=r[1,0]**2; M[1,1]=r[1,1]**2; M[1,2]=r[1,2]**2; M[1,3]=2*r[1,1]*r[1,2]; M[1,4]=2*r[1,0]*r[1,2]; M[1,5]=2*r[1,0]*r[1,1]
    M[2,0]=r[2,0]**2; M[2,1]=r[2,1]**2; M[2,2]=r[2,2]**2; M[2,3]=2*r[2,1]*r[2,2]; M[2,4]=2*r[2,0]*r[2,2]; M[2,5]=2*r[2,0]*r[2,1]
    M[3,0]=r[1,0]*r[2,0]; M[3,1]=r[1,1]*r[2,1]; M[3,2]=r[1,2]*r[2,2]; M[3,3]=r[1,1]*r[2,2]+r[1,2]*r[2,1]; M[3,4]=r[1,0]*r[2,2]+r[1,2]*r[2,0]; M[3,5]=r[1,0]*r[2,1]+r[1,1]*r[2,0]
    M[4,0]=r[2,0]*r[0,0]; M[4,1]=r[2,1]*r[0,1]; M[4,2]=r[2,2]*r[0,2]; M[4,3]=r[2,1]*r[0,2]+r[2,2]*r[0,1]; M[4,4]=r[2,0]*r[0,2]+r[2,2]*r[0,0]; M[4,5]=r[2,0]*r[0,1]+r[2,1]*r[0,0]
    M[5,0]=r[0,0]*r[1,0]; M[5,1]=r[0,1]*r[1,1]; M[5,2]=r[0,2]*r[1,2]; M[5,3]=r[0,1]*r[1,2]+r[0,2]*r[1,1]; M[5,4]=r[0,0]*r[1,2]+r[0,2]*r[1,0]; M[5,5]=r[0,0]*r[1,1]+r[0,1]*r[1,0]
    return M

def orientation_average_2D(C_loc_6):
    """Average a stiffness tensor (symmetry axis 3) over all in‑plane (1‑2) orientations."""
    N = 2000
    sum6 = np.zeros((6,6))
    for k in range(N):
        theta = 2*np.pi*k/N
        # Rotate original 3‑axis to (cosθ, sinθ, 0) in global (X3 axis remains fiber direction).
        R = rot_z(theta) @ rot_y(-np.pi/2)
        M = bond_matrix(R)
        Cglob = M @ C_loc_6 @ M.T
        sum6 += Cglob
    C_avg = sum6 / N
    # symmetrize expected transversely isotropic about 3
    C_avg[0,0]=C_avg[1,1]=(C_avg[0,0]+C_avg[1,1])/2
    C_avg[0,1]=C_avg[1,0]=(C_avg[0,1]+C_avg[1,0])/2
    C_avg[3,3]=C_avg[4,4]=(C_avg[3,3]+C_avg[4,4])/2
    return C_avg

#-------------------------------------------------------------------------------
# Material constants (MPa)
nu_M = 0.3; E_M = 2890;   C_mat = iso_stiff(E_M, nu_M)
E_CN = 1000000; nu_CN = 0.3; C_CNT = iso_stiff(E_CN, nu_CN)
C_fiber = trans_iso_stiff(15410, 230000, 0.46, 0.29, 10040, 25000)

# Geometry (nm)
rF = 7000; rCN = 1.357; lCN = 1500
Nlay = 10; tlay = lCN / (Nlay-2)

cases = [
    ("Vf0.3_Vcnt0.08", 0.003, 0.0008),
    ("Vf67_Vcnt20",  0.67,  0.20),
    ("Vf41_Vcnt2",   0.41,  0.02),
]

def rho(Vf, Vcnt):
    # Eq.(36) solved for areal density
    return Vcnt * rF / (2*np.pi * rCN**2 * lCN * Vf)

print("Case,E11_GPa,E22_GPa")

for name, Vf, Vcnt in cases:
    rhoCN = rho(Vf, Vcnt)

    # Build phases [0]=fiber, [1..Nlay-2]=interphase, [Nlay-1]=matrix
    phases = [C_fiber]
    for i in range(2, Nlay):   # interphase layers 2..N-1
        # Local CNT volume fraction in layer i (Eq.21)
        Vi_loc = 2*np.pi * rhoCN * rF * rCN**2 / (2*rF + (2*i-3)*tlay)
        # Micro-scale homogenization (Mori-Tanaka, cylindrical inclusion in isotropic polymer)
        C_loc = mori_tanaka(C_mat, C_CNT, Vi_loc, eshelby_cyl_iso(nu_M))
        # Transform from local (radial symmetry axis) to global (fiber-axis symmetry) via 2D random orientation average
        C6_loc = w_to_6(C_loc)
        C6_avg = orientation_average_2D(C6_loc)
        C_glo = w_from_6(C6_avg)
        phases.append(C_glo)
    phases.append(C_mat)

    # Global volume fractions of layers (Eq.32) and matrix
    V_lay = [ Vf * (2*rF*tlay + (2*i-3)*tlay**2) / (rF**2) for i in range(2, Nlay) ]
    Vmat = 1.0 - Vf - sum(V_lay)
    Vols = [Vf] + V_lay + [Vmat]

    # Sequentially homogenisation (outside → inside)
    C_eff = phases[-1]
    V_eff = Vols[-1]
    for j in range(Nlay-2, -1, -1):
        f = Vols[j] / (Vols[j] + V_eff)     # volume fraction of phase j in binary mix
        S = eshelby_cyl_trans(C_eff)          # Eshelby tensor in current transversely isotropic medium
        dC = w_sub(phases[j], C_eff)
        inner = w_add(w_dot(dC, S), C_eff)
        A = w_sub((1,0,0,1,1,1), w_dot(S, w_dot(w_inv(inner), dC)))
        B = w_add( ((1-f),0,0,(1-f),(1-f),(1-f)), tuple(f*x for x in A) )
        term = w_dot(dC, w_dot(A, w_inv(B)))
        C_eff = w_add(C_eff, tuple(f*x for x in term))
        V_eff += Vols[j]

    # Extract E11 (axial) and E22 (transverse) by inverting the 6x6 stiffness matrix
    C6_eff = w_to_6(C_eff)
    S6 = np.linalg.inv(C6_eff)    # compliance matrix (1/MPa)
    E11_MPa = 1.0 / S6[2,2]       # compliance component S33 = 1/E_axial
    E22_MPa = 1.0 / S6[0,0]       # compliance component S11 = 1/E_transverse
    print(f"{name},{E11_MPa/1000:.4f},{E22_MPa/1000:.4f}")
SIM_EOF
