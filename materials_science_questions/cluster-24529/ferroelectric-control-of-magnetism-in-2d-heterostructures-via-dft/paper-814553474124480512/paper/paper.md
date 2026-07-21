# Band structure engineering of topological insulator heterojunctions

Kyung-Hwan Jin, $^{1,2}$ Han Woong Yeom, $^{1,3}$ and Seung-Hoon Jhi $^{1, *}$

$^{1}$ Department of Physics, Pohang University of Science and Technology, Pohang 790-784, Republic of Korea
$^{2}$ Department of Materials Science and Engineering, University of Utah, Salt Lake City, Utah 84112, USA
$^{3}$ Center for Low Dimensional Electronic Symmetry, Pohang University of Science and Technology, Pohang 790-784, Republic of Korea

(Received 20 November 2015; revised manuscript received 27 January 2016; published 19 February 2016)

We investigate the topological surface states in heterostructures formed from a three-dimensional topological insulator (TI) and a two-dimensional insulating thin film, using first-principles calculations and the tight-binding method. Utilizing a single Bi or Sb bilayer on top of the topological insulators $Bi_2Se_3$, $Bi_2Te_3$, $Bi_2Te_2Se$, and $Sb_2Te_3$, we find that the surface states evolve in very peculiar but predictable ways. We show that strong hybridization between the bilayer and TI substrates causes the topological surface states to migrate to the top bilayer. It is found that the difference in the work function of constituent layers, which determines the band alignment and the strength of hybridization, governs the character of newly emerged Dirac states.

DOI: 10.1103/PhysRevB.93.075308

## I. INTRODUCTION

Heterostructures comprised of topological insulators (TIs) and materials with other types of physical order have been explored to produce interfacial phenomena that may not arise in the heterojunctions of conventional materials, which should thus bear fundamental importance and potential for innovative applications [1,2]. For instance, the TI-superconductor hybrid structure exhibits the superconducting proximity effect at the interface and leads to the possibility of observing Majorana fermions [3]. The ferromagnetic insulator-TI structure is suggested to realize the topological magnetoelectric effect [4,5] and the inverse spin-galvanic effect [6]. Graphene turns out to have giant spin-orbit coupling (SOC) when it is in contact with TI substrates [7–9].

Similar to the heterostructure of TI and the materials with other types of physical order, mixed-dimensional TI systems, which combine TI materials of different dimensions, say a three-dimensional (3D) TI with a two-dimensional (2D) TI and/or non-TI, can also provide interesting platforms to investigate unconventional interfacial phenomena. On one hand, the topological order of 3D TIs dictates the existence of the gapless surface states at the interface, which may penetrate into the 2D systems. On the other hand, there should be no conducting states inside the gap if the 2D system in contact has nontrivial topological order regardless of the contact strength. Also, if the 2D systems form nanostructures having edges, one-dimensional (1D) and 2D helical conducting states from the 2D and 3D TIs, respectively, should coexist. So far, a standard model of the TI heterosturctures, in particular, of how we control the interfacial phenomena via chemical or physical methods at a similar level as in semiconductor heterojunctions is not yet established. Scattered demonstrations of tunability of the topological surface states were reported in a thin semiconducting overlayer on top of TI substrates [10,11]. In most cases, variation in atomic composition or doping is used to control the helical states [12–14], and a small band gap is opened at the Dirac point by magnetic doping from the time-reversal symmetry breaking [15–18]. In semiconductor-TI junctions with a good contact, nontrivial states can penetrate into the semiconductor as evanescent waves depending on the band gap and the work function of the constituent materials [10]. General pictures of TI heterostructures similar to those for conventional semiconductor heterojunctions are very desirable for development of TI-based devices.

