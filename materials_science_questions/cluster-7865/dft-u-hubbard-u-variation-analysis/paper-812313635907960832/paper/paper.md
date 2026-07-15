# First-principles prediction of redox potentials in transition-metal compounds with LDA+$U$

F. Zhou
Department of Physics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA

M. Cococcioni, C. A. Marianetti, D. Morgan, and G. Ceder
Department of Material Science and Engineering, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA

Received 11 April 2004; published 20 December 2004

First-principles calculations within the local density approximation (LDA) or generalized gradient approximation (GGA), though very successful, are known to underestimate redox potentials, such as those at which lithium intercalates in transition metal compounds. We argue that this inaccuracy is related to the lack of cancellation of electron self-interaction errors in LDA/GGA and can be improved by using the DFT+$U$ method with a self-consistent evaluation of the $U$ parameter. We show that, using this approach, the experimental lithium intercalation voltages of a number of transition metal compounds, including the olivine $\mathrm{Li}_{x}\mathrm{MPO}_{4}$ (M=Mn, Fe Co, Ni), layered $\mathrm{Li}_{x}\mathrm{MO}_{2}$ (x=Co, Ni) and spinel-like $\mathrm{Li}_{x}\mathrm{M}_{2}\mathrm{O}_{4}$ (M=Mn, Co), can be reproduced accurately.

DOI: 10.1103/PhysRevB.70.235121
PACS number(s): 71.27.+a, 71.15.Nc, 82.47.Aa

## I. INTRODUCTION

Redox processes are relevant to many technological applications, including corrosion, fuel cells and rechargeable Li batteries, and the ability to study these processes from first principles is therefore crucial. The key to a redox reaction is the transfer of electrons from one species to another. When the redox electron is transferred between very distinct environments (e.g., metallic to ionic) the standard local density approximation (LDA) and generalized gradient approximation (GGA) lead to considerable errors in the calculated redox energies. We show in this paper that treating self-interaction with the DFT+$U$ (Refs. 1–3) method gives considerably better agreement with experiment and thereby provides a tool to accurately predict redox potentials.

In particular, we focus on the study of Li insertion in transition metal compounds using GGA and GGA+$U$. Transition metal (TM) compounds have attracted intense research as cathode materials for rechargeable Li batteries due to their ability to simultaneously absorb $\mathrm{Li}^{+}$ ions and electrons. In the discharge cycle of a rechargeable battery Li is oxidized on the anode side and inserted as $\mathrm{Li}^{+}+e^{-}$ in the TM compound that comprises the cathode. The energy of this reaction determines the oxidization/reduction potential at which the battery operates. It is the high redox potential of Li cells that makes them so desirable in applications where high energy density is required.

First principles calculations have been used extensively to predict important properties of Li-insertion materials such as the average potential $^{4–14}$ and potential profile $^{15,16}$ for Li insertion, phase stability $^{17–19}$ and Li diffusion. $^{20}$ While this has led to considerable success in predicting the trends of Li insertion voltages $^{4}$ and even new phases, $^{15}$ it has been noted that LDA or GGA can give relatively large errors for the average Li insertion potential. $^{4,21}$ For example, Table I compares the experimental voltage for different structures with the one calculated in the GGA and with computational details discussed in Sec. III. The Li insertion potential is consistently underpredicted by as much as 0.5 to 1.0 V. Similar results have been obtained with LDA. $^{4}$

Recently, we have shown that electron correlation plays an important role in predicting the phase diagram of the $\mathrm{Li}_{x}\mathrm{FePO}_{4}$ system, $^{25}$ for which LDA and GGA qualitatively fail. In this work we demonstrate that the DFT+$U$ method also corrects the voltage error from LDA and GGA. In our approach, $U$ is calculated self-consistently, $^{26}$ thereby making this a "first-principles" approach to predict redox potentials with no adjustable parameters.

We first present some background information on the specific Li insertions materials investigated and how the electrochemical reactions take place in a rechargeable lithium battery. We also discuss the details of the DFT+$U$ method and the self-consistent calculation of $U$. In Sec. III we show the results of our approach, highlighting the improvement over GGA and the good agreement with experiment.

## II. MATERIALS AND METHODOLOGY

### A. Materials and crystal structures

As a representative set of Li-insertion compounds, we have selected several materials representing different environments for Li and TM ions, which are well characterized experimentally.

The family of $\mathrm{LiMPO}_{4}$ olivine structures (M=Mn, Fe, Co, and Ni) are promising candidates for rechargeable Li-battery electrodes in large applications such as electric and hybrid vehicles. $^{27}$ Olivine-type $\mathrm{LiMPO}_{4}$ and the delithiated structure $\mathrm{MPO}_{4}$, have an orthorhombic unit cell with four formula units (FU) and space group $Pnma$ (see Fig. 1). The olivine

<table>
<caption>TABLE I. Calculated and experimental redox couple voltage in units of volts.</caption>
<thead>
  <tr>
    <th>
    </th>
    <th>
      $\mathrm{LiNiO}_{2}$/$\mathrm{NiO}_{2}$
    </th>
    <th>
      $\mathrm{LiMn}_{2}\mathrm{O}_{4}$/$\mathrm{Mn}_{2}\mathrm{O}_{4}$
    </th>
    <th>
      $\mathrm{LiFePO}_{4}$/$\mathrm{FePO}_{4}$
    </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>
      GGA
    </td>
    <td>
      3.19
    </td>
    <td>
      3.18
    </td>
    <td>
      2.97
    </td>
  </tr>
  <tr>
    <td>
      Expt.
    </td>
    <td>
      3.85 (Ref. 22)
    </td>
    <td>
      4.15 (Ref. 23)
    </td>
    <td>
      3.5 (Ref. 24)
    </td>
  </tr>
</tbody>
</table>

![](./images/812313635907960832_1.jpg)

FIG. 1. (Color online) The olivine structure with cation polyhedra.

