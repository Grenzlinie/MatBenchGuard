# Oxygen vacancy induced site-selective Mott transition in LaNiO₃

Xingyu Liao¹, Vijay Singh¹, and Hyowon Park¹,²

¹Department of Physics, University of Illinois at Chicago, Chicago, IL 60607, USA
²Materials Science Division, Argonne National Laboratory, Argonne, IL, 60439, USA
(Dated: February 18, 2021)

While defects such as oxygen vacancies in correlated materials can modify their electronic properties dramatically, understanding the microscopic origin of electronic correlations in materials with defects has been elusive. Lanthanum nickelate with oxygen vacancies, LaNiO₃₋ₓ, exhibits the metal-to-insulator transition as the oxygen vacancy level $x$ increases from the stoichiometric LaNiO₃. In particular, LaNiO₂.₅ exhibits a paramagnetic insulating phase, also stabilizing an antiferromagnetic state below $T_N \simeq 152$K. Here, we study the electronic structure and energetics of LaNiO₃₋ₓ using first-principles. We find that LaNiO₂.₅ exhibits a "site-selective" paramagnetic Mott insulating state at $T \simeq 290$K as obtained using density functional theory plus dynamical mean field theory (DFT+DMFT). The Ni octahedron site develops a Mott insulating state with strong correlations as the Ni $e_g$ orbital is half-filled while the Ni square-planar site with apical oxygen vacancies becomes a band insulator. Our oxygen vacancy results cannot be explained by the pure change of the Ni oxidation state alone within the rigid band shift approximation. Our DFT+DMFT density of states explains that the peak splitting of unoccupied states in LaNiO₃₋ₓ measured by the experimental X-ray absorption spectra originates from two nonequivalent Ni ions in the vacancy-ordered structure.

## I. INTRODUCTION

Rare-earth nickelates $R$NiO₃ ($R$ is the rare-earth ion) have attracted significant research interests due to their rich electronic properties. These include the metal-insulator transition, charge order, magnetism, multiferroicity, and the site-selective Mott transition [1–6]. Although the $R$ ion can be treated as electrically inert, the phase boundaries of the metal to insulator transition and the paramagnetic (PM) to anti-ferromagnetic (AFM) transition depend sensitively on the subtle structural tolerance factor controlled by the size of the $R$ ion [7]. This close interplay between the structural, electronic, and magnetic degrees of freedom puts the rare-earth nickelate into an intriguing correlated material.

Oxygen vacancy is one of the common defects in transition metal oxides and it can play a central role in oxide electronics [8]. It is also known that oxygen vacancies in LaNiO₃, one of the rare-earth nickelates, also change its electronic and magnetic properties significantly as they can modify electronic correlation effects. Although LaNiO₃ is the only metallic case among the known rare-earth nickelate series, Ni $d$ orbitals are still moderately correlated as indicated by experimental spectroscopic measurements [9–11]. Experimental measurements on the conductivity in LaNiO₃₋ₓ show that the increase of the vacancy level $x$ reduces the conductivity and the metal-to-insulator transition occurs as $x$ approaches to 0.5 [12, 13]. As the oxygen vacancy level $x$ increases further, LaNiO₂₊δ is found to be semiconducting or poorly conducting [14]. The complete absence of the apical oxygens leads to the infinite-layer structure of LaNiO₂ and the role of electronic correlations in LaNiO₂ has been drawing much attention recently as similar nickelates such as NdNiO₂ and PrNiO₂ exhibit superconductivity when they are hole-doped [15, 16]. Although LaNiO₂ is metallic, resistivity increases at low temperatures hinting possibly strong correlation effects.

In addition to transport properties, oxygen vacancies also have significant effects on magnetism. Although LaNiO₃ has been known to remain PM at all temperatures, there was a controversial experimental work showing some evidence of AFM orders in LaNiO₃ [17]. It was also argued that AFM in LaNiO₃ can be originated from small oxygen vacancies [18, 19]. As oxygen vacancy level further increases, LaNiO₂.₅ becomes AFM below 152K, and LaNiO₂.₇₅ shows ferromagnetic (FM) structure below 225K [19]. However, LaNiO₂ does not show any clear evidence of the long-range magnetic order [20].

Spectroscopic measurements of LaNiO₃₋ₓ are also widely performed using X-ray Absorption Spectroscopy (XAS) and Photo-Emission Spectroscopy (PES) to study electronic structure in experiments. Consistently with the transport measurement, spectra at the Fermi energy decreases as the vacancy level $x$ increases from LaNiO₃, opening a spectral gap near the level at $x = 0.5$. An interesting feature measured from XAS in LaNiO₃₋ₓ bulk [21, 22] as well as the thin-layer structure [23] is the splitting of the spectral peak above the Fermi energy, which has been attributed to the oxygen vacancy effect.

There have been some first-principles studies of magnetism and oxygen vacancy effects on rare-earth nickelates. Previous density functional theory (DFT) and $GW$ study on LaNiO₃₋ₓ systems addressed the metal-insulator transition and resulting spectra due to the vacancy effect [24]. A. Malashevich *et al* [25] did a systematic study on LaNiO₃₋ₓ with small $x$ value and found that oxygen vacancies stay around the same Ni ion and localize extra electrons created by the vacancy. The strong localization of electrons due to the oxygen vacancies in other rare-earth nickelates also has been studied using DFT+U [26]. A. Subedi *et al* [27] studied structural and magnetic instabilities in LaNiO₃ with pos-

sible breathing-type lattice distortions using DFT and DFT+U. Theoretical studies on $RNiO_2$ with $R$=La, Nd, Sr, and Pr have attracted much attention recently as they can serve as model systems of experimentally dis- covered nickelate superconductors [28-34]. Nevertheless, the microscopic origin of the strongly correlated insulat- ing phase induced by oxygen vacancies and the changes of the correlated spectra in $LaNiO_{3-x}$ compared to ex periments have not been systematically investigated.

In this paper, we study the strong correlation ef- fect on the electronic structure and the energetics of $LaNiO_{3-x}$ from first-principles as the oxygen vacancy level $x$ evolves. We adopt dynamical mean field theory (DMFT) in combination with DFT to treat strong cor- relations in the paramagnetic phase as well as DFT+U for the long-range magnetic state. We show that the vacancy-ordered structure becomes thermodynamically stable in $LaNiO_{2.5}$ and the metal-to-insulator transition due to the change of the vacancy level $x$ can be captured correctly in DFT+DMFT. The insulating nature of the vacancy-ordered $LaNiO_{2.5}$ structure with two nonequiva lent Ni ions originates from the site-selective Mott phase due to both structural and electronic correlation effects. While bulk $LaNiO_3$ forms a rhombohedral structure with the octahedral geometry of the Ni ion surrounded by six O ions, oxygen vacancies can change both the oxidation number of the Ni ion and the local structure, which can lead to the substantial change of electronic structures in $LaNiO_{3-x}$.

Our paper is organized as follows. First, we explain the computational methods we used including DFT, DFT+U and DFT+DMFT in Sec. II and show the structural de- tails and magnetism in Sec. III A. We also study forma- tion energies of $LaNiO_{3-x}$ in Sec. III B. Then we dis play the spectral functions of $LaNiO_{3-x}$ computed using DFT+DMFT and DFT+U, and compare to experimen- tal measurements in Sec. III C. The DMFT self-energies in $LaNiO_{3-x}$ are displayed to explain the nature of the insulating phase in Sec. III D and compare our results to the rigid band shift approximation in Sec. III E. And we conclude our discussion in Sec. IV.

## II. COMPUTATIONAL METHODS

First, we performed structural relaxation calculations for $LaNiO_{3-x}$ ($x$=0, 0.25, 0.5, 0.75, and 1) systems and obtained the ground-state energies and magnetism us- ing both DFT and DFT+U. Vienna Ab-initio Simula- tion Package (VASP) [35, 36] has been used in all DFT and DFT+U calculations adopting the Perdew-Burke- Ernzerhof for solids (PBE-sol) [37] as the exchange and correlation energy functional. We set 600 eV as the energy cutoff for the plane wave basis and a Gaussian smearing of 0.2 eV is used for the summation over the Monkhorst-Pack $k$-point mesh. For $LaNiO_3$, $LaNiO_{2.5}$ and $LaNiO_2$ structures, we use a $8×8×8$ $k$-point grid. $LaNiO_{2.25}$ and $LaNiO_{2.75}$ have a rather large supercell with a long lattice vector along the $y-$direction, therefore we use a $6×3×6$ $k$-grid. For all structural relaxations, we set $0.001\ \mathrm{eV/\mathring{A}}$ as the force convergence condition fully relaxing the cell shape, volume and internal ionic positions.

