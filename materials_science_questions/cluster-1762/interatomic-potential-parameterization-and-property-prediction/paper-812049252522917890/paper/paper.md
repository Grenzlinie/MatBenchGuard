ORIGINAL PAPER

# Monte Carlo simulation of mixing in $\mathbf{Ca_3Fe_2Ge_3O_{12}-Ca_4Ge_4O_{12}}$ garnets and implications for the thermodynamic stability of pyrope-majorite solid solution

Victor L. Vinograd · Bjoern Winkler ·
Daniel J. Wilson · Andrew Putnis · Julian D. Gale

Received: 10 April 2006/ Accepted: 23 June 2006/ Published online: 17 October 2006
© Springer-Verlag 2006

## Abstract
Static lattice energy calculations, based on empirical pair potentials, were performed for a large set of structures differing in the arrangement of octa- hedral cations within the garnet $2 \times 2 \times 2$ supercell. The compositions of these structures varied between $Ca_3Fe_2Ge_3O_{12}$ and $Ca_4Ge_4O_{12}$. The energies were cluster expanded using pair and quaternary terms. The derived ordering constants were used to constrain Monte Carlo simulations of temperature-dependent mixing properties in the ranges of 1,073-3,673 K and 0-10 GPa. The free energies of mixing were calculated using the method of thermodynamic integration. The calculations predict a wide miscibility gap between Fe- rich (cubic) and Fe-pure (tetragonal) garnets consistent with recent experimental observations of Iezzi et al. (Phys Chem Miner 32:197-207, 2005). It is shown that the miscibility gap arises due to a very strong cation ordering at the Fe-pure composition, driven by the charge difference between $Ca^{2+}$ and $Ge^{4+}$ cations. The structural and thermodynamic analogies between Ca- Ge and Mg-Si systems suggest that a similar miscibility gap should exist between pyrope and Mg-Si-majorite.

## Keywords
Majorite · Ca-Fe-Ge garnets ·
Mixing properties · Phase relations

---

V. L. Vinograd (凶) · B. Winkler · D. J. Wilson
Institute of Geosciences, University of Frankfurt,
Senckenberganlage 30, 60054 Frankfurt/Main, Germany
e-mail: v.vinograd@kristall.uni-frankfurt.de

A. Putnis
Institute of Mineralogy, University of Münster,
Corrensstrasse 24, 48149 Münster, Germany

J. D. Gale
Nanochemistry Research Institute, Curtin University
of Technology, P.O. Box U1987, Perth 6845 WA, Australia

---

## Introduction
Experimental and theoretical studies of mineral trans- formations in the $MgSiO_3-Al_2O_3$ system (e.g. Akaogi and Akimoto 1977; Kanzaki 1987; Akaogi et al. 1987; Gasparik 2003; Fabrichnaya et al. 2004) show that py- rope-, $Mg_3Al_2Si_3O_{12}$, and majorite-, $Mg_4Si_4O_{12}$, rich garnet should be a main phase of variable composition at the pressure and temperature parameters of the transition zone of the Earth's mantle. Therefore, any model of mineral transformations in the transition zone would benefit from the knowledge of the thermody- namic activities of pyrope and majorite in the garnet phase. Due to experimental challenges, the thermody- namics of mixing of Al, Si, and Mg in the octahedral sites remains poorly constrained. The commonly ac- cepted model (Akaogi et al. 1987) assumes ideal mixing of Al/Si and Al/Mg on two non-equivalent octahedral sites. The two-site model is an acceptable approxima- tion for well-ordered majorite-rich garnets, which crystallize in $I4_1/a$ symmetry. This space group has three Wyckoff positions 4a, 4b, and 8c, which in the fully ordered majorite are occupied by Si, Si, and Mg, respectively (Angel et al. 1989). When the mole frac- tion of pyrope exceeds 20-25%, the tetragonal struc- ture becomes unstable with respect to the cubic, $Ia\overline{3}d$, phase (Heinemann et al. 1997). Within the cubic sym- metry, all octahedral sites are equivalent, and this makes the two-site model less reasonable. In fact, one can expect that the thermodynamics of mixing differs in the two phases. Recently, Vinograd et al. (2006) have

![](./images/812049252522917890_1.jpg)

developed a mixing model for the pyrope-majorite solution that is consistent with the symmetry change at intermediate compositions. This model predicted a miscibility gap at majorite-rich compositions develop- ing as a consequence of the cubic/tetragonal, $Ia\overline{3}d \ll \gg I4_{1}/a$, phase transformation. Although this transformation has been observed experimentally (e.g. Heinemann et al. 1997), the miscibility gap has not been reported. This lack of experimental evidence weakens the conclusions of the study of Vinograd et al. (2006). However, the experimental confirmation of the existence of a miscibility gap is possible only when both the exsolved phases are stable with respect to an alternative mineral assemblage. Phase equilibrium calculations of Gasparik (2003) and Fabrichnaya et al. (2004) show that majorite-rich garnet is unstable with respect to various high-pressure assemblages (e.g. pyrope-rich garnet + high-pressure entstatite, wads- leyite + stishovite, and ilmenite) up to very high tem- peratures. Thus, the existence of a miscibility gap in the pyrope-majorite system can be confirmed only above 2,000 K, where garnets of pure majorite composition become stable together with more pyrope-rich varieties.

It is well known that phase transformations in germanates mirror the transformations in silicates, but occur at more easily accessible pressure and tempera- ture intervals (e.g. Ringwood and Seabrook 1963; Ross et al. 1986). Iezzi et al. (2005) have recently observed the cubic/tetragonal transformation associated with a miscibility gap in $Ca_{3}Fe_{2}Ge_{3}O_{12}-Ca_{4}Ge_{4}O_{12}$ system at 900 and $1,100^{\circ}C$. The $Ca_{3}Fe_{2}Ge_{3}O_{12}-Ca_{4}Ge_{4}O_{12}$ solid solution is a complete structural analogue of pyrope- majorite garnets. Thus, it is interesting to simulate the mixing properties in the Ca,Fe,Ge garnets with exactlythe same tools as in the study of Vinograd et al. (2006) and to compare the simulation results with the experi- mental data of Iezzi et al. (2005). This would permit a straightforward test of the simulation method. There- fore, the present study mirrors the simulations ofVinograd et al. (2006) in performing the following steps:

- Development of a set of transferable empirical in- teratomic potentials by fitting to structure and elas- ticity data of chemically similar minerals.
- Testing the potentials by comparing the predicted properties of a limited set of ordered structures with the results of quantum mechanical calculations.
- Static lattice energy calculations (SLEC) on a large set of structures with randomly varied cation con- figurations.
- Finding a simple equation that describes the energies of the simulated structures. This procedure is known as the 'cluster expansion'.
- Using the cluster expansion model to obtain tem- perature-dependent properties by Monte Carlo simulations.
- Calculation of the free energies of mixing and ordering by thermodynamic integration of the Monte Carlo results.

## Simulation procedure

### The empirical potentials

