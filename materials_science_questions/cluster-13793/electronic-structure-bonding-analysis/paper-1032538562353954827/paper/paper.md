# Tailoring light holes in $\beta$-Ga₂O₃ via Anion-Anion Antibonding Coupling

Ke Xu¹†, Qiaolin Yang²,³†, Wenhao Liu², Rong Zhang¹, Zhi Wang²*, and Jiandong Ye¹*

¹ School of Electronic Science and Engineering, Nanjing University, Nanjing 210023, China.
² State Key Laboratory of Superlattices and Microstructures, Institute of Semiconductors, Chinese Academy of Sciences,
Beijing 100083, China
³ School of Physics and Zhejiang Province Key Laboratory of Quantum Technology and Device, Zhejiang University,
Hangzhou 310027, China.

†K. X. and Q.-L. Y. contributed equally to this work.

## AUTHOR CONTRIBUTIONS

K.X. and Q.-L.Y. contributed equally to this work. J.-D.Y., R.Z. and Z.W. conceived and supervised the project. K.X. and
Q.-L.Y. developed the idea, designed the research, and implemented the computational algorithm. K.X. and Q.-L.Y.
collated the computational data, performed the electronic structure calculations. K.X., Q.-L.Y., W.-H.L., Z.W., and J.D.Y.
analyzed the AAAC mechanism and polaronic effect, plotted figures, and wrote the manuscript.

A significant limitation of wide-bandgap materials is their low hole mobility related to localized holes
with heavy effective masses ($m_h^*$). We identify in low-symmetric wide-bandgap compounds an anion-
anion antibonding coupling (AAAC) effect as the intrinsic factor behind hole localization, which explains
the extremely heavy $m_h^*$ and self-trapped hole (STH) formation observed in gallium oxide ($\beta$-Ga₂O₃). We
propose a design principle for achieving light holes by manipulating AAAC, demonstrating that specific
strain conditions can reduce $m_h^*$ in $\beta$-Ga₂O₃ from 4.77 $m_0$ to 0.38 $m_0$, making it comparable to the
electron mass (0.28 $m_0$), while also suppressing STH. The light holes show significant anisotropy,
potentially enabling two-dimensional transport in bulk material. This study provides a fundamental
understanding of hole mass enhancement and STH formation in novel wide-bandgap materials and
suggest new pathways for engineering hole mobilities.


### I. INTRODUCTION

A well-known challenge in the development of wide-bandgap material devices lies in how to reduce the difference in magnitude between electron and hole mobilities. Compounds such as SiC, GaN, ZnO, and $\text{Ga}_2\text{O}_3$ [1–5] not only exhibit flat valence band maximum (VBM) and the consequential heavy effective masses of hole ($m_h^*$) but also hold strong hole-phonon interactions that can cause significant carrier scattering, leading to reduced carrier lifetimes [3,6]. The phenomenon of self-trapped holes (STH), or hole polarons, where excess holes are trapped by the local potential wells created by themselves distorting the lattice nearby, provides evidence of this strong hole-phonon coupling [7–9]. These effects constrain the delocalization of hole states and inherently limit the *intrinsic* hole mobility in wide-gap materials. To enhance hole mobility, it is crucial to investigate the physical origins of the heavy $m_h^*$ and the formation of STH.

Although significant progress has been made in synthesizing high-quality, low-cost single crystals and heterojunctions of wide-gap compounds [10–12], the understanding of hole mass enhancement and hole polaron formation remains incomplete and contentious. In a conventional view, the observed heavy $m_h^*$ is attributed to the orbital composition of the VBM. For example, in SiC, GaN, and ZnO, the VBMs predominantly comprise the $2p$ (or, $2s$-$2p$ hybrid) orbitals of C, N, and O, respectively [4,13,14]. These orbitals have low principal quantum numbers, resulting in deep energy levels and strong localization. Consequently, it appears that the hole masses in these compounds are inherently difficult to tune, given that the electronegativity of the anion and the orbital quantum number are fundamental properties.

However, recent discussions suggest that even in the pristine, defect-free crystals, the orbital composition of the band edge may not exclusively account for the heavy $m_h^*$. Evidence includes studies demonstrating that the hole mass can be remarkably lightened by strain, e.g., in GaN [15], which was explained as the band order reversion caused by changes in crystal-field splitting. Nonetheless, this presents difficulties in explaining the magnitude difference in hole mass between wide-gap materials with the same orbital composition of VBM. For instance, $\text{Ga}_2\text{O}_3$, a wide-gap compound with an ultraviolet bandgap and a complex phase diagram, has garnered substantial attention [16–18] Its hole mass has been reported as unusually heavy in both photoemission experiments [19–21] and *ab initio* calculations [22–26], holding a range from $3\ m_0$ up to $40\ m_0$ ($m_0$ is the bare electron mass). This contrasts with materials like SiC, GaN, and ZnO, which all have VBMs composed of anion $2p$ orbitals, yet

exhibit more moderate hole effective masses of ~0.6-1.0 $m_0$ [27,28] , 1.1~1.6 $m_0$ [29,30], and ~0.8 $m_0$ [5], respectively. Furthermore, spontaneous STH has been observed in high-quality Ga₂O₃ to play a crucial role in optical emission and electrical transport [8,16,31], a unique phenomenon in wide-gap materials. All these findings suggest that there may be additional, yet overlooked or neglected, factors that dominate the hole mass and the formation of STH.

In this work, we aim to address the gap between experimental observations and physical understandings. Using density functional theory (DFT) for the ground-state β-Ga₂O₃, we achieved excellent agreements with experimental observations for both the lattice and electronic structures (Table I). Our results reveal that the dominant mechanism of the hole mass enhancement and STH formation is an anion-anion antibonding coupling (AAAC) between several oxygen pairs. Despite the distances between these oxygens being significantly larger than the covalent radius, the strengths of AAAC are remarkably high. This insight led us to the design principle for tuning the hole masses and STH by modifying the strength of AAAC, following which we investigated the effects of strain on the hole states, as strain is a straightforward method to control inter-atom distances hence the coupling. We found that uniaxial tensile strain along the $b$ axis or biaxial compressive strain along $a$-$c$ plane can modulate the AAAC effect as expected and achieve step-function changes on the hole masses. Specifically, the $m_{h\parallel c^*}^*$ (hole mass along $c^*$) decreases to 8% of its original value, from 4.77 $m_0$ to 0.38 $m_0$, making it comparable to the mass of the electron (0.28 $m_0$ ). The conductivity mass $m_h^*$, $(m_h^*)^{-1} = \left[(m_{h\parallel a^*}^*)^{-1} + (m_{h\parallel b^*}^*)^{-1} + (m_{h\parallel c^*}^*)^{-1}\right]/3$, also decreases to 29% of its original state, from 3.47 $m_0$ to 0.99 $m_0$. The critical strains for such a transition are 1.5% for the uniaxial tensile strain and 0.7% for the biaxial compressive strain. The resulting light holes are highly anisotropic with $m_{h\parallel b^*}^* \approx 70m_{h\parallel c^*}^*$, indicating potential for low-dimensional transport in pristine bulk Ga₂O₃ without the need for interfaces. Strain also suppressed the formation of STH as evidenced by the decreased formation energy of hole polaron. We believe that understanding and manipulating the AAAC effect to control hole mass and STH could pave the way for the design of next-generation wide-gap materials with tailored electronic properties.

