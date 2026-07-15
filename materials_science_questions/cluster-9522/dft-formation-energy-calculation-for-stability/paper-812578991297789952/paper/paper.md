# Large-gap topological insulators in functionalized ordered double transition metal carbide MXenes

Zhi-Quan Huang, $^{1,*}$ Mei-Ling Xu, $^{1,*}$ Gennevieve Macam, $^{1,*}$ Chia-Hsiu Hsu, $^{1,*}$ and Feng-Chuan Chuang $^{1,2,3,\dagger}$

$^{1}$Department of Physics, National Sun Yat-sen University, Kaohsiung 80424, Taiwan
$^{2}$Department of Physics, National Tsing Hua University, Hsinchu 30013, Taiwan
$^{3}$Physics Division, National Center for Theoretical Sciences, Hsinchu 30013, Taiwan

![](./images/812578991297789952_1.jpg)
(Received 11 July 2019; accepted 27 July 2020; published 14 August 2020)

Two-dimensional MXenes continue to receive much research attention owing to their versatility and predicted topological phase, which are yet to be fully explored. Here, we conduct a rigorous search on $M_{2}'M''C_{2}$ ($M'$ = V, Nb, or Ta; $M''$ = Ti, Zr, or Hf) with various surface terminations, $X_{2}$ ($X$ = F, Cl, Br, I, O, H, or OH), using first-principles calculations. The majority of the systems exhibit the topological phase with semimetallic band structures. Most importantly, fluorinated MXenes, $M_{2}'M''C_{2}F_{2}$, are topological insulators. They possess sizable nontrivial band gaps from 34 to 318 meV using Heyd-Scuseria-Ernzerhof (HSE) hybrid functional calculations which are within the range capable of realizing quantum spin-Hall effects even at room temperature. Furthermore, the $d$ orbitals of $M'$ and $M''$ atoms mostly contribute to the spin-orbit coupling-induced band gaps. Selecting $V_{2}TiC_{2}F_{2}$ as an exemplar, we demonstrate the presence of edge states, verifying the calculated $Z_{2}$ invariant, and reveal its robustness against tensile strain. Finally, we propose SiC(0001) as a candidate substrate for material realization as it can preserve the nontrivial band topology.

DOI: 10.1103/PhysRevB.102.075306

## I. INTRODUCTION

Topological insulators (TIs) have attracted a great deal of attention in theoretical and experimental studies. They are highly pursued after their unique properties such as dissipationless transport, which is highly promising in numerous applications. They possess conducting edge states in two dimensions and conducting surface states in three dimensions but are insulating in the interior [1–3]. This phenomenon, generally observed in heavy elements due to their large spin-orbit coupling (SOC), exhibits edge/surface states that are protected by time-reversal symmetry [4,5]. Thus, TIs are not affected by backscattering from impurities. Owing to the robustness of their edge/surface states, TIs are continuously researched in the fields of quantum computing, spintronics, optoelectronics, high-efficiency electronic components, and other applications.

Two-dimensional (2D) TIs, also known as quantum spin-Hall (QSH) insulators, have been discovered in both free-standing and chemically functionalized 2D materials with honeycomb structures such as thin films of group IV [6–9], group V (Bi,Sb) [10–15] elements, and groups III–V compounds [16–19]. Reviews on topological insulators [20–23] also report more members in the growing 2D family of TIs such as transition metal dichalcogenides [24], Janus materials [25], and organometallic frameworks [26].

Among these 2D systems, some MXenes have also been reportedly shown potential to possess versatile physical and chemical properties as well as topological phases [27–32]. MXenes have the chemical formula $M_{n+1}X_{n}T_{2}$, where $M$ is an early transition metal, $X$ is carbon and/or nitrogen, $T_{2}$ is the surface termination, and $n$ is the thickness ($n = 1, 2, 3, \dots$). Experimental studies [33–37] show that MXene surfaces are easily terminated by F, O, or OH groups after chemical exfoliation by hydrofluoric acid solutions from the precursor MAX phase with the chemical formula $M_{n+1}AX_{n}$ ($A$ = Al, Si, P, S, Ga, Ge, As, In, or Sn).

In 2011, the first MXene, $Ti_{3}C_{2}T_{2}$, was synthesized [38], which was also reported to possess higher elasticity compared to graphene oxide [39]. The experimental realization has expanded the applications of MAX phases and has spurred interest to discover new phases to synthesize into MXenes. Alloying MAX phases has been an effective approach and it gave rise to chemically disordered solid-solution MXenes [31,40–42], for instance, alloyed $Ti_{2}C$ [31,40–42] MXenes such as such as $(Ti_{0.5}Nb_{0.5})_{2}C$ [40], and $(Nb_{0.8}Ti_{0.2})_{4}C_{3}$ [41]. In a similar approach, the first chemically ordered MXenes, $Mo_{2}TiC_{2}T_{x}$, $Mo_{2}Ti_{2}C_{3}T_{x}$, and $Cr_{2}TiC_{2}T_{x}$, were realized in 2015 [43].

The recently discovered ordered double transition metal MXenes reveal novel exotic properties and open new avenues to tune electronic properties for device applications [43,44]. At present, MXenes can be categorized into four different forms, mono-transition metal, solid solution, ordered divacancy, and ordered double transition metal MXenes [27–30].

There have been many studies which focused on the mechanical [42,45], electronic [43,46–51], magnetic [46,47,52,53], thermoelectric [54–56], and optical [49,50] properties of MXenes. They are used in many applications such as composite materials, energy storage [57,58], sensors [59,60], wireless communication [61], spintronics [62], and electromagnetic shielding [63]. Apart from the many properties MXenes may possess, topological phases have

*These authors contributed equally to this work.
$^{\dagger}$fchuang@mail.nsysu.edu.tw

