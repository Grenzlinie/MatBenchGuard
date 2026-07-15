# Divacancies in diamond: a stepwise formation mechanism
Brad Slepetz and Miklos Kertesz*

Diffusion of monovacancies in diamond creates various trapped multivacancy clusters. The simplest diffusion process leads to a divacancy, $V_2$. The formation of $V_2$ is a critical step in the formation of larger vacancy clusters. We explored the relaxed potential energy surfaces in the formation of $V_2$ by ab initio density functional theory (DFT) obtaining structures, relative energies, diffusion barriers and reaction paths. The constricted environment of a diamond lattice leads to unexpected chemical bonding situations with unusually elongated carbon-carbon bonds that have multicenter character. Divacancies separated by one carbon are not stable. Even though the divacancy is the most stable final product, a novel isolated divacancy with two vacant sites separated by two bonded carbons [V-C=C-V] can be transformed into a divacancy only via a very large (>4.3 eV) barrier and therefore it should be a defect observable in irradiated diamonds. Trapping of a vacancy by another by forming a stable divacancy trap affects the development of NV-defects in nitrogen implanted diamonds that are subject to active current interest in a wide range of applications.

## 1. Introduction
Diamond-like materials including nanodiamonds contain a large variety of defects that are difficult to identify at the atomic level. $^1$ This work has a three-fold motivation. (1) There is currently high interest in the photoluminescence of NV-defects (nitrogen atoms adjacent to a vacancy) in diamonds that arise from the creation of vacancies and their recombination with implanted nitrogens. $^2$ Applications from electronics to quantum informatics to biomarkers have received wide interest. $^3$ (2) The diffusion of vacancies and their trapping is of basic interest. What is the atomistic mechanism for a vacancy to change place or to get trapped by another to form a stable vacancy aggregate, cluster? (3) Under the constrained conditions of a covalent lattice, carbon atoms behave in unique, sometimes unexpected ways. The internal "surface" of a vacancy or a vacancy cluster lacks the sufficient number of valence electrons to form only electron pair bonds. The presence of the resulting "dangling bonds," unpaired electrons, is the driving force for strong reorganization, the formation of unusually long bonds with multicenter characteristics. $^4$ In this work we apply sate of the art density functional theory combined with the nudged elastic band (NEB) determination of reaction paths$^5$ and obtain realistic estimates of the energetics of vacancy diffusion and divacancy formation in diamond.

Baker has emphasized the importance to consider the vacancy cluster formation as resulting from precursors that have been created by accumulation of migrating vacancies such that a "family tree of ancestors" with sufficient stabilities and lifetimes can be identified. From this genealogical approach it follows that the steps to accumulate any particular cluster must involve precursors with the same configuration of vacancies, less one or two adjacent vacancies. The simplest of such genealogies is the formation of a bound pair of two monovacancies, which is the subject of this work. It is surprising that the literature lacks discussion of the most elementary of these processes, the
$$\mathrm{V_1 + V_1 \rightarrow bound\ V_2} \tag{1}$$
process, where $\mathrm{V_1}$ is a monovacancy and $\mathrm{V_2}$ refers to a divacancy.

Vacancy diffusion is considered as the dominant self-diffusion mechanism in diamond. $^6$ Butorac and Mainwood$^7$ revealed key parameters by first principles DFT methods of the migration of the complexes of N, H with $\mathrm{V_1}$ (V in their notation) in diamond. In this work we applied a similar methodology to the following problem: what are the immediate preceding steps represented by eqn (1)? Are there any traps that are sufficiently stable to prevent the formation of a divacancy from two diffusing monovacancies?

The nearest neighbour divacancy $\mathrm{V_2}$ in diamond was confirmed by Twitchen *et al.* to be responsible for the "R4/W6" EPR active center. In their analysis they considered, but ruled out a possible divacancy arrangement involving a "[V-C-C-V]" defect that might contain a double bond between isolated carbons and possess $C_{2\mathrm{h}}$ symmetry. $^{8,9}$ This notation indicates that the two vacant atoms can be connected *via* a shortest path that includes two singly bonded carbons. Here, we discuss this and

---
Chemistry Department, Georgetown University, 37th and O Streets, NW, Washington, DC, 20057-1227, USA. E-mail: Kertesz@georgetown.edu

![](./images/813182218787618817_1.jpg)