## II. THE CRYSTALLOGRAPHIC AND ELECTRONIC STRUCTURES OF β-Ga₂O₃.

Fig. 1 shows the (a) conventional (20-atom) and (b) primitive (10-atom) crystallographic structures

of the $\beta$-Ga₂O₃. We adopt the lattice vectors and internal atomic coordinates fully relaxed by DFT. The calculated electronic band structure in the first BZ is plotted in Fig. 1(c), while the first BZ and k-points are presented in the inset. All our DFT calculations use the HSE exchange-correlation functional [32,33]. The computational details are given in the Appendix section. The calculated band structure holds an indirect, 4.91 eV gap between the CBM on $\Gamma$ and the global VBM on $M_2$-$D$ path (marked as point $I$) 32 meV higher than the VBM on $\Gamma$ (A more detailed band structure can be found in the supporting information Fig. S1). As the validation of our results, we summarize in Table I the comparisons between this work and experimental observations. All lattice and electronic properties are in good agreement. Note that there are arguments about the position of global VBM. The experimental observation of accurate VBM is yet uncertain due to the wide gap and the flat band edge; in experiment it is reported to be at or nearby $M$ (identical to $M_2$) and about 50 meV higher than that on $\Gamma$ [19–21,34,35] while in previous theoretical works it is claimed to be on the $M_2$-$D$ path [36]. Our calculated hole masses along the three reciprocal directions $a^*$, $c^*$, and $c^*$(directions are shown in the inset of Fig. 1(c)) are 3.06, 3.06, and 4.77 $m_0$, respectively, while the conductivity mass $m_h^*$ is 3.47 $m_0$..Note that these masses are significantly larger than that of heavy holes in SiC (0.6~1.0 $m_0$) [27,28], GaN (1.1~1.6 $m_0$) [29,30], and ZnO (~0.8 $m_0$) [5].

Table I: Comparison of properties in monoclinic $\beta$-Ga₂O₃ from experiments, previous theoretical works, and from this work. Hole masses are calculated along three reciprocal directions $a^*$, $b^*$ and $c^*$, while the electron mass is isotropic. All our DFT results use the HSE exchange-correlation functional [32,33].

<table>
  <thead>
    <tr>
      <th colspan="2"></th>
      <th>Experiment</th>
      <th>Theory</th>
      <th>This work</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Crystallographic</td>
      <td>$a$ (Å)</td>
      <td>12.23 ± 0.02 [a]</td>
      <td>12.25 [b]</td>
      <td>12.25</td>
    </tr>
    <tr>
      <td>$b$ (Å)</td>
      <td>3.04 ± 0.01 [a]</td>
      <td>3.05 [b]</td>
      <td>3.04</td>
    </tr>
    <tr>
      <td>$c$ (Å)</td>
      <td>5.80 ± 0.01 [a]</td>
      <td>5.84 [b]</td>
      <td>5.80</td>
    </tr>
    <tr>
      <td>$\beta$ (°)</td>
      <td>103.7 ± 0.3 [a]</td>
      <td>103.9 [b]</td>
      <td>103.83</td>
    </tr>
    <tr>
      <td rowspan="4">Electronic</td>
      <td>Gap (eV)</td>
      <td>4.85 (indirect) [c]</td>
      <td>4.83 (indirect) [b]</td>
      <td>4.91 (indirect)</td>
    </tr>
    <tr>
      <td>Electron mass ($m_0$)</td>
      <td>0.28 ± 0.01 [c]</td>
      <td>0.28 [b]</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>Hole mass ($m_0$)</td>
      <td>18.75 [d]</td>
      <td>40 ($b^*$), 0.4 ($c^*$) [b]<br>6.14 ($xx$), 2.9 ($yy$), 4.19 ($zz$) [e]<br>3.3 [f], 8.72 [g]</td>
      <td>3.06 ($a^*$), 3.06 ($b^*$), 4.77 ($c^*$)</td>
    </tr>
    <tr>
      <td>CBM in k-space</td>
      <td>$\Gamma$ [c]</td>
      <td>$\Gamma$ [b]</td>
      <td>$\Gamma$</td>
    </tr>
  </tbody>
</table>


VBM in k-space
$M$ [c] [*]
along $M-A$ [b][e] [*]
along $M_2-D$ [h]
along $M_2-D$

[a] ref [37] ; [b] ref [22] ; [c] ref [19] ; [d] ref [38] ; [e] ref [24] ; [f] ref [23] ; [g] ref [39] ; [h] ref [36] ; [*] the points $M$ (0.5, 0.5, 0.5) and $M_2$ (-0.5, 0.5, 0.5) are identical; the paths $M-A$ and $M_2-D$ are the same direction along $b^*$.

![](./images/1032538562353954827_1.jpg)

![](./images/1032538562353954827_2.jpg)

FIG. 1. Crystal structure, band structure, and atomic orbital coupling of $\beta$-Ga₂O₃. (a) The conventional and (b) the primitive cell, where the shaded green areas are (GaO₆) and (GaO₄) polyhedrons. (c) The electronic band structure calculated by DFT, showing the indirect gap between $\Gamma$ (CBM) and $I$ (global VBM, marked by orange) on $M_2$-D path, and the calculated conductivity effective masses. Inset of (c) shows the primitive first Brillouin zone. Note that the orientations in (b) and inset of (c) are consistent. (d) The atomic orbital projected density of states near VBM onto Ga and O. (e) The projected density of COHP near VBM over all O-O pairs (red) and over all Ga-O pairs (blue), where positive and negative values indicate bonding and antibonding coupling. We mark in (e) the energy range where the O-O antibonding coupling dominates. All our DFT results use the HSE exchange-correlation functional.

### III. THE OXYGEN-DOMINATED VBM AND THE ANION-ANION ANTIBONDING COUPLING.

To understand the physical origin of the heavy hole mass, we firstly do the projection of the density of states (PDOS) onto different atomic orbitals. As shown in Fig. 1(d), within an energy range from -2 eV

