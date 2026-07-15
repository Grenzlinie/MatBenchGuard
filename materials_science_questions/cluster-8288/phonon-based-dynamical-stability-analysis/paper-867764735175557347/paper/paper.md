# Calcium peroxide from ambient to high pressure

Joseph R. Nelson, $^{1, \ast}$ Richard J. Needs, $^{1}$ and Chris J. Pickard$^{2}$

$^{1}$Theory of Condensed Matter Group, Cavendish Laboratory,
J. J. Thomson Avenue, Cambridge CB3 0HE, United Kingdom
$^{2}$Department of Physics and Astronomy, University College London,
Gower Street, London WC1E 6BT, United Kingdom
(Dated: August 2, 2021)

Structures of calcium peroxide (CaO₂) are investigated in the pressure range 0-200 GPa using the *ab initio* random structure searching (AIRSS) method and density functional theory (DFT) calculations. At 0 GPa, there are several CaO₂ structures very close in enthalpy, with the ground-state structure dependent on the choice of exchange-correlation functional. Further stable structures for CaO₂ with $C2/c$, $I4/mcm$ and $P2_{1}/c$ symmetries emerge at pressures below 40 GPa. These phases are thermodynamically stable against decomposition into CaO and O₂. The stability of CaO₂ with respect to decomposition increases with pressure, with peak stability occurring at the CaO B1-B2 phase transition at 65 GPa. Phonon calculations using the quasiharmonic approximation show that CaO₂ is a stable oxide of calcium at mantle temperatures and pressures, highlighting a possible role for CaO₂ in planetary geochemistry. We sketch the phase diagram for CaO₂, and find at least five new stable phases in the pressure/temperature ranges $0 \leq P \leq 60$ GPa, $0 \leq T \leq 600$ K, including two new candidates for the zero-pressure ground state structure.

PACS numbers:

## INTRODUCTION

The typical oxide formed by calcium metal is calcium oxide, CaO, having Ca and O in +2 and -2 oxidation states respectively. Calcium and oxygen can also combine to form calcium peroxide, CaO₂, a compound which enjoys a variety of uses in industry and agriculture. Calcium peroxide is used as a source of chemically bound but easily evolved oxygen in fertilisers, for oxygenation and disinfection of water, and in soil remediation [1, 2].

At ambient pressure bulk calcium peroxide decomposes at a temperature of about 620 K [2, 3]. Early X-ray diffraction (XRD) experiments assigned a tetragonal 'calcium carbide' structure of space group $I4/mmm$ to CaO₂ [4]. This same structure was already known to be formed by heavier alkaline earth metal peroxides [5, 6]. Recently, Zhao *et al.* [7] used an adaptive genetic algorithm and density functional theory (DFT) calculations to search for structures of CaO₂, finding a new orthorhombic ground state structure of $Pna2_{1}$ symmetry, which is calculated to be close to thermodynamic stability at zero pressure and temperature. The simulated XRD pattern from this structure is in good agreement with the available experimental data [7]. Thermodynamic stability in this case means stability against decomposition via

$$\mathrm{CaO}_{2} \longrightarrow \mathrm{CaO} + \frac{1}{2}\mathrm{O}_{2}. \tag{1}$$

We are interested in the stabilities of structures of CaO₂ from zero pressure up to 200 GPa, and temperatures up to 1000 K. Calcium and oxygen have high abundances in the Earth's crust and mantle and, because they also have high cosmic abundances, stable compounds formed from these elements at high pressures are key (exo)-planetary building blocks. Understanding the structures of such compounds allows insight into the composition of planetary interiors, including exoplanets. To date, almost no work has been performed investigating CaO₂ as a stable oxide of calcium at high pressures. Some previous work has explored the effect of low pressures (<10 GPa) on the bond lengths and lattice parameters of $I4/mmm$-CaO₂ [5]. We therefore employ DFT calculations to explore the behaviour of CaO₂ at pressures in the GPa range. DFT calculations provide an excellent avenue for investigating materials properties under pressure, both at pressures accessible to diamond anvil cells [8] and at terapascal pressures [9, 10]. To explore the stability of CaO₂, we search for new crystal structures of this compound at a variety of pressures in the range 0-200 GPa.

## METHODS