Bi and Sb bilayers are representative 2D TIs with many interesting electrical and mechanical properties [19–21]. In particular, the Bi bilayer has been studied extensively as it exhibits various topological phases upon structural and chemical modification [22,23]. The Bi bilayer grown on 3D TI substrates is a real system where the 1D helical edge state is observed explicitly [24–26]. They thus constitute truly realistic platforms to test the manipulation of topological surface states. An essential step is to understand the effect of TI substrates on the electronic properties of the Bi bilayer. Previous studies showed that the Bi bilayer grown on TI substrates has Dirac states, becoming metallic [24–35]. However, development of the topological Dirac states at such heterostructures is hard to track down due to the complexity of the band structures near the Fermi level, and assignment of the newly emerging Dirac states from Bi bilayers shows inconsistency [26,31–34]. A unified concept of the helical states in Bi bilayer-TI heterostructures can provide a key to developing a standard model of mixed-dimensional topological heterostructures.

In this work, we studied the interaction of the bilayer states with topological surface states in a heterostructure of a single Sb or Bi bilayer on top of 3D TI substrates using first-principles calculations and the tight-binding method. In particular, we investigated the development of spin-helical electronic states from the hybridization between the 2D states, the surface states of 3D TIs, and quantum well states. We presented a comprehensive picture to analyze the evolvement of the helical states and the material properties that determine the band alignment.

## II. COMPUTATION

First-principles calculations are carried out within the generalized gradient approximation with the Perdew-Burke-Ernzerhof functional using the VASP package [36–38]. We used the experimental lattice constant of the substrate and

*Corresponding author: jhish@postech.ac.k

<table>
 <thead>
  <tr>
   <th colspan="2">
   </th>
   <th>
    Bi₂Se₃
   </th>
   <th>
    Bi₂Te₃
   </th>
   <th>
    Bi₂Te₂Se
   </th>
   <th>
    Sb₂Te₃
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th colspan="2">
    $a$ (Å)
   </th>
   <td>
    4.138
   </td>
   <td>
    4.383
   </td>
   <td>
    4.280
   </td>
   <td>
    4.250
   </td>
  </tr>
  <tr>
   <th>
    Mismatch (%)
   </th>
   <th>
    Sb
   </th>
   <td>
    +0.36
   </td>
   <td>
    +6.30
   </td>
   <td>
    +3.80
   </td>
   <td>
    +3.08
   </td>
  </tr>
  <tr>
   <th>
   </th>
   <th>
    Bi
   </th>
   <td>
    $-$4.65
   </td>
   <td>
    +0.99
   </td>
   <td>
    $-$1.38
   </td>
   <td>
    $-$2.07
   </td>
  </tr>
  <tr>
   <th>
    $d$ (Å)
   </th>
   <th>
    Sb
   </th>
   <td>
    2.71
   </td>
   <td>
    2.52
   </td>
   <td>
    2.67
   </td>
   <td>
    2.72
   </td>
  </tr>
  <tr>
   <th>
   </th>
   <th>
    Bi
   </th>
   <td>
    2.53
   </td>
   <td>
    2.72
   </td>
   <td>
    2.80
   </td>
   <td>
    2.90
   </td>
  </tr>
  <tr>
   <th colspan="2">
    $W$ (eV)
   </th>
   <td>
    5.545
   </td>
   <td>
    5.022
   </td>
   <td>
    5.018
   </td>
   <td>
    4.606
   </td>
  </tr>
 </tbody>
</table>

adjusted the lattices of single Bi and Sb bilayers to make a commensurate match with the substrate. All calculations are done with a cutoff energy of 400 eV for plane-wave basis expansion and the $k$-point mesh of $11 \times 11 \times 1$. The Sb(Bi)/TI heterostructure is modeled by a supercell with a single Sb(Bi) bilayer on one surface of a slab that consists of six-quintuple–layer-(QL-)–thick TI and a 20-Å-thick vacuum layer between the cells. During structural relaxations, the atoms in the Sb(Bi) bilayer and in the first three layers of the TI slab are allowed to relax until the forces are smaller than 0.01 eV/Å. Calculations using the Quantum-ESPRESSO package [39] give consistent results with those from VASP. The bilayer alloys of Sb and Bi were modeled using the virtual crystal approximation (VCA) in which the pseudopotentials are generated by mixing Sb and Bi pseudopotentials.