structure can be thought of as a distorted hexagonal close packing of oxygen anions, with three types of cations occupying the interstitial sites: (1) Transition metals M in corner-sharing $MO_6$ octahedra which are nearly coplanar to form a distorted two-dimensional (2D) square lattice perpendicular to the $\mathbf{a}$ axis, (2) lithium ions in edge-sharing $LiO_6$ octahedra aligned in parallel chains along the $\mathbf{b}$ axis, and (3) P ions in tetrahedral $PO_4$ groups connecting neighboring planes or arrays. It is believed that the $PO_4$ groups hybridize less with the TM than an oxygen anion does in simple close-packed oxides, and hence leads to more localized $3d$ states on the TM than in an oxide.

The layered $LiMO_2$ and spinel-like $Li_xM_2O_4$ are more traditional cathode materials that have been thoroughly studied experimentally$^{28}$ and theoretically.$^{4,5,19,20}$ They are both ordered rock salts (see Figs. 2 and 3). The layered structure can be envisioned as two interpenetrating fcc lattices, one consisting of oxygen, and the other consisting of alternating (111) planes of Li and TM. In the $R\overline{3}m$ space group the Li and the metal ions remain fixed in the ideal rock salt positions, but the whole (111) oxygen planes can relax in the [111] direction. The spinel-like structure $Li_xM_2O_4$ is so named because at $x=1$ it has the same structure as the spinel mineral $MgAl_2O_4$. We shall refer to it as spinel even when $x=2$. It can be envisioned as a fcc oxygen sublattice, with TM in one-half of the octahedral oxygen interstices, and lithium either in part of the tetrahedral sites at $x=1$ or in the octahedral sites not occupied by the TM ions at $x=2.^{28}$

![](./images/812313635907960832_2.jpg)

FIG. 2. (Color online) The layered structure with $MO_6$ octahedra and lithium atoms.

![](./images/812313635907960832_3.jpg)

FIG. 3. (Color online) The spinel-like structure when fully lithiated ($x=2$, Li atoms taking octahedral positions) with $MO_6$ octahedra and lithium atoms.

### B. Relation between insertion voltage and total energies

When Li is inserted into a TM oxide, its charge is compensated by an electron absorbed from the external circuit. The insertion reaction is symbolized by the following equation:
$$
\Delta x\ \text{Li} + \text{Li}_x\text{MO}_y \Leftrightarrow \text{Li}_{x+\Delta x}\text{MO}_y, \tag{1}
$$
where $\text{MO}_y$ is the TM compound host material. Using thermodynamical arguments, it is possible to relate the voltage $V$ of the cell to the lithium chemical potential ($\mu_{\text{Li}}$) on both sides of Eq. (1) in the cathode$^{29}$
$$
V(x)=-\frac{\mu_{\text{Li}(x)}^{\text{cathode}} - \mu_{\text{Li}}^{\text{anode}}}{F}. \tag{2}
$$
$F$ is the Faraday constant, and $\mu_{\text{Li}}^{\text{anode}}$ is the chemical potential in the anode, or more generally, the chemical potential of the Li source.

The average voltage $\langle V \rangle$ for Li insertion between two composition limits, $\text{Li}_{x_1}\text{MO}_y$ and $\text{Li}_{x_2}\text{MO}_y$, can be found by integrating Eq. (2) (usually between $x=0$ and 1), and is determined by the free energy of the compounds at the composition limits.$^{4}$ Neglecting the entropic and $P\Delta V$ contributions,$^{4}$ $\langle V \rangle$ can simply be determined by computing the total energy of $\text{Li}_{x_2}\text{MO}_y$, $\text{Li}_{x_1}\text{MO}_y$, and Li,
$$
\langle V \rangle=\frac{-\left[E(\text{Li}_{x_2}\text{MO}_y)-E(\text{Li}_{x_1}\text{MO}_y)-(x_2-x_1)E(\text{Li metal})\right]}{(x_2-x_1)F}. \tag{3}
$$

Typically $x_1=0$ and $x_2=1$ are taken as composition limits, as in these cases no Li-vacancy disorder occurs.

Experimentally, the voltage vs lithium composition curve $V(x)$ can be conveniently measured for both the charging and the discharging processes. The corresponding curves differ in general because of the overcharge potential present in the circuit. We obtain the experimental average open circuit volt-

age values by numerically averaging the charge and dis-
charge curves published in Refs. 22–24 and 30–32 over the
appropriate composition range.

### C. The DFT+$U$ method
The DFT+$U$ method, developed in the 1990s, $^{1-3}$ is now a
well-established model to deal with electron correlation in
TM and rare earth compounds. The method combines the
high efficiency of LDA/GGA, and an explicit treatment of
correlation with a Hubbard-type model for a subset of states
in the system. To investigate whether the underestimation of
the lithium intercalation voltage in LDA/GGA could be re-
lated to Coulombic on-site effects we carried out rotationally
invariant DFT+$U^3$ calculations. The essence of the method
can be summarized by the expression for the total energy

$$
\begin{aligned}
E_{\mathrm{LDA}+U}[\rho, \hat{n}]= & E_{\mathrm{LDA}}[\rho]+E_{\mathrm{Hub}}[\hat{n}]-E_{\mathrm{dc}}[\hat{n}] \equiv E_{\mathrm{LDA}}[\rho] \\
& +E_{U}[\hat{n}],
\end{aligned}
\tag{4}
$$

where $\rho$ denotes the charge density and $\hat{n}$ is the TM on-site
$3d$ occupation matrix. For these states the Hubbard interac-
tion term $E_{\text{Hub}}$ replaces the LDA energy contribution $E_{\text{dc}}$.
The $U$ correction term $E_{U} \equiv E_{\text{Hub}}-E_{\text{dc}}$ is defined by Eq. (4).
Although $E_{\text{dc}}$ is not uniquely defined, we have chosen the
spherically averaged version $^{33}$ due to the considerations dis-
cussed in Ref. 25,

$$
E_{\mathrm{dc}}(\hat{n})=\frac{U-J}{2} \operatorname{Tr} \hat{n}(\operatorname{Tr} \hat{n}-1)=\frac{U_{\mathrm{eff}}}{2} \operatorname{Tr} \hat{n}(\operatorname{Tr} \hat{n}-1), \quad (5)
$$