also been theoretically predicted in mono-transition metal MXenes, $M_2CX_2$ (where $M$ is group VB, VIB (W, Mo, or Cr), or IIB transition metals, and surface termination $X =$ F, O, OH) [64,65], MXene nitrides ($M_3N_2F_2$, where $M =$ Ti, Zr) [66], triangular MXenes ($W_2M_2C_3$) [67], ordered double transition metal carbides, $M_2'M''C_2O_2$ [44,68,69], and $M_2'M_2''C_3O_2$ [44] ($M'$ and $M''$ are transition metals). Notably, some members of the MXene family have been experimentally synthesized [62,70]. Specifically, it was predicted that $M_2'M''C_2O_2$ ($M' =$ Mo or W; $M'' =$ Ti, Zr, or Hf) [44,68,69] and $M_2'M_2''C_3O_2$ ($M' =$ Mo or W; $M'' =$ Ti or Zr) are nontrivial topological semimetals [44]. However, these studies are limited to the combination of groups IVB and VIB elements and therefore, there remain ordered double-transition-metals yet to be explored for numerous properties as well as for topological phases.

In this study, we conducted a rigorous search on $M_2'M''C_2$ ($M' =$ V, Nb, or Ta; $M'' =$ Ti, Zr, or Hf) with various surface terminations, $X_2$ ($X =$ F, Cl, Br, I, O, H, or OH), using first-principles calculations. We found that the family of $M_2'M''C_2F_2$ studied shows sizable gaps ranging from 34 to 318 meV using hybrid functionals, sufficiently large for realizing room-temperature QSH effects. Further analysis shows that majority of the contribution are from the $d$ orbitals of the transition metal. The nontrivial phase of $V_2TiC_2F_2$ is demonstrated to be robust against tensile strain up to $19\%$. Finally, further calculations support SiC(0001) as a candidate substrate for material realization since the nontrivial band topology observed in freestanding MXenes remains even with a substrate. The results of this calculation may encourage the researcher to develop new etching processes or chemical procedures to synthesize the desired ordered double transition metal MXenes.

## II. COMPUTATIONAL METHODS

First-principles calculations were performed in the density-functional theory (DFT) [71] using the Perdew-Burke-Ernzerhof (PBE) generalized gradient approximation (GGA) [72] and projector augmented-wave [73] method with an energy cutoff of 400 eV in the VIENNA AB INITIO SIMULATION PACKAGE (VASP) [74,75]. The hybrid functional HSE06 [76] was also performed as it is well known that GGA underestimates the band gap. The thin slabs of ordered double transition metal MXenes were periodically simulated with a vacuum space of $\sim 20\,\mathring{A}$. The Brillouin-zone integration is sampled using a set of $12 \times 12 \times 1$ Gamma-centered Monkhorst-Pack grids [77]. The structures were fully relaxed until the residual forces were not greater than $10^{-3}\, \text{eV}/\mathring{A}$. The convergence criteria for electronic structure calculations with and without spin-orbit coupling are set at $1 \times 10^{-6}\, \text{eV}$.

We predict the topology of the structure by calculating the $Z_2$ topological invariant [1] via two methods: (i) wavefunction parity analysis [78] and (ii) Wannier-derived $Z_2$ topological invariant [79,80]. The trivial and nontrivial topological phases are characterized by $Z_2 = 0$ and 1, respectively. In the first method, parity analysis [78], the existence of inversion symmetry allows us to calculate $Z_2$ topological invariant, $v$, from the parity of their wave functions in the valence bands at the time-reversal invariant momentum points of the Brillouin zone below the Fermi level using the formula, $(-1)^v = 1$ $(-1)^v = \prod_{i=1}^n \delta(ki)$. The trivial phase is $v = 0$ and the nontrivial topological phase is $v = 1$. The second method utilizes the z2PACK package [79,80] which calculates the $Z_2$ topological invariant via tracking of hybrid Wannier charge centers. Edge states were calculated using the maximally localized Wannier functions as implemented in the WANNIER90 package [81].

![](./images/812578991297789952_2.jpg)

FIG. 1. The crystal structure of $M_2'M''C_2X_2$. (a) is top view and (b) is the side view of $M_2'M''C_2X_2$. (c), (d) The 3D perspective side views of $M'_2M''C_2F_2$ and $M'_2M''C_2(OH)_2$, respectively. Yellow circles represent the surface termination atoms, $X =$ F, Cl, Br, I, O, or H; yellow and gray circles represent O and H atoms in OH adsorbate, respectively. Black, light green, and orange circles, respectively, denote $M'$ (V, Nb, or Tb), C, and $M''$ (Ti, Hf, or Zr) atoms.

## III. RESULTS AND DISCUSSION

### A. Atomic structure and stabilities

It is well known that in experiments, the chemically exfoliated MXenes are saturated with a mixture of F, O, or OH. Thus, it is highly interesting to understand the effect of other halogen (Cl, Br, or I) terminations. In total, 63 combinations of $M_2'M''C_2X_2$ ($M' =$ V, Nb, or Ta; $M'' =$ Ti, Zr, or Hf; $X =$ F, Cl, Br, I, O, H, or OH) were examined. The atomic structure of functionalized ordered double transition metal $M_2'M''C_2X_2$ forms a hexagonal lattice with $P3\bar{m}1$ group symmetry as shown in Fig. 1. $M'$ and $M''$ are two different transition metals. It has seven layers in which the bottom-most and topmost layers are surface terminations labeled X in Fig. 1(b). The second outer layers are occupied by $M'$ atoms followed by a third layer of C atoms. The $M''$ atoms fill the center layer.

A previous theoretical study reported that pristine $V_2TiC_2$ is most structurally stable in the fully ordered state, while $M_2'TiC_2$ ($M' =$ Nb or Ta) is more stable in the partially ordered state [43]. These findings are consistent with our results. However, we found that only $V_2TiC_2$ prefer the fully ordered state, whereas $M_2'M''C_2$ ($M' =$ Nb, or Ta; $M'' =$ Zr or Hf) and $V_2M''C_2$ ($M'' =$ Zr or Hf) prefer the partially ordered state. See the formation energy profiles in Fig. S1 in the Supplemental Material [82]. The stabilities of the ordered phase are further verified from the phonon spectra which show

