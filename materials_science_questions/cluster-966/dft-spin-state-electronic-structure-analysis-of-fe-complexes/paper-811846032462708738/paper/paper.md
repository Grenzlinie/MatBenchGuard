# Modeling the Oxygen activation on Dinuclear Iron MMO Mimics,
## a Quantum Mechanic Study

Peter-Paul H. J. M. Knops-Gerrits $^{a,b*}$, Peter A. Jacobs $^{b}$ & William A. Goddard III $^{a}$

$^{a}$Material & Process Simulation Center, Beckman Institute (139-74),
California Inst. of Technology, Pasadena CA 91125, USA
Tel 626-395-2731, Fax 626-585-0918, email ppkg@wag.caltech.edu

$^{b}$Center for Surface Science and Catalysis, Katholieke Universiteit Leuven,
Kardinaal Mercierlaan 92, B-3001 Heverlee, Belgium,
Tel: 32-16-32 1597; Fax : 32-16-32 1998, email ppkg@agr.kuleuven.ac.be

Methane Mono-Oxygenase (MMO) is a di-iron active site containing enzyme that catalyzes the dissociative binding of molecular oxygen. To mimic the MMO active site we chose to study the heptapodate coordinated binuclear iron (II or III)-complexes of $N,N,N',N'$-tetrakis(2-benzimidazolylmethyl)-2-hydroxy-1,3-diamino-propane (HPTB), $N,N,N',N'$-Tetrakis(2-pyridylmethyl)-2-hydroxy-1,3-diamino-propane (HPTP) in experiments and their finite cluster model $N,N,N',N'$-Tetrakis(2-iminomethyl)-2-hydroxy-1,3-diamino-propane (HPTM) in theoretical calculations. These have active sites of the form $[Fe_2(HPTL)(\mu-OH)]^{4+}$ or $^{2+}$. Quantum Mechanic structures are compared with experimental EXAFS data. For the $O_2$ binding on the reduced active site the $\mu-\eta^1:\eta^1-O_2$ mode seems to proceed formation of the O=Fe-O-Fe=O bis-ferryl active site that reacts exothermally with methane. The nature of the ferryl groups are these of a reactive two center three electron bond.

## 1. INTRODUCTION

Methane Mono-Oxygenase (MMO) [1] and Deoxyhemerythrin [2] are examples of diiron enzymes that catalyze the dissociative and non-dissociative binding of molecular oxygen. Dissociative binding of oxygen via a peroxo intermediate to a diamond core structure [3] leads to a reactive species active in the oxidation of alkanes [4-5]. Non-dissociative binding of oxygen via a side-on peroxo intermediate such as in the active site of deoxy-hemerythrin does not allow the splitting and allows binding/release of oxygen as a function of the physiological conditions [2]. These active sites are among the growing list related to O- and OH-bridged di- or poly-iron cores in biological systems [8-9].

MMO has a binuclear iron active site with two histidines and four glutarates. Both iron ions are coordinated by a histidine, an oxygen from a bridging carboxylate and a $\mu$-oxo bridge [5]. Theoretical modeling of such enzyme active sites has been recently reported [10-16]. Yoshizawa *et al.* studied the dioxygen cleavage and methane activation on diiron enzyme models with the extended Hückel method, an approximate molecular orbital method, the $\mu$-$\eta^1:\eta^1-O_2$ or $\mu-\eta^2:\eta^2-O_2$ binding modes are distorted to the corresponding dioxygen complex. The $\mu-\eta^1:\eta^1-O_2$ mode is more effective for electron transfer to the d-block orbitals. Regarding methane activation Crabtree [11] reviewed the recent data. According to Siegbahn *et al.* [12].

the most significant structure is the $Fe^{III}$-O-$Fe^{V}$=O oxo structure. The ground state of this structure is $^{11}$A and the iron spins are 4.00 and 2.94, the spin on the bridging oxygen is 0.76 and on the oxo ligand is as high as 1.13. In reactions with ethane there is 35% of inversion of configuration, the 65% that remains unchanged is difficult to realize if free radicals have more than a transient existence. The mimicking of MMO by immobilization of the model complexes in the voids of clays or mesoporous silica and silica-alumina has been our ongoing interest [21-23]. The characterization and theoretical quantum structure of $[Fe_{2}(HPTP)(\mu-OH)(NO_{3})_{2}](ClO_{4})_{2}$ (1) and $[Fe_{2}(HPTB)(\mu-OH)(NO_{3})_{2}]\ (ClO_{4})_{2}$ (2) and their oxygen and methane activation, is investigated here.

