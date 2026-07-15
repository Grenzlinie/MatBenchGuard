# Native defects, hydrogen impurities, and metal dopants in CeO₂

Khang Hoang¹,∗ and Michelle D. Johannes²

¹ Center for Computationally Assisted Science and Technology & Department of Physics,
North Dakota State University, Fargo, North Dakota 58108, United States.
² Center for Computational Materials Science, U.S. Naval Research Laboratory,
4555 Overlook Ave SW, Washington, District of Columbia 20375, United States.

(Dated: September 1, 2025)

Ceria (CeO₂) is a material of significant technological importance. A detailed understanding of
the material’s defect physics and chemistry is key to understanding and optimizing its properties.
Here, we report a hybrid density-functional study of native point defects, hydrogen impurities, and
metal dopants in CeO₂. We find that electron polarons ($\eta_{Ce}^{-}$) and oxygen vacancies ($V_{O}^{2+}$) are
the dominant native defects under conditions ranging from extreme oxidizing to highly reducing.
Hydrogen is stable either in the hydroxyl ($H_{i}^{+}$) or hydride ($H_{O}^{+}$) structure but the substitutional
$H_{O}^{+}$ is energetically more favorable than $H_{i}^{+}$ only under highly reducing conditions. The interstitial
$H_{i}^{+}$ is highly mobile in the bulk. Yttrium (Y) is energetically most favorable at the substitutional
Ce site. Copper (Cu) and nickel (Ni) can be incorporated at the substitutional site and/or an
interstitial site, depending on actual conditions during preparation, and the dopants can exist in
different charge and spin states. In light of the results, we discuss electronic and ionic conduction
and the effects of metal doping on the formation of electron polarons and oxygen vacancies.

## I. INTRODUCTION

Ceria (CeO₂), a rare-earth metal oxide, is of interest
for numerous important applications. CeO₂-based ma-
terials have most commonly been used as a catalyst or
as a non-inert support for catalysts; they have also been
considered for use in fuel cells, hydrocarbon reforming,
photocatalysis, water splitting, biomedical applications,
among others [1]. Defect physics and chemistry plays an
essential role in the properties and functionalities of ma-
terials [2–4]. Oxygen release and uptake in CeO₂, for ex-
ample, arises from the ability to deviate from stoichiome-
try. Electronic and ionic conduction in the metal oxide is
also governed by the formation and migration of respec-
tive charge-carrying electronic and ionic defects [5–8]. In
addition to native point defects, which are intrinsic to the
material, extrinsic defects such as impurities and dopants
are present or intentionally introduced to manipulate the
material’s properties [9–23]. A detailed understanding of
the defect physics and chemistry in CeO₂ is key to opti-
mizing its performance in various applications.

Density-functional theory (DFT) based first-principles
studies of defects in CeO₂ have been carried out by many
authors [24–35], mainly using the DFT+$U$ method [36,
37] with the Hubbard $U$ term often applied on the Ce $4f$
states and with few studies using a hybrid DFT/Hartree-
Fock method [38, 39]. Although much has been learned
from these studies, the fundamental understanding is still
far from satisfactory. Certain aspects of defects in CeO₂
are under debate; for example, the dominant native de-
fects in the materials under different experimental condi-
tions or the lattice and electronic structure and energetics
of specific defects. More importantly, there is still a lack
of a more comprehensive and rigorous approach that can
provide a deep understanding of the defect physics that
in turn can offer physical insights for materials design.

We herein report a study of native defects, hydrogen
impurities, and metal dopants in CeO₂, using a hybrid
DFT/Hartree-Fock method [38, 39] which treats all or-
bitals in all elements on equal footing. Supercell models
much larger than those used in the previous DFT-based
studies are employed to properly take into account local
lattice distortion and to reduce artificial defect-defect in-
teraction. In addition to common native defects, hydro-
gen impurities are selected for this study as CeO₂ is often
prepared, treated, or used in an H₂-rich environment. For
metal dopants, we select yttrium (Y), copper (Cu), and
nickel (Ni) as examples. These metal dopants are often
found in CeO₂-based materials [13–23] and, as it will be
made clear later, they represent rather distinct physics
and chemistry. In light of the results for the lattice and
electronic structure, energetics, and migration of defects,
we discuss possible defect landscapes in CeO₂, the elec-
tronic and ionic conduction, and the effects of hydrogen
impurities and of metal doping. Comparison with previ-
ously reported computational studies and with available
experiments is made where appropriate.

## II. METHODOLOGY

First-principles calculations are based on the Heyd-
Scuseria-Ernzerhof (HSE06) screened hybrid functional
[38], the projector augmented wave (PAW) method [40],
and a plane-wave basis set, as implemented in the Vi-
enna Ab Initio Simulation Package (VASP) [41–43]. We
use the standard PAW potentials in the VASP database
which treat Ce $5s^25p^64f^15d^16s^2$, O $2s^22p^4$, H $1s^1$, Y
$4s^24p^64d^15s^2$, Cu $3d^{10}4s^1$, and Ni $3d^84s^2$ explicitly as
valence electrons and the rest as core electrons. The

∗ E-mail: khang.hoang@ndsu.edu

Hartree-Fock mixing parameter and the screening length are set to the standard values of 25% and 10 Å, respectively; the plane-wave basis-set cutoff is set to 500 eV. The calculations for bulk $CeO_2$ (four formula units per unit cell) are carried out using $\mathbf{k}$-point meshes as dense as $8 \times 8 \times 8$; $\mathbf{k}$-point meshes for other bulk phases (Ce, $Ce_2O_3$, Cu, CuO, Ni, NiO, Y, and $Y_2O_3$) and isolated molecules ($O_2$, $H_2$, and $H_2O$) are chosen appropriately. Defects in $CeO_2$ are modeled using cubic $3 \times 3 \times 3$ (324-atom) supercells. Integrations over the Brillouin zone in the defect calculations are carried out using the $\Gamma$ point. In all calculations, structural relaxations are performed with the HSE06 functional and the force threshold is chosen to be $0.02\ \text{eV}/\text{Å}$; the spin polarization is included and the convergence is assumed when the total energy difference between consecutive cycles is within $10^{-5}\ \text{eV}$.

The formation energy of a defect or defect complex X in effective charge state $q$ is defined as [44, 45]

$$
\begin{aligned}
E^{f}(\mathrm{X}^{q})= & \quad E_{\mathrm{tot}}(\mathrm{X}^{q})-E_{\mathrm{tot}}(\mathrm{bulk})-\sum_{i} n_{i} \mu_{i} \quad (1) \\
& \quad +q(E_{\mathrm{v}}+\mu_{\mathrm{e}})+\Delta^{q},
\end{aligned}
$$

where $E_{\mathrm{tot}}(\mathrm{X}^{q})$ and $E_{\mathrm{tot}}(\mathrm{bulk})$ are, respectively, the total energies of a supercell containing X and of an equivalent supercell of the perfect host material. $\mu_{i}$ is the atomic chemical potential of species $i$ that have been added to ($n_i$>0) or removed from ($n_i$<0) the supercell to form the defect. $\mu_{\mathrm{e}}$ is the electron chemical potential, i.e., the Fermi level, referenced to the valence-band maximum (VBM) in the bulk ($E_{v}$). Finally, $\Delta^{q}$ is the correction term to align the electrostatic potentials of the perfect bulk and defect supercells and to account for finite-size effects on the total energies of charged defects [46].