to 0 eV (VBM has been chosen as energy zero), the DOS comes mostly from oxygen orbitals with only negligible contribution from gallium, indicating an anion-dominated VBM. We then investigate the coupling between different orbitals by calculating the crystal orbital Hamiltonian population (COHP) [40]. The absolute value of COHP represents the coupling strength between specific orbitals, while its sign reveals either such coupling is bonding (if the sign is positive) or antibonding (if it is negative). Details about the COHP calculations are given in the Appendix section. In this work, we mark the COHP between the $\mu$ orbital of the $i^{th}$ atom and the $v$ orbital of the $j^{th}$ atom at a given energy $\varepsilon$ as $\text{COHP}_{\mu i, v j}(\varepsilon)$.

We firstly calculate the total COHP for all Ga-O coupling and all O-O coupling by using

$$
\mathrm{COHP}_{\mathrm{Ga}-\mathrm{O}}(\varepsilon)=\sum_{\mu, v \in s, p, d} \sum_{i \in \mathrm{Ga}, j \in \mathrm{O}} \mathrm{COHP}_{\mu i, v j}(\varepsilon) \tag{1}
$$

$$
\mathrm{COHP}_{\mathrm{O}-\mathrm{O}}(\varepsilon)=\sum_{\mu, v \in s, p, d} \sum_{i \neq j \in \mathrm{O}} \mathrm{COHP}_{\mu i, v j}(\varepsilon) \tag{2}
$$

notice that in Eq. (2) we avoid the self-interaction ($i \neq j$). Fig. 1(e) shows these two COHPs, both calculated from DFT wavefunctions. It can be seen that the VBM is dominated by an anion-anion antibonding coupling (AAAC) of O-O rather than the conventional Ga-O bonding coupling, the latter of which rises only when going into deeper energy of valence bands. The existence of AAAC can be illustrated by another way, that is to calculate the decomposition of the total COHP on wave vectors $\mathbf{k}$, i.e., $\text{COHP}(\varepsilon, \mathbf{k})$. It allows us to overlay the COHP onto the electronic band structure to investigate the distribution of orbital coupling in momentum space. It can be seen from Fig. 2(a) that the COHP of VBM show significant antibonding characteristics along the whole BZ. The most negative value is -0.182 on $\Gamma$, while on $I$ (global VBM) it is -0.08. As we delve deeper into the matrices of $\text{COHP}_{\mu i, v j}(\text{VBM}, \Gamma)$ and $\text{COHP}_{\mu i, v j}(\text{VBM}, I)$ (Fig. 2(b) and Fig. 2(c)), we find that such antibonding coupling on VBM come from very specific oxygen pairs. For VBM on $\Gamma$, the antibonding coupling is primarily characterized by the O-O $p_z$-$p_z$ interactions (the top-right triangle region in Fig. 2(b)) among which the strongest one is between $\mathrm{O_2}$-$\mathrm{O_5}$ pair, while all other couplings (the Ga-O and Ga-Ga regions) are negligible. While for VBM on $I$ the dominant contribution is from the $p_x$-$p_x$ antibonding between $\mathrm{O_1}$-$\mathrm{O_4}$.

![](./images/1032538562353954827_3.jpg)

FIG. 2. The antibonding coupling between different oxygens. (a) The $\text{COHP}(\varepsilon,k)$ plotted on band structure showing the density of COHP as the function of energy and wave vector. The two numbers in small frames are the $\text{COHP}(\varepsilon,k)$ value of VBM at $I$ and $\Gamma$, respectively. The overall $\text{COHP}(\varepsilon,k)$ can be furtherly decomposed into matrix $\text{COHP}_{\mu i, \nu j}(\varepsilon,k)$ for different orbital pairs $\mu i$-$vj$, as visualized by triangle matrices in (b) for VBM at $\Gamma$, and in (c) for VBM at $I$, where each solid square represents one coupling, going through all $Ga$-$p$ and $O$-$p$ orbitals. Note that all diagonal squares are blank as the self-interactions are ignored. Among all the coupling, the $\text{O}_2\text{-O}_5$ $p_z$-$p_z$ and the $\text{O}_1\text{-O}_4$ $p_x$-$p_x$ coupling are the strongest ones and hence marked by red texts. The three numbers in (b) (as well as in (c)) are the sum of the matrix elements over all Ga-Ga coupling, all Ga-O coupling, and all O-O coupling, respectively. The distributions in real space of the real and imaginary parts of VBM wavefunction at $\Gamma$ (d) and $I$ (e), with all Ga and O atoms labeled.

Such an AAAC effect in $\beta\text{-Ga}_2\text{O}_3$ seems to be non-trivial, given that even the closest oxygens are separated by over $3$ Å, a distance much larger than their covalent radius $0.7$ Å. In fact, it can be understood by the following two facts.

(a) The unique crystallographic feature of $\text{Ga}_2\text{O}_3$. Fig. 2(d) and Fig. 2(e) show the atomistic model of the conventional cell of $\beta\text{-Ga}_2\text{O}_3$, together with the real-space distribution of VBM wavefunctions on $\Gamma$ and on $I$, respectively. It can be seen that between the $\text{O}_2$ and $\text{O}_5$ - where the strongest AAAC occurs - there are "void" region along the $c$ axis, that these two oxygens are not only close to each other ($3.0$ Å,

which is the shortest distance among all O-O pairs), but have no cations (Ga) in between them, leaving enough space for their $p_z$ orbitals to interact with each other; the same situation exists for $O_1$ and $O_4$ along the $a$ axis.

(b) The symmetry and ligand orbital interactions. Firstly, the $\beta$-Ga₂O₃ has space group $C2/m$ with severely distorted octahedral and tetrahedral Ga-O local clusters, and hence relatively weak symmetry restrictions on orbital coupling, i.e., almost all O and Ga orbitals can interact with each other. Secondly, for each formula unit, the two Ga atoms have in total 8 orbitals that can be paired (one $4s$ and three $4p$ for each Ga, while $3d$ are too deep in energy to be involved, see supporting information Fig. S2), while the three O atoms have in total 9 orbitals (three $2p$ for each O, while $2s$ are too deep in energy). It means that there always leaves one O orbital not coupled with Ga orbitals per formula unit; these "leftovers" then could form O-O bonding/antibonding states if they meet the proper conditions with respect to symmetry and distance.

## IV. THE AAAC ENHANCES THE HOLE MASS AND THE FORMATION OF STH.

Now, given these findings in Ga₂O₃ as discussed above, at first glance, one may think that (i) the AAAC effect is a consequence of (ii) the anion-dominated VBM, and so as (iii) the heavy hole mass, i.e., (ii) results in (i) and (iii). However, such causality is in fact reverse, that (i) actually results in (ii) and (iii). We provide the discussion as below:

(1) AAAC effect results in the oxygen-dominated VBM. Indeed, an anion-dominated VBM can be found in other compounds, e.g., ionic compounds and ligand-hole transition-metal oxides ( [41]) such as titanates, vanadates, and nickelates. Ga₂O₃, however, does not belong to either case. Firstly, the strong Ga-O bonding effect on deeper valence bands (Fig. 1(e), where the Ga-O COHP is positive) shows a covalent nature rather than ionic. Secondly, in a ligand-hole transition-metal oxide, the symmetries of crystal allow bonding/antibonding between $O$-$p$ and transition metal $d$-orbitals that have the same irreducible representation, but forbid those who do not; these bonding $O$-$p$ and metal-$d$ orbitals are hence pushed by Coulomb repulsion into deeper/higher energies, and leave a VBM holding no-bonding $O$-$p$ orbitals. The low-symmetric Ga₂O₃, as we discussed above, cannot host such strong symmetry restrictions on orbital coupling. Therefore, if one only considers the metal-oxygen coupling as in the conventional case, it should not have strong enough Coulomb repulsion to separate in energy the O and

Ga contributions and make an oxygen-dominated VBM. However, the existence of AAAC effect now offers extra repulsion from the O-O bonding states below, which eventually pushes the AAAC state up in energy to form the VBM.

(2) AAAC effect leads to hole mass enhancement. After the AAAC VBM being pushed up in energy, the internal gap between the VBM and other valence bands are opened by the avoid-crossing mechanism. As a consequence, the VBM state has a narrow bandwidth <1 eV (as shown in Fig. 2(a)). This could introduce a significant mass enhancement for the holes. A brief intuition originates from that the factors that control effective masses can be gleaned qualitatively from the $\boldsymbol{k} \cdot \boldsymbol{p}$ perturbation theory [42],

$$
\frac{1}{m_{\mathrm{VBM}, \mathbf{k} \alpha}^{*}}=\frac{1}{m_{0}}+\frac{2}{m_{0}{ }^{2}} \sum_{n \neq \mathrm{VBM}} \frac{\left|\left\langle\mathrm{VBM}, \mathbf{k}\left|p_{\| \alpha}\right| n \mathbf{k}\right\rangle\right|^{2}}{\varepsilon_{\mathrm{VBM}, \mathbf{k}}-\varepsilon_{n \mathbf{k}}} \tag{3}
$$

where $m_{\mathrm{VBM}, \mathbf{k} \alpha}^{*}$ is the effective mass of VBM at wave vector $\mathbf{k}$ along direction $\alpha$, $m_{0}$ is the bare electron mass, $\left\langle\mathrm{VBM}, \mathbf{k}\left|p_{\| \alpha}\right| n \mathbf{k}\right\rangle$ is the transition dipole moment (TDM) between VBM and state $n$ along direction $\alpha$, and $\varepsilon_{\mathrm{VBM}, \mathbf{k}}$ and $\varepsilon_{n \mathbf{k}}$ are the eigenvalue of VBM and state $n$, respectively. The sum is over all states except VBM itself. A trivial case in semiconductors is when there exists a large and negative term at the Van Hove singularity between CBM-VBM due to the strong TDM while all other terms are relatively weak. The sum is hence significantly negative and eventually results in a light and negative $m_{\mathrm{VBM}, \mathbf{k} \alpha}^{*}$, i.e., a light hole state. While in $\beta-\mathrm{Ga}_{2} \mathrm{O}_{3}$, (i) the wide gap enhances the denominator $\varepsilon_{\mathrm{VBM}, \mathbf{k}}-\varepsilon_{\mathrm{CBM}, \mathbf{k}}$, while (ii) the AAAC effect weakens the numerator between CBM-VBM and induces extra positive terms between VBM and deeper valence bands. Here we would take the VBM at $\Gamma$ point as an example. Note that the space group of $\beta-\mathrm{Ga}_{2} \mathrm{O}_{3}$ is $C 2 / m$, while the little group at $\Gamma$ is $C_{2 h}$ and has 4 irreducible representations $A_{g}$, $A_{u}$, $B_{g}$ and $B_{u}$. As discussed above and shown in Fig. 2(d), in the real space the VBM at $\Gamma$ mainly distributes between O-O pairs distanced from Ga nuclei, which suppresses the overlap in real space between VBM and CBM (the latter being Ga 4s orbitals). Moreover, Fig. 2(d) reveals that the VBM at $\Gamma$ has an irreducible representation of $B_{u}$ $(\Gamma_{2}^{-})$. The symmetry analysis then teaches that states that can hold non-zero TDM to VBM would be $A_{g}$ $(\Gamma_{1}^{+})$ and $B_{g}$ $(\Gamma_{2}^{+})$, while within the range of 2 eV below VBM there are many O-p VBs with these two representations (Table SI), leading to extra positive terms in the sum in Eq. (3), and compensating the negative term from CBM-VBM coupling. In the end, the heavy hole mass at $\Gamma$ can be a consequence of the sum in Eq. (3) being only slightly negative. This approach can also explain the positive hole mass (inverted sign) at k-points such as

$M_2$, $A$ and $Y_2$, as at these k-points the CBM-VBM gap goes larger while the VBM-deeper-VB gaps are relatively consistent, in which case the sum in Eq. (3) becomes positive and, eventually, $m_{\text{VBM,k}\alpha}^\ast$ becomes positive.

(3) *AAAC effect enhances the formation of STH.* The acceptors in $\text{Ga}_2\text{O}_3$, once ionized, will contribute excess holes to occupy firstly the AAAC VBM. The O-O antibonding strength will hence be weakened, and the distance between these O-O pairs are shortened. As the AAAC VBM is highly localized, it will induce local distortions, which will in-return trap the excess holes. Such a positive feedback will eventually enhance the formation of STH.

## V. THE DESIGN PRINCIPLE TO TUNE THE HOLE MASS IN $\boldsymbol{\beta}$-$\boldsymbol{\text{Ga}_2\text{O}_3}$

In previous section, we have investigated the origin of AAAC effect and its consequence on the hole mass enhancement and formation of STH. It then enlightens us the design principle if one could use the AAAC effect as a "route to light holes" in $\beta$-$\text{Ga}_2\text{O}_3$. As can be seen from Fig. 2(a)(b), the VBM at $\varGamma$ point has O-O $p_z$-$p_z$ AAAC in the majority and hosts a much lighter hole mass, but is slightly lower in energy than the global VBM on $I$, the latter of which has the heavy mass and AAAC between O-O $p_x$-$p_x$. Therefore, by (1) enhancing the O-O $p_z$-$p_z$ coupling and/or (2) suppressing the $p_x$-$p_x$ ones, one can reverse the order in the energy of the VBM at $\varGamma$ point and the one on $I$, and hence achieves a light hole mass. Following this design principle, one of the simplest ways to control the O-O coupling is to use strain to tune the O-O distance along different directions. Therefore, in the following sections, we show the predictions on hole mass and STH formation under strains.

