Earth and Planetary Science Letters 562 (2021) 116873

![](./images/812486899028459521_1.jpg)

Contents lists available at ScienceDirect

# Earth and Planetary Science Letters

www.elsevier.com/locate/eps

![](./images/812486899028459521_2.jpg)

# Deep fractionation of Hf in a solidifying magma ocean and its implications for tungsten isotopic heterogeneities in the mantle

![](./images/812486899028459521_3.jpg)

Jie Deng*, Lars Stixrude

Department of Earth, Planetary, and Space Sciences, University of California, Los Angeles, 90095, United States of America

---

## ARTICLE INFO

**Article history:**
Received 27 June 2020
Received in revised form 1 March 2021
Accepted 2 March 2021
Available online 16 March 2021
Editor: J. Badro

**Keywords:**
tungsten anomaly
silicate melt partitioning
ab initio calculation

## ABSTRACT

Recent geochemical studies document a wide range of $^{182}$W anomalies in mantle-derived rocks, the origin of which is unknown. Here we explore the consequences of basal magma ocean crystallization while $^{182}$Hf was extant. We determine the partition coefficient of Hf between bridgmanite and silicate melt $D_{\text{Hf}}$ throughout the pressure-temperature regime of Earth's lower mantle from first principles molecular dynamics coupled with thermodynamic integration. The calculations are based on Hf⁴⁺ entering the Mg-site, which we show is energetically preferable to the Si-site. We find that $D_{\text{Hf}}$ increases by more than an order of magnitude from 25 GPa to 140 GPa, making Hf much more compatible with increasing pressure. The larger $D_{\text{Hf}}$ at greater depths produces a strong fractionation of $^{182}$Hf between crystallized bridgmanite and silicate melt. We use a simple geochemical model to show that heterogeneous tungsten anomalies are a natural outcome of the formation and crystallization of a basal magma ocean, with the crystallized products enriched in $^{182}$W, while the remaining liquid is depleted by a similar amount. Our results show that the observed large variability of $^{182}$W/$^{184}$W in terrestrial samples may be due to the solidification of a basal magma ocean.

© 2021 Elsevier B.V. All rights reserved.

---

## 1. Introduction

The early Earth was once extensively molten due to the massive energy released during its early accretion and differentiation, leading to the formation of a magma ocean (Elkins-Tanton, 2012), which may have encompassed the entire mantle (Nakajima and Stevenson, 2015). As it crystallized, a basal magma ocean may have formed, due to a combination of crystal buoyancy at great depth (Ramo and Stixrude, 2014), and the initial crossing of the adiabat with the liquidus in the mid-mantle (Stixrude et al., 2009). The presence of a basal magma ocean may have fundamentally influenced Earth's thermochemical evolution (Labrosse et al., 2007): crystallized products may have formed dense piles that could account for the presence of large low shear wave velocity provinces (LLSVP) in the present Earth, while remaining liquid may account for ultra-low velocity zones (ULVZ), and the basal magma ocean may have produced Earth's earliest magnetic field (Ziegler and Stegman, 2013; Stixrude et al., 2020). Yet, many questions remain as to the depth, timing, and chemical fractionation of the magma ocean.

The trace element geochemistry of mantle-derived lavas may be able to constrain magma ocean processes. During crystallization of the basal magma ocean, many trace elements would have been partitioned between solid and liquid reservoirs, according to the partition coefficient ($D$) between silicate liquid and crystalline phases. Indeed, previous numerical models have argued that crystallization of the basal magma ocean can explain various isotopic signatures observed in ocean island basalts, including rare-Earth, and rare gas isotopic signatures (Labrosse et al., 2007; Coltice et al., 2011).

Short-lived radioactive isotopes are a particularly powerful means of constraining magma ocean processes, because cooling and crystallization were likely rapid in the very earliest stages of Earth's history. Here we examine the decay of $^{182}$Hf to $^{182}$W. This system has been widely used to study core formation because Hf is lithophile, while W is moderately siderophile (Jacobsen, 2005; Righter, 2011; Siebert et al., 2011; Wade et al., 2012). Measurements of meteorites show that the presumptive chondritic source has a large $^{182}$W deficit compared with the mantle ($\mu^{182}$W$=-200$). Because the half-life of $^{182}$Hf is short (8.9 Myr), these observations mean that core-formation must have occurred very early in Earth's history.

Recent studies have more closely examined the tungsten isotopic composition of terrestrial samples, finding variations that cannot be explained by core formation ($\mu^{182}$W$=-20$ to $+48$)

---

* Corresponding author.
E-mail address: jd848@g.ucla.edu (J. Deng).

https://doi.org/10.1016/j.epsl.2021.116873
0012-821X/© 2021 Elsevier B.V. All rights reserved.

![](./images/812486899028459521_4.jpg)

Fig. 1. Relaxed crystal structures of (a) MgSiO₃ bridgmanite and Hf-bearing bridgmanites with (b) ${\text{Hf}}_{\text{Mg}}^{\cdot \cdot }$, and (c) ${\text{Hf}}_{\text{Si}}^{\text{X}}$. The figure is made with VESTA (Momma and Izumi, 2011).

(Touboul et al., 2012; Willbold et al., 2015; Puchtel et al., 2016; Rizo et al., 2016; Mundl et al., 2017). The anomalies show an intriguing temporal pattern with Hadean to Archean samples typically characterized by positive anomalies and more recent ocean island basalts typically showing negative anomalies (Mei et al., 2019; Rizo et al., 2019). The origin of these anomalies is unknown. Processes that can produce negative anomalies include addition of a late veneer of chondritic material and entrainment of core material. Positive anomalies can be produced by silicate differentiation during the lifetime of ¹⁸²Hf (Touboul et al., 2012; Mei et al., 2019), or may reflect the ambient pre-late veneer mantle (Willbold et al., 2015). Uncertainties remain in part because the chemical and physical processes invoked (accretion, entrainment, silicate differentiation) are poorly constrained.

An important limitation to our understanding of tungsten isotopic anomalies is that the effect of silicate differentiation at the high pressure, high temperature conditions of a basal magma ocean is unknown. The partition coefficient of Hf between silicate melt and dominant mineral phases, including bridgmanite, have not been measured beyond 25 GPa (700 km depth), corresponding to the very top of the lower mantle (Corgne et al., 2005; Liebske et al., 2005).

Here, we study the partitioning of Hf in the deep mantle to better understand W isotopic heterogeneities. We predict the partition coefficient of Hf between silicate melt and bridgmanite over the entire pressure regime of the lower mantle (25-150 GPa). We first search for the most energetically favorable mechanism of incorporation Hf into MgSiO₃ bridgmanite, finding that Hf⁴⁺ preferentially enters the Mg-site. We then perform first-principles molecular dynamics (FPMD) simulations combined with the thermodynamic integration technique to investigate the partitioning of Hf between MgSiO₃ bridgmanite and silicate melt. We combine our predictions of partition coefficients with a simple model of basal magma ocean cooling and crystallization to explore the consequences of deep silicate fractionation for tungsten anomalies of the mantle.

### 2. Methodology

We study the partitioning of Hf between bridgmanite and silicate liquid and the resulting evolution of W isotopic composition. First, we investigate two plausible substitution mechanisms in bridgmanite: Hf⁴⁺ for Si⁴⁺ (${\text{Hf}}_{\text{Si}}^{\text{X}}$ in Kroger-Vink notation), and Hf⁴⁺ for Mg²⁺ (${\text{Hf}}_{\text{Mg}}^{\cdot \cdot }$) (Fig. 1). We then construct the Hf-bearing MgSiO₃ bridgmanite and silicate melt systems according to the most favorable substitution mechanism. First principles molecular dynamics simulations and thermodynamic integration are then performed on these systems to determine the partitioning of Hf between bridgmanite and silicate melt. Finally, we use our computed partition coefficient to model Hf partitioning and the evolution of W isotopic composition in a cooling basal magma ocean.

#### 2.1. Hf substitution mechanism