We examine defect landscapes in $CeO_2$ using three sets of atomic chemical potentials which correspond to three different experimental conditions. Condition $\mathbf{A}$ assumes equilibrium with air at $T=500^\circ\text{C}$ (within the temperature range in which $CeO_2$ is often prepared), which leads to the oxygen chemical potential $\mu_{\mathrm{O}}=-0.87$ eV [47]. Condition $\mathbf{B}$ corresponds to a highly reducing environment in which the host material is assumed to be in equilibrium with the O-deficient phase $Ce_2O_3$, which gives $\mu_{\mathrm{O}}=-3.09$ eV; equivalently, this condition corresponds approximately to, e.g., the oxygen partial pressure $p_{\mathrm{O}_2}=10^{-10}$ atm and $T=1200^\circ\text{C}$ [47]. For completeness, we also consider condition $\mathbf{C}$ which assumes an extreme oxidizing environment where the host is in equilibrium with isolated $O_2$ molecules at 0 K, corresponding to $\mu_{\mathrm{O}}=0$ eV. In each case, the atomic chemical potential of the other species (Ce, H, Y, Cu, and Ni) is determined accordingly using, respectively, $CeO_2$, an isolated $H_2O$ molecule, $Y_2O_3$, CuO, and NiO as limiting phases, except in the case of $\mathbf{B}$ where the limiting phase of Ni, Cu, and H is elemental Ni, elemental Cu, and an isolated $H_2$ molecule, respectively. Since $\mathbf{A}$ and $\mathbf{B}$ are more experimentally relevant, their results will be explicitly reported; we will mention results obtained under condition $\mathbf{C}$ only when needed to have a more complete picture.

The migration of a small polaron between two positions $Q_{\mathrm{A}}$ and $Q_{\mathrm{B}}$ can be described by the transfer of its lattice distortion [48]. We estimate the migration barrier ($E_m$) by computing the total energies of a set of supercell configurations linearly interpolated between $Q_{\mathrm{A}}$ and $Q_{\mathrm{B}}$ and identify the energy maximum. For an oxygen vacancy or hydrogen interstitial, the migration barrier is calculated by using the climbing-image nudged elastic-band (NEB) method [49]. Unless otherwise noted, these sets of NEB calculations are carried out using the DFT+$U$ method [36] that is based on the Perdew-Burke-Ernzerhof (PBE) functional [50], with the effective Hubbard parameter $U=5$ eV applied on the Ce $4f$ states. Castleton et al. [51] have thoroughly benchmarked various DFT functionals for the study of polaron migration in $CeO_2$ and found that PBE+$U$ (with $U=5$ eV) gives a better description over HSE06. Although the same conclusion may not be made regarding the ionic defects, we also employ PBE+$U$ in the NEB calculations for the oxygen vacancy and the hydrogen interstitial to reduce computational costs, thus making the calculations feasible.

Finally, it should be noted that spin-orbit coupling (SOC) is not included as significant cancellation is expected between the terms in Eq. (1). Our tests show that the formation energy of the electron polaron ($\eta_{\mathrm{Ce}}^{-}$) obtained in HSE+SOC calculations is different from that obtained in HSE calculations by only 40 meV, well within the typical error bar of the formation energy calculation (about 0.1 eV). This is also consistent with computational tests done for Eu-related defects in GaN [52].

## III. RESULTS AND DISCUSSION

### A. Bulk properties

$CeO_2$ crystallizes in a face-centered cubic, fluorite-type structure (space group $Fm\overline{3}m$). The lattice constant within the HSE06 functional is $5.387\ \text{Å}$ (at 0 K), which is comparable to the experimental value ($5.401\ \text{Å}$, measured at 100 K) [53]. The Ce–O bond length is $2.33\ \text{Å}$. The electronic contribution to the static dielectric constant of $CeO_2$ is 4.56, based on the real part of the dielectric function $\epsilon_{1}(\omega)$ for $\omega \to 0$. The ionic contribution is 21.89, obtained from the macroscopic ion-clamped static dielectric tensor [54], as calculated using the VASP code. The total dielectric constant is thus 26.45.

Figure 1 shows the electronic structure of $CeO_2$. We find that the VBM is predominantly the O $2p$ states, whereas the conduction-band minimum (CBM) is predominantly the Ce $4f$ states. The calculated band gap is 3.62 eV (indirect). For comparison, the reported experimental band gap is in the range 2.9–4.4 eV [32]. As it will be made clear later, the nature of the electronic structure at the VBM and CBM has great impact on defect formation. Our calculated bulk properties (e.g., band gap and dielectric constant at 0 K) are in agreement with the previous HSE06 bulk calculations [55].

![](./images/1115033252864720907_1.jpg)

FIG. 1. Total and projected electronic densities of states of CeO₂. The zero of energy is set to the highest occupied states.

![](./images/1115033252864720907_2.jpg)

FIG. 2. Formation energies of native defects in CeO₂ obtained under (a) condition $\boldsymbol{A}$ and (b) condition $\boldsymbol{B}$, plotted as a function of the Fermi level from the VBM (at 0 eV) to the CBM (at 3.62 eV). The slope indicates the charge state ($q$): positively (negatively) charged defects have positive (negative) slopes. A solid energy segment represents a stable single point defect configuration; dotted energy segments are complexes of the single defect and one or more electron or hole polarons. $\mu_{\mathrm{e}}^{\mathrm{int}}$, marked by the vertical dotted line, is the position of the Fermi level determined by the native defects.

### B. Native defects

Figure 2 shows the formation energies of relevant native defects in CeO₂. Electronic defects include a hole polaron localized mostly at an O site $[\eta_{\mathrm{O}}^{+}$ with spin $S=1/2$, which can be regarded as $\mathrm{O}^{-}$ at the $\mathrm{O}^{2-}$ site; see Fig. 3(a)] and an electron polaron localized at a Ce site $[\eta_{\mathrm{Ce}}^{-}$, i.e., $\mathrm{Ce}^{3+}$ $4f^{1}$, $S=1/2$, at the $\mathrm{Ce}^{4+}$ site; see Fig. 3(b)]. $\eta_{\mathrm{O}}^{+}$ is formed upon removing an electron from the CeO₂ supercell; naturally, it is the electron from the highest occupied state (i.e., the VBM, which is predominantly the O $2p$ states) that is removed. $\eta_{\mathrm{Ce}}^{-}$ is, on the other hand, formed upon adding an electron to the supercell, naturally to the lowest unoccupied state (i.e., the CBM, which is predominantly the Ce $4f$ states). These polarons are stable even in the absence of any other defect. The interplay between polaron formation and electronic structure in metal oxides has been well discussed in, e.g., Ref. 2. The local lattice environment is distorted with longer Ce-O bond lengths as the negative (positive) charge gets reduced; $2.42$ Å in the case of $\eta_{\mathrm{O}}^{+}$ and $2.41$ Å in the case of $\eta_{\mathrm{Ce}}^{-}$, compared to $2.33$ Å in the perfect bulk material. Since the hole (electron) is highly localized on the lattice, it can be regarded as small polaron.