Density functional theory calculations are performed using the **CASTEP** plane-wave pseudopotential code [11]. Ultrasoft pseudopotentials [12] generated with the CASTEP code are used for both calcium and oxygen, with core states $1s^{2}2s^{2}2p^{6}$ and $1s^{2}$, respectively. We use the Perdew-Burke-Ernzerhof (PBE) [13] form of the exchange-correlation functional with a plane-wave basis cutoff of 800 eV. A $k$-point sampling density of $2\pi \times 0.03$ Å⁻¹ is used for our CaO and CaO₂ phases. For our oxygen phases, we use a denser $k$-point sampling of $2\pi \times 0.02$ Å⁻¹. Bulk modulii are calculated by fitting static lattice pressure-volume data to the third-order Birch-Murnaghan equation of state.

The electronic density of states is calculated using the OPTADOS code [14–16]. Calculations of phonon frequencies are performed with the CASTEP code and a finite-displacement supercell method, using the quasiharmonic approximation [17, 18].

To search for new phases of CaO₂, we use the ab ini- tio random structure searching (AIRSS) technique [19]. AIRSS proceeds by generating random starting structures containing a given number of formula units. Of these, structures which have lattice parameters giving reasonable bond lengths and cell volumes at a particular pressure are then relaxed to an enthalpy minimum, and the lowest enthalpy structures are selected for refinement. AIRSS has proved to be a very powerful tool in predicting new structures, several of which have subsequently been found experimentally. AIRSS searches have for example uncovered high pressure phases of silane [20], and correctly predicted high pressure metallic phases in aluminium hydrides [21].

In this study, we perform structure searching at pressures of 0, 10, 20, 50, 100, 150 and 200 GPa. The bulk (about 60%) of our searches use cells with 2 or 4 formula units of CaO₂, and we have also performed searches with cells containing 1, 3, 5, 6 and 8 formula units. Not all combinations of pressures and formula unit numbers are searched. In total, we relax over 25,000 structures in our CaO₂ searches. We supplement our AIRSS searches by calculating the enthalpies of five known alkaline earth metal peroxide structures taken from the Inorganic Crystal Structure Database (ICSD) [22], and other authors [7, 23, 24]. The relevant alkaline earth metal is replaced with calcium where appropriate.

### CaO
CaO undergoes a transition from the rocksalt ($Fm\overline{3}m$) to the CsCl ($Pm\overline{3}m$) structure (the B1-B2 transition) around 60-65 GPa. Diamond-anvil-cell experiments indicate a transition pressure of 60±2 GPa at room temperature [25], while DFT calculations give a transition pressure of 65-66 GPa [26, 27]. We find a pressure of 65 GPa in the present study, and we therefore use the $Fm\overline{3}m$ rocksalt structure below 65 GPa and the CsCl structure at higher pressures. The bulk modulus of $Fm\overline{3}m$-CaO has been measured to be 104.9 GPa [28], while our static-lattice DFT calculations give a value of 108.5 GPa. To exclude the possibility that CaO might have a different, more stable structure (other than $Fm\overline{3}m$ or $Pm\overline{3}m$) over the pressure range 0-200 GPa, we also perform AIRSS on CaO at pressures of 50, 100 and 200 GPa. We do not find any new low-enthalpy structures for CaO at these pressures.

### Solid oxygen
Structure searching over the pressure range 0-200 GPa has already been performed for solid oxygen [29, 30], and we use the lowest enthalpy structures found therein. We also examine the enthalpies of the experimentally-determined $\alpha$ and $\delta$ oxygen phases at low pressures [31]. Choosing the lowest-enthalpy oxygen structure at each pressure, we find that $\delta$-O₂ is stable between 0 and 1.2 GPa, after which an insulating phase with space group $Cmcm$ [31] is stable up to 41 GPa. A phase of symmetry $C2/m$ [30] then becomes stable, remaining so up to 200 GPa. Our spin-polarised calculations show no discernable difference in enthalpy between a $\delta$-O₂ phase with antiferromagnetic spin ordering, and the experimentally-determined ferromagnetic spin-ordering for $\delta$-O₂ [32].

These results are not in accord with low-temperature experiments on solid oxygen, which predict $\alpha$-O₂ to be stable between 0 and about 5 GPa, $\delta$-O₂ to be stable between about 5 and 10 GPa, followed by the ‘$\epsilon$-O₂’ phase between 10 and 96 GPa, with a further isostructural phase transition around 100 GPa [33–35]. Our DFT calculations do not yield $\alpha$-O₂; optimising its structure at low pressures simply gives the $\delta$-O₂ structure. The aforementioned $C2/m$ oxygen phase is however very similar in structure to $\epsilon$-O₂ (which is also of $C2/m$ symmetry), and is within 50 meV/f.u. of that phase in enthalpy over the pressure range 0-200 GPa. Any higher enthalpy structure for oxygen over the pressure range being explored here would only increase the calculated stability of CaO₂, so we proceed with the lowest enthalpy DFT phases for oxygen.