Then we calculate the correlated electronic struc- ture using DFT+DMFT and DFT+U for $LaNiO_3$, $LaNiO_{2.5}$ and $LaNiO_2$. While DFT+U can cap- ture static correlations beyond DFT at the Hartree- Fock level based on single-determinant wavefunctions, DFT+DMFT can go beyond the static approximation in DFT+U and capture dynamical correlations based on multi-determinant many-body wavefunctions. To study magnetism, DFT+U is adopted to relax structures im- posing experimental magnetic orderings and to study the electronic structure from those relaxed structures. For a paramagnetic state, we adopt DFT+DMFT using the DFT relaxed structure with the non-magnetic(NM) or- der. The relaxed structures obtained using DFT and DFT+U are quite similar, as will be shown in next section. We adopt the DMFTwDFT package [38] for DFT+DMFT calculations. Wannier90 package [39, 40] has been adopted to obtain maximally localized Wannier functions for the construction of the DMFT correlated subspace. Nickelates show a rather strong $d-p$ hybridiza- tion due to the covalent bonding between Ni and O ions. Therefore, it is important to construct both Ni $3d$ and O $2p$ orbitals for the Wannier basis to treat the hybridiza- tion effect. To construct the Wannier orbitals, we take an energy window from -9 eV to 5 eV from the Fermi energy, which basically all Ni $3d$ and O $2p$ orbitals.

For DFT+U and DFT+DMFT, we need to define in- teraction parameters to treat the on-site Coulomb inter- action within the $d-$orbitals of the Ni ion. A rather small value of $U{(\simeq}$2eV) was used in the $d-$orbital model of previous rare-earth nickelates studies [41, 42] while $U$=5$\sim$7eV was used for the wide-energy window calcu- lation including both $d-$ and $p-$orbitals to reproduce the metal-insulator and structural phase diagram and to compare with the angle resolved photoemission spec- tra [43, 44]. Similar $U$ value ($\simeq$5.7eV) was also obtained from the constrained DFT calculation using the Quan- tum ESPRESSO code [45].For both DFT+DMFT and DFT+U calculations in this paper, we use the Hubbard $U$=5eV and the Hund's coupling $J$=0.8eV which are pa- rameterized by the Slater integrals. To account for the double-counting correction of DFT+DMFT, the modi- fied fully-localized-limit form of the double-counting po- tential, which was used for the phase diagram study of rare-earth nickelates [43, 46], has been used. To solve the DMFT impurity problem, we use the continuous- time quantum Monte Carlo [47, 48] solver with temper- ature $T\approx290$K. After DFT+DMFT calculations are converged, we used the post-processing tool from the DMFTwDFT package to calculate the spectral function $\mathrm{A}(\omega)$ for $LaNiO_{3-x}$. More details of the DMFT calcula- tion method are shown in the Supplemental Material.

![](./images/867756106598842495_1.jpg)

FIG. 1: Crystal structures of (a) LaNiO₃, (b) LaNiO₂.₅, (c) LaNiO₂.₂₅, (d) LaNiO₂.₇₅, and (e) LaNiO₂

## III. RESULTS

### A. Structural relaxation and magnetism

Bulk LaNiO₃ forms a rhombohedral structure given by the $R\overline{3}c$ space symmetry group [49]. This structure has two La, two Ni, and six O ions in a unit-cell, which can be obtained by rotating the Ni-O octahedra from the cubic perovskite structure. Namely, without any defects, each Ni ion is surrounded by six O ions forming the octahedron and all Ni-O octahedra are equivalent with the same Ni-O bond lengths (see Fig.1a). The oxygen vacancy formation induces the local structural distortion due to the absence of apical oxygens, which breaks the cubic symmetry. While it is challenging to measure the crystal structure with vacancies, several experiments [13, 50, 51] suggest the LaNiO₂.₅ structure such that NiO₆ octahedra and NiO₄ square-planes are alternating in the $x-y$ plane as shown in Fig 1b. Previous DFT calculation [25] also provides the insight that the apical divacancy configuration lowers the formation energy than other configurations meaning a four-coordinated Ni-O square plane is energetically favored when oxygen vacancies are introduced. In this paper, we denote Ni in the octahedral environment as Niₒ and Ni in the square-planar symmetry as Niₛₚ. We also construct LaNiO₂.₂₅ and LaNiO₂.₇₅ structures with vacancy orderings such that Niₒ and Niₛₚ ions modulated along the $x-y$ plane, as shown in Fig 1c and Fig 1d. LaNiO₂ becomes a tetragonal structure of purely Niₛₚ ions with NiO₄ square-planes (see Fig. 1e).

While LaNiO₃ remains a PM metallic state at all temperatures, LaNiO₃₋ₓ $(x>0)$ undergoes the magnetic transition for most cases. In Table I, we list the experimentally observed long-range magnetic orderings of LaNiO₃₋ₓ including the ground state (metal or insulator) and the Neel temperature $(T_N)$ with relevant references. Most LaNiO₃ structures with O vacancies become FM except LaNiO₂.₅. Previous experimental work [50] in LaNiO₂.₅ suggests that LaNiO₂.₅ is the G-type AFM and the Niₒ ions have relatively large magnetic moments, while the Niₛₚ ions have almost no magnetic moment. All LaNiO₃₋ₓ structures become paramagnetic above $T_N$.

To study the structural and magnetic properties, we fully relaxed the oxygen-vacancy ordered structures of LaNiO₃₋ₓ with $x$ =0, 0.25, 0.5, 0.75 and 1 using both DFT and DFT+U. In Table II, we provide the structure details obtained from the relaxations with magnetic structures observed in experiments for x=0, 0.5 and 1. That is to say, we impose the G-type AFM order on LaNiO₂.₅ relaxations. The non-magnetic(NM) order calculations on LaNiO₂ and LaNiO₃ are performed to simulate PM nature in experiment. In LaNiO₃, DFT Ni-O bond length and Ni-O-Ni bond angle are similar to experiment while DFT+U overestimate the bond angle along with the contracted bond length. LaNiO₂.₅ has two nonequivalent Ni ions and the Niₒ-O bond length is much larger than the Niₛₚ-O bond length. LaNiO₂.₅ structure relaxed with DFT shows the Ni-O bond length difference to be 0.14Å. DFT+U predicts the similar Ni-O bond difference $(\sim0.22Å)$ as the experimental value $(\sim0.21Å)$ although the absolute values of the bond lengths in DFT+U are smaller than experimental values. In LaNiO₂, the Ni-Ni distance along $z$-axis is quite smaller than along the $x-y$ plane due to the loss of apical oxygens and the DFT structural parameters are closer to experimental values than the DFT+U parameters.

<table>
<caption>TABLE I: Experimental magnetic and transport (metal/insulator) properties of LaNiO₃₋ₓ</caption>
<thead>
  <tr>
    <th>LaNiO₃₋ₓ</th>
    <th>M/I</th>
    <th>MAG.</th>
    <th>$T_N$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>LaNiO₃ [13, 18]</td>
    <td>M</td>
    <td>PM</td>
    <td>0K</td>
  </tr>
  <tr>
    <td>LaNiO₂.₇₅ [13, 19]</td>
    <td>M</td>
    <td>FM</td>
    <td>225K</td>
  </tr>
  <tr>
    <td>LaNiO₂.₅₃ [51]</td>
    <td>N/A</td>
    <td>FM</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>LaNiO₂.₅ [13, 19]</td>
    <td>I</td>
    <td>AFM</td>
    <td>152K</td>
  </tr>
  <tr>
    <td>LaNiO₂ [14, 20]</td>
    <td>M</td>
    <td>PM</td>
    <td>N/A</td>
  </tr>
</tbody>
</table>