<table>
<caption>TABLE I. The lattice constant, $Z_2$ topological invariant, system band gap, and $\Gamma$-point band gap of $\text{V}_2\text{TiC}_2\text{X}_2$ ($X$ = F, Cl, Br, I, O, H, or OH).</caption>
<thead>
<tr>
<th></th>
<th>Lattice constant (Å)</th>
<th>$Z_2$</th>
<th>System band gap (meV)</th>
<th>$\Gamma$-point band gap (meV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\text{V}_2\text{TiC}_2\text{F}_2$</td>
<td>2.86</td>
<td>1</td>
<td>35</td>
<td>39</td>
</tr>
<tr>
<td>$\text{V}_2\text{TiC}_2\text{Cl}_2$</td>
<td>3.02</td>
<td>1</td>
<td>−169</td>
<td>13</td>
</tr>
<tr>
<td>$\text{V}_2\text{TiC}_2\text{Br}_2$</td>
<td>3.10</td>
<td>1</td>
<td>−447</td>
<td>135</td>
</tr>
<tr>
<td>$\text{V}_2\text{TiC}_2\text{I}_2$</td>
<td>3.24</td>
<td>1</td>
<td>−449</td>
<td>273</td>
</tr>
<tr>
<td>$\text{V}_2\text{TiC}_2\text{O}_2$</td>
<td>2.88</td>
<td>0</td>
<td>−785</td>
<td>14</td>
</tr>
<tr>
<td>$\text{V}_2\text{TiC}_2\text{H}_2$</td>
<td>2.87</td>
<td>1</td>
<td>−424</td>
<td>29</td>
</tr>
<tr>
<td>$\text{V}_2\text{TiC}_2(\text{OH})_2$</td>
<td>2.90</td>
<td>1</td>
<td>−148</td>
<td>65</td>
</tr>
</tbody>
</table>

no negative frequencies indicating that the systems are structurally stable and could possibly be synthesized (see Fig. S2 in the Supplemental Material [82]). To provide a comparative discussion, we focus on the fully ordered structure for the rest of the paper.

The functional group atoms have three different adsorption sites. It can be vertically adsorbed on top of $M'$ atom [labeled as site $A$ in Figs. 1(b) and 1(d)] or adsorbed on top of the middle-layer transition metal ($M''$) which is labeled as site $B$. It can also be adsorbed on top of carbon atoms which is labeled as site $C$. These three adsorption configurations were examined for every compound with seven kinds of surface terminations. The energetics for the various adsorption sites (see Table S1 in the Supplemental Material [82]) shows that the preferred adsorption site is either site $B$ or $C$. For the halogen terminations, the lighter elements F and Cl prefer site $C$ except for $\text{V}_2\text{ZrC}_2\text{F}_2$, $\text{V}_2\text{HfC}_2\text{F}_2$, $\text{V}_2\text{ZrC}_2\text{Cl}_2$, $\text{V}_2\text{HfC}_2\text{Cl}_2$, and $\text{V}_2\text{TiC}_2\text{Cl}_2$, which prefer site $B$. For the slightly heavier halogen termination $\text{Br}_2$, we observed partial preference to sites $B$ and $C$. For the systems that prefer site $C$ (i.e., $M'$ = Nb and $\text{Ta}_2\text{HfC}_2\text{Br}_2$), the energies are very close to those of site $B$ and not exceeding 130-meV energy difference. The much heavier halogen, I, as well as O and H prefer adsorption site $B$. Finally, (OH) terminations prefer site $C$, where the O atom is on site $C$, while the H atom is perpendicularly adsorbed on top of O atom as shown in Fig. 1(d).

### B. Topological invariant and electronic structure
As the structure possesses inversion symmetry, two methods were used to examine its topology—the $Z_2$ number [1] and parity analysis [78]. These two methods show consistent results for all our calculations. The majority of the systems exhibit the topological phase with semimetallic band structures but $\text{V}_2\text{TiC}_2\text{F}_2$, which is a topological insulator. The $Z_2$ topological invariants and other relevant data are summarized in Tables S2 to S10 for all the 63 compounds in the Supplemental Material [82].

Here, we provide an elaborate discussion on the electronic and topological properties of $\text{V}_2\text{TiC}_2\text{X}_2$ ($X$ = F, Cl, Br, I, O, H, or OH). Table I shows the calculated $Z_2$ invariants, system band gaps and $\Gamma$-point band gaps for $\text{V}_2\text{TiC}_2\text{X}_2$ ($X$ = F, Cl, Br, I, O, H, or OH). See Fig. S3 in the Supplemental Material [82] for the band structures with and without SOC. We found that $\text{V}_2\text{TiC}_2\text{X}_2$ possess topological phases except for $\text{V}_2\text{TiC}_2\text{O}_2$ which is trivial. Among the topological phases found, $\text{V}_2\text{TiC}_2\text{X}_2$ (where $X$ = F, Cl, I, Br, H, or OH), $\text{V}_2\text{TiC}_2\text{F}_2$ is an insulator and the rest of them are semimetals.

Nontrivial insulating phases are also found in the rest of F-terminated $M'_2M''\text{C}_2\text{X}_2$ systems. In order to study the behavior of different transition metal combinations of F-terminated compounds $M'_2M''\text{C}_2\text{F}_2$ ($M'$ = V, Nb, or Ta; $M''$ = Ti, Hf, or Zr), we present a summary of results in Table II. See Fig. S4 in the Supplemental Material [82] for the band structures using PBE and HSE06. The PBE and HSE06 band structures are similar in band dispersions. Since PBE underestimates the band gap, HSE06 can give a more accurate band gap. The topological phase is the same in PBE and HSE06 calculations. All nine $M'_2M''\text{C}_2\text{F}_2$ systems are topological insulators ($Z_2 = 1$) with a sizable gap of 34 to 318 meV under HSE06 calculations as shown in Table II.

Next, to further explore the mechanism causing the topological phase, we again focus on F-terminated systems. We present the band structures of $M'_2\text{TiC}_2\text{F}_2$ ($M'$ = V, Nb, or Ta) with orbital contributions in Fig. 2. See Fig. S5 in the Supplemental Material [82] for the band structures of $\text{V}_2M''\text{C}_2\text{F}_2$ ($M''$ = Ti, Hf, or Zr). As shown in Fig. 2, $M'_2\text{TiC}_2\text{F}_2$ ($M'$ = V, Nb, or Ta) are gapless at the $\Gamma$ point without SOC and becomes gapped after including SOC effects. In previous studies [44,68], band inversions in ordered double transition metals are due to $d$ orbitals. Thus, we analyze the orbital contributions at the Fermi level of $M'_2\text{TiC}_2\text{F}_2$ ($M'$ = V, Nb, or Ta) as illustrated in Fig. 2. The contributions are represented as multicolor circles with size proportional to its magnitude. Analysis of the atomic and orbital contributions show similar behavior with previous studies [44,68]. The orbital contributions at the valence and conduction bands are dominated by $d_{xy,x^2-y^2}$ orbitals of the transition metals, $M'$ and $M''$. However, the contributions from C are more concentrated at the band far below the Fermi level.