The computation of defect formation energies from density functional theory is a well-developed subject (Freysoldt et al., 2014), although there have been few applications to Earth materials (Verma and Karki, 2009a). The formation energy of a defect X of charge $q$ is

$$
\Delta G^{f}\left(X^{q}, P, T\right)=G\left(X^{q}, P, T\right)-G(0, P, T)-\sum_{i} n_{i} \mu_{i}+q \mu_{e}+E_{c}
\tag{1}
$$

where $G(X^q, P, T)$ is the Gibbs free energy of the system containing the defect at pressure $P$ and temperature $T$, $G(0, P, T)$ is the Gibbs free energy of the perfect crystal; $n_i$ is the number of atoms of type $i$ that have been added to ($n_i < 0$) or removed from ($n_i > 0$) the crystal to form the defect; $\mu_i$ are the corresponding chemical potentials; $\mu_e$ is the chemical potential of electrons; and $E_c$ is the energy correction due to the presence of periodic images of defects (Freysoldt et al., 2014). We use the finite size energy correction scheme of (Makov and Payne, 1995): $E_c = q^2\alpha/2\varepsilon L$ where $\alpha$ is the Madelung constant; $L$ is the size of the supercell; and $\varepsilon$ is the macroscopic dielectric constant of bridgmanite, including both the ionic and electronic contribution. We compute $\varepsilon$ self-consistently using density functional perturbation theory (Fig. S1) (Karki et al., 2000; Gajdoš et al., 2006). We also consider two other widely used correction schemes (Freysoldt et al., 2009) and (Lany and Zunger, 2009) and show that various correction schemes yield similar results (Fig. S2). For the case where Mg²⁺ is substituted by Hf⁴⁺, a uniform background charge of $-2$ is added to maintain global neutrality (Freysoldt et al., 2014).

The formation Gibbs free energies of ${\text{Hf}}_{\text{Si}}^{\text{X}}$ and ${\text{Hf}}_{\text{Mg}}^{\cdot \cdot }$ (Fig. 1) then read

$$
\begin{aligned}
\Delta G^{f}\left(\mathrm{Hf}_{\mathrm{Si}}^{\mathrm{X}}, P, T\right) & =G\left(\mathrm{Hf}_{\mathrm{Si}}^{\mathrm{X}}, P, T\right)-G(0, P, T) \\
& -\mu_{\mathrm{Hf}}^{\mathrm{bm}}(P, T)+\mu_{\mathrm{Si}}^{\mathrm{bm}}(P, T),
\end{aligned}
\tag{2}
$$

and

$$
\begin{aligned}
\Delta G^{f}\left(\mathrm{Hf}_{\mathrm{Mg}}^{\cdot \cdot}, P, T\right) & =G\left(\mathrm{Hf}_{\mathrm{Mg}}^{\cdot \cdot}, P, T\right)-G(0, P, T) \\
& -\mu_{\mathrm{Hf}}^{\mathrm{bm}}(P, T)+\mu_{\mathrm{Mg}}^{\mathrm{bm}}(P, T)+2 \mu_{e}+E_{c}
\end{aligned}
\tag{3}
$$


respectively, where $\mu_{i}^{\mathrm{j}}$ denotes the chemical potential of atom $i$ in phase $j$ and $j=$ bm refers to the bridgmanite phase.

We determinate the chemical potential of the electrons $(\mu_{e})$ and Hf $(\mu_{\mathrm{Hf}}^{\mathrm{bm}})$ by solving simultaneously the equations for charge neutrality and the specified concentration of impurities

$$
N_{e}=2 \sum_{i, \vec{k}} \frac{w_{\vec{k}}}{\exp \left(-\frac{\varepsilon_{i, \vec{k}}-\mu_{e}}{k_{B} T}\right)+1}+N_{s} c
\tag{4.1}
$$

$$
c=\exp \left(-\frac{\Delta G_{f}}{k_{B} T}\right)
\tag{4.2}
$$

where $c$ is the concentration of defects, $N_{e}$ is the number of valence electrons; $N_{s}$ is the number of sublattice sites of interest (i.e., Mg-site or Si-site); $\varepsilon_{i, \vec{k}}$ is the energy of $i$-th band at Brillouin zone point $\vec{k}$, and $k_{B}$ is the Boltzmann constant, and $w_{\vec{k}}$ is the weight of Brillouin zone point $\vec{k}$ (Zhang and Northrup, 1991; Verma and Karki, 2009b). Here we consider two representative values of $c$: 283 parts per billion (ppb) for the concentration of Hf in the bulk silicate earth (BSE) (McDonough and Sun, 1995) and 732 parts per million (ppm) for that used in experiments (Corgne et al., 2005; Liebske et al., 2005).

We determine the chemical potential of Mg by assuming that bridgmanite is in equilibrium with MgO periclase (pe) in the lower mantle, so that (Sundell et al., 2006), $\mu_{\mathrm{Mg}}^{\mathrm{bm}}=\mu_{\mathrm{Mg}}^{\mathrm{pe}}=\mu^{\mathrm{pe}}-\frac{1}{2} \mu_{\mathrm{O}_{2}}$ and $\mu_{\mathrm{Si}}^{\mathrm{bm}}=\mu_{\mathrm{Mg}}^{\mathrm{bm}}-\mu_{\mathrm{O}_{2}}^{\mathrm{bm}}-\frac{3}{2} \mu_{\mathrm{O}_{2}}$, yielding, for the difference in defect formation energies

$$
\begin{aligned}
\Delta G(P, T)= & \Delta G^{f}\left(\mathrm{Hf}_{\mathrm{Mg}}^{\cdot}, P, T\right)-\Delta G^{f}\left(\mathrm{Hf}_{\mathrm{Si}}^{\times}, P, T\right) \\
= & G\left(\mathrm{Hf}_{\mathrm{Mg}}^{\cdot}, P, T\right)-G\left(\mathrm{Hf}_{\mathrm{Si}}^{\times}, P, T\right)-\mu^{\mathrm{bm}}(P, T) \\
& +2 \mu^{\mathrm{pe}}(P, T)+\frac{1}{2} \mu_{\mathrm{O}_{2}}(P, T)+2 \mu_{e}+E_{c}
\tag{5}
\end{aligned}
$$

and $\mu_{\mathrm{O}_{2}}$ is the chemical potential of oxygen, which is expressed as (Freysoldt et al., 2014)

$$
\mu_{\mathrm{O}_{2}}(P, T)=E\left(\mathrm{O}_{2}\right)+G(1 \mathrm{bar}, T)+R T \ln f_{\mathrm{O}_{2}}(P, T)
\tag{6}
$$

where $E\left(\mathrm{O}_{2}\right)$ is the binding energy of the oxygen molecule (Schimka et al., 2011), $G$ is the Gibbs free energy including vibrational, rotational, and translational contributions, and $f_{\mathrm{O}_{2}}$ is the oxygen fugacity of the IW buffer taken from (Campbell et al., 2009). The Gibbs free energies of the solid phases are calculated by

$$
G(P, T)=H_{D F T}(P, \text { static })+\left[G_{H}(P, T)-H_{H}(P, \text { static })\right]
\tag{7}
$$

where $H_{D F T}(P$, static) is computed via density functional theory and the thermal correction in square brackets is computed with HeFESTo (Stixrude and Lithgow-Bertelloni, 2011).

### 2.2. Hf crystal-liquid partitioning

We determine the Gibbs free energy of the reaction

$$
\begin{array}{cccc}
\mathrm{MgSiO}_{3}: \mathrm{Hf}+ & \mathrm{MgSiO}_{3} & =\mathrm{MgSiO}_{3}: \mathrm{Hf}+\mathrm{MgSiO}_{3} \\
\text { melt } & \text { bridgmanite } & \text { bridgmanite } & \text { melt }
\end{array}
\tag{8}
$$

As we are interested in the dilute limit, the Gibbs free energy of the reaction $\Delta G_{R}$ yields the distribution coefficient, $K_{\mathrm{D}}$, and the partition coefficient $D_{\mathrm{Hf}}$,