### III. RESULTS AND DISCUSSION
A single Sb or Bi bilayer has a buckled hexagonal structure, and its commensurate alignment on top of the (111) surface of Bi₂Se₃ (BS), Bi₂Te₃ (BT), Bi₂Te₂Se (BTS), or Sb₂Te₃ (ST) produces a slight lattice mismatch (Table I and Fig. 1). The binding energy is given as $E_{b} = E(\text{bilayer} + \text{TI}) - E(\text{bilayer}) - E(\text{TI})$, where $E(\cdot)$ represents the cohesive energies of the bilayer-6QL TI, the bilayer, and 6QL TI, respectively. The Bi bilayer is weakly bound to the TI substrates with a binding energy of about $\sim$0.1 eV per Bi atom and the equilibrium separation $d \leqslant 2.9$ Å. Our calculated results are in good agreement with available experimental data and other calculations [27,30,33]. For the Sb bilayer, the adsorption is weaker with $E_{b} \sim 0.06$ eV per Sb atom but its equilibrium separation is similar to that in the Bi bilayer case. The absence of direct chemical bonding indicates that the binding is an electrostatic type. We also calculated the work functions of the substrates and pristine Sb and Bi bilayers [Fig. 1(d)], which determines the band alignment of the Dirac states in the heterostructures as discussed below. The Sb bilayer has a similar work function to that of TI substrates while the Bi bilayer has a smaller value by $\sim$1.5 eV.

Emergence of the surface states in the heterostructures exhibits intriguing material dependence. Figure 2 shows calculated band structures of the Sb/TI heterostructure projected onto those of the Sb bilayer and upper 2QL TI substrate. Near the Fermi level, we observe only one Dirac cone at

![](./images/814553474124480512_1.jpg)

FIG. 1. A perspective (a) side view and (b) top view of atomic structure of single Sb and Bi bilayers on a TI surface. (c) Calculated binding energy ($E_{b}$) of bilayer on each TI substrate. (d) Calculated work function ($W$) of TI substrates and pristine Sb and Bi bilayers on each TI substrate lattice.

![](./images/814553474124480512_2.jpg)

FIG. 2. Calculated band structures of Sb bilayer on (a) Bi₂Se₃, (b) Bi₂Te₃, (c) Bi₂Te₂Se, and (d) Sb₂Te₃ along the $\Gamma$-$K$ direction. Shaded (gray) regions are the projection of the bulk band structure of 3D TI into the 2D surface Brillouin zone. The color bar indicates the origin of the states. The band originating from the Sb bilayer (upper 2QL of TI) is colored in magenta (blue). Emerging Dirac states labeled by D* and $D_{R}$ are the intrinsic and the Rashba-split states, respectively.

![](./images/814553474124480512_3.jpg)

FIG. 3. Calculated band structure for Bi bilayer on (a) $Bi_2Se_3$, (b) $Bi_2Te_3$, (c) $Bi_2Te_2Se$, and (d) $Sb_2Te_3$ along the $\Gamma$-$K$ direction. Shaded (gray) regions are the projection of bulk band structures of 3D TI into the 2D surface Brillouin zone. The bands originating from the Bi bilayer (upper 2QL of TI) are colored in red (blue).

the $\Gamma$ point as denoted by D*. The original surface state of TI is buried into the bulk states and the new D* emerges almost solely from the Sb bilayer. The energy and shape of the Dirac cone are slightly different for each substrate but the helical nature of the surface states is well presented. The D* is located in the bulk conduction band for BS and BT substrates, but inside the bulk gap for BTS and ST substrates. We note that another Dirac cone (labeled as $D_R$) originating from the top QL of the TI substrates appears below the Fermi level. However, absence of partner switching between the time-reversal-invariant momenta indicates that the Dirac cone $D_R$ is the Rashba-split states without the topological protection.

The Dirac cones appear more complex in the Bi/TI heterostructure. Figure 3 shows calculated band structures of Bi/TI projected onto the Bi bilayer and the top 2QL of the TI substrate. Different from the Sb/TI case, we observe three Dirac cones $D_Q$, $D_R$, and D* at the $\Gamma$ point denoted. We found that the $D_Q$ and $D_R$ states are extrinsic Dirac-cone-like states arising from the hybridization of Bi bilayer states with TI quantum-well states and from the Rashba splitting of Bi bilayer states, respectively, and the D* is the intrinsic Dirac state. For all substrates, an odd number of bands cross the Fermi level with clear helical spin texture (Fig. 4), ensuring the topological insulating property of the heterostructure. The original single Dirac state of the TI substrates at the $\Gamma$ point merges into the bulk states due to the charge transfer from the Bi bilayer.