### C. Origin of the SOC-induced band gap
In Fig. 2, we had observed band-gap opening at the $\Gamma$ point after including SOC effects. Here, we determine the origin of the band gap in detail by performing additional calculations with SOC separately turned on for only $M'$ or only $M''$ in $M'_2M''\text{C}_2\text{F}_2$. The sum of the gaps induced when the SOC is on for only $M'$ or only $M''$ is close to the gap induced by the SOC of all atoms as shown in Table III. Thus, the SOC of $M'$ or $M''$ is the major cause of band-gap opening, similar to the conclusion of previous studies [44,68]. Furthermore, we can see that the heavier elements induced a larger SOC band gap as seen in Table III. However, the range of induced band gap when SOC is turned on only for the heavier element Ta is 0.0642 eV, whereas the band-gap range in lighter elements are smaller by one order (i.e. 0.0055 and 0.0038 eV, respectively, for V and Nb). Hence, we look into another parameter that may affect the band gap—the contributions of $d$ orbital.

The contributions from the $d_{xy}$ and $d_{x^2-y^2}$ orbitals for $M'$ or only $M''$ in the bands at the Fermi level are calculated and listed in Table III. The band gap induced when SOC is on for only $M'$ ($M''$) is plotted against the $d$-orbital contributions in Figs. 3(a) and 3(b). From the two figures, we can observe that the lighter elements have more contribution. Since $d_{xy}$ and

<table>
<caption>TABLE II. The lattice constant, $Z_2$ topological invariant, system band gap, and $\Gamma$-point band gap by PBE and HSE06 of $M_2^\prime M^{\prime\prime}\text{C}_2\text{F}_2$ ($M^\prime$ = V, Nb, or Ta; $M^{\prime\prime}$ = Ti, Zr, or Hf). The values in the parentheses are obtained by hybrid functional calculations.</caption>
<tbody><tr>
<td>
</td>
<td>
Lattice constant
</td>
<td>
$Z_2$
</td>
<td>
System band gap (meV)
</td>
<td>
$\Gamma$-point band gap (meV)
</td>
</tr>
<tr>
<td>
</td>
<td>
(Å)
</td>
<td>
</td>
<td>
PBE(HSE06)
</td>
<td>
PBE(HSE06)
</td>
</tr>
<tr>
<td>
$\text{V}_2\text{TiC}_2\text{F}_2$
</td>
<td>
2.86
</td>
<td>
1
</td>
<td>
35 (211)
</td>
<td>
39 (248)
</td>
</tr>
<tr>
<td>
$\text{V}_2\text{ZrC}_2\text{F}_2$
</td>
<td>
2.99
</td>
<td>
1
</td>
<td>
48 (194)
</td>
<td>
55 (254)
</td>
</tr>
<tr>
<td>
$\text{V}_2\text{HfC}_2\text{F}_2$
</td>
<td>
2.96
</td>
<td>
1
</td>
<td>
49 (294)
</td>
<td>
101 (389)
</td>
</tr>
<tr>
<td>
$\text{Nb}_2\text{TiC}_2\text{F}_2$
</td>
<td>
3.00
</td>
<td>
1
</td>
<td>
52 (234)
</td>
<td>
82 (276)
</td>
</tr>
<tr>
<td>
$\text{Nb}_2\text{ZrC}_2\text{F}_2$
</td>
<td>
3.07
</td>
<td>
1
</td>
<td>
$-$5 (120)
</td>
<td>
110 (296)
</td>
</tr>
<tr>
<td>
$\text{Nb}_2\text{HfC}_2\text{F}_2$
</td>
<td>
3.04
</td>
<td>
1
</td>
<td>
$-$18 (122)
</td>
<td>
217 (405)
</td>
</tr>
<tr>
<td>
$\text{Ta}_2\text{TiC}_2\text{F}_2$
</td>
<td>
3.01
</td>
<td>
1
</td>
<td>
$-$6 (318)
</td>
<td>
207 (482)
</td>
</tr>
<tr>
<td>
$\text{Ta}_2\text{ZrC}_2\text{F}_2$
</td>
<td>
3.04
</td>
<td>
1
</td>
<td>
$-$80 (34)
</td>
<td>
278 (489)
</td>
</tr>
<tr>
<td>
$\text{Ta}_2\text{HfC}_2\text{F}_2$
</td>
<td>
3.05
</td>
<td>
1
</td>
<td>
$-$23 (126)
</td>
<td>
424 (665)
</td>
</tr>
</tbody>
</table>

$d_{x^2-y^2}$ are orbitals of $M^\prime$ and $M^{\prime\prime}$ for the filled bonding and empty antibonding orbitals, respectively, the bonding energy will be closer to the site with lower $d_{xy}$ and $d_{x^2-y^2}$ orbital energy [see Fig. 3(c)]. The heavier element has a higher principal quantum number. Thus, the $d_{xy}$ and $d_{x^2-y^2}$ orbital energy increases and the hybridization between the heavier element and bond state decreases.

In order to reveal the relationship between the gap, SOC strength, and the orbital contributions, the data in Table III are plotted in Figs. 3(a) and 3(b) and the data are fitted with linear equations labeled and indicated as dashed lines. The linear relationship is defined as the following equation to approximate the band gap:

$$
Gap \sim \langle d_{M^\prime} | \Psi \rangle^2 \lambda_{SOC}(M^\prime) + \langle d_{M^{\prime\prime}} | \Psi \rangle^2 \lambda_{SOC}(M^{\prime\prime}),
$$

where $\langle d_{M^{\prime\prime}} | \Psi \rangle^2$ and $\langle d_{M^\prime} | \Psi \rangle^2$ refer to the square of the projection of $\Psi$ on the $d$ orbitals of $M^\prime$ and $M^{\prime\prime}$. The $d$-orbital contribution columns in Table III correspond to $\langle d_{M^\prime} | \Psi \rangle^2$ and

![](./images/812578991297789952_3.jpg)

FIG. 2. The band structures of (a), (b) $\text{V}_2\text{TiC}_2\text{F}_2$, (c), (d) $\text{Nb}_2\text{TiC}_2\text{F}_2$, and (e), (f) $\text{Ta}_2\text{TiC}_2\text{F}_2$ with (lower panels) and without (upper panels) SOC. The even or odd parities at the $\Gamma$ point are denoted by $+$ and $-$, respectively.

