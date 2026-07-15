# Anisotropic charge transport and optoelectronic properties of wide band gap organic semiconductors based on biphenyl derivatives: A computational study

Rudranarayan Khatua⁎, Smruti Ranjan Sahoo⁎, Sagar Sharmaᵇ, Sridhar Sahu⁎,∗

⁎ High Performance Computing Lab, Department of Physics, Indian Institute of Technology (ISM), Dhanbad 826004, India
ᵇ Department of Chemistry, School of Fundamental and Applied Sciences, Assam Don Bosco University, Tapesia Gardens, Sonapur 782402, Assam, India

---

## ARTICLE INFO

**Keywords:**
Organic semiconductors
Air-stability
Anisotropic mobility
Absorption spectra
Wide band gap
DFT

---

## ABSTRACT

The electronic structures and the charge transport properties of the biphenyl derivatives were calculated using density functional theory (DFT). The values of ionization potential (IP) of all the compounds were found in the range of 5.4–6.6 eV inferring the fact that the studied compounds held considerable air-stability properties. Moreover, lower values of hole-injection barrier as compared to those of electron-injection barrier implied that the investigated compounds were p-type semiconductors. The Hirshfeld Surface analysis depicting the distribution of surface charge in between the molecular layers of the crystals revealed that the principal interactions were mostly due to the C⋯H/H⋯C and H⋯H contacts for all the studied crystals. Bathochromic shifts were observed in absorption spectra of the compounds due to the substitution of different functional groups. The excitation energy and electronic HOMO–LUMO gap > 3 eV inferred the compounds to be wide band gap semiconductors. Further, the electronic band structure calculations for all the crystals ensued the band gap of the studied crystals in the range of 2.3–2.4 eV.

---

## 1. Introduction

Over the past few decades, organic semiconductors (OSCs) have attracted considerable amount of attentions due to their wide potential applications in various electronic devices such as organic field-effect transistors (OFETs) [1,2], organic photovoltaic devices (OPVs) [3], organic light emitting diodes (OLEDs) [4] and organic solar cells (OSCs) [5]. Unlike their inorganic counterparts, organic semiconducting materials are cost-effective, light weight and fairly flexible and also provide the versatility of chemical synthesis [6–14]. In comparison to the conventional inorganic semiconductors, organic semiconductors show relatively low charge carrier mobility mostly in the range of $10^{-5}$–$10\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$ [15–18]. Previously reported FET mobility of the different OSCs are listed in *Table 1*.

However, one of the major challenges for the development and fabrications of organic semiconductors for the industrial applications are their air-instabilities. From the theoretical point of view, the air-stability of the p-type organic semiconducting materials are characterized by their high ionization potential (IP) values (5.7–7.0 eV) and low electron affinity (EA) values (2.4–3.5 eV) [22–24]. For example, Liu and coworkers reported that the IP values of all benzo[1,2-k;4,5-k′] difluoranthene (BDF) derivatives are in the range (5.836–6.585 eV) could be suitable for p-type air-stable organic semiconductors [25]. Chang et al. studied the EA of 47 different compounds and analyzed that the EA value larger than 2.80 eV mostly afford their air-stability under ambient conditions [26]. Similar report was also published by Wang et al. for p-type diperfluorophenyl and thienyl substituted thiophene based organic semiconductors [27].