![](./images/1115033252864720907_3.jpg)

FIG. 3. Structures of representative electronic and ionic native defects in CeO₂: (a) the hole polaron $\eta_{\mathrm{O}}^{+}$, (b) the electron polaron $\eta_{\mathrm{Ce}}^{-}$, and (c) the neutral oxygen vacancy (i.e., a complex of $V_{\mathrm{O}}^{2+}$ and two $\eta_{\mathrm{Ce}}^{-}$). The isovalue for the chargedensity isosurface (yellow) is set to $0.02$ e/Å³. The large (gray) spheres are Ce and small (red) spheres are O. The vacancy is behind the front oxygen atom at the center. All the atomic structures are visualized using VESTA [56].

Ionic defects include the following structurally, electronically, and energetically stable *single* defects: $V_{\mathrm{O}}^{2+}$ (i.e., the removal of an $\mathrm{O}^{2-}$ ion from the supercell), $\mathrm{O}_{i}^{0}$ (the addition of an oxygen that leads to the formation of an O-O dimer with an existing oxygen; the O-O distance is $1.42$ Å), $\mathrm{O}_{i}^{2-}$ (the added $\mathrm{O}^{2-}$ ion is octahedrally coordinated by Ce; the O-Ce distance is $2.55$-$2.62$ Å), $V_{\mathrm{Ce}}^{4-}$ (the removal of a $\mathrm{Ce}^{4+}$ ion), and $\mathrm{Ce}_{i}^{4+}$ (the addition of a $\mathrm{Ce}^{4+}$ ion). In the $V_{\mathrm{O}}^{2+}$ configuration, the nearest O neighbors of the vacancy move inward by $0.23$ Å, and the nearest Ce neighbors move outward by $0.17$ Å. In $V_{\mathrm{Ce}}^{4-}$, the nearest O neighbors of the vacancy move outward by $0.23$ Å, and the nearest Ce neighbors move inward by $0.07$ Å. In $\mathrm{Ce}_{i}^{4+}$, the added $\mathrm{Ce}^{4+}$ ion is octahedrally coordinated by Ce with the distance being $3.01$-$3.02$ Å.

Note that $\mathrm{O}_{i}^{0}$ at the octahedral site is found to be $1.30$ eV higher in energy compared to the O-O dimer configuration. On the other hand, $\mathrm{O}_{i}^{2-}$ in the dimer configuration is $2.45$ eV higher compared to being at the octahedral site. Our results for $\mathrm{O}_{i}^{2-}$ appear to be consistent with experiments where the octahedral interstitial site was assumed in structure refinements [57, 58]. The octahedrally coordinated $\mathrm{O}_{i}^{2-}$ is expected to occur together with $V_{\mathrm{O}}^{2+}$ via an anion-Frenkel pair mechanism, and can recombine under high-temperature treatment [57].

Other (nominal) charge states of these vacancies and interstitials are, in fact, *defect complexes* consisting of the single defects and the electron or hole polaron(s). For example, the +, 0, or − state of $V_O$ is a complex of $V_O^{2+}$ and one, two, or three $\eta_{\text{Ce}}^-$ with the binding energy of 0.29 eV, 0.44 eV, or 0.55 eV with respect to its constituents, respectively. Figure 3(c) shows the structure of the (nominal) neutral oxygen vacancy with two electron polarons as nearest neighbors. Similarly, the 3−, 2−, −, 0, or + state of $V_{\text{Ce}}$ is a complex of $V_{\text{Ce}}^{4-}$ and one, two, three, four, or five $\eta_O^+$ with the binding energy of 1.14 eV, 2.19 eV, 3.01 eV, 3.76 eV, or 4.43 eV, respectively.

Energetically, $\eta_{\text{Ce}}^-$ and $V_O^{2+}$ have the lowest formation energies and thus are the dominant defects in undoped $\text{CeO}_2$, under conditions from extreme oxidizing ($\mu_O = 0$ eV) to highly reducing ($\mu_O = -3.09$ eV). Note that although $V_{\text{Ce}}^{4-}$ has the lowest formation energy in a range of Fermi level values below the CBM, this range is physically inaccessible under experimentally relevant conditions as the formation energy there becomes negative. In the absence of electrically active impurities that can shift the Fermi-level position or when such impurities occur in much lower concentrations than charged native defects, the Fermi level is at $\mu_e^{\text{int}}$, determined by the native defects (As $\mu_e^{\text{int}}$ is at least 0.6 eV from the band edges, contributions from free holes and electrons are negligible). $\mu_e^{\text{int}}$ is the Fermi-level position at which the material maintains its charge neutrality [2]. In $\text{CeO}_2$, $\mu_e^{\text{int}}$ is approximately where $\eta_{\text{Ce}}^-$ and $V_O^{2+}$ have equal formation energies; $\mu_e^{\text{int}} = 1.95$ eV above the VBM for $\mu_O = 0$ eV, 2.24 eV for $\mu_O = -0.87$ eV [Fig. 2(a)], and 2.98 eV for $\mu_O = -3.09$ eV [Fig. 2(b)]. The Fermi level is thus higher in a more reducing environment, which is consistent with experiments [59]. The Fermi level was reported to be about 2.7 eV [60] or $\sim 3$ eV [59] above the VBM in $\text{CeO}_2$ thin films. Note that our results are different from those of Zacherle et al. [26]; the discrepancy can be ascribed to the DFT+$U$ method used in the previous work in which the $U$ term was applied on the Ce $4f$ orbitals only and all other orbitals were left uncorrected. Our findings are also in contrast to those of Zhang et al. [32] (who used a hybrid quantum mechanical/molecular mechanical method) where the anion-Frenkel pair (i.e., $V_O^{2+}$ and $O_i^{2-}$) was found to be dominant and determine the Fermi-level position. As it will be made clear later, knowing $\mu_e^{\text{int}}$ is key to analyzing the interaction between $\text{CeO}_2$ and hydrogen impurities or metal dopants.

The formation energy of $\eta_{\text{Ce}}^-$ (i.e., $\text{Ce}^{3+}$) and $V_O^{2+}$ at $\mu_e^{\text{int}}$ is low, especially under reducing conditions, e.g., 1.14 eV for $\mu_O = -0.87$ eV [an oxidizing environment, see Fig. 2(a)] or 0.41 eV for $\mu_O = -3.09$ eV [highly reducing, Fig. 2(b)]. With such a low formation energy, positively charged oxygen vacancies and $\text{Ce}^{3+}$ can occur with a high concentration. These two defects can be formed simultaneously, e.g., via oxygen loss during materials preparation or under heat treatment in an reducing environment, or during the oxygen release process in electrochemical applications. This is consistent with the fact that $\text{CeO}_2$ samples are often O-deficient and contain $\text{Ce}^{3+}$ [61, 62]. Using our defect notation, the oxygen release and uptake reaction can be written as