<table>
<caption>TABLE III. Band gaps at the $\Gamma$ point with SOC turned on for both $M'$ and $M''$ atoms, $M'$ atom only, or $M''$ atom only. The summation of $d_{xy}$ and $d_{x^2-y^2}$ orbital contributions from $M'$ or $M''$ are listed.</caption>
<thead>
<tr>
<th rowspan="2">$M'_2M''\text{C}_2\text{F}_2$</th>
<th colspan="3">SOC gap (eV) at $\Gamma$</th>
<th colspan="2">$d_{xy}+d_{x^2-y^2}$ orbitals at $\Gamma$</th>
</tr>
<tr>
<th>$M'$ and $M''$</th>
<th>$M'$</th>
<th>$M''$</th>
<th>Contribution from $M'$</th>
<th>Contribution from $M''$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\text{V}_2\text{TiC}_2\text{F}_2$</td>
<td>0.0393</td>
<td>0.0245</td>
<td>0.0120</td>
<td>0.231</td>
<td>0.367</td>
</tr>
<tr>
<td>$\text{V}_2\text{ZrC}_2\text{F}_2$</td>
<td>0.0553</td>
<td>0.0258</td>
<td>0.0254</td>
<td>0.258</td>
<td>0.232</td>
</tr>
<tr>
<td>$\text{V}_2\text{HfC}_2\text{F}_2$</td>
<td>0.1014</td>
<td>0.0203</td>
<td>0.0753</td>
<td>0.244</td>
<td>0.174</td>
</tr>
<tr>
<td>$\text{Nb}_2\text{TiC}_2\text{F}_2$</td>
<td>0.0821</td>
<td>0.0654</td>
<td>0.0141</td>
<td>0.182</td>
<td>0.400</td>
</tr>
<tr>
<td>$\text{Nb}_2\text{ZrC}_2\text{F}_2$</td>
<td>0.1104</td>
<td>0.0691</td>
<td>0.0372</td>
<td>0.196</td>
<td>0.309</td>
</tr>
<tr>
<td>$\text{Nb}_2\text{HfC}_2\text{F}_2$</td>
<td>0.2167</td>
<td>0.0692</td>
<td>0.1416</td>
<td>0.201</td>
<td>0.298</td>
</tr>
<tr>
<td>$\text{Ta}_2\text{TiC}_2\text{F}_2$</td>
<td>0.2070</td>
<td>0.1871</td>
<td>0.0163</td>
<td>0.142</td>
<td>0.462</td>
</tr>
<tr>
<td>$\text{Ta}_2\text{ZrC}_2\text{F}_2$</td>
<td>0.2777</td>
<td>0.2268</td>
<td>0.0458</td>
<td>0.173</td>
<td>0.369</td>
</tr>
<tr>
<td>$\text{Ta}_2\text{HfC}_2\text{F}_2$</td>
<td>0.4237</td>
<td>0.2513</td>
<td>0.1613</td>
<td>0.190</td>
<td>0.334</td>
</tr>
</tbody>
</table>

$\langle d_{M''} | \Psi \rangle^2$. The slope of the linear equation is now the SOC strength $\lambda_{SOC}$ for one element, assuming the strength of the other atom is turned off. From the figure, we observe that the slope becomes steeper as the element becomes heavier. The slope of the heaviest element, $\lambda_{SOC}(\text{Ta})$, is 1.317 while the lightest, $\lambda_{SOC}(\text{Ti})$, has a slope of only 0.0346. The SOC strength (i.e., slope) for all the elements are labeled in the plots.

The SOC gap now can be estimated again from the fitted equation $\langle d_{M'} | \Psi \rangle^2 \lambda_{SOC}(M') + \langle d_{M''} | \Psi \rangle^2 \lambda_{SOC}(M'')$. For example, in $\text{V}_2\text{TiC}_2\text{F}$, $\lambda_{SOC}(V)=0.0962$, $\langle d_V | \Psi \rangle^2=0.231$, $\lambda_{SOC}(Ti)=0.0962$, and $\langle d_{Ti} | \Psi \rangle^2=0.367$. The approximated band gap is 0.03492 eV which is on the same order as the VASP-calculated band gap of 0.0393 eV. Similar estimations can be performed for the rest of the systems listed in Table III. The nearly linear relationship implies that not only SOC strength $\lambda_{SOC}(M)$ but also both the orbital contributions play a significant role in the band-gap opening at the $\Gamma$ point.

### D. Topologically protected edge state

The robustness of the topological phase in $\text{V}_2\text{TiC}_2\text{F}_2$ is further explored by applying tensile strain. Interestingly, we find that the topological phase remains even if the lattice constant, $a$, is expanded up to 18.5%. See Fig. S6 in the Supplemental Material [82] for the detailed discussion regarding the effect of strain.

We illustrated the presence of edge states of MXenes ribbon in Fig. 4(a). To calculate the topologically protected edge state of MXenes, we first used DFT-fitted tight-binding Hamiltonians derived from maximally localized Wannier functions (MLWFs) and verified the $Z_2$ calculations. Next, the Green's function of the semi-infinite lattice is constructed using the MLWFs to calculate the local density of states (LDOS) of the edge states [Fig. 4(b)]. The brighter bands in Fig. 4(b) show the edge states connecting the valence and conduction bands forming a Dirac cone at the M point. Lastly, it can possibly be synthesized via lithography method to create different surface termination (F vs O) to create different topological phases as illustrated in Fig. 4(c).

### E. The substrate-supported MXenes

The synthesis of 2D thin films require a suitable substrate on which the target topological phases are preserved. A previous study proposed $h$-BN as a candidate substrate [68]. However, they found that it is not an ideal substrate because the valence electronic states of the substrate are close to the Fermi level. Hence, the need to search for an ideal substrate remains. As we demonstrated in Fig. 2, in $M'_2M''\text{C}_2\text{X}_2$, the nontrivial topology originates from the band inversion of

![](./images/812578991297789952_4.jpg)