## RESULTS

### Structure searching and static lattice results
Our structure searching is carried out by minimising the enthalpy at a given pressure within the static-lattice approximation. We discuss these results first before presenting our calculations of the Gibbs free energy.

Fig. 1 shows the enthalpy-pressure curves for nine phases of CaO₂. The first five of these, labelled with their space group symmetries $I4/mmm$, $Pa\overline{3}$, $Pna2_1$, $Cmmm$ and $I4/mcm$ in Fig. 1, are known alkaline earth metal peroxide structures as mentioned in the ‘Methods’ section. The other four, with space group symmetries $C2/c$ and $P2_1/c$, are new CaO₂ structures. These are the lowest-enthalpy phases that turned up during our AIRSS searches. The dotted line in Fig. 1 shows the enthalpy of $CaO+\frac{1}{2}O_2$, calculated using the lowest-enthalpy phases of CaO and O₂ at each pressure. Any CaO₂ phase below this dotted line is stable against decomposition in the manner of Eq. (1).

![](./images/867764735175557347_1.jpg)

FIG. 1: Static lattice enthalpies, in eV per unit of $CaO_2$, of calcium peroxide phases in the pressure range 0-5 GPa (left) and 0-200 GPa (right). Enthalpies are given relative to the $I4/mmm$ phase of $CaO_2$. $C2/c$-I, $C2/c$-II, $P2_1/c$-H and $P2_1/c$-L are new structures of $CaO_2$ found using AIRSS. The left-hand plot highlights the enthalpy differences between the $Pna2_1$ and two $C2/c$ phases at low pressures; $C2/c$-I is the lowest-enthalpy structure at 0 GPa from our searches. The arrow and box in the right-hand figure indicate the scope of the left-hand figure. Structures of $CaO_2$ below the dotted line are thermodynamically stable against decomposition into $CaO$ and $O_2$.

We find the following sequence of phase transitions for $CaO_2$ by considering the lowest enthalpy structure at each pressure:

$$
\begin{aligned}
C2/c\text{-I} &\xrightarrow{1.8\ \text{GPa}} Pna2_1 \xrightarrow{2.0\ \text{GPa}} C2/c\text{-II} \\
&\xrightarrow{27.6\ \text{GPa}} I4/mcm \xrightarrow{37.9\ \text{GPa}} P2_1/c\text{-L},
\end{aligned}
$$

with the transition pressures between each structure as indicated by the arrows. The $P2_1/c$-L phase is then predicted to be stable up to at least 200 GPa.

At 0 GPa, our structure searching reveals a number of $CaO_2$ phases which are very close (within 10 meV/f.u.) in enthalpy. Within the present approximations (DFT with PBE exchange-correlation), a phase of $C2/c$ symmetry ('$C2/c$-I') is lowest in enthalpy at 0 GPa. This phase is 8.4 meV/f.u. lower in enthalpy than the proposed $Pna2_1$-symmetry ground state structure of Zhao et al. [7], which we note also turned up in our AIRSS searches. Our searches also uncover a second $C2/c$-symmetry phase ('$C2/c$-II') which is slightly higher in enthalpy than $Pna2_1$ at 0 GPa. The enthalpies of these three phases at low pressures are shown in more detail in the left-hand panel of Fig. 1.

We find that the calculated XRD patterns for the $C2/c$-I, $C2/c$-II and $Pna2_1$ structures share many similar features with available experimental data [23], although this XRD data is best fitted by the $Pna2_1$ structure. The enthalpy differences between the $C2/c$-I, -II and $Pna2_1$ phases at 0 GPa are dependent on the choice of exchange-correlation functional. In Table I, we show the enthalpies of the $Pna2_1$ and $C2/c$-II phases relative to the $C2/c$-I phase using a variety of different functionals. We find differences in calculated equilibrium volumes as well: for $C2/c$-I at 0 GPa, the LDA gives a volume of $35.8\ \AA^3$/f.u., while the PBE functional gives $39.1\ \AA^3$/f.u. The LDA typically overbinds in DFT calculations, with PBE instead underbinding, so these two volumes likely bracket the true volume of the $C2/c$-I phase at 0 GPa. Given that $dP/dV$ is about $-2.3\ \text{GPa}/\AA^3$ for this phase at 0 GPa, this volume difference (due to functional choice) corresponds to a pressure uncertainty in the neighbourhood of $\pm 3$ GPa. In light of this uncertainty, $C2/c$-I,$C2/c$-II and $Pna2_1$ are all reasonable candidates for the structure of $CaO_2$ at 0 GPa.