Fig. 1 Structural models for the migration of monovacancies in diamond.
On the top series, color coded vacancy atoms (red) separated by 3, 2 and
1 atoms, which are shown in the diagrams underneath with respective
symbols. The first number in the symbol indicates the number of atoms
separating the two monovacancies.

other hypothetical defects that must form before coalescing to
the $V_{2}$. As two isolated monovacancies in a cubic diamond lattice
migrate towards each other, the two monovacancies must approach
each other in one of the three topologically different configurations
separated by at least 3 atoms—shown in the left column of
Fig. 1—before they can merge to form the more stable $V_{2}$, shown at
the right end, passing through or possibly getting stuck in a series
of configurations separated by at least 2 atoms (2O and 2C) and a
configuration separated by one atom (1I). These are indicated in
Fig. 1. Our goal here is to explore these pathways using geometry
optimizations based on density functional theory (DFT).

Due to the structural isomerisms illustrated in Fig. 1, various
structures need to be compared and their mutual transforma-
tions explored energetically. For the 3 series (the vacancy posi-
tions are separated by at least 3 atoms in the lattice) the notations
of E, A, and C refer to equatorial, axial and chain configurations,
respectively. For the 2 series (the vacancy positions are separated
by at least 2 atoms in the lattice) C and O refer to chain and
opposite, respectively. For the divacancy separated by one atom
there is only one isomer, (I for isolated, commonly referred to as
the 'saddle divacancy') which in our analysis turns out not to be a
local minimum.

Some of the barriers are so high that transformations among
them are not viable at any reasonable temperature. The sequence
of arrows illustrates the general direction of the formation of a $V_{2}$,
which is generally an energetically favorable process due to the
reduction of the number of dangling bonds from 8 (for isolated
monovacancies, $2V_{1}$) to 6 (for a divacancy, $V_{2}$). However, just by
simple bond counting one might assume that the structure 2C
might become stabilized due to the possibility of relaxation of the
central single $\sigma$-bond into a double bond as indicated by 2C
in Fig. 1 when the dangling bonds are reoriented. Indeed, the
presented calculations point to 2C being a stable trap, although
not as stable as $V_{2}$.

## 2. Methods
The augmented plane wave electronic structure code PWscf—
part of the Quantum ESPRESSO$^{10}$ package—was used to per-
form self-consistent field (SCF) total energy calculations on the
seven species shown in Fig. 1 in both spin-polarized (spin-
unrestricted) and closed shell formalism. We also note that the
approach adopted here is based on separate calculations using
the spin-polarized vs. non-polarized formalism. Ideally, computa-
tions would be performed for pure spin states. The spin-polarized
calculations represent a mixture of singlet and non-singlet
states. $^{11}$ However, where the two differ significantly, the energy
lowering obtained by the spin-polarized calculations indicates
a large diradicaloid component and should provide a better
approximation to the true barrier than the unpolarized compu-
tations. All calculations on vacancy species and potential sur-
faces were made with the exchange correlation functional of
Perdew et al. (PBE).$^{12}$ For all calculations, the kinetic energy
cutoff of the plane waves was 48.0 Ry with a charge density cutoff
of 348 Ry. Electron SCF convergency was set at $10^{-8}$ within the
gamma point, and Fermi-Dirac electron smearing of $10^{-3}$ Ry
was used. A Vanderbilt ultra-soft pseudopotential, parameterized
for carbon systems by Meyer$^{13}$ was used to treat the carbon core
electrons. For the full geometric optimizations, convergency was
satisfied when the total energy change between successive steps
was less than $10^{-7}E_{\text{H}}$ and the components of all the forces on
the atoms were reduced below $51\ \text{meV}\ \mathring{\text{A}}^{-1}$.

Formation energies for defects were calculated as follows
$$
E_{\text{f}}^{n}=E_{\text{vac}}^{n}-\frac{N-n}{N}E_{\text{cryst}}^{N} \tag{2}
$$
where $E_{\text{f}}$ is the formation energy, $N$ is the number of atoms of
the defect-free unit cell, $n$ is the number of vacancies, $E_{\text{vac}}^{N}$ is the
calculated energy of a cluster containing $N - n$ atoms, $E_{\text{vac}}^{n}$ is
the energy of a defect-cluster. A cubic supercell containing
$N = 216$ atoms within the $\Gamma$-point approximation was used.
These approximations allowed extensive searches on the potential
energy surface (PES).