In Table III, we calculate the ground-state energies of LaNiO₃₋ₓ using DFT and DFT+U. Different magnetic orderings including G-type AFM, FM and NM order are imposed during the relaxation calculations and subtract the resulting FM energy from the G-type AFM energy for each system. In each structure, different magnetism can be obtained by converging the solutions from different initial configurations. In LaNiO₃, the ground-state converges to the NM structure regardless of FM or AFM initial configurations in DFT while DFT+U predicts it to be FM. Also in LaNiO₂, DFT converges to the NM configuration while AFM is more stable in DFT+U. In LaNiO₂.₅, DFT+U predicts the ground-state to be AFM

<table>
<caption>TABLE II: Structural information of LaNiO₃, LaNiO₂.₅, and LaNiO₂ obtained from DFT and DFT+U relaxations.</caption>
<tbody>
<tr>
<td/>
<td>Parameters</td>
<td>DFT</td>
<td>DFT+U</td>
<td>Exp</td>
</tr>
<tr>
<td>LaNiO₃</td>
<td>d<sub>Ni−O</sub> [Å]</td>
<td>1.90</td>
<td>1.88</td>
<td>1.93[52]</td>
</tr>
<tr>
<td>(NM)</td>
<td>α<sub>Ni−O−Ni</sub> [°]</td>
<td>164.5</td>
<td>168.3</td>
<td>164.8[52]</td>
</tr>
<tr>
<td>LaNiO₂.₅</td>
<td>d<sub>Ni−Ni</sub>ᵃ [Å]</td>
<td>3.83</td>
<td>3.82</td>
<td>3.91[50]</td>
</tr>
<tr>
<td>(AFM)</td>
<td>d<sub>Ni−Ni</sub>ᵇ [Å]</td>
<td>3.64</td>
<td>3.67</td>
<td>3.74[50]</td>
</tr>
<tr>
<td/>
<td>d<sub>Ni<sub>sp</sub>−O</sub> [Å]</td>
<td>1.86</td>
<td>1.83</td>
<td>1.91[50]</td>
</tr>
<tr>
<td/>
<td>d<sub>Ni<sub>o</sub>−O</sub>ᵃ [Å]</td>
<td>2.00</td>
<td>2.05</td>
<td>2.12[50]</td>
</tr>
<tr>
<td/>
<td>d<sub>Ni<sub>o</sub>−O</sub>ᵇ [Å]</td>
<td>1.86</td>
<td>1.88</td>
<td>1.92[50]</td>
</tr>
<tr>
<td>LaNiO₂</td>
<td>d<sub>Ni−Ni</sub>ᵃ [Å]</td>
<td>3.89</td>
<td>3.84</td>
<td>3.96[20]</td>
</tr>
<tr>
<td>(NM)</td>
<td>d<sub>Ni−Ni</sub>ᵇ [Å]</td>
<td>3.34</td>
<td>3.32</td>
<td>3.37[20]</td>
</tr>
<tr>
<td/>
<td>d<sub>Ni−O</sub>ᵃ [Å]</td>
<td>1.95</td>
<td>1.92</td>
<td>1.98[20]</td>
</tr>
</tbody>
</table>

ᵃ Along the $x-y$ plane.
ᵇ Along the $z$ axis.

consistently with the experiment (see TableI) while DFT converges to the FM ground state. This implies that the correlation treated in DFT+U can be important to capture the ground-state magnetic configuration in structures with vacancies. Both DFT and DFT+U give the FM order lower energy than AFM order in LaNiO₂.₇₅, which is also consistent with experiments.

In LaNiO₂.₅, the spin-state ordering occurs as the Ni<sub>o</sub> ion in NiO₆ exhibits a high-spin state while the Ni<sub>sp</sub> ion in NiO₄ shows a low-spin state [50]. This spin-state ordering induced by the oxygen vacancy ordering is also consistent with our DFT+U calculation. We find the Ni<sub>O</sub> ion shows a high-spin state with the magnetic moment of $1.62\mu_B$, which is much larger than the low-spin moment in Ni<sub>sp</sub> ($0.16\mu_B$). This spin-state ordering is also accompanied by the in-plane Ni-O bond disproportionation in which the Ni<sub>o</sub> bond length is much larger than the Ni<sub>sp</sub>-O bond length by $\sim0.22Å$ (see Table II). LaNiO₂.₇₅ and LaNiO₂.₂₅ with FM order also show the similar trends of the spin-state ordering in our calculations in that the Ni<sub>o</sub> ion has a larger moment than the Ni<sub>sp</sub> ion, as shown in Table IV.

<table>
<caption>TABLE III: Total energy difference per formula unit [meV] between FM and AFM in LaNiO₃₋ₓ.</caption>
<tbody>
<tr>
<td>LaNiO₃₋ₓ</td>
<td>DFT</td>
<td>DFT+U</td>
</tr>
<tr>
<td/>
<td>AFM-FM</td>
<td>AFM-FM</td>
</tr>
<tr>
<td>LaNiO₃</td>
<td>0ᵃ</td>
<td>341</td>
</tr>
<tr>
<td>LaNiO₂.₇₅</td>
<td>4</td>
<td>40</td>
</tr>
<tr>
<td>LaNiO₂.₅</td>
<td>10</td>
<td>-41</td>
</tr>
<tr>
<td>LaNiO₂.₂₅</td>
<td>2</td>
<td>68</td>
</tr>
<tr>
<td>LaNiO₂</td>
<td>20ᵇ</td>
<td>-51</td>
</tr>
</tbody>
</table>

ᵃ Both FM and AFM converged to zero magnetic moment.
ᵇ FM converged to zero magnetic moment.

<table>
<caption>TABLE IV: Magnetic moments $[\mu B]$ of LaNiO₃₋ₓ computed using DFT+U.</caption>
<tbody>
<tr>
<td>LaNiO₃₋ₓ</td>
<td>Ni<sub>o</sub></td>
<td>Ni<sub>sp</sub></td>
</tr>
<tr>
<td>LaNiO₂.₇₅[FM]</td>
<td>1.04/1.47/1.04</td>
<td>0.11</td>
</tr>
<tr>
<td>LaNiO₂.₅[AFM]</td>
<td>1.62</td>
<td>0.16</td>
</tr>
<tr>
<td>LaNiO₂.₂₅[FM]</td>
<td>1.60</td>
<td>0.8/0.8/0.8</td>
</tr>
</tbody>
</table>

## B. Formation energies

The stability of the oxygen vacancy ordered structure can be determined by the formation energy calculation. Here, we compute the vacancy formation energy per formula unit for LaNiO₃₋ₓ structures as a function of the oxygen chemical potential related to the given oxygen pressure. The formation energy can be given by [53]

$$
E_{form}=E_{LaNiO_{3-x}}-E_{LaNiO_{3}}+x\cdot\frac{1}{2}E_{O_{2}}+x\cdot\mu_{O}\ (1)
$$

where $E_{form}$ is the Gibbs formation energy, $x$ is the vacancy level, $E_{LaNiO_{3-x}}$ is the total energy of LaNiO₃₋ₓ, $E_{O_{2}}$ is the total energy of the $O_2$ molecule, and $\mu_O$ is the oxygen chemical potential depending on pressure and temperature. Here, we neglect the phonon and entropy contributions of LaNiO₃₋ₓ to the Gibbs formation energy at finite temperatures. In experiments, the thermodynamic stability condition of oxygen vacancies in given materials can depend on the applied oxygen pressure $P$ and temperature $T$. We assume that the oxygen molecule forms an ideal-gas-like reservoir during the experimental sample growth, therefore its chemical potential can be given by [53–56]

$$
\mu_{O}(T,P)=\mu_{O}(T,P^{0})+\frac{1}{2}k_{B}T\ln\left(\frac{P}{P^{0}}\right)\qquad(2)
$$

where $P^0$ is the ambient pressure. The $\mu_O(T,P^0)$ values are taken from Ref.54. Typical experimental growth of LaNiO₃ on the SrTiO₃ substrate is carried out at around 920K and 10 Pa oxygen pressure [22].