A set of the empirical interatomic potentials has been developed in this study using the relax-fitting proce- dure (Gale 1996) as implemented in the GULP pro- gram (Gale 1997; Gale and Rohl 2003). The procedure involves simultaneous SLEC on a number of chemi- cally similar structures. Within the procedure, the parameters of the empirical potential functions are varied in the search for the minimum in the discrep- ancy between the calculated and observed structure, energy and/or elasticity constraints. The set of poten- tials involves two-body metal-oxygen (M-O) Buck- ingham potentials, three-body O-M-O bond-bending terms, and the shell model for the oxygen polarizabil- ity, as described by Sanders et al. (1984), Patel et al.(1991), and Winkler et al. (1991). Following Vinograd et al. (2004a), we have multiplied formal cation and anion charges by the common factor 0.85, so that the charges of 2-, 3-, and 4-valent ions have been reduced to the values of 1.7, 2.55, and 3.4, respectively. Such a reduction has already permitted the development of a set of potentials for the Mg-Al-Si-O system (Vinograd et al. 2006), which showed good transferability within a large number of silicate and aluminosicate structures of different density. The O(shell)-O(shell) and O(shell)- O(core) potentials have been taken from the study of Vinograd et al. (2006). The Buckingham Ge(core)- O(shell) potential has been fitted to the structures of Ca-Ge-majorite (Nakatsuka et al. 2005), Ca-Ge- perovskite (Sasaki et al. 1983), Ge-forsterite and Mg- Ge-spinel (Von Dreele et al. 1977; Weidner and Ha- maya 1983), Mg-Ge-ilmenite (Yamanaka et al. 2005), and to both structural data and elastic stiffness con- stants of $GeO_{2}$ with the rutile structure (Heines et al.2000; Wang and Simmons 1973). The Fe-O potential has been fitted to the structure and elasticity data for hematite (Gualtieri and Venturelli 1999; Liebermann and Schreiber 1968) and andradite (Hazen and Finger1989; Bass 1986), and to the structure of Ge-andradite(Lévy and Barbier 1999). The $Ca^{[6,8]}-O$ potential has been fitted to the structure data for larnite (Midgley

![](./images/812049252522917890_2.jpg)

1952), Ca-Tschermak pyroxene (Okamura et al. 1974) and to the structure and elasticity data of grossular (Geiger and Armbruster 1997; Bass 1995), anorthite (Angel et al. 1990; Bass 1995) and lime (Fiquet et al. 1999; Bass 1995). The potential set for Ca-Mg-Si-Ge-Al-Fe³⁺-O system is given in Table 1. Tables 2, 3, and 4 compare the predicted and observed structural and elastic properties of Ca-Ge-majorite, Ge-andradite, and andradite.

Quantum mechanical calculations as a test for the accuracy of the potentials