The nudged elastic band (NEB) with climbing image method$^{5}$
was used to calculate the energies of structures along the pathway
that connects relevant species. In NEB, a series of "images" or
structures along a potential energy surface connecting equili-
brium structures are optimized such that the forces on the atoms
and along the "band" that connects images, as modeled by a
spring, are minimized. The "climbing image" allows the struc-
ture with highest energy to optimize to a saddle point. We used at
least five, and sometimes, 11 intermediate images finding no
qualitative difference between the two. We used a variable elastic
spring constant $k = 0.62$ and the process was considered con-
verged when the norm of the force orthogonal to the path was
less than $0.05\ \text{eV}\ \mathring{\text{A}}^{-1}$ for all images. Spin-polarization was not
used in NEB calculations; instead single point spin-polarized
energies are calculated on transition structure (TS) and this value
is used in reporting barrier heights. Initial transition structures
were found by repeated conjugate gradient minimizations from
the well-defined reactant and product structures as followed by
quadratic synchronous transit (QST) maximization.$^{14}$ The TS
search process found local maxima for all structures with the
exception of the 1I structure (see below).

For the NEB reaction pathway calculations we used $S = 0$
states only. From this PES, we then did structural optimizations

on the minima with a variety of spin states and single point energies on the maximum (TS) with a variety of spin states. From this, we report a new estimate of the reaction barrier by taking the difference of the spin-polarized TS energy and the energy of the reactant that is lowest of all competing spin states.

## 3. Validation

We report on three cases as a way to validate our approach. First, for $V_2$ we obtain a ground state triplet $^4(D_{3d})$ as did Coomer et al.$^{15}$ both being consistent with experiment.$^{8}$ We performed a reaction path search along the straight connecting line of the two $V_1$ locations along the [111] direction and obtained a barrier of 3.14 eV for the diffusion of $V_1$. This is in close agreement with the 3.3 eV barrier of Breuer and Briddon$^{16}$ along the same path although higher than the experimental barrier of $2.3 \pm 0.3$ eV.$^{17}$ The authors calculated a symmetry-breaking path barrier of 2.8 eV, which we were unable to duplicate in NEB. For $V_1$, we use a small smearing in order to maintain the $T_d$ symmetry. We obtained a relaxed structure with an increase in the nearest neighbor distance by $0.196$ Å, to be compared with the earlier LDA value of $0.2$ Å.$^{18}$ The formation energy for $V_1$ was 6.07 eV, to be compared with the LDA results of 7.2 eV from Bernholc et al.$^6$

## 4. Results

### Equilibrium vacancy structures

What follows are brief descriptions of the eight species studied in this work: the monovacancy and seven divacancies. Both spin-restricted and spin-polarized calculations were performed and we find $S=1$ states be the lowest in energy for all species except for 2O and $V_1$, for which unrestricted $S=0$ states were found to be lower, highlighting the importance of spin-polarization in describing these equilibrium structures. The geometries of the defects are not generally dependent on the spin state as the rigid framework of the diamond lattice prevents large changes in atomic relaxation, but subtle changes are observed which sometimes makes convergency difficult. Table 1 summarizes the formation energies, spin states, and geometries of the vacancies of Fig. 1 and are listed in the ascending order of their spin-restricted formation energies.