In Fig.2 we plot $E_{form}$ as a function of $\mu_O$ (related to the applied pressure) at 920K computed using DFT+U, DFT and DFT+DMFT. We compute the total energies of LaNiO₃₋ₓ in Eq.1 using first-principles (DFT, DFT+U, and DFT+DMFT) by adopting the same relaxed structures of LaNiO₃₋ₓ as used in the spectra calculations. We choose the magnetic order in DFT or DFT+U calculations resulting the lowest energy while DFT+DMFT calculations adopt the PM order for all LaNiO₃₋ₓ structures at 920K. Our results suggest that, for the oxygen-rich region, when the oxygen pressure higher than 55Pa (corresponding to $\mu_o$ > -1.3 eV), LaNiO₃ is the most stable structure compared to other vacancy structures with the positive vacancy formation energies. However, as the oxygen pressure is lowered than 4.5Pa (corresponding to -2.1 eV $< \mu_o <$ -1.4 eV), we find that LaNiO₂.₅ becomes

![](./images/867756106598842495_2.jpg)

FIG. 2: Formation energies $E_{form}$ of LaNiO$_{3-x}$ as a function of the oxygen chemical potential $\mu_O$ (related to the oxygen pressure $P$) calculated using DFT+U (at $T$ =0K), DFT (at $T$ =0K) and DFT+DMFT (at $T$ =920K). The vertical dashed line indicates the typical oxygen pressure used in experiment.

the most stable structure in the DFT+U calculation al- though different vacancy structures have very similar for- mation energies in DFT. DFT+DMFT also shows the similar energetics as a function of the oxygen pressure compared to DFT+U implying that correlation effects in DFT+DMFT or DFT+U treated beyond DFT can be important to capture the correct formation energy in oxy- gen vacancy structures. Since DFT+U (DFT+DMFT) can capture the correct AFM (PM) order as well as the insulating state in LaNiO$_{2.5}$, the predicted vacancy or- dered structure from first-principles can be indeed sta- ble under the experimental growth condition of the lower oxygen pressure region.

## C. Correlated density of states

In this section, we study the correlated density of states (DOS) for the vacancy-ordered structure in LaNiO$_{2.5}$ as well as stoichiometric LaNiO$_3$ and LaNiO$_2$ using both DFT+DMFT and DFT+U to treat correlations beyond DFT. First, we compare the DOS for stoi- chiometric LaNiO$_3$ ($x$=0; Fig. 3a) and LaNiO$_2$ ($x$=1; Fig. 3b) computed using DFT+DMFT. LaNiO$_3$ com- puted using DFT+DMFT shows the Fermi-liquid metal feature, which is consistent with the experimental mea- surement [9]. The overall peak positions computed in DFT+DMFT are also consistent with the experi- mental PES peak positions [22]. Our orbital-resolved DFT+DMFT DOS reveals that the small bump below the Fermi energy has mostly the Ni $e_g$ character and the sharp peak near -0.7 eV is mostly contributed from the $t_{2g}$ character although O $2p$ orbitals are also mixed with these orbitals. O $2p$ peaks are distributed broadly below -2 eV. The unoccupied DOS also shows a broad $e_g$ peak with a strong mixture with O $2p$ spectra due to the co- valent bonding between Ni and O ions. As a result, the hole density per the O ion is 0.26 and the occupancy of the Ni $3d$ orbital becomes $\sim$7.8 (See Table V).

The absence of apical oxygens in LaNiO$_2$ changes electronic structures significantly compared to LaNiO$_3$. First, the apical oxygen vacancy breaks the symmetry of the Ni-O octahedron and split the on-site orbital energies within $e_g$ and $t_{2g}$ manifolds as the local geometry of the Ni-O bonding becomes a square-planar symmetry. As a result, two $e_g$ orbitals in Ni$_{sp}$ become non-degenerate and the $d_{z^2}$ orbital is lower in energy than the $d_{x^2-y^2}$ or- bital. Second, the removal of the apical oxygen ions from the Ni-O octahedron means that two electrons are effec- tively donated to the remaining the Ni-O square plane. The donation of two electrons from the apical oxygen changes the oxidation state of Ni$^{3+}$ in LaNiO$_3$ to Ni$^{1+}$ in LaNiO$_2$. Due to this electron transfer, $d$-occupancy in Ni$_{sp}$ becomes close to 9.1 while the hole per O ion is also reduced to 0.06 (See Table V). As a result, the $d_{z^2}$ orbital tends to be fully filled while the $d_{x^2-y^2}$ orbital is almost half-filled enhancing the electronic correlation effect.

Our DMFT DOS in LaNiO$_2$ is also consistent with the experimental XAS measurement [57] showing the strong reduction of the unoccupied O $2p$ spectra com- pared to the LaNiO$_3$ case. Our unoccupied O $2p$ DOS (blue dashed line in Fig.3b) is also much reduced and the occupied O $2p$ peak in LaNiO$_2$ is located further below the Fermi energy due to the reduced hole density in the O ion and the decreased Ni-O hybridization compared to LaNiO$_3$. Due to this much reduced Ni-O hybridization

![](./images/867756106598842495_3.jpg)

FIG. 3: The orbital-resolved DOS of LaNiO$_3$ (a,c) and LaNiO$_2$ (b,d) computed using DFT+DMFT (a,b) and DFT+U (c,d). The $e_g$ orbitals in LaNiO$_3$ are degenerate. The shaded region is taken from the experimental PES measurement[22].

and the $d_{x^2-y^2}$ orbital occupancy close to the half-filling, the $LaNiO_2$ becomes close to the Mott insulating phase as reflected in the strong reduction of the $d_{x^2-y^2}$ spectra near the Fermi energy which is also consistent with the experimental XAS measurement [57]. This incoherent metallic state due to the strong correlation effect is also reflected in the large scattering rate (the imaginary part of the self-energy at the zero frequency in Fig. 5b) and consistent with the poor conductivity measured experimentally in $LaNiO_2$ [14]. Our DFT band structure calculation reveals that some La $5d$ bands are also crossing below the Fermi energy (see Supplemental Material) although we do not include this hybridization effect of the La $5d$ orbital as we construct the Wannier functions for only Ni $3d$ and O $2p$ orbitals. Although treating the effect of this La $5d$ orbital on the DMFT correlation is beyond the scope of our paper, previous DMFT calculation in the similar $NdNiO_2$ material argues that the Nd $5d$ band acts as a charge reservoir without significant hybridization with the Ni $3d$ orbital [30].

In Fig.3c and 3d, we also plot the orbital-resolved DOS for both $LaNiO_3$ and $LaNiO_2$ obtained using DFT+U. We impose the NM spin order for both materials, consistently with the experiment as listed in Table I. In both materials, the DFT+U calculations also exhibit qualitatively similar features as the DFT+DMFT spectra. In $LaNiO_3$, the $t_{2g}$ peak is located slightly below the experimental peak at -0.7eV and the it is somewhat strongly hybridized with O $p$ orbitals. Consistently with DMFT, the unoccupied O $2p$ DOS becomes much reduced in $LaNiO_2$ and $d_{x^2-y^2}$ orbital is also nearly half filled. However, the DFT+U spectra have still large DOS intensity at Fermi level and the O $2p$ peak is relatively close to the Fermi energy compared to DMFT.

Now we turn to the $LaNiO_{2.5}$ case with the oxygen vacancy ordering. We performed both DFT+DMFT and DFT+U calculations to study the correlated electronic structure beyond DFT treating the realistic oxygen vacancy structure (Fig.4b-e). DFT+U was performed with the G-type AFM ordering (the lowest-energy magnetic structure; see TableIII) and DFT+DMFT was performed with the paramagnetic spin symmetry. In this structure, the six-coordinated Ni-O octahedron $(Ni_o)$ and the four-coordinated Ni-O square-plane $(Ni_{sp})$ are alternating in the $x-y$ plane as two apical oxygen ions are removed from the half of octahedra in $LaNiO_3$ (see Fig. 4a). Our structural relaxation calculation shows that the Ni-O octahedron is distorted as the in-plane Ni-O bond length is larger than the out-of-plane bond (see Table II). However, the orbital energy difference between two $e_g$ orbitals is only 0.04eV, which is much smaller than $e_g$-$t_{2g}$ splitting of 0.62eV. In $Ni_{sp}$, the energy splitting between $d_{z^2}$ and $d_{x^2-y^2}$ is as large as 0.8eV.