In recent years organic semiconductors based on biphenyl derivatives have attracted wide research attention due to their potential applications in optoelectronic industries [28–30]. Design of amorphous organic semiconductor based on 4,4′-N,N′-dicarbazole-biphenyl (CBP) was reported by Yuan et al. who measured the hole mobility of $9.93 \times 10^{-2}\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$ which is smaller than the calculated value. The discrepancy was suggested due to the defect and traps in amorphous films [31]. The charge transfer rate and carrier mobility of tetrafluorobiphenyl (TFBP) derivatives were theoretically reported by Maiti et al. using both quantum mechanical and semiclassical approaches who calculated the hole mobility up to $5.6\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$ for 2,6-hexafluoroterphenyl [32]. Density functional study of the cross stacking crystal of trans-2,5-diphenyl-1,4-distyrylbenzene was performed by Liu and coworkers who reported high anisotropic charge mobility (~

---

∗ Corresponding author.
E-mail addresses: sagars@outlook.com (S. Sharma), sridharsahu@iitism.ac.in (S. Sahu).

https://doi.org/10.1016/j.synthmet.2020.116474
Received 7 January 2020; Received in revised form 1 June 2020; Accepted 8 June 2020
0379-6779/ © 2020 Elsevier B.V. All rights reserved.
![](./images/812594790913802242_1.jpg)
![](./images/812594790913802242_2.jpg)
![](./images/812594790913802242_3.jpg)

<table><caption>Table 1
Reported FET mobility ($\mu$) values in $\text{cm}^2\text{V}^{-1}\text{s}^{-1}$ of various OSCs.</caption>
<thead>
  <tr>
    <th>References</th>
    <th>Compounds</th>
    <th>Mobility ($\mu$)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>[15,19]</td>
    <td>Pentacene</td>
    <td>5.6–35</td>
  </tr>
  <tr>
    <td>[16]</td>
    <td>Anthracene</td>
    <td>3</td>
  </tr>
  <tr>
    <td>[17]</td>
    <td>polythiphene</td>
    <td>~ $10^{-5}$</td>
  </tr>
  <tr>
    <td>[18]</td>
    <td>Trifluoro-dibenzoperylene</td>
    <td>0.234</td>
  </tr>
  <tr>
    <td>[20]</td>
    <td>Rubrene</td>
    <td>40</td>
  </tr>
  <tr>
    <td>[21]</td>
    <td>2,7-dioctyl[1]benzothieno[3,2-b]
[1]benzothiophene (C8-BTBT)</td>
    <td>43</td>
  </tr>
</tbody>
</table>

$10^{-2}\text{cm}^2\text{V}^{-1}\text{s}^{-1}$) for the compound [33]. The charge transport properties of the amorphous compounds N,N,N',N'-tetrakis(9,9-di-methyl-2-fluorenyl)-[1,1'-biphenyl]-4,4'-diamine (FFD) and N,N'-bis[9,9-di-methyl-2-fluorenyl]-N,N'-diphenyl-9,9-dimethylfluorene-2,7-diamine (PFFA) were experimentally investigated by Okumoto et al. who reported drift mobilities of $10^{-2}\text{cm}^2\text{V}^{-1}\text{s}^{-1}$ [34]. Further, Noh et al. synthesized the organic field-effect transistors based on fused bithiophene with fluorene and biphenyl compounds and reported that the compounds possessed herringbone packing and resulted in maximum field-effect mobilities in the order of ~ $10^{-2}\text{cm}^2\text{V}^{-1}\text{s}^{-1}$ under ambient conditions [35]. Similar work was also reported by Tao et al. for the hole-transporting materials 1,4-bis[2-(1-naphthyl)vinyl]benzene (BNVB) and 4,4'-bis[2-(1-naph- thyl)vinyl]biphenyl (BNVBP) [36]. Apart from the above citations, the electronic and charge transport properties of various OSCs based on biphenyl derivatives have also been extensively reported in literature [29,37–39].

Moreover, over the past few years, wide band gap organic semiconductors have also attracted considerable attention due to their potential applications as ultraviolet (UV) sensors, and low processing and fabrication cost as compared to their inorganic counterparts [40,41]. The wide band gap semiconductors, due to their high potential barrier, are ideal for preserving trapped charges, which hold great promise for use in memory devices [42]. The most common spectra cover the optical range from 300 nm to 400 nm [43,44]. For example, the maximum absorption spectra 348 nm of bis-vinylpyridine biphenyl compound was reported by Mei et al. [45]. Qiu et al. reported the absorption spectrum of benzofuranvinyl substituted benzene derivatives in the range of ~ 346–415 nm [46]. In addition, the wide band gap semiconductor based on triphenylbenzene carbazole derivative (PCP) having hole mobility up to $10^{-4}\text{cm}^2\text{V}^{-1}\text{s}^{-1}$ were experimetally reported by Zhang et al. [47].

In the present work, the optoelectronic and charge transport properties of biphenyl based compounds viz., 4,4'-bis(2-(2-Pyridyl)vinyl) biphenyl (BPVB), 4,4'-(Biphenyl-4,4'-diyldiethene-2,1-diyl)dipyridine (BDDP), 3,3'-(Biphenyl-4,4'-diyldiethene-2,1-diyl)dipyridine (BDDP1), trans-4,4'-bis(2-(2-Methoxyphenyl)vinyl)biphenyl (BMVB), 9,9'-(Biphenyl-4,4'-diyldiethene-2,1-diyl)dianthracene (BDDA), 4,4'-bis(9H-fluoren-9-ylidenemethyl)biphenyl (BFMB) and ph-biphenyl are systematically studied using density functional theory. The structural and electronic properties as well as the band structure of biphenyl derivatives have been investigated and their hole and electron reorganization energies were evaluated using their adiabatic potential energy surfaces. The Marcus–Hush theory has been used to investigate anisotropic hole and electron mobilities of these biphenyl derivatives.

## 2. Theory and computation

### 2.1. Theory

The simulation model is based on a combination of first-principles quantum mechanical calculations and Marcus–Hush theory, for the prediction of the anisotropic charge mobility of organic crystals [48].

At room temperature, the charge hopping rate ($K$) is described by Marcus theory as;
$$
K=\frac{V_{\text{eff}}^{2}}{\hbar}\left(\frac{\pi}{\lambda k_{B} T}\right)^{\frac{1}{2}} \exp \left(-\frac{\lambda}{4 k_{B} T}\right)
\tag{1}
$$
where $V_{\text{eff}}$ is the effective electronic coupling, $k_{B}$ is Boltzmann constant, and $\lambda$ is reorganization energy which is calculated as the energy difference between the neutral and ionic states of the systems [49];

Based on the molecular orbitals of the conjugated organic materials, $V_{\text{eff}}$ for the hole ($h$) or the electron ($e$) ($V_{\text{eff}}^{h/e}$) can be evaluated as [50–52];
$$
V_{\text{eff}}^{h / e}=\frac{J_{\alpha \beta}-S_{\alpha \beta}\left(t_{\alpha \alpha}^{H / L}+t_{\beta \beta}^{H / L}\right) / 2}{1-S_{\alpha \beta}^{2}}
\tag{2}
$$
where $S_{\alpha \beta}$ and $J_{\alpha \beta}$ are spatial overlap and charge transfer integral respectively. $t_{\alpha \alpha}^{H/L}$ and $t_{\beta \beta}^{H/L}$ are the site energies contributed from highest occupied molecular orbitals (HOMO) or lowest unoccupied molecular orbitals (LUMO), respectively.

Assuming that $H_{\text{ks}}$ is the Kohn–Sham Hamiltonian of the dimer system with $\phi_{\alpha}^{H / L}$ and $\phi_{\beta}^{H / L}$ being HOMO or LUMO of the two constituting monomers $\alpha$ and $\beta$, the other specified terms can be evaluated as [50,51];
$$
J_{\alpha \beta}=\left\langle\phi_{\alpha}^{H / L}\left|H_{\mathrm{ks}}\right| \phi_{\beta}^{H / L}\right\rangle
\tag{3}
$$

$$
S_{\alpha \beta}=\left\langle\phi_{\alpha}^{H / L} | \phi_{\beta}^{H / L}\right\rangle
\tag{4}
$$

$$
t_{\alpha \alpha}^{H / L}=\left\langle\phi_{\alpha}^{H / L}\left|H_{\mathrm{ks}}\right| \phi_{\alpha}^{H / L}\right\rangle
\tag{5}
$$

$$
t_{\beta \beta}^{H / L}=\left\langle\phi_{\beta}^{H / L}\left|H_{\mathrm{ks}}\right| \phi_{\beta}^{H / L}\right\rangle
\tag{6}
$$

At room temperature, assuming that the motion of the charge is a homogeneous random walk and hopping events are independent of each other, the charge transfer between the adjacent compounds of organic crystal exhibits a diffusive behavior. According to the Einstein relation, the drift mobility ($\mu$) from charge carrier hopping which specifies the isotropic mobility of organic crystals, is given by [48,50,51];
$$
\mu=\frac{e}{k_{B} T} D
\tag{7}
$$
where $D$ defines the diffusion coefficient resulted due to charge hopping in the organic crystals and is defined as follows;
$$
D=\frac{1}{2 n} \sum_{i} r_{i}^{2} \cdot K_{i} \cdot P_{i}
\tag{8}
$$
$n$ represents the spatial dimensionality (in our system $n = 1$), $r_{i}$ defines the intermolecular distance for $i$th hopping pathway, $K_{i}$ is the charge hopping rate and $P_{i}$ represents the hopping probability which is calculated as;
$$
P_{i}=\frac{K_{i}}{\sum K_{i}}
\tag{9}
$$

We calculate the charge mobility of organic semiconductors for each direction in terms of angles ($\gamma_{i}$) between the charge-hopping pathways and the plane of interest ($K_{i} \cdot r_{i} \cdot \cos \gamma_{i}$). If $\Phi$ is the angle of orientation of the transport channel relative to the reference axis (a, b, or c), and $\theta_{i}$ are the angles between the projected hopping paths of different dimers and the reference axis, then mobility orientation function to predict the angular-anisotropic charge carrier mobility in the organic crystals can be deduced from the relation [48];
$$
\mu_{\Phi}=\frac{e}{2 k_{B} T} \sum_{i} K_{i}.\ r_{i}^{2}.\ P_{i}.\ \cos ^{2} \gamma_{i} \cos ^{2}\left(\theta_{i}-\Phi\right)
\tag{10}
$$

### 2.2. Computation

The initial geometries of the biphenyl derivatives were obtained from the reported crystal structures of BPVB (CCDC 628422), BDDP (CCDC 227582), BDDP1 (CCDC 227584), BMVB (CCDC 744432), BDDA

(CCDC 844123) and BFMB (CCDC 296446) as provided in Cambridge Crystallographic Data Center [45,53-55,36]. We optimized the neutral and ionic molecular geometries of the above compounds using B3LYP hybrid exchange-correlation functional and 6-311 + +G(d,p) basis set within the framework of density functional theory (DFT). Because the gas-phase ionization potential (IP) and electron affinity (EA) at B3LYP level are supposed to provide over-estimated values, therefore, the frontier molecular orbitals (FMOs), ionization potential (IP) and electron affinity (EA) of the biphenyl derivatives were studied in $CHCl_3$ solvent with dielectric constant $(\varepsilon=4.81)$ using continuum solvation model (CSM) at the same level of theory [56,57]. For all the studied compounds, we obtained the SCF converged geometries with no imaginary frequencies. These optimized geometries are used for further properties calculations of the studied compounds. The time-dependent density functional theory (TDDFT) method with hybrid exchange-correlation functional using the Coulomb-Attenuating Method (CAM-B3LYP) was employed to investigate the absorption spectra of the biphenyl derivatives. The computation of effective transfer integral $(V_{eff})$, site energy $(t)$, and spatial overlap $(S_{\alpha\beta})$ of each dimer and monomer orbitals accomplished using Kohn-Sham Hamiltonian, $H_{ks}$ [48,50-52] through fragment molecular orbital (FMO) approach of dimers [58,59]. All these calculations were performed using GAUSSIAN 09 computational package [60]. First principle calculation using generalized gradient approximation with Perdew-Burke-Ernzerhof parameterization (GGA-PBE) [61] was used to calculate density of state (DOS) and electronic band-structure of the studied compounds [62]. The Monkhorst-Pack method [63] is used to generate k-point meshes $3\times1\times1$ (BDDA), $1\times3\times1$ (BDDP), $1\times3\times1$ (BDDP1), $2\times1\times1$ (BFMB), $1\times3\times1$ (BMVB) and $2\times3\times1$ (BPVB) for monoclinic, monoclinic, monoclinic, triclinic, monoclinic and orthorhombic unit cell respectively. The Hirshfeld Surface was performed using crystal explore 17.5 [64]. The Hirshfeld Surface analysis was also carried out to study the intermolecular interactions contributed by different atoms in the crystal.

## 3. Result and discussion

### 3.1. Structural and electronic properties

#### 3.1.1. Geometry

The chemical structures of the biphenyl derivatives are shown in Fig. 1. The optimized structures of biphenyl, ph-biphenyl, BPVB, BDDP, BDDP1, BMVB, BDDA and BFMB compounds in neutral state are provided in the supplementary information (Fig. S2(a-h)). The bond length of neutral and charge states (anion and cation) as a function of bond index are also provided in the supplementary information (Table S1(a-f)). As shown in the figure, a very small change in the geometries is noted in all the studied compounds. The maximum deviation in optimized bond lengths of BPVB, BDDP, BDDP1, BMVB, BDDA and BFMB relative to their respective experimental geometries are found to be $0.019\mathring{A}$, $0.022\mathring{A}$, $0.020\mathring{A}$, $0.028\mathring{A}$, $0.026\mathring{A}$ and $0.012\mathring{A}$ respectively. The bond length change between the neutral and anionic state and bond length change between the neutral and cationic state of all the compounds are illustrated in Fig. S3(a-b). We observed slight elongation in the bond length of both the reduction and oxidation states in the range of $(-0.035$ to $0.020\mathring{A})$ at the bond index number 1-8. This can be attributed to the effects of different substitutions at the end positions of the compounds. It can also be noted that the change in bond length of reduction states is slightly more $(\sim0.002\mathring{A})$ than that of the oxidation states at bond index 1, 2, 4, 6, and 8 and the fact is reflected on the respective reorganization energies of the compounds. The dihedral angles of the studied derivatives are provided in the supplementary information (Table S2 and Table S3). Very negligible dihedral angles in the range of $0.005-0.949^\circ$ were observed in the case of BPVB, BDDP, and BDDP1 compounds. However, in the cases of BFMB and BDDA, large dihedral angles in the range of $0.848-42.919^\circ$ and $0.313-52.266^\circ$ respectively, were observed in their end positions. In the case of BMVB, dihedral angle in the range of $0.001-36.482^\circ$ was found in the core position. Relatively large twists in BFMB, BDDA, and BMVB compounds were found due to the substitutional effects of larger functional groups such as fluorine, anthracene, and methoxyphenyl at the end positions of the biphenyl compound. The change in dihedral angles of the studied compounds with respect to their experimental crystal structures are found in the ranges of $0.025-13.953^\circ$, $0.72-7.227^\circ$, $0.199-10.526^\circ$, $7.519-13.574^\circ$, $1.203-35.958^\circ$ and $0.131-31.992^\circ$ for the compounds BPVB, BDDP, BDDP1, BFMB, BMVB and BDDA respectively. These changes might affect the molecular orbital energies (HOMO and LUMO) and electronic couplings.

![](./images/812594790913802242_4.jpg)

Fig. 1. Chemical structure of the biphenyl organic compounds with different substituent groups. The number 1-8 indicates the bond index of the studied compounds, where the values are provided in the supplementary information.

### 3.1.2. Frontier molecular orbitals (FMO), IP, EA and air-stability

The computed HOMO, LUMO, HOMO-LUMO gaps, ionization potential (IP) and electron affinity (EA) of the studied biphenyl derivatives in $CHCl_3$ solvent are provided in Table 2. The HOMO (LUMO) energy of all the compounds are found to be in the range of $-5.383$ to $-6.362$ eV ($-1.471$ to $-2.620$ eV) respectively. The large HOMO energy ($-5.383$ to $-6.362$ eV) suggests that the investigated compounds can be of p-type [65,66]. The theoretically calculated HOMO-LUMO gap of BFMB is 3.25 eV, which is very close to the experimental HOMO-LUMO gap (3.17 eV) (supplementary information) [53]. Similarly as listed in Table 2, the range of adiabatic ionization potential (AIP) (vertical ionization potential (VIP)) and adiabatic electron affinity (AEA) (vertical electron affinity (VEA)) are found to be in range of 5.36 eV (5.46 eV) to 6.55 eV (6.60 eV) and 1.46 eV (1.30 eV) to 2.64 eV (2.52 eV) respectively, inferring the fact that the compounds possess substantial air-stability properties [22-24]. The calculated values of IP and EA of BFMB are found to be 5.74 eV and 2.48 eV respectively, which are in good agreement with the experimental data (5.51 eV and 2.34 eV) (supplementary information) [53].

In addition, the electron affinities (EAs) and ionization potentials (IPs) are closely related to the charge injection from the electrodes and determine the redox stability of molecular materials [67]. In our study we have considered gold (Au) electrode (work function ~5.1 eV) which is widely used for OFET devices [68,69]. The calculated values of hole and electron injection barrier are found to be in the range of 0.26-1.45 eV and 2.38-3.64 eV respectively. Lower values of hole injection barrier as compared to those of electron injection barrier suggest that the investigated compounds can be of p-type [68]. It is noted that the substitution of different functional groups reduces the injection barrierof the bare biphenyl compound. In the cases of BMVB and BDDA, the decrease in hole injection barrier is phenomenal (reduced almost by five times) as compared to the bare biphenyl, whereas the electron injection barriers are reduced by 0.75 eV and 1.03 eV, for BMVB and BDDA compounds respectively [68,69]. Hence, the substitution of anthracene, fluorene, pyridine, methoxyphenyl groups in biphenyl is found to largely improve the hole (electron) transportability in the compounds.

<table>
<caption>Table 2
Adiabatic electron affinity (AEA), vertical electron affinity (VEA), adiabatic ionization potential (AIP), vertical ionization potential (VIP), frontier molecular orbital energy, and HOMO–LUMO gap at B3LYP/6-311++G(d,p) in CHCl₃ solvent and hole reorganization energy (λ₊) and electron reorganization energy (λ₋) at B3LYP/6-311++G(d,p) of all the investigated compounds. All parameters are given in the electron volt (eV) unit.</caption>
<thead>
<tr>
<th>Molecule</th>
<th>AEA</th>
<th>VEA</th>
<th>AIP</th>
<th>VIP</th>
<th>λ₊</th>
<th>λ₋</th>
<th>HOMO</th>
<th>LUMO</th>
<th>H-L gap</th>
</tr>
</thead>
<tbody>
<tr>
<td>Biphenyl</td>
<td>1.46</td>
<td>1.30</td>
<td>6.55</td>
<td>6.60</td>
<td>0.25</td>
<td>0.30</td>
<td>−6.362</td>
<td>−1.471</td>
<td>4.891</td>
</tr>
<tr>
<td>ph-biphenyl</td>
<td>2.26</td>
<td>2.10</td>
<td>5.68</td>
<td>5.75</td>
<td>0.26</td>
<td>0.30</td>
<td>−5.631</td>
<td>−2.199</td>
<td>3.432</td>
</tr>
<tr>
<td>BPVB</td>
<td>2.47</td>
<td>2.35</td>
<td>5.71</td>
<td>5.81</td>
<td>0.19</td>
<td>0.25</td>
<td>−5.688</td>
<td>−2.445</td>
<td>3.243</td>
</tr>
<tr>
<td>BDDP</td>
<td>2.64</td>
<td>2.52</td>
<td>5.90</td>
<td>6.01</td>
<td>0.20</td>
<td>0.25</td>
<td>−5.884</td>
<td>−2.620</td>
<td>3.264</td>
</tr>
<tr>
<td>BDDP1</td>
<td>2.48</td>
<td>2.37</td>
<td>5.74</td>
<td>5.84</td>
<td>0.21</td>
<td>0.22</td>
<td>−5.719</td>
<td>−2.466</td>
<td>3.253</td>
</tr>
<tr>
<td>BMVB</td>
<td>2.21</td>
<td>2.03</td>
<td>5.45</td>
<td>5.61</td>
<td>0.33</td>
<td>0.36</td>
<td>−5.496</td>
<td>−2.116</td>
<td>3.38</td>
</tr>
<tr>
<td>BDDA</td>
<td>2.49</td>
<td>2.36</td>
<td>5.36</td>
<td>5.46</td>
<td>0.19</td>
<td>0.24</td>
<td>−5.383</td>
<td>−2.429</td>
<td>2.954</td>
</tr>
<tr>
<td>BFMB</td>
<td>2.72</td>
<td>2.48</td>
<td>5.74</td>
<td>5.90</td>
<td>0.31</td>
<td>0.43</td>
<td>−5.807</td>
<td>−2.556</td>
<td>3.251</td>
</tr>
</tbody>
</table>

### 3.2. Hirshfeld Surface analysis

The Hirshfeld Surface (HS) is defined as the surface of the crystal electron density which encodes the quantitative information related to the intermolecular interaction of the molecular fragments in the organic crystals. The HS of the intermolecular layers of the studied compounds are provided in the supplementary information (Fig. S4(a–f)). The HS of the compounds is basically explained in terms of three colors; white: the intermolecular contacts with distances equal to the sum of the van der Waals radii, red: the distances shorter than the sum of the van der Waals radii, and blue: the distances longer than the sum of the van der Waals radii [70]. Mathematically, HS can be analyzed in terms of two-dimensional histogram called 2D fingerprint plot which gives the information about the percentage of major and minor contribution of interatomic contacts in the molecule. The plot is explained in terms of the reciprocal contact distances such as; $d_e$ and $d_i$ which are defined as the distances from a point on the HS to the nearest nucleus outside and inside the surface, respectively. These contact distances are normalized ($d_{norm}$) using the van der Waals radius of the appropriate internal ($r_i^{vdw}$) and external ($r_e^{vdw}$) atom of the surface.

Now the normalized contact distance ($d_{norm}$) can be defined as [71,72];

$$
d_{\text{norm}} = \frac{d_i - r_i^{\text{vdw}}}{r_i^{\text{vdw}}} + \frac{d_e - r_e^{\text{vdw}}}{r_e^{\text{vdw}}}
\tag{11}
$$

The charge transport property of an organic crystal is substantially affected by its molecular packing structure and inter (intra)-molecular coupling [73,74]. The Hirshfeld Surface analysis provides a quantitative picture of molecular interaction contributed by each constituting atoms or molecular layers. The 2D fingerprint plots of all the studied crystals are illustrated in Fig. 2 and relative contributions for different intermolecular contacts of all the crystals are listed in the Table 3. Hirshfeld Surface for individual molecules is provided in the supplementary information Fig. S5(a–f). It is observed that the principal interactions between the molecular layers (MLs) are mostly due to the C···H/H···C and H···H contacts for all the studied crystals. The C···H/H···C interactions to the total Hirshfeld Surface have two symmetrical wings on the right and left sides and have maximum contributions of 39.6% (BPVB), 47.7% (BDDP), 47.8% (BDDP1), 50.8% (BDDA), 45.2% (BMVB) and 37.2% (BFMB) respectively. Similarly, the H···H contacts are found to be only on the top most spike of the Hirshfeld Surface (with $d_i$ ranging from 1.1 Å to 2.7 Å and $d_e$ in the range of 1.1–2.6 Å) for all the crystals and also provide major contributions to the HS. However, the C···C, N···C, N···H and N···N intermolecular interactions contribute only 3.7%, 0.9%, 13.2% and 0.1% of the total HS for BDDP crystal. Similar trend is also observed in other compounds. The C···N and H···N intermolecular interactions of BDDP and BDDP1 crystals are found to be larger than those of the BPVB crystal. The relatively large intermolecular interactions in these two crystals result in the increase of electronic charge coupling between the neighbour monomers of the crystals.

### 3.3. Charge transport properties

#### 3.3.1. Reorganization energy

Reorganization energy is the relaxation energy that arises because of the charge redistribution over the molecule during the oxidation and reduction process and it reflects the capability of charge transfer in OSCs. The reorganization energies of the studied compounds were calculated based on adiabatic potential energy surface method [75]. The calculated internal reorganization energies (excluding external contribution) for holes (λ₊) and electrons (λ₋) of biphenyl, ph-biphenyl, BPVB, BDDP, BDDP1, BMVB, BDDA and BFMB are found to be 0.25 (0.30) eV, 0.26 (0.30) eV, 0.19 (0.25) eV, 0.20 (0.25) eV, 0.21 (0.22) eV, 0.33 (0.36) eV, 0.19 (0.24) eV and 0.31 (0.43) eV, respectively which are supported by smaller geometry relaxation by oxidation than that of the reduction. It is found that the computed values of λ₊ and λ₋ for all the biphenyl derivatives except BFMB and BMVB, are much lower than that of the bare biphenyl and ph-biphenyl compounds inferring better charge transport capability in those compounds. It should be noted that the substitution of electron-withdrawing ring pyridine in BPVB, BDDP and BDDP1 compounds lowers the λ₊ and λ₋ as compared to those of phenyl substituted ph-biphenyl compound. In all the cases, λ₊ is found to be smaller than λ₋ which indicate that the hole transfer rate is supposed to be faster than the electron transfer rate [75].

#### 3.3.2. Molecular packing and electronic coupling

The charge transport properties of the organic semiconductors basically depend on the molecular packing in organic crystals and also on the electronic couplings among the adjacent molecular units in the crystals [76,77]. The rate of charge transfer (K) is evaluated using Marcus-Hush theory at room temperature (300 K). The distinct nearest molecular dimers selected as the hopping channels for the charge carrier in BPVB crystal is shown in Fig. 3(a). The herringbone packing in BPVB crystal structure has possible pathways namely parallel face-to-face (P) and edge-to-edge (T1 and T2) packing patterns. The intermolecular distances $r_i$ of the three accounted pathways P, T1 and T2 are 7.44 Å, 5.997 Å and 5.997 Å respectively, and the conducting angles between the hopping paths and the reference axis $b$ are $θ_P = 0°$, $θ_{T1} = 51.66°$ and $θ_{T2} = 128.34°$. $φ$ is the angle of orientation with respect to the reference axis $b$ and the reference plane of the crystal is $b$-$a$. The calculated values of intermolecular distance, angle between the dimers and effective electronic coupling ($V_{eff}$) for all nearest dimers of the BPVB crystal have been summarized in the Table 4. It is found that the maximum value of $V_{eff}^h$ is −13 meV meV for the parallel P dimer, which is because of the maximum overlapping of the π-orbitals in the face-to-face packing form. However, relatively small effective HOMO electronic coupling leads to lower transfer integral for T1 and T2 (−4.6 meV) dimers as compared to the P dimer. Similarly for the BDDP crystal as depicted in Fig. 3(b), the conduction angles with respect to the references axis $b$ are $θ_P = 0°$, $θ_{T1} = 65.81°$, $θ_{T2} = 114.19°$. The calculated $V_{eff}^e$ is found to be comparatively larger (35.0 meV) in P

![](./images/812594790913802242_5.jpg)

Fig. 2. 2D fingerprint plots for di-substituted biphenyl compounds; (a) BPVB, (b) BDDP, (c) BDDP1, (d) BMVB, (e) BDDA and (f) BFMB.

<table>
<caption>Table 3
The relative contributions for intermolecular contacts of crystals; BPVB, BDDP, BDDP1, BMVB, BDDA and BFMB.</caption>
<thead>
<tr>
<th>Crystals</th>
<th>C…C</th>
<th>H…H</th>
<th>C…H</th>
<th>H…N</th>
<th>C…N</th>
<th>N…N</th>
<th>O…C</th>
<th>O…H</th>
<th>O…O</th>
</tr>
</thead>
<tbody>
<tr>
<td>BPVB</td>
<td>5.0</td>
<td>46.6</td>
<td>39.6</td>
<td>8.9</td>
<td>0.0</td>
<td>0.0</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>BDDP</td>
<td>3.7</td>
<td>34.5</td>
<td>47.7</td>
<td>13.2</td>
<td>0.9</td>
<td>0.1</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>BDDP1</td>
<td>2.1</td>
<td>37.7</td>
<td>47.8</td>
<td>9.2</td>
<td>3.2</td>
<td>0.0</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>BMVB</td>
<td>0.0</td>
<td>49.1</td>
<td>45.2</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>0.0</td>
<td>5.6</td>
<td>0.0</td>
</tr>
<tr>
<td>BDDA</td>
<td>0.6</td>
<td>48.6</td>
<td>50.8</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>BFMB</td>
<td>9.2</td>
<td>53.6</td>
<td>37.2</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
</tbody>
</table>

dimer than T1 (7.9 meV) and T2 (7.9 meV) dimers whereas $V_{\text{eff}}^{h}$ of T1 ($-19.5$ meV) and T2 ($-19.5$ meV) dimers are comparatively larger than P dimer (11.0 meV). This is due to the fact that the bonding (antibonding) overlapping of LUMO orbital in P dimer is relatively more than that of HOMO overlapping, whereas in T dimers, the HOMO interaction is comparatively more. Similar result is observed in the case of BDDP1 crystal Fig. 3(c). For the BMVB crystal (Fig. 3(d)), the value of $V_{\text{eff}}^{h}/V_{\text{eff}}^{e}$ for T1 ($-3.0$ meV/9.0 meV) and T2 ($-3.0$ meV/9.0 meV) are found to be much smaller than the values of P dimer (8.9 meV/33.6 meV). However, in BDDA crystal which also shows herringbone packing, the effective electronic coupling ($V_{\text{eff}}^{h}/V_{\text{eff}}^{e}=15.6$ meV/1.0 meV) is observed along T1 and T2 channels with an intermolecular distance of $11.486\,\mathring{\text{A}}$ and almost no contribution is found from the P dimer. In BFMB crystal, crystallographic axis c is chosen as the reference axis as shown in Fig. 3(f). The possible nearest parallel dimmers are P1, P2, P3 and P4 respectively. We observe maximum value of $V_{\text{eff}}^{e}$ along P2 dimer ($-14.1$ meV) as compared to the other two dimers P1 (1.3 meV) and P3 ($-9.0$ meV). Similarly, we observe larger $V_{\text{eff}}^{h}$ along P3 dimer ($-5.8$ meV) than other two dimers P1 ($-1.2$ meV) and P2 ($-2.5$ meV) respectively. It is worth mentioning that except BPVB, the value of $V_{\text{eff}}^{e}$ is larger than $V_{\text{eff}}^{h}$ for all the compounds along P channels, whereas along T channels, $V_{\text{eff}}^{h}$ is found larger than $V_{\text{eff}}^{e}$ in the cases of BDDP, BDDP1 and BDDA. We observe that in pyridine substituted BDDP and BDDP1 crystals, value of $V_{\text{eff}}^{e}$ is relatively larger than those of other crystals clarifying the effect of the electron-withdrawing pyridine group. It can be noted that electronic couplings in BPVB, BDDP and BDDP1 are relatively larger than those in BDDA and BMVB which are due to noticeable twists in the former compounds. For anthracene substituted BDDA, value of $V_{\text{eff}}^{h}$ is found to be larger than $V_{\text{eff}}^{e}$, whereas $V_{\text{eff}}^{e}$ for BFMB and BMVB are found to be relatively larger than $V_{\text{eff}}^{h}$ respectively.

### 3.4. Anisotropic charge mobility

The charge carrier (hole and electron) mobilities of the studied compounds show the remarkable anisotropic behavior due to their molecular crystal packing. The calculated hole mobilities of biphenyl derivatives are found in the order of $10^{-3}$–$10^{-1}\,\text{cm}^{2}\text{V}^{-1}\text{s}^{-1}$, which is nearly in the range of the experimentally reported values $10^{-4}$–$10^{-2}\,\text{cm}^{2}\text{V}^{-1}\text{s}^{-1}$ [78–81]. The computed values of anisotropic mobilities ($\mu_{\Phi}$) of different compounds are given in Table 4. The electron and hole mobility of BPVB crystal is shown in Fig. 4(a). It is found that the maximum hole and electron anisotropic mobilities ($\mu_{\Phi}^{h}=0.0889\,\text{cm}^{2}\text{V}^{-1}\text{s}^{-1}$ and $\mu_{\Phi}^{e}=0.0152\,\text{cm}^{2}\text{V}^{-1}\text{s}^{-1}$) in BPVB appears at $\Phi=0^{\circ}$ and $\Phi=90^{\circ}$, respectively. Due to large HOMO electron coupling, the P channel contribute more to the hole mobility ($\mu_{\Phi}^{h}=0.0889\,\text{cm}^{2}\text{V}^{-1}\text{s}^{-1}$ at $\Phi=0^{\circ}$) than the T1/T2 channel ($0.03438\,\text{cm}^{2}\text{V}^{-1}\text{s}^{-1}$ at $\Phi=52^{\circ}/128^{\circ}$). However, the electron mobility along T1/T2 channel ($\mu_{\Phi}^{e}=0.00\,\text{cm}^{2}\text{V}^{-1}\text{s}^{-1}$ at $\Phi=52^{\circ}/128^{\circ}$) is found to be more than the P channel ($\mu_{\Phi}^{e}=0.0095$ at $\Phi=0^{\circ}$) due to large LUMO

![](./images/812594790913802242_6.jpg)

Fig. 3. The molecular packing and charge hopping pathways to the transistor channel in the a-b plane of (a) BPVB and b-c plane of (b) BDDP, (c) BDDP1 (d) BMVB (e) BDDA and (f) BFMB respectively.

electronic coupling. In BDDP crystal the maximum hole and electron mobility (Fig. 4(b)) of $0.193\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$ and $0.211\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$ occur at the reference angle $\Phi = 90^\circ$ and $\Phi = 0^\circ$ and minima appear at $\Phi = 0^\circ$ $(0.0337\ \text{cm}^2\text{V}^{-1}\text{s}^{-1})$ and $\Phi = 90^\circ$ $(0.0013\ \text{cm}^2\text{V}^{-1}\text{s}^{-1})$ respectively. Similar observation is also found in the case of BDDP1 molecular crystal (Fig. 4(c)). As depicted in Fig. 4(d), the maximum (hole/electron) mobility in BMVB crystal is observed to be $7.91 \times 10^{-3}\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}/$$4.988 \times 10^{-2}\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$ at $\Phi = 68^\circ$. However, in the case of BDDA crystal (Fig. 4(e)), the edge-to-edge (T1 and T2) dimers exhibit large hole/electron mobilities $(\mu_{\phi}^{h} = 2.215 \times 10^{-1}\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$ at $\Phi = 57^\circ)/(\mu_{\phi}^{e} = 5.0 \times 10^{-4}\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$ at $\Phi = 123^\circ)$ than those along P channel. The $\mu_{\phi}^{h}(\text{max})$ and $\mu_{\phi}^{e}(\text{max})$ are found to be $2.679 \times 10^{-1}\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$ and $6 \times 10^{-4}\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$ at $\Phi = 90^\circ$. Similarly, in BFMB (Fig. 4(f)), the $\mu_{\phi}^{h}(\text{max})$ and $\mu_{\phi}^{e}(\text{max})$ are observed to be 7.111 are found to enhance $\mu_{\phi}^{h}$ and $\mu_{\phi}^{e}$ relatively more ( $\sim$ factor of $10^1$-$10^2$) than those of O-functionalized BMVB. The above results show that BPVB and BDDA crystals exhibit larger $\mu_{\phi}^{h}$ than $\mu_{\phi}^{e}$ whereas, crystals BDDP, BDDP1, BMVB and BFMB shows comparatively larger electron mobility which indicates the fact that the later set of crystals possess a bit electron transporting characters.

Table 4
The calculated intermolecular distance ($r$), angle of orientation ($\theta$), effective charge transfer integral ($V_{eff}$), charge hopping rate ($K$) and range of anisotropic charge mobility ($\mu_{\phi}$) for BPVB, BDDP, BDDP1, BMVB, BDDA and BFMB compounds.

<table>
<thead>
<tr>
<th>Compounds</th>
<th>channel</th>
<th>$r$ (Å)</th>
<th>$\theta$ (degree)</th>
<th>$V_{eff}^{h}/V_{eff}^{e}$ (meV)</th>
<th>$K^{h}/K^{e}$ (s⁻¹)</th>
<th>$\mu_{\phi}^{h}$ (cm²V⁻¹s⁻¹)</th>
<th>$\mu_{\phi}^{e}$ (cm²V⁻¹s⁻¹)</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">BPVB</td>
<td>P</td>
<td>7.440</td>
<td>0</td>
<td>−13.00/0.4</td>
<td>$1.03 × 10^{12}/4.78 × 10^{8}$</td>
<td rowspan="3">$1.104 × 10^{-3}$–$8.89 × 10^{-2}$</td>
<td rowspan="3">$9.50 × 10^{-3}$–$1.52 × 10^{-2}$</td>
</tr>
<tr>
<td>T1</td>
<td>5.997</td>
<td>51.66</td>
<td>−4.6/10.9</td>
<td>$1.29 × 10^{11}/3.55 × 10^{11}$</td>
</tr>
<tr>
<td>T2</td>
<td>5.997</td>
<td>128.34</td>
<td>−4.6/10.9</td>
<td>$1.29 × 10^{11}/3.55 × 10^{11}$</td>
</tr>
<tr>
<td rowspan="3">BDDP</td>
<td>P</td>
<td>5.714</td>
<td>0</td>
<td>11.00/35.00</td>
<td>$6.55 × 10^{11}/3.67 × 10^{12}$</td>
<td rowspan="3">$3.37 × 10^{-2}$–$1.39 × 10^{-1}$</td>
<td rowspan="3">$1.342 × 10^{-3}$–$2.11 × 10^{-1}$</td>
</tr>
<tr>
<td>T1</td>
<td>6.974</td>
<td>65.81</td>
<td>−19.50/7.90</td>
<td>$2.06 × 10^{12}/1.86 × 10^{11}$</td>
</tr>
<tr>
<td>T2</td>
<td>6.974</td>
<td>114.19</td>
<td>−19.50/7.90</td>
<td>$2.06 × 10^{12}/1.86 × 10^{11}$</td>
</tr>
<tr>
<td rowspan="3">BDDP1</td>
<td>P</td>
<td>5.562</td>
<td>0</td>
<td>14.30/40.4</td>
<td>$9.78 × 10^{11}/6.94 × 10^{12}$</td>
<td rowspan="3">$2.955 × 10^{-2}$–$6.441 × 10^{-2}$</td>
<td rowspan="3">$1.204 × 10^{-2}$–$3.398 × 10^{-1}$</td>
</tr>
<tr>
<td>T1</td>
<td>7.033</td>
<td>66.71</td>
<td>−15.4/13.7</td>
<td>$1.14 × 10^{12}/7.98 × 10^{11}$</td>
</tr>
<tr>
<td>T2</td>
<td>7.033</td>
<td>113.29</td>
<td>−15.4/13.7</td>
<td>$1.14 × 10^{12}/7.98 × 10^{11}$</td>
</tr>
<tr>
<td rowspan="3">BMVB</td>
<td>P</td>
<td>5.505</td>
<td>0</td>
<td>8.9/33.6</td>
<td>$9.49 × 10^{10}/9.70 × 10^{11}$</td>
<td rowspan="3">$1.75 × 10^{-4}$–$4.567 × 10^{-3}$</td>
<td rowspan="3">$7.9 × 10^{-3}$–$4.988 × 10^{-2}$</td>
</tr>
<tr>
<td>T1</td>
<td>7.264</td>
<td>67.73</td>
<td>−3.0/9.0</td>
<td>$1.08 × 10^{10}/6.96 × 10^{10}$</td>
</tr>
<tr>
<td>T2</td>
<td>7.264</td>
<td>112.27</td>
<td>−3.0/9.0</td>
<td>$1.08 × 10^{10}/6.96 × 10^{10}$</td>
</tr>
<tr>
<td rowspan="3">BDDA</td>
<td>P</td>
<td>12.454</td>
<td>0</td>
<td>0.0/0.0</td>
<td>0.0/0.0</td>
<td rowspan="3">$1.115 × 10^{-1}$–$2.679 × 10^{-1}$</td>
<td rowspan="3">$2.52 × 10^{-4}$–$6.05 × 10^{-4}$</td>
</tr>
<tr>
<td>T1</td>
<td>11.486</td>
<td>57.17</td>
<td>15.6/1.0</td>
<td>$1.49 × 10^{12}/3.36 × 10^{09}$</td>
</tr>
<tr>
<td>T2</td>
<td>11.486</td>
<td>122.83</td>
<td>15.6/1.0</td>
<td>$1.49 × 10^{12}/3.36 × 10^{09}$</td>
</tr>
<tr>
<td rowspan="4">BFMB</td>
<td>P1</td>
<td>11.063</td>
<td>0</td>
<td>−1.2/1.3</td>
<td>$2.16 × 10^{09}/6.75 × 10^{08}$</td>
<td rowspan="4">$2.74 × 10^{-4}$–$7.11 × 10^{-3}$</td>
<td rowspan="4">$5.18 × 10^{-4}$–$3.203 × 10^{-2}$</td>
</tr>
<tr>
<td>P2</td>
<td>16.925</td>
<td>29.46</td>
<td>−2.5/−14.1</td>
<td>$9.38 × 10^{09}/7.94 × 10^{10}$</td>
</tr>
<tr>
<td>P3</td>
<td>9.099</td>
<td>66.19</td>
<td>−5.8/−9.0</td>
<td>$5.05 × 10^{10}/3.23 × 10^{10}$</td>
</tr>
<tr>
<td>P4</td>
<td>11.131</td>
<td>131.60</td>
<td>0.0/0.0</td>
<td>0.0/0.0</td>
</tr>
</tbody>
</table>

![](./images/812594790913802242_7.jpg)

Fig. 4. The predicted anisotropic hole and electron mobilities of the studied compounds; (a) BPVB, (b) BDDP, (c) BDDP1, (d) BMVB, (e) BDDA and (f) BFMB respectively.

### 3.5. Absorption spectra

The absorption spectra of the biphenyl derivatives are investigated at TD/CAM-B3LYP/6-311++G(d,p) level in $CHCl_3$ solvent, within the frame work of density functional theory (DFT). Though singlet, triplet excitations and singlet fissions are all reported in organic semi-conducting materials, however, we have performed only the singlet excited calculations for the studied compounds [82,83]. A maximum of 20 excited states are taken into consideration for determining the absorption spectra of the compounds. The optical transition of all the studied compounds are illustrated in Fig. 5 and the corresponding optical datas are provided in Table 5. The UV-visible absorption spectra of all the studied compounds are found in the wavelength region of 192-409 nm. The absorption spectrum of biphenyl compound shows two strong absorption peaks at 197 nm and 192 nm corresponding to the electronic transitions $S_0 \to S_7$ and $S_0 \to S_9$ respectively. The calculated excitation energy of biphenyl compound at vapor phase is found to be in the range of 4.81-6.43 eV which is comparable to the data (5.6-6.8 eV) reported by Fukuda et al. [84]. Similarly, the wavelength corresponding to the largest peak of BDDP and BDDP1 compounds are found to be 372 nm and 373 nm, which are in good agreement with the experimentally reported value of 354 nm and 348 nm [45]. All the substituted compounds have $\lambda_{max}$ (related to the highest absorption peak) corresponding to the electronic transition state $S_0 \to S_1$ (H $\to$ L), except BPVB in which $\lambda_{max}$ is observed at 237 nm corresponding to the electronic transition state $S_0 \to S_{12}$ (H $\to$ L + 1). It is obvious from Fig. 5 that the substitution of different groups into the biphenyl compound causes red-shift in the absorption spectra in the order of BDDA (409 nm) > BFMB (377 nm) > BDDP1 (373 nm) > BDDP (372 nm) > BMVB (361 nm) > ph-biphenyl (355 nm) > BPVB (237 nm) > biphenyl (197 nm). The bathochromic shift in the absorption spectrum of BDDA as compared to BDDP, BPVB and BDDP1 is expected due to the substitution of anthracene which has low-energy absorption spectra in comparison with pyridine [85,86]. The excitation energy levels of all the studied compounds (except BPVB) corresponding to H $\to$ L transition is found in the range of 3.0-3.5 eV which is almost comparable to the electronic HOMO-LUMO gaps (3.0-3.4 eV). The fact concludes the studied materials to be wide band gap semiconductors [87].

![](./images/812594790913802242_8.jpg)

Fig. 5. The absorption spectra for the biphenyl derivatives are evaluated at TD/ CAM-B3LYP/6-311++G(d,p) level in $CHCl_3$ solvent.

### 3.6. Band structure and density of states

The electronic band structure and density of states (DOS) of all the studied biphenyl derivatives are illustrated in Fig. 6. In BPVB crystal, the conduction band minima (CBM) and valence band maxima (VBM) are found to occur at $\Gamma$-point and M-point inferring the fact that the materials are indirect band gap semiconductor with band gap ($E_g$) of 2.28 eV. The band dispersion and band splitting for all the compounds are calculated near the Fermi level. The largest band dispersion of CB and VB is calculated to be 67.51 meV and 33.14 meV along $\Gamma$R and $\Gamma$X respectively. In addition, both largest splitting of VB and CB are found

Table 5
The electronic transition, absorption wavelength ($\lambda$), excitation energy ($E$), oscillator strength ($f$) and major contribution for biphenyl derivatives are evaluated at TD/CAM-B3LYP/6-311++G(d,p) level in $\text{CHCl}_3$ solvent.

<table>
  <thead>
    <tr>
      <th>Compounds</th>
      <th>Transition</th>
      <th>$\lambda$ (nm)</th>
      <th>$E$ (eV)</th>
      <th>$f$</th>
      <th>Major contribution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Biphenyl</td>
      <td>$S_0 \rightarrow S_1$</td>
      <td>263</td>
      <td>4.71</td>
      <td>0.6546</td>
      <td>$\text{H} \rightarrow \text{L}$ (96%)</td>
    </tr>
    <tr>
      <td>$S_0 \rightarrow S_7$</td>
      <td>197</td>
      <td>6.30</td>
      <td>1.0489</td>
      <td>$\text{H} - 1 \rightarrow \text{L} + 1$ (81%)</td>
    </tr>
    <tr>
      <td>$S_0 \rightarrow S_9$</td>
      <td>192</td>
      <td>6.44</td>
      <td>0.7731</td>
      <td>$\text{H} - 2 \rightarrow \text{L}$ (38%), $\text{H} \rightarrow \text{L} + 5$ (58%)</td>
    </tr>
    <tr>
      <td rowspan="3">ph-biphenyl</td>
      <td>$S_0 \rightarrow S_1$</td>
      <td>355</td>
      <td>3.49</td>
      <td>2.6403</td>
      <td>$\text{H} \rightarrow \text{L}$ (84%)</td>
    </tr>
    <tr>
      <td>$S_0 \rightarrow S_{12}$</td>
      <td>223</td>
      <td>5.55</td>
      <td>0.5614</td>
      <td>$\text{H} - 6 \rightarrow \text{L}$ (33%), $\text{H} \rightarrow \text{L} + 5$ (17%), $\text{H} \rightarrow \text{L} + 9$ (12%)</td>
    </tr>
    <tr>
      <td>$S_0 \rightarrow S_{15}$</td>
      <td>217</td>
      <td>5.70</td>
      <td>0.3169</td>
      <td>$\text{H} - 4 \rightarrow \text{L}$ (18%), $\text{H} - 3 \rightarrow \text{L} + 1$ (14%), $\text{H} \rightarrow \text{L} + 10$ (17%),</td>
    </tr>
    <tr>
      <td>BPVB</td>
      <td>$S_0 \rightarrow S_{12}$</td>
      <td>237</td>
      <td>5.22</td>
      <td>2.0157</td>
      <td>$\text{H} \rightarrow \text{L} + 1$ (70%)</td>
    </tr>
    <tr>
      <td>BDDP</td>
      <td>$S_0 \rightarrow S_1$</td>
      <td>372</td>
      <td>3.34</td>
      <td>2.5539</td>
      <td>$\text{H} \rightarrow \text{L}$ (88%)</td>
    </tr>
    <tr>
      <td rowspan="2">BDDP1</td>
      <td>$S_0 \rightarrow S_{14}$</td>
      <td>220</td>
      <td>5.64</td>
      <td>0.7603</td>
      <td>$\text{H} - 3 \rightarrow \text{L}$ (21%), $\text{H} \rightarrow \text{L} + 6$ (27%), $\text{H} \rightarrow \text{L} + 11$ (20%)</td>
    </tr>
    <tr>
      <td>$S_0 \rightarrow S_1$</td>
      <td>373</td>
      <td>3.33</td>
      <td>2.589</td>
      <td>$\text{H} \rightarrow \text{L}$ (88%)</td>
    </tr>
    <tr>
      <td rowspan="3">BDDA</td>
      <td>$S_0 \rightarrow S_{10}$</td>
      <td>242</td>
      <td>5.13</td>
      <td>0.2355</td>
      <td>$\text{H} - 1 \rightarrow \text{L} + 1$ (17%), $\text{H} - 1 \rightarrow \text{L} + 3$ (16%), $\text{H} \rightarrow \text{L} + 7$ (30%)</td>
    </tr>
    <tr>
      <td>$S_0 \rightarrow S_{17}$</td>
      <td>220</td>
      <td>5.64</td>
      <td>0.4456</td>
      <td>$\text{H} - 4 \rightarrow \text{L}$ (28%), $\text{H} - 1 \rightarrow \text{L} + 4$ (17%), $\text{H} \rightarrow \text{L} + 12$ (35%)</td>
    </tr>
    <tr>
      <td>$S_0 \rightarrow S_1$</td>
      <td>409</td>
      <td>3.03</td>
      <td>1.6444</td>
      <td>$\text{H} \rightarrow \text{L}$ (63%)</td>
    </tr>
    <tr>
      <td rowspan="3">BFMB</td>
      <td>$S_0 \rightarrow S_3$</td>
      <td>336</td>
      <td>3.69</td>
      <td>0.6204</td>
      <td>$\text{H} - 2 \rightarrow \text{L}$ (26%), $\text{H} \rightarrow \text{L} + 2$ (41%)</td>
    </tr>
    <tr>
      <td>$S_0 \rightarrow S_{14}$</td>
      <td>254</td>
      <td>4.88</td>
      <td>3.2896</td>
      <td>$\text{H} - 4 \rightarrow \text{L}$ (21%), $\text{H} - 3 \rightarrow \text{L} + 1$ (20%), $\text{H} \rightarrow \text{L} + 4$ (21%)</td>
    </tr>
    <tr>
      <td>$S_0 \rightarrow S_1$</td>
      <td>377</td>
      <td>3.28</td>
      <td>2.1129</td>
      <td>$\text{H} \rightarrow \text{L}$ (83%)</td>
    </tr>
    <tr>
      <td rowspan="4">BMVB</td>
      <td>$S_0 \rightarrow S_6$</td>
      <td>271</td>
      <td>4.57</td>
      <td>0.1472</td>
      <td>$\text{H} - 6 \rightarrow \text{L}$ (25%), $\text{H} - 2 \rightarrow \text{L} + 2$ (26%), $\text{H} - 1 \rightarrow \text{L} + 3$ (25%)</td>
    </tr>
    <tr>
      <td>$S_0 \rightarrow S_{14}$</td>
      <td>243</td>
      <td>5.10</td>
      <td>1.1505</td>
      <td>$\text{H} - 6 \rightarrow \text{L}$ (25%), $\text{H} \rightarrow \text{L} + 4$ (16%)</td>
    </tr>
    <tr>
      <td>$S_0 \rightarrow S_1$</td>
      <td>361</td>
      <td>3.43</td>
      <td>2.5487</td>
      <td>$\text{H} \rightarrow \text{L}$ (82%)</td>
    </tr>
    <tr>
      <td>$S_0 \rightarrow S_{11}$</td>
      <td>230</td>
      <td>5.39</td>
      <td>0.1207</td>
      <td>$\text{H} - 2 \rightarrow \text{L}$ (12%), $\text{H} - 1 \rightarrow \text{L} + 2$ (11%), $\text{H} \rightarrow \text{L} + 3$ (16%)</td>
    </tr>
    <tr>
      <td></td>
      <td>$S_0 \rightarrow S_{14}$</td>
      <td>224</td>
      <td>5.54</td>
      <td>0.2665</td>
      <td>$\text{H} - 6 \rightarrow \text{L}$ (34%), $\text{H} \rightarrow \text{L} + 4$ (12%), $\text{H} \rightarrow \text{L} + 9$ (21%)</td>
    </tr>
    <tr>
      <td></td>
      <td>$S_0 \rightarrow S_{20}$</td>
      <td>215</td>
      <td>5.77</td>
      <td>0.2188</td>
      <td>$\text{H} - 4 \rightarrow \text{L}$ (27%), $\text{H} - 1 \rightarrow \text{L} + 1$ (24%)</td>
    </tr>
  </tbody>
</table>

![](./images/812594790913802242_9.jpg)

Fig. 6. Band structure and density of states of biphenyl compounds; (a) BPVB (b) BDDP (c) BDDP1 (d) BMVB (e) BDDA and (f) BFMB.

to be 4.91 meV and 6.02 meV at Γ-point . Similarly, the CBM and VBM of BDDP crystal is found at X-point and Γ-point in the Brilluoin zone with band gap value 2.36 eV. The largest band dispersion of VB and CB for BDDP crystal is computed to be 126.55 meV and 128.23 meV along ΓR and ΓX respectively. Further, largest splitting of VB and CB is found to be 170.74 meV and 201.54 meV at Γ-point and X-point respectively. For the organic crystals BDDP1, BFMB, BMVB and BDDA, the band gaps are found to be 2.35 eV, 2.40 eV, 2.26 eV and 2.28 eV respectively. The largest band dispersion of VB and CB is calculated to be 130.23 meV and 250.86 meV along ΓR and ΓM for BDDP1, 57.92 meV and 93.3 meV along ΓM and ΓX for BFMB, 77.67 meV and 44.19 meV along ΓM and ΓX for BMVB, 118.07 meV and 107.35 meV along ΓR and ΓR for BDDA. The functionalized N-groups substituted compounds (BPVB, BDDP and BDDP1) are found in the range of 2.28–2.36 eV, which are slightly larger than that of O-group substituted BMVB compound (2.26 eV). Large dispersive CB and VB characterize enhanced charge mobilities of the studied compounds [88,89]. For example, large CB in BDDP1 indicates the compound to have enhanced n-type characteristics whereas large VB in BDDA shows the p-type characteristics of the compound.

## 4. Conclusion

In summary, we studied the anisotropic charge transport properties of di-substituted biphenyl derivatives using density functional theory. Our results indicated that the substitutions of different groups such as pyridine, methoxyphenyl, fluorene and anthracene at two end position of biphenyl molecule could improved the air-stability and carrier mobility of the compounds. The IP values of all the studied compounds were found in the energy range (5.36–6.60 eV), which were good enough to held considerable air-stability properties. Substitution of electron-withdrawing groups in pyridine based compounds, BPVB, BDDP and BDDP1 was found to increase the value of $V_{\text{eff}}^{e}$ as compared to those of the other crystals substituted with electron-donating groups, which indicated the fact that the electron transfer rate in the former groups of crystals is more than the hole transfer rate. It was noted that except BPVB, the value of $V_{\text{eff}}^{e}$ was larger than $V_{\text{eff}}^{h}$ for all the compounds along P channels, whereas along T channels, $V_{\text{eff}}^{h}$ was found larger than $V_{\text{eff}}^{e}$ in the cases of BDDP, BDDP1 and BDDA. The Hirshfeld Surface analysis depicting the distribution of surface charge in between the molecular layers of the crystals revealed that the principal interactions were mostly due to the C···H/H···C and H···H contacts for all the studied crystals. The computed anisotropic electron mobilities ($\mu_{\phi}^{e}$) in BDDP, BDDP1, BFMB, BMVB crystals were found to be larger than the hole mobilities ($\mu_{\phi}^{h}$), whereas, in other crystals, $\mu_{\phi}^{h}$ were found relatively more. The band gap ($E_{g}$) of the crystals BPVB, BDDA, BDDP, BDDP1, BMVB and BFMB were found to be in the energy range 2.3–2.4 eV. The UV-visible absorption spectra of all studied compounds were found to be in the wavelength region of 192–409 nm and showed bathochromic shift as compared to bare biphenyl compound. The studied derivatives are observed to be shifted towards red as compared to the biphenyl. The excitation energy and electronic HOMO–LUMO gap > 3 eV inferred the compounds to be wide band gap semiconductors.

## Conflict of interest

The authors declare that there is no conflict of interest regarding the publications of this manuscript.

## Acknowledgement

S. Sahu gratefully acknowledges Indian Institute of Technology (ISM), Dhanbad.

## Appendix A. Supplementary data

Supplementary data associated with this article can be found, in the online version, at https://doi.org/10.1016/j.synthmet.2020.116474.

## References

[1] L.L. Chua, J. Zaumseil, J.F. Chang, E.C.Kl. Ou, P.K.H. Ho, H. Sirringhaus, R.H. Friend, Nature 434 (2005) 194–199.
[2] M. Muccini, Nat. Mater. 5 (2006) 605–613.
[3] Y. Shirota, H. Kageyama, Chem. Rev. 107 (2007) 953–1010.
[4] R.H. Friend, R.W. Gymer, A.B. Holmes, J.H. Burroughes, R.N. Marks, C. Taliani, D.D.C. Bradley, D.A. Dos Santos, J.L. Bredas, M. Logdlund, W.R. Salaneck, Nature 397 (1999) 121–128.
[5] J.H. Yun, S. Park, J.H. Heo, H.S. Lee, S. Yoon, J. Kang, S.H. Im, H. Kim, W. Lee, B.S. Kim, M.J. Ko, D.S. Chung, H.J. Son, Chem. Sci. 7 (2016) 6649–6661.
[6] Y. Olivier, V. Lemaurr, J.L. Bredas, J. Cornil, J. Phys. Chem. A 110 (2006) 6356–6364.
[7] E.F. Valeev, V. Coropceanu, D.A. da Silva Fihlo, S. Salman, J.L. Bredas, J. Am. Chem. Soc. 128 (2006) 9882–9886.
[8] Y. Yamashita, Sci. Technol. Adv. Mater. 10 (2009) 24313.
[9] M.M. Torrent, C. Rovira, Chem. Rev. 111 (2011) 4833–4856.
[10] H. Sirringhaus, T. Sakanoue, T.F. Chang, Phys. Status Solidi B 249 (2012) 1655–1676.
[11] H. Lin, F. Bai, Wiley-VCH Verlag GmbH & Co. KGaA (2013) 1.
[12] H. Sun, A. Putta, M. Billion, J. Phys. Chem. A 116 (2012) 8015–8022.
[13] L. Zhang, A. Fonari, Y. Liu, A.L.M. Hoyt, H. Lee, D. Granger, S. Parkin, T.P. Russell, J.E. Anthony, J.L. Bredas, V. Coropceanu, A.L. Briseno, J. Am. Chem. Soc. 136 (2014) 9248–9251.
[14] R. Mondal, C. Tonshoff, D. Khon, D.C. Neckers, H.F. Bettinger, J. Am. Chem. Soc. 131 (2009) 14281–14289.
[15] S.A. Arabi, J. Dong, M. Mirza, P. Yu, L. Wang, J. He, C. Jiang, Cryst. Growth Des. 16 (2016) 2624–2630.
[16] H. Dong, C. Wang, W. Hu, Chem. Commun. 46 (2010) 5211–5222.
[17] H. Koezuka, A. Tsumura, T. Ando, Synth. Met. 18 (1987) 699–704.
[18] K. Bhattacharyya, T.K. Mukhopadhyay, A. Datta, Phys. Chem. Chem. Phys. 18 (2016) 14886–14893.
[19] J. Takeya, M. Yamagishi, Y. Tominari, R. Hirahara, Y. Nakazawa, T. Nishikawa, T. Kawase, T. Shimoda, S. Ogawa, Appl. Phys. Lett. 90 (2007) 102120.
[20] O.D. Jurchescu, J. Baas, T.T.M. Palstra, Appl. Phys. Lett. 84 (2004) 3061–3063.
[21] Y. Yuan, G. Giri, A.L. Ayzner, A.P. Zoombelt, S.C.B. Mannsfeld, J. Chen, D. Nordlund, M.F. Toney, J. Huang, Z. Bao, Nat. Commun. 5 (2014) 3005.
[22] Y.R. Shi, H.L. Wei, X.B. Jia, Y.F. Liu, J. Mater. Sci. 53 (2018) 15569–15587.
[23] U. Purushotham, G.N. Sastry, Phys. Chem. Chem. Phys. 15 (2013) 5039–5048.
[24] C.C. Liu, S.W. Mao, M.Y. Kuo, J. Phys. Chem. C 114 (2010) 22316–22321.
[25] W.S. Liu, C.C. Liu, M.Y. Kuo, Chem. Eur. J. 15 (2009) 5896–5900.
[26] Y. Chang, M. Kuo, C. Chen, H. Lu, I. Chao, J. Phys. Chem. C 114 (2010) 11955–11601.
[27] L. Wang, J. Dai, Y. Song, Int. J. Quant. Chem. 119 (2019) e25824.
[28] T. He, X. Zhang, J. Jia, Y. li, X. Tao, Adv. Mater. 24 (2012) 2171–2175.
[29] H.Z. Gao, Synth. Met. 160 (2010) 2104–2108.
[30] A. Valaboju, K.C. Gunturu, B. Kotamarthi, D. Joly, M. Hissler, Comput. Theor. Chem. 1113 (2017) 61–71.
[31] L.H. Yuan, C. Liang, Q. Juan, D. Lian, Z.D. Qiang, D.G. Fang, W.L. Duo, Q. Yong, Sci. China Chem. 55 (2012) 2428–2432.
[32] B. Maiti, K. Wang, S. Bhandari, S.D. Bunge, R.J. Twieg, B.D. Dunietz, J. Mater. Chem. C 7 (2019) 3881–3888.
[33] D. Liu, H. Xu, X. Liu, X. Xie, B. Yang, Y. Ma, Chem. Phys. Lett. 514 (2011) 174–180.
[34] K. Okumoto, Y. Shirota, Mater. Sci. Eng.: B 85 (2001) 135–139.
[35] Y.Y. Noh, R. Azumi, M. Goto, B.J. Jung, E. Lim, H.K. Shim, Y. Yoshida, K. Yase, D.Y. Kim, Chem. Mater. 17 (2005) 3861–3870.
[36] Y.X. Li, J. Jiac, X.T. Tao, CrystEngCommun 14 (2012) 2843–2848.
[37] H. Gao, J. Mol. Struct. 962 (2010) 80–84.
[38] J. Li, S.C. Dong, A. Opitz, L.S. Liao, N. Koch, J. Mater. Chem. C 5 (2017) 6989–6996.
[39] P. Lu, H. Zhang, M. Li, Y. Zheng, Y. Ma, X. Chen, N. Tamai, Polym. Int. 57 (2008) 987–994.
[40] S. Carturan, A. Quaranta, G. Maggioni, M. Bonafini, G. Della Mea, Sens. Actuators A 113 (2004) 288–292.
[41] D. Ray, K.L. Narasimhan, Appl. Phys. Lett. 91 (2007) 93516.
[42] W. Li, Fe. Guo, H. Ling, H. Liu, M. Yi, P. Zhang, W. Wang, L. Xie, W. Huang, Small 14 (2017) 1701437.
[43] F. Yan, H.H. Liu, W.L. Li, B. Chu, Z.S. Su, G. Zhang, Y.R.C.J.Z. Zhu, D.F. Yang, J.B. Wang, Appl. Phys. Lett. 95 (2009) 253308.
[44] H.G. Li, G. Wu, M.M. Shi, H.Z. Chen, M. Wang, Synth. Met. 160 (2010) 1648–1653.
[45] L.D. Mei, Z. Qiong, A.M.S. Hossain, S. Mei, W.J. Ying, Y.J. Xiang, Z.H. Ping, T.L. Min, W.C. Kui, T.Y. Peng, Sci. China Chem. 54 (2011) 730–736.
[46] J.X. Qiu, Y.X. Li, X.F. Yang, Y. Nie, Z.W. Zhang, Z.H. Chen, G.X. Sun, J. Mater. Chem. C 2 (2014) 5954–5962.
[47] J.L. Zhang, Y.X. Nan, H.G. Li, W.M. Qiu, X. Yang, G. Wu, H.Z. Chen, M. Wang, Sens. Actuators B 162 (2012) 321–326.
[48] W.Q. Deng, L. Sun, J.D. Huang, S. Chai, S.H. Wen, K.L. Han, Nat. Protoc. 10 (2015) 632–642.
[49] G.R. Hutchison, M.A. Ratner, T.J. Marks, J. Am. Chem. Soc. 127 (2005) 2339–2350.
[50] S.H. Wen, A. Li, J.L. Song, W.Q. Deng, K.L. Han, W.A. Goddard, J. Phys. Chem. B 113 (2009) 8813–8819.
[51] J.D. Huang, S.H. Wen, W.Q. Deng, K.L. Han, J. Phys. Chem. B 115 (2011) 2140–2147.

[52] H.L. Wei, Y.F. Liu, Appl. Phys. A 116 (2014) 1711-1717.

[53] K. Ono, T. Hiei, K. Saito, Heterocycles 68 (2006) 667-672.

[54] H.J. Liu, X.T. Tao, H.P. Zhao, W.T. Yu, M.H. Jiang, Acta. Crystallogr., Sec. E 62 (2006) o5319.

[55] Y.F. Li, F.F. Jian, Acta. Crystallogr., Sec. E 65 (2009) o1930.

[56] G. Neculqueo, V.R. Fuentes, A.L.R. Matute, S.O. Vasquez, F. Martinez, Struct. Chem. 23 (2012) 1751-1760.

[57] S.R. Sahoo, S. Sharma, S. Sahu, J. Mol. Mod. 26 (2020) 14.

[58] http://www.sg-chem.net.

[59] Y. Hu, J. Yin, K. Chaitanya, X.H. Ju, Comput. Theor. Chem. 1072 (2015) 63-71.

[60] M.J. Frisch, G.W. Trucks, H.B. Schlegel, G.E. Scuseria, M.A. Robb, J.R. Cheeseman, G. Scalmani, V. Barone, B. Men- nucci, G.A. Petersson, H. Nakatsuji, M. Caricato, X. Li, H.P. Hratchian, A.F. Izmaylov, J. Bloino, G. Zheng, J.L. Sonnen- berg, M. Hada, M. Ehara, K. Toyota, R. Fukuda, J. Hasegawa, M. Ishida, T. Nakajima, Y. Honda, O. Kitao, H. Nakai, T. Vreven, J.A. Montgomery Jr., J.E. Peralta, F. Ogliaro, M. Bearpark, J.J. Heyd, E. Brothers, K.N. Kudin, V.N. Staroverov, R. Kobayashi, J. Normand, K. Raghavachari, A. Rendell, J.C. Burant, S.S. Iyengar, J. Tomasi, M. Cossi, N. Rega, J.M. Millam, M. Klene, J.E. Knox, J.B. Cross, V. Bakken, C. Adamo, J. Jaramillo, R. Gomperts, R.E. Stratmann, O. Yazyev, A.J. Austin, R. Cammi, C. Pomelli, J.W. Ochterski, R.L. Martin, K. Morokuma, V.G. Zakrzewski, G.A. Voth, P. Salvador, J.J. Dannenberg, S. Dap- prich, A.D. Daniels, Ö. Farkas, J.B. Foresman, J.V. Ortiz, J. Cioslowski, D.J. Fox, Gaussian 09, Revision E. 01, Gaussian Inc, Wallingford, CT, 2013.

[61] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865-3868.

[62] P. Blaha, K. Schwarz, G.K.H. Madsen, D. Kvasnicka, J. Luitz, Karlheinz Schwarz, Techn. Universität Wien, Austria, 2001.

[63] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188-5192.

[64] http://hirshfeldsurface.net.

[65] G. Lu, H. Usta, C. Risko, L. Wang, A. Facchetti, M.A. Ratner, T.J. Marks, J. Am. Chem. Soc. 130 (2008) 7670-7685.

[66] A. Lv, S.R. Puniredd, J. Zhang, Z. Li, H. Zhu, W. Jiang, H. Dong, Y. He, L. Jiang, Y. Li, W. Pisula, Q. Meng, W. Hu, Z. Wang, Adv. Mater. 24 (2012) 2626-2630.

[67] J.X. Fan, L.F. Ji, N.X. Zhang, P.P. Lin, G.Y. Qin, S.F. Zhang, A.M. Ren, New J. Chem. 43 (2019) 3583-3600.

[68] K. Zhou, H. Dong, H.L. Zhang, W. Hu, Phys. Chem. Chem. Phys. 16 (2014) 22448-22457.

[69] L.F. Ji, J.X. Fan, S.F. Zhang, A.M. Ren, Phys. Chem. Chem. Phys. 19 (2017) 13978-13993.

[70] P. Venkatesan, S. Thamotharan, A. Ilangovan, H. Liang, T. Sundius, Spectrochim. Acta A 153 (2016) 625-636.

[71] M.A. Spackman, P.G. Byrom, Chem. Phys. Lett. 267 (1997) 215-220.

[72] M.A. Spackman, D. Jayatilaka, CrystEngCommun 11 (2009) 19-32.

[73] Z.F. Yao, J.Y. Wang, J. Pei, Cryst. Growth Des. 18 (2018) 7-15.

[74] A.D. Martin, J. Britton, T.L. Esun, A.J. Blake, W. Lewis, M. Schroder, Cryst. Growth Des. 15 (2015) 1697-1706.

[75] P.P. Lin, S.F. Zhang, N.X. Zhang, J.X. Fan, L.F. Ji, J.F. Guo, A.M. Ren, Phys. Chem. Chem. Phys. 21 (2019) 3044-3058.

[76] H. Gao, Theor. Chem. Acc. 127 (2010) 759.

[77] H. Oberhofer, K. Reuter, J. Blumberger, Chem. Rev. 117 (2017) 10319-10357.

[78] R.A. Klenkler, G. Voloshin, J. Phys. Chem. C 115 (2011) 16777-16781.

[79] B. Li, J. Chen, Y. Zhao, D. Yang, D. Ma, Org. Elect. 12 (2011) 974-979.

[80] R. Rohloff, N.B. Kotadiya, N.I. Craciun, P.W.M. Blom, G.A.H. Wetzelaer, Appl. Phys. Lett. 110 (2017) 73301.

[81] Y.G. Han, G. Wu, H.Z. Chen, M. Wang, J. Mater. Sci. 43 (2008) 1044-1049.

[82] K. Bhattacharyya, A. Datta, J. Phys. Chem. C 121 (2017) 1412-1420.

[83] C.A. Draxl, K. Hummer, S. Sagmeister, P. Puschnig, Chem. Phys. 325 (2006) 3-8.

[84] R. Fukuda, M. Ehara, Phys. Chem. Chem. Phys. 15 (2013) 17426-17434.

[85] J.S.A. Ishibashi, C. Darrigan, A. Chrostowska, B. Li, S.Y. Liu, Dalton Trans. 48 (2019) 2807-2812.

[86] J.H. Mokkath, Phys. Chem. Chem. Phys. 21 (2019) 448-454.

[87] L. Yan, F. Popescu, M.R. Rao, H. Meng, D.F. Perepichka, Adv. Electron. Mater. 3 (2017) 1600556.

[88] T.P. Nguyen, J.H. Shim, Phys. Chem. Chem. Phys. 18 (2016) 13888-13896.

[89] M. Hammouri, T.M. Garcia, C. Cook, S. Monaco, S. Jezowski, N. Marom, B. Schatschneider, J. Phys. Chem. C 122 (2018) 23828-23844.