<table>
<caption>Table 1 Formation energies, spin states, and geometries of the presented vacancy clusters</caption>
<thead>
<tr>
<th>Species</th>
<th>$E_f$$^a$</th>
<th>Spin</th>
<th>Mag$^b$</th>
<th>Sym</th>
<th>R1$^c$</th>
<th>R2</th>
<th>R3</th>
<th>R4</th>
<th>R5</th>
<th>R6</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">$V_2$</td>
<td>8.85</td>
<td>0</td>
<td>0.0</td>
<td>$D_{3d}$</td>
<td>2.66</td>
<td>2.66</td>
<td>3.07</td>
<td>3.07</td>
<td></td>
<td></td>
</tr>
<tr>
<td>8.60</td>
<td>0</td>
<td>2.1</td>
<td>$C_{2h}$</td>
<td>2.65</td>
<td>2.67</td>
<td>3.07</td>
<td>3.06</td>
<td></td>
<td></td>
</tr>
<tr>
<td>8.49</td>
<td>1</td>
<td>2.3</td>
<td>$D_{3d}$</td>
<td>2.65</td>
<td>2.65</td>
<td>3.07</td>
<td>3.07</td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="4">2C</td>
<td>10.86</td>
<td>0</td>
<td>0.0</td>
<td>$C_{2h}$</td>
<td>1.35</td>
<td>2.69</td>
<td>2.70</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>10.49</td>
<td>1</td>
<td>2.4</td>
<td></td>
<td>1.35</td>
<td>2.71</td>
<td>2.68</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>10.37</td>
<td>0</td>
<td>3.9</td>
<td></td>
<td>1.35</td>
<td>2.77</td>
<td>2.66</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>10.34</td>
<td>1</td>
<td>4.0</td>
<td></td>
<td>1.35</td>
<td>2.77</td>
<td>2.67</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="4">2O</td>
<td>11.81</td>
<td>0</td>
<td>0.0</td>
<td>$C_{2h}$</td>
<td>1.39</td>
<td>2.85</td>
<td>2.77</td>
<td>2.70</td>
<td>2.75</td>
<td></td>
</tr>
<tr>
<td>11.76</td>
<td>0</td>
<td>2.0</td>
<td></td>
<td>1.39</td>
<td>2.84</td>
<td>2.77</td>
<td>2.65</td>
<td>2.75</td>
<td></td>
</tr>
<tr>
<td>11.59</td>
<td>1</td>
<td>2.4</td>
<td></td>
<td>1.40</td>
<td>2.80</td>
<td>2.78</td>
<td>2.70</td>
<td>2.72</td>
<td></td>
</tr>
<tr>
<td>11.55</td>
<td>0</td>
<td>3.3</td>
<td></td>
<td>1.40</td>
<td>2.80</td>
<td>2.77</td>
<td>2.68</td>
<td>2.72</td>
<td></td>
</tr>
<tr>
<td rowspan="2">3C</td>
<td>12.07</td>
<td>0</td>
<td>0.0</td>
<td>$C_{2v}$</td>
<td>1.48</td>
<td>3.08</td>
<td>2.69</td>
<td>2.66</td>
<td>3.01</td>
<td>2.98</td>
</tr>
<tr>
<td>11.50</td>
<td>1</td>
<td>3.8</td>
<td></td>
<td>1.48</td>
<td>3.08</td>
<td>2.65</td>
<td>2.74</td>
<td>3.00</td>
<td>3.00</td>
</tr>
<tr>
<td rowspan="2">1I</td>
<td>12.47</td>
<td>0</td>
<td>0.0</td>
<td>$C_{2v}$</td>
<td>2.57</td>
<td>2.70</td>
<td>2.65</td>
<td>2.65</td>
<td>2.51</td>
<td></td>
</tr>
<tr>
<td>12.12</td>
<td>1</td>
<td>2.5</td>
<td></td>
<td>2.59</td>
<td>2.69</td>
<td>2.62</td>
<td>2.72</td>
<td>2.52</td>
<td></td>
</tr>
<tr>
<td rowspan="4">3E</td>
<td>13.20</td>
<td>0</td>
<td>0.0</td>
<td>$C_s$</td>
<td>1.50</td>
<td>1.53</td>
<td>2.49</td>
<td>2.73</td>
<td></td>
<td></td>
</tr>
<tr>
<td>12.42</td>
<td>1</td>
<td>4.4</td>
<td></td>
<td>1.49</td>
<td>1.52</td>
<td>2.50</td>
<td>2.77</td>
<td></td>
<td></td>
</tr>
<tr>
<td>12.35</td>
<td>2</td>
<td>4.6</td>
<td></td>
<td>1.50</td>
<td>1.51</td>
<td>2.51</td>
<td>2.72</td>
<td></td>
<td></td>
</tr>
<tr>
<td>12.23</td>
<td>1</td>
<td>5.5</td>
<td></td>
<td>1.51</td>
<td>1.51</td>
<td>2.53</td>
<td>2.76</td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="2">3A</td>
<td>13.46</td>
<td>0</td>
<td>0.0</td>
<td>$C_s$</td>
<td>1.51</td>
<td>1.51</td>
<td>2.49</td>
<td>2.69</td>
<td></td>
<td></td>
</tr>
<tr>
<td>12.29</td>
<td>1</td>
<td>5.5</td>
<td></td>
<td>1.50</td>
<td>1.49</td>
<td>2.49</td>
<td>2.63</td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="3">$V_1$$^d$</td>
<td>13.10</td>
<td>0</td>
<td>0.0</td>
<td>$D_{2d}$</td>
<td>2.72</td>
<td>2.59</td>
<td>2.72</td>
<td>2.72</td>
<td>2.72</td>
<td>2.59</td>
</tr>
<tr>
<td>12.34</td>
<td>1</td>
<td>2.9</td>
<td>$C_{2v}$</td>
<td>2.76</td>
<td>2.76</td>
<td>2.76</td>
<td>2.68</td>
<td>2.68</td>
<td>2.68</td>
</tr>
<tr>
<td>12.13</td>
<td>0</td>
<td>3.0</td>
<td>$T_d$</td>
<td>2.73</td>
<td>2.73</td>
<td>2.73</td>
<td>2.73</td>
<td>2.73</td>
<td>2.73</td>
</tr>
</tbody>
</table>