While calculations based on empirical potentials are computationally very efficient, the predictive power of this approach cannot be guaranteed a priori, and therefore requires further validation. Here, we compare selected SLEC results with parameter-free quantum mechanical calculations. For crystals, most modern calculations are based on the density functional theory (DFT) (Hohenberg and Kohn 1964; Kohn and Sham 1965; Parr and Yang 1989; Jones and Gunnarsson 1989; Kryachko and Ludena 1990). While DFT itself is exact (Hohenberg and Kohn 1964), practical calculations require an approximation for the treatment of the exchange and correlation energies. Here, we use the generalized gradient approximation (GGA), in the form suggested by Perdew et al. (1996). Results based on GGA calculations are generally in better agreement with experiment than those obtained with the local density approximation (Leung et al.

<table>
<caption>Table 1 The empirical interatomic potentials used in the study</caption>
<tbody>
<tr>
<td>Buckingham</td>
<td>A (eV)</td>
<td>B (Å)</td>
<td>C (eV Å⁶)</td>
</tr>
<tr>
<td>Fe[6]–O(shell)</td>
<td>691.1103</td>
<td>0.335602</td>
<td>0.0</td>
</tr>
<tr>
<td>Al[4,6]–O(shell)</td>
<td>1,262.2081</td>
<td>0.286370</td>
<td>0.0</td>
</tr>
<tr>
<td>Mg[6,8]–O(shell)</td>
<td>1,432.8544</td>
<td>0.277265</td>
<td>0.0</td>
</tr>
<tr>
<td>Si[4,6]–O(shell)</td>
<td>1,073.4668</td>
<td>0.298398</td>
<td>0.0</td>
</tr>
<tr>
<td>Ca[6,8]–O(shell)</td>
<td>2,707.5868</td>
<td>0.282668</td>
<td>0.0</td>
</tr>
<tr>
<td>Ge[4,6]–O(shell)</td>
<td>1,011.0577</td>
<td>0.317520</td>
<td>0.0</td>
</tr>
<tr>
<td>O(shell)–O(shell)</td>
<td>598.8996</td>
<td>0.314947</td>
<td>26.89746</td>
</tr>
<tr>
<td>Spring</td>
<td colspan="3">K (eV Å⁻²)</td>
</tr>
<tr>
<td>O(core)–O(shell)</td>
<td colspan="3">56.5598</td>
</tr>
<tr>
<td>Three-body</td>
<td>Q (eV deg⁻²)</td>
<td></td>
<td>G (deg)</td>
</tr>
<tr>
<td>O(shell)–Ge[4]–O(shell)</td>
<td>0.11167</td>
<td></td>
<td>109.47</td>
</tr>
<tr>
<td>O(shell)–Ge[6]–O(shell)</td>
<td>0.89061</td>
<td></td>
<td>90.0</td>
</tr>
<tr>
<td>O(shell)–Fe[6]–O(shell)</td>
<td>1.6284</td>
<td></td>
<td>90.0</td>
</tr>
<tr>
<td>O(shell)–Si[4]–O(shell)</td>
<td>0.77664</td>
<td></td>
<td>109.47</td>
</tr>
<tr>
<td>O(shell)–Si[6]–O(shell)</td>
<td>2.2955</td>
<td></td>
<td>90.0</td>
</tr>
<tr>
<td>O(shell)–Al[4]–O(shell)</td>
<td>1.2883</td>
<td></td>
<td>109.47</td>
</tr>
<tr>
<td>O(shell)–Al[6]–O(shell)</td>
<td>1.8807</td>
<td></td>
<td>90.0</td>
</tr>
</tbody>
</table>

The charges on the oxygen core and shell are 0.746527 and –2.446527, respectively. Cut-off distance for the Buckingham potentials is 12 Å

<table>
<caption>Table 2 Structural and elastic constants for Ca-Ge-majorite predicted with the SLEC and DFT GGA in the comparison with the experimental data</caption>
<tbody>
<tr>
<td>Cell parameters</td>
<td>XRD</td>
<td>SLEC</td>
<td>DFT</td>
</tr>
<tr>
<td>A (Å)</td>
<td>12.535ª</td>
<td>12.539</td>
<td>12.679</td>
</tr>
<tr>
<td>C (Å)</td>
<td>12.37ª</td>
<td>12.34</td>
<td>12.527</td>
</tr>
<tr>
<td>a/c</td>
<td>1.013ª</td>
<td>1.015</td>
<td>1.012</td>
</tr>
<tr>
<td>V (Å³)</td>
<td>1,943.65ª</td>
<td>1,940.47</td>
<td>2,013.77</td>
</tr>
<tr>
<td>Atomic coordinates</td>
<td>XRDª</td>
<td>SLEC</td>
<td>DFT</td>
</tr>
<tr>
<td>Ca1 16f</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.1246</td>
<td>0.1251</td>
<td>0.1243</td>
</tr>
<tr>
<td>y</td>
<td>0.0030</td>
<td>0.0076</td>
<td>0.0045</td>
</tr>
<tr>
<td>z</td>
<td>0.2531</td>
<td>0.2567</td>
<td>0.2527</td>
</tr>
<tr>
<td>Ca2 8e</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.0000</td>
<td>0.0000</td>
<td>0.0000</td>
</tr>
<tr>
<td>y</td>
<td>0.2500</td>
<td>0.2500</td>
<td>0.2500</td>
</tr>
<tr>
<td>z</td>
<td>0.6232</td>
<td>0.6245</td>
<td>0.6225</td>
</tr>
<tr>
<td>Ca3 8c</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.0000</td>
<td>0.0000</td>
<td>0.0000</td>
</tr>
<tr>
<td>y</td>
<td>0.0000</td>
<td>0.0000</td>
<td>0.0000</td>
</tr>
<tr>
<td>z</td>
<td>0.5000</td>
<td>0.5000</td>
<td>0.5000</td>
</tr>
<tr>
<td>Ge1 4a</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.0000</td>
<td>0.0000</td>
<td>0.0000</td>
</tr>
<tr>
<td>y</td>
<td>0.2500</td>
<td>0.2500</td>
<td>0.2500</td>
</tr>
<tr>
<td>z</td>
<td>0.3750</td>
<td>0.3750</td>
<td>0.3750</td>
</tr>
<tr>
<td>Ge2 4b</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.0000</td>
<td>0.0000</td>
<td>0.0000</td>
</tr>
<tr>
<td>y</td>
<td>0.2500</td>
<td>0.2500</td>
<td>0.2500</td>
</tr>
<tr>
<td>z</td>
<td>0.8750</td>
<td>0.8750</td>
<td>0.8750</td>
</tr>
<tr>
<td>Ge3 16f</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.1265</td>
<td>0.1266</td>
<td>0.1265</td>
</tr>
<tr>
<td>y</td>
<td>0.0151</td>
<td>0.0166</td>
<td>0.0147</td>
</tr>
<tr>
<td>z</td>
<td>0.7572</td>
<td>0.7595</td>
<td>0.7567</td>
</tr>
<tr>
<td>Ge4 8d</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.0000</td>
<td>0.0000</td>
<td>0.0000</td>
</tr>
<tr>
<td>y</td>
<td>0.0000</td>
<td>0.0000</td>
<td>0.0000</td>
</tr>
<tr>
<td>z</td>
<td>0.0000</td>
<td>0.0000</td>
<td>0.0000</td>
</tr>
<tr>
<td>O1 16f</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.0309</td>
<td>0.0301</td>
<td>0.0297</td>
</tr>
<tr>
<td>y</td>
<td>0.0662</td>
<td>0.0650</td>
<td>0.0657</td>
</tr>
<tr>
<td>z</td>
<td>0.6713</td>
<td>0.6750</td>
<td>0.6704</td>
</tr>
<tr>
<td>O2 16f</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.0430</td>
<td>0.0460</td>
<td>0.0417</td>
</tr>
<tr>
<td>y</td>
<td>0.9581</td>
<td>0.9622</td>
<td>0.9562</td>
</tr>
<tr>
<td>z</td>
<td>0.8614</td>
<td>0.8639</td>
<td>0.8601</td>
</tr>
<tr>
<td>O3 16f</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.2226</td>
<td>0.2239</td>
<td>0.2243</td>
</tr>
<tr>
<td>y</td>
<td>0.1108</td>
<td>0.1115</td>
<td>0.1105</td>
</tr>
<tr>
<td>z</td>
<td>0.8055</td>
<td>0.8043</td>
<td>0.8068</td>
</tr>
<tr>
<td>O4 16f</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.2103</td>
<td>0.2089</td>
<td>0.2123</td>
</tr>
<tr>
<td>y</td>
<td>0.9224</td>
<td>0.9234</td>
<td>0.9211</td>
</tr>
<tr>
<td>z</td>
<td>0.6997</td>
<td>0.7043</td>
<td>0.7004</td>
</tr>
<tr>
<td>O5 16f</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.9328</td>
<td>0.9344</td>
<td>0.9331</td>
</tr>
<tr>
<td>y</td>
<td>0.1668</td>
<td>0.1675</td>
<td>0.1663</td>
</tr>
<tr>
<td>z</td>
<td>0.4663</td>
<td>0.4653</td>
<td>0.4674</td>
</tr>
<tr>
<td>O6 16f</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x</td>
<td>0.8965</td>
<td>0.8964</td>
<td>0.8973</td>
</tr>
<tr>
<td>y</td>
<td>0.2098</td>
<td>0.2164</td>
<td>0.2090</td>
</tr>
<tr>
<td>z</td>
<td>0.7844</td>
<td>0.7873</td>
<td>0.7836</td>
</tr>
</tbody>
</table>

ªNakatsuka et al. (2005)

![](./images/812049252522917890_3.jpg)

<table>
<caption>Table 3 Structural constants for Ge-andradite predicted with the SLEC in the comparison with the experimental data</caption>
<tbody>
<tr>
<td>Cell parameters</td>
<td>XRD</td>
<td>SLEC</td>
</tr>
<tr>
<td>$a$ (Å)</td>
<td>12.321ª</td>
<td>12.341</td>
</tr>
<tr>
<td>$V$ (Å³)</td>
<td>1,870.415ª</td>
<td>1,879.318</td>
</tr>
<tr>
<td>Atomic coordinates</td>
<td>XRDª</td>
<td>SLEC</td>
</tr>
<tr>
<td>O 96h</td>
<td></td>
</tr>
<tr>
<td>$x$</td>
<td>0.0342</td>
<td>0.0351</td>
</tr>
<tr>
<td>$y$</td>
<td>0.0510</td>
<td>0.0469</td>
</tr>
<tr>
<td>$z$</td>
<td>0.6517</td>
<td>0.6522</td>
</tr>
</tbody>
</table>

ªLévy and Barbier (1999)

<table>
<caption>Table 4 Structural and elastic constants for andradite predicted with the SLEC in the comparison with available experimental data</caption>
<tbody>
<tr>
<td>Cell parameters</td>
<td>XRD</td>
<td>SLEC</td>
</tr>
<tr>
<td>$a$ (Å)</td>
<td>12.051;ª 12.031ᵇ</td>
<td>12.10</td>
</tr>
<tr>
<td>$V$ (Å³)</td>
<td>1,750.126;ª 1,741.427ᵇ</td>
<td>1,771.658</td>
</tr>
<tr>
<td>Atomic coordinates</td>
<td>XRDª</td>
<td>SLEC</td>
</tr>
<tr>
<td>O 96h</td>
<td></td>
</tr>
<tr>
<td>$x$</td>
<td>0.0391</td>
<td>0.0388</td>
</tr>
<tr>
<td>$y$</td>
<td>0.0489</td>
<td>0.0471</td>
</tr>
<tr>
<td>$z$</td>
<td>0.6553</td>
<td>0.6546</td>
</tr>
<tr>
<td>Elastic constants</td>
<td>Observed (GPa)</td>
<td>SLEC (GPa)</td>
</tr>
<tr>
<td>$C_{11}$</td>
<td>289.0ᶜ</td>
<td>270.0</td>
</tr>
<tr>
<td>$C_{44}$</td>
<td>85.0ᶜ</td>
<td>81.5</td>
</tr>
<tr>
<td>$C_{12}$</td>
<td>92.0ᶜ</td>
<td>87.9</td>
</tr>
<tr>
<td>Bulk modulus</td>
<td>157.0ᶜ</td>
<td>148.6</td>
</tr>
</tbody>
</table>

ªArmbruster and Geiger (1993)
ᵇHazen and Finger (1989)
ᶜBass (1986)

1991; Holdender et al. 1996; Hamman 1996). The study of structures with large unit cells requires a computa-tionally efficient approach. Here, we use the compu-tational scheme in which the charge density and electronic wavefunctions are expanded in a basis set of plane waves. To avoid explicit description of tightly bound core electrons, the approach employs ‘ultrasoft’ pseudopotentials (Vanderbilt 1990; Kresse and Hafner 1994), which mimic the screening of the Coulomb po-tential of the nucleus by the core electrons.