$$
E_{U}(\hat{n})=\frac{U-J}{2} \operatorname{Tr}(\hat{n}(1-\hat{n}))=\frac{U_{\mathrm{eff}}}{2} \operatorname{Tr}(\hat{n}(1-\hat{n})), \quad (6)
$$

where we have defined the effective interaction parameter
$U_{\text{eff}}$=$U-J$, or simply $U$ afterwards. The calculated energies
are insensitive to the $J$ parameter at fixed $U_{\text{eff}}$ (Ref. 25) and
we include it in $U_{\text{eff}}$.

### D. Self-consistent calculation of effective $U$
We determine the $U$ parameter using the method pre-
sented in Ref. 26 which we briefly outline below. This
method is based on calculating the response in the occupa-
tion of TM states to a small perturbation of their local poten-
tial.

We start from an LDA/GGA ($U$=0) calculation as the
reference point. Then a small perturbation

$$
d V=\alpha P_{d}^{i}, \quad P_{d}^{i}=\sum_{m=-2}^{2}\left|m^{i}\right\rangle\left\langle m^{i}\right|
$$

in the local $d$-orbital potential is exerted on metal site $i$,
where $P_{d}^{i}$ represents the projector on the $d$ states manifold of
ion $i$, and $\alpha$ is the amplitude of the potential shift applied to
the $d$ levels. This induces a change in the occupation number
of ion $i$ as well as other ions. Thus we can calculate directly
the response matrices,

$$
\chi_{j i}=\frac{d n_{d}^{j}}{d \alpha_{i}}, \quad \chi_{0 j i}=\frac{d n_{0 d}^{j}}{d \alpha_{i}}, \tag{7}
$$

which measure the variation of the $d$-manifold charge den-
sity $n_{d}^{j}$, on ion $j$, produced by a potential shift at ion $i$. The
subscript "0" denotes the bare response, calculated without
self-consistency (the Kohn-Sham potential apart from $dV$ is
frozen at the value obtained in LDA/GGA before the pertur-
bation), and corresponds to the response from an indepen-
dent electron system, while $\chi_{ji}$ is the screened response
(charge density and potential relaxed to reach self-
consistency). The effective interaction parameter $U$ is then
obtained as

$$
U=\left(\chi_{0}^{-1}-\chi^{-1}\right)_{i i}. \tag{8}
$$

This is a well-known result in linear response theory, in
which the effective electron-electron interaction kernel is
given as a difference among the interacting density response
and the noninteracting one. $^{34}$ Since DFT is used, a finite
contribution from the exchange-correlation potential is also
included in the effective $U$. As we use the integrated quantity
$n_d^i$ to probe the responses, the calculated effective interaction
is averaged over the ion in the same spirit as DFT+$U$. The
matrix in Eq. (8), whose diagonal term defines the on-site
Hubbard $U$, also contains nondiagonal terms corresponding
to intersite effective interactions in LDA/GGA. These are not
used in the DFT+$U$ model. This method to compute $U$ con-
tains full account of the screening to the external perturba-
tion operated by the electron-electron interactions. In fact the
perburtation is applied in larger and larger supercells until
convergence of calculated $U$ is reached. Note that the calcu-
lation of $U$ is based on the use of the same occupancy ma-
trices entering the DFT+$U$ functional, guaranteeing full con-
sistency with the energy calculation performed in DFT+$U.^{26}$

### III. DETAILS OF THE CALCULATION AND RESULTS
Total energy calculations are performed for Ni, Mn, Co,
and Fe in the olivines, layered and spinel structures. For each
system the total energy of the lithiated and delithiated state is
calculated with GGA and GGA+$U$, with the projector-
augmented wave (PAW) method $^{35,36}$ as implemented in the
Vienna $Ab$-initio Simulation Package. $^{37}$ The use of GGA
over LDA has previously been shown to be essential for
correctly reproducing magnetic interactions and possible
Jahn-Teller distortions. $^{38}$ An energy cutoff of 500 eV and
appropriate $k$-point mesh were chosen so that the total
ground state energy is converged to within 3 meV per FU.
All atoms and cell parameters of each structure are fully
relaxed. Jahn-Teller distortions are allowed where the transi-
tion metal ions are Jahn-Teller active ($\text{Mn}^{3+}$ and $\text{Ni}^{3+}$ in our
case) by explicitly breaking the symmetry of the unit cell.
Our relaxed cells of layered $\text{LiNiO}_2$ and spinel $\text{Li}_2\text{Mn}_2\text{O}_4$
agree well with the calculations in Ref. 39 on Jahn-Teller
distorted systems using GGA. All calculations are performed
with spin polarization. As discussed later, the total energy of
a given structure depends critically on the magnetic state of
the metal ions, and high-spin states are favored by the
DFT+$U$ scheme we used. The ordering of the spin on the

<table>
<caption>TABLE II. Calculated $U$ in eV.</caption>
<tbody>
<tr>
<td>
</td>
<td>
Mn²⁺
</td>
<td>
Mn³⁺
</td>
<td>
Mn⁴⁺
</td>
<td>
Fe²⁺
</td>
<td>
Fe³⁺
</td>
<td>
Co²⁺
</td>
<td>
Co³⁺
</td>
<td>
Co⁴⁺
</td>
<td>
Ni²⁺
</td>
<td>
Ni³⁺
</td>
<td>
Ni⁴⁺
</td>
</tr>
<tr>
<td>
Olivine
</td>
<td>
3.92
</td>
<td>
5.09
</td>
<td>
</td>
<td>
3.71
</td>
<td>
4.90
</td>
<td>
5.05
</td>
<td>
6.34
</td>
<td>
</td>
<td>
5.26
</td>
<td>
6.93
</td>
<td>
</td>
</tr>
<tr>
<td>
Layered
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
4.91
</td>
<td>
5.37
</td>
<td>
</td>
<td>
6.70
</td>
<td>
6.04
</td>
</tr>
<tr>
<td>
Spinel
</td>
<td>
</td>
<td>
4.64
</td>
<td>
5.04
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
5.62
</td>
<td>
6.17
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
Monoxide (Ref. 40)
</td>
<td>
3.6
</td>
<td>
</td>
<td>
</td>
<td>
4.6
</td>
<td>
</td>
<td>
5.0
</td>
<td>
</td>
<td>
</td>
<td>
5.1
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