$$
D_{\mathrm{Hf}}=\frac{X_{\mathrm{Hf}}^{\mathrm{bm}}}{X_{\mathrm{Hf}}^{\text {melt }}} \cong \frac{X_{\mathrm{Hf}}^{\mathrm{bm}}\left(1-X_{\mathrm{Hf}}^{\mathrm{bm}}\right)}{X_{\mathrm{Hf}}^{\text {melt }}\left(1-X_{\mathrm{Hf}}^{\text {melt }}\right)}=K_{\mathrm{D}}=\exp \left(-\Delta G_{R} / k_{B} T\right), \quad(9)
$$

where $X_{i}^{j}$ is the molar concentration of species $i$ in phase $j$.

The Gibbs free energy of reaction (8) may be expressed as,

$$
\begin{aligned}
\Delta G_{R} & =\Delta G^{\text {melt }}-\Delta G^{\mathrm{bm}} \\
& =G_{\mathrm{MgSiO}_{3}}^{\text {melt }}-G_{\mathrm{MgSiO}_{3}: \mathrm{Hf}}^{\text {melt }}-\left(G_{\mathrm{MgSiO}_{3}}^{\mathrm{bm}}-G_{\mathrm{MgSiO}_{3}: \mathrm{Hf}}^{\mathrm{bm}}\right),
\end{aligned}
\tag{10}
$$

and $\Delta G^{\mathrm{bm}}$ and $\Delta G^{\text {melt }}$ can be further related to the differences of Helmholtz free energy (Sola and Alfe, 2009),

$$
\Delta G^{\text {melt } / \mathrm{bm}} \cong \Delta F^{\text {melt } / \mathrm{bm}}-V \Delta P^{2} / 2 K_{T}
\tag{11}
$$

where $\Delta P$ is the pressure difference between the doped and undoped system; $V$ is the volume, and $K_{T}$ is the isothermal bulk modulus of bridgmanite (Stixrude and Lithgow-Bertelloni, 2005).

We calculated $\Delta F^{\text {melt/bm }}$ using FPMD simulations combined with the thermodynamic integration method. The Helmholtz free energy difference $\Delta F$ is the reversible work done on adiabatically switching the total energy function from that of the pure $\mathrm{MgSiO}_{3}$ system (denoted as $U_{0}$ ) to the Hf-bearing system (denoted as $U_{1}$ ), which is given by

$$
\Delta F=\int_{0}^{1}\left\langle U_{1}-U_{0}\right\rangle_{\lambda} \mathrm{d} \lambda=\int_{0}^{1}\langle\Delta U\rangle_{\lambda} \mathrm{d} \lambda,
\tag{12}
$$

where $\langle\Delta U\rangle_{\lambda}$ represents an ensemble average of $\Delta U$ and $\lambda$ is a parameter connecting the Hf bearing and Hf free system with $U_{\lambda}=(1-\lambda) U_{0}+\lambda U_{1}$. More specifically, when performing the thermodynamic integration for the solid system, $U_{0}$ refers to $\mathrm{MgSiO}_{3}$ bridgmanite and $U_{1}$ Hf-bearing $\mathrm{MgSiO}_{3}$ solid; while for the liquid system, $U_{0}$ refers to $\mathrm{MgSiO}_{3}$ melt and $U_{1}$ Hf-bearing $\mathrm{MgSiO}_{3}$ melt.

In order to integrate over $\langle\Delta U\rangle_{\lambda}$, we examine two methods. In method 1, we consider $\langle\Delta U\rangle_{\lambda}$ to be a linear function of $\lambda$ and $\Delta F=\left(\langle\Delta U\rangle_{\lambda=0}+\langle\Delta U\rangle_{\lambda=1}\right) / 2$. In method 2, we express $\langle\Delta U\rangle_{\lambda}$ as a polynomial $\langle\Delta U\rangle_{\lambda}=a+b \lambda+c \lambda^{2}+d \lambda^{3}$, with coefficients set by the computed values of $\langle\Delta U\rangle_{\lambda=0}$ and $\langle\Delta U\rangle_{\lambda=1}$, and the derivatives of $\langle\Delta U\rangle_{\lambda}$ with respect to $\lambda$ at the two endpoints, which are related to the fluctuations in $\langle\Delta U\rangle_{\lambda}$ by (Frenkel and Smit, 2002)

$$
\left(\frac{\partial\langle\Delta U\rangle_{\lambda}}{\partial \lambda}\right)_{N, V, T}=-\frac{1}{k_{B} T}\left[\left\langle\Delta U^{2}\right\rangle-\langle\Delta U\rangle^{2}\right]
\tag{13}
$$

We compared the linear and cubic methods for both liquid and solid systems. These two methods yield very similar results for both systems and the difference in partitioning coefficients is within uncertainty. (Table 1, Fig. S3). This is consistent with the analysis of (Sola and Alfè, 2009) that if the fluctuations of $\langle\Delta U\rangle_{\lambda}$ are small compared with $\langle\Delta U\rangle_{\lambda}$, the free energy can be reliably evaluated with $\langle\Delta U\rangle_{\lambda}$ at two endpoints only. In this study, the reference system (pure $\mathrm{MgSiO}_{3}$ system) and the target system (Hf-bearing $\mathrm{MgSiO}_{3}$ system) is similar and the fluctuation of $\langle\Delta U\rangle_{\lambda}$ at these two points are almost identical (Fig S3). As a result, $\langle\Delta U\rangle_{\lambda}$ at $\lambda=0$ and 1 are sufficient to derive the free energy.

### 2.3. Computation

Our system consists of $32 \mathrm{MgSiO}_{3}$ units, with or without a single Hf substituent for both solid and melt phases. The simulations are based on density functional theory in the PBEsol approximation (Perdew et al., 2008). We use the projector augmented wave (PAW) method (Kresse and Joubert, 1999) as implemented in VASP (Kresse and Furthmüller, 1996). The core radii are O: $0.820 \AA$ $\left(2 s^{2} 2 p^{4}\right)$, Si: $1.312 \AA\left(3 s^{2} 3 p^{2}\right)$, Mg: $1.058 \AA\left(2 p^{6} 3 s^{2}\right)$, Hf: $1.614 \AA$ $\left(5 s^{2} 5 p^{6} 6 s^{2} 5 d^{2}\right)$. Sampling the Brillouin zone at the Gamma point and a basis-set energy cutoff of 500 eV were found to be sufficient to converge the total energy and pressure to within 4 meV/atom and 0.2 GPa, respectively.


Born-Oppenhiemer molecular dynamics calculations are performed in the canonical ensemble using the Nose-Hoover thermostat (Hoover, 1985) and run for 5-20 ps with 1 fs time step. We assume thermal equilibrium between ions and electrons via the Mermin functional (Mermin, 1965). For crystalline molecular dynamics simulations, we ensure that the stress is hydrostatic by adjusting the lattice parameters while maintaining a constant volume. The resulting cell shapes are given in Table S1 and are in excellent agreement with (Zhang et al., 2013). For liquid phase molecular dynamics simulations, following our previous work (Deng et al., 2020), we first melt the crystalline structure uniformly strained to a cubic supercell shape at 10,000 K, and then cool to the temperature of interest. For static calculations, we relax all atomic positions and lattice parameters while keeping the pressure fixed.

### 2.4. Tungsten anomaly of a crystallizing basal magma ocean

We apply our calculated Hf partition coefficients to model the time evolution of tungsten anomalies expressed as ppm deviations of the isotopic ratio from a standard

$$
\mu^{182} \mathrm{~W}=\left[\left({ }^{182} \mathrm{~W} /{ }^{184} \mathrm{~W}\right) /\left({ }^{182} \mathrm{~W} /{ }^{184} \mathrm{~W}\right)_{\text {std }}-1\right] \times 10^{6} \tag{14}
$$