## 2. EXPERIMENTAL
### 2.1.SYNTHESIS
#### 2.1.1.$[Fe_{2}(HPTB)(OH)(NO_{3})_{2}](NO_{3})_{2}$
N,N,N',N'-tetrakis(2-benzimidazolylmethyl))-2-hydroxy-1,3-diaminopropane (HPTB) is prepared [8-9]. To an ethanol solution of $Fe(NO_{3})_{3}.6H_{2}O$ (0.31 g) the HL (0.30 g) is added and the precipitated complex is collected.

#### 2.1.2.$[Fe_{2}(HPTP)(OH)(NO_{3})_{2}](ClO_{4})_{2}$
N,N,N',N',-tetrakis(2-pyridylmethyl)-2-hydroxy -1,3-diamino-propane H(HPTP)* as perchlorate is prepared from p-chloropicoline and 2-hydroxy-1,3-diamino-propane after [10]. As in the previous synthesis, $Fe(NO_{3})_{3}.6H_{2}O$ (0.31 g) and $H(HPTP)(ClO_{4})_{2}$ (0.28 g) are solved in ethanol. The complex is washed with acetonitrile/diethylether and recrystallised in diethylether.

![](./images/811846032462708738_1.jpg)

Figure 1. Structure of $[Fe_{2}(HPTM)(O_{2})]^{3+}$ optimized by Quantum Mechanics.

### 2.2.COMPUTATIONAL ANALYSIS
The *ab initio* calculations used involve full geometry optimization of the clusters with density functional theory (dft) as implemented in Jaguar [15] (Jaguar 3.0, Schrodinger, *Inc.*, Portland, Oregon, 1997) at the B3LYP method level (Becke3 hybridization functionals, Slater/Becke88 non-local exchange and Li, Yang, Parr local and nonlocal correlation corrections to the local potential energy functionals of Vosko, Wilk and Nusair ) using the Los Alamos effective core potential and valence double Zeta for iron ( LACVP** basis sets ).
The molecular mechanics calculations involve a new molecular mechanics force field, the Universal force field (UFF) of Rappé *et al.* [13-14]. The force field parameters are estimated using general rules based only on the element, its hybridization and its connectivity. The force field functional forms, parameters, and generating formulas for the full periodic table have

been published [13]. For charge equilibration used in molecular dynamics simulations the charges in the complexes were determined [16] to readjust charges based on geometry and experimental atomic properties. The initial structures were energy minimized using suitable sets of parameters appended to UFF, to better describe coordination around iron.