ions in different magnetic structures (i.e., ferromagnetic, antiferromagnetic or more complicated ordering) results in difference in the total energy of the order 10–60 meV per formula unit. From the total energies, the average lithiation potential can be calculated through Eq. (3).

Table II shows the self-consistently calculated effective $U$ values for Mn, Fe, Co, and Ni in different valence states and structures. For each structure, $U$ is calculated for the low and high valence states, respectively, in a fully lithiated and delithiated structure. In all cases, except Ni³⁺/Ni⁴⁺ in the layered structure, a higher valence state leads to a higher $U$. For the three cases (Mn³⁺/Co³⁺/Ni³⁺) for which we have a $U$ in close-packed (layered or spinel) oxides and in an olivine phosphate structure, $U$ is higher for the olivine structure. This may be related to the fact that the TM octahedra in the olivine are only corner sharing in two directions but separated from each other by phosphate groups in the third direction, leading to very narrow bandwidth and well localized TM-$d$ states. For comparison we also list the $U$ values calculated in Ref. 40 for TM monoxides MO (M=Mn, Fe, Co, and Ni) in non-spin-polarized state. Good agreement with LiMPO₄ is found except for Fe²⁺. We note that in Ref. 26 the $U$ value of 4.3 eV for FeO was obtained with the same linear response approach, in good agreement with Ref. 40. So the difference between our results for Fe²⁺ and that in Ref. 40 may be due to different crystal environment.

Figures 4 and 5 show, respectively, the average Li insertion voltage as function of $U$ in the olivine, and in the layered and spinel structure. The horizontal short line indicates the experimentally measured voltage. Three calculated points for each system are marked on the curve: the small open circles indicate, respectively, the voltage one would obtain using the calculated $U$ for the most reduced and most oxidized TM state in each structure (e.g., Fe²⁺ and Fe³⁺ in LiFePO₄). The large filled circle corresponds to the voltage for the averaged $U$. The results for each system are discussed in more detail below.

![](./images/812313635907960832_4.jpg)

FIG. 4. Voltage as a function of $U$ for the LiMPO₄ materials in the olivine structure. The short horizontal lines on the curves indicate the experimental voltage of each material (no experimental information is available for LiNiPO₄). The two small open circles on a curve represent the voltage for $U$ calculated in the oxidized (delithiated) or reduced (lithiated) states. The big solid circle represents the voltage at the average of the two $U$ values.

### A. Olivine structures LiₓMPO₄ (M=Mn, Fe, Co, Ni)

According to neutron-diffraction experiments⁴¹,⁴² the magnetic ordering of LiMPO₄ is antiferromagnetic (AFM) within the approximately square lattice of metal ions for each of the above four TM. FePO₄ is also found to have AFM magnetic ordering.⁴² The results in Fig. 4 have been calculated with AFM spin configuration in both end members. The calculated and experimental cell parameters, as well as the electronic occupation of the TM ions are listed in Table III.

Mn: Both Mn²⁺ and Mn³⁺ are high-spin ions in GGA and GGA+$U$ calculations. Attempts to constrain them to lower spin states lead to much higher energy. FM ordered magnetic structures are 10–30 meV higher in energy than the AFM ordered magnetic structure as $U$ is varied. A strong collective Jahn-Teller distortion is observed in MnPO₄, where Mn³⁺ is in the high-spin $t_{2g}^{3}e_{g}^{1}$ state, in GGA(+$U$). The experimental voltage for the MnPO₄/LiMnPO₄ redox couple has been obtained from Ref. 30. The voltage predicted with GGA+$U$ $U$=($U_{\text{Mn}^{2+}}$+$U_{\text{Mn}^{3+}}$)/2 is within a few percent of the experimental voltage (4.1 V), and in sharp contrast to the large error made by GGA ($V_{\text{GGA}}$=2.98 V).

Fe: Both Fe²⁺ and Fe³⁺ are high-spin in GGA(+$U$) calculations, and the AFM ordering is more stable than FM ordering. Using $U_{\text{Fe}^{2+}}$ and $U_{\text{Fe}^{3+}}$ we calculated a voltage of 3.39 and 3.55 V, respectively. The voltage calculated with the average $U$=4.30 eV is 3.47 V, which agrees very well with the experimentally measured value of 3.5 V.²⁴ This is a sub-

![](./images/812313635907960832_5.jpg)

FIG. 5. Voltage as a function of $U$ for the layered and spinel structures. Legend the same as in Fig. 4.