$^a$ Energies are in eV. $^b$ Absolute magnetization; Bohr magnetons per unit cell. $^c$ Distances are in Å; see Fig. 3-8 for a description of the parameters. $^d$ $V_1$ formation energies are multiplied by 2 for comparison.

Monovacancy, $V_1$. $V_1$ in diamond (Fig. 2) has been studied extensively both experimentally and theoretically. Removal of a single carbon from the ideal diamond lattice leaves four nearest neighbors separated by $2.52$ Å with $T_d$ symmetry and outward relaxation maintains this symmetry. The defect is identified$^{18}$ with the GR1 absorption line at 1.673 eV arising from electronic transition from the ground $^1$E state to a near lying $^3$T excited state. Correctly modeling $V_1$ normally requires configuration interaction of competing multiplets, otherwise Jahn-Teller distortion is observed lowering the symmetry to $D_{2d}$ or $C_{2v}$ symmetry,$^{19}$ as is the case in our spin-restricted calculation (Table 1). We obtain a formation energy of 6.55 eV, a value that is between the representative LDA calculations$^6$ and a restricted open-shell Hartree-Fock method.$^{21}$ With spin-polarization, we find a $T_d$ structure with a formation energy of 6.06 eV and a near-lying triplet state with the $C_{2v}$ point group. Above 1100 K, $V_1$ is mobile and appreciably forms divacancies unless the diamond sample is rich in nitrogen which traps migrating vacancies.$^{8}$ Anderson et al. obtained a stabilization energy of

![](./images/813182218787618817_2.jpg)

Fig. 2 Nearest neighbors (yellow) to the monovacancy $V_1$. The vacancy removed is shown in red.

3.45 eV²⁰ using their semi-empirical quantum chemical method for the V₁ + V₁ → V₂ process, which compares well with our calculated value of 3.55 eV.

Divacancy, V₂. The V₂ divacancy (Fig. 3) is created from removing two adjacent carbons in the diamond lattice leaving six nearest neighbors with D₃d symmetry. This leaves six states in the gap with the one electron description $a_{1g}^{2}a_{1u}^{2}e_{u}^{2}$ leaving the possibility of a Jahn-Teller distortion.¹⁷ ESR experiments confirm the S = 1 ground state but with temperature dependent geometry; C₂h below 30 K and undistorted D₃d above this mark.⁸ We calculate the restricted formation energy to be 8.85 eV which lowers by 0.36 eV when spin-polarization is introduced. Our calculation reveals D₃d symmetry and S = 1 spin with a C₂h unrestricted singlet state 0.11 eV higher.

Divacancy defect, 2C. The 2C defect (Fig. 4) is produced by removing a pair of carbon atoms separated by two along the [110] chain direction. Relaxation of the isolated pair along [110] produces a pyramidalized (~24°) sp² bond of 1.35 Å length which has a calculated characteristic C=C stretching frequency close to 1610 cm⁻¹.²¹ This defect was considered by Twitchen et al. as it was ruled out as a possible explanation for the R4/W6 ESR center in irradiated diamond. We previously described²³ this defect modeling it with a hydrogen-terminated cluster and a 216 atom supercell with BLYP density functional and a numerical atomic orbital basis set. In contrast to that study, here we find an S = 1 ground state with a low-lying S = 0 diradical state; the results were reversed in our previous study. In both spin states, the spin density is located primarily on the six atoms that make up the two triangles that lie above and below the sp²-bonded carbons. Migration of 2C to V₂ is high relative to 2O migration (see below) and thus may be a stable trap for migrating vacancies and observable with ESR.