As shown in Fig.4b-e, both DFT+DMFT and DFT+U predict the $LaNiO_{2.5}$ to be insulating consistently with experiments. This is in sharp contrast with the DFT DOS predicting the ground state to be metallic as DFT underestimates correlations (see Supplemental Material). DFT+DMFT DOS opens a spectral gap of 0.3 eV resulting in the PM insulating state while the band gap computed in DFT+U with AFM becomes much larger ($\sim$1.5 eV). Our DFT+DMFT calculation can also reveal that the two-peak structure of the unoccupied spectra measured in experiment originates from the two nonequivalent Ni ions in $LaNiO_{2.5}$. The $Ni_o$ ion (Fig. 4b) develops a spectral Mott gap in the middle of the almost degenerate $e_g$ orbitals and the broad unoccupied peak near 2eV above the Fermi energy emerges as the upper Hubbard band due to the localized nature of $Ni_o$ $e_g$ orbitals induced by the oxygen vacancy. In $Ni_{sp}$, the $d_{z^2}$ orbital spectra become occupied while the unoccupied DOS near 1eV is mostly contributed from the $d_{x^2-y^2}$ orbitals also hybridized with the in-plane O $2p$ orbitals. Although all O ions are equivalent in $LaNiO_3$, two types of nonequiva-

![](./images/867756106598842495_4.jpg)

FIG. 4: (a) The crystal structure of $NiO_{2.5}$ showing two nonequivalent Ni ions with the distinct orbital energy level diagram. The site- and orbital-resolved DOS of $LaNiO_{2.5}$ obtained using DFT+DMFT (b and c) and DFT+U (d and e) computed for $Ni_o$ (b and d) and $Ni_{sp}$ (c and e). PES and XAS data are taken from experimental measurements [22].

lent O ions exist in $LaNiO_{2.5}$, which are circled in Fig. 4a denoted as $O_A$ and $O_B$. $O_A$ is the apical oxygen of the $Ni_o$ ion and $O_B$ is the in-plane oxygen located between $Ni_o$ and $Ni_{sp}$. The O1s XAS spectra provide a relatively unperturbed probe of the unoccupied DOS since the O1s core hole effect is negligible [58]. However, it can probe not only O $2p$ but also $3d$ states in oxide materials due to strong $d-p$ hybridization [59]. The $O_B$ $2p$ unoccupied DOS is mostly distributed near 1eV as it is strongly hybridized with the $Ni_{sp}$ $d_{x^2-y^2}$ orbitals. The $O_A$ $2p$ unoccupied DOS is rather weakly hybridized with the $Ni_o$ ion showing much reduced spectra, but it is broadly distributed at higher energies than the $O_B$ spectra. In DFT+U DOS (Fig. 4d and e), the qualitative features of DOS are similar as the DMFT DOS confirming that the unoccupied two-peak structure is originated from two nonequivalent Ni ions. However, the DFT+U peak positions are higher in energy than the experimental peak positions.

### D. Site-selective Mott insulating state in $LaNiO_{2.5}$

Here, we show the imaginary part of the self-energy on the real energy axis, $Im\Sigma(\omega)$ of Ni $e_g$ orbitals computed using DMFT in Fig. 5. Two types of Ni ions in $LaNiO_{2.5}$ are plotted in Fig. 5c and Fig. 5d. $LaNiO_3$ (Fig. 5a) and $LaNiO_2$ (Fig. 5b) are also compared. The self-energies of $e_g$ orbitals in $LaNiO_3$ are degenerate and show the Fermi-liquid behavior $(Im\Sigma \sim \omega^2)$ at the low frequency, consistently with the metallic state. In $LaNiO_2$, the $d_{x^2-y^2}$ orbital develop correlations as the self-energy develops a pole near the Fermi energy with the large scattering rate at $\omega=0$. In $LaNiO_{2.5}$, both $Ni_o$ $e_g$ orbitals have strong correlations at the Fermi energy as self energy curves have poles right near $\omega$=0 while $Ni_{sp}$ in $LaNiO_{2.5}$ exhibits a flat curve. Since $Ni_o$ $e_g$ orbitals in $LaNiO_{2.5}$ are also nearly half filled (see Fig. 4a energy diagram), this indicates a Mott type insulator in $Ni_o$ while the $Ni_{sp}$ ions with oxygen vacancies behave similarly as the band insulator as only one $e_g$ orbital is fully filled and the other $e_g$ orbital is almost unoccupied (see Fig.4a energy diagram). This Mott insulating behavior occurs at the half of lattice sites selectivity (in this case for $Ni_o$ sites), therefore it can be understood as the "site-selective" Mott transition.

This site-selective Mott insulating phase is also accompanied by the substantial Ni-O bond disproportionation of $0.22Å$ between $Ni_o$ and $Ni_{sp}$ as obtained in the DFT+U relaxation calculation (see Table II) since the Mott insulating site is expanded to reduce the hybridization between Ni and neighboring O ions. In DFT+U, this mechanism occurs as the spin-state ordering since the Mott insulating site becomes a high-spin state while the band insulating site exhibits a low-spin state. This site-selective Mott mechanism also occurs in other correlated materials including rare-earth nickelates with smaller rare-earth ions such as $LuNiO_3$ [6], the spin-state ordered $LaCoO_3$ [60], $Fe_2O_3$ under the high pressure [61, 62], and doped manganese oxides [63]. Like the $LaNiO_3$ case with oxygen vacancies, the site-selective Mott insulating phase in other materials also accompanies some degrees of breathing-type lattice distortions as the Mott insulating site develops in an expanded octahedron and the band insulating site forms in a contracted octahedron due to strong hybridization of transition metal spins with surrounding O holes.

![](./images/867756106598842495_5.jpg)

FIG. 5: Imaginary part of self-energies $Im\Sigma(\omega)$ computed for Ni $d_{z^2}$ and $d_{x^2-y^2}$ orbitals in (a) $LaNiO_3$, (b) $LaNiO_2$, and $LaNiO_{2.5}$ for two nonequivalent Ni ions, (c) $Ni_o$ and (d) $Ni_{sp}$ respectively.

In DMFT calculation, one can also measure the correlation strength from the obtained quasi-particle residue $Z$ defined as:
$$
Z = \left(1 - \left.\frac{\partial\Sigma}{\partial\omega}\right|_{\omega=0}\right)^{-1} \tag{3}
$$
which gives the inverse of the effective mass renormalization factor $(m^*/m=Z^{-1})$. The Ni $e_g$ band of $LaNiO_3$ has an effective mass factor of 1.7. For $LaNiO_2$, electronic correlation is further enhanced than $LaNiO_3$ and the quasi-particle band of the $d_{x^2-y^2}$ orbital is strongly renormalized with a factor of 9.4. As $LaNiO_{2.5}$ with oxygen vacancies becomes an insulator, the concept of the quasiparticle mass renormalization cannot be applied any more since quasiparticles do not exist in an insulator.

Oxygen vacancy also changes the Ni oxidation state and increases the electron occupation in the Ni-O manifold effectively as two electrons are donated from the removed oxygen ion. Table V shows the occupation number for Ni $3d$ and O $2p$ orbitals in each structure obtained from DFT+DMFT and DFT+U. In DFT+DMFT calculations, as the Ni oxidation state changes from $Ni^{3+}$ in $LaNiO_3$ to $Ni^{1+}$ in $LaNiO_2$, the $d$-orbital occupancy increases from 7.8 to 9.12 and the hole occupancy in the

O ion decreases from 0.26 to 0.06. DFT+U also shows the increase of the average $d-$orbital occupancy from LaNiO₃ to LaNiO₂, however its value is larger than the DFT+DMFT result. In LaNiO₂.₅, the average Ni oxidation state is $Ni^{2+}$. However, it is not clear whether the electron transfer due to oxygen vacancy will occur mostly to $Ni_{sp}$ resulting in charge ordering between $Ni^{3+}$ in the $Ni_o$ ion and $Ni^{1+}$ in the $Ni_{sp}$ ion or both $Ni_o$ and $Ni_{sp}$ ions will have the similar $Ni^{2+}$ configuration without charge ordering. Our DFT+DMFT calculation shows that $Ni_o$ is close to $Ni^{2+}$ as the $e_g$ orbitals in $Ni_o$ are almost half filled ($\sim$2.13) and the $e_g$ occupancy in $Ni_{sp}$ is slightly more occupied than the half-filling leaving some holes per the O site ($\sim$0.15). This hole state in O is rather strongly hybridized with the $Ni_{sp}$ $e_g$ orbital as shown in the previous DOS result. Therefore, the site-selective Mott transition in LaNiO₂.₅ also leads to small charge ordering between $Ni_o$ and $Ni_{sp}$ ions. DFT+U also shows the similar charge ordering in LaNiO₂.₅.