<table>
<caption>TABLE III. Cell parameters of the olivine structures in the lithiated and delithiated states, as well as the corresponding electron configuration at the TM ions.</caption>
<thead>
<tr>
<th>
</th>
<th>
</th>
<th>
$a$($\mathring{\text{A}}$)
</th>
<th>
$b$($\mathring{\text{A}}$)
</th>
<th>
$c$($\mathring{\text{A}}$)
</th>
<th>
$V$($\mathring{\text{A}}^{3}$)
</th>
<th>
TM ion configuration
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
LiMnPO4
</td>
<td>
GGA
</td>
<td>
10.55
</td>
<td>
6.13
</td>
<td>
4.78
</td>
<td>
309.13
</td>
<td>
$t_{2g}^{3}e_{g}^{2}$
</td>
</tr>
<tr>
<td>
</td>
<td>
GGA+$U$
</td>
<td>
10.62
</td>
<td>
6.17
</td>
<td>
4.80
</td>
<td>
314.52
</td>
<td>
$t_{2g}^{3}e_{g}^{2}$
</td>
</tr>
<tr>
<td>
</td>
<td>
Expt. (Ref. 30)
</td>
<td>
10.44
</td>
<td>
6.09
</td>
<td>
4.75
</td>
<td>
302.00
</td>
<td>
</td>
</tr>
<tr>
<td>
MnPO4
</td>
<td>
GGA
</td>
<td>
9.92
</td>
<td>
6.01
</td>
<td>
4.93
</td>
<td>
293.92
</td>
<td>
$t_{2g}^{3}e_{g}^{1}$
</td>
</tr>
<tr>
<td>
</td>
<td>
GGA+$U$
</td>
<td>
9.98
</td>
<td>
6.07
</td>
<td>
4.96
</td>
<td>
300.47
</td>
<td>
$t_{2g}^{3}e_{g}^{1}$
</td>
</tr>
<tr>
<td>
</td>
<td>
Expt. (Ref. 30)
</td>
<td>
9.69
</td>
<td>
5.93
</td>
<td>
4.78
</td>
<td>
274.67
</td>
<td>
</td>
</tr>
<tr>
<td>
LiFePO4
</td>
<td>
GGA
</td>
<td>
10.39
</td>
<td>
6.04
</td>
<td>
4.75
</td>
<td>
298.09
</td>
<td>
$t_{2g}^{4}e_{g}^{2}$
</td>
</tr>
<tr>
<td>
</td>
<td>
GGA+$U$
</td>
<td>
10.42
</td>
<td>
6.07
</td>
<td>
4.76
</td>
<td>
301.07
</td>
<td>
$t_{2g}^{4}e_{g}^{2}$
</td>
</tr>
<tr>
<td>
</td>
<td>
Expt. (Ref. 27)
</td>
<td>
10.33
</td>
<td>
6.01
</td>
<td>
4.69
</td>
<td>
291.39
</td>
<td>
</td>
</tr>
<tr>
<td>
FePO4
</td>
<td>
GGA
</td>
<td>
9.99
</td>
<td>
5.93
</td>
<td>
4.90
</td>
<td>
290.28
</td>
<td>
$t_{2g}^{3}e_{g}^{2}$
</td>
</tr>
<tr>
<td>
</td>
<td>
GGA+$U$
</td>
<td>
9.99
</td>
<td>
5.88
</td>
<td>
4.87
</td>
<td>
286.07
</td>
<td>
$t_{2g}^{3}e_{g}^{2}$
</td>
</tr>
<tr>
<td>
</td>
<td>
Expt. (Ref. 27)
</td>
<td>
9.82
</td>
<td>
5.79
</td>
<td>
4.79
</td>
<td>
272.36
</td>
<td>
</td>
</tr>
<tr>
<td>
LiCoPO4
</td>
<td>
GGA
</td>
<td>
10.30
</td>
<td>
5.93
</td>
<td>
4.75
</td>
<td>
290.13
</td>
<td>
$t_{2g}^{5}e_{g}^{2}$
</td>
</tr>
<tr>
<td>
</td>
<td>
GGA+$U$
</td>
<td>
10.33
</td>
<td>
5.97
</td>
<td>
4.76
</td>
<td>
293.55
</td>
<td>
$t_{2g}^{5}e_{g}^{2}$
</td>
</tr>
<tr>
<td>
</td>
<td>
Expt. (Ref. 31)
</td>
<td>
10.20
</td>
<td>
5.92
</td>
<td>
4.70
</td>
<td>
283.90
</td>
<td>
</td>
</tr>
<tr>
<td>
CoPO4
</td>
<td>
GGA
</td>
<td>
9.71
</td>
<td>
5.48
</td>
<td>
4.59
</td>
<td>
244.24
</td>
<td>
$t_{2g}^{6}$
</td>
</tr>
<tr>
<td>
</td>
<td>
GGA+$U$
</td>
<td>
9.98
</td>
<td>
5.78
</td>
<td>
4.74
</td>
<td>
273.42
</td>
<td>
$t_{2g}^{4}e_{g}^{2}$
</td>
</tr>
<tr>
<td>
</td>
<td>
Expt. (Ref. 31)
</td>
<td>
10.09
</td>
<td>
5.85
</td>
<td>
4.72
</td>
<td>
278.66
</td>
<td>
</td>
</tr>
<tr>
<td>
LiNiPO4
</td>
<td>
GGA
</td>
<td>
10.09
</td>
<td>
5.91
</td>
<td>
4.74
</td>
<td>
282.66
</td>
<td>
$t_{2g}^{6}e_{g}^{2}$
</td>
</tr>
<tr>
<td>
</td>
<td>
GGA+$U$
</td>
<td>
10.12
</td>
<td>
5.90
</td>
<td>
4.73
</td>
<td>
282.42
</td>
<td>
$t_{2g}^{6}e_{g}^{2}$
</td>
</tr>
<tr>
<td>
</td>
<td>
Expt. (Ref. 43)
</td>
<td>
10.03
</td>
<td>
5.85
</td>
<td>
4.68
</td>
<td>
274.49
</td>
<td>
</td>
</tr>
<tr>
<td>
NiPO4
</td>
<td>
GGA
</td>
<td>
9.66
</td>
<td>
5.72
</td>
<td>
4.71
</td>
<td>
260.25
</td>
<td>
$t_{2g}^{6}e_{g}^{1}$
</td>
</tr>
<tr>
<td>
</td>
<td>
GGA+$U$
</td>
<td>
9.92
</td>
<td>
5.82
</td>
<td>
4.84
</td>
<td>
279.43
</td>
<td>
$t_{2g}^{6}e_{g}^{1}$
</td>
</tr>
</tbody>
</table>

stantial improvement over the GGA predicted value of 2.97 V. Previously, the localization of electrons induced by $U$ was also shown to qualitatively affect the phase behavior in this system.25

