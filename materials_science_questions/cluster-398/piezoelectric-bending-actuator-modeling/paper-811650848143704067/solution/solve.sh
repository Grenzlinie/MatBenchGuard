#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# Install required packages (the oracle sandbox has only stdlib)
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: results.json ===
cat > /app/compute_results.py << 'PYEOF'
import numpy as np, math, json, os

# ========== material data ==========
def prop_T(P, T):
    return P['P0'] * (P['Pm1']/T + 1 + P['P1']*T + P['P2']*T**2 + P['P3']*T**3)

ceramic_E={"P0":348.43e9,"Pm1":0,"P1":-3.070e-4,"P2":2.160e-7,"P3":-8.946e-11}
ceramic_alpha={"P0":5.8723e-6,"Pm1":0,"P1":9.095e-4,"P2":0,"P3":0}
ceramic_kappa=13.732
metal_E={"P0":201.04e9,"Pm1":0,"P1":3.079e-4,"P2":-6.534e-7,"P3":0}
metal_alpha={"P0":12.330e-6,"Pm1":0,"P1":8.086e-4,"P2":0,"P3":0}
metal_kappa=15.379
mu_F=0.28

C11f=121e9; C22f=121e9; C33f=111e9
C12f=75.4e9; C13f=75.2e9; C23f=75.2e9
C44f=21.1e9; C55f=21.1e9; C66f=22.6e9
e31f=-5.4; e32f=-5.4; e33f=15.8
alpha11f=0.9e-6; alpha22f=0.9e-6
kappa_f=2.1

def mat_C11m(T): return (5.4015-0.000385*T)*1e9
def mat_C12m(T): return 0.515*mat_C11m(T)
def mat_C44m(T): return 0.242*mat_C11m(T)
alpha_m=45.0e-6; kappa_m=0.19

def pfrx_props(Vf,T):
    Vm=1-Vf
    C11m=mat_C11m(T); C12m=mat_C12m(T); C13m=C12m; C23m=C12m
    C22m=C11m; C33m=C11m
    C11=(C11f*C11m)/(Vf*C11f+Vm*C11m)
    C12=C11*(Vf*C12f/C11f+Vm*C12m/C11m)
    C22=Vf*C22f+Vm*C22m+C12**2/C11-Vf*C12f**2/C11f-Vm*C12m**2/C11m
    C13=C11*(Vf*C13f/C11f+Vm*C13m/C11m)
    C23=Vf*C23f+Vm*C23m+C12*C13/C11-Vf*C12f*C13f/C11f-Vm*C12m*C13m/C11m
    C33=Vf*C33f+Vm*C33m+C13**2/C11-Vf*C13f**2/C11f-Vm*C13m**2/C11m
    C66m=0.242*C11m
    C66=(C66f*C66m)/(Vf*C66f+Vm*C66m)
    alpha11=C11*(Vf*alpha11f/C11f+Vm*alpha_m/C11m)
    alpha22=Vf*alpha22f+Vm*alpha_m+C12*alpha11/C11-Vf*C12f*alpha11f/C11f-Vm*C12m*alpha_m/C11m
    g=(Vm*C22f+Vf*C22m)*(Vm*C33f+Vf*C33m)-(Vm*C23f+Vf*C23m)**2
    e31=Vf*e31f-(Vm*Vf/g)*((C13f-C13m)*((Vm*C22f+Vf*C22m)*e33f-(Vm*C23f+Vf*C23m)*e31f)+
                             (C12f-C12m)*((Vm*C33f+Vf*C33m)*e31f-(Vm*C23f+Vf*C23m)*e33f))
    e32=Vf*e32f+(Vm/g)*(C22f*((Vm*C23f+Vf*C23m)*e33f-(Vm*C33f+Vf*C23m)*e32f)-
                          C23f*((Vm*C22f+Vf*C22m)*e33f-(Vm*C23f+Vf*C23m)*e32f))
    Q11p=C11-C13*C13/C33
    Q12p=C12-C13*C23/C33
    Q22p=C22-C23*C23/C33
    Q66p=C66
    alpha11e=alpha11-(C13*alpha11+C23*alpha22)/C33
    alpha22e=alpha22-(C13*alpha11+C23*alpha22)/C33
    e31e=e31/C66; e32e=e32/C66
    return Q11p,Q12p,Q22p,Q66p,alpha11e,alpha22e,kappa_f*Vf+kappa_m*Vm,e31e,e32e