$$
\text{O}_\text{O}^0 + 2\text{Ce}_\text{Ce}^{0} \rightleftharpoons \frac{1}{2}\text{O}_2 + V_\text{O}^{2+} + 2\eta_{\text{Ce}}^-. \tag{2}
$$

The oxygen storage capacity is thus necessarily related to the ability to form oxygen vacancies in the material.

Notably, among the native defects, $\eta_{\text{Ce}}^-$ and $V_O^{2+}$ can serve as charge-carrying defects in electronic and ionic conduction, respectively. The migration barrier ($E_m$) of $\eta_{\text{Ce}}^-$ is calculated to be 0.19 eV within DFT+$U$. The energy is only 43 meV in HSE06 calculations; however, it is known that the hybrid functional can underestimate the polaron migration barrier in metal oxides [51]. In both sets of calculations, the saddle-point configuration has the extra electron almost equally distributed over the two neighboring Ce atoms, which is different from DFT+$U$ results of Sun et al. [29], probably due to the smaller (96-atom) supercell used in their calculations. The energy barrier for the migration of $V_O^{2+}$ is 0.72 eV.

Experimentally, electrical conductivity data reported by Blumenthal and Hofmaier [6] for $\text{CeO}_{2-x}$ ($x = 0.00424$) clearly shows two regions in the $\log \sigma$ vs. $1/T$ plot: a high-$T$ (low-$T$) region with an activation energy ($E_a$) of 0.22 eV (0.59 eV). In the high-$T$ region, $E_a = E_m$, showing that our calculated migration barrier (0.19 eV) is in good agreement with experiment (0.22 eV). The higher activation energy (0.59 eV) measured in the low-$T$ region can be ascribed to defect association; i.e., $E_a = E_m + E_b$, where $E_b = 0.37$ eV is the binding energy. This value is comparable to the binding energy (0.29 eV) of $\eta_{\text{Ce}}^-$ and $V_O^{2+}$ we mention earlier. Naik and Tien also reported an activation energy of 0.19 eV in the high-$T$ region for $\text{CeO}_{2-x}$, independent of $x$ up to $x = 0.03$ [8]. Note that the formation energy ($E^f$) does not enter the formula for $E_a$ as the charge-carrying defects (athermal $\eta_{\text{Ce}}^-$) already pre-exist in the material during the conductivity measurement [2]. Finally, the calculated migration barrier for $V_O^{2+}$ is comparable to the experimental activation energy values (0.64-0.82) for ionic conduction reported for various rare-earth doped $\text{CeO}_2$ materials [22, 63-65].

### C. Hydrogen impurities

Figure 4 shows the formation energies of various hydrogen impurities in $\text{CeO}_2$. The hydrogen interstitial is stable as $H_i^+$ with the added proton ($\text{H}^+$) forming a *hydroxyl* structure with an oxygen (the O–H distance is 1.01 Å) and staying in the line connecting two neighboring O atoms; see Fig. 5(a). This $H_i^+$ configuration is 37 meV lower in energy than another one in which the added $\text{H}^+$ ion forms a Ce–O–H line (where the O–H distance is only slightly shorter, 0.97 Å). The 0 (or $-$) state of $H_i$ is not stable as a single defect but a complex of $H_i^+$ and one (two) $\eta_{\text{Ce}}^-$ with a binding energy of 0.22 eV (0.25 eV). The hydrogen molecule interstitial is stable as $(\text{H}_2)_i^0$ with

![](./images/1115033252864720907_4.jpg)

FIG. 4. Formation energies of hydrogen impurities in $CeO_2$ obtained under (a) condition $\mathbf{A}$ and (b) condition $\mathbf{B}$. A solid energy segment represents a stable ionic defect configuration; dotted energy segments are complexes of the ionic defect and one or more electron or hole polarons. $\mu_e^{\text{int}}$ marks the Fermi-level position determined by the native defects.

![](./images/1115033252864720907_5.jpg)

FIG. 5. Structures of hydrogen impurities in $CeO_2$: (a) $H_i^+$, (b) $H_O^+$, and (c) $(H_i$-$V_O)^{3+}$ (i.e., a complex of $H_i^+$ and $V_O^{2+}$). The small green sphere is H; the circle represents the vacancy.

the neutral $H_2$ molecule residing at the center of the Ce octahedron. The substitutional hydrogen at the O lattice site is stable as $H_O^+$ which is an $H^-$ ion at the void left by the removal of an $O^{2-}$ ion; see Fig. 5(b). Although the $H^-$ ion can be seen as standing alone, its distance to the nearest Ce neighbors is $2.40$ Å, comparable to the Ce–H bond lengths in $CeH_3$. $H_O^+$ can thus be regarded as having a hydride structure. Such a substitutional defect can move off-center and form a $H_i$-$V_O$ complex. This complex is found to be stable as $(H_i$-$V_O)^{3+}$, a complex of $H_i^+$ (hydroxyl) and $V_O^{2+}$ with a binding energy of 0.18 eV; see Fig. 5(c). Other (nominal) charge states of $H_i$-$V_O$ are just complexes of $(H_i$-$V_O)^{3+}$ and one or more $\eta_{Ce}^-$.

Among these defects, $H_i^+$ is energetically more favorable at $\mu_e^{\text{int}}$ for $0$ eV $\leq \mu_O \lesssim -2.50$ eV [which includes condition $\mathbf{A}$-see Fig. 4(a)-and condition $\mathbf{C}$]. Interestingly, $H_O^+$ is more favorable for $-2.50$ eV $\lesssim \mu_O \leq -3.09$ eV [which includes condition $\mathbf{B}$, see Fig. 4(b)]. Under less reducing conditions (which also correspond to lower $\mu_e^{\text{int}}$ values), $H_O^+$ (hydride) decomposes into $H_i^+$ (hydroxyl) and an oxygen vacancy. Our results thus suggest that one can control the dominant hydrogen species in the bulk by tuning experimental conditions. We also find that $H_i^+$ is highly mobile in the bulk; its migration barrier is only 60 meV within DFT+$U$, in agreement with the values recently reported by Stimac and Goldman [34] for (nominally neutral) hydrogen interstitials. The migration of $H^+$ ions from the surface into the bulk may be affected by competing processes, however. The out-diffusion from the bulk to the surface, for example, can counteract the in-diffusion. Besides, hydrogen can react with oxygen on the surface to form $H_2O$ or some OH species and get cleaned out. The high activation energy ($< 1.69$ eV) for hydrogen diffusion experimentally observed in $CeO_2$ polycrystalline thin films [12] seems to suggest that the in-diffusion may be impeded by certain processes at the surface/subsurface layers or grain boundaries. This issue, especially regarding hydrogen diffusion in $CeO_2$ single crystals, needs further experimental investigations.