We observe that the position of these Dirac-cone-like states, in particular $D_Q$ and $D_R$, moves as the substrates are changed. For Bi/BS and Bi/BT, $D_R$ is located above $D_Q$ whereas, for BTS

![](./images/814553474124480512_4.jpg)

FIG. 4. Calculated spin texture of (a)-(d) Sb bilayer and (e)-(f) Bi bilayer on $Bi_2Se_3$, $Bi_2Te_3$, $Bi_2Te_2Se$, and $Sb_2Te_3$, respectively, along the $\Gamma$-$K$ direction. The color bar indicates the $x$ component of the spin (red for up and blue for down spin). The new Dirac cone D* that emerges almost solely from the Sb or Bi bilayer exhibits a helical spin texture.

![](./images/814553474124480512_5.jpg)

FIG. 5. Calculated band structures of (a) Sb/BTS and (b) Bi/BTS at artificially increased interfacial distance between the bilayer and the TI surface from the equilibrium position ($\Delta d$) by 4, 2, 1, and 0.5 Å, from left to right. The parameter $\delta$ is the valence band maximum energy relative to the Dirac point.

![](./images/814553474124480512_6.jpg)

FIG. 6. Evolution of the spin texture in (a) Sb/BTS and (b) Bi/BTS. The interfacial distance between the bilayer and the TI surface is increased from equilibrium by $\Delta d = 4$, 2, 1, and 0.5 Å (from left to right). The color bar indicates the $x$ component of the spin with up in red and down in blue. We observe the helical spin texture migrating to the bilayer.

![](./images/814553474124480512_7.jpg)

FIG. 7. Evolution of the orbital character in (a) Sb/BTS and (b) Bi/BTS. The interfacial distance between the bilayer and the TI surface is increased from equilibrium by $\Delta d = 4, 2, 1$, and $0.5$ Å (from left to right). The states near the Fermi level originate from the Sb or Bi bilayer, having mostly $p$-orbital character, as marked by colored dots ($p_x$, $p_y$ in red and $p_z$ in blue). We observe the $p_z$-character states in Sb but $p_x$, $p_y$, and $p_z$ states in Bi bilayer, which form new topological surface states.

and ST substrates, $D_R$ state is located below $D_Q$. The relative position of $D_R$ and $D_Q$ in different substrates is related to the shift in the energy level of the hybridized states between the Bi bilayer and the TI quantum-well states. The band alignment of the bilayer state with the TI bulk bands, which is related to the work function, determines the position of $D_Q$. The calculated work functions of TI substrates are in the range of 4.6–5.5 eV, and the one for the Bi bilayer is $\sim$3.5 eV. The work-function difference ($\Delta W_{Bi}$) between the Bi bilayer and TI substrates is in the order of $\Delta W_{Bi}(BS) > \Delta W_{Bi}(BT) > \Delta W_{Bi}(BTS) > \Delta W_{Bi}(ST)$. As the work-function difference between TI substrates and the Bi bilayer decreases, the $D_R$ state becomes lower in energy than the $D_Q$ state and becomes located inside the bulk gap of TI.

The $D^*$ state is a truly intrinsic Dirac cone that preserves the topological property. Without this state, it turns out that an even number of bands cross the Fermi level. For the Sb bilayer, the $D^*$ state replaces the intrinsic BTS Dirac state. On the other hand, for the Bi bilayer, which has stronger interfacial coupling with the substrate, one of the Bi bilayer valence bands merges into the BTS bulk conduction band, and the $D^*$ state shifts to a higher energy, forming a linear band. This becomes clearer as we artificially control the strength of hybridization by changing the distance between the bilayer and the TI substrate. We elaborate this in more detail below.