def fgm_props(z,h,k,T):
    Vc=(0.5+z/h)**k if 0.5+z/h>0 else 0.0
    Vm=1-Vc
    Ec=prop_T(ceramic_E,T); Em=prop_T(metal_E,T)
    alphac=prop_T(ceramic_alpha,T); alpham=prop_T(metal_alpha,T)
    E=Vc*Ec+Vm*Em
    alpha=Vc*alphac+Vm*alpham
    return E,alpha

def temperature_field(H,h,k,To,Ti,Vf):
    kc=ceramic_kappa; km=metal_kappa; kcm=kc-km
    kappa_p=Vf*kappa_f+(1-Vf)*kappa_m
    imax=5
    I=sum(((-kcm/km)**i)/(i*k+1) for i in range(imax+1))
    sum_r=sum((-kcm/km)**i for i in range(imax+1))
    den=(1/(h*I))*(km+kc*sum_r)+2*kappa_p/(H-h)
    Tc=((1/(h*I))*(km*Ti+kc*sum_r*To)+2*kappa_p/(H-h)*To)/den
    Tm=((1/(h*I))*(km*Ti+kc*sum_r*To)+2*kappa_p/(H-h)*Ti)/den
    def T(z):
        if z<=-h/2:
            return (2/(H-h))*((H/2)*Tm-(h/2)*To+(Tm-To)*z)
        elif z>=h/2:
            return (2/(H-h))*((H/2)*Tc-(h/2)*Ti+(Ti-Tc)*z)
        else:
            denom=sum(((-kcm/km)**i)*((z/h+0.5)**(i*k+1))/(i*k+1) for i in range(imax+1))
            return Tm+(Tc-Tm)*(denom/I)
    return T,Tc,Tm