Other experimental reports indicated that hydrogen can be incorporated into the bulk [10, 11], although the solubility appears to be low [66], and $CeO_2$ prepared under $H_2$ flow has a significantly increased $Ce^{3+}$ concentration [9, 67]. The formation of $Ce^{3+}$ is likely associated with the formation of oxygen vacancies. However, as a positively charged defect (donor-like dopant) and if present in the bulk with a significant concentration, $H_i^+$ can also shift the Fermi level toward the CBM [2], thus lowering the the formation energy of $\eta_{Ce}^-$ and therefore increasing its concentration. Finally, Wu et al. [67] reported evidence for the presence of bulk Ce–H species upon $H_2$ dissociation over $CeO_2$. Such hydride species could be related to the $H_O^+$ defect we discussed above.

![](./images/1115033252864720907_6.jpg)

FIG. 6. Formation energies of Y-related defects in $CeO_2$ obtained under (a) condition $\mathbf{A}$ and (b) condition $\mathbf{B}$.

### D. Metal dopants

Figures 6 and 7 show the calculated formation energies of select metal dopants in $CeO_2$. In the following

![](./images/1115033252864720907_7.jpg)

FIG. 7. Formation energies of Cu- and Ni-related defects in
CeO₂ obtained under (a) condition A and (b) condition B.

![](./images/1115033252864720907_8.jpg)

FIG. 8. Structures of representative metal dopants and re-
lated defect complexes in CeO₂: (a) Y⁻_Ce, (b) (Y_Ce-V_O)⁺, (c)
Cu²⁻_Ce, (d) (Cu_Ce-V_O)⁰, (e) Ni²⁻_Ce, and (f) (Ni_Ce-V_O)⁰.

discussion, we focus on the stable charge states (ionic
defect configurations) presented by the solid energy lines
in the formation-energy plot as other (nominal) charge
states (dotted energy lines) are just complexes of the sta-
ble ionic defects and η̄_Ce or η⁺_O (or η*_O in the case of Y_Ce,
where η*_O is an electron hole delocalized over two O sites).

We find that the substitutional Y_Ce is stable as Y⁻_Ce in
which Y³⁺ replaces Ce⁴⁺ at a Ce site. The Y-O distance
is 2.36 Å, comparable to the Ce-O bond length (2.33 Å)
in the perfect bulk material; see Fig. 8(a). The small
lattice distortion is due to the small difference in the
ionic radii of eight-fold coordinated Ce⁴⁺ (0.97 Å) and
Y³⁺ (1.02 Å) [68]. Due to the Coulombic attraction, Y⁻_Ce
and V²⁺_O can come close and form (Y_Ce-V_O)⁺ with the
binding energy of 0.44 eV; see Fig. 8(b). This complex
can capture an η̄_Ce to become (Y_Ce-V_O)⁰ with a binding
energy of 0.59 eV, or combine with another Y⁻_Ce to form a
(2Y_Ce-V_O)⁰ with a binding energy of 0.73 eV. (2Y_Ce-V_O)⁰
is found to be lower in energy than (Y_Ce-V_O)⁰, except in
highly reducing environments (e.g., under condition B).

The interstitial Y_i is stable as Y³⁺_i, which is an extra
Y³⁺ ion at the center of a Ce octahedron. Y³⁺_i is always
in much higher in energy than Y⁻_Ce and related defect
complexes. This is due to the large ionic radius of Y³⁺.

Next, Cu_Ce is stable as Cu²⁻_Ce (i.e., Cu²⁺ 3d⁹, S = 1/2,
at the Ce⁴⁺ site) and/or Cu⁻_Ce (i.e., Cu³⁺ 3d⁸, S = 0,
at the Ce⁴⁺ site). The Cu⁺ ion is thus not stable at the
substitutional site. Cu_Ce is significantly off-center, by
0.99 Å (1.11 Å) in the case of Cu²⁻_Ce (Cu⁻_Ce), and forms a
(slightly square pyramidal distorted) square planar with
four oxygens; see Fig. 8(c). The large lattice distortion
is consistent with the large difference in the ionic radii of
Cu²⁺ (Cu³⁺) and Ce⁴⁺ [68]. Possible Cu-related defect
complexes include (Cu_Ce-V_O)⁰, a complex of Cu²⁻_Ce and
V²⁺_O with a binding energy of 1.35 eV, see Fig. 8(d), and
(Cu_Ce-V_O)⁺, a complex of Cu⁻_Ce and V²⁺_O with a binding
energy of 1.11 eV. Note that our results for Cu are differ-
ent from those of Sun and Yildiz [30]; e.g., (Cu_Ce-V_O)⁺
does not appear in their formation-energy plot.

The interstitial Cu_i is electronically stable as Cu²⁺_i
(i.e, Cu²⁺ 3d⁹, S = 1/2) or Cu⁺_i (Cu⁺ 3d¹⁰, S = 0),
with the Cu²⁺ (or Cu⁺) ion at the center of the Ce
octahedron. We find that, at the Fermi-level position
μ^int_e, the formation energy of Cu⁺_i is higher than Cu²⁻_Ce
for 0 eV ≤ μ_O ≲ −1.10 eV [which includes condition
A—see Fig. 7(a)—and condition C] and lower for −1.10
eV ≲ μ_O ≤ −3.09 eV [which includes condition B, see
Fig. 7(b)]. Cu⁺_i and Cu²⁻_Ce have comparable formation
energies for μ_O ≈ −1.10eV [i.e., near condition A, see
Fig. 7(a)]. Our results suggest that under normal condi-
tions, Cu may exist both as Cu²⁺ at the substitutional
site and as Cu⁺ at the interstitial site. Under reducing
conditions, on the other hand, Cu⁺_i (i.e., Cu⁺) becomes
the dominant Cu species; see, e.g., Fig. 7(b). This ap-
pears to be consistent with experimental observations of
multiple Cu oxidation states in Cu-doped CeO₂ [15, 16].

Finally, Ni_Ce is stable as Ni⁻_Ce (i.e., low-spin Ni³⁺ 3d⁷,
S = 1/2, at the Ce⁴⁺ site) and Ni²⁻_Ce (i.e., low-spin Ni²⁺
3d⁸, S = 0, at the Ce⁴⁺ site). Like Cu, Ni is signifi-
cantly off-center, by 1.07 Å (1.17 Å) in the case of Ni⁻_Ce
(Ni²⁻_Ce), and forms a (slightly square pyramidal distorted)
square planar with four oxygen atoms; see Fig. 8(e). The
high-spin state of Ni²⁺ (S = 2) is only 5 meV higher in
energy than the low-spin one; i.e., they are essentially
degenerate. Defect complexes with oxygen vacancies in-
clude (Ni_Ce-V_O)⁰, a complex of Ni²⁻_Ce and V²⁺_O with a
binding energy of 1.33 eV, see Fig. 8(f), and (Ni_Ce-V_O)⁺,
a complex of Ni⁻_Ce and V²⁺_O with a binding energy of
1.11 eV. Similar to Cu_i, the interstitial Ni_i is also stable
electronically as Ni²⁺_i (where the low-spin and high-spin
states Ni²⁺ are degenerate in energy) or Ni⁺_i (i.e., Ni⁺
3d⁹; S = 1/2). At μ^int_e, Ni⁺_i is higher in energy than Ni²⁻_Ce
under conditions A and C, but lower under condition B;
see Fig. 7(b); the crossover point is at μ_O ≈ −1.59 eV.
Note that Wang et al. [35] also found the interstitial Ni