To understand the origin of the different band structures in Sb and Bi bilayers, we artificially tune the interaction between the adsorption layer and the TI surface by changing the interfacial distance. Figure 5 shows calculated band structures of Sb/BTS and Bi/BTS after adjusting the interfacial distance from the equilibrium. At large interfacial distances, the interfacial interaction between the substrate and the bilayer

![](./images/814553474124480512_8.jpg)

FIG. 8. Band structures from the model Hamiltonian for bilayer/TI heterostructure. (a) Sb bilayer and (b) Bi bilayer on BTS in the absence (left panel) and presence (right panel) of interfacial interactions. The energy zero is set to the Dirac point of the BTS surface states in the absence of the hopping term. The bands in magenta and red are the bilayer states and the linear band in blue shows the BTS surface states.

![](./images/814553474124480512_9.jpg)

FIG. 9. Calculated band structures of BTS₁QL/BTS₅QL with the interfacial distance increased by $\Delta d = 4, 1, 0.5$, and $0$ Å (from left to right) from the equilibrium distance.

is negligible and the band structure is a simple superposition of the bands of the isolated Sb/Bi bilayer and the BTS substrate. We note that the valence band maximum (VBM) relative to the Dirac point is about $\sim$0.05 eV for Sb and $\sim$0.4 eV for Bi due to the work-function difference. The Sb bilayer has a work function of about $\sim$5 eV, similar to that of BTS, and its VBM is well aligned with that of BTS. However, the Bi bilayer with the work function of $\sim$3.5 eV has the VBM in the BTS bulk conduction band. This explains the different band shapes for Sb and Bi bilayers. As the interfacial distance is decreased, we observe a slight band splitting in doubly degenerate bands of the bilayer due to the broken inversion symmetry. When the interfacial coupling is enhanced, the bands split further and start to hybridize with the TI bands, eventually forming new Dirac cones. This behavior is also found in the evolution of the spin texture and orbital character as the interfacial distance is changed (Figs. 6 and 7).

We construct a minimal tight-binding model that includes only the topological surface states, a single band from the bilayer insulator (BI), and the interaction between them in order to track down the evolution of the Dirac states. There is misalignment of the band edges of the TI and the bilayer due to the difference in electron affinity. Such misalignment produces a large transverse $E$ field near the interface, which is the source of the Rashba interaction. The general form of the effective Hamiltonian for a BI/TI heterostrucutre is written as

$$
H=\begin{pmatrix}
H_{TI} & T \\
T^{\dagger} & H_{BI}
\end{pmatrix}, \tag{1}
$$

with the basis $|\Psi\rangle=(|\Psi_{TI}^{\uparrow}\rangle,|\Psi_{TI}^{\downarrow}\rangle,|\Psi_{BI}^{\uparrow}\rangle,|\Psi_{BI}^{\downarrow}\rangle)$, where $|\Psi_{TI}^{\uparrow\downarrow}\rangle$ are the topological surface states and $|\Psi_{BI}^{\uparrow\downarrow}\rangle$ are the BI states. The TI states are described by a massless Dirac cone with helical spin textures, $H_{TI}=v_F(\vec{k}\times\vec{\sigma})\cdot\hat{z}$. The single band of the BI interacting with TI surface states is given as a spin-degenerate quadratic band, $(k^2/2m^*)1_{2\times2}$, with effective mass $m^*$. Including the Rashba SOC, $H_{BI}=(k^2/2m^*+\delta)1_{2\times2}+\alpha_R(k_y\sigma_x+k_x\sigma_y)$, where $\delta$ is the band offset determined by the work-function difference and $\alpha_R$ is the Rashba coupling strength. The hopping between the

![](./images/814553474124480512_10.jpg)

FIG. 10. (a) Schematic representation of the band alignment in BI/TI interfaces. The band alignment is determined by the work function difference between TI ($W_{TI}$) and BI ($W_{BI}$). For $W_{TI}\approx W_{BI}$, the band is aligned at a similar level (I); if $W_{TI}>W_{BI}$, the valence band of the BI hybridizes with the surface states of the TI (II); if $W_{TI}<W_{BI}$, the conduction band of the BI hybridizes with the TI surface states (III). The arrows in blue indicate the electron flow. (b) Schematic illustration of the hybridization of the BI band (in red) with the topological surface state (in blue). Shaded regions denote the bulk states.