$Co$: In LiCoPO4, $Co^{2+}$ is stable in the high-spin $t_{2g}^{5}e_{g}^{2}$ state. In the delithiated CoPO4,$Co^{3+}$ is stable as non-spin-polarized with GGA, but more stable by several eV with GGA+$U$ in the high spin $t_{2g}^{4}e_{g}^{2}$ configuration at the calculated $U$ value of 6.34 eV. As shown in Table III the cell parameters of CoPO4 calculated with non-spin-polarized $Co^{3+}$ in GGA is appreciably smaller than experimental values, while GGA usually slightly overestimates cell parameters. With GGA +$U$ and high-spin $Co^{3+}$ the calculated parameters are close to experimental values. While there is only limited electrochemical data on this material,27 the predicted voltage of 4.73 V at $U_{\text{average}}$ is within a few % of the result 4.8 V established by Anime et al.,31 compared to the poor GGA prediction of 3.70 V. The high voltage of this material makes it particularly attractive for high-energy density applications.

$Ni$: Though LiNiPO4 has been synthesized, no Li can be removed from it electrochemically.44 Hence the voltage is probably larger than 5 V, the limit of most electrolyte systems. At $x$=1 $Ni^{2+}$ is stable as high-spin $t_{2g}^{6}e_{g}^{2}$. At $x$=0 $Ni^{3+}$ occurs in the low spin state $t_{2g}^{6}e_{g}^{1}$ for both GGA and GGA +$U$, but the high spin state $t_{2g}^{5}e_{g}^{2}$ is less unstable in GGA +$U$ than in GGA. Note that low-spin $Ni^{3+}$ is a weak Jahn-Teller ion, and no appreciable collective distortion is observed in our relaxed unit cell. With $U_{\text{average}}$, a voltage of 5.07 V is obtained, which is in agreement with the fact that no Li can be removed from this material.

### B. Layered $Li_{x}$MO2 (M=Co, Ni)

For the layered and spinel structures AFM spin ordering on transition metal ions is topologically frustrated, and their

actual magnetic ground states are not always clear in experiment. But as the energy associated with different magnetic orderings is small, the simple FM ordering is used in the following calculations.

Co: In $LiCoO_2$, $Co^{3+}$ is stable in the non-spin-polarized state for the calculated $U_{Co^{3+}}=4.91$ eV. At $x=0$,$Co^{4+}$ is almost degenerate in either non-spin-polarized or spin-polarized $t_{2g}^{5}$ in GGA, but more stable with spin-polarization in GGA+$U$ at the calculated $U_{Co^{4+}}=5.37$ eV. While GGA $+U$ still improves the agreement of voltage with experiment$^{23}$ over pure GGA, the error for this system is larger than in the other systems we calculated. This might be related to the fact that the GGA result is already closer to experiment than for all other systems.

Ni: In $LiNiO_2$, $Ni^{3+}$ is most stable in the low-spin $t_{2g}^{6}e_{g}^{1}$ state and is a weak Jahn-Teller ion. With GGA a distorted unit cell is found with the short and the long Ni-O bond length being $1.92$ $\mathring{A}$ and $2.13$ $\mathring{A}$, respectively, compared to experimental values of $1.91$ $\mathring{A}$ and $2.14$ $\mathring{A}$, $^{39}$ and a stabilization energy relative to an undistorted cell of only $-2$ meV, within the range of numerical errors, compared to $-11$ meV in Ref. 39. With GGA+$U$ no appreciable distortion is observed. Experimentally there is no cooperative Jahn-Teller distortion in $LiNiO_2$ though the Ni-O octahedra are locally Jahn-Teller distorted,$^{45}$ suggesting a very small stabilization energy, consistent with both GGA and GGA+$U$ results. At $x=0$,$Ni^{4+}$ is stable as a non-spin-polarized ion. The GGA $+U$ voltage value of $3.92$ V agrees well with the experimental average voltage of $3.85$ V,$^{22}$ and is substantially better than the GGA result of $3.19$ V.

### C. Spinel $Li_xM_2O_4$ (M=Mn, Co)
For the spinel $Li_xMn_2O_4$ there are two distinct plateaus in the voltage profile, between $0<x<1$ and $1<x<2$, respectively. For $0<x<1$ Li enters tetrahedral sites, while the reaction from $LiMn_2O_4$ to $Li_2Mn_2O_4$ occurs through a two-phase process whereby the $LiMn_2O_4$ phase with only tetrahedral Li disappears at the expense of the $Li_2Mn_2O_4$ phase with all Li octahedral. Calculations were done for $x$ =0, 1, and 2 structures to get separate average voltage values for the two processes. For M=Co the $0<x<1$ reaction potential curve is difficult to obtain accurately in experiments. Therefore only the average voltage for the $1<x<2$ reaction is shown in Fig. 5.

Mn: Both $Mn^{4+}$ and $Mn^{3+}$ are high-spin. $Mn^{3+}$ is a strong Jahn-Teller active ion. In GGA, the calculated Mn-O short and long bond lengths $1.94$ $\mathring{A}$ and $2.40$ $\mathring{A}$ agree with Ref. 39; in GGA+$U$ they become $1.96$ $\mathring{A}$ and $2.32$ $\mathring{A}$, respectively. Experimental values are $1.94$ $\mathring{A}$ and $2.29$ $\mathring{A}$, respectively,$^{46}$ showing that the good structural prediction of GGA is retained in GGA+$U$. Coexistence of distinct $Mn^{4+}$ and $Mn^{3+}$ is found in GGA+$U$ in the $LiM_2O_4$ compound. The GGA+$U_{average}$ results (4.19 V and 2.97 V, respectively, for the first and second plateaus) are in excellent agreement with the experimentally measured values of 4.15 V and 2.95 V.$^{23}$

Co: Like in the layered structure, $Co^{3+}$ in $Li_2Co_2O_4$ is non-spin-polarized, and at $x=0$ $Co^{4+}$ is more stable as spin polarized $t_{2g}^{5}$ in GGA+$U$. The GGA+$U$ voltage (3.56 V at $U_{average}$=4.84 eV) agrees very well with experimental data available for the $Li_1Co_2O_4$ to $Li_2Co_2O_4$ reaction [3.5 V (Ref. 32)].

![](./images/812313635907960832_6.jpg)