Both the academic and commercial versions of CASTEP were used in the present study. Calculations were performed for ordered structures of Ca–Ge-majorite with the tetragonal, $I4_1/a$, and cubic, $P4_132$, symmetries using the primitive cell. The $k$-point sampling was performed using a $4 × 4 × 4$ Monkhorst–Pack grid in the first Brillouin zone. The cut-off energy for the plane wave expansion was 380 eV. In these calculations, all symmetry independent structural parameters were varied simultaneously in the search for the ground state geometry. The parameters of the ‘relaxed’ (optimized) $I4_1/a$ structure are given in Table 2, where they are compared to experimental values and to the results of the calculations based on the empirical potentials. Figure 1 shows the correlation between the experimentally observed and predicted cation–oxygen distances. Both the ab initio and the SLEC predicted structural parameters are in good agreement with the experimental data of Nakatsuka et al. (2005).

Although absolute values of lattice energies pre-dicted with ab initio and SLEC calculations cannot be compared, the energy differences between the config-urations of the same composition should be consistent. The difference in energies of the cubic $P4_132$ and tetragonal $I4_1/a$ majorites constitutes 0.138 eV per octahedral cation (13.29 kJ per mole of octahedral cations) and 0.082 eV (7.94 kJ/mol) for the SLEC and ab initio calculations, respectively. These values are in a reasonably good agreement with each other. This suggests that the potentials are able to predict realistic energy differences between structures with different ordering schemes. However, the lower value calculated with the DFT GGA method indicates that the empir-ical approach might slightly overestimate the real effect of disorder.

![](./images/812049252522917890_4.jpg)

Fig. 1 The correlation between theoretically calculated and experimentally observed cation–anion distances in $I4_1/a$ Ca–Ge-majorite. The circles and crosses denote the DFT GGA and SLEC results, respectively. The experimental data are from Nakatsuka et al. (2005)

![](./images/812049252522917890_5.jpg)

### Supercell calculations

The SLEC calculations have been performed in the athermal limit employing a $2 \times 2 \times 2$ supercell (128 octahedral sites) for a set of specially constructed structures (configurations) with different compositions and ordering states. In the first set of calculations, the pressure was fixed at 0 GPa. We have started with the ordered octahedral arrangement of Ca and Ge mirroring the Mg/Si arrangement in $I4_1/a$ majorite (Angel et al. 1989), and calculated its relaxed energy. The relaxed coordinates have been used as starting values for a new structure in which one randomly chosen pair of Ca and Ge was swapped. The swapping has been repeated 60 times. In this exercise, the static energy increased sharply during the first steps. Then, the increase slowed down, indicating the approach to a random distribution. The 60 generated structures with variable degrees of disorder have been added to the data base. The same procedure has been repeated for structures with the compositions $x_{\text{maj}} = 0.75$, $x_{\text{maj}} = 0.50$, and $x_{\text{maj}} = 0.25$ ($x_{\text{maj}}$ denotes mole fraction of Ca–Ge majorite), which have been prepared from $I4_1/a$ Ca–Ge-majorite by replacing appropriate numbers of Ca and Ge with Fe atoms. The whole set of configurations was used again in the next set of SLEC calculations at 10 GPa.

### Cluster expansion

The aim of the cluster expansion is to find a simple equation which fits the energies of all simulated configurations and, hopefully, predicts the energy of any other possible configuration. One popular form for such an expansion is known as the $J$s formalism (e.g. Bosenick et al. 2001 and references therein):

$$
E_{i} \approx \frac{1}{2} \sum_{l \neq m} \sum_{n} z^{(n)} P_{lm^{(n)}} J_{lm^{(n)}} + E_{0} \tag{1}
$$

where $z^{(n)}$, $P_{lm^{(n)}}$ and $J_{lm^{(n)}}$ are the coordination numbers, frequencies of $lm$-type pairs (CaGe, CaFe and FeGe), and ordering constants for pairs of the order $n$. The $J_{lm^{(n)}}$ values correspond to the energy of the exchange reaction $ll + mm = 2lm$ between atoms $l \in \{\text{Fe}, \text{Ca}, \text{Ge}\}$ and $m \in \{\text{Fe}, \text{Ca}, \text{Ge}\}$ located at the $n$th distance. $E_0$ denotes a part of the excess energy, which is assumed to be independent of the arrangement of the exchangeable cations. When this equation is applied to the excess energies of the structures with the same composition, the $E_0$ is observed to vary with the composition. In solid solutions with charge mismatch, the $E_0$ term includes the deformation energy of the lattices of the end-members due to their adjustment to the intermediate lattice parameters at an intermediate composition (e.g. Vinograd et al. 2004b; Vinograd and Sluiter 2006). In solid solutions with coupled substitutions, $E_0$ is observed to correlate with the charge mismatch (Vinograd et al. 2006). The largest value of the $E_0$ corresponds to the end-member composition (e.g. majorite), where the average charge difference of the exchangeable cations reaches a maximum. In order to allow for such a variation, we model the $E_0$ with a two-parameter equation:

$$
E_{0}=y_{1}y_{2}(y_{1}A_{12}+y_{2}A_{21}) \tag{2}
$$

where $y_2 = x_2/2 = x_{\text{maj}}/2$ and $y_1 = 1 - y_2$. This equation permits a non-zero value at the end-member (Ge-majorite) composition and accounts for the possible non-linear variation of the non-configurational term. However, the study of Vinograd et al. (2006) has shown that the cluster expansion (1) containing pair terms only was inadequate for the description of the Mg, Si distribution in the octahedral sites of majorite

Fig. 2 The $I4_1/a$ (a) and $C2/c$
(b) majorites viewed along
the fourfold axis of the
tetragonal phase. The
tetragonal symmetry is lost
when CaCaCaCa and
GeGeGeGe tetrahedral
clusters move away from the
centring $\text{Ge}^{[4]}$ atoms. This
image was prepared using the
GDIS software (adapted from
Fleming and Rohl 2005)

![](./images/812049252522917890_6.jpg)
![](./images/812049252522917890_7.jpg)

because it could not distinguish between $I4_1/a$ and $C2/c$ structures. The same problem is relevant for the Ca–Ge-analogue of majorite. The $C2/c$ majorite, having an identical distribution of the octahedral cations to that of $I4_1/a$ majorite, has a significantly higher excess energy. The difference is that in the $C2/c$ structure, the octahedral sublattice is shifted against the fixed sublattice of $Ge^{[4]}$ atoms (Fig. 2). This shift preserves the symmetry of the octahedral sublattice, but destroys the tetragonal symmetry of the lattice as a whole. The difference between the energies of $I4_1/a$ and $C2/c$ structures can be understood by considering interactions between the octahedral and tetrahedral sites. The octahedral cations in garnets form a perfect BCC lattice. The BCC lattice naturally splits into four-atom clusters of tetrahedral shape. Only one quarter of these tetrahedral clusters are centred on a $Si^{[4]}$ atom in majorite or on $Ge^{[4]}$ atom in its Ca–Ge-analogue. The other three quarters are vacant. This creates the situation where each local arrangement of four octahedral cations can be either centred on a Ge atom or not. These two possibilities correspond to different local energies. To allow for this difference, we introduce additional energetic constants, $Q_{ijkl}$, which correspond to the reactions of the type:

$$ijkl^{[\mathrm{Ge}]}=ijkl^{[\mathrm{Va}]}\tag{3}$$

The reactions can be interpreted as a ‘jump’ of a four-atom octahedral cluster $ijkl$ from a locality centred on $Ge^{[4]}$ to a locality centred on a vacancy. The cluster expansion thus takes the form:

$$
\begin{aligned}
E_{i} & \approx \frac{1}{2} \sum_{l \neq m} \sum_{n} z^{(n)} P_{l m^{(n)}} J_{l m^{(n)}}+\sum_{i, j, k, l} a_{i j k l}\left(P_{i j k l}^{\mathrm{Va}}-3 P_{i j k l}^{\mathrm{Ge}}\right) \\
& \times Q_{i j k l}+E_{0}
\end{aligned}\tag{4}
$$