![](./images/813182218787618817_3.jpg)

Fig. 3 The six nearest neighbors (yellow) to the divacancy (red).

![](./images/813182218787618817_4.jpg)

Fig. 4 Nearest neighbors (yellow) to the 2C divacancy (red).

Divacancy defect, 2O. Removing a pair of carbons situated at the opposite ends of a C₆ chair in the diamond lattice produces the 2O defect (Fig. 5). Although removal of these atoms leaves behind two pairs of isolated nearest neighbors, as in 2C, these atoms are not as readily free to sp²-hybridize because structural motif of these atoms is not situated along [110] and their bonded neighbors are twisted relative to each other, denying potential overlap. These carbons shrink to a distance of about 1.40 Å. The void space can be viewed as two closely interacting monovacancies and concerted migration of one quasi-sp² pair towards the void space produces the adjacent V₂. The simplicity of this path combined with the high cost of breaking the sp² bond in 2C make this the more favorable precursor to V₂ production. This is the only divacancy for which we find an S = 0 (unrestricted) ground state.

Divacancy defect, 3C. The 3C (C for chain) defect (Fig. 6) is produced by removing a pair of atoms along [110] separated by

![](./images/813182218787618817_5.jpg)

Fig. 5 Nearest neighbors (yellow) to the 2O divacancy (red).

![](./images/813182218787618817_6.jpg)

Fig. 6 The nearest neighbors (yellow) to the 3C divacancy (red).

three carbons. The two carbons along [110] that neighbor the vacancies relax towards their common neighbor shrinking their bond length to 1.48 Å. Concerted migration of these two atoms towards the void would produce the $V_2$ but we find this costly relative to the migration of a single atom towards one vacancy producing the [110] 2C divacancy.

Divacancy defect, 1I. Early work reported by Coulson and Larkins⁴ considered the 1I (Fig. 7) competitive with $V_2$. We achieve convergency on this structure for both spin-restricted and spin-polarized formalism but its formation energy is about 3.6 eV higher than $V_2$. NEB calculations for the $1I \rightarrow V_2$ process shows no barrier and we consider the 1I to be a transition structure for $V_2$ migration. This not only rules out one of the seemingly stable divacancy structures, but also limits the pathways of viable interconversion processes as we discuss below.

Divacancy defects, 3E and 3A. Starting with a $C_6$ chair, removing a carbon from the chair followed by the removal of a carbon separated by three atoms produces either the 3E or 3A defect (Fig. 8) depending on whether the axial or equatorial carbon is removed. 3E is shown (Table 1) to be more stable but the difference is small and both are on accord with two isolated monovacancies. It is interesting then to note that even at this close of a distance the vacancies do not interact in an appreciable way. Migration of the point carbon on the $C_6$ chair towards its respective equatorial or axial vacancy produces the 2O defect. Conversion of 3E or 3A to 3C is complicated due to structural constraints and therefore energetically unfavorable. One expects high barriers between structures in the three series due to the large atomic rearrangement that would be necessary for these transformations. The calculated barriers among 3A, 3E and 3C range from 5.0 eV to 7.5 eV, and are too high to consider these processes as viable. Therefore, once one of the three 3A, 3E or 3C structures has been formed, they should either dissociate or form either 2C or 2O.

![](./images/813182218787618817_7.jpg)

Fig. 7 Nearest neighbors (yellow) to the isolated divacancy 1I (red).

![](./images/813182218787618817_8.jpg)

Fig. 8 3E (left) and 3A (right) defects showing the nearest neighbors (yellow) surrounding the vacancies (red).

### Pathways
The results of our NEB calculations for transition structures and the related energetics are presented in Table 2. The reaction energies are according to the direction of the written step, thus the negative values indicate all processes are exothermic. All NEB calculations were performed with RBPE and these results are shown on the first line for each step. The second line shows the estimated values taking spin-polarization into account. Thus, the reaction energy found in the second line is the difference between the reactive species' lowest formation energies, regardless of the spin state and the barriers are estimated by taking the difference between the spin-polarized single point SCF energy of the (spin-restricted) transition structure and the calculated energy of the ground state of the reactant (or product) as defined by the arrows in the subsequent discussion.