![](./images/814553474124480512_11.jpg)

FIG. 11. (a) The band structures of a free-standing ${\rm Bi}_{1-x}{\rm Sb}_{x}$ alloy bilayer with $x=1$, 0.8, 0.6, 0.4, and 0, from left to right. The band gap is closed at $x=0.4$, indicating a topological phase transition from trivial insulator to quantum spin-Hall insulator. (b) Calculated band structures of ${\rm Bi}_{1-x}{\rm Sb}_{x}$/BTS heterostructure. The bands highlighted in blue represent the states originating from the alloy bilayer. The critical Sb composition for the topological phase transition is now shifted to $x\sim0.67$ due to the interaction with the BTS substrate. We observe a gradual change in the band structure from the Sb-bilayer ($x=1$) to the Bi-bilayer case ($x=0$).

bilayer and the TI surface states is given as $T=t\sigma_{z}1_{2\times2}$ with the parameter $t$ characterizing the interfacial contact of the heterostructure. The parameters in the model Hamiltonian are obtained from a fitting to first-principles calculations. For Sb(Bi)/BTS, $m^{*}=-0.2(-0.12)\,{\rm eV}^{-1}\mathring{\mathrm{A}}^{-2}$, $\alpha_{R}=0.5(0.2)\,{\rm eV\mathring{A}}$, and $t=0.05$ (0.1) eV, and the Fermi velocity of BTS $v_{\rm F}\sim5.8\times10^{5}\,{\rm m/s}$. Figure 8 shows the band structure of this model Hamiltonian. Without the hopping term (left panels), Sb and Bi bilayers show a clear difference in the band offset $\delta$ and the VBM. Immediate changes when the hopping term is included are the Rashba splitting in the bilayer bands and the appearance of two Dirac cones D$^{*}$ and D$_{\rm R}$. Depending on the position of the VBM, an additional Dirac cone may appear. The valence band of the Bi bilayer overlaps with the bulk conduction band of BTS, and its hybridization with quantum-well states (not included in the tight-binding Hamiltonian) can produce another Dirac cone D$_{\rm Q}$. On the other hand, the Sb bilayer's VBM is close to the Dirac point of BTS surface states within about 0.05 eV, and hybridization of the Sb band and BTS surface states still leaves the Dirac cones inside the bulk gap of BTS. The formation of the Dirac cone inside the bulk band gap when the Dirac point of the substrate and the VBM of the overlayer are close is supported by an apparent example of a homogeneous BTS block. When 1QL BTS is overlaid on top of 5QL BTS, the surface state of 5QL BTS should move to the top 1QL BTS (Fig. 9). The VBM of 1QL is located in the bulk energy gap since the workfunction of 1QL and 5QL BTS is very similar (5.08 vs 5.02 eV).

Analysis of the tight-binding model Hamiltonian reveals the factors that control the hybridization between BI states and TI surface states. The first is the band alignment, which is related to the work functions of the constituent materials. When the work function of BI is smaller than that of the TI substrate, the VBM of BI is located in the bulk conduction band of TI. In the opposite case, the conduction band minimum of BI is aligned with the VBM of bulk TI as illustrated in Fig. 10. The second is the coupling between BI and TI surface states. As we presented above for the Sb and Bi cases, BI with a large SOC tends to have strong coupling with TI substrates. In order to confirm this tendency and thus to utilize this result for engineering topological surface states, we consider the alloy of Bi and Sb, ${\rm Bi}_{1-x}{\rm Sb}_{x}$, using the VCA method because Bi and Sb are isoelectronic and have the same structure. We assume a uniform distribution and neglect disorder effects. On increasing the Sb content (or reducing the SOC strength), the alloy makes a transition from a 2D TI to a BI. We observe a continuous evolution of the Dirac cones in ${\rm Bi}_{1-x}{\rm Sb}_{x}$/BTS heterostructure from the case of Sb to a Bi bilayer (Fig. 11).