FIG. 6. Difference between calculated and experimental voltage (Refs. 5-9), for GGA and GGA+$U$, at the calculated $U$ of the oxidized (delithiated) and reduced (lithiated) states, respectively ($l$ =layered,$s$=spinel). For the spinel structures two voltage values for the $0<x<1$ and $1<x<2$ plateaus are calculated separately. Olivine $LiNiPO_4$ is not shown here because the voltage is unknown.

Note that in the $x=1$ structure of the spinel materials $Li_xM_2O_4$ we find distinct $M^{3+}$ and $M^{4+}$ ions in GGA+$U$ instead of ions of intermediate valence. The same phenomenon was observed in the intermediate structures $Li_xFePO_4$ of the iron phosphate.$^{25}$ This is a direct consequence of the $E_U$ correction term to the total energy in Eq. (4) which penalizes the nonintegral occupation of the $d$ orbitals. Such charge ordering is necessary for correctly predicting the 0 $<x<1$ and $1<x<2$ average voltage values of $Li_xMn_2O_4$ simultaneously, as well as the $1<x<2$ voltage of $Li_xCo_2O_4$, and is not present in pure GGA unless localization is assisted by a strong polaronic contribution such as the Jahn-Teller distortion around $Mn^{3+}$.

### IV. DISCUSSION
Introduction of Coulombic on-site correlations in GGA through the GGA+$U$ clearly improves predicted lithiation potentials considerably over the use of pure GGA (or LDA for that matter). The errors of GGA+$U$ and pure GGA on all systems for which we have experimental data are summarized in Fig. 6. Pure GGA consistently underestimates the lithiation voltage, which is a measure of the energy lowering when Li is transferred from Li metal (the anodic reference) to a $Li^+$ ion and electron in the TM oxide or phosphate. The contribution of the $Li^+$ ion to the reaction energy is largely electrostatic, and one would expect this effect to be well captured in GGA or LDA. Hence, the large voltage error in LDA/GGA must arise from the electron transfer from Li

235121-6

metal to the TM cation. Since the voltage is always underes- timated in LDA/GGA these approximations clearly penalize the energy of the electron on the TM, thereby lowering the reaction energy. It seems reasonable to attribute this to the poor treatment of electronic correlations in LDA/GGA. In metallic lithium the electron is affected by a small self- interaction in LDA/GGA as its charge density is delocalized. On the TM ion, however, the electron occupies a much more localized $d$-orbital and will experience a much larger self- interaction. The lack of cancellation between the self- interactions contributions to the energy, which are related to an improper description of the correlation effects in LDA/ GGA, leads to a systematic error in the prediction of the redox potential. In the direction in which the electron is transferred from a delocalized to a localized state, the reac- tion energy is penalized (not negative enough), making the potential too small. The use of GGA+$U$ allows for a better description of the electronic correlation and, by discouraging fractional occupations of the Kohn-Sham orbitals, removes the spurious self-interaction thus producing a much more accurate prediction of the redox voltage. While we demon- strate the GGA/LDA problem and improvement obtained with DFT+$U$ on Li-insertion materials, we believe that a more accurate description of correlation effects within the DFT+$U$ scheme is also necessary in the study of other redox processes in which electrons are transferred between states of different kind (e.g., catalysis of organic molecules on TM surfaces). In fact, as explained in Ref. 26, a better description of the electronic correlation (which enforces the indepen- dence of the single electron energy eigenvalues of the par- tially occupied states on their occupation, thus leading to the elimination of the spurious self-interaction) is needed to re- produce the physical difference among the ionization poten- tial and the electronic affinity (or the band gap in crystalline solids) which plays a very important role in the energetics of processes involving electron transfer.

In our calculations high-spin TM ions are always energeti- cally favored by GGA+$U$ over low-spin or non-spin- polarized states. In $CoPO_{4}$ the non-spin-polarized $Co^{3+}$ in GGA leads to cell parameters inconsistent with experiment. In GGA+$U$ $Co^{3+}$ becomes high spin, improving agreement with experiment. For the other systems the GGA and GGA+$U$ cell parameters are rather close, though GGA+$U$ seems to lead to volumes that are slightly too high. Jahn-Teller distortions predicted by GGA are also reproduced in GGA+$U$ for $Mn^{3+}$.

In summary, we have shown that the underestimation of the lithium intercalation voltage in LDA/GGA can be cor- rected by using GGA+$U$ with a self-consistently calculated parameters $U$, without sacrificing properties that are already accurately predicted by GGA (e.g., Jahn-Teller effect, cell parameters, magnetic ordering). Voltages for most systems are predicted within a few % of experimental values.

We believe that DFT+$U$ will significantly improve the accuracy of voltage prediction for candidate materials can be predicted, and therefore enhance the capability of screening new materials for their ability to be good cathodes.

## ACKNOWLEDGMENTS

The authors thank Thomas Maxisch for helpful discus- sions. This work was supported by the Department of Energy under Contract No. DE-FG02-96ER45571 and by the MRSEC program of the National Science Foundation under Contract No. DMR-0213282.