The formation of $V_2$ from 2O is a two atom migration where the bond of one of the isolated pairs breaks, with the atoms moving towards the 2O vacancy sites, leaving the void of $V_2$. The barrier is comparable to the $V_1$ diffusion barrier and proves the only viable path for the formation of $V_2$. A one atom migration

Table 2 Reaction energies $(E_R)$ and barriers for the elementary steps computed in this work. Energies are in eV. The first line in each step refers the spin-restricted calculations. The second line shows the values using spin-polarization
| Step | $E_R$ | Barrier |
|------|-------|---------|
| 3E → 2O | $-1.39$<br>$-0.68$ | $1.92$<br>$2.52$ |
| 3A → 2O | $-1.66$<br>$-0.74$ | $1.61$<br>$2.33$ |
| 3C → 2C | $-1.21$<br>$-1.16$ | $1.72$<br>$1.64$ |
| 2C → V2 | $-2.01$<br>$-1.85$ | $4.40$<br>$4.33$ |
| 2O → V2 | $-2.96$<br>$-3.06$ | $2.26$<br>$2.46$ |

![](./images/813182218787618817_9.jpg)

Fig. 9 Energy profiles of the $2O \rightarrow V_2$ (black) and $2C \rightarrow V_2$ (dashed red) processes.

was considered where one carbon on one of the two isolated pairs moves towards a vacancy at the opposite end, however, the long distance traveled along this path induces a high barrier. Fig. 9 shows the integrated energy profile of $V_2$ production from 2O and 2C. One immediately notices the reduced barrier starting from 2O despite the extra stability the 2C possesses.

Moving backwards in the genealogy of Fig. 1, the integrated potential energy scan for the production of 2O from 3E and 3A is shown in Fig. 10. Both have similar and modest (spin-restricted) barriers of 1.92 eV ($3A \rightarrow 2O$) and 1.61 eV ($3E \rightarrow 2O$). This establishes a path from two free $V_1$ vacancies to $V_2$, first via 3A or 3E and then via 2O.

On the other hand, 3C (which is twice as likely to be formed on statistical grounds assuming all else being equivalent) can only be transformed into a trap, 2C (barrier = 1.72 eV), from which the barrier as discussed is too high to generate $V_2$.

Some of the transition structures show interesting relaxations, such as in the case of $2O \rightarrow V_2$ where the transition structure (TS) contains a shortening of the quasi-sp$^2$ bonded pair which again elongates in the product. This transient shortening leads to a stabilization of the TS and lowers the barrier.

![](./images/813182218787618817_10.jpg)

Fig. 10 Energy profile of the $3E \rightarrow V_2$ (black) and $3A \rightarrow 2O$ (dashed red) processes.

![](./images/813182218787618817_11.jpg)

Fig. 11 Calculated spin-polarized energy barriers for the processes discussed in this paper. $V_2$ is more stable than 2C [V-C=C-V] by about 1.85 eV, but given the smaller barriers leading to 2C, it may be more prevalent than $V_2$. (Position of symbols does not represent relative energetics.)

Fig. 11 summarizes the spin-polarized barriers for the processes discussed above. It is surprising that the process leading to the most stable end product, $V_2$, encounters barriers that are significantly higher than the barrier to the novel 2C structure with the C=C bond. Note that assuming a random initial structure, the 3C is twice as likely to occur compared to the 3A and 3E. Therefore, we conclude that the product 2C should be observable in addition to the more stable $V_2$ divacancy.

## 5. Conclusions

We have shown with DFT computations that the capture of one monovacancy, $V_1$, by another can lead to a stable divacancy $V_2$ and alternatively to a more complex novel 2C isolated divacancy [V-C=C-V] structure, which would trap the two monovacancies in a stable state. Computational modeling indicates that the mechanism of the formation of these bound vacancy clusters is likely to occur via the 2O intermediate, while the chain-like intermediate is stabilized by the formation of a double bond creating a stable divacancy trap. The computed series of barriers indicate that the novel 2C isolated divacancy [V-C=C-V] should be produced in the process of monovacancy diffusion in addition to the more stable divacancy, $V_2$. The new structure of the isolated divacancy shows that the eight dangling bonds of a divacancy can relax not only as the nearest neighbor adjacent divacancy, but in a manner creating an approximate double bond inside of diamond. While it may be desirable to avoid the formation of the stable divacancy $V_2$ or the stable novel 2C isolated divacancy [V-C=C-V], their presence should be considered in the development of important NV-defects. The novel 2C isolated divacancy [V-C=C-V] should be observable spectroscopically.