We consider an initial basal magma ocean of thickness $h_{\mathrm{i}}$ formed by batch melting of the mantle with melt fraction $F$ at time $t_{\mathrm{i}}$ after the formation of CAIs. The basal magma ocean then cools and fractionally crystallizes with a timescale $\tau$. We assume that solid and liquid reservoirs are well-mixed. We adopt the values $h_{\mathrm{i}}=850 \mathrm{~km}, F=0.8, \tau=887 \mathrm{Myr}$, and $t_{\mathrm{i}}=50 \mathrm{Myr}$, identical to those assumed by (Labrosse et al., 2007). Partitioning of elements is constrained by our computed value of $D_{\mathrm{Hf}}$. We assume a value $D_{\mathrm{W}} / D_{\mathrm{Hf}}=0.43$, consistent with experimentally based lattice strain models (Corgne et al., 2005; Liebske et al., 2005), and our estimate of the ionic radius of $\mathrm{W}^{4+}(0.77 \AA)$ (Shannon, 1976) (Fig. S4). We consider the effect of other values of $D_{\mathrm{W}} / D_{\mathrm{Hf}}, F$, and $t_{\mathrm{i}}$ in the supplementary information, which also contains further details of our geochemical model.

## 3. Results

### 3.1. Substitution mechanism

The $\mathrm{Hf}_{\mathrm{Mg}}^{\cdot}$ substitution is more energetically favorable than the $\mathrm{Hf}_{\mathrm{Si}}^{\times}$substitution throughout the pressure regime of the lower mantle, and is increasingly favored with increasing pressure (Fig. 2). With the BSE Hf concentration, the difference of the defect formation energies becomes positive at pressures lower than $\sim 20$ GPa and is negative at higher pressures. When the Hf concentration is close to that present in high-pressure experiments (Corgne et al., 2005; Liebske et al., 2005), $\mathrm{Hf}_{\mathrm{Mg}}^{\cdot}$ is even more favored. Based on these results, we compute $D_{\mathrm{Hf}}$ assuming the $\mathrm{Hf}_{\mathrm{Mg}}^{\cdot}$ substitution mechanism.

![](./images/812486899028459521_5.jpg)

Fig. 2. Differences of the formation energies of $\mathrm{Hf}_{\mathrm{Mg}}^{\cdot}$ and $\mathrm{Hf}_{\mathrm{Si}}^{\times}$in $\mathrm{MgSiO}_{3}$ bridgmanite at $2000 \mathrm{~K} \Delta G=\Delta G^{f}\left(\mathrm{Hf}_{\mathrm{Mg}}^{\cdot}, P, T\right)-\Delta G^{f}\left(\mathrm{Hf}_{\mathrm{Si}}^{\times}, P, T\right)$. Energy differences are for $32 \mathrm{MgSiO}_{3}$ with a single substitution. Both the Gibbs free energies differences, $\Delta G$ (triangles) and enthalpy differences $(\Delta H)$ (circles) are shown, where the latter are computed by neglecting the thermal correction for the solid phases in Eq. (7) so that $G(P, T)=H_{D F T}(P$, static). The solid symbols and solid lines correspond to $c=283 \mathrm{ppb}$, and the empty symbols and dashed lines correspond to $c=732 \mathrm{ppm}$. The errors of formation enthalpies derived from difference in finite size energy correction schemes are also included (see Fig. S2 for more discussion).

### 3.2. Hf partitioning

We find that $D_{\mathrm{Hf}}$ increases substantially with increasing pressure over the lower mantle regime, while increasing temperature diminishes $D_{\mathrm{Hf}}$ (Fig. 3; Table 1). Our results at $3000 \mathrm{~K}$ agree well with experimental results at $\sim 25 \mathrm{GPa}$ and $2600 \mathrm{~K}$ within uncertainty (Corgne et al., 2005; Liebske et al., 2005).

We fit our results to Eq. (9) with

$$
\Delta G_{R}=\Delta E_{R}+P \Delta V_{R}-T \Delta S_{R} \tag{15}
$$

where $\Delta E_{R}, \Delta V_{R}$, and $\Delta S_{R}$ are the internal energy change, the volume change, and entropy change of the substitution reaction. We find best fitting values $\Delta E_{R}=-2.4 \pm 1.3 \times 10^{4} \mathrm{~J} / \mathrm{mol}, \Delta V_{R}=$ $-0.70 \pm 0.06 \mathrm{~cm}^{3} / \mathrm{mol}$, and $\Delta S_{R}=-4.6 \pm 3.8 \mathrm{~J} / \mathrm{K} / \mathrm{mol}$.

![](./images/812486899028459521_6.jpg)

Fig. 3. Partition coefficient of $\mathrm{Hf}, D_{\mathrm{Hf}}$ between $\mathrm{MgSiO}_{3}$ bridgmanite and $\mathrm{MgSiO}_{3}$ melt at $3000 \mathrm{~K}$ (blue circle), $4000 \mathrm{~K}$ (green upward triangle), and $5000 \mathrm{~K}$ (red downward triangle). The big solid symbols represent $D_{\mathrm{Hf}}$ calculated with thermodynamic integration method; the small black and white symbols represent $D_{\mathrm{Hf}}$ calculated with the lattice strain model (Eqs. (16), (17)) using bonded radii and Shannon radii, respectively. The three colored curves are the least squares fit to the thermodynamic integration results using Eqs. (9) and (15). The results of the experimental studies are also shown for comparison (Corgne et al., 2005; Liebske et al., 2005). (For interpretation of the colors in the figure(s), the reader is referred to the web version of this article.)

### 3.3. Lattice strain model

We use our $a b$ initio values of $D_{\mathrm{Hf}}$ to evaluate the lattice strain model: a semi-empirical model that has been widely used to rationalize trends in trace element partitioning. The comparison also yields additional insight into the origin of the pressure dependence of $D_{\mathrm{Hf}}$ that we find from our $a b$ initio results. According to the lattice strain model (Brice, 1975; Blundy and Wood, 1994)

$$
D_{\mathrm{Hf}}=D_{0} \exp \left[-\frac{\left(\Delta u_{s}-\Delta u_{l}\right)}{R T}\right] \tag{16}
$$

where $\Delta u_{s}$ and $\Delta u_{l}$ are the strain energies caused by incorporating the trace element into the solid and liquid respectively, and $D_{0}$

