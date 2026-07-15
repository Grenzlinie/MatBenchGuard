# Controlling Na diffusion by rational design of Si-based layered architectures

Vadym V. Kulish, $^{*a}$ Oleksandr I. Malyi, $^{b}$ Man-Fai Ng, $^{c}$ Zhong Chen, $^{d}$ Sergei Manzhos $^{*b}$ and Ping Wu $^{*a}$

By means of density functional theory, we systematically investigate the insertion and diffusion of Na and Li in layered Si materials (polysilane and H-passivated silicene), in comparison with bulk Si. It is found that Na binding and mobility can be significantly facilitated in layered Si structures. In contrast to the Si bulk, where Na insertion is energetically unfavorable, Na storage can be achieved in polysilane and silicene. The energy barrier for Na diffusion is reduced from 1.06 eV in the Si bulk to 0.41 eV in polysilane. The improvements in binding energetics and in the activation energy for Na diffusion are attributed to the large surface area and available free volume for the large Na cation. Based on these results, we suggest that polysilane may be a promising anode material for Na-ion and Li-ion batteries with high charge-discharge rates.

## I. Introduction
Advanced energy storage is essential for the realization of many emerging technologies, such as hybrid electric vehicles (HEVs) and grid integration of renewable sources (e.g. solar and wind). $^{1}$ Li-ion batteries are currently the most popular electrochemical energy storage devices, but their future long-term and large-scale application faces some serious concerns, such as limited lithium resources and their increasing price. $^{2}$ It is, therefore, desirable to develop rechargeable batteries based on abundant and cheaper alternatives. In this respect, sodium-ion (Na-ion) batteries represent an attractive solution for the applications in smart electric grids that store clean renewable energy. The production of Na is relatively simple and clean, which makes Na-ion batteries considerably more environment-friendly. Based on the above motivation and a growing market for electricity storage, Na-ion batteries receive growing scientific attention. $^{3-9}$ However, despite the significant advances in the cathode research with many suitable cathode compounds identified, $^{10-12}$ the knowledge of prospective anode materials is still limited.

Interestingly, the reactivity of sodium and lithium with anode materials is quite different despite their close chemical properties. For instance, silicon has been a particularly attractive and actively-studied anode material for Li-ion batteries due to its ultra-high specific capacity $(\sim 4200$ mA h g$^{-1}$, about ten times larger than that of the conventional graphite anode) and large abundance. Remarkable performance has been achieved for Si nanoparticles, $^{13}$ nanowires, $^{14,15}$ nanosheets, $^{16,17}$ and composite materials. $^{18-20}$ However, recent studies showed that crystalline Si is not as attractive as an anode material for Na-ion batteries. $^{21-23}$ Theoretical studies show that although the formation of the NaSi compound is thermodynamically favorable, Na insertion into crystalline Si is limited. These studies indicate that the limited Na insertion arises, in particular, from the slow diffusion at low Na concentrations. $^{23-25}$ The main challenges are associated with the larger size of Na as compared to Li (ionic radii of $0.98\ \mathring{A}$ and $0.68\ \mathring{A}$, respectively), $^{4}$ resulting in both slow bulk diffusion and prohibitive insertion. Since a Na ion is about 44% larger than a Li ion, Si and some other host materials with good potential for Li storage do not have sufficiently big interstitial space to accommodate Na ions. This suggests that the usual diamond bulk structure of silicon may not be suitable for Na-ion batteries. $^{22,23}$ Much effort has been made to explore new anode materials for Na-ion batteries, such as tin, antimony, phosphorus, or oxides. $^{26-30}$ Identification of suitable anode materials and further understanding of Na diffusion mechanisms have become critical challenges for further development of Na-ion batteries.

Here, we suggest that the challenges of poor Na kinetics can be efficiently tackled by an alternative approach – rational design of Si-based anode morphology. It is known that fast kinetics and high capacity can be achieved in battery materials by introducing porosity and large void spaces, as demonstrated

---
$^{a}$ Singapore University of Technology and Design, 20 Dover Drive, Singapore 138682, Singapore. E-mail: wuping@sutd.edu.sg, vadym_kulish@sutd.edu.sg
$^{b}$ Department of Mechanical Engineering, National University of Singapore, Singapore 117576, Singapore. E-mail: mpemanzh@nus.edu.sg
$^{c}$ Institute of High Performance Computing, 1 Fusionopolis Way, #16-16 Connexis, Singapore 138632, Singapore
$^{d}$ School of Materials Science and Engineering, Nanyang Technological University, 50 Nanyang Avenue, Singapore 639798, Singapore

in nanotubes and porous/yolk-shell structures. $^{31-33}$ Besides, improvements in charge-discharge rates can be achieved in layered materials and ultra-thin nanosheets, where lithium storage mainly takes place on the surfaces (in a pseudo- capacitive manner), maintaining rapid Li surface diffusion and electron transport. $^{34}$