The second term reflects the tendency of a tetrahedral group $ijkl$ to locate itself either around $Ge^{[4]}$ or an empty site. The $P_{ijkl}$ and $a_{ijkl}$ denote the probability and the multiplicity of the tetrahedral group $ijkl$. The factor of 3 is needed to equalize the numbers of the filled and vacant sites. There are 21 symmetrically and chemically distinct groups. Vinograd et al. (2006) noted that six arbitrarily chosen constants can be set to zero. The reduction to a 15-term expansion does not lead to any noticeable decrease in the accuracy of the fit as compared to the 21-term expansion. Each configuration, $i$, out of the set of 240 structures, has been thus characterized with a value of $E_{i}$, the composition variable, $x_{i}$, the frequencies of dissimilar pairs at eight distances, and with the frequencies of $ijkl$ clusters both centred on Ge-atoms and vacancies. This gave a system of 240 equations which has been solved with the least-squares method for the $24\ J_{lm^{(n)}}$ and $15\ Q_{ijkl}$ constants and for the $A_{12}$ and $A_{21}$ parameters. In order to improve the accuracy of the cluster expansion and to ensure that it predicts correct ground states, we have used a feedback algorithm, which was described in detail by Vinograd et al. (2006). This algorithm consists of alternating Monte Carlo annealing simulations and GULP energy minimization calculations (Fig. 3). The cation distribution is annealed within the small $2\times2\times2$ supercell at a low temperature consistently with the current values of $J_{lm^{(n)}}$ and $Q_{ijkl}$ constants. The Monte Carlo simulated configuration is used as an input for a new GULP calculation. The energy of this structure and the frequency numbers are added to the set of previously simulated structures. A new least-squares solution is obtained and the Monte Carlo annealing is repeated with the new values of $J_{lm^{(n)}}$and $Q_{ijkl}$, $A_{12}$ and $A_{21}$ parameters. Effectively, the algorithm adds a set of well-ordered structures to the original set of randomly varied structures. When a newly predicted structure is not the true ground state, the accuracy of the fit automatically decreases, and the ordering constants have to adjust to the new situation to make the sum of the squares smaller. The $J_{lm^{(n)}}$and $Q_{ijkl}$ constants continue to vary throughout the algorithm until the cluster-expanded energy of the low-energy configuration becomes consistent with the SLEC results. The final values of $J_{lm^{(n)}}$and $Q_{ijkl}$, $A_{12}$ and $A_{21}$ parameters calculated with this algorithm are listed in Table 5. The accuracy of the fit is illustrated in Fig. 4. We assume that the energy of any other possible configuration not included in the fit will be also accurately approximated by Eq. 4. This allows us to efficiently simulate the Boltzmann probability distribution of the octahedral atoms with the Monte Carlo method.

## Monte Carlo simulation

Monte Carlo simulations have been performed on a $4\times4\times4$ supercell with periodic boundary conditions

![](./images/812049252522917890_8.jpg)

Fig. 3 The feedback algorithm which improves the accuracy of the cluster expansion in predicting ground state configurations

![](./images/812049252522917890_9.jpg)

**Table 5** The parameters of
the cluster expansion
resulting of the fit

<table>
  <thead>
    <tr>
      <th>Distance
(Å)</th>
      <th colspan="3">Pair-wise energies</th>
      <th colspan="3"></th>
    </tr>
    <tr>
      <th></th>
      <th>Ca–Fe
0 GPa</th>
      <th>Fe–Ge</th>
      <th>Ca–Ge</th>
      <th>Ca–Fe
10 GPa</th>
      <th>Fe–Ge</th>
      <th>Ca–Ge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>4.9511</td>
      <td>-10.431</td>
      <td>–14.856</td>
      <td>–38.201</td>
      <td>–20.551</td>
      <td>–18.650</td>
      <td>–55.714</td>
    </tr>
    <tr>
      <td>5.7178</td>
      <td>-20.540</td>
      <td>–14.606</td>
      <td>–45.861</td>
      <td>–26.840</td>
      <td>–19.224</td>
      <td>–49.847</td>
    </tr>
    <tr>
      <td>8.0883</td>
      <td>-11.212</td>
      <td>–10.744</td>
      <td>–20.335</td>
      <td>–12.842</td>
      <td>–10.209</td>
      <td>–24.530</td>
    </tr>
    <tr>
      <td>9.4852</td>
      <td>-3.949</td>
      <td>–4.094</td>
      <td>–5.260</td>
      <td>–10.413</td>
      <td>–6.438</td>
      <td>–17.306</td>
    </tr>
    <tr>
      <td>9.9072</td>
      <td>-4.958</td>
      <td>–3.680</td>
      <td>–7.969</td>
      <td>–5.735</td>
      <td>–4.001</td>
      <td>–10.598</td>
    </tr>
    <tr>
      <td>11.4400</td>
      <td>-2.878</td>
      <td>–2.389</td>
      <td>–2.803</td>
      <td>–6.565</td>
      <td>–1.876</td>
      <td>–1.334</td>
    </tr>
    <tr>
      <td>12.4676</td>
      <td>-3.123</td>
      <td>–1.887</td>
      <td>1.225</td>
      <td>–5.224</td>
      <td>–2.847</td>
      <td>–1.114</td>
    </tr>
    <tr>
      <td>12.7916</td>
      <td>-2.293</td>
      <td>–1.756</td>
      <td>–2.882</td>
      <td>–2.633</td>
      <td>–1.362</td>
      <td>–2.000</td>
    </tr>
    <tr>
      <td>Parameter</td>
      <td colspan="2">The non-configura-
tional term</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>0 GPa</td>
      <td>10 GPa</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$A_{12}$</td>
      <td>643.89</td>
      <td>964.66</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$A_{21}$</td>
      <td>676.44</td>
      <td>931.45</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cluster type</td>
      <td colspan="2">Quaternary energies</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>0 GPa</td>
      <td>10 GPa</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CaCaCaGe</td>
      <td>–4.661</td>
      <td>–5.068</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CaGeCaGe</td>
      <td>–15.165</td>
      <td>–18.300</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CaGeGeGe</td>
      <td>–4.129</td>
      <td>–5.132</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FeFeFeGe</td>
      <td>2.405</td>
      <td>4.474</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FeFeGeGe</td>
      <td>5.700</td>
      <td>10.071</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FeGeFeGe</td>
      <td>–1.946</td>
      <td>–1.836</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FeGeGeGe</td>
      <td>1.1486</td>
      <td>4.634</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FeFeFeCa</td>
      <td>–1.567</td>
      <td>–3.807</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FeFeCaCa</td>
      <td>0.327</td>
      <td>–1.650</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FeCaFeCa</td>
      <td>–7.722</td>
      <td>–15.942</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FeCaCaCa</td>
      <td>–2.159</td>
      <td>–6.740</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CaFeGeGe</td>
      <td>1.416</td>
      <td>3.307</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CaGeFeGe</td>
      <td>–6.076</td>
      <td>–7.490</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FeGeCaCa</td>
      <td>0.055</td>
      <td>0.079</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FeCaGeCa</td>
      <td>–9.799</td>
      <td>–10.064</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

The values are in kJ per mol
of octahedral cations, or per
1.5 mol of $Ge^{[4]}$ atoms

![](./images/812049252522917890_10.jpg)

**Fig. 4** Correlation between the energies calculated within the
static lattice energy calculation approach and those predicted
with the $J$–$Q$ expansion