<table><caption>Table 1
Results of thermodynamic integration using linear and cubic integration methods including the partition coefficient $D_{Hf}$, and the Gibbs free energy difference $\Delta G_{R}$. Also shown are time-averaged values of $U_0$ (MgSiO₃) and $U_1$ (MgSiO₃:Hf) for each phase along the undoped trajectory $\lambda = 0$.</caption>
<tbody>
<tr>
<td>T
(K)</td>
<td>P
(GPa)</td>
<td colspan="4">$\langle U\rangle_\lambda$
(eV)</td>
<td colspan="3">$\Delta G_{R}$
(eV)</td>
<td colspan="3">$\log_{10}D_{Hf}$</td>
</tr>
<tr>
<td></td>
<td></td>
<td colspan="2">Solid</td>
<td colspan="2">Liquid</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>MgSiO₃</td>
<td>MgSiO₃:Hf</td>
<td>MgSiO₃</td>
<td>MgSiO₃:Hf</td>
<td>Linear</td>
<td>Cubic</td>
<td>$1\sigma$</td>
<td>Linear</td>
<td>Cubic</td>
<td>$1\sigma$</td>
</tr>
<tr>
<td>3000</td>
<td>31</td>
<td>−26.91</td>
<td>−31.28</td>
<td>−27.53</td>
<td>−31.33</td>
<td>0.33</td>
<td>0.42</td>
<td>0.11</td>
<td>0.56</td>
<td>0.71</td>
<td>0.19</td>
</tr>
<tr>
<td>3000</td>
<td>50</td>
<td>−28.04</td>
<td>−32.64</td>
<td>−28.85</td>
<td>−32.74</td>
<td>0.45</td>
<td>0.62</td>
<td>0.16</td>
<td>0.76</td>
<td>1.05</td>
<td>0.28</td>
</tr>
<tr>
<td>3000</td>
<td>93</td>
<td>−29.50</td>
<td>−33.76</td>
<td>−29.17</td>
<td>−35.77</td>
<td>0.84</td>
<td>0.84</td>
<td>0.16</td>
<td>1.41</td>
<td>1.41</td>
<td>0.27</td>
</tr>
<tr>
<td>3000</td>
<td>129</td>
<td>−29.94</td>
<td>−34.55</td>
<td>−30.03</td>
<td>−36.86</td>
<td>1.20</td>
<td>1.33</td>
<td>0.17</td>
<td>2.01</td>
<td>2.24</td>
<td>0.28</td>
</tr>
<tr>
<td>4000</td>
<td>31</td>
<td>−26.51</td>
<td>−30.59</td>
<td>−26.27</td>
<td>−31.47</td>
<td>0.32</td>
<td>0.55</td>
<td>0.20</td>
<td>0.40</td>
<td>0.69</td>
<td>0.26</td>
</tr>
<tr>
<td>4000</td>
<td>58</td>
<td>−27.72</td>
<td>−32.05</td>
<td>−27.41</td>
<td>−33.38</td>
<td>0.51</td>
<td>0.51</td>
<td>0.30</td>
<td>0.64</td>
<td>0.64</td>
<td>0.38</td>
</tr>
<tr>
<td>4000</td>
<td>101</td>
<td>−28.93</td>
<td>−33.70</td>
<td>−29.36</td>
<td>−35.08</td>
<td>0.90</td>
<td>1.01</td>
<td>0.20</td>
<td>1.14</td>
<td>1.27</td>
<td>0.25</td>
</tr>
<tr>
<td>4000</td>
<td>140</td>
<td>−29.75</td>
<td>−34.68</td>
<td>−29.52</td>
<td>−36.83</td>
<td>0.96</td>
<td>1.15</td>
<td>0.20</td>
<td>1.21</td>
<td>1.44</td>
<td>0.25</td>
</tr>
<tr>
<td>5000</td>
<td>66</td>
<td>−27.52</td>
<td>−32.06</td>
<td>−27.98</td>
<td>−32.53</td>
<td>0.47</td>
<td>0.55</td>
<td>0.22</td>
<td>0.47</td>
<td>0.55</td>
<td>0.22</td>
</tr>
<tr>
<td>5000</td>
<td>109</td>
<td>−28.68</td>
<td>−33.38</td>
<td>−29.05</td>
<td>−34.84</td>
<td>0.92</td>
<td>1.11</td>
<td>0.27</td>
<td>0.92</td>
<td>1.12</td>
<td>0.28</td>
</tr>
<tr>
<td>5000</td>
<td>144</td>
<td>−29.08</td>
<td>−34.04</td>
<td>−29.23</td>
<td>−36.27</td>
<td>1.19</td>
<td>1.35</td>
<td>0.24</td>
<td>1.20</td>
<td>1.36</td>
<td>0.24</td>
</tr>
</tbody>
</table>

![](./images/812486899028459521_7.jpg)

Fig. 4. Difference of the Hf-O and Mg-O bondlengths in Hf-bearing bridgmanite (solid symbols) and melt (open symbols) at 3000 K (blue circle), 4000 K (green upward triangle), and 5000 K (red downward triangle).

is the reference partition coefficient corresponding to a fictive ion of the same charge and radius $r_0$ which enters the lattice without strain (i.e., $\Delta u=0$). Here we adopt the most recent formulation of $\Delta u$ (Karato, 2016),

$$
\begin{aligned}
\Delta u= & 6 \pi r_{\mathrm{Mg}}^{3} \frac{K_{\mathrm{Hf}}^{2}}{K_{\mathrm{Hf}}+\frac{4}{3} G_{0}}\left(\frac{d_{\mathrm{Hf}}-d_{\mathrm{Mg}}}{r_{\mathrm{Mg}}}\right)^{2} \\
& \times\left[1+\frac{K_{\mathrm{Hf}}}{K_{\mathrm{Hf}}+\frac{4}{3} G_{0}}\left(\frac{d_{\mathrm{Hf}}-d_{\mathrm{Mg}}}{r_{\mathrm{Mg}}}\right)\right],
\end{aligned}
\tag{17}
$$

where the $K_{\mathrm{Hf}}$ and $G_0$ are the bulk modulus of Hf and the shear modulus of the MgSiO₃ matrix respectively; $r_X$ and $d_X$ are the radius of cation X and the corresponding X-O bondlength, respectively. We approximate $K_{\mathrm{Hf}}=0.15 Z / d_{\mathrm{Hf}}^{4}$ where $Z$ is the ionic charge (Karato, 2016). $G_0$ of MgSiO₃ bridgmanite is calculated using the equation of state presented by (Stixrude and Lithgow-Bertelloni, 2005) and we assume $G_0=0$ for the liquid phase. We determine the bondlength $d_X$ as the position of the first peak of the radial distribution function from our FPMD simulations (Figs. 4 and S5). Unlike bond-lengths, the ionic radius $r_X$ is not a well-defined quantity and in order to apply the lattice strain model, we require an estimate of $r_{Mg}$. We consider two different estimates for $r_{Mg}$: 1) the ionic radii reported by (Shannon, 1976), which have been widely used in applications of the lattice strain model (Corgne et al., 2005; Liebske et al., 2005) and 2) the bonded radii derived from our ab initio electron density via Bader analysis (Tang et al., 2009) (Fig. S6). We set the value of $D_0$ such that the lattice strain model matches our FPMD result for $D_{\text {Hf }}$ at 3000 K and 30 GPa for both cases.

With increasing pressure, $d_{\text {Hf }}-d_{\text {Mg }}$ diminishes for bridgmanite while increasing for the liquid phase (Fig. 4), indicating increasing compatibility of Hf in bridgmanite with increasing pressure, and consistent with our finding the $D_{\text {Hf }}$ increases with increasing pressure (Fig. 3). For both Shannon radii and bonded radii, the lattice strain model is in excellent quantitative agreement with our ab initio value of $D_{\text {Hf }}$ (Fig. 3).

### 3.4. Evolution of W isotopic anomaly

We find that $\mu^{182} \mathrm{~W}$ of liquid and solid reservoirs grow rapidly to $-14$ and $+18$, respectively within several tens of millions of years (Fig. 5a and Fig. S7, S8). This rapid rise occurs when $^{182} \mathrm{Hf}$ is still alive and the decay of $^{182} \mathrm{Hf}$ to $^{182} \mathrm{~W}$ supplements all reservoirs with $^{182} \mathrm{~W}$. As Hf is more compatible than W, more $^{182} \mathrm{Hf}$ stays in the solid reservoir, leading to a positive value $\mu^{182} \mathrm{~W}$ that reaches a maximum value near 50 Myr. The anomaly of the solid reservoir then drops gradually towards the modern mantle value of 0 as magma ocean crystallization proceeds. Note that the $\mu^{182} \mathrm{~W}$ of the solid reservoir remains a positive value $(\sim 0.0002)$ even at present-day and should remain positive until the basal magma ocean is completely recycled back. Concurrently, the $\mu^{182} \mathrm{~W}$ of the liquid reservoir reaches $-14$ and then essentially does not vary anymore. This is because $^{182} \mathrm{Hf}$ dies out and subsequent elemental partitioning does not change the isotopic signature, in the liquid reservoir.

The effect of pressure on isotopic fractionation is shown in Fig. 5b. The larger value of $D_{\text {Hf }}$ that we find at high pressure leads to isotopic anomalies of similar magnitude but opposite sign in solid and liquid reservoirs. In contrast, $D_{\text {Hf }} \sim 1$, as indicated by lower pressure experiments, produces significantly smaller liquid reservoir anomalies and larger solid reservoir anomalies. The timing of basal magma ocean formation also influences the isotopic anomalies, with earlier formation leading to larger isotopic anomalies.

### 4. Discussion