## VI. STRAIN-INDUCED LIGHT HOLES AND THE QUASI-TWO-DIMENSIONAL TRANSPORT BEHAVIOR

We have tested all types of uniaxial, biaxial, and hydrostatic strains, and found that the most efficient strain to lighten to hole mass is (a) uniaxial tensile strain along the $b$ axis and (b) biaxial compressive strain on $a$-$c$ plane. As the evolutions of hole properties are almost identical under (a) and (b) but differ only by the value of the critical strain, in the following sections we will discuss (a) as the example. Cases for other strains are summarized in the supporting information. As illustrated in Fig. 3(a), with the tensile strain increasing, the band gap decreases, while the VBM on $\varGamma$ rises in energy faster than that on $I$ point. At a critical strain of 1.5%, the VBM on $\varGamma$ becomes the new global VBM, which also indicates a

transition from indirect to direct band gap, as demonstrated in Fig. 3(c). Such band edge transition is also observed in the compressive biaxial strain on the $a$-$c$ plane with a smaller critical strain of 0.7% (see Fig. S3 (a)(b)). As the consequence of the shift of VBM in momentum space, we observe a direct, step-function-like changes in $m_{h}^{*}$ near the critical strain (Fig. 3(b)). For instance, the hole mass along $c^{*}$ ($m_{h\parallel c^{*}}^{*}$) drops suddenly from 4.77 to $0.38\ m_{0}$, decreasing to 8% of its original value brings it comparable to the effective mass of electrons ($m_{e}^{*}=0.28\ m_{0}$). This further causes the conductivity effective mass ($m_{h}^{*}$) decreasing from the $3.47\ m_{0}$ to $0.99\ m_{0}$.

Furthermore, we also find that the VBM now becomes highly anisotropic, e.g., the hole mass along $b^{*}$ is approximately 70 times the mass along $c^{*}$, $m_{h\parallel b^{*}}^{*}\approx70m_{h\parallel c^{*}}^{*}$. It potentially reveals a quasi-two-dimensional transport behavior within the 3-dimensional bulk $\text{Ga}_{2}\text{O}_{3}$. The low-dimensional behavior of holes can also be visualized from the Fermi surfaces shown in Fig. 3(d), (e). In both the unstrained and the 2%-tensile-strained cases, the Fermi surfaces are chosen as the isosurfaces of valence bands at -0.05 eV (~2kT at 300 K) below VBM to mimic the p-doped crystal at room temperature. Note that the more spreading the hole has in momentum space, the more localization and difficulty in transport it has in real space. The unstrained Fermi surfaces spread almost isotropically in the whole first BZ (i.e., heavily localized in all directions in real space), while the tensile-strained Fermi surfaces show much smaller spreading along $a^{*}$ and $c^{*}$, indicating the hole mass lightening along these two directions.

![](./images/1032538562353954827_4.jpg)

FIG. 3. Strain-induced modulation on VBM in $\beta$-Ga₂O₃. (a) Changes in band gap and VBM energies at $\Gamma$ and $I$ under uniaxial strain along the $b$ axis. $E_{\text{VBM}}^{0}$ is the VBM energy while the superscript '0' means no strain. The vertical dash line indicates the critical strain of direct-indirect gap transition. (b) Hole masses of VBM under strain. (c) Band structure under a 2.0% tensile strain along $b$, compared to the one in the unstrained case; valence bands and conduction bands have been aligned to CBM and VBM, respectively. Fermi surfaces upon (d) zero strain and (e) 2.0% tensile strain along the $b$ axis, drawn for an energy -0.05 eV below VBM, which mimics the distribution of holes in a p-doped crystal.

Furthermore, we find that the evolutions of $m_{h}^{*}$ under strain indeed follow our design principle, that they are the consequence of the modulation on AAAC strengths. As the strongest AAAC is on O₂-O₅, followed by the ones on O₁-O₄, O₁-O₆, and O₃-O₄ (see the labels for all Ga and O in Fig. 4(a)), we trace under strain the variation of distance between these O pairs (Fig. 4(b)), and the differential of COHP ($\Delta$COHP; we use the COHP under zero strain as the reference) on them (Fig. 4(c)-(e)). It can be seen from Fig. 4(b) that when applying the uniaxial tensile strain along the $b$ axis, the distance between O₁-O₄ is elongated, while the ones between O₁-O₆ and O₃-O₄ are shortened. The distance between O₂-O₅ only shows negligible changes under all strains calculated. As the consequence shown in Fig. 4(d), (e), the AAAC strength on O₁-O₄ is weakened by such strain, with the AAAC on O₁-O₆ and O₃-O₄ strengthened,

12 / 22

and the one on O₂-O₅ almost unchanged. All other COHP matrix elements show negligible variations. It results in the increase of the overall AAAC on VBM at $\Gamma$, and the decrease of such property on VBM at $I$, as shown in Fig. 4(c). Eventually, under the tensile strain along the $b$ axis, the VBM at $\Gamma$ has been pushed up in energy in an amplitude larger than VBM at $I$, making it the new global VBM after the critical strain of 1.5%, and leading to the step-function change on hole mass, all in agreement with the band structure calculations shown in Fig. 3.

![](./images/1032538562353954827_5.jpg)

FIG. 4. Strain-induced modulation on lattice structure and COHP in $\beta$-Ga₂O₃. (a) The side view of the conventional cell, where all Ga and O are labeled. (b) Variations of distance between oxygen pairs O₂-O₅, O₁-O₄, O₁-O₆, and O₃-O₄; these oxygen pairs are the ones that have strong AAAC. (c) The differential COHP($\varepsilon, \mathbf{k}$) ($\Delta$COHP($\varepsilon, \mathbf{k}$)) under strain. The values under zero strain have been taken as the references. The matrix elements of $\Delta$COHP($\varepsilon, \mathbf{k}$) for VBM at $\Gamma$ (d) and VBM at $I$ (e).

## VII. THE SUPPRESSION OF STH

Indeed, the formation energy of polaron is known to be related to the effective mass $m^{*}$ of the host state. For instance, it has been suggested by D. W. Davies *et al.* [43] and W. H. Sio *et al.* [44] that

13 / 22

$E_{\text{polaron}} \propto -m^*$, that the heavier the mass is on one band, the easier the polaron forms from there.