(1,024 octahedral sites) with our own code. The swapping of sites has been performed according to the Metropolis algorithm, with the energy differences between subsequent steps being calculated using Eq. 4. The temperature-dependent properties have been calculated for a grid of 32 different compositions across the pyrope–majorite binary in the interval of 1,073–3,673 K with the step of 200 K. Each point in the $T$–$X$ space was annealed for two million Monte Carlo steps, and an additional two million steps were used for the calculation of the averages. The whole procedure was repeated twice, with the $J$–$Q$ sets corresponding to 0 and to 10 GPa. The results of both calculation sets are qualitatively similar, and therefore we plot only the 10- GPa set. Figure 5 shows the isotherms of the excess configurational enthalpy together with the original set of energies calculated with GULP. It is clear that even at 3,673 K, the octahedral distribution significantly deviates from random and that Ca–Ge-majorite remains essentially ordered within the temperature range studied.

![](./images/812049252522917890_11.jpg)

![](./images/812049252522917890_12.jpg)

Fig. 5 The excess energies of the sampled structures (circles) and the enthalpy of disorder predicted with Monte Carlo simulation (solid lines). All values are per mole of formula units with one octahedral atom (six oxygens)

### Thermodynamic integration

It has been shown (Myers et al. 1998; Myers 1999; Warren et al. 2001) that the configurational free energy can be calculated from Monte Carlo averaged excess energies using the method of thermodynamic integration:

$$
F=F_{0}+\int_{0}^{\lambda}\langle E\rangle_{\lambda} \mathrm{d} \lambda
\tag{5}
$$

In this equation, $F_{0}$ corresponds to the free energy of mixing of the solid solution with zero ordering energy, which can be calculated theoretically:

$$
F_{0}=R T\left(x_{\mathrm{Ca}} \ln x_{\mathrm{Ca}}+x_{\mathrm{Ge}} \ln x_{\mathrm{Ge}}+x_{\mathrm{Fe}} \ln x_{\mathrm{Fe}}\right)
\tag{6}
$$

The integral describes the contribution to the free energy from the internal energy (or the enthalpy in the case of a non-zero pressure), $\langle E\rangle_{\lambda}$, when it changes from the state of complete disorder to the state of equilibrium order. To calculate $\langle E\rangle_{\lambda}$ for a state with an intermediate degree of order defined by certain value of $\lambda$, $0<\lambda<1$, one scales the $J s$ and $Q s$:

$$
J_{n}^{\lambda}=\lambda J_{n}, \quad Q_{i j k l}^{\lambda}=\lambda Q_{i j k l}
\tag{7}
$$

and simulates a Boltzmann distribution constrained with $J_{n}^{\lambda}$ and $Q_{i j k l}^{\lambda}$. Effectively, the scaling implies that the probabilities of microstates become more random than in the non-scaled case. $\langle E\rangle_{\lambda}$ is then calculated using Eq. 4 with nominal (not scaled) values of $J s$ and $Q s$ by taking a simple average over a sufficient number of the equilibrated configurations. The scaling thus makes the distribution more random, but does not affect the strength of the interactions. In our simulations, $\lambda$ was gradually increased from 0 to 1 with a step size of 0.04. The integral was calculated using Simpson's method. The configurational entropy was calculated with the equation:

$$
S=\frac{F-\langle E\rangle}{T}
\tag{8}
$$

where $\langle E\rangle$ is the average excess internal energy (or enthalpy) calculated with $\lambda=1$. Figure 6 shows the configurational entropy in the interval of 1,073-3,673 K. This function reflects various short-range and long-range order phenomena. The configurational entropy of Ca-Ge-majorite remains close to zero even up to very high temperatures. An additional calculation over a wider temperature interval has shown that the order/disorder transition at the majorite composition under an applied pressure of 0 GPa occurs at 4,273 K. It is also clear that some sort of ordering occurs for the 50/50 compositions at temperatures below 1,073 K. Figure 7 shows the free energy of mixing at 0 GPa in the interval of 1,073-3,673 K. The analysis of the

![](./images/812049252522917890_13.jpg)

Fig. 6 The configurational entropy of the octahedral site (per 1 mol of octahedral atoms) calculated using the method of thermodynamic integration. The dashed line shows the entropy of ideal mixing

![](./images/812049252522917890_14.jpg)

![](./images/812049252522917890_15.jpg)

Fig. 7 The free energy of mixing and ordering calculated using the method of thermodynamic integration

curvature of the free energy of mixing isotherms makes it possible to outline the miscibility gap (Fig. 8). At zero pressure, the gap starts to develop at about 3,500 K and $x_{\text{maj}} = 0.8$, and widens with the decrease in the temperature. A similar thermodynamic analysis performed at 10 GPa shows that the gap widens with pressure. Similarly, a decrease in the miscibility with pressure has been predicted by Vinograd et al. (2006) for the pyrope-majorite system.

![](./images/812049252522917890_16.jpg)

Fig. 8 The temperature-composition phase diagram of $Ca_3Fe_2$-$Ge_3O_{12}$-$Ca_4Ge_4O_{12}$ garnets calculated based on the results of the Monte Carlo simulations. The solid black curve shows the result at zero pressure, the dashed line shows the phase boundaries at 10 GPa. Arrows show the limits of the miscibility gap according to the experimental results of Iezzi et al. (2005) at 7 GPa

## Discussion

The present calculations explore the mixing properties of the $Ca_3Fe_2Ge_3O_{12}$-$Ca_4Ge_4O_{12}$ system over a wide range of $P$-$T$ space. A significant part of this space corresponds to the miscibility gap. Consistent with the results of Iezzi et al. (2005), the gap is shifted to Fe-pure compositions. However, its limits appear to be wider than those observed experimentally. It is possible that the empirical calculations overestimate the tendency towards unmixing. This explanation would be consistent with the smaller energy difference between the cubic $P4_132$ and tetragonal $I4_1/a$ majorites predicted by the present ab initio calculations. Another explanation can be offered by considering the reported presence of a measurable amount of $Fe^{2+}$ in the experimental samples. The presence of the extra component in the solid solution increases its configurational entropy and decreases the tendency to phase separate. Evidently, the presence of $Fe^{2+}$ should have a stronger effect on the equilibrium composition of the Fe-rich phase. The latter explanation is consistent with the experimentally observed widening of the gap with increasing temperature (Fig. 8). Iezzi et al. (2005) have shown that the amount of $Fe^{2+}$ in the samples annealed at $1,100^\circ\text{C}$ was considerably smaller than in the $900^\circ\text{C}$ runs. The complete avoidance of $Fe^{2+}$ would further widen the gap and bring its limits to near perfect agreement with our simulations.

The present results, together with the recent ones of Vinograd et al. (2006), show that the tendency towards unmixing in the $Ca_3Fe_2Ge_3O_{12}$-$Ca_4Ge_4O_{12}$ system is comparable to that in the pyrope-majorite system. The order/disorder transition is predicted to lie at 3,300 K in Mg-Si-majorite (Vinograd et al. 2006), while in its Ca-Ge-analogue, it occurs at about 4,300 K. The comparable values of the critical temperatures are consistent with the very similar energies of disorder in both systems. To compare the energy differences between ordered and disordered states in Ca-Ge- and Mg-Si-majorites, we have performed additional SLEC on a set of 60 configurations within a $2\times2\times2$ supercell. These configurations differ in the average degree of disorder, but there is an exact correspondence between Mg-Si and Ca-Ge configurations. In each pair of Ca-Ge and Mg-Si configurations, Ca, Ge and Mg, Si occupy exactly the same positions. Figure 9 plots the energies of Ca-Ge configurations against the energies

![](./images/812049252522917890_17.jpg)