By comparing the formation energies of $\mathrm{Hf}_{\mathrm{Mg}}^{\ddot{*}}$ and $\mathrm{Hf}_{\mathrm{Si}}^{\times}$, we find that Hf prefers to enter the Mg-site throughout the lower mantle. This result can be understood on the basis of cation radii. MgSiO₃ bridgmanite has two cation sites, a large distorted site occupied by 8-12-fold coordinated $\mathrm{Mg}^{2+}$ and a smaller site occupied by 6-fold coordinated $\mathrm{Si}^{4+}$. The effective ionic radius of $\mathrm{Mg}^{2+}$ is more than two times of that of $\mathrm{Si}^{4+}$ (Shannon, 1976), while the radii of $\mathrm{Mg}^{2+}$

![](./images/812486899028459521_8.jpg)

Fig. 5. (a) Evolution of $\mu^{182}\text{W}$ for the liquid (red dashed curve) and solid (blue dotted curve) reservoirs for the value that we find for $D_{\text{Hf}}=4.9$ and other parameters given in the text. For comparison, we also show $\mu^{182}\text{W}$ of the portion of the mantle that does not participate in basal magma ocean formation or crystallization (standard, black solid curve). The blue and red shaded bars represent the average $\mu^{182}\text{W}$ with $2\sigma$ uncertainties for Hadean-Archean, and OIB samples, respectively (Rizo et al., 2019). (b) The present-day $\mu^{182}\text{W}$ of the liquid reservoir (red dashed contour) and the maximum $\mu^{182}\text{W}$ of the solid reservoir (blue dotted contour) as a function of $t_{\text{i}}$ and $D_{\text{Hf}}$. The vertical green bar represents the $D_{\text{Hf}}$ calculated in this study at conditions relevant to the formation of the basal magma ocean.

and $\text{Hf}^{4+}$ are similar. The significant size mismatch between the Si-site and $\text{Hf}^{4+}$ disfavors the substitution in this site, and makes the $\text{Hf}_{\text{Si}}^{\times}$ substitution increasingly unfavorable with increasing pressure. The favorability of the Mg-site increases with Hf concentration as the higher Hf concentration lowers the chemical potential of electrons and thus the defect formation energy. In our calculations of $\Delta G$, we have assumed an Mg rich environment, but recognized that some portions of the mantle may be silica saturated, rather than magnesia saturated, such as in regions of subducted oceanic crust (Stixrude and Lithgow-Bertelloni, 2012). In such enriched regions the $\text{Hf}_{\text{Mg}}^{\cdot}$ substitution mechanism will be even more favored, since an Mg-rich environment tends to disfavor the creation of Mg vacancies. Our findings are consistent with the experimental inference based on Onuma diagrams (Onuma et al., 1968) that at 25 GPa, tetravalent cations larger than $\text{Ge}^{4+}$, such as $\text{Hf}^{4+}$, $\text{Zr}^{4+}$, $\text{U}^{4+}$, and $\text{Th}^{4+}$ substitute exclusively onto the Mg-site (Liebske et al., 2005). We note that our calculated formation energy of $\text{Hf}_{\text{Mg}}^{\cdot}$ does not require us to assume a specific charge-balancing mechanism. In our calculations, the extra charge of $\text{Hf}^{4+}$ is balanced by a uniform background, which may correspond to charge balancing cation vacancies or heterovalent substitution (e.g., Al for Si) (Liebske et al., 2005).

We find that the partition coefficient of Hf between $\text{MgSiO}_{3}$ bridgmanite and silicate melt increases by a large amount with increasing pressure: by a factor of 12 on the 4000 K isotherm over the pressure ragne of the lower mantle (25-140 GPa). With increasing pressure, the size mismatch of Mg-O and Hf-O bondlengths diminishes in the solid while increasing in the liquid. The smaller size mismatch in the solid phase induces smaller strain energy compared with that in liquid phase, making Hf increasingly compatible with increasing pressure (Fig. 3). We recognize that other mantle crystalline phases may also influence Hf partitioning, such as $\text{CaSiO}_{3}$ perovskite. Available experiments at 25 GPa show that the partition coefficient of Hf between liquid and $\text{CaSiO}_{3}$ perovskite is approximately equal to that between liquid and $\text{MgSiO}_{3}$ bridgmanite (Corgne et al., 2005). Although $\text{CaSiO}_{3}$ perovskite is the major host for rare earth elements (REEs) and other large-ion lithophile elements (such as $\text{U}^{4+}$) (Corgne and Wood, 2002; Perry et al., 2017). $\text{Hf}^{4+}$ partitions differently from these large ions as its ionic radius (85 Å) is not as large as that of $\text{Ca}^{2+}$ (100 Å), but instead is close to that of $\text{Mg}^{2+}$ (86 Å) (Shannon, 1976). As $\text{MgSiO}_{3}$ bridgmanite is the dominant phase in the mantle, and Hf is similarly compatible in bridgmanite and $\text{CaSiO}_{3}$ perovskite, bridgmanite plays a more important role in redistributing Hf than $\text{CaSiO}_{3}$ perovskite in the crystallizing magma ocean.

Crystallization of the basal magma ocean is able to reproduce key features of tungsten anomalies found in the geologic record. Silicate differentiation produces both positive and negative anomalies that are similar to each other in magnitude, as observed (Rizo et al., 2019). Moreover, the signature of basal magma ocean crystallization is time dependent in a way that is mirrored by the geologic record. The $\mu^{182}\text{W}$ of the solid reservoir, vanishes during the Archean, in qualitative agreement with the general trend that most positive $\mu^{182}\text{W}$ occur in the Archean (Rizo et al., 2016; Mundl et al., 2017; Mei et al., 2019). We speculate that Archean magmatic source material entrained portions of the solid reservoir and that this is the origin of the positive $\mu^{182}\text{W}$ of Hadean-Archean rocks. We note that we have assumed perfect homogenization of the solid reservoir. This may not be realistic, and regions of large positive anomaly may survive throughout the Archean. The negative $\mu^{182}\text{W}$ of the liquid reservoir is independent of time throughout the Archean to the present day. Once the positive anomaly of the solid reservoir has died away, we speculate that the negative anomaly of the entrained liquid reservoir dominates the tungsten isotopic signature of more recent lavas.

Silicate fractionation explains another important feature of geochemical observations. The geologic record shows no strong correlation between negative tungsten anomalies and highly siderophile element (HSE) concentrations (Rizo et al., 2019). Such a correlation would be expected if core entrainment or a late veneer were responsible for negative $\mu^{182}\text{W}$, contrary to observations. However, if silicate fractionation is responsible for negative $\mu^{182}\text{W}$, then no correlation with HSE would result, as observed.

Silicate fractionation has been dismissed as an explanation of observed tungsten anomalies because they are not correlated with $^{142}\text{Nd}$ isotopic anomalies (Rizo et al., 2019). Based on low pressure partition coefficients of Sm and Nd, a strong correlation is expected. However, the partition coefficients of Sm and Nd have recently been found to depend strongly on pressure (Tateno et al., 2018). The partition coefficients of these two elements become much more similar at high pressure - identical within uncertainty at the highest pressures measured - and much closer to unity. The crystalline phase examined in these experiments is $\text{CaSiO}_{3}$ rather than $\text{MgSiO}_{3}$ perovskite and the maximum pressure of the experiments is 70 GPa, short of the conditions of the basal magma ocean, emphasizing the importance of further experimental measurements. With these caveats, it seems possible that deep silicate crystallization may not produce significant $^{142}\text{Nd}$ anomalies, explaining the lack of correlation with tungsten isotopic anomalies. Jackson et al. (2014) argued on the basis of low pressure