FIG. 3. The relation between the band gap at $\Gamma$ point and the $d_{xy}$ and $d_{x^2-y^2}$ orbital contributions for each element with the SOC on (a) only for $M'$ and (b) only for $M''$. In (a), the dashed lines are the fitted linear equations for the orbital contribution from $M' = \text{V}$, $\text{Nb}$, or $\text{Ta}$. In (b), the dotted-dashed lines are the fitted linear equations for $M'' = \text{Ti}$, $\text{Zr}$, or $\text{Hf}$. (c) The schematic illustration of the hybridization between the $d_{xy}$ and $d_{x^2-y^2}$ orbitals of $M'$ and $M''$.

![](./images/812578991297789952_5.jpg)

FIG. 4. (a) Illustration of topologically protected state edge states. (b) LDOS of edge states in $V_2TiC_2F_2$, and (c) is an illustration of possible synthesis of MXene via two different surface terminations.

the transition metal atoms in the bulk of $M_2'M''C_2X_2$ rather than at the surfaces. Thus, it is expected that the topological properties can be retained provided that the substrate provides the same bonding as the surfactants with $M_2'M''C_2X_2$.

It has been reported in previous studies that chemical func- tionalization can be replaced by a substrate [17,19]. It was also predicted previously that the SiC(0001) substrate can retain the nontrivial phase [15]. Here, we propose SiC(0001) to support $M_2'M''C_2F_2$ by replacing the F atoms with SiC(0001) substrate. We chose $Nb_2ZrC_2F_2$ as an exemplar as the lattice constants match well and it has the smallest mismatch (0.3%) among the $M_2'M''C_2F_2$ systems investigated in this study. The bulk substrate is simulated using two layers of SiC and passivating its one side with H atoms as shown in Fig. 5(a). The band structure with SOC of $Nb_2ZrC_2F_2$ on SiC(0001) substrate is shown in Fig. 5(b). The topological band is main- tained and bands along the Fermi level are contributed from the Nb and Zr atoms of MXene. Our $Z_2$ calculations verify that it is nontrivial with a gap of 0.078 eV. Finally, the results of this calculation may encourage researchers to develop new etching processes or chemical procedures to synthesize the desired ordered double transition metal MXenes.

## IV. CONCLUSION

We found that ordered double transition metal MXenes, $M_2'M''C_2F_2$ ($M' = V$, Nb, or Ta; $M'' = Ti$, Zr, or Hf) are topological insulators by first-principles calculations. Atomic and orbital contribution analyses show that the majority of the contribution in the bands near the Fermi level at the $\Gamma$ point are from $d_{xy}$ and $d_{x^2-y^2}$ orbitals of the transition metal. Choosing $V_2TiC_2F_2$ as an exemplar, we demonstrate the topologically protected edge states which are consistent with the $Z_2$ calculations and the robustness of topological phase against tensile strain. Finally, we propose SiC(0001) as a candidate substrate for material realization as calculations show preserved nontrivial band topology. MXenes are worthy of research because of their various compositional and surface functional possibilities. More interesting features have been revealed and effectively applied. We expect that more topo- logical insulators in MXenes will be discovered in the future.

![](./images/812578991297789952_6.jpg)

FIG. 5. (a) The crystal structure of SiC(0001)-supported $Nb_2ZrC_2F_2$. Yellow, black, green, orange, violet, and pink, respec- tively, denote F, Nb, C, Zr, Si, and H atoms. (b) The band structure of $Nb_2ZrC_2F_2$ on SiC(0001) substrate. Red dots indicate that majority of the contribution is from Nb and Zr atoms.

## ACKNOWLEDGMENTS

F.-C.C. acknowledges support from the National Center for Theoretical Sciences and the Ministry of Science and Technology of Taiwan under Grant No. MOST-107-2628- M-110-001-MY3. He is also grateful to the National Cen- ter for High-Performance Computing for computer time and facilities.

F.-C.C. and Z.-Q.H. conceived and initiated the study; Z.-Q.H. and M.-L.X. performed first-principles calculations; Z.-Q.H., G.M., C.-H.H., and F.-C.C. performed the de- tailed analysis and contributed to the discussions; and G.M., C.-H.H., and F.-C.C. wrote the manuscript. All authors re- viewed the manuscript.

The authors declare no competing financial interests.

[1] C. L. Kane and E. J. Mele, *Phys. Rev. Lett.* **95**, 146802 (2005).

[2] A. Roth, C. Brune, H. Buhmann, L. W. Molenkamp, J. Maciejko, X.-L. Qi, and S.-C. Zhang, *Science* **325**, 294 (2009).

[3] B. A. Bernevig and S.-C. Zhang, *Phys. Rev. Lett.* **96**, 106802 (2006).

[4] X.-L. Qi, T. L. Hughes, and S.-C. Zhang, *Phys. Rev. B* **78**, 195424 (2008).

[5] X.-L. Qi and S.-C. Zhang, *Phys. Today* **63**(1), 33 (2010).

[6] Y. Xu, B. Yan, H.-J. Zhang, J. Wang, G. Xu, P. Tang, W. Duan, and S.-C. Zhang, *Phys. Rev. Lett.* **111**, 136804 (2013).

[7] B.-H. Chou, Z.-Q. Huang, C.-H. Hsu, F.-C. Chuang, Y.-T. Liu, H. Lin, and A. Bansil, *New J. Phys.* **16**, 115008 (2014).

[8] T.-C. Wang, C.-H. Hsu, Z.-Q. Huang, F.-C. Chuang, W.-S. Su, and G.-Y. Guo, *Sci. Rep.* **6**, 39083 (2016).

[9] K. H. Jin and S. H. Jhi, *Sci. Rep.* **5**, 8426 (2015).

[10] L. Chen, G. Cui, P. Zhang, X. Wang, H. Liu, and D. Wang, *Phys. Chem. Chem. Phys.* **16**, 17206 (2014).

[11] C.-C. Liu, S. Guan, Z. Song, S. A. Yang, J. Yang, and Y. Yao, *Phys. Rev. B* **90**, 085431 (2014).

[12] Z. Song, C.-C. Liu, J. Yang, J. Han, M. Ye, B. Fu, Y. Yang, Q. Niu, J. Lu, and Y. Yao, *NPG Asia Mater.* **6**, e147 (2014).

[13] Z.-Q. Huang, F.-C. Chuang, C.-H. Hsu, Y.-T. Liu, H.-R. Chang, H. Lin, and A. Bansil, *Phys. Rev. B* **88**, 165301 (2013).