$^{1}$V. I. Anisimov, J. Zaanen, and O. K. Andersen, Phys. Rev. B $\textbf{44}$, 943 (1991).
$^{2}$V. I. Anisimov $et$ $al.$, Phys. Rev. B $\textbf{48}$, 16929 (1993).
$^{3}$A. I. Liechtenstein, V. I. Anisimov, and J. Zaanen, Phys. Rev. B $\textbf{52}$, R5467 (1995).
$^{4}$M. K. Aydinol, A. F. Kohan, G. Ceder, K. Cho, and J. Joannopo- ulos, Phys. Rev. B $\textbf{56}$, 1354 (1997).
$^{5}$C. Wolverton and A. Zunger, J. Electrochem. Soc. $\textbf{145}$, 2424 (1998).
$^{6}$M. Launay, F. Boucher, P. Gressier, and G. Ouvrard, J. Solid State Chem. $\textbf{176}$, 556 (2003).
$^{7}$P. Tang and N. A. W. Holzwarth, Phys. Rev. B $\textbf{68}$, 165107 (2003).
$^{8}$B. J. Hwang, Y. W. Tsai, D. Carlier, and G. Ceder, Chem. Mater. $\textbf{15}$, 3676 (2003).
$^{9}$X. Rocquefelte, F. Boucher, P. Gressier, and G. Ouvrard, Chem. Mater. $\textbf{15}$, 1812 (2003).
$^{10}$K. R. Kganyago, P. E. Ngoepe, and C. R. A. Catlow, Solid State Ionics $\textbf{159}$, 21 (2003).
$^{11}$R. Prasad, R. Benedek, and M. M. Thackeray, Bull. Mater. Sci. $\textbf{26}$, 147 (2003).
$^{12}$Y. Koyama, I. Tanaka, and H. Adachi, Adv. Quantum Chem. $\textbf{42}$, 145 (2003).
$^{13}$D. Morgan, G. Ceder, M. Y. Saidi, J. Barker, J. Swoyer, H. Huang, and G. Adamson, Chem. Mater. $\textbf{14}$, 4684 (2002).
$^{14}$M. L. Doublet, F. Lemoigno, F. Gillot, and L. Monconduit, Chem. Mater. $\textbf{14}$, 4126 (2002).
$^{15}$A. Van der Ven, M. K. Aydinol, and G. Ceder, J. Electrochem. Soc. $\textbf{145}$, 2149 (1998).
$^{16}$I. A. Courtney, J. S. Tse, O. Mao, J. Hafner, and J. R. Dahn, Phys. Rev. B $\textbf{58}$, 15 583 (1998).
$^{17}$A. Van der Ven $et$ $al.$, Phys. Rev. B $\textbf{58}$, 2975 (1998).
$^{18}$M. E. Arroyo y de Dompablo, A. Van der Ven, and G. Ceder, Phys. Rev. B $\textbf{66}$, 064112 (2002).
$^{19}$J. Reed, G. Ceder, and A. Van der Ven, Electrochem. Solid-State Lett. $\textbf{4}$, A78 (2001).
$^{20}$A. Van der Ven and G. Ceder, Electrochem. Solid-State Lett. $\textbf{3}$, 301 (2000).
$^{21}$D. Morgan $et$ $al.$, J. Power Sources $\textbf{119}$, 755 (2003).
$^{22}$C. Delmas $et$ $al.$, Int. J. Inorg. Mater. $\textbf{1}$, 11 (1999).
$^{23}$T. Ohzuku and A. Ueda, Solid State Ionics $\textbf{69}$, 201 (1994).
$^{24}$A. Yamada, S. C. Chung, and K. Hinokuma, J. Electrochem. Soc. $\textbf{148}$, A224 (2001).
$^{25}$F. Zhou, C. A. Marianetti, M. Cococcioni, D. Morgan, and G. Ceder, Phys. Rev. B $\textbf{69}$, 201101 (2004).
$^{26}$M. Cococcioni, Ph.D. thesis, International School for Advanced Studies (SISSA), 2002, available at http://www.sissa.it/cm/

phd.php; M. Cococcioni and S. de Gironcoli, cond-mat/0405160, Phys. Rev. B (to be published).

$^{27}$A. K. Padhi, K. S. Nanjundaswamy, and J. B. Goodenough, J. Electrochem. Soc. 144, 1188 (1997).

$^{28}$For review see M. M. Thackeray, J. Electrochem. Soc. 142, 2558 (1995) and references therein.

$^{29}$W. R. McKinnon, "Insertion electrodes I: Atomic and electronic structure of the hosts and their insertion compounds," in *Solid State Electrochemistry*, edited by P. G. Bruce (Cambridge University Press, Cambridge, 1995), Vol. 16, pp. 163-198.

$^{30}$G. Li, H. Azuma, and M. Tohda, Electrochem. Solid-State Lett. 5, A135 (2002).

$^{31}$K. Amine, H. Yasuda, and M. Yamachi, Electrochem. Solid-State Lett. 3, 178 (2000).

$^{32}$S. Choi and A. Manthiram, J. Electrochem. Soc. 149, A162 (2002).

$^{33}$S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, Phys. Rev. B 57, 1505 (1998).

$^{34}$S. L. Adler, Phys. Rev. 126, 413 (1962); N. Wiser, ibid. 129, 62 (1963).

$^{35}$P. E. Blöchl, Phys. Rev. B 50, 17 953 (1994).

$^{36}$G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).

$^{37}$G. Kresse and J. Furthmuller, Phys. Rev. B 54, 11 169 (1996); Comput. Mater. Sci. 6, 15 (1996).

$^{38}$S. K. Mishra and G. Ceder, Phys. Rev. B 59, 6120 (1999).

$^{39}$C. A. Marianetti, D. Morgan, and G. Ceder, Phys. Rev. B 63, 224304 (2001).

$^{40}$W. E. Pickett, S. C. Erwin, and E. C. Ethridge, Phys. Rev. B 58, 1201 (1998).

$^{41}$R. P. Santoro, D. J. Segal, and R. E. Newman, J. Phys. Chem. Solids 27, 1192 (1966); R. P. Santoro and R. E. Newman, Acta Crystallogr. 22, 344 (1967).

$^{42}$G. Rousse, J. Rodriguez-Carvajal, S. Patoux, and C. Masquelier, Chem. Mater. 15, 4082 (2003) and the references therein.

$^{43}$O. García-Moreno, M. Alvarez-Vega, F. García-Alvarado, J. García-Jaca, J. M. Gallardo-Amores, M. L. Sanjuán, and U. Amador, Chem. Mater. 13, 1570 (2001).

$^{44}$S. Okada et al., J. Power Sources 97-98, 430 (2001).

$^{45}$A. Rougier, C. Delmas, and A. V. Chadwick, Solid State Commun. 94, 123 (1995).

$^{46}$R. Hoppe, G. Brachtel, and M. Jansen, Z. Anorg. Allg. Chem. 417, 1 (1975).