(<25 GPa) partition coefficients that bridgmanite crystallization decouples $^{143}$Nd and $^{176}$Hf anomalies because $D_{Lu}<D_{Hf}$, while $D_{Nd}<D_{Sm}$, a conclusion nominally unaffected by our results since we find $D_{Hf}$ at high pressure to be even larger than it is at 25 GPa. Caution however is warranted: $D_{Lu}$ is also likely to depend on pressure and it is currently unknown beyond 25 GPa; it may depend more or less strongly on pressure than $D_{Hf}$. Further analysis of the effect of basal magma ocean crystallization on systems other than Hf/W at this time seems unwarranted because the effect of pressure on the partitioning of most elements is unknown beyond 25 GPa. Our results and those of (Tateno et al., 2018) highlight the importance of understanding the effect of pressure on the partition coefficients of not only Hf/W, Sm/Nd, and Lu/Hf but other geochemical tracers as well, including other REE, other trace elements, and noble gases. Analyses of the effect of a basal magma ocean on chemical signatures of the mantle, which to date have been based on partition coefficients measured at 25 GPa (Walter et al., 2004; Labrosse et al., 2007; Coltice et al., 2011; Jackson et al., 2014), should be revisited as we gain knowledge of element partitioning at higher pressure.

The magnitudes of the tungsten anomalies of the solid and liquid reservoirs are sensitive to various aspects of magma ocean formation and crystallization processes, including the initial size of the basal magma ocean, the degree of batch melting, the timescale of crystallization, and mixing efficiency of different reservoirs. This sensitivity raises the possibility that W and other isotopic anomalies may be used to further constrain magma ocean processes. For example, with $t_i=25$ Myr instead of our fiducial 50 Myr, $\mu^{182}$W are an order of magnitude larger in solid and liquid reservoirs, which means that only a small amount of entrainment of these reservoirs into the magmatic source region could explain observed anomalies. Indeed, with $t_i=25$ Myr, the $\mu^{182}$W anomaly of the liquid reservoir ($-100$) is comparable in magnitude to that estimated for the core ($-200$). We have not attempted to model quantitatively the process by which the solid and liquid reservoirs are entrained into the magmatic source. Entrainment likely depends on the density and viscosity contrast between these reservoirs and the ambient mantle, emphasizing the importance of geodynamical modeling of the process of entrainment, and of better seismological constraints on the density contrasts of LLSVP and ULVZ with surrounding mantle. Our model can place some constraints on the age of material entrained from the basal magma ocean. This material, with negative W anomaly, must be ancient because the basal magma ocean becomes depleted in W with time, since W is compatible. We find that the W concentration in the basal magma ocean exceeds that of the upper mantle (Arevalo and McDonough, 2008) for one billion years (Fig. S9).

## 5. Conclusion

We have determined the partition coefficient of Hf between bridgmanite and silicate melt from first principles. Our results agree well with experimental data at low pressure (25 GPa), and extend our knowledge of the partitioning of this element throughout the mantle pressure regime. The partition coefficient increases strongly with increasing pressure, by more than a factor of 10 on the 4000 K isotherm, so that Hf is much more compatible in the basal magma ocean than at lower pressure conditions. These trends are captured by simple arguments based ionic radii, bond lengths, and models of lattice strain.

The large value of $D_{Hf}$ at high pressure means that deep fractionation of silicates and melt during the lifetime of $^{182}$Hf can generate reservoirs with significantly different tungsten anomalies. The crystalline residue of basal magma ocean crystallization is enriched in $^{182}$W, while the remaining liquid is depleted. The magnitude of the anomalies show that silicate differentiation must be considered in future models of the origin of tungsten isotopic anomalies. Moreover, silicate differentiation can produce many features of the geologic record of $\mu^{182}$W, including the similar magnitudes of positive and negative anomalies, the scarcity of positive anomalies post-Archean, and the lack of correlation with HSE concentrations.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This project is supported by the National Science Foundation (EAR-1853388). This work used computational and storage services associated with the Hoffman2 Shared Cluster provided by UCLA Institute for Digital Research and Education's Research Technology Group. Part of the computation was performed at the Yale Center for Research Computing (thanks to Kaylea Nelson for guidance). We are grateful to the two anonymous reviewers for the comments that greatly improved the manuscript.

## Appendix A. Supplementary material

Supplementary material related to this article can be found online at https://doi.org/10.1016/j.epsl.2021.116873.

## References

Arevalo, R., McDonough, W.F., 2008. Tungsten geochemistry and implications for understanding the Earth's interior. Earth Planet. Sci. Lett. 272, 656-665.

Blundy, J., Wood, B., 1994. Prediction of crystal-melt partition coefficients from elastic moduli. Nature 372, 452-454.

Brice, J.C., 1975. Some thermodynamic aspects of the growth of strained crystals. J. Cryst. Growth 28, 249-253.

Campbell, A.J., Danielson, L., Righter, K., Seagle, C.T., Wang, Y., Prakapenka, V.B., 2009. High pressure effects on the iron-iron oxide and nickel-nickel oxide oxygen fugacity buffers. Earth Planet. Sci. Lett. 286, 556-564.

Coltice, N., Moreira, M., Hernlund, J., Labrosse, S., 2011. Crystallization of a basal magma ocean recorded by Helium and Neon. Earth Planet. Sci. Lett. 308, 193-199.

Corgne, A., Liebske, C., Wood, B.J., Rubie, D.C., Frost, D.J., 2005. Silicate perovskite-melt partitioning of trace elements and geochemical signature of a deep perovskitic reservoir. Geochim. Cosmochim. Acta 69, 485-496.

Corgne, A., Wood, B.J., 2002. CaSiO3 and CaTiO3 perovskite-melt partitioning of trace elements: Implications for gross mantle differentiation. Geophys. Res. Lett. 29, 39-31-39-34.

Deng, J., Du, Z., Karki, B.B., Ghosh, D.B., Lee, K.K.M., 2020. A magma ocean origin to divergent redox evolutions of rocky planetary bodies and early atmospheres. Nat. Commun. 11, 2007.

Elkins-Tanton, L.T., 2012. Magma oceans in the inner Solar System. Annu. Rev. Earth Planet. Sci. 40 (40), 113-139.

Frenkel, D., Smit, B., 2002. Chapter 7 - Free energy calculations. In: Frenkel, D., Smit, B. (Eds.), Understanding Molecular Simulation, second edition. Academic Press, San Diego, pp. 167-200.

Freysoldt, C., Grabowski, B., Hickel, T., Neugebauer, J., Kresse, G., Janotti, A., Van de Walle, C.G., 2014. First-principles calculations for point defects in solids. Rev. Mod. Phys. 86, 253-305.

Freysoldt, C., Neugebauer, J., Van de Walle, C.G., 2009. Fully ab initio finite-size corrections for charged-defect supercell calculations. Phys. Rev. Lett. 102, 016402.

Gajdoš, M., Hummer, K., Kresse, G., Furthmüller, J., Bechstedt, F., 2006. Linear optical properties in the projector-augmented wave methodology. Phys. Rev. B 73, 045112.

Hoover, W.G., 1985. Canonical dynamics: equilibrium phase-space distributions. Phys. Rev. A 31, 1695-1697.

Jackson, C.R.M., Ziegler, L.B., Zhang, H., Jackson, M.G., Stegman, D.R., 2014. A geochemical evaluation of potential magma ocean dynamics using a parameterized model for perovskite crystallization. Earth Planet. Sci. Lett. 392, 154-165.

Jacobsen, S.B., 2005. The Hf-W isotopic system and the origin of the Earth and Moon. Annu. Rev. Earth Planet. Sci. 33, 531-570.

Karato, S.-i., 2016. Physical basis of trace element partitioning: a review. Am. Mineral. 101, 2577-2593.

Karki, B.B., Wentzcovitch, R.M., de Gironcoli, S., Baroni, S., 2000. Ab initio lattice dynamics of MgSiO₃ perovskite at high pressure. Phys. Rev. B 62, 14750–14756.

Kresse, G., Furthmüller, J., 1996. Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set. Comput. Mater. Sci. 6, 15–50.

Kresse, G., Joubert, D., 1999. From ultrasoft pseudopotentials to the projector augmented-wave method. Phys. Rev. B 59, 1758–1775.

Labrosse, S., Hernlund, J.W., Coltice, N., 2007. A crystallizing dense magma ocean at the base of the Earth's mantle. Nature 450, 866–869.