of Mg-Si configurations. There is a perfect correlation between the two sets. The energies of all Mg-Si con- figurations are larger than the energies of the corre- sponding Ca-Ge configurations by the same factor of about 1.2. If the constant factor of 1.2 is applicable to any pair of configurations in Mg-Si and Ca-Ge maj- orites, then the Mg-Si system would exhibit identical thermodynamic behaviour to the Ca-Ge system at a temperature that is 1/1.2 times lower. This is what the calculations predict. The transition temperature in the Mg-Si-majorite is about 80% lower than in Ca- Ge-majorite. The similar correlation also holds for the predicted magnitudes of the enthalpy of mixing. Due to the stronger tendency to order in the Ca-Ge-majorite, the enthalpy of mixing is larger in the Ca-Fe-Ge sys- tem. This explains the slightly wider miscibility gap predicted for the Ca-Fe-Ge garnets in comparison to that calculated for Mg-Al-Si garnets.

The present results are also interesting from a purely theoretical point of view. The influence of high pres- sures on mixing properties of solid solutions remains poorly characterised. Here, we have shown that a 10-GPa pressure can significantly affect the phase separation, not merely via the excess volume, but via its direct influence on the enthalpy of ordering and on the enthalpy of mixing. We observe that the magni- tudes of pair-wise and quaternary ordering interactions significantly increase with pressure (Table 5). Obvi- ously, the ordering interactions become affected by the increased stiffness of the structure. In a stiffer lattice, the unfavourable pairs of Ca-Ca and Ge-Ge, which are either too long or too short for the average octa- hedral distances in Ca-Ge-majorite, experience a lar- ger strain. Thus, the tendency for the formation of dissimilar Ca-Ge pairs becomes stronger. This ten- dency is reflected in the values of the $J$s, which become more negative with pressure. At the same time, we observe that the size mismatch has only a minor influence on the magnitude of the $J$s. From Table 5, one can see that the magnitudes of the $J$s are strong functions of the charge difference. The strongest interactions correspond to Ca-Ge pairs, which have the formal charge difference of 2 a.u. Ca-Fe and Fe- Ge pairs, which both have the charge difference of 1 a.u., have consistently smaller magnitudes. Similar observations on the magnitudes of Mg-Al, Al-Si, and Mg-Si interactions have been reported by Vinograd et al. (2006). This domination of the charge mismatch effect explains the very similar energies of disorder in Ca-Ge- and Mg-Si-majorites (Fig. 9).

![](./images/812049252522917890_18.jpg)

Fig. 9 The energy of disordered configurations of Ca- Ge-majorite versus the energies of the same configurations of Mg-Si-majorite. The energies are plotted relative to the ordered $I4_1/a$ structures of Ca-Ge- and Mg-Si-majorites, respectively. The dashed line shows 1:1 correlation. The calculations are at zero pressure

Considering the very small difference in the ther- modynamic behaviour of both systems, it is clear that the mixing phenomena in the pyrope-grossular system cannot be qualitatively different from those in the $Ca_3Fe_2Ge_3O_{12}$-$Ca_4Ge_4O_{12}$ system. Thus, the finding of a miscibility gap in $Ca_3Fe_2Ge_3O_{12}$-$Ca_4Ge_4O_{12}$ garnets implies that a similar gap must exist in the $Mg_3Al_2$ $Si_3O_{12}$-$Mg_4Si_4O_{12}$ system.

## Conclusions
We have shown that modern simulation tools permit the realistic modelling of mixing effects in a solid solution with a complex coupled substitution mecha- nism. The missing thermodynamic information can be extracted from the structure and elasticity data on chemically similar compounds using SLEC mediated by a transferable set of interatomic empirical poten- tials. The simulated mixing effects in $Ca_3Fe_2Ge_3O_{12}$-$Ca_4Ge_4O_{12}$ garnets agree well with the experimental results of Iezzi et al. (2005). Our results, and the results of Iezzi et al. (2005), favour the existence of a wide miscibility gap separating cubic and tetragonal garnets. The predicted analogy between the mixing effects in Ca-Fe-Ge and Mg-Al-Si garnets suggests that a sim- ilar miscibility gap must exist for $Mg_3Al_2Si_3O_{12}$-$Mg_4Si_4O_{12}$ garnets, although at slightly lower temper- atures. This supports the activity-composition model of Vinograd et al. (2006) for the pyrope-majorite

binary. The predicted non-ideality of the garnet phase associated with the cubic/tetragonal transition should be taken into account in petrological models of the lower interval of the transition zone.

Acknowledgments Some of the results included in this publi- cation have been developed as illustration materials during the lecture course 'Introduction to Computer Simulations of Min- erals' read during the Spring semester 2005 at the University of Münster by AP and VLV. U. Hans, J. Hansmann, E. Hoffman, A. Janßen, and D. Niedermeier are thanked for the active par- ticipation in the course and for the help in the calculations. This project is funded by the Deutsche Forschungsgemeinschaft (grant Wi 1232/14-2). JDG would like to thank the Government of Western Australia for funding under the Premier's Research Fellowship program.

References

Akaogi M, Akimoto S (1977) Pyroxene-garnet solid solution equilibria in the systems $Mg_4Si_4O_4$–$Mg_3Al_2Si_3O_{12}$ and $Fe_4Si_4O_4$–$Fe_3Al_2Si_3O_{12}$ at high pressures and temperatures. Phys Earth Planet Inter 15:90–106

Akaogi M, Navrotsky A, Yagi T, Akimoto S (1987) Pyroxene- garnet transformation: thermochemistry and elasticity of garnet solid solutions, and applications to a pyrolite mantle. In: Manghnani MH, Syono Y (eds) High-pressure research in mineral physics. American Geophysical Union, Wash- ington, pp. 251–260

Angel RJ, Finger LW, Kanzaki M, Weidner DJ, Liebermann RC, Veblen DR (1989) Structure and twinning of single- crystal $MgSiO_3$ garnet synthesised at 17 GPa and $1800^\circ$C. Am Mineral 74:509–512

Angel RJ, Carpenter MA, Finger LW (1990) Structural varia- tion associated with compositional variation and order- disorder behavior in anorthite-rich feldspars. Am Mineral 75:150–162

Armbruster T, Geiger CA (1993) Andradite crystal chemistry, dynamic X-site disorder and structural strain in silicate garnets. Eur J Mineral 5:57–71

Bass JD (1986) Elasticity of uvarovite and andradite garnets. J Geophys Res 91:7505–7516

Bass JD (1995) Elasticity of minerals, glasses, and melts. In: Ahrens ThJ (ed) Mineral physics & crystallography. A handbook of physical constants. AGU Reference Shelf Ser 2, American Geophysical Union, Washington, pp. 45–63

Bosenick A, Dove MT, Myers ER, Palin EJ, Sainz-Diaz CI, Guiton BS, Warren MC, Craig MS, (2001) Computational methods for the study of energies of cation distributions: applications to cation-ordering phase transitions and solid solutions. Mineral Mag 65:193–219

Fabrichnaya OB, Saxena SK, Richet P, Westrum EF (2004) Thermodynamic data, models and phase diagrams in mul- ticomponent oxide systems. Springer, Berlin Heidelberg New York, p 198

Fiquet G, Richet P, Montagnac G (1999) High-temperature thermal expansion of lime, periclase, corundum and spinel. Phys Chem Miner 27:103–111

Fleming SD, Rohl AL (2005) GDIS: a visualization program for molecular and periodic systems. Z Kristallogr 220:580–584

Gale JD (1996) Empirical derivation of interatomic potentials for ionic materials. Philos Mag B 73:3–19

Gale JD (1997) GULP—a computer program for symmetry adapted simulations of solids. J Chem Soc: Faraday Trans 93:629–637

Gale JD, Rohl AL (2003) The General Utility Lattice Program (GULP). Mol Simul 29:291–341

Gasparik T (2003) Phase diagrams for geoscientists. An atlas of the Earth's interior. Springer, Berlin Heidelberg New York, p 462