Polysilane and silicene are novel materials belonging to a broad family of layered 2D nanomaterials. $^{35,36}$ Polysilane $(Si_{6}H_{6})$ has a layered structure, composed of corrugated H-terminated Si(111) planes with a hexagonal atomic arrangement. $^{37-39}$ Moreover, the polysilane precursor can be further exfoliated into single-layer Si nanosheets by a solution method as demonstrated by Nakano et al. $^{39-42}$ Pristine or passivated single-layer Si (silicene) has become the subject of active research, both theoretically and experimen- tally, since it exhibits a graphene-like band structure with the charge carriers behaving as massless Dirac fermions, quantum spin Hall effect (QSHE) and other attractive properties. $^{43-47}$ Note that a layered structure of Ge (i.e. germanane) has been synthesized for the first time in 2013, $^{48}$ promising a bright future for this class of materials. $^{49}$ Importantly, polysilane has been successfully tested as an anode material in Li-ion batteries, demonstrating a first charge capacity of $1677 mA h g^{-1}$ and good capacity retention after10 cycles. $^{50,51}$ The diffusion coefficients of Li during the first charge in the layered polysilane and Si powder electrodes wereestimated to be $2.3 \times 10^{-9}$ and $4.9 \times 10^{-10} ~cm^{2} ~s^{-1}$ , respectively. $^{51}$  Moreover, the specific capacity and reversibility of a polysilane anode can be improved by further modification, such as carboncoating. $^{50}$ However, there have been no studies on layered $Si$  materials for sodium-ion batteries so far.

In this work, we use first-principles calculations with van der Waals corrections to study energetics, electronic properties, and diffusion of $Na$ atoms in layered $Si$ nanomaterials. To gain a better understanding of interactions of alkali atoms with the Si host, we compare $Na$ and $Li$ insertion in silicene/polysilane with that in bulk Si. $^{23}$ We find that, in contrast to the Si bulk where $Na$ insertion is energetically unfavorable, $Na$ storage can be achieved in polysilane and silicene. The energy barrier for $Na$ diffusion is reduced from $1.06 eV$ in the Si bulk to $0.41 eV$ in polysilane. The improvements are attributed to an unusual layered structure of polysilane which provides large interstitial sites and channels for $Na$ atoms. Although our study does not consider possible evolution of the layered structures at higher states of charge (for instance, the amorphization of the layered polysilane by insertion of $Li$ (and possibly $Na$ ) was reported at high concentrations), $^{52}$ the obtained results can be useful to explain the initial stage of $Na / Li$ insertion which was identified as the important rate-limiting step for the Na-ion/Li-ion bat- teries. $^{16,21,25,53,54}$ Based on our study, we suggest that polysilane may be a promising anode material for the Na-ion batteries.

## Il. Computational methods
Our calculations are performed within the density-functional theory (DFT) framework, as implemented in the QuantumEspresso package. $^{55}$ The exchange-correlation functional is approximated by the generalized gradient approximation(GGA) $^{56}$ using the Perdew-Burke-Ernzerhof (PBE) functional. $^{57}$  Ultrasoft pseudopotentials of the Rappe-Rabe-Kaxiras-Joanno- poulos type are used for the description of electron-ion inter- actions. $^{58}$ The kinetic-energy cutoffs for valence electron wavefunctions and the charge density are set to 37 Ry and370 Ry, respectively. The Brillouin zone is sampled by $5 \times 5 \times 5$ , $5 \times 5 \times 5$ , and $5 \times 5 \times 1$ Monkhorst-Pack $k$ -point grids for the Si bulk, polysilane, and silicene, respectively. All structures are treated with periodic boundary conditions. A 64-atom cubic cell is used to model bulk Si. We use $11.52 \times 11.52 \times 10.9 \AA$ and $11.52 \times 11.52 \times 20 \AA$ supercells to model polysilane and silicene, respectively. In the latter case, a vacuum layer of greater than $15 \AA$ is added to the supercell to prevent the interaction of single-layer silicene with its periodic images. These supercell sizes have been shown to produce reliable binding energies and migration barriers in the previous studies on the Si bulk $^{23,24,59-62}$ and surfaces. $^{54,63,64}$ The optimized structures are obtained by relaxing all atomic positions using the Broyden-Fletcher-Goldfarb-Shanno quasi-Newton algo- rithm until all forces are smaller than $0.01 eV \AA^{-1}$ .

The $Na / Li$ binding energy per $Na / Li$ atom $(E_{b})$ is defined asfollows:
$$E_{\mathrm{b}}(\mathrm{Na} / \mathrm{Li})=[E(\mathrm{Na} / \mathrm{Li}-\mathrm{Si})-E(\mathrm{Si})-n E(\mathrm{Na} / \mathrm{Li})] / n \quad(1)$$
 where $E(Na / Li-Si), E(Si)$ , and $E(Na / Li)$ are the total energies of the Si host with $n$ inserted $Na / Li$ atoms, pure $Si$ host, and a single $Na / Li$ atom (in a large vacuum box), respectively. Accord ing to this equation, $E_{b}<0$ represents a favorable interaction between $Li / Na$ and $Si$ , while $E_{b}>0$ indicates that the $Li / Na$  insertion is not energetically favorable.

Activation barriers for $Li$ diffusion are calculated using the climbing-image nudged elastic band (CI-NEB) method. $^{65}$ In this method, a set of images (i.e. geometric configurations of the system) is constructed to describe a diffusion pathway. The initial guess of the diffusion trajectory is generated by linear interpola- tions between the initial and final points of the pathway. The NEB method has been used successfully in the previous studies to determine Li diffusion rates in silicon structures, $^{16,23,25,54,66}$ aswell as various electrode materials. $^{63,67-71}$