def compute_stiffness(H,h,k,Tfunc,Vf):
    Nz=200
    zf=np.linspace(-h/2,h/2,Nz); dz=zf[1]-zf[0]
    A11=A12=A66=0.0; B11=B12=B66=0.0; D11=D12=D66=0.0
    NxT=NyT=0.0; MxT=MyT=0.0
    for z in zf:
        T=Tfunc(z)
        E,alpha=fgm_props(z,h,k,T)
        G=E/(1-mu_F**2)
        Q11=G; Q12=mu_F*G; Q66=(1-mu_F)*G/2
        A11+=Q11*dz; A12+=Q12*dz; A66+=Q66*dz
        B11+=Q11*z*dz; B12+=Q12*z*dz; B66+=Q66*z*dz
        D11+=Q11*z**2*dz; D12+=Q12*z**2*dz; D66+=Q66*z**2*dz
        dT=T-300
        NxT+=(Q11+Q12)*alpha*dT*dz
        NyT+=(Q11+Q12)*alpha*dT*dz
        MxT+=(Q11+Q12)*alpha*dT*z*dz
        MyT+=(Q11+Q12)*alpha*dT*z*dz
    zpl=np.linspace(-H/2,-h/2,Nz//2); dzp=zpl[1]-zpl[0]
    zpr=np.linspace(h/2,H/2,Nz//2)
    all_z=np.concatenate([zpl,zpr])
    A11p=A12p=A66p=0.0; B11p=B12p=B66p=0.0; D11p=D12p=D66p=0.0
    NxPT=NyPT=0.0; MxPT=MyPT=0.0
    for z in all_z:
        T=Tfunc(z)
        Q11p,Q12p,Q22p,Q66p,a11e,a22e,kp,e31e,e32e=pfrx_props(Vf,T)
        A11p+=Q11p*dzp; A12p+=Q12p*dzp; A66p+=Q66p*dzp
        B11p+=Q11p*z*dzp; B12p+=Q12p*z*dzp; B66p+=Q66p*z*dzp
        D11p+=Q11p*z**2*dzp; D12p+=Q12p*z**2*dzp; D66p+=Q66p*z**2*dzp
        dT=T-300
        NxPT+=(Q11p*a11e+Q12p*a22e)*dT*dzp
        NyPT+=(Q12p*a11e+Q22p*a22e)*dT*dzp
        MxPT+=(Q11p*a11e+Q12p*a22e)*dT*z*dzp
        MyPT+=(Q12p*a11e+Q22p*a22e)*dT*z*dzp
    A11_t=A11+A11p; A12_t=A12+A12p; A66_t=A66+A66p
    B11_t=B11+B11p; B12_t=B12+B12p; B66_t=B66+B66p
    D11_t=D11+D11p; D12_t=D12+D12p; D66_t=D66+D66p
    NxT_tot=NxT+NxPT; NyT_tot=NyT+NyPT
    MxT_tot=MxT+MxPT; MyT_tot=MyT+MyPT
    return (A11_t,A12_t,A66_t,B11_t,B12_t,B66_t,D11_t,D12_t,D66_t,
            NxT_tot,NyT_tot,MxT_tot,MyT_tot)

def buckling_load(ABD,L,R,m,n):
    A11,A12,A66,B11,B12,B66,D11,D12,D66=ABD
    alpha=m*math.pi/L; beta=n/R
    A11b=A11; A12b=A12; B11b=B11; B12b=B12
    F6=(A11b*B12b-B11b*A12b)/A11b
    F7=(A11b**2-A12b**2)/A11b
    J1=A11b/(A11b**2-A12b**2)
    J3=(A11b*(B11b**2+B12b**2)-2*B11b*B12b*A12b+D11*(A11b**2-A12b**2))/(A12b**2-A11b**2)
    term=F7/R*alpha**2/(alpha**2+beta**2)**2-F6
    Pcr=(J1*term**2*(alpha**2+beta**2)**2+J3*(alpha**2+beta**2)**2)/alpha**2
    return Pcr

def min_critical_load(ABD,L,R):
    best=float('inf'); best_mode=(1,1)
    for m in range(1,6):
        for n in range(1,11):
            P=buckling_load(ABD,L,R,m,n)
            if P<best:
                best=P; best_mode=(m,n)
    return best,best_mode

def post_buckling_path(ABD,thermal,L,R,m,n,f2_vals):
    A11,A12,A66,B11,B12,B66,D11,D12,D66,NxT,NyT,MxT,MyT=ABD+thermal
    alpha=m*math.pi/L; beta=n/R
    A11b=A11; A12b=A12; B11b=B11; B12b=B12; D11b=D11; D12b=D12
    F0=1/(A11b**2-A12b**2)
    F6=(A11b*B12b-B11b*A12b)/A11b
    F7=(A11b**2-A12b**2)/A11b
    J1=A11b/(A11b**2-A12b**2)
    J2=2*A12b/(A12b**2-A11b**2)
    J3=(A11b*(B11b**2+B12b**2)-2*B11b*B12b*A12b+D11*(A11b**2-A12b**2))/(A12b**2-A11b**2)
    J6=1/(A11b+A12b)
    phi1=-NxT
    zeta1=J1*(F7**2*alpha**4*beta**4/(alpha**2+beta**2)**2+F7**2*alpha**4*beta**4/(9*alpha**2+beta**2)**2)
    zeta2=J1*(2*F6*F7*alpha**2*beta**2-F7**2*alpha**4*beta**2/(R*alpha**2+beta**2)**2-F7**2*beta**2/(8*R))
    zeta3=J1*(F7*alpha**2/(R*(alpha**2+beta**2))+F6*(alpha**2+beta**2))**2+J3*(alpha**2+beta**2)**2
    zeta4=-J1*F7**2*(alpha**4+beta**4)/16
    zeta5=8*J1*(F6*alpha**2-F7/(4*R))**2+8*J3*alpha**4
    loads=[]; shortenings=[]; deflections=[]
    for f2 in f2_vals:
        num=(zeta1**2*f2**3+3*zeta1*zeta2*f2**2+(zeta2**2+zeta1*(zeta3-zeta4*zeta5))*f2+zeta2*zeta3)
        den=((zeta2+(zeta1-zeta4)*f2))*alpha**2
        load=2*num/den if den!=0 else float('inf')
        c0=(F7/R)*alpha**2-F6*(alpha**2+beta**2)**2
        c1=F7*alpha**2*beta**2
        c2_val=F7**2*alpha**4*beta**4/(9*alpha**2+beta**2)**2
        c3_val=J1*(8*F6*F7*alpha**2*beta**2-4*F7**2*beta**2/R)
        c4_val=F7**2*alpha**4*beta**2
        a_f1=0.5*J1*c4_val
        b_f1=(0.5*J1/(alpha**2+beta**2)**2*(c0-c1*f2)**2
              +0.5*J1*f2**2*c2_val
              +c3_val*f2
              -0.5*alpha**2*load
              +0.5*J3*(alpha**2+beta**2)**2
              -beta**2/(4*F0*A11b)*(J2+2*F0*A12b)*load)
        f1=math.sqrt(-b_f1/a_f1) if a_f1!=0 and -b_f1/a_f1>0 else 0.0
        Nbar_y0=J6/(2*J1)*phi1
        f0=F0*R*(A11b*Nbar_y0+f1**2*beta**2/(8*F0)-A12b*load+(A11b-A12b)*phi1)-f2/2
        w_max=f0+f1+f2
        shortening=((3*alpha**2/32)*f2**2
                     -4/zeta3*(zeta1+zeta4*f2**2+zeta5*f2-0.5*alpha**2*load)
                     +F0*A12b*load
                     +0.5*F0*(A11b-A12b)*phi1)
        loads.append(load)
        shortenings.append(shortening)
        deflections.append(w_max)
    return loads,shortenings,deflections

# ======== main computation ========
out_dir=os.environ.get('OUTDIR','/app/outputs')
results={"critical_buckling_loads":[],"post_buckling":[]}

# --- critical buckling loads ---
for Ti,To,case_label in [(300,300,'I'),(600,300,'II')]:
    for k in [0,2,3,4]:
        Tfunc,_,_=temperature_field(0.005,0.003,k,To,Ti,0.6)
        ABD=compute_stiffness(0.005,0.003,k,Tfunc,0.6)[:9]
        Pcr,_=min_critical_load(ABD,3.0,0.5)
        results["critical_buckling_loads"].append({
            "Ti":Ti,"k":k,"Vf":0.6,"Pcr":round(Pcr,4)
        })

# --- post-buckling paths ---
for Ti,To,case_label in [(300,300,'I'),(600,300,'II')]:
    for k in [0.5,2.0,4.0]:
        Tfunc,_,_=temperature_field(0.005,0.003,k,To,Ti,0.6)
        stiff=compute_stiffness(0.005,0.003,k,Tfunc,0.6)
        ABD=stiff[:9]; thermal=stiff[9:]
        Pcr,mode=min_critical_load(ABD,0.5,0.5)   # L=0.5, R=0.5 (R/H=100)
        f2_arr=np.linspace(0,0.01,50)
        loads,shortenings,deflections=post_buckling_path(ABD,thermal,0.5,0.5,mode[0],mode[1],f2_arr)
        results["post_buckling"].append({
            "case":case_label,"k":k,
            "load":[round(v,6) for v in loads],
            "shortening":[round(v,8) for v in shortenings],
            "deflection":[round(v,8) for v in deflections]
        })

with open(os.path.join(out_dir,'results.json'),'w') as f:
    json.dump(results,f,indent=2)
PYEOF
python3 /app/compute_results.py