Nevertheless, the formation of STH in wide-gap materials could be more complex, and simple approach could be incorrect or imprecise to describe it. Here, to understand if the tailoring of AAAC and $m_h^*$ can also affect the STH, we calculate before and after strain the formation energy of hole polaron from DFT with HSE. Details are given in the Appendix section.

Fig. 5(a) presents the hole polaron in the unstrained, pristine $\beta$-Ga₂O₃ with no vacancy or impurity. The STH is heavily localized between $\text{O}_2$ and $\text{O}_5$. Notice that it is the oxygen pair that has the strongest AAAC. It then supports our conclusion that a strong AAAC will lead to STH. Our results predict a 0.57 eV formation energy ($\varepsilon_{\text{STH}}$) for such STH, with the two oxygens distorted from their equilibrium positions by 0.22 Å. With a 2% tensile strain along the $b$ axis, the STH still exists, but its formation energy has been suppressed by 0.12 eV. The local distortions are also smaller than those under 0 strain. Moreover, the formation energy shows a significant drop between 1% and 2%, which is also consistent with the evolution of hole mass predicted in the last section, as shown in Fig. 5(b). We suggest that this result demonstrates that the AAAC mechanism can also be applied to suppress the formation of STH.

![](./images/1032538562353954827_6.jpg)

FIG. 5. Strain-induced modulation on STH: (a) The 80-atom supercell of β-Ga₂O₃ under 0% strain, showing the spontaneous formation of STH with the yellow isosurfaces. The isosurfaces are 0.0075 e/Å³. (b) The DFT-predicted formation energy (red) and local distortion (blue) of STH under different strain along the $b$ axis. The inset of (b) shows the local atom displacement caused by the STH, while the blue arrows mark the directions of displacement.

### VIII. SUMMARY AND OUTLOOK

In this work, we identify the physical origin of the intrinsic, heavy hole mass in β-Ga₂O₃ as an anion-anion antibonding coupling (AAAC) among oxygen atoms. This coupling, occurring at distances longer than atomic covalent radii, arises from the low symmetry and ligand orbital interactions, where oxygen orbitals interact without gallium involvement. The resulting Coulomb repulsion pushes the antibonding states up in energy to form the VBM, narrowing its bandwidth to less than 1 eV, significantly enhancing

15 / 22

the hole mass and leading to STH.

Based on these insights, we propose a design principle to tune hole masses and STH by modifying the strength of AAAC. We find that specific strain conditions can reduce the hole mass along $c^{*}$ from $4.77\ m_0$ to $0.38\ m_0$, tailoring its mass to a value comparable to the electron mass in the same compound. This significant reduction of hole mass along $c^{*}$ leads to the conductivity mass decreases from $3.47\ m_0$ to $0.99\ m_0$. The critical strains are 1.5% for uniaxial tensile strain along the $b$ axis and 0.7% for biaxial compressive strain on $a$-$c$ plane. This strain modification also induces high anisotropy in the hole mass, enabling quasi-two-dimensional transport in bulk material. Strain also suppresses the formation of STH.

These findings provide a new perspective on controlling hole transport properties in novel wide-gap materials, especially those with low-symmetric crystallographic structures, potentially leading to more efficient electronic and optoelectronic devices. We expect future research to validate these findings in gallium oxide and explore other material systems where similar mechanisms might be exploited to enhance performance.

## ACKNOWLEDGEMENTS
This work was supported by the National Key R&D Program of China (2022YFB3605403), the National Natural Science Foundation of China (62234007, 62293521, U21A20503, U21A2071 and 12174380). We would like to thank Lin-Wang Wang from Institute of Semiconductors, Chinese Academy of Sciences for insightful discussions.

## COMPETING INTERESTS
The authors declare no competing interests.

## APPENDIX I: Computational parameters

The crystallographic structure of $\beta$-Ga₂O₃ was firstly obtained from the Materials Project database [45], then fully relaxed by ourselves. All calculations in this work were implemented within the framework of density functional theory (DFT) implemented in the Vienna ab initio simulation package (VASP) [46] using the projector augmented wave (PAW) pseudopotentials [47]. A hybrid functional within the Heyd–Scuseria–Ernzerhof (HSE06) method was used in all DFT runs with 35% mixing of the Hartree–Fock exchange interaction [20]. The cutoff energy of plane-wave basis was 520 eV in all runs. An 8×8×4 Monkhorst-Pack k-point mesh was used for conventional cell. Energy minimization and ionic relaxation were performed with a tolerance of $10^{-8}$ eV per formula unit for the total energy, and $10^{-6}$ eV/Å on each nuclear for the atomic force, respectively. The shifts in energy of eigen levels in Fig. 3(a) under different strains were calculated by aligning the electrostatic potential (core level). The effective mass $m^*$ was calculated by fitting a quadratic curvature at the band extrema $(m^*)^{-1} = \partial^2 E/\partial k^2/\hbar^2$.

## APPENDIX II: Basic concept of COHP

The crystal orbital Hamilton populations (COHPs) was calculated by the Local-Orbital Basis Suite Towards Electronic-Structure Reconstruction package (LOBSTER) [48,49]. Here, we offer a brief explanation of the COHP method [50]:

$$
\operatorname{COHP}_{\mu i, v j}(\varepsilon, \mathbf{k})=\sum_{l} \mathcal{R}\left[P_{\mu i, v j, l}^{(p r o j)}(\mathbf{k}) H_{v j, \mu i}^{(p r o j)}(\mathbf{k})\right] \times \delta\left(\varepsilon_{l}(\mathbf{k})-\varepsilon\right) \tag{4}
$$

where $\mu$, $v$ are the atomic orbitals of the $i^{\text{th}}$ and $j^{\text{th}}$ atoms, respectively, $i$ is the index of electronic band, and $\varepsilon_{l}(\mathbf{k})$ is the eigen energy of the $i^{\text{th}}$ band at wave vector $\mathbf{k}$. The $H_{v j, \mu i}^{(p r o j)}$ on the right-hand side is the Hamiltonian matrix elements expressed in the basis of the local functions. The $P_{\mu i, v j, l}^{(p r o j)}$ is the projected density matrix

$$
P_{\mu i, v j, l}^{(p r o j)}(\mathbf{k})=T_{l, \mu i}^{*}(\mathbf{k}) T_{l, v j}(\mathbf{k}) \tag{5}
$$

and $T_{l, \mu i}(\mathbf{k})$ is the transfer matrix

$$
T_{l, \mu i}(\mathbf{k})=\left\langle\varphi_{l}(\mathbf{k}) \mid \phi_{\mu i}\right\rangle \tag{6}
$$