[14] C.-H. Hsu, Z.-Q. Huang, C. P. Crisostomo, L.-Z. Yao, F.-C. Chuang, Y.-T. Liu, B. Wang, C.-H. Hsu, C.-C. Lee, H. Lin, and A. Bansil, *Sci. Rep.* **6**, 18993 (2016).

[15] C. H. Hsu, Z. Q. Huang, F. C. Chuang, C. C. Kuo, Y. T. Liu, H. Lin, and A. Bansil, *New J. Phys.* **17**, 025005 (2015).

[16] F. C. Chuang, L. Z. Yao, Z. Q. Huang, Y. T. Liu, C. H. Hsu, T. Das, H. Lin, and A. Bansil, *Nano Lett.* **14**, 2505 (2014).

[17] C. P. Crisostomo, L.-Z. Yao, Z.-Q. Huang, C.-H. Hsu, F.-C. Chuang, H. Lin, M. A. Albao, and A. Bansil, *Nano Lett.* **15**, 6568 (2015).

[18] L. Li, X. Zhang, X. Chen, and M. Zhao, *Nano Lett.* **15**, 1296 (2015).

[19] C. P. Crisostomo, Z.-Q. Huang, C.-H. Hsu, F.-C. Chuang, H. Lin, and A. Bansil, *Npj Comput. Mater.* **3**, 39 (2017).

[20] M. Z. Hasan and C. L. Kane, *Rev. Mod. Phys.* **82**, 3045 (2010).

[21] B. Yan and S. C. Zhang, *Rep. Prog. Phys.* **75**, 096501 (2012).

[22] A. Bansil, H. Lin, and T. Das, *Rev. Mod. Phys.* **88**, 021004 (2016).

[23] L. Kou, Y. Ma, Z. Sun, T. Heine, and C. Chen, *J. Phys. Chem. Lett.* **8**, 1905 (2017).

[24] L.-Y. Feng, R. A. B. Villaos, H. N. Cruzado, Z.-Q. Huang, C.-H. Hsu, H.-C. Hsueh, H. Lin, and F.-C. Chuang, *Chin. J. Phys.* **66**, 15 (2020).

[25] A. B. Maghirang, Z.-Q. Huang, R. A. B. Villaos, C.-H. Hsu, L.-Y. Feng, E. Florido, H. Lin, A. Bansil, and F.-C. Chuang, *Npj 2D Mater. Appl.* **3**, 35 (2019).

[26] C.-H. Hsu, Z.-Q. Huang, G. M. Macam, F.-C. Chuang, and L. Huang, *Appl. Phys. Lett.* **113**, 233301 (2018).

[27] M. Khazaei, A. Ranjbar, M. Arai, T. Sasaki, and S. Yunoki, *J Mater. Chem. C* **5**, 2488 (2017).

[28] B. Anasori, M. R. Lukatskaya, and Y. Gogotsi, *Nat. Rev. Mater.* **2**, 16098 (2017).

[29] V. M. Hong Ng, H. Huang, K. Zhou, P. S. Lee, W. Que, J. Z. Xu, and L. B. Kong, *J. Mater. Chem. A* **5**, 3039 (2017).

[30] L. Wang, P. Hu, Y. Long, Z. Liu, and X. He, *J. Mater. Chem. A* **5**, 22855 (2017).

[31] B. Anasori, M. R. Lukatskaya, and Y. Gogotsi, *2D Metal Car- bides and Nitrides (MXenes)* (Springer International Publishing, Cham, 2019).

[32] M. Khazaei, A. Mishra, N. S. Venkataramanan, A. K. Singh, and S. Yunoki, *Curr. Opin. Solid State Mater. Sci.* **23**, 164 (2019).

[33] M. A. Hope, A. C. Forse, K. J. Griffith, M. R. Lukatskaya, M. Ghidiu, Y. Gogotsi, and C. P. Grey, *Phys. Chem. Chem. Phys.* **18**, 5099 (2016).

[34] H. W. Wang, M. Naguib, K. Page, D. J. Wesolowski, and Y. Gogotsi, *Chem. Mater.* **28**, 349 (2016).

[35] D. Magne, V. Mauchamp, S. Célérier, P. Chartier, and T. Cabioc’h, *Phys. Chem. Chem. Phys.* **18**, 30946 (2016).

[36] K. D. Fredrickson, B. Anasori, Z. W. Seh, Y. Gogotsi, and A. Vojvodic, *J. Phys. Chem. C* **120**, 28432 (2016).

[37] K. J. Harris, M. Bugnet, M. Naguib, M. W. Barsoum, and G. R. Goward, *J. Phys. Chem. C* **119**, 13713 (2015).

[38] M. Naguib, M. Kurtoglu, V. Presser, J. Lu, J. Niu, M. Heon, L. Hultman, Y. Gogotsi, and M. W. Barsoum, *Adv. Mater.* **23**, 4248 (2011).

[39] A. Lipatov, H. Lu, M. Alhabeb, B. Anasori, A. Gruverman, Y. Gogotsi, and A. Sinitskii, *Sci. Adv.* **4**, eaau0491 (2018).

[40] M. Naguib, O. Mashtalir, J. Carle, V. Presser, J. Lu, L. Hultman, Y. Gogotsi, and M. W. Barsoum, *ACS Nano* **6**, 1322 (2012).

[41] J. Yang, M. Naguib, M. Ghidiu, L. M. Pan, J. Gu, J. Nanda, J. Halim, Y. Gogotsi, and M. W. Barsoum, *J. Am. Ceram. Soc.* **99**, 660 (2016).

[42] P. Chakraborty, T. Das, D. Nafday, L. Boeri, and T. Saha- Dasgupta, *Phys. Rev. B* **95**, 184106 (2017).

[43] B. Anasori, Y. Xie, M. Beidaghi, J. Lu, B. C. Hosler, L. Hultman, P. R. C. Kent, Y. Gogotsi, and M. W. Barsoum, *ACS Nano* **9**, 9507 (2015).

[44] M. Khazaei, A. Ranjbar, M. Arai, and S. Yunoki, *Phys. Rev. B* **94**, 125152 (2016).

[45] R. Khaledialidusti, B. Anasori, and A. Barnoush, *Phys. Chem. Chem. Phys.* **22**, 3414 (2020).