We also concluded that 1I (the divacancy separated by one carbon) is not a stable structure, similar to the case of silicon, where Hwang and Goddard have pointed$^{22}$ out the instability of such a structure toward $V_2$. Given the well-known differences$^{17,23}$ between Si and diamond; this similarity does not follow automatically.

## Acknowledgements

Research is supported by the U.S. Department of Energy, Office of Basic Energy Sciences, Division of Materials Sciences and Engineering under Award No. DE-FG02-07ER46472. Support from GridChem

is acknowledged for computer time. We thank the National Science Foundation for partial support of this research (grant number CHE-1006702). We are indebted to Prof. Yury Gogotsi and Dr Vadym Mochalin for useful discussions.

## References

1 J. M. Baker, *Diamond Relat. Mater.*, 2007, **16**, 216.

2 For a recent review on theory see: M. W. Doherty, N. B. Manson, P. Delaney, F. Jelezko, J. Wrachtrup and L. C. L. Hollenberg, *Phys. Rep.*, 2013, **528**, 1.

3 For a recent review on applications see: I. Aharonovich, S. Castelletto, D. A. Simpson, C.-H. Su, A. D. Greentree and S. Prawer, *Rep. Prog. Phys.*, 2011, **74**, 076501.

4 C. A. Coulson and F. P. Larkins, *J. Phys. Chem. Solids*, 1969, **30**, 1963.

5 G. Henkelman, B. P. Uberuaga and H. Jonsson, *J. Chem. Phys.*, 2000, **113**, 9901.

6 J. Bernholc, A. Antonelli, T. M. Del Sole, Y. Bar-Yam and S. T. Pantelides, *Phys. Rev. Lett.*, 1988, **61**, 2689.

7 B. Butorac and A. Mainwood, *Diamond Relat. Mater.*, 2008, **17**, 1225.

8 D. J. Twitchen, M. E. Newton, J. M. Baker, T. R. Anthony and W. F. Banholzer, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1999, **59**, 12900.

9 J. M. Baker, D. C. Hunt, M. E. Newton and D. J. Twitchen, *Radiat. Eff. Defects Solids*, 1999, **149**, 233.

10 Quantum ESPRESSO is a community project for high-quality quantum-simulation software, based on density-functional theory, and coordinated by P. Giannozzi. See http://www. quantum-espresso.org and http://www.pwscf.org.

11 See *e.g.* A. Szabo and N. S. Ostlund, *Modern Quantum Chemistry*, Dover, New York, 1996.

12 J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865.

13 See http://www.quantum-espresso.org/pseudo-search-results/?el_id=6&unp_id&fun_id&colum_k&origin_id.

14 T. A. Halgren and W. N. Lipscomb, *Chem. Phys. Lett.*, 1977, **49**, 225.

15 B. J. Coomer, A. Resende, J. P. Goss, R. Jones, S. Oberg and P. R. Briddon, *Physica B*, 1999, **273**, 520.

16 S. J. Breuer and P. R. Briddon, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1996, **51**, 6984.

17 G. Davies, S. C. Lawson, A. T. Collins, A. Mainwood and S. J. Sharp, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1992, **46**, 13517.

18 C. D. Clark, R. W. Ditchbum and H. B. Dyer, *Proc. R. Soc. A*, 1956, **234**, 363.

19 S. S. Moliver, *Phys. Solid State*, 2000, **42**, 655.

20 A. B. Anderson, E. J. Grantscharova and J. C. Angus, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1996, **54**, 14341.

21 D. Hyde-Volpe, B. Slepetz and M. Kertesz, *J. Phys. Chem. C*, 2010, **114**, 9563.

22 G. S. Hwang and W. A. Goddard III, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2002, **65**, 233205.

23 In carbons both $sp^2$/$sp^3$ hybridizations play an important role, as opposed to Si.