TABLE V: Occupations of Ni $3d$ and O $2p$ orbitals in LaNiO₃₋ₓ obtained from DFT+DMFT and DFT+U.

<table>
  <thead>
    <tr>
      <th>DFT+DMFT</th>
      <th>Niₒ</th>
      <th>Niₛₚ</th>
      <th>Oₐᵥ₉</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LaNiO₃(PM)</td>
      <td>7.79</td>
      <td>N/A</td>
      <td>5.74</td>
    </tr>
    <tr>
      <td>LaNiO₂.₅(PM)</td>
      <td>8.15</td>
      <td>8.57</td>
      <td>5.86</td>
    </tr>
    <tr>
      <td>LaNiO₂(PM)</td>
      <td>N/A</td>
      <td>9.12</td>
      <td>5.94</td>
    </tr>
    <tr>
      <td>DFT+U</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LaNiO₃(NM)</td>
      <td>8.23</td>
      <td>N/A</td>
      <td>5.59</td>
    </tr>
    <tr>
      <td>LaNiO₂.₅(AFM)</td>
      <td>8.27</td>
      <td>8.73</td>
      <td>5.80</td>
    </tr>
    <tr>
      <td>LaNiO₂(NM)</td>
      <td>N/A</td>
      <td>9.30</td>
      <td>5.85</td>
    </tr>
  </tbody>
</table>

## E. Rigid band shift approximation in LaNiO₃₋ₓ

Our DFT+DMFT calculation in LaNiO₂.₅ shows that the paramagnetic insulating phase in LaNiO₂.₅ originates from the change of Ni oxidation states as well as the oxygen vacancy ordering structure which induces both the local symmetry change of Ni ions and different hybridization of Ni ions with surrounding O ions. To investigate the effect of the oxygen vacancy ordering structure on electronic correlations, we apply the rigid band shift approximation to LaNiO₃ within DFT+DMFT to impose the effect of the Ni oxidation state change alone. In this approximation, we use the same Wannier band structure obtained from LaNiO₃ at different vacancy levels while the effect of different Ni oxidation states is adopted by shifting the Fermi level to modify the total number of electrons within DMFT calculations accordingly.

Fig.6a-e shows the DOS of different Ni oxidation states due to the change of vacancy level $x$, namely $Ni^{3+}$ for $x$=0 and $Ni^{1+}$ for $x$=1. As the oxidation number changes from $Ni^{3+}$ to $Ni^{1+}$, O $p$ and Ni $t_{2g}$ states move further below the Fermi energy while keep the shape mostly unchanged. This trend is also consistent with the experiment data depicted as the shaded region. The Ni $e_g$ states near the Fermi energy also do not change significantly as the Fermi level shifts higher in energy for the smaller oxidation state. The $Ni^{2+}$ state corresponding to LaNiO₂.₅ still exhibits the metallic state without developing a Mott state although the $e_g$ occupancy becomes close to the half-filling. In Fig.6f, we plot the mass renormalization factor $m^*/m$ and the corresponding Ni $d$ occupancies as

![](./images/867756106598842495_6.jpg)

FIG. 6: (a)-(e) DFT+DMFT DOS of LaNiO₃₋ₓ systems at different Ni oxidation states computed using the rigid band shift approximation. (f) The $d$ occupancy and the mass renormalization factor as a function of different Ni oxidation states.

a function of Ni oxidation states. While the $d$ occupancies change linearly, the effective mass becomes maximum only when the $d$ occupancy becomes close to 8.0 meaning the half-filled $e_g$ occupancy although the mass renormalization remains in range of 1.5-2.5. Therefore, the strong correlation effect occurring in the oxygen vacancy structure cannot be captured by the Ni oxidation change alone within the rigid band shift approximation.

## IV. CONCLUSION

In conclusion, we performed first principles calculations in $\mathrm{LaNiO}_3$ with oxygen vacancies ($\mathrm{LaNiO}_{3-x}$ with $x$=0, 0.25, 0.5, 0.75, and 1). Experimentally, the metal-to-insulator transition occurs as the oxygen vacancy level $x$ approaches to 0.5 and the ground state is AFM (AFM becomes PM at higher temperature). We find that the vacancy ordering structure of alternating $\mathrm{NiO}_6$ octahedra and $\mathrm{NiO}_4$ square planes (with apical oxygen vacancies) becomes thermodynamically stable in $\mathrm{LaNiO}_{2.5}$ when the oxygen pressure is lowered than the typical growth condition of $\mathrm{LaNiO}_3$. DFT+U converges to the correct AFM magnetic order in $\mathrm{LaNiO}_{2.5}$ while DFT favors FM implying that the electronic correlation effect can be important for oxygen vacancy structures. Our DFT+DMFT calculation in $\mathrm{LaNiO}_{2.5}$ shows that the PM state is insulating and the nature of this insulating state is the site-selective Mott phase in which the octahedral Ni ion develops a Mott state with strong electron correlations and the square-planar Ni ion becomes a band insulator with the negligible self-energy. We also explain the nature of the two-peak structure in unoccupied spectra measured in O1s XAS experiments of $\mathrm{LaNiO}_{3-x}$. The lower energy peak in XAS originates from the square-planar Ni state strongly hybridized with O ions while the higher energy peak is resulted from the broad spectra of the localized $e_g$ orbitals in strongly correlated octahedral Ni ion. $\mathrm{LaNiO}_2$ with the complete apical oxygen vacancies becomes also strongly correlated as it reduces the Ni-O hybridization and lifts the degeneracy between $e_g$ orbitals, as a result, it becomes close to the Mott state although it is still metallic.

The change of Ni oxidation states alone within the rigid band shift approximation cannot capture the strongly correlated insulating phase occurring in the oxygen vacancy structure of $\mathrm{LaNiO}_3$ implying that it is important to treat realistic oxygen vacancy structures of materials using first-principles to account for electronic correlation effects induced by oxygen vacancies. Moreover, the Hubbard $U$ values of Ni ions can be site-dependent in oxygen-vacancy structures since chemical environments of Ni ions can be varied due to oxygen vacancies. In principle, site-dependent $U$ values can be computed from first-principles, and their effects on electronic structure of materials with oxygen vacancies can be an interesting topic for future studies.

## ACKNOWLEDGEMENT

X. Liao and H. Park are supported by the Materials Sciences and Engineering Division, Basic Energy Sciences, Office of Science, US DOE. The part of this work related to the vacancy formation energy calculation is supported by ACS-PRF grant 60617. V. Singh is supported by the NSF SI2-SSE Grant 1740112. We gratefully acknowledge the computing resources provided on Bebop, a high-performance computing cluster operated by the Laboratory Computing Resource Center at Argonne National Laboratory.

[1] G. Catalan, Phase Transitions 81, 729 (2008), https://doi.org/10.1080/01411590801992463.
[2] P. Zubko, S. Gariglio, M. Gabay, P. Ghosez, and J.-M. Triscone, Annual Review of Condensed Matter Physics 2, 141 (2011), https://doi.org/10.1146/annurev-conmatphys-062910-140445.
[3] J. A. Alonso, M. J. Martínez-Lope, M. T. Casais, J. L. García-Muñoz, and M. T. Fernández-Díaz, Phys. Rev. B 61, 1756 (2000).
[4] U. Staub, G. I. Meijer, F. Fauth, R. Allenspach, J. G. Bednorz, J. Karpinski, S. M. Kazakov, L. Paolasini, and F. d'Acapito, Phys. Rev. Lett. 88, 126402 (2002).
[5] J.-S. Zhou, J. B. Goodenough, B. Dabrowski, P. W. Klamut, and Z. Bukowski, Phys. Rev. Lett. 84, 526 (2000).
[6] H. Park, A. J. Millis, and C. A. Marianetti, Phys. Rev. Lett. 109, 156402 (2012).
[7] S. Catalano, M. Gibert, J. Fowlie, J. Íñiguez, J.-M. Triscone, and J. Kreisel, Reports on Progress in Physics 81, 046501 (2018).
[8] F. Gunkel, D. V. Christensen, Y. Z. Chen, and N. Pryds, Applied Physics Letters 116, 120505 (2020).
[9] R. Eguchi, A. Chainani, M. Taguchi, M. Matsunami, Y. Ishida, K. Horiba, Y. Senba, H. Ohashi, and S. Shin, Phys. Rev. B 79, 115122 (2009).
[10] M. K. Stewart, C.-H. Yee, J. Liu, M. Kareev, R. K. Smith, B. C. Chapler, M. Varela, P. J. Ryan, K. Haule, J. Chakhalian, and D. N. Basov, Phys. Rev. B 83, 075125 (2011).
[11] D. G. Ouellette, S. B. Lee, J. Son, S. Stemmer, L. Balents, A. J. Millis, and S. J. Allen, Phys. Rev. B 82, 165112 (2010).
[12] T. Moriga, O. Usaka, I. Nakabayashi, T. Kinouchi, S. Kikkawa, and F. Kanamaru, Solid State Ionics 79, 252 (1995), proceedings of the 20th Commemorative Symposium on Solid State Ionics in Japan.
[13] R. D. Sánchez, M. T. Causa, A. Caneiro, A. Butera, M. Vallet-Regí, M. J. Sayagués, J. González-Calbet, F. García-Sanz, and J. Rivas, Phys. Rev. B 54, 16574 (1996).
[14] D. Kaneko, K. Yamagishi, A. Tsukada, T. Manabe, and M. Naito, Physica C: Superconductivity 469, 936 (2009), proceedings of the 21st International Symposium on Su-