to be stable as $Ni^+$ in their DFT+$U$ calculations.

Overall, we find that, under experimentally relevant conditions such as in Fig. 6 and Fig. 7, the substitutional dopants Y, Cu, and Ni in $CeO_2$ are stable, respectively, as $Y_{Ce}^-$, $Cu_{Ce}^{2-}$, and $Ni_{Ce}^{2-}$ (either as unassociated defects or in complexes with oxygen vacancies) at the Fermi level $\mu_e^{int}$ determined by native defects. The Y, Cu, and Ni interstitials, on the other hand, are stable as $Y_i^{3+}$, $Cu_i^+$, and $Ni_i^{2+}$, respectively. For Cu and Ni, the lattice site preference (substitutional vs. interstitial) and the charge and spin state of the metal dopants depends on actual experimental conditions. The difference in the structure and energetics between Cu (or Ni) versus Y can be ascribed to the Shannon ionic radius of Cu (Ni) being smaller than that of Y [68]. As negatively charged (acceptor-like) defects, $Y_{Ce}^-$, $Cu_{Ce}^{2-}$, and $Ni_{Ce}^{2-}$ can facilitate the formation of charge-compensating, positively charged oxygen vacancies, without increasing the concentration of $Ce^{3+}$ and thus without increasing the electronic conductivity. As positively charged (donor-like) defects and if present with a large concentration, $Y_i^{3+}$, $Cu_i^+$, and $Ni_i^{2+}$ can lower the formation energy of $\eta_{Ce}^-$ and thus increase the $Ce^{3+}$ concentration. See, e.g., Ref. 2 for a further discussion of effects of doping in complex metal oxides.

As a general note, having a finite binding energy does not mean a complex will readily form. Under thermal equilibrium, the binding energy needs to be greater than the larger of the formation energies of the individual defects for the complex to have higher concentration than its constituents [44]. Most of the relevant defect complexes considered in this work have a small binding energy. This suggests that their concentration is expected to be much smaller than that of the isolated constituents.

Experimentally, Thurber et al. [19] reported x-ray photoelectron spectroscopy studies of $Ce_{1-x}Ni_xO_2$ nanoparticles ($0.01 \leq x \leq 0.20$) which showed that nickel is substitutionally incorporated as $Ni^{2+}$ at the Ce site in the bulk; there is also contribution from $Ni^{3+}$ surface states. Derafa et al. [20], on the other hand, reported the incorporation of nickel into the lattice in the form of $Ni^{3+}$ species in $Ni_{0.1}Ce_{0.9}O_{2-x}$ nanoparticles. The determination of the identity of Ni species in $CeO_2$ is expected to be challenging as, according to our results, the dopant can be incorporated into the lattice at different lattice sites and exist in different charge and spin states. Regarding the effects of substitutional metal doping, experimental studies appear to be unanimous on the role of Y, Cu, and Ni in promoting oxygen vacancies [13, 14, 17, 19–23], which is consistent with our above analysis.

## IV. CONCLUSIONS

We have carried out a hybrid density-functional study of defect physics in bulk $CeO_2$. The (negatively charged) electron polaron ($\eta_{Ce}^-$, i.e., $Ce^{3+}$) and the positively charged oxygen vacancy ($V_O^{2+}$) are found to be the dominant native defects under conditions ranging from extreme oxidizing to highly reducing. The migration barriers of and the binding energy between $\eta_{Ce}^-$ and $V_O^{2+}$ are in good agreement with experiments. Hydrogen is stable either in the hydroxyl ($H_i^+$) or hydride ($H_O^+$) configuration, depending actual experimental conditions. The interstitial $H_i^+$ is highly mobile in the bulk. Yttrium is most stable as the substitutional lattice site; the lattice preference (substitutional versus interstitial) of copper and nickel, on the other hand, depends on actual conditions during materials preparation, and the dopants can exist in different charge and spin states. In light of the results, we discuss the effects of metal doping on the formation of electron polarons and oxygen vacancies.

This work thus provides guidance for experimental defect characterization and defect-controlled synthesis. It also serves as a methodological template and a basis for further investigation of other dopants and impurities. A detailed understanding of the synthesis-(defect) structure–property relationship such as that developed here would ultimately lead to the design and discovery of $CeO_2$-based materials with better performance.

## ACKNOWLEDGMENTS

M.D.J. was supported by the U.S. Office of Naval Research through the U.S. Naval Research Laboratory's core fundamental research program. This work used resources of the Center for Computationally Assisted Science and Technology (CCAST) at North Dakota State University, which were made possible in part by National Science Foundation Major Research Instrumentation (MRI) Award No. 2019077.

[1] T. Montini, M. Melchionna, M. Monai, and P. Fornasiero, Fundamentals and Catalytic Applications of $CeO_2$-Based Materials, Chem. Rev. 116, 5987 (2016).

[2] K. Hoang and M. D. Johannes, Defect physics in complex energy materials, J. Phys.: Condens. Matter 30, 293001 (2018).

[3] J. Paier, C. Penschke, and J. Sauer, Oxygen Defects and Surface Chemistry of Ceria: Quantum Chemical Studies Compared to Experiment, Chem. Rev. 113, 3949 (2013).

[4] R. Schmitt, A. Nenning, O. Kraynis, R. Korobko, A. I. Frenkel, I. Lubomirsky, S. M. Haile, and J. L. M. Rupp, A review of defect structure and chemistry in ceria and its solid solutions, Chem. Soc. Rev. 49, 554 (2020).

[5] E. Shoko, M. Smith, and R. H. McKenzie, Charge distribution and transport properties in reduced ceria phases: A review, J. Phys. Chem. Solids 72, 1482 (2011).

[6] R. N. Blumenthal and R. L. Hofmaier, The Temperature and Compositional Dependence of the Electrical Conduc-

tivity of Nonstoichiometric $CeO_{2-x}$, J. Electrochem. Soc.
121, 126 (1974).

[7] H. Tuller and A. Nowick, Small polaron electron trans-
port in reduced $CeO_2$ single crystals, J. Phys. Chem.
Solids 38, 859 (1977).

[8] I. Naik and T. Tien, Small-polaron mobility in nonstoi-
chiometric cerium dioxide, J. Phys. Chem. Solids 39, 311
(1978).

[9] K. Lee, S. Kim, S. Sun, G. Lee, J. Kwon, J. Hwang,
J. Seo, U. Paik, and T. Song, Hydrogenated ceria
nanoparticles for high-efficiency silicate adsorption, New
J. Chem. 46, 20572 (2022).

[10] J. Fierro, J. Soria, J. Sanz, and J. Rojo, Induced changes
in ceria by thermal treatments under vacuum or hydro-
gen, J. Solid State Chem. 66, 154 (1987).

