Structural, electronic, and magnetic properties of FeSi: hybrid functionals and non-local exchange

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2006 J. Phys.: Condens. Matter 18 7437

(http://iopscience.iop.org/0953-8984/18/31/035)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 136.186.1.81
This content was downloaded on 17/05/2015 at 13:26

Please note that terms and conditions apply.

# Structural, electronic, and magnetic properties of FeSi: hybrid functionals and non-local exchange

Matthias Neef, Klaus Doll and Gertrud Zwicknagl

Institut für Mathematische Physik, TU Braunschweig, Mendelssohnstraße 3,
D-38106 Braunschweig, Germany

E-mail: m.neef@tu-bs.de

Received 23 March 2006, in final form 21 June 2006
Published 21 July 2006
Online at stacks.iop.org/JPhysCM/18/7437

## Abstract
The structural, electronic, and magnetic properties of FeSi are investigated by first-principles all-electron density functional calculations. The interplay between non-local exchange and correlations is studied by comparing results obtained with standard density functionals, the hybrid functional B3LYP and the Hartree–Fock ansatz. The calculations are performed using a local basis set. For the standard functionals, previous theoretical results for the non-magnetic semiconducting ground state are well reproduced. With the hybrid functional B3LYP, a magnetic metallic solution is found in addition to the non-magnetic low-energy semiconducting one. The influence of the non-local exchange is also reflected in the increased value of the indirect gap which separates the valence and conduction bands.

## 1. Introduction
Magnetic semiconductors are attracting great scientific interest because of their potential use for spintronics. Promising candidates for technological applications are the transition metal monosilicides and their alloys. These materials exhibit rich phase diagrams reflecting the great sensitivity with respect to changes in external control parameters like temperature, pressure, and magnetic field. An indispensable prerequisite for technical applications is therefore a microscopic understanding of the subtle interplay between the structural, electronic, and magnetic properties.

FeSi is experimentally found to have a non-magnetic ground state and a narrow excitation gap of $\Delta < 0.1$ eV [1–3]. The unusual variation with temperature of the magnetic susceptibility [4] and of the resistivity exhibit similarities with the behaviour found in lanthanide compounds like CeNiSn and $\mathrm{Ce_3Bi_4Pt_3}$. This fact prompted some groups to model FeSi as a transition metal analogue of a Kondo insulator [5, 6]. This model, in turn, implies adopting a localized picture for the Fe d electrons and to describe them as local moments. The alternative itinerant picture [7], on the other hand, is supported by detailed band structure calculations within the

local density approximation (LDA) [8–11]. The latter correctly yield a non-magnetic insulating ground state and a small indirect gap of $\Delta_{\text{LDA}} \sim 0.1$ eV. In addition, the experimental geometry is well reproduced [11, 12].

Despite this success of LDA and the generalized gradient approximation (GGA), important questions remain open. Prominent among them is the variation with temperature of the magnetic susceptibility, which points to the existence of metastable low-energy magnetic states. The fact that the latter cannot be reproduced in LDA or GGA indicates that the local effective single-particle picture does not fully capture the complex low-energy physics. An adequate description of the electronic structure must account for non-local exchange and local Coulomb correlations. The consequences of the latter were studied by Anisimov *et al* [13], who augmented the LDA treatment by a finite Coulomb repulsion $U$. The model studies yielded a metastable magnetic state; the required values for $U$, however, were rather large. The *ab initio* calculations presented here explore the influence of non-local exchange in that they could be considered as complementary to the correlation model study.

The Hartree–Fock (HF) approach, which exclusively accounts for the non-local exchange neglecting correlation effects, on the other hand, usually yields too large a theoretical value for the gap. Hybrid functionals which mix Fock exchange with standard functionals have recently become popular in solid state physics [14] because they often improve the results for electronic properties, especially band gaps [15–17]. It is thus interesting to explore this system with the hybrid functional B3LYP [18, 19] (for a brief review see also [20]) and the Hartree–Fock approach, in addition to the standard LDA and GGA functionals. A comparison of the band gap with the various schemes can be made, and the question of possible magnetic solutions can be addressed.

The intent of the present paper is twofold. The main purpose is to further assess the range of validity of the itinerant band picture in FeSi. This is achieved by extending the density functional theory (DFT) calculations to hybrid functionals which recently became available for solids. In addition, the pure Hartree–Fock approach is applied to get an insight into the interplay of non-local exchange and electronic correlations. The quantities chosen for discussion include ground state properties like the lattice constant and internal coordinates in the equilibrium as well as the band gap. The (meta)stability of magnetic and metallic solutions is discussed. The effective Schrödinger equation is solved using a local basis with Gaussian type orbitals. This paper therefore also aims at establishing the usage of Gaussian type orbitals as basis functions for this class of systems. To demonstrate the flexibility and reliability of the computational scheme we compare our results to reference data obtained from standard band structure methods wherever possible.

The paper is structured as follows. Section 2 gives a brief exposition of the methods and approximations employed. The numerical procedure adopted in the actual calculation is tested in section 3. In the subsequent sections 4 and 5 we give details of the models and results obtained. The conclusions are summarized in section 6.

## 2. Method and calculational details

FeSi is considered in its experimentally established B20 structure with a unit cell containing four silicon and four iron atoms. This structure is referred to as as $\epsilon$-FeSi and it has 12 symmetry operations. The space group is $P2_13$ (198) and the point symmetry at the iron or silicon site is $C_3$. Fe has seven Si neighbours, whose distance is dependent on the internal coordinates. The experimental values for the lattice constant and the internal coordinates at ambient pressure are $a = 4.489$ Å, $u_{\text{Fe}} = 0.137$, and $u_{\text{Si}} = 0.842$, respectively [21]. The latter indicate significant deviations from the rock salt structure B1 which is characterized by $u_{\text{Fe}} = 0.25$ and $u_{\text{Si}} = 0.75$.

<table><caption>Table 1. Diffuse exponents of the basis functions.</caption>
<tbody><tr><td></td><td colspan="3">Fe</td><td colspan="3">Si</td></tr>
<tr><td></td><td>sp</td><td>sp</td><td>d</td><td>sp</td><td>sp</td><td>d</td></tr>
<tr><td>LDA/GGA</td><td>0.53</td><td>0.13</td><td>0.27</td><td>0.45</td><td>0.18</td><td>0.53</td></tr>
<tr><td>B3LYP/HF</td><td>0.53</td><td>0.15</td><td>0.27</td><td>0.47</td><td>0.17</td><td>0.55</td></tr>
</tbody></table>

First-principles all-electron calculations were performed within the framework of DFT. The exchange-correlation functionals considered include the local density approximation with the Perdew-Zunger parameterization [22] derived from the Ceperley-Alder data and the gradient-corrected Perdew-Wang functional PW91 [23] as a variant of the generalized gradient approximation, which is referred to as GGA in the following. Of particular interest is the hybrid functional B3LYP which allows us to incorporate the non-local exchange. To better understand the role of electronic correlations, we compare the results to those obtained with the HF method.

All-electron calculations using a local basis set formalism were performed with the code CRYSTAL2003. A detailed description of the method is found in [24]. For a given functional we choose a fixed set of Gaussian type orbitals centred at the position of the atoms. The single-electron wavefunctions are represented as linear combinations of these basis functions. The present calculations use a basis set consisting of a [6s5p2d] basis at the Fe site and a [5s4p1d] basis at the Si site. The inner basis functions ([4s3p1d] for Fe and [3s2p] for Si) were taken from [25] and [26], respectively. Two more diffuse sp shells and one diffuse d shell were added to these basis sets. The latter were determined so as to minimize the total energy of FeSi in a hypothetical rock salt structure. The exponents of these additional basis functions are given in table 1.

A $\vec{k}$-point sampling net of size $16\times16\times16$ was used. A smearing temperature of 0.01 $E_h\approx0.272$ eV was applied to the Fermi function. A fully numerical integration was performed with an enlarged grid having 75 radial points and a maximum number of 434 angular points.

The electronic structure depends rather sensitively on the lattice parameters. For all effective single-particle models (HF, LDA, GGA and B3LYP), the optimal theoretical structure was determined. The internal coordinates, $u_{\text{Fe}}$ and $u_{\text{Si}}$, were determined using analytical gradients [27-29]; the equilibrium lattice constant was obtained by numerically determining the minimum of the total energy.

To search for metastable magnetic states, spin polarized calculations were performed for the lattice parameters as in [8] and for the optimized geometries of the present work.

### 3. Test of the basis set and the computational method

To demonstrate the accuracy and reliability of the computational method, we adopt both the LDA and GGA and compare the theoretical results for electronic and structural properties obtained with the local Gaussian type orbitals to reference data derived by other band structure methods. The latter include the linear augmented plane wave (LAPW) method and its full-potential version (FLAPW) as well as the ultra soft pseudopotential (USPP) method.

All methods consistently yield an insulating ground state. The values of the indirect band gap are listed in table 2 together with the structural parameters and the available experimental data. The results obtained using the Gaussian type orbitals are in excellent agreement with the corresponding FLAPW and USPP calculations and, in turn, with experiment. This demonstrates that CRYSTAL2003 provides a reliable and efficient method for geometry optimization.

<table>
<caption>Table 2. Results of the optimized geometry obtained by using the LDA and GGA. The lattice constant $a$ and the internal coordinates of iron $u_{\rm Fe}$ and of silicon $u_{\rm Si}$ were optimized. The bulk modulus $B$ and the indirect band gap $\Delta_{\rm ind}$ are displayed.</caption>
<tbody><tr>
<td/>
<td>$a$
($\text{\AA}$)</td>
<td>$B$
(GPa)</td>
<td>$u_{\rm Fe}$</td>
<td>$u_{\rm Si}$</td>
<td>$\Delta_{\rm ind}$
(eV)</td>
</tr>
<tr>
<td>LDA (present work)</td>
<td>4.39</td>
<td>264</td>
<td>0.140</td>
<td>0.843</td>
<td>0.121</td>
</tr>
<tr>
<td>LDA-FLAPW [11]</td>
<td>4.41</td>
<td/>
<td/>
<td/>
<td/>
</tr>
<tr>
<td>LDA-USPP [11]</td>
<td>4.38</td>
<td/>
<td/>
<td/>
<td/>
</tr>
<tr>
<td>GGA (present work)</td>
<td>4.46</td>
<td>224</td>
<td>0.139</td>
<td>0.842</td>
<td>0.151</td>
</tr>
<tr>
<td>GGA-USPP [11]</td>
<td>4.46; 4.47</td>
<td>209</td>
<td>0.136</td>
<td>0.841</td>
<td>0.15</td>
</tr>
<tr>
<td>Exp.</td>
<td>4.489 [21]</td>
<td>185 [30]; 209 [31]</td>
<td>0.137 [21]</td>
<td>0.842 [21]</td>
<td>&lt;0.1 [1–3]</td>
</tr>
</tbody></table>

<table>
<caption>Table 3. Results of the different methods calculated with the lattice parameter $a = 4.493$ $\text{\AA}$ and the internal coordinates $u_{\rm Fe} = 0.1358$ and $u_{\rm Si} = 0.844$. The indirect band gap $\Delta_{\rm ind}$, the total charges of iron and silicon, and the charges of iron sp and d basis functions are displayed.</caption>
<tbody><tr>
<td/>
<td>$\Delta_{\rm ind}$
($|e|$)</td>
<td>Fe sp
($|e|$)</td>
<td>Fe d
($|e|$)</td>
<td>Fe total
($|e|$)</td>
<td>Si total
($|e|$)</td>
</tr>
<tr>
<td>LDA</td>
<td>0.125</td>
<td>19.53</td>
<td>7.12</td>
<td>26.64</td>
<td>13.36</td>
</tr>
<tr>
<td>GGA</td>
<td>0.149</td>
<td>19.51</td>
<td>7.09</td>
<td>26.60</td>
<td>13.40</td>
</tr>
<tr>
<td>B3LYP</td>
<td>1.472</td>
<td>19.23</td>
<td>7.17</td>
<td>26.40</td>
<td>13.60</td>
</tr>
<tr>
<td>HF</td>
<td>6.140</td>
<td>19.42</td>
<td>6.93</td>
<td>26.36</td>
<td>13.65</td>
</tr>
</tbody></table>

## 4. Hybrid functionals and the role of non-local exchange: non-magnetic states

We next turn to the question of how the theoretical values for the structural and electronic properties are affected by the non-local exchange which is accounted for in the hybrid functional B3LYP. The focus is on the interplay between the latter and the correlation effects as described by LDA and GGA in the class of systems under consideration. With this objective, we compare the results obtained with B3LYP to their counterparts derived from HF. To illustrate the consequences arising from the differences in the treatment of the many-electron problem, we proceed in two steps. First we discuss the electronic properties at fixed geometry. We choose the same values for the lattice parameters as in [8], which are close to the experimental ones. In the second step, we determine the optimized geometry for the hybrid functional and the HF ansatz in close analogy to the procedure described in the preceding section. Throughout this section, we restrict ourselves to non-magnetic ground states and postpone the discussion of their stability to the next section.

### 4.1. Calculations at fixed geometry

The results for non-magnetic states at fixed geometry are summarized in table 3. The system appears to be rather covalent as the Mulliken population shows only small charge transfer from Si to Fe. Characteristic differences, however, appear in the band structure. This can be seen from the fact that the values of the indirect energy gap depend rather sensitively on the detailed effective single-particle model. LDA and GGA both give a small value which agrees remarkably well with the experiment. It was argued [8] that this was due to the fact that the states on both sides of the band gap are similar, since they are dominated by the Fe d states. Generally, the correction to the gap can be expressed in terms of the matrix elements of the self-energy operator evaluated with the valence and conduction band wavefunctions [32].

![](./images/811773866383769601_1.jpg)

Figure 1. Projected density of states for the different methods relative to the top of the valence band which is fixed at 0 eV. The straight line is the projection onto the Fe 3d band and the dashed line that onto the Si 3p band. The inset visualizes the Hartree-Fock band structure.

When the valence and conduction bands are similar, i.e., when the corresponding wavefunctions are derived from atomic orbitals of the same symmetry, the local (dynamic) self-energy contributions change only weakly across a narrow gap. As a result, one expects a rather small correction to the gap, which explains why the LDA gap is in good agreement with the experiment.

The gap is strongly overestimated by the HF method. This failure is well known from conventional semiconductors like Si, where it is usually attributed to the lack of screening. The B3LYP value of $\sim$1.5 eV is intermediate between LDA and HF values. This is to be expected, since this hybrid functional essentially augments the LDA by non-local exchange. These findings for narrow gap semiconductors disprove the speculation that a naive single-particle picture derived from B3LYP will give a better value for the energy gap than LDA does.

The differences in the electronic structure are associated with the Fe d states. This can be seen from the projected densities of states (PDOSs) displayed in figure 1. The results can be summarized as follows. LDA and GGA, whose PDOSs exhibit only marginal differences, support an itinerant picture for the Fe d electrons. The HF ansatz, on the other hand, suggests a

![](./images/811773866383769601_2.jpg)

Figure 2. Band placements of the Fe 3d and Si 3p band for the investigated methods relative to the top of the valence band. The centres of the bands were calculated by $\langle E\rangle=\int N(E)E\mathrm{d}E/\int N(E)\mathrm{d}E$ with the corresponding projected density of states $N(E)$. Calculating $\sqrt{\langle E^{2}\rangle-\langle E\rangle^{2}}$ yields to the effective band width.

(partially) localized description. This can be concluded from the fact that the band states in the vicinity of the top of the valence band have predominantly d-character for LDA and GGA while the spectral weight for the Fe d states is concentrated far away from the top of the valence band, at the HF level. The B3LYP density of states can be interpreted as an intermediate step between LDA or GGA and HF combining the characteristic features of the standard functionals (the high Fe d contribution close to the top of the valence band) and of HF (the broadening of the band gap and transfer of Fe d spectral weight from the low-energy to the high-energy regime).

For a more qualitative comparison, the band centre $\langle E\rangle_{a}$ and effective band widths $\sqrt{\langle E^{2}\rangle_{a}-\langle E\rangle_{a}^{2}}$ were calculated. Here $\langle\ldots\rangle_{a}$ with $a=\mathrm{Fe\ d}$ or $a=\mathrm{Si\ p}$ denotes the average $\langle\ldots\rangle_{a}=\int N_{a}(E)\ldots\mathrm{d}E/\int N_{a}(E)\mathrm{d}E$ formed with the PDOS for the Fe d or Si p states. The data are displayed in figure 2. Obviously, the widths of the Si p and Fe d HF bands are enlarged relative to their LDA counterparts. Focusing on the region close to the top of the valence band, we notice that the absolute position of the bottom of the Si p band is roughly the same with all methods. Thus, the main change in the Si bands is the position of the band centre and the width, which does however not have a huge influence on the physics close to the top of the valence or bottom of the conduction bands. The important differences which affect the low- energy behaviour are related to the Fe d band. Both the upper and the lower band edge of LDA, B3LYP and HF are different. The LDA and GGA results are similar and have the smallest band width. However, it should be mentioned that figure 2 gives only a crude description of the bands, and in particular the band gap is not visible in the band placements.

### 4.2. Optimized geometry

The differences in the electronic structure are reflected in the theoretical values for the equilibrium lattice parameters. The latter are listed in table 4 together with their experimental values. Excellent agreement is found among the values derived from LDA, GGA and the hybrid functional B3LYP. The HF geometry, on the other hand, differs significantly from the above- mentioned DFT results. The large lattice constant may arise from the fact that the Fe d electrons have a more localized character and consequently contribute less to the binding. This large lattice constant also leads to a relatively small value of the bulk modulus. Apart from an overall inflation of the lattice, the HF geometry is characterized by a different internal atomic position

![](./images/811773866383769601_3.jpg)

Figure 3. The band structure and density of states of the different methods with the corresponding optimized geometry of table 4. The band structure is plotted along the high symmetry points of the B20 structure and is relative to the top of the valence band.

<table>
<caption>Table 4. Results of the optimized geometry obtained by using the LDA, GGA, B3LYP functional and the Hartree–Fock method. The lattice constant $a$ and the internal coordinates of iron $u_{\text{Fe}}$ and of silicon $u_{\text{Si}}$ were optimized. The geometrical parameters, the resulting bulk modulus $B$ and the indirect band gap $\Delta_{\text{ind}}$ are displayed.</caption>
<thead>
<tr>
<th></th>
<th>$a$ (Å)</th>
<th>$B$ (GPa)</th>
<th>$u_{\text{Fe}}$</th>
<th>$u_{\text{Si}}$</th>
<th>$\Delta_{\text{ind}}$ (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>LDA</td>
<td>4.39</td>
<td>264</td>
<td>0.140</td>
<td>0.843</td>
<td>0.121</td>
</tr>
<tr>
<td>GGA</td>
<td>4.46</td>
<td>224</td>
<td>0.139</td>
<td>0.842</td>
<td>0.151</td>
</tr>
<tr>
<td>B3LYP</td>
<td>4.45</td>
<td>230</td>
<td>0.135</td>
<td>0.840</td>
<td>1.531</td>
</tr>
<tr>
<td>HF</td>
<td>4.81</td>
<td>53</td>
<td>0.152</td>
<td>0.846</td>
<td>3.362</td>
</tr>
<tr>
<td>Exp.</td>
<td>4.489 [21]</td>
<td>185 [30]; 209 [31]</td>
<td>0.137 [21]</td>
<td>0.842 [21]</td>
<td>&lt;0.1 [1–3]</td>
</tr>
</tbody>
</table>

parameter for the Fe site, $u_{\text{Fe}}$. The corresponding Si value deviates only slightly from the DFT values.

The changes in the atomic positions are also reflected in the dispersion of the energy bands displayed in figure 3. As expected, the LDA and GGA band structures are rather similar. Of particular interest are the magnitudes of the band gaps and the positions in $\vec{k}$-space they involve. For LDA, GGA, and B3LYP the minimum gap is indirect and involves the valence band maximum along $\Gamma R$ and the conduction band minimum along $\Gamma M$. The non-local exchange increases the magnitude of the indirect band gap which rises from 0.12 and 0.15 eV for LDA and GGA to 1.53 eV for B3LYP. The HF gap decreases strongly compared to the

Table 5. Results of the optimized geometry obtained by using the LDA, GGA, B3LYP functional
and the Hartree-Fock method. The lattice constant $a$ and the internal coordinates of iron $u_{\mathrm{Fe}}$ and of
silicon $u_{\mathrm{Si}}$ were optimized. The resulting iron and silicon charges are displayed.

|     | Fe sp ($|e|$) | Fe d ($|e|$) | Fe total ($|e|$) | Si total ($|e|$) |
|-----|---------------|--------------|------------------|------------------|
| LDA | 19.49         | 7.16         | 26.65            | 13.35            |
| GGA | 19.49         | 7.10         | 26.59            | 13.42            |
| B3LYP | 19.24       | 7.20         | 26.44            | 13.56            |
| HF  | 19.53         | 6.66         | 26.18            | 13.82            |

value at the shorter lattice constant in table 3, from $\sim 6$ to $\sim 3$ eV. This decrease of the gap with
increasing lattice constant is somewhat unexpected, but can be explained due the fact that the
iron sp occupancy and the silicon charge slightly increase and thus the broad sp bands get more
occupied, which results in a larger band width and thus a smaller gap. This is especially visible
when comparing the HF bands at the R point (figures 1 and 3).

The maximum direct band gap occurs for LDA, GGA and B3LYP (1.15 eV, 1.11 eV,
2.85 eV) at the R point, whereas the maximum direct gap for HF is at the M point (6.62 eV).
The minimum direct gap of LDA and GGA occurs along the $\Gamma$M direction (0.18 eV, 0.21 eV)
in contrast to B3LYP and HF, where the minimum direct gap is located along $\Gamma$R (1.59 eV,
4.07 eV). The band structure obtained by the plane wave method [11] is similar to the present
GGA band structure.

The total density of states for the optimized geometry is displayed in figure 3. The
LDA, GGA and B3LYP DOS is virtually identical to the one obtained with the parameters in
section 4.1, as the computed equilibrium geometry is close to the geometry used in section 4.1.
In the vicinity of the gap, there is a large contribution of the d states to the total DOS; see
figure 3 for details. This is due to the fact that there are several places in the band structure
where the bands at the top of the valence band are very flat and thus the DOS is large. The
B3LYP method yields to a greater gap and a smaller contribution at the top of the valence band,
because there are fewer places with a flat dispersion near the top of the valence band.

In contrast, the HF method gives a completely different picture of the DOS. The states near
the gap are p like, and the d states are pushed even further away from the top of the valence
band, with a relatively high peak beginning at around $-10$ eV.

The Mulliken charges are displayed in table 5. Si is slightly positively charged, which
agrees very well with recent x-ray fluorescence experiments where the charge was determined
to be $0.56\ |e|$ [33].

## 5. Low-energy magnetic states

We next turn to the question of whether the theoretical non-magnetic insulating state is indeed
stable with respect to magnetism. In addition, we are interested in whether DFT allows for
metastable magnetic states at low energies. In searching for magnetic self-consistent solutions,
we adopt the optimized lattice parameters derived in the previous section. Technically, we
start from a symmetry-broken state characterized by a finite polarization and iterate the spin
densities to self-consistency.

For LDA and GGA, the iteration procedure always converged to the non-magnetic
insulating state analysed in the preceding section. We therefore conclude that this state is
indeed the theoretical ground state for LDA and GGA.

For the HF approximation, however, a ferromagnetic solution is found whose energy is
lower by 12 eV per unit cell (containing four iron and four silicon atoms) compared to the

<table>
<caption>Table 6. Results of the spin polarized calculation with the corresponding optimized geometry of table 4. $E_{\text{FM-NM}}$ is the difference of energy between the spin polarized calculation and the non-magnetic solution, per unit cell (containing four iron and four silicon atoms). The corresponding magnetization $M$ of the magnetic state is per iron atom. Additionally the total charge of the iron and silicon atom and the charge of the Fe d basis functions are displayed.</caption>
<thead>
<tr>
<th>
</th>
<th>
$E_{\text{FM-NM}}$
</th>
<th>
$M_{\text{Fe}}$
</th>
<th>
$M_{\text{Si}}$
</th>
<th>
Fe total
</th>
<th>
Fe d
</th>
<th>
Si total
</th>
</tr>
<tr>
<th>
</th>
<th>
(eV)
</th>
<th>
($\mu_{\text{B}}$)
</th>
<th>
($\mu_{\text{B}}$)
</th>
<th>
(|$e$|)
</th>
<th>
(|$e$|)
</th>
<th>
(|$e$|)
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
B3LYP
</td>
<td>
+0.335
</td>
<td>
1.64
</td>
<td>
$-$0.23
</td>
<td>
26.38
</td>
<td>
7.13
</td>
<td>
13.62
</td>
</tr>
<tr>
<td>
HF
</td>
<td>
$-$12.020
</td>
<td>
3.82
</td>
<td>
$-$0.23
</td>
<td>
25.95
</td>
<td>
6.07
</td>
<td>
14.05
</td>
</tr>
</tbody>
</table>

non-magnetic solution. The characteristic properties are summarized in table 6. The presence of a magnetic ground state within HF seems plausible considering the fact that the Hartree–Fock method leads for the insulating system to a stronger localization and thus larger Coulomb repulsion, when compared with the LDA approach. Thus, a magnetic solution can become favourable, to reduce the Coulomb repulsion by occupying the d orbitals in a different way for up and down spin, in analogy to Hund’s rules. In addition the larger lattice constant implies a larger Fe–Fe separation, i.e. approaching the atomic limit, and thus with a stronger tendency to magnetism. Accounting for Hund’s rule coupling among the localized Fe d electrons leads to a local moment of $4\ \mu_{\text{B}}$ at the Fe site. The energy gain as compared to the non-magnetic state is consistent with the energy gain due to Hund’s rule coupling.

For B3LYP, a low-energy magnetic solution is found whose energy exceeds the one of the non-magnetic state by 0.3 eV. Similarly to the discussion for the HF solution in the previous paragraph, also B3LYP leads to more localized states (though not as localized as the HF states) and thus magnetic states become more favourable, compared to LDA. The magnetic moment amounts to $1.6\ \mu_{\text{B}}$ per Fe atom. It is interesting to note that the density of states in the minority spin channel vanishes slightly above the Fermi level. With electron doping, this solution might thus become half-metallic, i.e. conducting for only one type of spin, which is indeed observed for ${\text{Fe}}_{1 - x}{\text{Co}}_{x}\text{Si}$ [34]. We would like to emphasize that a solution of this type is not necessarily the B3LYP ground state with electron doping. The existence of such a solution is, however, very interesting.

The magnetic solutions obtained within the HF and B3LYP level are metallic in the sense that the bands continuously cross the Fermi energy. The position of the Fermi energy is defined as zero in figure 4, and the bands and the density of states are given with respect to the Fermi energy. Fock exchange leads to a logarithmic singularity at the Fermi energy, which, in turn, implies a divergent derivative ${\nabla}_{\vec{k}}\epsilon(k)$. The latter results in a vanishing density of states at the Fermi energy, for the homogeneous electron gas [35] and for metallic systems in general [36]. The vanishing density of states is however very difficult to be reproduced numerically, due to the difficulty of summing the exchange [37–39] and due to the large number of $k$-points required [40]. This explains why in figure 4, the DOS does not vanish at the Fermi level.

### 6. Conclusion

We have studied the structural, electronic, and magnetic properties of FeSi by first-principles all-electron DFT calculations using a local basis of Gaussian type orbitals. The LDA and GGA results are in good agreement with previously published theoretical data. These findings convincingly demonstrate the reliability of the computational procedure for electronic structure calculations and structure determination in the class of systems under consideration.

![](./images/811773866383769601_4.jpg)

Figure 4. Total density of states and band structure of $\alpha$ and $\beta$ electrons of the magnetic state obtained by using the B3LYP functional and the Hartree-Fock method. The calculations were performed with the optimized geometry of table 4. The Fermi energy is positioned at 0 eV.

Accounting for non-local exchange contributions significantly increases the indirect gap which separates the valence and conduction bands in the non-magnetic low-energy state. In general, the non-local exchange drives the system towards magnetism. This is clearly evident from HF calculations, which favour a magnetic metallic ground state. For the hybrid functional B3LYP, the latter state is found to be metastable. A detailed investigation of the low-temperature phase diagram and its implications is currently in progress.

### References

[1] Schlesinger Z, Fisk Z, Zhang H-T, Maple M B, DiTusa J F and Aeppli G 1993 *Phys. Rev. Lett.* **71** 1748
[2] Fäth M, Aarts J, Menovsky A A, Nieuwenhuys G J and Mydosh J A 1998 *Phys. Rev.* B **58** 15483
[3] Ishizaka K, Kiss T, Shimojima T, Yokoya T, Togashi T, Watanabe S, Zhang C Q, Chen C T, Onose Y, Tokura Y and Shin S 2005 *Phys. Rev.* B **72** 233202
[4] Jaccarino V, Wertheim G K, Wernick J H, Walker L R and Arajs S 1967 *Phys. Rev.* B **160** 476
[5] Mason T E, Aeppli G, Ramirez A P, Clausen K N, Broholm C, Stücheli N, Bucher E and Palstra T T M 1992 *Phys. Rev. Lett.* **69** 490
[6] Mandrus D, Sarrao J L, Migliori A, Thompson J D and Fisk Z 1995 *Phys. Rev.* B **51** 4763
[7] Takahashi Y and Moriya T 1979 *J. Phys. Soc. Japan* **46** 1451
[8] Mattheiss L F and Hamann D R 1993 *Phys. Rev.* B **47** 13114
[9] Fu C, Krijn M P C M and Doniach S 1994 *Phys. Rev.* B **49** 2219
[10] Jarlborg T 1999 *Phys. Rev.* B **59** 15002
[11] Moroni E G, Wolf W, Hafner J and Podloucky R 1999 *Phys. Rev.* B **51** 12860
[12] Al-Sharif A I, Abu-Jafar M and Qteish A 2001 *J. Phys.: Condens. Matter* **13** 2807

[13] Anisimov V I, Ezhof S Yu, Elfimov I S, Solovyev I V and Rice T M 1996 *Phys. Rev. Lett.* **76** 1735

[14] Corà F, Alfredsson M, Mallia G, Middlemiss D S, Mackrodt W C, Dovesi R and Orlando R 2004 *Principles and Applications of Density Functional Theory in Inorganic Chemistry II* vol 113 (Berlin: Springer) p 171

[15] Bredow T and Gerson A R 2000 *Phys. Rev. B* **61** 5194

[16] Muscat J, Wander A and Harrison N M 2001 *Chem. Phys. Lett.* **342** 397

[17] Kudin K N, Scuseria G E and Martin R L 2002 *Phys. Rev. Lett.* **89** 266402

[18] Becke A D 1993 *J. Chem. Phys.* **98** 5648

[19] Stephens P J, Devlin F J, Chabalowski C F and Frisch M J 1994 *J. Phys. Chem.* **98** 11623

[20] Raghavachari K 2000 *Theor. Chem. Acc.* **103** 361

[21] Villars P and Calvert L D 1985 *Pearson's Handbook of Crystallographic Data for Intermetallic Phases* (Metals Park, OH: ASM International)

[22] Perdew J P and Zunger A 1981 *Phys. Rev. B* **23** 5048

[23] Perdew J P, Chevary J A, Vosko S H, Jackson K A, Pederson M R, Singh D J and Fiolhais C 1992 *Phys. Rev. B* **46** 6671

[24] Saunders V R, Dovesi R, Roetti C, Orlando R, Zicovich-Wilson C M, Harrison N M, Doll K, Civalleri B, Bush I J, D'Arco Ph and Llunell M 2003 *Crystal2003 User's Manual* (Torino: University of Torino)

[25] Valerio G, Catti M, Dovesi R and Orlando R 1995 *Phys. Rev. B* **52** 2422

[26] D'Arco Ph *et al* 1993 *Phys. Chem. Minerals* **20** 407

[27] Doll K, Saunders V R and Harrison N M 2001 *Int. J. Quantum Chem.* **82** 1

[28] Doll K 2001 *Comput. Phys. Commun.* **137** 74

[29] Civalleri B, D'Arco Ph, Orlando R, Saunders V R and Dovesi R 2000 *Chem. Phys. Lett.* **348** 131

[30] Lin J-F, Campbell A J, Heinz D L and Shen G 2003 *J. Geophys. Res.* **108** ECV 11

[31] Knittle E and Williams Q 1995 *Geophys. Res. Lett.* **445** 22

[32] Godby R, Schlüter M and Sham L J 1986 *Phys. Rev. Lett.* **56** 2415

[33] Liu Z, Sugata S, Yuge K, Nagasono M, Tanaka K and Kawai J 2004 *Phys. Rev. B* **69** 035106

[34] Menzel D, Zur D and Schoenes J 2004 *J. Magn. Magn. Mater.* **130** 272

[35] Ashcroft N W and Mermin N D 1976 *Solid State Physics* (Philadelphia, PA: Saunders)

[36] Monkhorst H J 1979 *Phys. Rev. B* **20** 1504

[37] March N, Young W and Sampanthar S 1967 *The Many Body Problem in Quantum Mechanics* (Cambridge: Cambridge University Press)

[38] Goedecker S 1999 *Rev. Mod. Phys.* **71** 1085

[39] Heyd J, Scuseria G E and Ernzerhof M 2003 *J. Chem. Phys.* **118** 8207

[40] Fry J L, Brener N E and Bruyere R K 1977 *Phys. Rev. B* **16** 5225