perconductivity (ISS 2008).

[15] D. Li, K. Lee, B. Wang, M. Osada, S. Crossley, H. R. Lee, Y. Cui, Y. Hikita, and H. Y. Hwang, Nature 572, 624 (2019).

[16] M. Osada, B. Y. Wang, B. H. Goodge, K. Lee, H. Yoon, K. Sakuma, D. Li, M. Miura, L. F. Kourkoutis, and H. Y. Hwang, Nano Letters 20, 5735 (2020).

[17] H. Guo, Z. W. Li, L. Zhao, Z. Hu, C. F. Chang, C.-Y. Kuo, W. Schmidt, A. Piovano, T. W. Pi, O. Sobolev, D. I. Khomskii, L. H. Tjeng, and A. C. Komarek, Nature Communications 9, 10.1038/s41467-017-02524-x (2018).

[18] J. Zhang, H. Zheng, Y. Ren, and J. F. Mitchell, Crystal Growth & Design 17, 2730 (2017), https://doi.org/10.1021/acs.cgd.7b00205.

[19] B.-X. Wang, S. Rosenkranz, X. Rui, J. Zhang, F. Ye, H. Zheng, R. F. Klie, J. F. Mitchell, and D. Phelan, Phys. Rev. Materials 2, 064404 (2018).

[20] M. A. Hayward, M. A. Green, M. J. Rosseinsky, and J. Sloan, Journal of the American Chemical Society 121, 8843 (1999), https://doi.org/10.1021/ja991573i.

[21] M. Abbate, G. Zampieri, F. Prado, A. Caneiro, J. M. Gonzalez-Calbet, and M. Vallet-Regi, Phys. Rev. B 65, 155101 (2002).

[22] K. Horiba, R. Eguchi, M. Taguchi, A. Chainani, A. Kikkawa, Y. Senba, H. Ohashi, and S. Shin, Phys. Rev. B 76, 155104 (2007).

[23] M. Golalikhani, Q. Lei, R. U. Chandrasena, L. Kasaei, H. Park, J. Bai, P. Orgiani, J. Ciston, G. E. Sterbinsky, D. A. Arena, P. Shafer, E. Arenholz, B. A. Davidson, A. J. Millis, A. X. Gray, and X. X. Xi, Nature Commu- nications 9, 2206 (2018).

[24] D. Misra and T. K. Kundu, The European Physical Jour- nal B 89, 4 (2016).

[25] A. Malashevich and S. Ismail-Beigi, Phys. Rev. B 92, 144102 (2015).

[26] M. Kotiuga, Z. Zhang, J. Li, F. Rodolakis, H. Zhou, R. Sutarto, F. He, Q. Wang, Y. Sun, Y. Wang, N. A. Aghamiri, S. B. Hancock, L. P. Rokhinson, D. P. Landau, Y. Abate, J. W. Freeland, R. Comin, S. Ramanathan, and K. M. Rabe, Proceedings of the National Academy of Sciences 116, 21992 (2019), https://www.pnas.org/content/116/44/21992.full.pdf.

[27] A. Subedi, SciPost Phys. 5, 20 (2018).

[28] S. Bandyopadhyay, P. Adhikary, T. Das, I. Dasgupta, and T. Saha-Dasgupta, Phys. Rev. B 102, 220502(R) (2020).

[29] A. S. Botana and M. R. Norman, Phys. Rev. X 10, 011024 (2020).

[30] J. Karp, A. S. Botana, M. R. Norman, H. Park, M. Zingl, and A. Millis, Phys. Rev. X 10, 021061 (2020).

[31] S. Ryee, H. Yoon, T. J. Kim, M. Y. Jeong, and M. J. Han, Phys. Rev. B 101, 064513 (2020).

[32] P. Werner and S. Hoshino, Phys. Rev. B 101, 041104(R) (2020).

[33] F. Lechermann, Phys. Rev. B 101, 081110(R) (2020).

[34] Y. Wang, C.-J. Kang, H. Miao, and G. Kotliar, Phys. Rev. B 102, 161118(R) (2020).

[35] G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).

[36] G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).

[37] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Phys. Rev. Lett. 100, 136406 (2008).

[38] V. Singh, U. Herath, B. Wah, X. Liao, A. H. Romero, and H. Park, Computer Physics Communications , 107778 (2020).

[39] N. Marzari and D. Vanderbilt, Phys. Rev. B 56, 12847 (1997).

[40] I. Souza, N. Marzari, and D. Vanderbilt, Phys. Rev. B 65, 035109 (2001).

[41] J. Ruppen, J. Teyssier, O. E. Peil, S. Catalano, M. Gibert, J. Mravlje, J.-M. Triscone, A. Georges, and D. van der Marel, Phys. Rev. B 92, 155145 (2015).

[42] A. Hampel, P. Liu, C. Franchini, and C. Ederer, npj Quantum Materials 4, 5 (2019).

[43] H. Park, A. J. Millis, and C. A. Marianetti, Phys. Rev. B 89, 245133 (2014).

[44] E. A. Nowadnick, J. P. Ruf, H. Park, P. D. C. King, D. G. Schlom, K. M. Shen, and A. J. Millis, Phys. Rev. B 92, 245109 (2015).

[45] G. Gou, I. Grinberg, A. M. Rappe, and J. M. Rondinelli, Phys. Rev. B 84, 144101 (2011).

[46] H. Park, A. J. Millis, and C. A. Marianetti, Phys. Rev. B 90, 235103 (2014).

[47] E. Gull, A. J. Millis, A. I. Lichtenstein, A. N. Rubtsov, M. Troyer, and P. Werner, Rev. Mod. Phys. 83, 349 (2011).

[48] K. Haule, Phys. Rev. B 75, 155113 (2007).

[49] A. Wold, B. Post, and E. Banks, Journal of the American Chemical Society 79, 4911 (1957), https://doi.org/10.1021/ja01575a022.

[50] J. A. Alonso, M. J. Martínez-Lope, J. L. García-Muñoz, and M. T. Fernández-Díaz, Journal of Physics: Con- densed Matter 9, 6417 (1997).

[51] T. Moriga, O. Usaka, T. Imamura, I. Nakabayashi, I. Matsubara, T. Kinouchi, K. Shinichi, and F. Kana- maru, Bulletin of the Chemical Society of Japan 67, 687 (1994).

[52] J. L. García-Muñoz, J. Rodríguez-Carvajal, P. Lacorre, and J. B. Torrance, Phys. B 46, 4414 (1992).

[53] B. Geisler and R. Pentcheva, Phys. Rev. B 101, 165108 (2020).

[54] K. Reuter and M. Scheffler, Phys. Rev. B 65, 035406 (2001).

[55] R. Pentcheva, F. Wendler, H. L. Meyerheim, W. Moritz, N. Jedrecy, and M. Scheffler, Phys. Rev. Lett. 94, 126101 (2005).