[11] L. A. Bruce, M. Hoang, A. E. Hughes, and T. W. Turney,
Surface area control during the synthesis and reduction
of high area ceria catalyst supports, Appl. Catal. A: Gen.
134, 351 (1996).

[12] W. Mao, W. Gong, Z. Gu, M. Wilde, J. Chen, K. Fuku-
tani, H. Matsuzaki, B. Fugetsu, I. Sakata, and T. Terai,
Hydrogen diffusion in cerium oxide thin films fabricated
by pulsed laser deposition, Int. J. Hydrogen Energy 50,
969 (2024).

[13] S. Zhang, C. Zhao, Y. Liu, W. Li, J. Wang, G. Wang,
Y. Zhang, H. Zhang, and H. Zhao, Cu doping in $CeO_2$
to form multiple oxygen vacancies for dramatically en-
hanced ambient $N_2$ reduction performance, Chem. Com-
mun. 55, 2952 (2019).

[14] K. S. Ranjith, C.-L. Dong, Y.-R. Lu, Y.-C. Huang, C.-L.
Chen, P. Saravanan, K. Asokan, and R. T. Rajendra Ku-
mar, Evolution of Visible Photocatalytic Properties of
Cu-Doped $CeO_2$ Nanoparticles: Role of $Cu^{2+}$-Mediated
Oxygen Vacancies and the Mixed-Valence States of Ce
Ions, ACS Sustain. Chem. Eng. 6, 8536 (2018).

[15] E. Sartoretti, C. Novara, M. C. Paganini, M. Chiesa,
M. Castellino, F. Giorgis, M. Piumetti, S. Bensaid,
D. Fino, and N. Russo, Study of Cu-doped ce-
ria through a combined spectroscopic approach: Involve-
ment of different catalytic sites in CO oxidation, Catal.
Today 420, 114037 (2023).

[16] A. Davó-Quiñonero, E. Bailón-García, S. López-
Rodríguez, J. Juan-Juan, D. Lozano-Castelló, M. García-
Melchor, F. C. Herrera, E. Pellegrin, C. Escudero, and
A. Bueno-López, Insights into the Oxygen Vacancy Fill-
ing Mechanism in $CuO/CeO_2$ Catalysts: A Key Step
Toward High Selectivity in Preferential CO Oxidation,
ACS Catal. 10, 6532 (2020).

[17] K. Polychronopoulou, A. A. AlKhoori, A. M. Efstathiou,
M. A. Jaoude, C. M. Damaskinos, M. A. Baker, A. Al-
mutawa, D. H. Anjum, M. A. Vasiliades, A. Belabbes,
L. F. Vega, A. F. Zedan, and S. J. Hinder, Design As-
pects of Doped $CeO_2$ for Low-Temperature Catalytic CO
Oxidation: Transient Kinetics and DFT Approach, ACS
Appl. Mater. Interfaces 13, 22391 (2021).

[18] G. Wrobel, C. Lamonier, A. Bennani, A. D'Huysser, and
A. Aboukaïs, Effect of incorporation of copper or nickel
on hydrogen storage in ceria. Mechanism of reduction, J.
Chem. Soc., Faraday Trans. 92, 2001 (1996).

[19] A. Thurber, K. M. Reddy, V. Shutthanandan, M. H. En-
gelhard, C. Wang, J. Hays, and A. Punnoose, Ferromag-
netism in chemically synthesized $CeO_2$ nanoparticles by
Ni doping, Phys. Rev. B 76, 165206 (2007).

[20] W. Derafa, F. Paloukis, B. Mewafy, W. Baaziz, O. Ersen,
C. Petit, G. Corbel, and S. Zafeiratos, Synthesis and
characterization of nickel-doped ceria nanoparticles with
improved surface reducibility, RSC Adv. 8, 40712 (2018).

[21] K. Fuda, K. Kishio, S. Yamauchi, K. Fueki, and Y. On-
oda, $^{17}$O NMR study of $Y_2O_3$-doped $CeO_2$, J. Phys.
Chem. Solids 45, 1253 (1984).

[22] D. Y. Wang, D. Park, J. Griffith, and A. Nowick, Oxygen-
ion conductivity and defect interactions in yttria-doped
ceria, Solid State Ion. 2, 95 (1981).

[23] W. Lee, S.-Y. Chen, Y.-S. Chen, C.-L. Dong, H.-J. Lin,
C.-T. Chen, and A. Gloter, Defect Structure Guided
Room Temperature Ferromagnetism of Y-Doped $CeO_2$
Nanoparticles, J. Phys. Chem. C 118, 26359 (2014).

[24] N. V. Skorodumova, S. I. Simak, B. I. Lundqvist, I. A.
Abrikosov, and B. Johansson, Quantum Origin of the
Oxygen Storage Capability of Ceria, Phys. Rev. Lett. 89,
166601 (2002).

[25] P. R. L. Keating, D. O. Scanlon, B. J. Morgan, N. M.
Galea, and G. W. Watson, Analysis of Intrinsic Defects
in $CeO_2$ Using a Koopmans-Like GGA+$U$ Approach, J.
Phys. Chem. C 116, 2443 (2012).

[26] T. Zacherle, A. Schriever, R. A. De Souza, and M. Mar-
tin, Ab initio analysis of the defect structure of ceria,
Phys. Rev. B 87, 134104 (2013).

[27] B. Huang, R. Gillen, and J. Robertson, Study of $CeO_2$
and Its Native Defects by Density Functional Theory
with Repulsive Potential, J. Phys. Chem. C 118, 24248
(2014).

[28] J. J. Plata, A. M. Márquez, and J. F. Sanz, Electron
Mobility via Polaron Hopping in Bulk Ceria: A First-
Principles Study, J. Phys. Chem. C 117, 14502 (2013).

[29] L. Sun, X. Huang, L. Wang, and A. Janotti, Disentan-
gling the role of small polarons and oxygen vacancies in
$CeO_2$, Phys. Rev. B 95, 245101 (2017).

[30] L. Sun and B. Yildiz, Solubility Limit of Cu and Fac-
tors Governing the Reactivity of $Cu-CeO_2$ Assessed from
First-Principles Defect Chemistry and Thermodynamics,
J. Phys. Chem. C 123, 399 (2019).

[31] L. Sun, X. Hao, Q. Meng, L. Wang, F. Liu, and M. Zhou,
Polaronic Resistive Switching in Ceria-Based Memory
Devices, Adv. Electron. Mater. 5, 1900271 (2019).

[32] X. Zhang, L. Zhu, Q. Hou, J. Guan, Y. Lu, T. W. Keal,
J. Buckeridge, C. R. A. Catlow, and A. A. Sokol, Toward
a Consistent Prediction of Defect Chemistry in $CeO_2$,
Chem. Mater. 35, 207 (2023).

[33] K. Sohlberg, S. T. Pantelides, and S. J. Pennycook, In-
teractions of Hydrogen with $CeO_2$, J. Am. Chem. Soc.
123, 6609 (2001).