Geiger CA, Armbruster T (1997) $Mn_3Al_2Si_3O_{12}$ spessartine and $Ca_3Al_2Si_3O_{12}$ grossular garnet: structural dynamics and thermodynamic properties. Am Mineral 82:740–747

Gualtieri A, Venturelli P (1999) In situ study of the goethite- hematite phase transformation by real time synchrotron powder diffraction. Am Mineral 84:895–904

Hamman DR (1996) Generalized gradient theory for silica phase transitions. Phys Rev Lett 76:660–663

Hazen RM, Finger LW (1989) High-pressure crystal chemistry of andradite and pyrope: revised procedures for high-pressure diffraction experiments. Am Mineral 74:352–359

Heinemann S, Sharp T, Seifert F, Rubie DC (1997) The cubic- tetragonal phase transition in the system majorite $(Mg_4Si_4O_{12})$–pyrope $(Mg_3Al_2Si_3O_{12})$, and garnet symmetry in the Earth's transition zone. Phys Chem Miner 24:206–221

Heines J, Leger JM, Chateau C, Pereira AS (2000) Structural evolution of rutile-type and $CaCl_2$-type germanium dioxide at high pressure. Phys Chem Miner 27:575–582

Hohenberg P, Kohn W (1964) Inhomogeneous electron gas. Phys Rev 136:B864–B871

Iezzi G, Boffa-Ballaran T, McCammon C, Langenhorst F (2005) The $CaGeO_3$–$Ca_3Fe_2Ge_3O_{12}$ garnet join: an experimental study. Phys Chem Miner 32:197–207

Jones RO, Gunnarsson O (1989) The density functional for- malism, its applications and prospects. Rev Mod Phys 61:689–746

Kanzaki M (1987) Ultrahigh-pressure phase relations in the system. Phys Earth Planet Inter 49:168–175

Kohn W, Sham LJ (1965) Self-consistent equations including exchange and correlation effects. Phys Rev 140:A1133– A1138

Kresse G, Hafner J (1994) Norm-conserving and ultrasoft pseudopotentials for first-row and transition elements. J Phys: Condens Matt 6:8245–8257

Kryachko ES, Ludena EV (1990) Energy density functional theory of many-electron systems. In: Understanding chem- ical reactivity, vol. 4. Kluwer Academic Publishers, Dord- echt

Leung TC, Chan CT, Harmon BN (1991) Ground-state proper- ties of Fe, Co, Ni and their monoxides: results of the gen- eralized gradient approximation. Phys Rev B44:2923–2927

Lévy D, Barbier J (1999) Normal and inverse garnets: $Ca_3Fe_2$ $Ge_3O_{12}$, $Ca_3Y_2Ge_3O_{12}$ and $Mg_3Y_2Ge_3O_{12}$. Acta Crystallo- graph C55:1611–1614

Liebermann RC, Schreiber E (1968) Elastic constants of poly- crystalline hematite as a function of pressure to 3 kilobars. J Geophys Res 73:6585–6590

Midgley CM (1952) The crystal structure of beta dicalcium sili- cate. Acta Crystallograph 5:307–312

Myers ER (1999) Al/Si ordering in silicate minerals. Ph.D. thesis, University of Cambridge

Myers ER, Heine V, Dove MT (1998) Some consequences of Al/ Al avoidance in the ordering of Al/Si tetrahedral framework structures. Phys Chem Miner 25:457–464

Nakatsuka A, Chaya H, Yoshiasa A (2005) Crystal structure of single-crystal tetragonal garnet synthesized at 3 GPa and $1000^\circ$C. Am Mineral 90:732–736

![](./images/812049252522917890_19.jpg)

Okamura FP, Ghose S, Ohashi H (1974) Structure and crystal chemistry of calcium Tschermak's pyroxene, CaAlAlSiO₆. Am Mineral 59:549–557

Parr RG, Yang W (1989) Density-functional theory of atoms and molecules. Oxford University Press, New York, p 342

Patel A, Price GD, Mendelsson MJ (1991) A computer-simula- tion approach to modeling the structure, thermodynamics and oxygen isotope equilibria of silicates. Phys Chem Miner 17:690–699

Perdew JP, Burke K, Ernzerhof M (1996) Generalized gradient approximation made simple. Phys Rev Lett 77:3865–3868

Ringwood AE, Seabrook M (1963) High-pressure transforma- tions in germinate pyroxenes and related compounds. J Geophys Res 68:4601–4609

Ross N, Akaogi M, Navrotsky A, Susaki JI, McMillan P (1986) Phase transitions among the CaGeO3 polymorphs (wollas- tonite, garnet and perovskite structures): studies by high- pressure synthesis, high-temperature calorimetry, and vibrational spectroscopy and calculation. J Geophys Res 91:4685–4696

Sanders MJ, Leslie M, Catlow CR (1984) Interatomic Potentials for SiO₂. J Chem Soc Chem Commun 19:1271–1273

Sasaki S, Prewitt CT, Liebermann RC (1983) The crystal struc- ture of CaGeO₃ perovskite and the crystal chemistry of the GdFeO₃-type perovsites. Am Mineral 68:1189–1198

Vanderbilt D (1990) Soft self-consistent pseudopotentials in a generalized eigenvalue formalism. Phys Rev B41:7894–7895

Vinograd VL, Sluiter MHF (2006) Thermodynamics of mixing in pyrope-grossular, Mg₃Al₂Si₃O₁₂–Ca₃Al₂Si₃O₁₂, solid solu- tion from lattice dynamics calculations and Monte Carlo simulations. Am Mineral (in press)

Vinograd VL, Sluiter MHF, Winkler B, Putnis A, Gale JD (2004a) Thermodynamics of mixing and ordering in silicates and oxides from static lattice energy and ab initio calculations. In: Warren M, Oganov A, Winkler B (eds) First-principles simulations: perspectives and challenges in mineral sciences. Berichte aus Arbeitskreisen der DFK, 14 Deutsche Gesellschaft für Kristallographie, pp 143–151

Vinograd VL, Sluiter MHF, Winkler B, Putnis A, Hålenius U, Gale JD, Becker U (2004b) Thermodynamics of mixing and ordering in the pyrope-grossular solid solution. Mineral Mag 68:101–121

Vinograd VL, Winkler B, Putnis A, Kroll H, Milman V, Gale JD, Fabrichnaya OB (2006) Thermodynamics of pyrope- majorite, Mg₃Al₂Si₃O₁₂–Mg₄Si₄O₁₂, solid solution from atomistic model calculations. Mol Simul 32(2):85–99

Von Dreele RB, Navrotsky A, Bowman AL (1977) Refinement of the crystal structure of Mg₂GeO₄ spinel. Acta Crystallo- graph B33:2287–2288

Wang H, Simmons G (1973) Elasticity of some mantle crystal structures 2. Rutile GeO₂. J Geophys Res 78:1262–1273

Warren MC, Dove MT, Myers ER, Bosenick A, Palin EJ, Sainz- Diaz CI, Guiton BS (2001) Monte Carlo methods for the study of cation ordering in minerals. Mineral Mag 65:221–248

Weidner DJ, Hamaya N (1983) Elastic properties of the olivine and spinel polymorphs of Mg₂GeO₄ and evaluation of elastic analogies. Phys Earth Planet Inter 33:275–283

Winkler B, Dove MT, Leslie M (1991) Static lattice energy minimization and lattice dynamics calculations on alumi- nosilicate minerals. Am Mineral 76:313–331

Yamanaka T, Komatsu Y, Sugahara M, Nagai T (2005) Structure change of MgSiO₃, MgGeO₃, and MgTiO₃ ilmenites under compression. Am Mineral 90:1301–1307

![](./images/812049252522917890_20.jpg)