[56] N. Mulakaluri, R. Pentcheva, M. Wieland, W. Moritz, and M. Scheffler, Phys. Rev. Lett. 103, 176102 (2009).

[57] M. Hepting, D. Li, C. J. Jia, H. Lu, E. Paris, Y. Tseng, X. Feng, M. Osada, E. Been, Y. Hikita, Y.-D. Chuang, Z. Hussain, K. J. Zhou, A. Nag, M. Garcia-Fernandez, M. Rossi, H. Y. Huang, D. J. Huang, Z. X. Shen, T. Schmitt, H. Y. Hwang, B. Moritz, J. Zaanen, T. P. Devereaux, and W. S. Lee, Nat. Mater. 19, 381 (2020).

[58] E. Z. Kurmaev, R. G. Wilks, A. Moewes, L. D. Finkel- stein, S. N. Shamin, and J. Kuneš, Phys. Rev. B 77, 165127 (2008).

[59] I. Timrov, P. Agrawal, X. Zhang, S. Erat, R. Liu, A. Braun, M. Cococcioni, M. Calandra, N. Marzari, and D. Passerone, Phys. Rev. Research 2, 033265 (2020).

[60] H. Park, R. Nanguneri, and A. T. Ngo, Phys. Rev. B 101, 195125 (2020).

[61] E. Greenberg, I. Leonov, S. Layek, Z. Konopkova, M. P. Pasternak, L. Dubrovinsky, R. Jeanloz, I. A. Abrikosov, and G. K. Rozenberg, Phys. Rev. X 8, 031059 (2018).

[62] I. Leonov, G. K. Rozenberg, and I. A. Abrikosov, npj Computational Materials 5, 10.1038/s41524-019-0225-9 (2019).

[63] A. Valli, H. Das, G. Sangiovanni, T. Saha-Dasgupta, and
K. Held, Phys. Rev. B **92**, 115143 (2015).

# SUPPLEMENTARY MATERIALS

## A. DFT and DFT+U density of states

In Fig. 7, we list the density of states (DOS) for $LaNiO_{3-x}$ with $x$=0, 0.25, 0.5, 0.75, and 1 computed using DFT and DFT+U with non-magnetic, ferromagnetic and G-type antiferromagnetic configurations. For $LaNiO_3$, $LaNiO_{2.75}$ and $LaNiO_{2.5}$ cases, we compare the orbital-resolved DOS with experimental photoemission spectroscopy (PES) spectra[22] as depicted in the shaded region. In all calculations, as the oxygen vacancy level $x$ increases, the La state moves down in energy close to the Fermi energy while the Ni state is slightly shifted below the Fermi energy. The Ni-O hybridization becomes also weaker as the vacancy level evolves. The ground-states of all DFT calculations become metallic as DFT underestimates correlation effects. In DFT+U, ferromagnetic and G-type antiferromagnetic ground states in $LaNiO_{2.5}$ become insulator consistently with the experimental transport property although the non-magnetic ground state is still metallic as the correlation effect is also underestimated.

## B. DFT+DMFT calculation details

The overall procedure of DFT+DMFT as implemented in the DMFTwDFT package[38] is as follows. First, we perform non-magnetic DFT calculations for each structure. Then, we adopt the Wannier90 package[39,40] to obtain maximally localized Wannier functions (MLWFs) as localized orbitals for DMFT. To construct the Wannier orbitals, we take an energy window from -9 eV to +5 eV, with respect to Fermi energies, which basically contains all Ni $3d$ and O $2p$ orbitals. It is also important that the interpolated band structure obtained from MLWFs matches to the original DFT band structure. In Fig. 8, we plot Wannier band structures for $LaNiO_3$, $LaNiO_{2.5}$ and $LaNiO_2$ and compare to DFT band structures. The Wannier bands match to the DFT bands almost perfectly capturing the original band structure in DFT. We applied frozen window in MLWFs construction processes of $LaNiO_2$ and $LaNiO_{2.5}$. For $LaNiO_2$ we set frozen window to be -9 eV $\sim$ -1.56 eV with respect to the Fermi energy. For $LaNiO_{2.5}$ it is -7.9 eV $\sim$ 1.2 eV with respect to the Fermi energy. Without frozen windows setting, the Wannier bands have relatively large discrepancies with DFT bands for $LaNiO_2$ and $LaNiO_{2.5}$.

From the obtained Wannier subspace, we perform the DMFT self-consistent calculation using the continuous-time quantum Monte Carlo as an impurity solver. We use 18$\times$18$\times$18 $k-$points which are denser than the DFT $k-$points while doing the DMFT calculations. To minimize the off-diagonal component of hybridization functions in DMFT, we adopt the rotated axis for constructing MLWFs which is aligned to the bonding direction of the local Ni octahedron sites. To avoid the double counting of the Coulomb interaction taken in DFT+DMFT, we also used the modified double counting correction energy (DC_type = 1 in the DMFTwDFT package) with the parameter $\alpha=0.2$, which is given by

$$
E^{D C}=\frac{(U-\alpha)}{2} \cdot N_{d} \cdot\left(N_{d}-1\right)-\frac{J}{4} \cdot N_{d} \cdot\left(N_{d}-2\right) \tag{4}
$$

where $U$ is the Hubbard interaction, $J$ is the Hund's coupling, and $N_d$ is the $d-$occupancy.

## C. Total energies of $LaNiO_{3-x}$

In Table VI, we list total energies of $LaNiO_3$, $LaNiO_{2.75}$, $LaNiO_{2.5}$, $LaNiO_{2.25}$, and $LaNiO_2$ obtained from DFT and DFT+U calculations by relaxing structures with different magnetism including PM, FM, and G-type AFM. The energy difference between FM and AFM for each structure was given and explained in the main text.

![](./images/867756106598842495_7.jpg)

FIG. 7: Orbital-resolved density of states calculated using the DFT method for $LaNiO_3$, $LaNiO_{2.75}$, $LaNiO_{2.5}$, $LaNiO_{2.25}$ and $LaNiO_2$ with (a) non-magnetic, (b) ferromagnetic, and (c) antiferromagnetic orderings, as well as using the DFT+U method with (d) non-magnetic, (e) ferromagnetic, (f) antiferromagnetic orderings. The shaded region is taken from previous experimental work[22]. Sub-figures with * in label indicates the ground state converged to zero magnetic moment.

![](./images/867756106598842495_8.jpg)

FIG. 8: Comparison of the Wannier band structures of Ni $3d$ and O $2p$ orbitals with the DFT band structures for (a) LaNiO₃, (b) LaNiO₂.₅, and (c) LaNiO₂.

TABLE VI: Total energies [eV] of LaNiO₃, LaNiO₂.₇₅, LaNiO₂.₅, LaNiO₂.₂₅, and LaNiO₂

<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th colspan="3">DFT</th>
      <th colspan="3">DFT+U</th>
    </tr>
    <tr>
      <th>PM</th>
      <th>FM</th>
      <th>AFM</th>
      <th>PM</th>
      <th>FM</th>
      <th>AFM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LaNiO₃</td>
      <td>-36.041</td>
      <td>-36.041ᵃ</td>
      <td>-36.041ᵃ</td>
      <td>-33.852</td>
      <td>-34.175</td>
      <td>-33.834</td>
    </tr>
    <tr>
      <td>LaNiO₂.₇₅</td>
      <td>-34.437</td>
      <td>-34.442</td>
      <td>-34.438</td>
      <td>-32.160</td>
      <td>-32.650</td>
      <td>-32.610</td>
    </tr>
    <tr>
      <td>LaNiO₂.₅</td>
      <td>-32.678</td>
      <td>-32.723</td>
      <td>-32.713</td>
      <td>-30.460</td>
      <td>-31.098</td>
      <td>-31.139</td>
    </tr>
    <tr>
      <td>LaNiO₂.₂₅</td>
      <td>-30.950</td>
      <td>-30.953</td>
      <td>-30.951</td>
      <td>-28.664</td>
      <td>-29.124</td>
      <td>-29.056</td>
    </tr>
    <tr>
      <td>LaNiO₂</td>
      <td>-29.233</td>
      <td>-29.233ᵃ</td>
      <td>-29.213</td>
      <td>-26.842</td>
      <td>-27.396</td>
      <td>-27.447</td>
    </tr>
  </tbody>
</table>

ᵃ Relaxation converged to 0 magnetic momentum.