## Ill. Results and discussion
### Crystal structures of bulk Si, layered polysilane and single-layer silicene
The calculated lattice parameters and structural properties of bulk silicon, layered polysilane and single-layer silicene are reported in Table 1. For each case, the lattice vectors and internal atomic coordinates were fully optimized. The opti- mized lattice parameter of bulk Si is $5.46 \AA$ , which is in good agreement with the experimental value of $5.43 \AA$ , and the average $Si-Si$ bond length is $2.35 \AA$ .

Polysilane $(Si_{6}H_{6})$ has a layered structure, composed of corrugated H-terminated Si(111) planes (Fig. 1a). Within the Si layers, each $Si$ atom is bonded to three neighboring $Si$ atoms,

<table>
<caption>Table 1 Structural properties of single-layer H-passivated silicene, layered polysilane and bulk silicon</caption>
<thead>
<tr>
<th colspan="2">Method</th>
<th>$a$ (Å)</th>
<th>$d$ (Å) (interlayer spacing)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Silicene</td>
<td>PBE</td>
<td>3.84</td>
<td>—</td>
</tr>
<tr>
<td rowspan="3">Polysilane</td>
<td>PBE</td>
<td>3.84</td>
<td>6.1</td>
</tr>
<tr>
<td>PBE + vdW</td>
<td>3.84</td>
<td>5.45</td>
</tr>
<tr>
<td>Exp.$^{a}$</td>
<td>3.83</td>
<td>5.5</td>
</tr>
<tr>
<td rowspan="2">Bulk silicon</td>
<td>PBE</td>
<td>5.46</td>
<td>—</td>
</tr>
<tr>
<td>Exp.</td>
<td>5.43</td>
<td>—</td>
</tr>
</tbody>
</table>

$^{a}$ Ref. 37

forming a honeycomb geometry. The fourth Si bond, perpendicular to the (111) plane, is saturated by H. The optimized Si-Si bond lengths are 2.36 Å, and Si-H bond lengths are 1.50 Å. The adjacent Si(111) layers in polysilane are bound to each other by weak van der Waals (vdW) forces. It is known that PBE calculations are usually unable to describe weak dispersive interactions between the layers, resulting in overestimated out-plane lattice parameters (as has been demonstrated for graphite, MoS$_2$ and BN).$^{72}$ The effect of vdW interactions in polysilane is taken into account by using the semi-empirical correction scheme of Grimme (DFT-D), which has been proven to describe successfully the structure of layered materials.$^{73}$ Results obtained using PBE and PBE + vdW techniques are compared in Table 1. The PBE calculations produce an overestimated interlayer spacing of 6.1 Å (see Fig. 1a). In contrast, PBE + vdW calculations show an optimal interlayer spacing of 5.45 Å, close to the experimental value of 5.5 Å.$^{37}$ The in-plane lattice parameter, governed mainly by strong covalent interactions between Si atoms, is reproduced with a good accuracy by both PBE and PBE + vdW methods, $a = 3.84$ Å.

A unique feature of silicene, a single-layer Si honeycomb structure, is its low-dimensional buckling distortion, as shown in Fig. 1b. In contrast to graphene, the $\pi$-$\pi$ overlap in silicene is very weak due to the increased interatomic distance. The poor $\pi$ bonding leads to an unstable planar structure, but silicene can gain extra stability by buckling.$^{74,75}$ The calculated sum of the bond angles at each Si atom in silicene is $324^\circ$, which is close to the idealized value of $328^\circ$ for the sp$^3$ tetrahedral configuration. Therefore, H-passivated silicene is expected to combine beneficial properties of single-layer materials ($i.e.$ high surface area without dangling bonds) and a tetrahedral local configuration, which is more natural and stable in silicon. Experimentally, single-layer H-passivated silicene has been derived from polysilane by the exfoliation method.$^{39-41,76}$

Due to experimental availability and stability, we focus on H-passivated silicene in this study. In the following discussion, we refer to layered polysilane as "polysilane" and single-layer H-passivated silicene as "silicene".

![](./images/813168141587709953_1.jpg)

Fig. 1 Crystal structures of (a) layered polysilane and (b) single-layer silicene. (c) Top view and typical adsorption sites (hollow (H), top (T) and bridge (B)) in polysilane and silicene.

## Na and Li insertion in bulk Si

Before we address Na insertion in layered Si nanomaterials, we first examine the insertion properties of Na and Li atoms in the Si bulk crystal as a reference. We perform structure optimization starting from different initial positions of the alkali atom inside a 64-atom Si diamond cell. The calculated binding energies and the nearest Na/Li-Si distances are summarized in Table 2. Both Na and Li energetically favor a tetrahedral interstitial configuration (Td, see Fig. 2a) with four nearest Si neighbors inside the bulk Si crystal, in agreement with experimental studies.$^{77}$ However, we find significant differences in the binding energies of Na and Li. The Li binding energy is negative ($-1.41$ eV, consistent with recent theoretical calculations$^{22,57}$), denoting favorable interaction between Li and the Si bulk.

In contrast, the binding energy of Na is positive ($+0.60$ eV), indicating that Na insertion in bulk Si is not energetically feasible, consistent with recent studies.$^{23}$ The large difference in binding energies of Na and Li is a direct consequence of a much greater stress/strain associated with the Na insertion.$^{24}$ Since Na has a larger atomic radius than Li, its insertion leads to larger displacements of neighboring Si atoms ($0.15$ vs. $0.08$ Å for Na and Li, respectively). We also find a smaller charge transfer in the Na-Si system as compared with Li-Si ($+0.75|e|$ and $+0.84|e|$ for Bader charges on Na and Li atoms at Td sites, respectively). Large deformations and less active charge transfer may be responsible for the unfavorable Na insertion in the bulk Si crystal.