[34] J. C. Stimac and N. Goldman, Quantum Calculations of
Hydrogen Absorption and Diffusivity in Bulk $CeO_2$, ACS
Omega 10, 12385 (2025).

[35] X. Wang, M. Shen, J. Wang, and S. Fabris, Enhanced
Oxygen Buffering by Substitutional and Interstitial Ni
Point Defects in Ceria: A First-Principles DFT+$U$
Study, J. Phys. Chem. C 114, 10221 (2010).

[36] V. I. Anisimov, J. Zaanen, and O. K. Andersen, Band
theory and Mott insulators: Hubbard U instead of Stoner
I, Phys. Rev. B 44, 943 (1991).

[37] A. I. Liechtenstein, V. I. Anisimov, and J. Zaanen,
Density-functional theory and strong interactions: Or-
bital ordering in Mott-Hubbard insulators, Phys. Rev. B
52, R5467 (1995).

[38] J. Heyd, G. E. Scuseria, and M. Ernzerhof, Hybrid func-
tionals based on a screened Coulomb potential, J. Chem.

Phys. 118, 8207 (2003).

[39] J. Paier, M. Marsman, K. Hummer, G. Kresse, I. C. Gerber, and J. G. Ángyán, Screened hybrid density functionals applied to solids, J. Chem. Phys. 124, 154709 (2006).

[40] P. E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50, 17953 (1994).

[41] G. Kresse and J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B 47, 558 (1993).

[42] G. Kresse and J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169 (1996).

[43] G. Kresse and J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mat. Sci. 6, 15 (1996).

[44] C. G. Van de Walle and J. Neugebauer, First-principles calculations for defects and impurities: Applications to III-nitrides, J. Appl. Phys. 95, 3851 (2004).

[45] C. Freysoldt, B. Grabowski, T. Hickel, J. Neugebauer, G. Kresse, A. Janotti, and C. G. Van de Walle, First-principles calculations for point defects in solids, Rev. Mod. Phys. 86, 253 (2014).

[46] C. Freysoldt, J. Neugebauer, and C. G. Van de Walle, Fully ab initio finite-size corrections for charged-defect supercell calculations, Phys. Rev. Lett. 102, 016402 (2009).

[47] M. W. Chase, Jr., *NIST-JANAF Themochemical Tables, Fourth Edition* (J. Phys. Chem. Ref. Data, Monograph 9, 1998) pp. 1–1951.

[48] K. M. Rosso, D. M. A. Smith, and M. Dupuis, An ab initio model of electron transport in hematite ($\alpha$-Fe₂O₃) basal planes, J. Chem. Phys. 118, 6455 (2003).

[49] G. Henkelman, B. P. Uberuaga, and H. Jónsson, A climbing image nudged elastic band method for finding saddle points and minimum energy paths, J. Chem. Phys. 113, 9901 (2000).

[50] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77, 3865 (1996).

[51] C. W. M. Castleton, A. Lee, and J. Kullgren, Benchmarking Density Functional Theory Functionals for Polarons in Oxides: Properties of CeO₂, J. Phys. Chem. C 123, 5164 (2019).

[52] K. Hoang, Tuning the valence and concentration of europium and luminescence centers in GaN through co-doping and defect association, Phys. Rev. Materials 5, 034601 (2021).

[53] M. L. Gupta and S. Singh, Thermal Expansion of CeO₂, Ho₂O₃, and Lu₂O3 from 100° to 300°K by an X-Ray Method, J. Am. Ceram. Soc. 53, 663 (1970).

[54] M. Gajdoš, K. Hummer, G. Kresse, J. Furthmüller, and F. Bechstedt, Linear optical properties in the projector-augmented wave methodology, Phys. Rev. B 73, 045112 (2006).

[55] S. Lany, Chemical Potential Analysis as an Alternative to the van't Hoff Method: Hypothetical Limits of Solar Thermochemical Hydrogen, J. Am. Chem. Soc. 146, 14114 (2024).

[56] K. Momma and F. Izumi, *VESTA*3 for three-dimensional visualization of crystal, volumetric and morphology data, J. Appl. Cryst. 44, 1272 (2011).

[57] E. Mamontov and T. Egami, Structural defects in a nanoscale powder of CeO₂ studied by pulsed neutron diffraction, J. Phys. Chem. Solids 61, 1345 (2000).

[58] S. Luo, M. Li, V. Fung, B. G. Sumpter, J. Liu, Z. Wu, and K. Page, New Insights into the Bulk and Surface Defect Structures of Ceria Nanocrystals from Neutron Scattering Study, Chem. Mater. 33, 3959 (2021).

[59] H. F. Wardenga and A. Klein, Surface potentials of (111), (110) and (100) oriented CeO₂−ₓ thin films, Appl. Surf. Sci. 377, 1 (2016).

[60] A. Crovetto, C. Yan, B. Iandolo, F. Zhou, J. Stride, J. Schou, X. Hao, and O. Hansen, Lattice-matched Cu₂ZnSnS₄/CeO₂ solar cell with open circuit voltage boost, Appl. Phys. Lett. 109, 233904 (2016).

[61] H. L. Tuller and A. S. Nowick, Defect Structure and Electrical Properties of Nonstoichiometric CeO₂ Single Crystals, J. Electrochem. Soc. 126, 209 (1979).

[62] A. T. Nelson, D. R. Rittman, J. T. White, J. T. Dunwoody, M. Kato, and K. J. McClellan, An Evaluation of the Thermophysical Properties of Stoichiometric CeO₂ in Comparison to UO₂ and PuO₂, J. Am. Ceram. Soc. 97, 3652 (2014).

[63] K. Huang, M. Feng, and J. B. Goodenough, Synthesis and Electrical Properties of Dense Ce₀.₉Gd₀.₁O₁.₉₅ Ceramics, J. Am. Ceram. Soc. 81, 357 (1998).

[64] B. Steele, Appraisal of Ce₁−ᵧGdᵧO₂−ᵧ/₂ electrolytes for IT-SOFC operation at 500°C, Solid State Ion. 129, 95 (2000).

[65] W. Lai and S. M. Haile, Impedance Spectroscopy as a Tool for Chemical and Electrochemical Analysis of Mixed Conductors: A Case Study of Ceria, J. Am. Ceram. Soc. 88, 2979 (2005).

[66] N. Sakai, K. Yamaji, T. Horita, H. Yokokawa, Y. Hirata, S. Sameshima, Y. Nigara, and J. Mizusaki, Determination of hydrogen solubility in oxide ceramics by using SIMS analyses, Solid State Ion. 125, 325 (1999).

[67] Z. Wu, Y. Cheng, F. Tao, L. Daemen, G. S. Foo, L. Nguyen, X. Zhang, A. Beste, and A. J. Ramirez-Cuesta, Direct Neutron Spectroscopy Observation of Cerium Hydride Species on a Cerium Oxide Catalyst, J. Am. Chem. Soc. 139, 9721 (2017).

[68] R. D. Shannon, Revised effective ionic radii and systematic studies of interatomic distances in halides and chalcogenides, Acta Crystallogr., Sect. A: Found. Crystallogr. 32, 751 (1976).