In summary, we studied the heterostructures of Sb (Bi) bilayers on top of TI substrates. We found that the strong hybridization between the Sb (Bi) bilayer and the TI substrate causes topological surface states to migrate from the TI to the overlaid bilayer. The band alignment of the overlaid bilayer and TI substrates, which is determined by the work functions of the materials, controls the band dispersion and the energy of emerging Dirac cones. Our findings illustrate a possibility

of controlling the surface states and topological phases in the heterostructures and open a way of designing appropriate material combinations for device applications. Also our study helps understand the complex evolution of the surface states and the topological properties in TI heterostructures.

## ACKNOWLEDGMENTS
This work was supported by the National Research Foun- dation of Korea through the SRC program (Grant No. 2011- 0030046) and the Institute for Basic Science (IBS) (Grant No. IBS-R014-D1).

[1] M. Z. Hasan and C. L. Kane, Rev. Mod. Phys. 82, 3045 (2010).
[2] X.-L. Qi and S.-C. Zhang, Rev. Mod. Phys. 83, 1057 (2011).
[3] L. Fu and C. L. Kane, Phys. Rev. Lett. 100, 096407 (2008).
[4] X.-L. Qi, T. L. Hughes, and S.-C. Zhang, Phys. Rev. B 78, 195424 (2008).
[5] X.-L. Qi, R. Li, J. Zang, and S.-C. Zhang, Science 323, 1184 (2009).
[6] I. Garate and M. Franz, Phys. Rev. Lett. 104, 146802 (2010).
[7] K.-H. Jin and S.-H. Jhi, Phys. Rev. B 87, 075442 (2013).
[8] J. Zhang, C. Triola, and E. Rossi, Phys. Rev. Lett. 112, 096802 (2014).
[9] P. Lee, J.-H. Jin, S. J. Sung, J. G. Kim, M.-T. Ryu, H.-M. Park, S.-H. Jhi, N. Kim, Y. Kim, S. U. Yu, K. S. Kim, D. Y. Noh, and J. Chung, ACS Nano 9, 10861 (2015).
[10] G. Wu, H. Chen, Y. Sun, X. Li, P. Cui, C. Franchini, J. Wang, X.-Q. Chen, and Z. Zhang, Sci. Rep. 3, 1233 (2013).
[11] T. V. Menshchikova, M. M. Otrokov, S. S. Tsirkin, D. A. Samorokov, V. V. Bebneva, A. Ernst, V. M. Kuznetsov, and E. V. Chulkov, Nano Lett. 13, 6064 (2013).
[12] Y. L. Chen, J. G. Analytis, J.-H. Chu, Z. K. Liu, S.-K. Mo, X. L. Qi, H. J. Zhang, D. H. Lu, X. Dai, Z. Fang, S. C. Zhang, I. R. Fisher, Z. Hussain, and Z.-X. Shen, Science 325, 178 (2009).
[13] J. Zhang, C.-Z. Chang, Z. Zhang, J. Wen, X. Feng, K. Li, M. Liu, K. He, L. Wang, X. Chen, Q.-K. Xue, X. Ma, and Y. Wang, Nat. Commun. 2, 574 (2011).
[14] T. Arakane, T. Sato, S. Souma, K. Kosaka, K. Nakayama, M. Komatsu, T. Takahashi, Z. Ren, K. Segawa, and Y. Ando, Nat. Commun. 3, 636 (2012).
[15] Y. L. Chen, J.-H. Chu, J. G. Analytis, Z. K. Liu, K. Igarashi, H.-H. Kuo, X. L. Qi, S. K. Mo, R. G. Moore, D. H. Lu, M. Hashimoto, T. Sasagawa, S. C. Zhang, I. R. Fisher, Z. Hussain, and Z. X. Shen, Science 329, 659 (2010).
[16] L. A. Wray, S.-Y. Xu, Y. Xia, D. Hsieh, A. V. Fedorov, Y. S. Hor, R. J. Cava, A. Bansil, H. Lin, and M. Z. Hasan, Nat. Phys. 7, 32 (2011).
[17] J. Henk, M. Flieger, I. V. Maznichenko, I. Mertig, A. Ernst, S. V. Eremeev, and E. V. Chulkov, Phys. Rev. Lett. 109, 076801 (2012).
[18] K.-H. Jin and S.-H. Jhi, J. Phys.: Condens. Matter 24, 175001 (2012).
[19] S. Murakami, Phys. Rev. Lett. 97, 236805 (2006).
[20] M. Wada, S. Murakami, F. Freimuth, and G. Bihlmayer, Phys. Rev. B 83, 121310 (2011).