Besides insertion energetics, slow Na diffusion in bulk Si would seriously hinder its application in Na-ion batteries, as suggested in a recent study.$^{23}$ Single Na atom diffusion in the Si bulk occurs in the form of jumps between neighboring Td sites

<table>
<caption>Table 2 Li and Na binding energies, nearest Li-Si and Na-Si distances and Bader charges in the Si bulk, polysilane and silicene</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="3">Li</th>
<th colspan="3">Na</th>
</tr>
<tr>
<th>$E$ (eV)</th>
<th>$d_{\text{Li-Si}}$ (Å)</th>
<th>$q$ ($|e|$)</th>
<th>$E$ (eV)</th>
<th>$d_{\text{Na-Si}}$ (Å)</th>
<th>$q$ ($|e|$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bulk</td>
<td>$-1.41$</td>
<td>2.45</td>
<td>$+0.84$</td>
<td>$+0.60$</td>
<td>2.52</td>
<td>$+0.75$</td>
</tr>
<tr>
<td>Polysilane</td>
<td>$-1.01$</td>
<td>3.25</td>
<td>$+0.91$</td>
<td>$-0.57$</td>
<td>3.34</td>
<td>$+0.86$</td>
</tr>
<tr>
<td>Silicene</td>
<td>$-0.90$</td>
<td>2.63</td>
<td>$+0.88$</td>
<td>$-0.32$</td>
<td>3.09</td>
<td>$+0.79$</td>
</tr>
</tbody>
</table>

![](./images/813168141587709953_2.jpg)

Fig. 2 (a, b) Stable Na/Li insertion sites in bulk Si: (a) tetrahedral (Td), and (b) hexagonal (Hex). (c) Energy profile of the (Td → Hex → Td) diffusion path in the Si bulk.

through the Hex intermediate. The calculated barrier for Na diffusion (1.06 eV) is much larger compared to that for Li diffusion (0.61 eV).

## Na and Li insertion in layered polysilane and single-layer silicene

The above challenges can be tackled by rational engineering of anode morphology and structure. We first examine possible sites for the Na and Li insertion in the layered structure of polysilane. Our calculations show that both Na and Li prefer the position just above the center of the $Si_6$ hexagonal ring, called the hollow site (H, see Fig. 1c). Such behavior is typical for the ionically bound impurities which usually prefer adsorption sites of high coordination on semiconductor surfaces. $^{78-80}$ Importantly, we find that both Na and Li have negative binding energies equal to -0.57 and -1.01 eV, respectively. This implies that Na insertion in polysilane is energetically favorable, which is an important advantage over the Si bulk. The nearest Na-Si distances in layered polysilane are much larger than in the Si bulk (3.34 Å vs. 2.52 Å) providing more interstitial space and efficient stress relaxation. The structural distortions caused by Na insertion in polysilane are found to be small. For instance, the interlayer distance changes only by $\sim$2% upon Na insertion (corresponding to the stoichiometry $Na_1Si_{12}H_{12}$ with the supercell used here). This differs from the alkali-intercalated graphite, where a large Li-driven interlayer shift ($\sim$10.5% in $LiC_6$) can be observed during Li-ion battery cycling. $^{81}$ This result suggests that good structural stability and reversibility upon cycling may be achieved in layered polysilane anodes.

When layered polysilane is exfoliated into single-layers, there are two representative adsorption sites on the H-passivated silicene surface, namely, the hollow site above the center of the $Si_6$ hexagon (H) and the top site above the Si atom (T) (Fig. 1c). Both sites have nearly equal Na binding energies (difference around 0.04-0.05 eV). Importantly, the Na binding energy in silicene is negative (Table 2), denoting energetically favorable Na adsorption, similar to that in polysilane. We note that Na-host and Li-host interactions are enhanced in layered polysilane as compared with single-layer silicene. This is a direct sequence of a stronger Coulomb interaction and charge transfer between adjacent Si layers and the Na/Li atom. For instance, a Bader charge analysis shows charges of +0.86 and +0.79$|e|$ on the Na atom in polysilane and silicene, respectively. Similar observations were reported for Li-graphene systems, $^{82,83}$ where it was concluded that the weakened Li-graphene interaction may result in the formation of metal clusters and deactivation of anode material. Hence, similar to the single layer graphene/graphite, silicene is expected to have a smaller storage capacity as compared with layered polysilane.

## Electronic structure

The binding mechanism between a Na atom and the layered Si hosts is examined via electronic structure analysis. The calculated density of states (DOS, see Fig. 3a) suggests that pristine layered polysilane is a semiconductor with a band gap of 2.10 eV, in fair agreement with previous theoretical studies. $^{38,84}$ Note that PBE calculations usually underestimate the band gap, as in the

![](./images/813168141587709953_3.jpg)

Fig. 3 Density of states of (a) pristine layered polysilane and (b) Na-polysilane. (c) Partial density of states of inserted Na atoms in layered polysilane. The Fermi level is shown by dotted lines. The origin is at the valence band maximum of the pristine structure.

case of bulk Si. The insertion of Na atoms does not significantly change the overall DOS of the layered polysilane host (Fig. 3b). The adsorbed Na atom transfers its partial charge to Si but does not create an extra level inside the band gap. Na makes two main contributions to the total DOS: one is located deep in the valence band while the other is around the Fermi level in the conduction band as shown in Fig. 3c. Due to the charge transfer from Na to polysilane, the Fermi level is shifted to the bottom of the conduction band. Although the pristine polysilane host is a semiconductor, the Na-inserted polysilane has electronic states at the Fermi level. Insertion should therefore lead to an improved electron conductivity of the polysilane anode which is beneficial for battery application. This finding is in good agreement with the experimental work of McDowell *et al.*, which showed that single Si nanowires in the lithiated state exhibit conductivities two to three orders of magnitude higher than those in the pristine (delithiated) state.⁸⁵ In order to estimate the amount of charge transfer, we performed a Bader charge analysis based on integration of the charge density over a grid in real space.⁸⁶ Our calculations suggest that Na and Li atoms transfer 0.86 and $0.91|e|$ to the polysilane host, respectively. These findings suggest that the Na atom becomes almost completely ionized by the transfer of its 3s valence electron to polysilane, and the bonding between an alkali atom and the polysilane host is mainly ionic with a small part of covalence (alternatively, it may be treated as covalent polar).

Na diffusion

Fast Na diffusion is of key importance for the performance of Na-ion batteries since it determines charge–discharge rates of batteries.⁸⁷,⁸⁸ In certain applications of rechargeable batteries, such as grid/bulk storage, high rate capability is more critical than energy capacity.⁴ In the dilute regime, the diffusivity is proportional to the activation energy (*i.e.* energy barrier) according to the classical Arrhenius equation:

$$
D \propto \exp\left(-\frac{E_{\text{barrier}}}{k_{\text{B}}T}\right) \tag{2}
$$

where $k_{\text{B}}$ is the Boltzmann constant and $T$ is the temperature. Accordingly, the intrinsic Na diffusivity in the given anode material can be evaluated by calculating the energy barrier ($E_{\text{barrier}}$) using theoretical techniques, such as the nudged elastic band (NEB) method.⁶⁵

As shown in the above discussion, Na diffusion inside the bulk Si crystal encounters a large energy barrier of >1 eV, which may represent a significant rate limitation. It is, therefore, desirable to examine whether Na diffusion can be facilitated by using layered structures of silicon. In polysilane, the diffusion of alkali atoms occurs in the empty interstitial space between the adjacent layers by moving from one stable hollow (H) site to another. We find that the transition state for the diffusion lies at a high-symmetry point where Na is located between two hydrogen atoms. At this site, the alkali atom is located above the mid-point of the Si–Si bond (B, see Fig. 1c). The calculated diffusion path (H → B → H) and the corresponding energy profile are shown in Fig. 4. The computed energy barrier for Na diffusion in polysilane is only 0.41 eV, which is a significant improvement over Na diffusion in bulk Si (1.06 eV). Similarly, we find that the energy barrier for Li diffusion is reduced in polysilane as well (0.34 eV in polysilane *vs.* 0.56 eV in the bulk Si). The reduced activation energy for Na diffusion will lead to improved diffusion rates according to eqn (2) and, hence, charge–discharge rates of the batteries. This trend compares well with the available experimental measurements of Li diffusion coefficients in layered polysilane and the Si powder.⁵¹

We then investigate how the exfoliation of polysilane into single-layers affects Na and Li diffusion rates. The diffusion of Na on the surface of single-layer silicene occurs in the form of jumps between the neighboring hollow surface sites as shown in Fig. 5. Our calculations suggest that the diffusion path goes through an intermediate state located on top of a Si atom, *i.e.* a T surface site. The calculated energy barrier for Na diffusion on silicene is only 0.12 eV, which is much lower than in the Si bulk (1.06 eV) and lower than in polysilane (0.41 eV). The calculated energy barrier for Li diffusion on silicene is 0.21 eV. Interestingly, the surface diffusion barrier in silicene decreases with cation size ($E_{\text{barrier}}^{\text{surface}}(\text{Na}) < E_{\text{barrier}}^{\text{surface}}(\text{Li})$), similar to the diffusion of alkali atoms (*e.g.* Li, Na and K) on graphene.⁸⁰ This trend is opposite to those in the case of bulk Si and polysilane where Li has the lowest migration barrier.

These results suggest that alkali atom diffusion in polysilane and silicene is mainly governed by the following factors: (1) in

![](./images/813168141587709953_4.jpg)

Fig. 4 (a) Side view and (b) corresponding energy barrier for the Na diffusion path (H → B → H) in layered polysilane.

![](./images/813168141587709953_5.jpg)

![](./images/813168141587709953_6.jpg)

Fig. 5 (a) Top view and (b) corresponding energy barrier for the Na diffusion path (H → T → H) in single-layer H-passivated silicene.

polysilane and the bulk Si, diffusion is controlled by the available interstitial space and free volume, which promotes migration of smaller Li atoms; (2) on the silicene surface, Li atoms experience a stronger potential than Na. Li experiences a more corrugated potential in the hexagons of silicene due to its smaller ionic radius and smaller Li-silicene distance compared with Na (Table 2). As the alkali atom radius increases (from Li to Na), the distance to the surface increases, and the effect of the corrugation of the silicene is reduced. Therefore, the surface diffusion barrier is correlated with atomic radius, promoting fast Na diffusion.

## IV. Conclusions

We have performed first-principles calculations on layered forms of silicon - polysilane and silicene - as potential anode materials for Na-ion batteries. Bulk Si has been previously identified as not a suitable material for Na-ion batteries due to unfavorable Na insertion energetics and slow Na kinetics. However, we have shown that by rational design of Si-based structure and morphology, the above challenges can be efficiently resolved. In particular, we have shown that:

(1) Na insertion in layered polysilane and silicene is exothermic with negative (favorable) binding energies of a Na atom of -0.57 and -0.32 eV, respectively (in contrast to the unfavorable Na binding energy of +0.60 eV in bulk Si).

(2) Although the pristine layered polysilane host is a semiconductor, the Na-inserted polysilane has electronic states at the Fermi level. This should lead to an improved electron conductivity of the polysilane anode which is beneficial for battery application.

(3) The diffusion barrier for Na migration has been reduced from 1.06 eV in the Si bulk to 0.41 eV in layered polysilane suggesting much facilitated Na diffusion rates.

The above improvements can be attributed to a beneficial architecture of polysilane and silicene. Due to the large surface area, large available free volume, and low activation energy for Na diffusion, layered polysilane may be a promising anode material for Na-ion batteries. We expect that our theoretical results will inspire further experimental studies.

## Notes and references

1 S. Chu and A. Majumdar, *Nature*, 2012, **488**, 294-303.
2 J. M. Tarascon, *Nat. Chem.*, 2010, **2**, 510.
3 B. L. Ellis and L. F. Nazar, *Curr. Opin. Solid State Mater. Sci.*, 2012, **16**, 168-177.
4 V. Palomares, P. Serras, I. Villaluenga, K. B. Hueso, J. Carretero-Gonzalez and T. Rojo, *Energy Environ. Sci.*, 2012, **5**, 5884-5901.
5 S. W. Kim, D. H. Seo, X. H. Ma, G. Ceder and K. Kang, *Adv. Energy Mater.*, 2012, **2**, 710-721.
6 M. D. Slater, D. Kim, E. Lee and C. S. Johnson, *Adv. Funct. Mater.*, 2013, **23**, 947-958.
7 S. Y. Hong, Y. Kim, Y. Park, A. Choi, N.-S. Choi and K. T. Lee, *Energy Environ. Sci.*, 2013, **6**, 2067-2081.
8 H. L. Pan, Y. S. Hu and L. Q. Chen, *Energy Environ. Sci.*, 2013, **6**, 2338-2360.
9 V. Palomares, M. Casas-Cabanas, E. Castillo-Martinez, M. H. Han and T. Rojo, *Energy Environ. Sci.*, 2013, **6**, 2312-2337.
10 B. Koo, S. Chattopadhyay, T. Shibata, V. B. Prakapenka, C. S. Johnson, T. Rajh and E. V. Sheychenko, *Chem. Mater.*, 2013, **25**, 245-252.
11 Y. L. Cao, L. F. Xiao, W. Wang, D. W. Choi, Z. M. Nie, J. G. Yu, L. V. Saraf, Z. G. Yang and J. Liu, *Adv. Mater.*, 2011, **23**, 3155-3160.
12 H. Kim, I. Park, D. H. Seo, S. Lee, S. W. Kim, W. J. Kwon, Y. U. Park, C. S. Kim, S. Jeon and K. Kang, *J. Am. Chem. Soc.*, 2012, **134**, 10369-10372.
13 H. Kim, M. Seo, M. H. Park and J. Cho, *Angew. Chem., Int. Ed.*, 2010, **49**, 2146-2149.
14 C. K. Chan, H. L. Peng, G. Liu, K. McIlwrath, X. F. Zhang, R. A. Huggins and Y. Cui, *Nat. Nanotechnol.*, 2008, **3**, 31-35.
15 X. H. Liu, H. Zheng, L. Zhong, S. Huang, K. Karki, L. Q. Zhang, Y. Liu, A. Kushima, W. T. Liang, J. W. Wang, J.-H. Cho, E. Epstein, S. A. Dayeh, S. T. Picraux, T. Zhu, J. Li, J. P. Sullivan, J. Cumings, C. Wang, S. X. Mao, Z. Z. Ye, S. Zhang and J. Y. Huang, *Nano Lett.*, 2011, **11**, 3312-3318.
16 V. V. Kulish, O. I. Malyi, M. F. Ng, P. Wu and Z. Chen, *RSC Adv.*, 2013, **3**, 4231-4236.
17 Z. Lu, J. Zhu, D. Sim, W. Zhou, W. Shi, H. H. Hng and Q. Yan, *Chem. Mater.*, 2011, **23**, 5293-5295.
18 L. Su, Z. Zhou and M. Ren, *Chem. Commun.*, 2010, **46**, 2590-2592.

19 Y. Wen, Y. Zhu, A. Langrock, A. Manivannan, S. H. Ehrman and C. Wang, *Small*, 2013, **9**, 2810-2816.

20 V. V. Kulish, M.-F. Ng, O. I. Malyi, P. Wu and Z. Chen, *RSC Adv.*, 2013, **3**, 8446-8453.

21 S. Komaba, Y. Matsuura, T. Ishikawa, N. Yabuuchi, W. Murata and S. Kuze, *Electrochem. Commun.*, 2012, **21**, 65-68.

22 V. L. Chevrier and G. Ceder, *J. Electrochem. Soc.*, 2011, **158**, A1011-A1014.

23 O. I. Malyi, T. L. Tan and S. Manzhos, *Appl. Phys. Express*, 2013, **6**, 027301.

24 F. Legrain, O. I. Malyi and S. Manzhos, *Solid State Ionics*, 2013, **253**, 157-163.

25 O. Malyi, V. V. Kulish, T. L. Tan and S. Manzhos, *Nano Energy*, 2013, **2**, 1149-1157.

26 S. Hariharan, K. Saravanan, V. Ramar and P. Balaya, *Phys. Chem. Chem. Phys.*, 2013, **15**, 2945-2953.

27 A. Rudola, K. Saravanan, C. W. Mason and P. Balaya, *J. Mater. Chem. A*, 2013, **1**, 2653-2662.

28 Y. L. Cao, L. F. Xiao, M. L. Sushko, W. Wang, B. Schwenzer, J. Xiao, Z. M. Nie, L. V. Saraf, Z. G. Yang and J. Liu, *Nano Lett.*, 2012, **12**, 3783-3787.

29 A. Darwiche, C. Marino, M. T. Sougrati, B. Fraisse, L. Stievano and L. Monconduit, *J. Am. Chem. Soc.*, 2012, **134**, 20805-20811.

30 W. Wang, C. J. Yu, Y. J. Liu, J. G. Hou, H. M. Zhu and S. Q. Jiao, *RSC Adv.*, 2013, **3**, 1041-1044.

31 N. Liu, H. Wu, M. T. McDowell, Y. Yao, C. Wang and Y. Cui, *Nano Lett.*, 2012, **12**, 3315-3321.

32 M.-H. Park, M. G. Kim, J. Joo, K. Kim, J. Kim, S. Ahn, Y. Cui and J. Cho, *Nano Lett.*, 2009, **9**, 3844-3847.

33 S. Wenzel, T. Hara, J. Janek and P. Adelhelm, *Energy Environ. Sci.*, 2011, **4**, 3342-3345.

34 J. Liu and X.-W. Liu, *Adv. Mater.*, 2012, **24**, 4097-4111.

35 S. Z. Butler, S. M. Hollen, L. Cao, Y. Cui, J. A. Gupta, H. R. Gutiérrez, T. F. Heinz, S. S. Hong, J. Huang, A. F. Ismach, E. Johnston-Halperin, M. Kuno, V. V. Plashnitsa, R. D. Robinson, R. S. Ruoff, S. Salahuddin, J. Shan, L. Shi, M. G. Spencer, M. Terrones, W. Windl and J. E. Goldberger, *ACS Nano*, 2013, **7**, 2898-2926.

36 M. Xu, T. Liang, M. Shi and H. Chen, *Chem. Rev.*, 2013, **113**, 3766-3798.

37 J. R. Dahn, B. M. Way, E. Fuller and J. S. Tse, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1993, **48**, 17872-17877.

38 C. G. Van de Walle and J. E. Northrup, *Phys. Rev. Lett.*, 1993, **70**, 1116-1119.

39 H. Okamoto, Y. Kumai, Y. Sugiyama, T. Mitsuoka, K. Nakanishi, T. Ohta, H. Nozaki, S. Yamaguchi, S. Shirai and H. Nakano, *J. Am. Chem. Soc.*, 2010, **132**, 2710-2718.

40 Y. Sugiyama, H. Okamoto, T. Mitsuoka, T. Morikawa, K. Nakanishi, T. Ohta and H. Nakano, *J. Am. Chem. Soc.*, 2010, **132**, 5946-5947.

41 H. Nakano, M. Nakano, K. Nakanishi, D. Tanaka, Y. Sugiyama, T. Ikuno, H. Okamoto and T. Ohta, *J. Am. Chem. Soc.*, 2012, **134**, 5452-5455.

42 M. J. S. Spencer, T. Morishita, M. Mikami, I. K. Snook, Y. Sugiyama and H. Nakano, *Phys. Chem. Chem. Phys.*, 2011, **13**, 15418-15422.

43 G. Brumfiel, *Nature*, 2013, **495**, 152-153.

44 J. Gao and J. Zhao, *Sci. Rep.*, 2012, **2**, 861.

45 D. Jose and A. Datta, *Phys. Chem. Chem. Phys.*, 2011, **13**, 7304-7311.

46 C. C. Liu, W. Feng and Y. Yao, *Phys. Rev. Lett.*, 2011, **107**, 076802.

47 X.-Q. Wang, H.-D. Li and J.-T. Wang, *Phys. Chem. Chem. Phys.*, 2012, **14**, 3031-3036.

48 E. Bianco, S. Butler, S. Jiang, O. D. Restrepo, W. Windl and J. E. Goldberger, *ACS Nano*, 2013, **7**, 4414-4421.

49 K. J. Koski and Y. Cui, *ACS Nano*, 2013, **7**, 3739-3743.

50 Y. Kumai, H. Kadoura, E. Sudo, M. Iwaki, H. Okamoto, Y. Sugiyama and H. Nakano, *J. Mater. Chem.*, 2011, **21**, 11941-11946.

51 Y. Kumai, S. Shirai, E. Sudo, J. Seki, H. Okamoto, Y. Sugiyama and H. Nakano, *J. Power Sources*, 2011, **196**, 1503-1507.

52 Y. Kumai, S. Shirai, H. Okamoto, Y. Sugiyama and H. Nakano, *IOP Conf. Ser.: Mater. Sci. Eng.*, 2011, **18**, 122005.

53 B. Peng, F. Y. Cheng, Z. L. Tao and J. Chen, *J. Chem. Phys.*, 2010, **133**.

54 S. C. Jung and Y.-K. Han, *Phys. Chem. Chem. Phys.*, 2011, **13**, 21282-21287.

55 P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari and R. M. Wentzcovitch, *J. Phys.: Condens. Matter*, 2009, **21**, 395502.

56 J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh and C. Fiolhais, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1992, **46**, 6671-6687.

57 J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865-3868.

58 A. M. Rappe, K. M. Rabe, E. Kaxiras and J. D. Joannopoulos, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1990, **41**, 1227-1230.

59 W. H. Wan, Q. F. Zhang, Y. Cui and E. G. Wang, *J. Phys.: Condens. Matter*, 2010, **22**, 415501.

60 Q. F. Zhang, W. X. Zhang, W. H. Wan, Y. Cui and E. G. Wang, *Nano Lett.*, 2010, **10**, 3243-3249.

61 O. I. Malyi, T. L. Tan and S. Manzhos, *J. Power Sources*, 2013, **233**, 341-345.

62 G. A. Tritsaris, K. J. Zhao, O. U. Okeke and E. Kaxiras, *J. Phys. Chem. C*, 2012, **116**, 22212-22216.

63 S. C. Jung and Y.-K. Han, *Phys. Chem. Chem. Phys.*, 2013, **15**, 13586-13592.

64 C. Y. Chou and G. S. Hwang, *Surf. Sci.*, 2013, **612**, 16-23.

65 G. Henkelman, B. P. Uberuaga and H. Jonsson, *J. Chem. Phys.*, 2000, **113**, 9901-9904.

66 V. V. Kulish, M.-F. Ng, O. I. Malyi, P. Wu and Z. Chen, *ChemPhysChem*, 2013, **14**, 1161-1167.

67 C. Arrouvel, S. C. Parker and M. S. Islam, *Chem. Mater.*, 2009, **21**, 4778-4783.

68 Y. Li, D. Wu, Z. Zhou, C. R. Cabrera and Z. Chen, *J. Phys. Chem. Lett.*, 2012, **3**, 2221-2227.

69 Q. Tang, Z. Zhou and P. Shen, *J. Am. Chem. Soc.*, 2012, **134**, 16909-16916.

70 K. Tibbetts, C. R. Miranda, Y. S. Meng and G. Ceder, *Chem. Mater.*, 2007, **19**, 5302-5308.

71 S. Yang, D. Li, T. Zhang, Z. Tao and J. Chen, *J. Phys. Chem. C*, 2012, **116**, 1307-1312.

72 T. Bucko, J. Hafner, S. Lebegue and J. G. Angyan, *J. Phys. Chem. A*, 2010, **114**, 11814-11824.

73 S. Grimme, *J. Comput. Chem.*, 2006, **27**, 1787-1799.

74 S. Cahangirov, M. Topsakal, E. Aktürk, H. Şahin and S. Ciraci, *Phys. Rev. Lett.*, 2009, **102**, 236804.

75 K. Takeda and K. Shiraishi, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1994, **50**, 14916-14922.

76 H. Okamoto, Y. Sugiyama and H. Nakano, *Chem.-Eur. J.*, 2011, **17**, 9864-9887.

77 R. L. Aggarwal, P. Fisher, V. Mourzine and A. K. Ramdas, *Phys. Rev.*, 1965, **138**, A882-A893.

78 K. T. Chan, J. B. Neaton and M. L. Cohen, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2008, **77**, 235430.

79 X. Liu, C. Z. Wang, Y. X. Yao, W. C. Lu, M. Hupalo, M. C. Tringides and K. M. Ho, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2011, **83**, 235411.

80 T. O. Wehling, M. I. Katsnelson and A. I. Lichtenstein, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2009, **80**, 085428.

81 V. A. Sethuraman, L. J. Hardwick, V. Srinivasan and R. Kostecki, *J. Power Sources*, 2010, **195**, 3655-3660.

82 X. Fan, W. T. Zheng, J.-L. Kuo and D. J. Singh, *ACS Appl. Mater. Interfaces*, 2013, **5**, 7793-7797.

83 Y. Liu, V. I. Artyukhov, M. Liu, A. R. Harutyunyan and B. I. Yakobson, *J. Phys. Chem. Lett.*, 2013, **4**, 1737-1742.

84 J. S. Tse, J. R. Dahn and F. Buda, *J. Phys. Chem.*, 1995, **99**, 1896-1899.

85 M. T. McDowell and Y. Cui, *Adv. Energy Mater.*, 2011, **1**, 894-900.

86 G. Henkelman, A. Arnaldsson and H. Jonsson, *Comput. Mater. Sci.*, 2006, **36**, 354-360.

87 B. Kang and G. Ceder, *Nature*, 2009, **458**, 190-193.

88 K. S. Kang, Y. S. Meng, J. Breger, C. P. Grey and G. Ceder, *Science*, 2006, **311**, 977-980.