<table>
<caption>TABLE I: Enthalpies of the $C2/c$-II and $Pna2_1$ phases of $CaO_2$ at 0 GPa, in meV per unit of $CaO_2$, relative to the $C2/c$-I phase using different exchange-correlation functionals.</caption>
<thead>
  <tr>
    <th>Functional</th>
    <th>LDA</th>
    <th>PBE</th>
    <th>PBESOL</th>
    <th>PW91</th>
    <th>WC</th>
  </tr>
</thead>
<tbody>
  <tr>
    <th>$C2/c$-I</th>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <th>$Pna2_1$</th>
    <td>0.1</td>
    <td>8.4</td>
    <td>2.9</td>
    <td>8.7</td>
    <td>3.5</td>
  </tr>
  <tr>
    <th>$C2/c$-II</th>
    <td>-16.3</td>
    <td>12.2</td>
    <td>-4.1</td>
    <td>12.0</td>
    <td>-2.7</td>
  </tr>
</tbody>
</table>

The $C2/c$-I, -II and $Pna2_1$ phases exhibit very similar structures. Looking down the $b$-axis of each phase, calcium atoms form a nearly-hexagonal motif, and we note that the monoclinic angle $\beta$ is close to $120^\circ$ for $C2/c$-I and $C2/c$-II. For the $C2/c$-I and -II phases, the peroxide ion axes are almost coplanar, as can be seen in Fig. 2. In $C2/c$-II, the axes of peroxide ions in the same plane are parallel, while in $C2/c$-I, they alternate in orientation in the same plane. We use red and blue colouring in Fig. 2

![](./images/867764735175557347_2.jpg)

FIG. 2: 2x2x2 slabs of the $C2/c$-I (left) and $C2/c$-II (right) structures, viewed almost down the $b$-axis. Both structures are very similar, with Ca atoms forming an almost-hexagonal motif when viewed from this angle. Green atoms correspond to Ca atoms, while red and blue correspond to O atoms. All O atoms in peroxide ions with parallel O-O axes are given the same colour.

to show peroxide ions with parallel axes.