The quantum mechanical study was performed at the *ab initio* level starting from a UFF optimized structure. UFF minimization is carried out on an Origin2000 machine. (16 MIPS R10000 (IP27) CPU's, 195 MHz w/4 MB secondary cache each, with an IRIX 6.4_S2MP + OCTANE operating system) using a Newton-Raphson minimization scheme with a norm of the gradient convergence criteria of $1 \times 10^{-10}$ kcal/ mol/ Å. In order to accommodate iron in five coordinate form, according to EXAFS data, after UFF optimization a QM calculation is performed. Atom types for iron and other transition metals in the UFF is given with its symbol, hybridization geometry and valence state. UFF contains 126 atom types, the force constants are generated using Badgers rules as described, the van der Waals parameters are computed based on a Lennard-Jones type potential [13-14].

## 3.RESULTS AND DISCUSSION
### 3.1. EXAFS SPECTROSCOPY
The Fe K-edge EXAFS-XANES analysis gives direct information of the coordination environment of the complexes as salts. The Fe K-edge XAS on $[Fe_{2}(HPTP)(\mu-OH)(NO_{3})_{2}](NO_{3})_{2}$ and $[Fe_{2}(HPTB)(\mu-OH)(NO_{3})](NO_{3})_{2}$ show pre-edge features indicative of a distorted five coordinated iron with a sixth Fe ligand, the edge-shifts of 13.1 eV and 15.5 eV are characteristic for its high spin ferric form. The Fe K-edge EXAFS indicates that the $[Fe_{2}(L)(\mu-OH)]^{4+}$ gives a coordination number (CN) of 1 for the Fe-Fe bonding and an Fe-Fe distance of $3.020 \mathring{A}$ for L=HPTP and of $3.223 \mathring{A}$ for L=HPTB in accordance with the crystallographic data [18-19]. For complexes with less bulky ligands e.g. HPTP the two species in the Mossbauer spectra are observed, i.e. a $\mu$-OH and a $\mu$-O species. Shorter Fe-OH inter-atomic distances are seen of 1.92-1.99 $\mathring{A}$ with EXAFS compared with computations and crystallographic structures [5]. The HPTP pyridine and amine groups give Fe-N bonds of 2.11 $\mathring{A}$ and 2.327 $\mathring{A}$. The HPTB benzimidazole and amine groups give Fe-N bonds of 2.185 $\mathring{A}$ and 2.384 $\mathring{A}$. The large Debye-Waller factor arises from many different species in the samples.

### 3.2. COMPUTATIONAL ANALYSIS
1. **Modeling the Structures.** The $[Fe_{2}(HPTP)(\mu-OH)]^{4+}$ (1), and $[Fe_{2}(HPTB)(\mu-OH)]^{4+}$ (2) complexes are used in catalysis. These are models that have a structure that combines all the features of the ligand and iron active site. The $[Fe_{2}(HPTM)(\mu-OH)]^{4+}$ complex was used in the calculations and an imine group is positioned where a pyridine or a benzimidazole occur in the actual ligands as seen in Figure 1. Both the ferric $[Fe_{2}(HPTM)(\mu-OH)]^{4+}$ and the ferrous $[Fe_{2}(HPTM)(\mu-OH)]^{2+}$ cores are then optimized with Quantum Mechanics (QM). The QM optimized structure of $[Fe_{2}(HPTM)(\mu-OH)]^{4+}$ is reacted with oxygen in an acidic medium to give intermediates P and Q . [21]. The charge of the $[Fe_{2}(HPTM)(\mu-OH)]^{X+}$ cluster is +4 or +2, depending on the simulation of a Fe(III) or an Fe(II) active site and the energy levels of different multiplicity are studied. The relative energies of some important catalytic reactants were analyzed, as are the effects of their solvation again obtained by QM calculations. In UFF due to the change of a ferrous to a ferric type the decrease in the bond-length and the increase in the force constant for the Fe-X distances are seen and some changes in the angle bending parameters are observed. Only a slight increase is seen for the angles of the N_2 from 111.2 to

$111.3\ ^{\circ}$, these for the O_R increase from the standard 110 to 128.0 and $126.4\ ^{\circ}$ in the diferric core. Also, a decrease of the O_R Fe O_R angle can be seen from 90 to $74,5\ ^{\circ}$. The N_2 Fe3+3 N_2 angles remain constant at $109.47\ ^{\circ}$. The complex has $C_{2h}$ symmetry and both ferrous ions occur either in a high-spin quintet state, and intermediate-spin triplet state or a low-spin singlet state. When these states couple we obtain a nonuplet state if the two iron ions are high-spin, the quintet state Q if the two iron ions are intermediate-spin, or singlet S when the two iron ions are in low-spin form.

$\mathrm{N}\ \ (\mathrm{dxz})^{2}\ (\mathrm{dxy})^{1}(\mathrm{dyz})^{1}(\mathrm{dz}^{2})^{1}(\mathrm{dx}^{2}\mathrm{-y}^{2})^{1}\ \ \mathrm{Q}\ \ (\mathrm{dxz})^{2}\ (\mathrm{dxy})^{2}(\mathrm{dyz})^{1}(\mathrm{dz}^{2})^{1}$
$\mathrm{S}\ \ (\mathrm{dxz})^{2}\ (\mathrm{dxy})^{2}(\mathrm{dyz})^{2}$

The ferric ions occur either in a high-spin sextet state, and intermediate-spin quartet state or a low-spin doublet state. When these states couple we obtain the undecuplet state if the two iron ions are high-spin, the septet state SP if the two iron ions are intermediate-spin, or triplet T when the two iron ions are in low-spin form.

$\mathrm{U}\ \ (\mathrm{dxz})^{1}\ (\mathrm{dxy})^{1}(\mathrm{dyz})^{1}(\mathrm{dz}^{2})^{1}(\mathrm{dx}^{2}\mathrm{-y}^{2})^{1}\ \ \mathrm{SP}\ \ (\mathrm{dxz})^{2}\ (\mathrm{dxy})^{1}(\mathrm{dyz})^{1}(\mathrm{dz}^{2})^{1}$
$\mathrm{T}\ \ (\mathrm{dxz})^{2}\ (\mathrm{dxy})^{2}(\mathrm{dyz})^{1}$

In the ferric case ($\mathrm{Fe^{III}}$) the septet (SP) and the undecuplet (U) are its ground state and low lying exited states. The equatorial (trans) and axial (cis) effect of the N atoms with respect to the bridging $\mu$-oxo groups dictate their bond lengths that are 2.03-2.04 Å, 2.31 Å and 1.95-1.99 Å respectively. The distances of 1.95 and 1.99 Å obtained from QM seen in the direction of the equatorial unprotonated and protonated O groups compared to the calculations, are accompanied by Fe-O-Fe angles of $90$-$93^{\circ}$ and an O-Fe-O bite angle of $74.5^{\circ}$.

2. Modeling the Oxygen Activation. Geometrical en electronic properties affect the relative catalytic properties such as the hydrogen bond abstraction energies of the binuclear cores of these iron complexes. In the QM optimized structure the iron core has two $\mu$-oxo and six terminating nitrogen atoms. In acid aqueous reactions, the bridging by a deprotonated ligand alcohol group remains strong, the bridging ($\mu$-OH) can be protonated and removed as water. This helps the binding of molecular oxygen and the consequent transformation into a peroxo ($\mathrm{O_{2}^{2-}}$) group (P) with formal change of charge of iron from +2 to +3. This leads to a diamagnetic singlet state $\mathrm{S}\ (\mathrm{dxz})^{2}\ (\mathrm{dxy})^{2}\ (\mathrm{dyz})^{1}(\mathrm{O}_{2}\pi)^{1}\ (\mathrm{dz}^{2})^{1}(\mathrm{O}_{2}\sigma)^{1}$ here the dyz orbital is coupled to the two orthogonal three electron pi-system of the $\mathrm{O_{2}}$ ligands. An alternative is a paramagnetic quintet state $\mathrm{Q}\ (\mathrm{dx^{2}-y^{2}})^{1}(\mathrm{dxz})^{2}(\mathrm{dxy})^{1}(\mathrm{dyz})^{1}(\mathrm{O}_{2}\pi)^{1}\ (\mathrm{dz}^{2})^{1}(\mathrm{O}_{2}\sigma)^{1}$

The two ferryl bonds become stronger by transfer of $\sigma$ bonding electrons between the two Oxygen atoms to their anti-bonding orbitals and the pairing of these with an extra electron from the iron ion. In a consequent step the peroxo ($\mathrm{O_{2}^{2-}}$) group is transformed into two ferryl ($\mathrm{O^{2-}}$) bound groups (intermediate Q), with the formal change of the charges of iron from +3 to +4. In an alternative step the peroxo ($\mathrm{O_{2}^{2-}}$) group of the complex can also transform to yield two bridging ($\mu$-O) oxo groups. The superexchange coupling for these complexes is fairly small, this agrees with the experimental observation of a J value of $12\ \mathrm{cm^{-1}}$ for the diferrous OH bridged model compound [18-19]. The geometrical implications on these reactions are probed with QM analysis and the results are shown in Table 1 and 2. The Fe-O bond length of 1.21 Å increases to 1.31 Å on the model compound and is smaller than the 1.49 Å distance in $\mathrm{H_{2}O_{2}}$, consequently this bond is broken in the model compound. The Fe..Fe distances of 3.14 Å increases to 3.43 Å in intermediate P and 3.63 Å in intermediate Q. Upon transformation into the bis ($\mu$-$\mathrm{O^{2-}}$) oxo bridged dimer, it decreases to 2.65 Å. The peroxo form P is slightly more stable than the ferryl form Q by about 18.9 kcal/mol. The formation of the bis ($\mu$-$\mathrm{O^{2-}}$) oxo is unfavorable since it is 44.4 kcal/mol higher in energy.

<table>
 <thead>
  <tr>
   <th colspan="6">
    Table 1. Bond lengths (Å) obtained by QM calculations (ligand L= HPTM)
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    bond
   </td>
   <td>
    L O(=O)2
   </td>
   <td>
    L O(O2)
   </td>
   <td>
    L O3
   </td>
   <td>
    L O(OH)2
   </td>
   <td>
    L O(OH)
    <br/>
    (OCH₃)
   </td>
  </tr>
  <tr>
   <td>
    Fe Fe
   </td>
   <td>
    3.628
   </td>
   <td>
    3.433
   </td>
   <td>
    2.647
   </td>
   <td>
    3.639
   </td>
   <td>
    3.60
   </td>
  </tr>
  <tr>
   <td>
    Fe O
   </td>
   <td>
    1.607-1.611
   </td>
   <td>
    1.843-2.037
   </td>
   <td>
    1.824, 1.909
   </td>
   <td>
    1.724, 1.756
   </td>
   <td>
    1.729, 1.747
   </td>
  </tr>
  <tr>
   <td>
    Fe O (C)
   </td>
   <td>
    1.971-1.982
   </td>
   <td>
    1.876-2.039
   </td>
   <td>
    2.071
   </td>
   <td>
    1.958-2.008
   </td>
   <td>
    1.993-1.993
   </td>
  </tr>
  <tr>
   <td>
    O O
   </td>
   <td>
   </td>
   <td>
    1.309
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    Feᵃ N(sp²)
   </td>
   <td>
    2.020-2.034
   </td>
   <td>
    2.000-2.085
   </td>
   <td>
    1.956-2.078
   </td>
   <td>
    2.093-2.109
   </td>
   <td>
    2.010-2.072
   </td>
  </tr>
  <tr>
   <td>
    Feᵇ N(sp²)
   </td>
   <td>
   </td>
   <td>
    2.093-2.095
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
    2.031-2.071
   </td>
  </tr>
  <tr>
   <td>
    Feᵃ N(sp³)
   </td>
   <td>
    2.101-2.166
   </td>
   <td>
    2.077
   </td>
   <td>
    2.056
   </td>
   <td>
    3.120
   </td>
   <td>
    2.094
   </td>
  </tr>
  <tr>
   <td>
    Feᵇ N(sp³)
   </td>
   <td>
   </td>
   <td>
    2.270
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
    2.107
   </td>
  </tr>
  <tr>
   <td>
    O1-H1
   </td>
   <td>
    -
   </td>
   <td>
    -
   </td>
   <td>
    -
   </td>
   <td>
    0.974-0.984
   </td>
   <td>
    0.974-0.984
   </td>
  </tr>
  <tr>
   <td>
    C1-O2
   </td>
   <td>
    1.437
   </td>
   <td>
    1.435
   </td>
   <td>
    1.420
   </td>
   <td>
    1.433
   </td>
   <td>
    1.432
   </td>
  </tr>
 </tbody>
</table>

However, solvation stabilization is higher in complexes with increased charge transfer i.e. the Fe(IV) complexes are better stabilized by solvation than the Fe(III) complexes. Shaik et al. [17] showed that iron oxide cations have a high spin ground state and adjacent low spin excited state. The adjacency of the two spin states together with the poor bonding of the high spin state and the good bonding of the low spin state, leads to a spin cross-over along the reaction coordinate and opens a low-energy TSR (two state reactivity) path for hydroxylation.

<table>
 <thead>
  <tr>
   <th colspan="6">
    Table 2. Bond angles (°) obtained by QM calculations
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    bond angles
   </td>
   <td>
    HPTM
    <br/>
    O(=O)2
   </td>
   <td>
    HPTM
    <br/>
    O(O2)
   </td>
   <td>
    HPTM
    <br/>
    O3
   </td>
   <td>
    HPTM
    <br/>
    O(OH)2
   </td>
   <td>
    HPTM O
    <br/>
    (OH)(OCH₃)
   </td>
  </tr>
  <tr>
   <td>
    Fe O Fe
   </td>
   <td>
    133.2
   </td>
   <td>
    122.4
   </td>
   <td>
    79.4- 93.0
   </td>
   <td>
    133.1
   </td>
   <td>
    133.7
   </td>
  </tr>
  <tr>
   <td>
    O Fe O
   </td>
   <td>
    97.8-98.7
   </td>
   <td>
    80.3-89.9
   </td>
   <td>
    72.2- 78.2
   </td>
   <td>
    93.2-101.9
   </td>
   <td>
    95.9-99.4
   </td>
  </tr>
  <tr>
   <td>
    Fe O O
   </td>
   <td>
    -
   </td>
   <td>
    119.9-123.7
   </td>
   <td>
    -
   </td>
   <td>
    -
   </td>
   <td>
    -
   </td>
  </tr>
  <tr>
   <td>
    H O Fe
   </td>
   <td>
    -
   </td>
   <td>
    -
   </td>
   <td>
    -
   </td>
   <td>
    113.0-117.1
   </td>
   <td>
    112.2
   </td>
  </tr>
  <tr>
   <td>
    C O Fe
   </td>
   <td>
    109.9-116.8
   </td>
   <td>
    117.9-119.6
   </td>
   <td>
    116.9
   </td>
   <td>
    112.2-114.5
   </td>
   <td>
    112.7-113.3
   </td>
  </tr>
  <tr>
   <td>
    Ne-Fe-Ne
   </td>
   <td>
    115.6-115.9
   </td>
   <td>
    108.9-110.1
   </td>
   <td>
    118.0
   </td>
   <td>
    116.9-119.2
   </td>
   <td>
    117.6-117.8
   </td>
  </tr>
  <tr>
   <td>
    Na-Fe-Ne
   </td>
   <td>
    81.0-81.3
   </td>
   <td>
    81.7-83.4
   </td>
   <td>
    80.6-83.9
   </td>
   <td>
    80.0-80.7
   </td>
   <td>
    80.2-81.3
   </td>
  </tr>
 </tbody>
</table>

Na : axial nitrogen, Ne : equatorial nitrogen.

3. Modeling the Alkane Activation. Upon interaction with CH₄ the geometry of the two ferryl (O²⁻) bound groups (intermediate Q) to the ferric (Feᵢᵢᵢ-OH, Feᵢᵢᵢ-OCH₃) groups does not change substantially, the Fe..O distances change, as the system becomes more asymmetric since one OH group that is formed will show hydrogen bonding with the neighboring methoxy group. For the ground state (multiplicity 7) the bridging Fe-O distances change from 1.97 and 1.96 Å to 1.993 and 1.993 Å and the terminal Fe-O distances increase from 1.61 and 1.61 Å to 1.747 (FeᵢᵢᵢOH) and 1.729 (FeᵢᵢᵢOCH₃) Å, the CH and OH distances are 1.097, 1.096, 1.095 and 0.982 Å, respectively. Overal the reaction with methane is exothermic by 50.56 kcal/mol, the consecutive substitution of the methoxy group by a hydroxo group is endothermic by 7.50 kcal/mol and the regeneration of the active site with H₂O₂ is again endothermic by 3.24 kcal/ mol. The solvation calculations are very important to obtain good quantitative data. The solvation energy is about 150, 300 and 500 kcal/mol for the 2+, 3+ and

4+ complexes, respectively. The active bis-ferryl $\mu$-oxo-bridged site (intermediate Q) shows eight unpaired electrons. The localization of these free d-electrons occurs partially on the iron ($\text{Fe}^\text{IV}$ like with a spin density of 2.6 to 2.8) and on the oxygen (spin density of 0.80 to 0.85).

## 4. CONCLUSION.
The reaction of the MMO binuclear heptapodate coordinated iron (III)-complexes of $N,N,N',N'$-tetrakis(iminomethyl)-2-hydroxy-1,3-diamino-propane model with methane is exothermic by 50.56 kcal/mol. The $[\text{Fe}_2(\text{HPTP})(\mu\text{-OH})]^{4+}$ and $[\text{Fe}_2(\text{HPTB})(\mu\text{-OH})]^{4+}$ model complexes give a coordination number of 1 for the Fe-Fe and a distance of $3.02\ \text{\AA}$ and of 3.22 $\text{\AA}$ respectively, in accordance with the QM value of $3.135\ \text{\AA}$ obtained on the $[\text{Fe}_2(\text{HPTM})(\mu\text{-OH})]^{4+}$ model complexes. The $\sigma$- and $\pi$-bonds of the ferryl $\text{Fe=O}$ in the plane of the Fe-O-Fe bridge, have the properties of a two atom three electron bond.

## ACKNOWLEDGEMENTS
PPKG thanks the FWO-Flanders for a post-doctoral fellowship, A.Fukuoka & M.Ichikawa from the CRC, at Hokkaido University, Sapporo, Japan for a collaboration on EXAFS. PPKG and WAG wish to thank BP Amoco for financial support.

## REFERENCES
1. L., Que, Y., Dong, Acc. Chem. Res., 29 (1996) 190.
2. Loehr, T. M. Ed., Iron carriers and Proteins; VCH, Weinheim, 1989, 373.
3. L. Shu, J.C.Nesheim, K.Kauffmann, E. Munck, J.D. Lipscomb, L. Que, Jr., Science, 275 (1997) 515. 4. Y. Dong, S. Yan, V.G.Young Jr., L.Que Jr., Angew. Chem., 108 (1996) 674.
5. A.C., Rosenzweig, C.A., Frederick, S.J., Lippard, P., Nordlund, Nature, 366 (1993) 537.
6. K.E. Liu, D. Wang, B.Huynh, D. Edmonson, A. Salifoglou, S.J. Lippard, J.Am.Chem.Soc., 116 (1994) 7465. 7. K.E. Liu, A.M. Valentine, D. Qiu, D.Edmonson, E.Appelman, T.Spiro, S.J. Lippard, J.Am.Chem.Soc., 117 (1995) 4997.
8. S.J. Lippard, Angew.Chem. Int.Ed. Engl., 27 (1988) 344.
9. D.M. Kurtz, Chem. Rev., 90 (1990) 585.
10. K. Yoshizawa, K. Ohta, T. Yamabe, R. Hoffmann, J.Am.Chem.Soc., 119(1997) 12311.
11. R.H., Crabtree, Chem.Rev., 95 (1995) 987.
12. P.E., Siegbahn, R.H., Crabtree, J. Am. Chem. Soc., 119 (1997) 3103.
13. A.K. Rappe, C.J. Casewit, K.S. Colwell, W.A.Goddard, W.M.Skiff, J.Am.Chem.Soc., 114 (1992) 10024.
14. A.K., Rappe, W.A., Goddard, J. Chem. Phys., 95 (1991) 3358.
15. References in the Jaguar User Guide.
16. P.P. Knops-Gerrits, F. Faglioni, W. Goddard III, J. Am. Chem. Soc., submitted.
17. S. Shaik, M. Filatov, D., Schröder, H., Schwarz, Chem. Eur. J., 1998, 4, 193-199.
18. S. Menage, B.A.Brennan, C.Juarez-Garcia, E.Munck, L.Que, Jr, J.Am.Chem.Soc., 112 (1990) 6423. 19. R.G.Wilkins, Chem. Soc. Rev., (1992) 171-178; P.C.Wilkins, R.G.Wilkins, Coord. Chem. Rev., 79 (1987) 195-214.
20. R.E.Norman, R.C.Holz, S.Menage, L.Que, jr., J.O'Connor, Inorg. Chem., 29 (1990) 4629.
21. P.P.Knops-Gerrits, A.Weiss, S.Dick, P.Jacobs, Stud.Surf.Sci.Catal., 1997, 110, 1061.
22. P.P.Knops-Gerrits, M.Van Bavel, G.Langouche, P.Jacobs, NATO ASI 3.44 (Derouane et al. Eds.), 1998, 215.
23. P.P.Knops-Gerrits, A.Verberckmoes, R.A.Schoonheydt, M. Ichikawa, P.A. Jacobs, Micro- and Mesoporous Mat., 1998, 21, (4-6) 475.