Lany, S., Zunger, A., 2009. Accurate prediction of defect properties in density functional supercell calculations. Model. Simul. Mater. Sci. Eng. 17, 084002.

Liebske, C., Corgne, A., Frost, D.J., Rubie, D.C., Wood, B.J., 2005. Compositional effects on element partitioning between Mg-silicate perovskite and silicate melts. Contrib. Mineral. Petrol. 149, 113–128.

Makov, G., Payne, M.C., 1995. Periodic boundary conditions in ab initio calculations. Phys. Rev. B 51, 4014–4022.

McDonough, W.F., Sun, S.S., 1995. The composition of the Earth. Chem. Geol. 120, 223–253.

Mei, Q.-F., Yang, J.-H., Wang, Y.-F., Wang, H., Peng, P., 2019. Tungsten isotopic constraints on homogenization of the Archean silicate Earth: implications for the transition of tectonic regimes. Geochim. Cosmochim. Acta.

Mermin, N.D., 1965. Thermal properties of the inhomogeneous electron gas. Phys. Rev. 137, A1441–A1443.

Momma, K., Izumi, F., 2011. VESTA 3 for three-dimensional visualization of crystal, volumetric and morphology data. J. Appl. Crystallogr. 44, 1272–1276.

Mundl, A., Touboul, M., Jackson, M.G., Day, J.M.D., Kurz, M.D., Lekic, V., Helz, R.T., Walker, R.J., 2017. Tungsten-182 heterogeneity in modern ocean island basalts. Science 356, 66–69.

Nakajima, M., Stevenson, D.J., 2015. Melting and mixing states of the Earth's mantle after the Moon-forming impact. Earth Planet. Sci. Lett. 427, 286–295.

Onuma, N., Higuchi, H., Wakita, H., Nagasawa, H., 1968. Trace element partition between two pyroxenes and the host lava. Earth Planet. Sci. Lett. 5, 47–51.

Perdew, J.P., Ruzsinszky, A., Csonka, G.I., Vydrov, O.A., Scuseria, G.E., Constantin, L.A., Zhou, X., Burke, K., 2008. Restoring the density-gradient expansion for exchange in solids and surfaces. Phys. Rev. Lett. 100, 136406.

Perry, S.N., Pigott, J.S., Panero, W.R., 2017. Ab initio calculations of uranium and thorium storage in CaSiO₃-perovskite in the Earth's lower mantle. Am. Mineral. 102, 321–326.

Puchtel, I.S., Touboul, M., Blichert-Toft, J., Walker, R.J., Brandon, A.D., Nicklas, R.W., Kulikov, V.S., Samsonov, A.V., 2016. Lithophile and siderophile element systematics of Earth's mantle at the Archean-Proterozoic boundary: evidence from 2.4 Ga komatiites. Geochim. Cosmochim. Acta 180, 227–255.

Ramo, D.M., Stixrude, L., 2014. Spin crossover in Fe₂SiO₄ liquid at high pressure. Geophys. Res. Lett. 41, 4512–4518.

Righter, K., 2011. Prediction of metal-silicate partition coefficients for siderophile elements: an update and assessment of PT conditions for metal-silicate equilibrium during accretion of the Earth. Earth Planet. Sci. Lett. 304, 158–167.

Rizo, H., Andrault, D., Bennett, N.R., Humayun, M., Brandon, A., Vlastelic, I., Moine, B., Poirier, A., Bouhifd, M.A., Murphy, D.T., 2019. 182W evidence for core-mantle interaction in the source of mantle plumes. Geochem. Perspect. Lett. 11, 6–11.

Rizo, H., Walker, R.J., Carlson, R.W., Horan, M.F., Mukhopadhyay, S., Manthos, V., Francis, D., Jackson, M.G., 2016. Preservation of Earth-forming events in the tungsten isotopic composition of modern flood basalts. Science 352, 809–812.

Schimka, L., Harl, J., Kresse, G., 2011. Improved hybrid functional for solids: the HSEsol functional. J. Chem. Phys. 134, 024116.

Shannon, R.D., 1976. Revised effective ionic radii and systematic studies of interatomic distances in halides and chalcogenides. Acta Crystallogr., Sect. A 32, 751–767.

Siebert, J., Corgne, A., Ryerson, F.J., 2011. Systematics of metal-silicate partitioning for many siderophile elements applied to Earth's core formation. Geochim. Cosmochim. Acta 75, 1451–1489.

Sola, E., Alfè, D., 2009. Melting of Iron under Earth's core conditions from diffusion Monte Carlo free energy calculations. Phys. Rev. Lett. 103, 078501.

Stixrude, L., de Koker, N., Sun, N., Mookherjee, M., Karki, B.B., 2009. Thermodynamics of silicate liquids in the deep Earth. Earth Planet. Sci. Lett. 278, 226–232.

Stixrude, L., Lithgow-Bertelloni, C., 2005. Thermodynamics of mantle minerals - I. Physical properties. Geophys. J. Int. 162, 610–632.

Stixrude, L., Lithgow-Bertelloni, C., 2011. Thermodynamics of mantle minerals - II. Phase equilibria. Geophys. J. Int. 184, 1180–1213.

Stixrude, L., Lithgow-Bertelloni, C., 2012. Geophysics of chemical heterogeneity in the mantle. Annu. Rev. Earth Planet. Sci. 40 (40), 569–595.

Stixrude, L., Scipioni, R., Desjarlais, M.P., 2020. A silicate dynamo in the early Earth. Nat. Commun. 11, 935.

Sundell, P.G., Björketun, M.E., Wahnström, G., 2006. Thermodynamics of doping and vacancy formation in BaZrO₃ perovskite oxide from density functional calculations. Phys. Rev. B 73, 104112.

Tang, W., Sanville, E., Henkelman, G., 2009. A grid-based bader analysis algorithm without lattice bias. J. Phys. Condens. Matter 21, 084204.

Tateno, S., Hirose, K., Sakata, S., Yonemitsu, K., Ozawa, H., Hirata, T., Hirao, N., Ohishi, Y., 2018. Melting phase relations and element partitioning in MORB to lower-most mantle conditions. J. Geophys. Res., Solid Earth 123, 5515–5531.

Touboul, M., Puchtel, I.S., Walker, R.J., 2012. ¹⁸²W evidence for long-term preservation of early mantle differentiation products. Science 335, 1065–1069.

Verma, A.K., Karki, B.B., 2009a. Ab initio investigations of native and protonic point defects in Mg2SiO4 polymorphs under high pressure. Earth Planet. Sci. Lett. 285, 140–149.

Verma, A.K., Karki, B.B., 2009b. First-principles simulations of native point defects and ionic diffusion in high-pressure polymorphs of silica. Phys. Rev. B 79, 214115.

Wade, J., Wood, B.J., Tuff, J., 2012. Metal-silicate partitioning of Mo and W at high pressures and temperatures: evidence for late accretion of sulphur to the Earth. Geochim. Cosmochim. Acta 85, 58–74.

Walter, M.J., Nakamura, E., Trønnes, R.G., Frost, D.J., 2004. Experimental constraints on crystallization differentiation in a deep magma ocean. Geochim. Cosmochim. Acta 68, 4267–4284.

Willbold, M., Mojzsis, S.J., Chen, H.W., Elliott, T., 2015. Tungsten isotope composition of the Acasta Gneiss Complex. Earth Planet. Sci. Lett. 419, 168–177.

Zhang, S.B., Northrup, J.E., 1991. Chemical potential dependence of defect formation energies in GaAs: application to Ga self-diffusion. Phys. Rev. Lett. 67, 2339–2342.

Zhang, Z., Stixrude, L., Brodholt, J., 2013. Elastic properties of MgSiO3-perovskite under lower mantle conditions and the composition of the deep Earth. Earth Planet. Sci. Lett. 379, 1–12.

Ziegler, L.B., Stegman, D.R., 2013. Implications of a long-lived basal magma ocean in generating Earth's ancient magnetic field. Geochem. Geophys. Geosyst. 14, 4735–4742.