[46] M. Khazaei, M. Arai, T. Sasaki, C. Y. Chung, N. S. Venkataramanan, M. Estili, Y. Sakka, and Y. Kawazoe, *Adv. Funct. Mater.* **23**, 2185 (2013).

[47] J. Yang, X. Zhou, X. Luo, S. Zhang, and L. Chen, *Appl. Phys. Lett.* **109**, 203109 (2016).

[48] M. Khazaei, A. Ranjbar, M. Ghorbani-Asl, M. Arai, T. Sasaki, Y. Liang, and S. Yunoki, *Phys. Rev. B* **93**, 205125 (2016).

[49] Y. Bai, K. Zhou, N. Srikanth, J. H. L. Pang, X. He, and R. Wang, *RSC Adv.* **6**, 35731 (2016).

[50] H. Lashgari, M. R. Abolhassani, A. Boochani, S. M. Elahi, and J. Khodadadi, *Solid State Commun.* **195**, 61 (2014).

[51] J. L. Hart, K. Hantanasirisakul, A. C. Lang, B. Anasori, D. Pinto, Y. Pivak, J. T. van Omme, S. J. May, Y. Gogotsi, and M. L. Taheri, *Nat. Commun.* **10**, 522 (2019).

[52] G. Gao, G. Ding, J. Li, K. Yao, M. Wu, and M. Qian, *Nanoscale* **8**, 8986 (2016).

[53] C. Si, J. Zhou, and Z. Sun, *ACS Appl. Mater. Interfaces* **7**, 17510 (2015).

[54] A. N. Gandi, H. N. Alshareef, and U. Schwingenschlögl, *Chem. Mater.* **28**, 1647 (2016).

[55] X.-H. Zha, J. Zhou, Y. Zhou, Q. Huang, J. He, J. S. Francisco, K. Luo, and S. Du, *Nanoscale* **8**, 6110 (2016).

[56] X.-H. Zha, Q. Huang, J. He, H. He, J. Zhai, J. S. Francisco, and S. Du, *Sci. Rep.* **6**, 27971 (2016).

[57] Q. Wan, S. Li, and J. B. Liu, *ACS Appl. Mater. Interfaces* **10**, 6369 (2018).

[58] X. Xie, K. Kretschmer, B. Anasori, B. Sun, G. Wang, and Y. Gogotsi, *ACS Appl. Nano Mater.* **1**, 505 (2018).

[59] J. Zhu, E. Ha, G. Zhao, Y. Zhou, D. Huang, G. Yue, L. Hu, N. Sun, Y. Wang, L. Y. S. Lee, C. Xu, K. Y. Wong, D. Astruc, and P. Zhao, *Coord. Chem. Rev.* **352**, 306 (2017).

[60] S. J. Kim, H.-J. Koh, C. E. Ren, O. Kwon, K. Maleski, S.-Y. Cho, B. Anasori, C.-K. Kim, Y.-K. Choi, J. Kim, Y. Gogotsi, and H.-T. Jung, *ACS Nano* **12**, 986 (2018).

[61] A. Sarycheva, A. Polemi, Y. Liu, K. Dandekar, B. Anasori, and Y. Gogotsi, *Sci. Adv.* **4**, eaau0920 (2018).

[62] L. Dong, H. Kumar, B. Anasori, Y. Gogotsi, and V. B. Shenoy, *J Phys. Chem. Lett.* **8**, 422 (2017).

[63] J. Liu, H. Bin Zhang, R. Sun, Y. Liu, Z. Liu, A. Zhou, and Z. Z. Yu, *Adv. Mater.* **29**, 1702367 (2017).

[64] H. Fas handi, I. Ivády, P. Eklund, A. L. Spetz, M. I. Katsnelson, and I. A. Abrikosov, *Phys. Rev. B* **92**, 155142 (2015).

[65] H. Weng, A. Ranjbar, Y. Liang, Z. Song, M. Khazaei, S. Yunoki, M. Arai, Y. Kawazoe, Z. Fang, and X. Dai, *Phys. Rev. B* **92**, 075436 (2015).

[66] Y. Liang, M. Khazaei, A. Ranjbar, M. Arai, S. Yunoki, Y. Kawazoe, H. Weng, and Z. Fang, *Phys. Rev. B* **96**, 195414 (2017).

[67] S. Zhang, W. Ji, C. Zhang, S. Zhang, P. Li, S. Li, and S. Yan, *Chin. Phys. Lett.* **35**, 087303 (2018).

[68] C. Si, K. H. Jin, J. Zhou, Z. Sun, and F. Liu, *Nano Lett.* **16**, 6584 (2016).

[69] L. Li, *Comput. Mater. Sci.* **124**, 8 (2016).

[70] R. Meshkian, Q. Tao, M. Dahlqvist, J. Lu, L. Hultman, and J. Rosen, *Acta Mater.* **125**, 476 (2017).

[71] P. Hohenberg and W. Kohn, *Phys. Rev.* **136**, B864 (1964).

[72] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).

[73] G. Kresse and D. Joubert, *Phys. Rev. B* **59**, 1758 (1999).

[74] G. Kresse and J. Hafner, *Phys. Rev. B* **47**, 558 (1993).

[75] G. Kresse and J. Furthmüller, *Phys. Rev. B* **54**, 11169 (1996).

[76] A. V. Krukau, O. A. Vydrov, A. F. Izmaylov, and G. E. Scuseria, *J. Chem. Phys.* **125**, 224106 (2006).

[77] H. J. Monkhorst and J. D. Pack, *Phys. Rev. B* **13**, 5188 (1976).

[78] L. Fu and C. L. Kane, *Phys. Rev. B* **76**, 045302 (2007).

[79] A. A. Soluyanov and D. Vanderbilt, *Phys. Rev. B* **83**, 235401 (2012).

[80] D. Gresch, G. Autès, O. V. Yazyev, M. Troyer, D. Vanderbilt, B. A. Bernevig, and A. A. Soluyanov, *Phys. Rev. B* **95**, 075146 (2017).

[81] A. A. Mostofi, J. R. Yates, Y.-S. Lee, I. Souza, D. Vanderbilt, and N. Marzari, *Comput. Phys. Commun.* **178**, 685 (2008).

[82] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.102.075306 for the detailed list of atomic and electronic properties, formation energy profiles, phonon spectra, band structures and discussion on strain effects.