AIRSS searches also reveal a second phase for $CaO_2$ with $P2_1/c$ symmetry (`$P2_1/c-H$'). As can be seen in the right-hand panel of Fig. 1, our static-lattice calculations show that this is not a stable phase for $CaO_2$ over the pressure range 0-200 GPa. However around 38 GPa, the enthalpy of this phase lies within 10 meV/f.u. of the $I4/mcm$ and $P2_1/c-L$ phases, opening up the possibility this phase could become stable once we take temperature into account. We consider this further in a later section ('Lattice dynamics'). The $I4/mcm$ phase reported here is also predicted for $MgO_2$ above 53 GPa [24].

We provide lattice parameters and bulk modulii for the $C2/c$-I, $C2/c$-II, $I4/mcm$, $P2_1/c-H$ and $P2_1/c-L$ phases at 0, 20, 30 and 50 GPa in Table II.

### Bonding and electronic structure

The bandstructure of the $P2_1/c-L$ phase at 50 GPa is shown in Fig. 3. The insulating nature of this phase is evident, with a calculated thermal bandgap of 2.4 eV and optical bandgap of 2.5 eV. These will be underestimates of the true bandgap owing to the use of the PBE functional. The lowest set of 4 bands is comprised almost entirely of Ca $3s$ orbitals. Above this, we find a central peak flanked by two smaller sidepeaks in the total density of states. The central peak is built from 12 bands and is largely Ca $3p$ orbitals, while the two sidepeaks contain 4 bands apiece and are dominated by O $2s$ orbitals. Thus, we have a splitting of the O $2s$ orbital energy levels, possibly arising from the covalent bonding present in the peroxide $[O-O]^-$ ion. Above this, and just below the HOMO (highest occupied molecular orbital), are 20 bands which arise largely from O $2p$ orbitals. The first orbitals above the Fermi level consist of (unoccupied) O $2p$ orbitals, followed by a dense band of Ca $3d$ orbitals. An almost identical pattern of bonding and electronic density of states are found in our other low-enthalpy phases.

![](./images/867764735175557347_3.jpg)

FIG. 3: Bandstructure and electronic density of states of the $P2_1/c-L$ phase at 50 GPa. The density of states is shown projected onto the $s$, $p$ and $d$ angular momentum channels. We calculate a thermal bandgap of 2.4 eV, and an optical bandgap of 2.5 eV. The Fermi level is shown as a black dashed line.

![](./images/867764735175557347_4.jpg)

FIG. 4: Phonon dispersion relations and density of states for $P2_1/c-L$ $CaO_2$ at 50 GPa.

Fig. 4 shows the corresponding phonon band structure and density of states for $P2_1/c-L$ at 50 GPa. The lack of imaginary phonon frequencies indicates the stability of this particular phase. The distinctly separate high frequency bands around 930 - 1000 cm$^{-1}$ in Fig. 4 correspond to phonon modes that stretch the O-O covalent bond in the peroxide ions. Two distinct peroxide bond lengths are found in the ions of this structure:

<table><caption>TABLE II: Structures of the $C2/c$-I, $C2/c$-II, $I4/mcm$, $P2_1/c$-H and $P2_1/c$-L phases of ${\rm CaO_2}$.</caption>
<thead>
  <tr>
    <th>Pressure</th>
    <th></th>
    <th colspan="3">Lattice parameters</th>
    <th></th>
    <th colspan="3">Atomic coordinates</th>
    <th>Wyckoff</th>
    <th></th>
  </tr>
  <tr>
    <th>(GPa)</th>
    <th>Space group</th>
    <th colspan="3">(Å, deg.)</th>
    <th>Atom</th>
    <th>$x$</th>
    <th>$y$</th>
    <th>$z$</th>
    <th>site</th>
    <th>$B_0$ (GPa)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0</td>
    <td>$C2/c$ ($\#15$)a</td>
    <td>(I) $a$=7.041 $b$=3.685</td>
    <td>$c$=6.820</td>
    <td>$\alpha$=90.0 $\beta$=117.8 $\gamma$=90.0</td>
    <td>Ca</td>
    <td>0.0000</td>
    <td>0.6399</td>
    <td>0.2500</td>
    <td>4e</td>
    <td>87</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>O</td>
    <td>0.2548</td>
    <td>0.1404</td>
    <td>0.4119</td>
    <td>8f</td>
    <td></td>
  </tr>
  <tr>
    <td>20</td>
    <td>$C2/c$ ($\#15$)a</td>
    <td>(II) $a$=6.829 $b$=3.403</td>
    <td>$c$=6.407</td>
    <td>$\alpha$=90.0 $\beta$=118.8 $\gamma$=90.0</td>
    <td>Ca</td>
    <td>0.0000</td>
    <td>0.3413</td>
    <td>0.2500</td>
    <td>4e</td>
    <td>89</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>O</td>
    <td>0.1661</td>
    <td>0.1553</td>
    <td>0.0252</td>
    <td>8f</td>
    <td></td>
  </tr>
  <tr>
    <td>30</td>
    <td>$I4/mcm$ ($\#140$)</td>
    <td>$a$=4.521 $b$=4.521</td>
    <td>$c$=5.745</td>
    <td>$\alpha$=90.0 $\beta$=90.0 $\gamma$=90.0</td>
    <td>Ca</td>
    <td>0.0000</td>
    <td>0.0000</td>
    <td>0.2500</td>
    <td>4a</td>
    <td>114</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>O</td>
    <td>0.1143</td>
    <td>0.6143</td>
    <td>0.0000</td>
    <td>8h</td>
    <td></td>
  </tr>
  <tr>
    <td>30</td>
    <td>$P2_1/c$-H ($\#14$)b</td>
    <td>$a$=6.590 $b$=4.842</td>
    <td>$c$=3.795</td>
    <td>$\alpha$=90.0 $\beta$=105.2 $\gamma$=90.0</td>
    <td>Ca</td>
    <td>0.0611</td>
    <td>0.7628</td>
    <td>0.2781</td>
    <td>4e</td>
    <td>93</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>O</td>
    <td>0.1301</td>
    <td>0.2714</td>
    <td>0.3087</td>
    <td>4e</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>O</td>
    <td>0.2446</td>
    <td>0.4378</td>
    <td>0.1012</td>
    <td>4e</td>
    <td></td>
  </tr>
  <tr>
    <td>50</td>
    <td>$P2_1/c$-L ($\#14$)b</td>
    <td>$a$=4.223 $b$=4.279</td>
    <td>$c$=5.949</td>
    <td>$\alpha$=90.0 $\beta$=98.7 $\gamma$=90.0</td>
    <td>Ca</td>
    <td>0.0613</td>
    <td>0.5133</td>
    <td>0.2539</td>
    <td>4e</td>
    <td>110</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>O</td>
    <td>0.0820</td>
    <td>0.0235</td>
    <td>0.4019</td>
    <td>4e</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>O</td>
    <td>0.1224</td>
    <td>0.1182</td>
    <td>0.0089</td>
    <td>4e</td>
    <td></td>
  </tr>
</tbody>
</table>

$^{a}$ $C12/c1$ - International Tables, Volume A: unique axis $b$, cell choice 1.

$^{b}$ $P12_1/a1$ - International Tables, Volume A: unique axis $b$, cell choice 3.

$1.44$ Å and $1.46$ Å, which splits these higher frequency bands. These peroxide O-O bond lengths are somewhat longer those found in molecular oxygen, which has an O-O bond length of $1.207$ Å [23] at ambient conditions, and the bond length in $C2/m$ oxygen at 50 GPa, which we calculate as $1.20$ Å. These longer O-O bond lengths are however typical of crystalline ionic peroxides [5].

## Stability of ${\rm CaO_2}$

As can be seen in Fig. 1, our low-enthalpy phases for ${\rm CaO_2}$ show remarkable stability against decomposition as pressure increases. We predict ${\rm CaO_2}$ to be most stable at the B1-B2 CaO phase transition pressure of 65 GPa. There, the decomposition enthalpy (Eq. (1)) of ${\rm CaO_2}$ is $+0.64$ eV/unit of ${\rm CaO_2}$ ($+62$ kJ/mol).

One implication of the stability of ${\rm CaO_2}$ is that it may be preferentially formed over CaO in an oxygen-rich environment under pressure, through the reverse of Eq. (1). For example, the pressure in the Earth’s lower mantle, at a depth of around 1550 km, is about 65 GPa [25], close to our predicted peak stability pressure for ${\rm CaO_2}$. The formation of ${\rm MgO_2}$ in this way has also been discussed [24], although much higher pressures ($>116$ GPa) are needed before ${\rm MgO_2}$ is stable against decomposition, whereas ${\rm CaO_2}$ is stable from around 0 GPa. The mantle temperature in the Earth at 65 GPa is in the neighbourhood of 2500 K, and our phonon calculations show that under these conditions, $\Delta G = +0.54$ eV/f.u. for the reaction of Eq. (1). Hence, ${\rm CaO_2}$ is a thermodynamically stable oxide at temperatures and pressures encountered in planetary interiors.

Reactions of the form $X$+${\rm O_2}$ $\rightarrow Y$ for species $X$ and $Y$, such as the reverse of Eq. (1), are known as redox buffers. Such reactions are key in determining planetary mantle compositions. In the Earth’s mantle, there are a number of such buffers, usually involving the further oxidation of iron and nickel compounds, such as ${\rm Fe_3O_4} + \frac{1}{4}{\rm O_2} \rightarrow \frac{3}{2}{\rm Fe_2O_3}$ and ${\rm Ni} + \frac{1}{2}{\rm O_2} \rightarrow {\rm NiO}$. The natural formation of ${\rm CaO_2}$ by further oxidation of CaO in Earth’s mantle, while energetically favourable at high pressures and temperatures, would also need to compete against the further oxidation of other such compounds. The average CaO content in the Earth’s mantle is about 3% [28], though exoplanet mantles offer a rich variety of alternative compositions.

We highlight the fact that the pressures at which these different ${\rm CaO_2}$ phases are predicted to become stable are amenable to experimental study in diamond anvil cells. Very few pressure-induced phase transitions for A[$B_2$] compounds are experimentally known [36], although at least one example already occurs among the alkaline earth metal peroxides, in ${\rm BaO_2}$ [36]. Equivalently, it would be interesting to test the reactivity of CaO and ${\rm O_2}$ under conditions of excess oxygen, as our results suggest that CaO and ${\rm O_2}$ are reactive at high pressures. The formation of ${\rm CaO_2}$ may require laser heating in a diamond anvil cell to overcome the likely high potential barriers between phases. High pressure phases of ${\rm CaO_2}$ could be recoverable at lower pressures, although possibly not at ambient or zero pressure.

## Lattice dynamics

In addition to our static-lattice calculations, we calculate the phonon free energies of our lowest-enthalpy ${\rm CaO_2}$ phases, namely those with $Pna2_1$, $C2/c$-I/II, $I4/mcm$, $P2_1/c$-H and $P2_1/c$-L symmetries. We encounter no imaginary phonon frequencies over the pressure ranges relevant to these phases, indicating that they are dynamically stable. The relevant thermodynamic potential is now the Gibbs free energy, which includes the phonon

![](./images/867764735175557347_5.jpg)

FIG. 5: T-P phase diagram of CaO₂ as calculated using the quasiharmonic approximation and our lowest-enthalpy structures.

pressure. Selecting the lowest Gibbs free energy structure from these six structures gives rise to the T-P phase diagram given in Fig. 5. We note that the upper-left (low-P, high-T) part of the phase diagram is representative only, because at ambient pressures CaO₂ decomposes at temperatures around 620 K [2, 3].

We find that the small enthalpy difference between the $I4/mcm$ and $P2_1/c-H$ phases seen in our static-lattice calculations (Fig. 1) closes with increasing temperature, and we see the emergence of $P2_1/c-H$ as a stable phase for CaO₂ at 37.7 GPa and for $T > 281$ K. The free energy difference between the $I4/mcm$ and $P2_1/c-H$ phases does remain quite small however, around 20 meV per CaO₂ unit at the most over the temperature range 0-1000 K.

At room temperature (300 K), we therefore predict a different sequence of phase transitions than those for our static-lattice calculations. We find that, with PBE exchange-correlation:

$$
\begin{aligned}
C2/c\text{-I} &\xrightarrow{2.2\ \text{GPa}} Pna2_1 \xrightarrow{2.6\ \text{GPa}} C2/c\text{-II} \xrightarrow{28.3\ \text{GPa}} \\
I4/mcm &\xrightarrow{37.4\ \text{GPa}} P2_1/c\text{-H} \xrightarrow{37.9\ \text{GPa}} P2_1/c\text{-L},
\end{aligned}
$$

with the arrows labelled by the predicted transition pressures.

The phase diagram of Fig. 5 does not extend all the way to 200 GPa. However, we expect $P2_1/c-L$ to continue to be the most stable phase at high pressures. This is because our structure searching results (which use static-lattice enthalpies) show that the next most stable structure for CaO₂ over the pressure range 100-200 GPa is at least 45 meV per unit of CaO₂ higher in enthalpy. This was not the case at low pressures, where our searches reveal quite a few structures (such as $P2_1/c-H$) that are close to becoming stable and may therefore do so at high temperatures.

## CONCLUSIONS

Structural changes in CaO₂ under pressure have been explored over the pressure range 0-200 GPa at temperatures up to 1000 K. CaO₂ remains insulating up to pressures of at least 200 GPa. Structure searching and DFT calculations reveal six stable phases for CaO₂ over these pressure and temperature ranges, of which five are reported for the first time in this study. Calculations of the phonon frequencies of these new structures confirms their dynamical stability. The lowest-enthalpy phase of CaO₂ at 0 GPa is dependent on the choice of DFT exchange-correlation functional. At pressures above 40 GPa, a phase of $P2_1/c$ symmetry ('$P2_1/c-L$') emerges for CaO₂ which is predicted to be stable up to 200 GPa, and at mantle pressures and temperatures. CaO₂ is a very stable oxide of calcium at high pressures, and may be a constituent of exoplanet mantles. The pressures at which these CaO₂ phases become stable are readily attainable in diamond anvil cells.

## ACKNOWLEDGEMENTS

Calculations were performed using the Darwin Supercomputer of the University of Cambridge High Performance Computing Service (http://www.hpc.cam.ac.uk/), as well as the ARCHER UK National Supercomputing Service (http://www.archer.ac.uk/). Financial support was provided by the Engineering and Physical Sciences Research Council (UK). JRN acknowledges the support of the Cambridge Commonwealth Trust.

* Electronic address: jn336@cam.ac.uk

[1] Y. Qian, X. Zhou, Y. Zhang, W. Zhang, and J. Chen, Chemosphere 91, 717-723 (2013).
[2] I. A. Massalimov, A. U. Shayakhmetov, and A. G. Mustafin, Russian J. Appl. Chem. 83, 1794-1798 (2010).
[3] This decomposition temperature may be lower for samples of different purities; for example the CRC Handbook [37] reports a decomposition temperature of $\approx$470K for CaO₂.
[4] C. Brosset and N.-G. Vannerberg, Nature 177, 238 (1956).
[5] M. Königstein, A. A. Sokol, and C. R. A. Catlow, Phys. Rev. B 60, 4594-4604 (1999).
[6] P. D. VerNooy, Acta Cryst. C 49, 433-434 (1993).

[7] X. Zhao, M. C. Nguyen, C.-Z. Wang, and K.-M. Ho, RSC Advances 3, 22135-22139 (2013).

[8] S. Ninet, F. Datchi, P. Dumas, M. Mezouar, G. Gar- barino, A. Mafety, C. J. Pickard, R. J. Needs, and A. M. Saitta, Phys. Rev. B 89, 174103 (2014).

[9] M. Martinez-Canales, C. J. Pickard, and R. J. Needs, Phys. Rev. Lett. 108, 045704 (2012).

[10] C. J. Pickard, M. Martinez-Canales, R. J. Needs, Phys. Rev. Lett. 110, 245701 (2013).

[11] S. J. Clark, M. D. Segall, C. J. Pickard, P. J. Has- nip, M. I. J. Probert, K. Refson, and M. C. Payne, Zeit. für Krist. 220, 567-570 (2005).

[12] D. Vanderbilt, Phys. Rev. B 41, 7892-7895 (1990).

[13] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865-3868 (1996).

[14] R. J. Nicholls, A. J. Morris, C. J. Pickard, and J. R. Yates, J. Phys.: Conf. Series 371, 012062 (2012).

[15] A. J. Morris, R. J. Nicholls, C. J. Pickard, and J. R. Yates, OptaDOS User Guide: Version 1.0.370 (2014). Available online at http://www.cmmp.ucl.ac.uk/~ajm/optados/.

[16] J. R. Yates, X. Wang, D. Vanderbilt, and I. Souza, Phys. Rev. B 75, 195121 (2007).

[17] B. B. Karki and R. M. Wentzcovitch, Phys. Rev. B 68, 224304 (2003).

[18] P. Carrier and R. M. Wentzcovitch, Phys. Rev. B 76, 064116 (2007).

[19] C. J. Pickard and R. J. Needs, J. Phys.: Condensed Matter 23, 053201 (2011).

[20] C. J. Pickard and R. J. Needs, Phys. Rev. Lett. 97, 045504 (2006).

[21] C. J. Pickard and R. J. Needs, Phys. Rev. B 76, 144114 (2007).

[22] F. H. Allen, G. Bergerhoff, and R Sievers, Crystal- lographic databases (Chester, England: International Union of Crystallography, 1987).

[23] M. Königstein and C. R. A. Catlow, J. Solid State Chem. 140, 103-115 (1998).

[24] Q. Zhu, A. R. Oganov, and Andriy O. Lyakhov, Phys. Chem. Chem. Phys. 15, 7696-7700 (2013).

[25] R. Jeanloz, T. J. Ahrens, H. K. Mao, and P. M. Bell, Science 206, 829-830 (1979).

[26] M. Catti, Phys. Rev. B. 68, 100101 (2003).

[27] J. Zhang and J. Kuo, J. Phys.: Condensed Matter 21, 015402 (2009).

[28] N. Soga, J. Geophys. Research 73, 5385-5390 (1968).

[29] J. Sun, M. Martinez-Canales, D. D. Klug, C. J. Pickard, and R. J. Needs, Phys. Rev. Lett. 108, 045503 (2012).

[30] Y. Ma, A. R. Oganov, and C. W. Glass, Phys. Rev. B 76, 064101 (2007).

[31] J. B. Neaton and N. W. Ashcroft, Phys. Rev. Lett. 88, 205503 (2002).

[32] I. N. Goncharenko, O. L. Makarova, and L. Ulivi, Phys. Rev. Lett. 93, 055502 (2004).

[33] L. F. Lundegaard, G. Weck, M. I. McMahon, S. Desgre- niers, and P. Loubeyre, Nature 443, 201-204 (2006).

[34] H. Fujihisa, Y. Akahama, H. Kawamura, Y. Ohishi, O. Shimomura, H. Yamawaki, M. Sakashita, and Y. Gotoh, S. Takeya, and K. Honda, Phys. Rev. Lett. 97, 085503 (2006).

[35] Y. Akahama, H. Kawamura, D. Häusermann, M. Hanfland, and O. Shimomura, Phys. Rev. Lett. 74, 4690-4693 (1995).

[36] I. Efthimiopoulos, K. Kunc, S. Karmakar, K. Syassen, M. Hanfland, and G. Vajenine, Phys. Rev. B 82, 134125 (2010).

[37] W. M. Haynes (ed.), CRC Handbook of Chemistry and Physics, 94th ed. (Taylor and Francis, 2013).