[21] F.-C. Chuang, C.-H. Hsu, C.-Y. Chen, Z.-Q. Huang, V. Ozolins, H. Lin, and A. Bansil, Appl. Phys. Lett. 102, 022424 (2013).
[22] Z. Song, C.-C. Liu, J. Yang, J. Han, M. Ye, B. Fu, Y. Yang, Q. Niu, J. Lu, and Y. Yao, NPG Asia Mater. 6, e147 (2014).
[23] K.-H. Jin and S.-H. Jhi, Sci. Rep. 5, 8426 (2015).
[24] T. Hirahara, G. Bihlmayer, Y. Sakamoto, M. Yamada, H. Miyazaki, S.-I. Kimura, S. Blügel, and S. Hasegawa, Phys. Rev. Lett. 107, 166801 (2011).
[25] F. Yang, L. Miao, Z. F. Wang, M.-Y. Yao, F. Zhu, Y. R. Song, M.-X. Wang, J.-P. Xu, A. V. Fedorov, Z. Sun, G. B. Zhang, C. Liu, F. Liu, D. Qian, C. L. Gao, and J.-F. Jia, Phys. Rev. Lett. 109, 016801 (2012).
[26] S. H. Kim, K.-H. Jin, J. Park, J. S. Kim, S.-H. Jhi, T.-H. Kim, and H. W. Yeom, Phys. Rev. B 89, 155436 (2014).
[27] N. Fukui, T. Hirahara, T. Shirasawa, T. Takahashi, K. Kobayashi, and S. Hasegawa, Phys. Rev. B 85, 115426 (2012).
[28] Z. F. Wang, M.-Y. Yao, W. Ming, L. Miao, F. Zhu, C. Liu, C. L. Gao, D. Qian, J.-F. Jia, and F. Liu, Nat. Commun. 4, 1384 (2013).
[29] L. Miao, Z. F. Wang, W. Ming, M.-Y. Yao, M. Wang, F. Yang, Y. R. Song, F. Zhu, A. V. Fedorov, Z. Sun, C. L. Gao, C. Liu, Q.-K. Xue, C.-X. Liu, F. Liu, D. Qian, and J.-F. Jia, Proc. Natl. Acad. Sci. USA 110, 2758 (2013).
[30] G. Q. Huang and B. Li, EPL 104, 57003 (2013).
[31] L. Miao, Z. F. Wang, M.-Y. Yao, F. Zhu, J. H. Dil, C. L. Gao, Canhua Liu, F. Liu, D. Qian, and J.-F. Jia, Phys. Rev. B 89, 155116 (2014).
[32] A. Eich, M. Michiardi, G. Bihlmayer, X.-G. Zhu, J.-L. Mi, Bo B. Iversen, R. Wiesendanger, Ph. Hofmann, A. A. Khajetoorians, and J. Wiebe, Phys. Rev. B 90, 155414 (2014).
[33] K. Govaerts, K. Park, C. De Beule, B. Partoens, and D. Lamoen, Phys. Rev. B 90, 155124 (2014).
[34] H. W. Yeom, S. H. Kim, W. J. Shin, K.-H. Jin, J. Park, T.-H. Kim, J. S. Kim, H. Ishikawa, K. Sakamoto, and S.-H. Jhi, Phys. Rev. B 90, 235401 (2014).
[35] T. Shoman, A. Takayama, T. Sato, S. Souma, T. Takahashi, T. Oguchi, K. Segawa, and Y. Ando, Nat. Commun. 6, 6547 (2015).
[36] P. E. Blöchl, Phys. Rev. B 50, 17953 (1994).
[37] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).
[38] G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).
[39] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, and I. Dabo, J. Phys.: Condens. Matter 21, 395502 (2009).