where $\varphi_{l}(\mathbf{k})$ is the eigen wavefunction of the $i^{th}$ band at wave vector $\mathbf{k}$, and $\phi_{\mu i}$ is the $\mu^{\text{th}}$ local orbitals of the $i^{\text{th}}$ atom.


## APPENDIX III: Polaron formation energy

The hole polarons in $\text{Ga}_2\text{O}_3$ were calculated using the 80-atom supercell (the 1×2×2 extension of the conventional cell). The steps are as follows. (1) An electron was firstly removed from the supercell to mimic the hole injection while all ions were frozen at their equilibrium positions. Mark the total energy for such a frozen-ion system with an extra hole as $\varepsilon_{tot}(\{\mathbf{R}_0\};\eta^+)$. (2) Secondly, random displacements were applied on ions as the initial "kicks". (3) Internal atomic positions were then relaxed with fixed lattice vectors. Mark the new total energy as $\varepsilon_{tot}(\{\mathbf{R}'\};h^+)$. During all steps the spin polarization was considered. The formation energy of polaron can be calculated by

$$
\varepsilon_{STH} = \varepsilon_{tot}(\{\mathbf{R}_0\};\eta^+) - \varepsilon_{tot}(\{\mathbf{R}'\};h^+) + \langle\Delta V\rangle \tag{7}
$$

where

$$
\langle\Delta V\rangle = \langle V(\{\mathbf{R}_0\};\eta^+)\rangle - \langle V(\{\mathbf{R}'\};h^+)\rangle \tag{8}
$$

are the difference in the average electric potential of the two systems [8].

## REFERENCE

[1] F. Zhou et al., *An Avalanche-and-Surge Robust Ultrawide-Bandgap Heterojunction for Power Electronics*, Nat. Commun. **14**, 4459 (2023).

[2] S. Poncé, D. Jena, and F. Giustino, *Hole Mobility of Strained GaN from First Principles*, Phys. Rev. B **100**, 085204 (2019).

[3] T. Deng, D. Yang, and X. Pi, *Phonon-Limited Carrier Mobilities and Hall Factors in 4H-SiC from First Principles*, Phys. Rev. B **107**, 235203 (2023).

[4] T. Yu et al., *Momentum-Resolved Electronic Structure and Band Offsets in an Epitaxial NbN/GaN Superconductor/Semiconductor Heterojunction*, Sci. Adv. 7, eabi5833 (2021).

[5] S. Shi and S. Xu, *Determination of Effective Mass of Heavy Hole from Phonon-Assisted Excitonic Luminescence Spectra in ZnO*, J. Appl. Phys. **109**, 053510 (2011).

[6] C. Hamaguchi, *Electron and Hole Mobilities of GaN with Bulk, Quantum Well, and HEMT Structures*, J. Appl. Phys. **130**, 125701 (2021).

[7] H. Sezen et al., *Evidence for Photogenerated Intermediate Hole Polarons in ZnO*, Nat. Commun. **6**, 6901 (2015).


[8] J. B. Varley, A. Janotti, C. Franchini, and C. G. Van de Walle, *Role of Self-Trapping in Luminescence and p-Type Conductivity of Wide-Band-Gap Oxides*, Phys. Rev. B **85**, 081109 (2012).

[9] D. Wickramaratne and J. L. Lyons, *Assessing the SCAN Functional for Deep Defects and Small Polarons in Wide Band Gap Semiconductors and Insulators*, Phys. Rev. B **109**, 245201 (2024).

[10] J. Wang, Y. Zhou, Z. Wang, A. Rasmita, J. Yang, X. Li, H. J. von Bardeleben, and W. Gao, *Bright Room Temperature Single Photon Source at Telecom Range in Cubic Silicon Carbide*, Nat. Commun. **9**, 4106 (2018).

[11] M. L. Coke, O. W. Kennedy, J. T. Sagar, and P. A. Warburton, *Electron Confinement at Diffuse ZnMgO/ZnO Interfaces*, APL Mater. **5**, 016102 (2017).

[12] Y. Xu et al., *Ultrahigh-Performance Solar-Blind Photodetectors Based on High Quality Heteroepitaxial Single Crystalline $\beta$-Ga₂O₃ Film Grown by Vacuumfree, Low-Cost Mist Chemical Vapor Deposition*, Adv. Mater. Technol. **6**, 2001296 (2021).

[13] M. N. Sharif, J. Yang, X. Zhang, Y. Tang, G. Yang, and K.-F. Wang, *Tailoring Electronic Properties of 6H-SiC with Different Composition of Silicon by First-Principles Calculations*, Adv. Theory Simul. 2400245 (2024).

[14] R. Vidya, P. Ravindran, H. Fjellvåg, B. Svensson, E. Monakhov, M. Ganchenkova, and R. M. Nieminen, *Energetics of Intrinsic Defects and Their Complexes in ZnO Investigated by Density Functional Calculations*, Phys. Rev. B **83**, 045206 (2011).

[15] S. Poncé, D. Jena, and F. Giustino, *Route to High Hole Mobility in GaN via Reversal of Crystal-Field Splitting*, Phys. Rev. Lett. **123**, 096602 (2019).

[16] J. Zhang et al., *Ultra-Wide Bandgap Semiconductor Ga2O3 Power Diodes*, Nat. Commun. **13**, 3900 (2022).

[17] S. Pearton, J. Yang, P. H. Cary, F. Ren, J. Kim, M. J. Tadjer, and M. A. Mastro, *A Review of Ga2O3 Materials, Processing, and Devices*, Appl. Phys. Rev. **5**, 011301 (2018).

[18] M. J. Tadjer, *Toward Gallium Oxide Power Electronics*, Science **378**, 724 (2022).

[19] C. Janowitz et al., *Experimental Electronic Structure of In₂O₃ and Ga₂O₃*, New J. Phys. **13**, 085014 (2011).


[20] M. Mohamed, C. Janowitz, I. Unger, R. Manzke, Z. Galazka, R. Uecker, R. Fornari, J. Weber, J. Varley, and C. Van de Walle, *The Electronic Structure of $\beta$-Ga₂O₃*, Appl. Phys. Lett. **97**, 211903 (2010).

[21] T. Lovejoy et al., *Band Bending and Surface Defects in $\beta$-Ga₂O₃*, Appl. Phys. Lett. **100**, 181602 (2012).

[22] J. B. Varley, J. R. Weber, A. Janotti, and C. G. Van de Walle, *Oxygen Vacancies and Donor Impurities in $\beta$-Ga₂O₃*, Appl. Phys. Lett. **97**, 142106 (2010).

[23] X. Liu and C.-K. Tan, *Electronic Properties of Monoclinic (InₓGa₁₋ₓ)₂O₃ Alloys by First-Principle*, AIP Adv. **9**, 035318 (2019).

[24] K. Yamaguchi, *First Principles Study on Electronic Structure of $\beta$-Ga₂O₃*, Solid State Commun. **131**, 739 (2004).

[25] C. Ma et al., *Exploring the Feasibility and Conduction Mechanisms of P-Type Nitrogen-Doped $\beta$-Ga₂O₃ with High Hole Mobility*, J. Mater. Chem. C **10**, 6673 (2022).

[26] A. Mock, R. Korlacki, C. Briley, V. Darakchieva, B. Monemar, Y. Kumagai, K. Goto, M. Higashiwaki, and M. Schubert, *Band-to-Band Transitions, Selection Rules, Effective Mass, and Excitonic Contributions in Monoclinic $\beta$-Ga₂O₃*, Phys. Rev. B **96**, 245205 (2017).

[27] N. Son, W. Chen, O. Kordina, A. Konstantinov, B. Monemar, E. Janzén, D. Hofman, D. Volm, M. Drechsler, and B. Meyer, *Electron Effective Masses in 4H-SiC*, Appl. Phys. Lett. **66**, 1074 (1995).

[28] N. Son, O. Kordina, A. Konstantinov, W. Chen, E. Sörman, B. Monemar, and E. Janzén, *Electron Effective Masses and Mobilities in High-Purity 6H-SiC Chemical Vapor Deposition Layers*, Appl. Phys. Lett. **65**, 3209 (1994).

[29] M. Leszczynski et al., *Lattice Parameters of Gallium Nitride*, Appl. Phys. Lett. **69**, 73 (1996).

[30] W. Fan, M. Li, T. Chong, and J. Xia, *Electronic Properties of Zinc-Blende GaN, AlN, and Their Alloys Ga₁₋ₓAlₓN*, J. Appl. Phys. **79**, 188–194 (1996).

[31] Y. Qin et al., *Ultra-High Performance Amorphous Ga₂O₃ Photodetector Arrays for Solar-Blind Imaging*, Adv. Sci. **8**, 2101106 (2021).

[32] J. Heyd, J. E. Peralta, G. E. Scuseria, and R. L. Martin, *Energy Band Gaps and Lattice Parameters*

20 / 22

Evaluated with the Heyd-Scuseria-Ernzerhof Screened Hybrid Functional, J. Chem. Phys. 123,
174101 (2005).

[33] A. V. Krukau, O. A. Vydrov, A. F. Izmaylov, and G. E. Scuseria, Influence of the Exchange Screening
Parameter on the Performance of Screened Hybrid Functionals, J. Chem. Phys. 125, 224106 (2006).

[34] H. He, M. A. Blanco, and R. Pandey, Electronic and Thermodynamic Properties of $\beta$-Ga₂O₃, Appl.
Phys. Lett. 88, 261904 (2006).

[35] T. Onuma, S. Saito, K. Sasaki, T. Masui, T. Yamaguchi, T. Honda, and M. Higashiwaki, Valence
Band Ordering in $\beta$-Ga₂O₃ Studied by Polarized Transmittance and Reflectance Spectroscopy, Jpn.
J. Appl. Phys. 54, 112601 (2015).

[36] H. Peelaers and C. G. Van de Walle, Brillouin Zone and Band Structure of $\beta$-Ga₂O₃, Phys. Status
Solidi B 252, 828 (2015).

[37] S. Geller, Crystal Structure of $\beta$-Ga₂O₃, J. Chem. Phys. 33, 676 (1960).

[38] M. M. R. Adnan, D. Verma, Z. Xia, N. K. Kalarickal, S. Rajan, and R. C. Myers, Spectral
Measurement of the Breakdown Limit of $\beta$-Ga₂O₃ and Tunnel Ionization of Self-Trapped Excitons
and Holes, Phys. Rev. Appl. 16, 034011 (2021).

[39] C. Ma et al., Correction: Exploring the Feasibility and Conduction Mechanisms of P-Type Nitrogen-
Doped $\beta$-Ga₂O₃ with High Hole Mobility, J. Mater. Chem. C 10, 7731 (2022).

[40] R. Dronskowski and P. E. Bloechl, Crystal Orbital Hamilton Populations (COHP): Energy-Resolved
Visualization of Chemical Bonding in Solids Based on Density-Functional Calculations, J. Phys.
Chem. 97, 8617 (1993).

[41] G. Trimarchi, Z. Wang, and A. Zunger, Polymorphous Band Structure Model of Gapping in the
Antiferromagnetic and Paramagnetic Phases of the Mott Insulators MnO, FeO, CoO, and NiO, Phys.
Rev. B 97, 035107 (2018).

[42] Y. Peter and M. Cardona, Fundamentals of Semiconductors: Physics and Materials Properties
(Springer Science & Business Media, 2010).

[43] D. W. Davies, C. N. Savory, J. M. Frost, D. O. Scanlon, B. J. Morgan, and A. Walsh, Descriptors for
Electron and Hole Charge Carriers in Metal Oxides, J. Phys. Chem. Lett. 11, 438 (2019).

21 / 22

[44] W. H. Sio, C. Verdi, S. Poncé, and F. Giustino, *Ab Initio Theory of Polarons: Formalism and Applications*, Phys. Rev. B **99**, 235139 (2019).

[45] A. Jain et al., *Commentary: The Materials Project: A Materials Genome Approach to Accelerating Materials Innovation*, APL Mater. **1**, 011002 (2013).

[46] G. Kresse and J. Furthmüller, *Efficient Iterative Schemes for Ab Initio Total-Energy Calculations Using a Plane-Wave Basis Set*, Phys. Rev. B **54**, 11169 (1996).

[47] P. E. Blöchl, *Projector Augmented-Wave Method*, Phys. Rev. B **50**, 17953 (1994).

[48] R. Nelson, C. Ertural, J. George, V. L. Deringer, G. Hautier, and R. Dronskowski, *LOBSTER: Local Orbital Projections, Atomic Charges, and Chemical-Bonding Analysis from Projector-Augmented- Wave-Based Density-Functional Theory*, J. Comput. Chem. **41**, 1931 (2020).

[49] S. Maintz, V. L. Deringer, A. L. Tchougréeff, and R. Dronskowski, *LOBSTER: A Tool to Extract Chemical Bonding from Plane-Wave Based DFT*, (2016).

[50] V. L. Deringer, A. L. Tchougréeff, and R. Dronskowski, *Crystal Orbital Hamilton Population (COHP) Analysis as Projected from Plane-Wave Basis Sets*, J. Phys. Chem. A **115**, 5461 (2011).