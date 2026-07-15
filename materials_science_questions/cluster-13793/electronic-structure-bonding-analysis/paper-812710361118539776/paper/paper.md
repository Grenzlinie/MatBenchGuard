![](./images/812710361118539776_1.jpg)

Applied Clay Science 183 (2019) 105356

Contents lists available at ScienceDirect

# Applied Clay Science

journal homepage: www.elsevier.com/locate/clay

![](./images/812710361118539776_2.jpg)

![](./images/812710361118539776_3.jpg)

## Research Paper

# DFT and 2D-CA methods unravelling the mechanism of interfacial interaction between amino acids and Ca-montmorillonite

Hai-long Li$^{\text{a}}$, Liang Bian$^{\text{a,b},*}$, Fa-qin Dong$^{\text{a},*}$, Wei-min Li$^{\text{a}}$, Mian-xin Song$^{\text{a}}$, Jia-nan Nie$^{\text{a}}$, Xiao-nan Liu$^{\text{a}}$, Ting-ting Huo$^{\text{a}}$, Hong-ping Zhang$^{\text{a}}$, Bing Xu$^{\text{a}}$, Frank S. Riehle$^{\text{a}}$, Shu-hui Sun$^{\text{a}}$

$^{\text{a}}$ Key Laboratory of Solid Waste Treatment and Resource Recycle, School of Environment and Resource, Fundamental Science on Nuclear Wastes and Environmental Safety Laboratory, Southwest University of Science and Technology, Mianyang 621010, Sichuan, China
$^{\text{b}}$ Institute of Gem and Material Technology, Hebei GEO University, Shijiazhuang 050000, Hebei, China

---

### ARTICLE INFO

**Keywords:**
Adsorption
2D-CA methods
Orbital coupling
Interfacial interaction

### ABSTRACT

We explored the effect of contact time on the interfacial interaction mechanism of amino acids (AAs) connected to the aluminol group (AlOH) and interlayer Ca ions of Ca-montmorillonite (Ca-Mt) in an aqueous solution using density functional theory (DFT) and two-dimensional correlation analysis (2D-CA) technology. The results showed that these interactions include electrostatic (or van-der-Waals) interaction, cation exchange and hydrophilic interaction. In particular, the electrostatic (or van-der-Waals) interaction between the $-\text{COO}^{-}$(H) (and $-\text{NH}_{3}^{+}$) groups of the AAs and surface negative O atoms of Ca-Mt were found to be the main interaction leading to the adsorption behaviour of AAs onto Ca-Mt. With increasing contact time, the Ca-d$^{0}$ orbital splitting ($\text{d}_{x^{2}-y^{2}} \rightarrow \text{d}_{x^{2}-y^{2}}^{2} + \text{d}_{z^{2}}^{2}$) not only changes the orbital coupling between the Ca-d$^{0}$ and O-2p$^{4}$ orbitals (Ca-$\text{d}_{x^{2}-y^{2}}^{2}$-O-2p$^{4} \rightarrow$ Ca-$\text{d}_{x^{2}-y^{2}}^{2}$ + $\text{d}_{z^{2}}^{2}$-O-2p$^{4}$) but also enhances the formation of $\text{Ca}^{+}$-$-\text{COO}^{-}$(H) p-p $\sigma$ (neutral: glycine and serine) and $\text{Ca}^{+}$-$-\text{NH}_{3}^{+}$ p-p $\pi$ (charged: glutamate and arginine) hybrid orbitals, as well as the cation exchange (AlOH-Ca + AAs) that mainly contributes to the short-range van-der-Waals interaction. Furthermore, the H-1 s ($\text{H}_{2}\text{O}$) orbital is degenerate, which in turn enhances the orbital overlap of H-1 s ($\text{H}_{2}\text{O}$) with O-2p$^{4}$ (-HOCO) and N-2p$^{3}$ ($-\text{NH}_{3}$), leading to the formation of hydrated clusters: $-\text{NH}_{3}(\text{H}_{2}\text{O})^{+}$ and $-\text{HOCO}(\text{H}_{2}\text{O})^{-}$. The hydrophilic interaction (AlOH-$\text{H}_{2}\text{O}$ + AAs) mainly contributes to the long-range electrostatic interaction. The results of the study provide a new perspective to understand the adsorption process of AAs onto clay mineral surfaces.

---

## 1. Introduction

The interfacial interaction of amino acids (AAs) with clay minerals, as a potentially important process in the natural environment, is closely related to the adsorption kinetics of AAs onto mineral surfaces in soils and sediments (Zaia, 2004; Lambert, 2008; Yu et al., 2013; Bu et al., 2019; Bu et al., 2017). The contact time, which is the most important factor in adsorption kinetics of AAs onto clay minerals, not only reflects the changes in the ionic species (neutral$\rightarrow$zwitterionic) of the AAs and charge characteristics (protonation/deprotonation) of the mineral surfaces, but also reflects the changes in the chemisorption process (edge/surface adsorption$\rightarrow$interlayer adsorption) (Swadling et al., 2013; Pagel-Wieder, et al., 2007; Dong et al., 2018). Note that the contact time for minerals to adsorb different AAs (serine, glycine, arginine and glutamate, etc.) under equilibrium conditions can be different in a natural environment (Zaia et al., 2008; Friebele et al., 1980). For example, the contact time for adsorption equilibrium in the case of serine, glycine, arginine and glutamate adsorbed onto montmorillonite (Mt) was approximately 4 h, 2 h, 2 h and 4 h, respectively (Hedges and Hare, 1987). These results reflect the differences in the reaction mechanism and the nature of the interaction between AAs and minerals on the time scale of the process. The causes of these differences are related to the transition mechanism of the interactions, including electrostatic (or van-der-Waals) interaction, cation exchange, and hydrophilic

---

Abbreviations: Ca-Mt, Ca type montmorillonite; AA, Amino acid; DFT, density functional theory; GGA, generalized gradient approximation; PBE, Perdew Burke Ernzerhof; DNP, double numerical integration with polarization; PAW, potential projector augmented wave; PDOS, partial densities of states; $\varepsilon_{(\omega)}$, dielectric functions; CB, conduction band; VB, valence band; dE$_{\text{ad}}$/dN, absolute average adsorption energy; CASTEP, Cambridge Sequential Total Energy Package; -COO⁻, carboxyl; $-\text{NH}_{3}^{+}$, amino; AlOH, aluminol group; e⁻, electron; h⁺, hole

* Corresponding authors at: Key Laboratory of Solid Waste Treatment and Resource Recycle, School of Environment and Resource, Fundamental Science on Nuclear Wastes and Environmental Safety Laboratory, Southwest University of Science and Technology, Mianyang 621010, Sichuan, China.

E-mail addresses: bianliang@swust.edu.cn (L. Bian), fqdong@swust.edu.cn (F.-q. Dong).

https://doi.org/10.1016/j.clay.2019.105356
Received 1 January 2019; Received in revised form 24 October 2019; Accepted 28 October 2019
0169-1317/ © 2019 Elsevier B.V. All rights reserved.

interaction (Ramos and Javier Huertas, 2013; Arora et al., 2016). Thus, the study of the transition mechanism of interaction with contact time contributes to a better understanding of the kinetic process and the adsorption behaviour of AAs with clay mineral surfaces (Yu et al., 2013; Ramos and Javier Huertas, 2013).

Naturally abundant clay minerals (montmorillonite, kaolinite, sa- ponite, etc.) in soils can absorb various biomolecules (amino acids, proteins, purines, pyrimidines, etc.) in the natural environment (Yu et al., 2013; Lambert, 2008; Polubesova et al., 2010). Among these clay minerals, Ca-Mt has a great adsorption capacity for AAs due to its high cation exchange capacity $(88-90 meq \cdot 100 g^{-1})$ and specific surface area $(\sim 800 m^{2} \cdot g^{-1})$ (Kalra et al., 2000; Newman et al., 2002; Gu et al.,2011; Laby, et al., 1962). Recently, the adsorption kinetic studies of AAs onto Ca-Mt allowed for interpreting the interaction mechanism involved in the adsorption reactions. For example, Ramos reported that glycine adsorption was dominated by complexation of the carboxylate group of zwitterionic glycine by edge and surface sites owing to electrostatic interaction at low glycine concentrations $(1.0-30.0 mmol \cdot L^{-1})$ (Ramos and Javier Huertas, 2013; Jaber et al., 2014). With increasing contact time, when the edge and surface sites were saturated, the ad- sorption of AAs through the cation exchange interaction in the inter- layer space became the prevailing factor (Ramos and Javier Huertas,2013). However, the maximum adsorption capacity $(186 mmol \cdot L^{-1})$ of adsorbed glycine exceeded the one resulting from cation exchange of Mt. $(35-40 mmol \cdot L^{-1})$ in the pH-neutral environment (Hedges and Hare, 1987; Farias et al., 2014). The reason for this is that the in- creasing of contact time led to change of the pH of the solution, which affected the surface charge of Mt. and the degree of ionization of AAs, leading to a change in the electrostatic (or van-der-Waals) interaction and hydrogen bond formation (Tran and James, 2012). These kinetic studies can be very useful to explain the possible interfacial interaction at different adsorption stages. However, it is difficult to explain the reason for the transition of the interfacial interaction with contact time, which becomes an obstacle to research the adsorption mechanism re- lated to changes of the Ca-Mt surface structure and the molecular structure of the AAs (Zhao and Burns, 2012). Furthermore, adsorption of AAs onto clay minerals that occurs quickly (such as, the adsorption of lysine and glutamic acid by Mt. reached apparent equilibrium in < 60 min) (Wang and Lee, 1993; Ding and Henrichs, 2002; Shaker et al.,2012) and the transition of the interfacial interaction of AAs + Mt. are still unclear because of the limitations of experimental techniques.

Recently, computational modelling studies have shown the poten- tial to provide significant insight into this question, how the Mt. was adsorbed bio-molecules at the molecular and atomic level (Zhao and Burns, 2012; Berghout et al., 2008; Joshi and Aldersley, 2013; Mignon et al., 2009). For AAs incorporated into the Mt. surface, an interesting study by Newman provided new insight into the interaction of a model Mt. and AAs (tyrosine, phenylalanine) using a molecular dynamics(MD) method (Newman et al., 2002). The simulation provided detailed insight into the arrangement of the counterion and water in the inter- layer of Mt. and suggested possible guest-layer interaction (cation ex- change, electrostatic interaction and hydrogen bonds) (Yu et al., 2000;Katti et al., 2005). E. Escamilla-Roa used density functional theory(DFT) to qualitatively study the adsorption behaviour of glycine onto Mt (Khoury et al., 2010). The calculations showed that glycine was adsorbed as a zwitterionic form in the interlayer through cation ex- change $(K^{+}$-glycinium), electrostatic interaction and hydrogen bond formation (Roa-Escamilla et al., 2017; Ho et al., 2012). However, the interfacial interaction can be dynamic due to the chemical reactions in the adsorption process (Zhao and Burns, 2012). The transition me- chanism of interaction occurring at the Ca-Mt + AAs interfaces is still far from a general understanding, especially at the electronic level. To solve this issue, Bian and co-workers used DFT and two-dimensional correlation analysis (2D-CA) methods to quantitatively study the orbital degenerate/split and electronic transition mechanism of minerals in the process of externally environmental (temperature, doping content, etc.) accumulation (Bian et al., 2015a, b, c). These investigations provided a novel pathway for the adsorption process of AAs onto Mt. at the elec- tronic scale with increasing contact time. Therefore, these computa- tional modelling approaches enable us to use fully atomistic large-scale classical MD and DFT to explore the interaction mechanism of Ca- Mt + AAs and to use 2D-CA methods to analyse the transition me- chanism of interfacial interaction during the adsorption process. The present study is expected to have significant relevance in understanding the transition mechanism of cation exchange and hydrophilic interac- tion between amino acids and clay minerals.

## 2. Computational details

### 2.1. Structural models

The Mt. structures include interlayer cations (e.g. $Ca^{2+}, K^{+}$and $Na^{+}$) and a 2:1 layer structure of phyllosilicates, which have one oc tahedral sheet sandwiched between two tetrahedral sheets (Parolo et al., 2012; Bu et al., 2019; Yuan et al., 2013). A unit cell model of Ca-Mt $(Ca[Al_{4}][Si_{8}O_{20}](OH)_{4})$ was used in this paper, with crystal lattice cell parameters $(a=4.80-5.0 \AA$, $b=8.30-8.70 \AA$, $c=13.90-14.50 \AA$ and all angles equal to $90^{\circ}$ ) that were consistent with the experimental reported values, as shown in Table 2 (Jaber et al.,2014; Yu et al., 2013; Kitadai et al., 2009; Cuadros et al., 2009, Fonseca et al., 2018). In these models, only isomorphic substitutions of one $Al^{3+}-3s^{2}3p^{1}$ by $Fe^{2+}-3d^{6}4s^{2}$ (or $Mg^{2+}-2p^{6}3s^{2}$) in the O-sheet (octahe dral sheet) were evaluated, namely, $Ca-Mt_{Fe}$ (or $Ca-Mt_{Mg}$). That in the in terlayer of Ca-Mt, the free volumes were reduced $(0.199 nm^{3} \to$ $0.121-0.132 nm^{3}$), being chiefly occupied by $Ca-3p^{6}4s^{2}$ and $O-2p^{4}$ states, as illustrated in Table 1. The molecular diffusion paths of the AAs and water molecules increase approximately 1.6-1.8 times and for glycine molecules are $0.56-0.6 nm^{3}$. The AAs clusters, including glycine $(C_{14}N_{7}P_{11}H_{24},$ $4.98-5.03 nm^{3})$, serine $(C_{18}N_{7}O_{15}H_{31},$ $6.1-6.47 nm^{3})$, glutamate $(C_{29}N_{7}O_{19}H_{45},$ $5.4-6.1 nm^{3})$ and arginine $(C_{27}N_{19}O_{11}H_{51},$ $6.84-7.1 nm^{3})$, were established (see Fig. 1a). To study the adsorption of AAs on the surface of Ca-Mt, a $16 \AA$ vacuum region in the z direction was employed in our calculation (Mignon et al., 2009). For both structures, a $2×1×1$ super-cell was used, and the interlayer cations $(Ca^{2+})$ were surrounded by four water molecules (each $Ca^{2+}$ cation was surrounded by two water molecules) in the interlayer space in accordance with Escamilla's (Roa-Escamilla et al., 2017) and Fonseca's(Fonseca et al., 2018) works. The grand canonical Monte Carlo (GCMC) method via Adsorption Locator was used to adsorb different AAs (ar- ginine, glutamate, glycine, serine) and four water molecules onto the surface of Ca-Mt. The optimized lattice constants $(2×1×1$ supercell) of Ca-Mt + AAs were $a=10.02-10.06 \AA$, $b=8.30-8.70 \AA$, $c=32.70-33.60 \AA$, $\alpha=\beta=\gamma=89^{\circ}-91^{\circ}$, as shown in Fig. 1b.

### 2.2. Methodology

The Accelrys Material Studio software was used to perform all GCMC and MD simulations and quantum mechanical calculations. First, the GCMC simulations via the Adsorption Locator were used to calcu- late the interaction energy of Ca-Mt + AAs. Conjugate gradient methods were adopted to minimize the MD simulation initial config- urations (GCMC simulation final configurations) (Zhang et al., 2018a,

Table 1
Free volumes (F, $nm^{3}$) of various AAs in Ca-Mt in an aqueous environment.

<table>
<thead>
  <tr>
    <th></th>
    <th>Ca-Mt</th>
    <th>Ca-Mt<sub>Mg</sub></th>
    <th>Ca-Mt<sub>Fe</sub></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Pure</td>
    <td>0.18</td>
    <td>0.21</td>
    <td>0.18</td>
  </tr>
  <tr>
    <td>Glycine</td>
    <td>0.56</td>
    <td>0.57</td>
    <td>0.6</td>
  </tr>
  <tr>
    <td>Serine</td>
    <td>0.33</td>
    <td>0.34</td>
    <td>0.34</td>
  </tr>
  <tr>
    <td>Glutamate</td>
    <td>0.33</td>
    <td>0.31</td>
    <td>0.32</td>
  </tr>
  <tr>
    <td>Arginine</td>
    <td>0.37</td>
    <td>0.32</td>
    <td>0.36</td>
  </tr>
</tbody>
</table>

![](./images/812710361118539776_4.jpg)

Fig. 1. (a) Structural diagram, (b) structure model and (c) adsorption energy (eV) of various AAs and Ca-Mt in an aqueous environment, (d) total charge density (eV).

b; Zhao and Burns, 2012). Then, 1000 ps NVE ($T = 298.0$ K) and NPT ($T = 298.0$ K, pressure $= 0.1$ MPa) MD simulations via the Forcite were relaxed for the models of Ca-Mt + AAs and performed to reach the equilibrium state (final configurations) (Zhang et al., 2018a, b). The short-range van-der-Waals and long-range electrostatic interaction were simulated by the atom-based and Ewald + Group methods, respectively. Finally, the initial input in the DFT calculations was taken from the MD simulation final configurations. The structure optimization and properties calculation of the Ca-Mt and Ca-Mt + AAs were performed by means of quantum mechanical calculations based on DFT using the GGA (generalized gradient approximation) and PBE (Perdew-Burke- Ernzerhof) exchange correlation functional (Bian et al., 2015a, b, c). The Dmol3 was used for structure optimization at a constant volume only in the preliminary calculations. The CASTEP was mainly used for property calculations (Roa-Escamilla et al., 2017). The highly accurate full potential projector augmented wave (PAW) method with ultrasoft pseudopotentials was used to describe the electron-ion interactions in the valence band region. Brillouin-zone integrations were calculated with a gamma-centered $3 \times 3 \times 3$ Monkhorst-Pack k-point mesh. The convergence criteria for the energy, maximum force, maximum displacement and SCF tolerance was set as $1.0 \times 10^{-5}$ eV/atom, $0.01$ eV/Å, $1.0 \times 10^{-4}$ Å and $1.0 \times 10^{-4}$ eV/atom, respectively. The DNP numerical basis set with semi-core pseudopotentials was comparable to Gaussian 6-31 G(d, p), and its accuracy for describing hybridized bond strength has been tested (Bian et al., 2015a, 2015b, 2015c). The density matrix convergence threshold was set to $1 \times 10^{-6}$. A Fermi smearing of 0.005 Hartree and a real-space cutoff of 0.45 nm

<table><thead><tr><th colspan="6">Table 2 Average lattice constants a, b, c (nm), bond lengths (nm) and bond angles ($\alpha$, $^{\circ}$) of different Ca-Mt obtained from experimental and theoretical methods. The lattice angles are 89–91$^{\circ}$ ($\alpha$~$\beta$~$\gamma$), respectively.</th></tr></thead><tbody><tr><td></td><td>Pure</td><td>Ca-Mt + AAs</td><td>Ca-Mt$_{Fe}$ + AAs</td><td>Ca-Mt$_{Mg}$ + AAs</td><td>Ref</td></tr><tr><td>a</td><td>0.48–0.5</td><td>0.51–0.53</td><td>0.51–0.52</td><td>0.51–0.52</td><td>0.51–0.52</td></tr><tr><td>b</td><td>0.83–0.87</td><td>0.88–0.91</td><td>0.88–0.9</td><td>0.89–0.91</td><td>0.88–0.9</td></tr><tr><td>c</td><td>1.39–1.45</td><td>3.27–3.36</td><td>3.27–3.3</td><td>3.3–3.36</td><td>1.2–1.6</td></tr><tr><td>Si-O</td><td>0.16–0.17</td><td>0.16–0.17</td><td>0.15–0.16</td><td>0.16–0.17</td><td>0.16</td></tr><tr><td>Al-O</td><td>0.17–0.18</td><td>0.17–0.18</td><td>0.18–0.19</td><td>0.18–0.19</td><td>0.17</td></tr><tr><td>Ca-Ca</td><td>1.39–1.45</td><td>0.27–0.46</td><td>0.28–0.52</td><td>0.45–0.75</td><td>1.2–1.6</td></tr><tr><td>$\alpha_{O-Al-O}$</td><td>90</td><td>59–62</td><td>72–75</td><td>53–72</td><td>89–91</td></tr><tr><td>$\alpha_{O-Fe(Mg)-O}$</td><td>–</td><td>–</td><td>72–78</td><td>62–66</td><td>–</td></tr><tr><td>$\alpha_{O-Si-O}$</td><td>100–101</td><td>110–112</td><td>102–116</td><td>109–118</td><td>100–101</td></tr></tbody><tfoot><tr><td colspan="6">(Ref: Jaber et al., 2014; Yu et al., 2013; Kitadai et al., 2009; Cuadros et al., 2009, Fonseca et al., 2018)</td></tr></tfoot></table>

<table><thead><tr><th colspan="4">Table 3 Interaction energies for the different group pairs in the systems (kJ$\cdot$mol$^{-1}$).</th></tr></thead><tbody><tr><td></td><td>Adsorption energy</td><td>dE$_{\text{ad}}$/dN (AAs)</td><td>dE$_{\text{ad}}$/dN (H$_2$O)</td></tr><tr><td rowspan="4">Ca-Mt</td><td>Glycine</td><td>−3515.05</td><td>−3471.62</td><td>−48.03</td></tr><tr><td>Serine</td><td>−3980.74</td><td>−3891.58</td><td>−64.87</td></tr><tr><td>Glutamate</td><td>−4882.87</td><td>−4954.39</td><td>−14.13</td></tr><tr><td>Arginine</td><td>−5562.87</td><td>−5471.83</td><td>−17.56</td></tr><tr><td rowspan="4">Ca-Mt$_{\text{Mg}}$</td><td>Glycine</td><td>−3512.45</td><td>−3392.28</td><td>−55.72</td></tr><tr><td>Serine</td><td>−3843.05</td><td>−3786.04</td><td>−35.53</td></tr><tr><td>Glutamate</td><td>−9420.72</td><td>−9354.8</td><td>−13.13</td></tr><tr><td>Arginine</td><td>−4871.83</td><td>−4845.12</td><td>−4.72</td></tr><tr><td rowspan="4">Ca-Mt$_{\text{Fe}}$</td><td>Glycine</td><td>−3362.85</td><td>−3231.81</td><td>−52.25</td></tr><tr><td>Serine</td><td>−3873.02</td><td>−3790.13</td><td>−54.67</td></tr><tr><td>Glutamate</td><td>−8986.5</td><td>−8969.61</td><td>−9.2</td></tr><tr><td>Arginine</td><td>−4917.44</td><td>−4868.28</td><td>−15.88</td></tr></tbody></table>

<table><thead><tr><th colspan="2">Table 4</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th><th></th></tr><tr><th colspan="10">Mulliken charges (e) of various AAs in the interlayers of Ca−Mt.</th></tr><tr><th></th><th></th><th>Pure</th><th colspan="2">Glycine</th><th colspan="2">Serine</th><th colspan="2">Glutamate</th><th colspan="2">Arginine</th></tr></thead><tbody><tr><td rowspan="2">Ca-Mt</td><td>-COO⁻(H)</td><td>−0.57~ − 0.29</td><td>&lt; 10 ps<br>−0.39</td><td>&gt; 10 ps<br>−0.43</td><td>&lt; 10 ps<br>−0.41</td><td>&gt; 10 ps<br>−0.26</td><td>&lt; 10 ps<br>−0.31</td><td>&gt; 10 ps<br>0.20</td><td>&lt; 10 ps<br>−0.41</td><td>&gt; 10 ps<br>−0.33</td></tr><tr><td>-NH₃⁺</td><td>−0.17~ − 0.16</td><td>−0.33</td><td>−0.23</td><td>−0.21</td><td>−0.10</td><td>−0.24</td><td>−0.24</td><td>−0.31</td><td>−0.16</td></tr><tr><td rowspan="2">Ca-MtMg</td><td>-COO⁻(H)</td><td>−0.57~ − 0.29</td><td>−0.31</td><td>−0.42</td><td>−0.35</td><td>−0.33</td><td>−0.39</td><td>−0.37</td><td>−0.37</td><td>−0.32</td></tr><tr><td>-NH₃⁺</td><td>−0.17~ − 0.16</td><td>−0.23</td><td>−0.30</td><td>−0.13</td><td>−0.12</td><td>−0.26</td><td>−0.48</td><td>−0.36</td><td>−0.12</td></tr><tr><td rowspan="2">Ca-MtFe</td><td>-COO⁻(H)</td><td>−0.57~ − 0.29</td><td>−0.42</td><td>−0.48</td><td>−0.51</td><td>−0.48</td><td>−0.39</td><td>−0.01</td><td>−0.52</td><td>−0.53</td></tr><tr><td>-NH₃⁺</td><td>−0.17~ − 0.16</td><td>−0.16</td><td>−0.20</td><td>−0.15</td><td>−0.19</td><td>−0.19</td><td>−0.28</td><td>−0.25</td><td>−0.47</td></tr></tbody></table>

were also used to improve the computational performance.

In general, the interaction process between AAs and Ca−Mt is not static in a certain external environment. However, in experiments, we could only measure the interaction at a certain time, and it was im- possible to measure the transformation of the interaction in the ad- sorption process. For this purpose, according to the change in adsorp- tion energy (the initial energy was transformed into long-range electrostatic interaction energy $(\sim 59.21 ~kJ \cdot mol^{-1})$ and short-range van-der-Waals energy $(\sim-98.29 ~kJ \cdot mol^{-1})$ , see Fig. 1c. The 2D-CA methods were used to describe the orbital fluctuation of Ca-Mt + AAs in 20 ps near the transition point (approximately 59.21 eV) of interac- tion energy. Thus, the contact time was distinguished by the changes in total-DOS (-1.0-2.0 eV) as follows: time = 0-10 ps, time = 10-20 ps, as shown in Fig. 2a. The transformation process of the interaction was explained by analysing the orbital fluctuation near the energy transition point at approximately 10 ps, and the corresponding time-areas of in- teraction were 0-10 ps (< 10 ps) and 10-20 ps (> 10 ps). Therein, the orbital fluctuation (synchronous $(\varphi_{(e 1, e 2)})$ and asynchronous $(\phi_{(e 1, e 2)}))$ intensity and range reflect the trend of orbital degeneracy/splitting of Ca-Mt + AAs. The PDOS was formally defined as the dynamic spectrum of a system associated with the application of an external perturbation(Bian et al., 2015a, 2015b, 2015c). If $\varphi_{(e 1, e 2)} × \phi_{(e 1, e 2)}>0$ , the PDOS intensity variation observed for $e_{1}$ predominantly occurred before that observed for $e_{2}$ , which implied that there was enhancement of the lo calized orbital coupling (Bian et al., 2015a, 2015b, 2015c). This en- hancement of the localized orbital coupling could reflect the effect of Ca-Mt + AAs electron accumulation on the outer electron orbitals.

## 3. Results and discussion
Since the binding interaction between the AAs and Ca-Mt plays a role in the solvation energy, it is expected to contribute to the final state of electronic relaxation of the system after electron ionization. Although the molecules were subjected to ionization lose one electron at a time on a timescale that is too short for the nuclear rearrangement, charge transfer from the solvent to the ionic state is expected to reduce the binding energy of the electron. Compared to the coordination number of AAs in bulk water, it is clear that the AAs molecules are not fully coordinated. The adsorption mechanism of AAs molecules and Ca-Mt are involved in a variety of electrostatic (or van-der-Waals) interaction, cation exchange and hydrophilic interaction (Ramos and Javier Huertas, 2013; Dong et al., 2018; Zhao and Burns, 2012; Roa- Escamilla et al., 2017).

Before studying these interaction mechanism, we calculated the ad- sorption energy of the Ca-Mt + AAs systems, distinguishing the effect of surface charges of AAs (see Table 3). In general, it is a chemical adsorption process for highly negative charge surface area of Ca-Mt absorbing charged AAs (glutamate and arginine) with the electrostatic force. Meanwhile, the "double electronic layers" between charged AAs and Mt. produce some high energy density oxygen to absorb charged AAs with the short-range chemical adsorption (short-range van-der-Waals force), based on the smaller adsorp- tion energy (Ca-Mt: $-5471.83 \sim-4882.87 ~kJ \cdot mol^{-1}$ , Ca-Mt $Fe_{Fe}$ : $-8986.50 \sim$  $-4868.28 kJ \cdot mol^{-1}, Ca-Mt_{Mg}: -9420.72 -4845.12 kJ \cdot mol^{-1}$ , see Table 3). However, the ionizable surface aluminol group (AlOH) has an amphoteric behaviour and can take up either a proton $(H^{+})$ or an $OH^{-}$ de pending on the nature of the AAs (Lambert, 2008). Compared to the charged AAs molecules, the active $N^{+}$ ions of neutral AAs (glycine and serine) have tendencies to change from the surface hydrogen adsorption processes to the chemical adsorption processes owing to the long-range electrostatic inter- action between $-NH_{3}^{+}$ (and $-COOH)^{-}$ group and AlOH group with rela tively high adsorption energy (Ca-Mt: $-3980.74 -3471.62 kJ \cdot mol^{-1}$ , Ca $Mt_{Fe}: -3873.02 -3231.81 kJ \cdot mol^{-1}, Ca-Mt_{Mg}: -3843.05 -$ 3392.28 kJ-mol-1, see Table 3). The presence of single -COO-(H) and $-NH_{3}^{+}$ entities ensures charged binding sites for surface negative O atoms of Ca-Mt (Dong et al., 2018). The H-s orbital of AAs molecules enhances the surface potentials of C=O sp2 and N-H sp. hybrid orbital with the neigh- bouring C-p and N-p states. This will induce the surface O-2p states in Ca-Mt to form two new -C-O-O sp3 and -NH-O sp2 hybrid orbital with 0.04-0.45 e and 0.02-0.2 e lost; see Table 4. It promotes an active H atom to move away from the -OH (or -NH) bond. A new hydrogen bond forms, increasing the electron transfer path, and the broken bonds emerge in the charge transitions of the type $C=O \to C-O-$ and $N^{3+} \to N^{+}$ . The $-COO^{-}(H)$ groups are seen to reside in the regions at approximately 0.12 nm (-C-OH) and 0.14 nm $(-C=O)$ compared to the $-NH_{3}^{+}$ groups at 0.11 nm. In short, the N atom of the $-NH_{3}^{+}$ group is mainly interacting with surface O atoms by short-range van-der-Waals interaction, whereas the C=O bond of the -COOH group is interacting via long-range electrostatic interaction.

### 3.1. Electrostatic (or van-der-Waals) interaction on the surface of an Al-O octahedron
The Kohn-Sham electron band structure of Ca-Mt is evaluated

<table><thead><tr><th colspan="2">Table 5</th><th></th><th></th><th></th><th></th><th></th><th></th><th></th><th></th></tr><tr><th colspan="10">Mulliken charges (e) of aluminium-oxygen octahedrons.</th></tr><tr><th></th><th></th><th>Pure</th><th colspan="2">Glycine</th><th colspan="2">Serine</th><th colspan="2">Glutamate</th><th colspan="2">Arginine</th></tr></thead><tbody><tr><td rowspan="2">Ca-Mt</td><td>0</td><td>−1.12</td><td>&lt; 10 ps<br>−1.12</td><td>&gt; 10 ps<br>−0.78</td><td>&lt; 10 ps<br>−1.16</td><td>&gt; 10 ps<br>−0.72</td><td>&lt; 10 ps<br>−1.09</td><td>&gt; 10 ps<br>−0.57</td><td>&lt; 10 ps<br>−1.05</td><td>&gt; 10 ps<br>−0.60</td></tr><tr><td>Al</td><td>2.01</td><td>2.12</td><td>2.08</td><td>2.08</td><td>2.11</td><td>2.06</td><td>2.07</td><td>2.07</td><td>2.08</td></tr><tr><td rowspan="3">Ca-MtMg</td><td>0</td><td>−1.12</td><td>−1.13</td><td>−0.81</td><td>−1.19</td><td>−0.71</td><td>−1.10</td><td>−0.63</td><td>−1.11</td><td>−0.59</td></tr><tr><td>Al</td><td>1.93</td><td>2.04</td><td>2.02</td><td>2.05</td><td>2.00</td><td>2.02</td><td>2.00</td><td>2.10</td><td>2.13</td></tr><tr><td>Mg</td><td>2.4</td><td>2.23</td><td>2.20</td><td>2.23</td><td>2.23</td><td>2.09</td><td>2.14</td><td>2.13</td><td>2.20</td></tr><tr><td rowspan="3">Ca-MtFe</td><td>0</td><td>−1.16</td><td>−1.11</td><td>−0.77</td><td>−1.04</td><td>−0.71</td><td>−1.05</td><td>−0.62</td><td>−1.05</td><td>−0.59</td></tr><tr><td>Al</td><td>2.01</td><td>1.97</td><td>1.96</td><td>1.97</td><td>1.94</td><td>1.94</td><td>1.92</td><td>1.95</td><td>1.88</td></tr><tr><td>Fe</td><td>1.03</td><td>1.62</td><td>2.24</td><td>1.15</td><td>1.01</td><td>0.79</td><td>0.37</td><td>1.32</td><td>0.85</td></tr></tbody></table>

<table><caption>Table 6 Elective electron/hole mass of Ca-Mt, Ca-Mt-Mg and Ca-Mt-Fe.</caption>
<tbody><tr><td colspan="2">Elective mass ($\times 10^{-31}$ kg)</td><td colspan="2">Glycine</td><td colspan="2">Serine</td><td colspan="2">Glutamate</td><td colspan="2">Arginine</td></tr>
<tr><td></td><td></td><td>electron</td><td>hole</td><td>electron</td><td>hole</td><td>electron</td><td>hole</td><td>electron</td><td>hole</td></tr>
<tr><td rowspan="2">Ca-Mt</td><td>$&lt;$ 10 ps</td><td>10.59</td><td>43.86</td><td>28.94</td><td>39.15</td><td>7.21</td><td>11.16</td><td>58.14</td><td>19.91</td></tr>
<tr><td>$&gt;$ 10 ps</td><td>18.34</td><td>23.38</td><td>35.06</td><td>27.74</td><td>3.31</td><td>3.64</td><td>23.96</td><td>35.04</td></tr>
<tr><td rowspan="2">Ca-Mt$_{Mg}$</td><td>$&lt;$ 10 ps</td><td>63.29</td><td>23.26</td><td>23.84</td><td>16.6</td><td>5.95</td><td>4.33</td><td>8.32</td><td>49.20</td></tr>
<tr><td>$&gt;$ 10 ps</td><td>11.11</td><td>19.84</td><td>9.47</td><td>1.72</td><td>3.41</td><td>9.29</td><td>8.18</td><td>14.88</td></tr>
<tr><td rowspan="2">Ca-Mt$_{Fe}$</td><td>$&lt;$ 10 ps</td><td>18.34</td><td>78.50</td><td>38.46</td><td>10.99</td><td>9.84</td><td>37.31</td><td>3.37</td><td>3.69</td></tr>
<tr><td>$&gt;$ 10 ps</td><td>7.87</td><td>71.23</td><td>11.76</td><td>16.23</td><td>49.51</td><td>15.63</td><td>32.05</td><td>30.68</td></tr>
</tbody></table>

taking into account a specific path inside the Brillouin zone, which is included in the supporting information with high symmetry points depicted. The full band structure is shown at the top part of Fig. 2b-c together with the partial (per type of orbital) density of states (PDOS). Three deep bands (0.82 eV, 0.83 eV and 1.15 eV) can be seen in the band structure. Qualitatively, the direct gap is 0.82 eV, with a secondary indirect gap displaying a slightly larger energy of 1.15 eV and it is located between the G point at the valence bands (VB) and Q at the conduction band (CB). In this case, these peak structures reveal the electronic transitions between the O-2p uppermost VB and the lowest Ca-d CB just above the main band gap. Looking at the top of the VB that is derived from the O-2p⁴, Fe-3d⁵ and Mg-2p⁶ orbits, one can see that the electronic energy levels have a strong O-2p⁴ character (above 0.1 eV), with a much smaller contribution from the Fe-3d⁵, O-2p⁴ (-COO⁻(H)) and N-2p³ (-NH₃⁺) levels.

In previous reports (Lambert, 2008; Mignon et al., 2009; Mignon and Sodupe, 2012; Shi et al., 2013), the adsorption systems were found to be in agreement with various experimental observations pertaining to the relative adsorption of AAs in the presence of charge balancing. For example, the interaction between Mt. and lysine (our work, Dong et al., 2018) or glycine (Ramos and Javier Huertas, 2013) includes electrostatic interaction of the -NH₃⁺/-COO⁻ group and AlOH, van-der-Waals force or hydrogen bond of the -NH₃⁺/-COO⁻ group with surface oxygen atoms. Because Mt. have permanent negative and variable surface charges, the -COO⁻(H) and -NH₃⁺ groups affect the surface charge of Ca-Mt (Kitadai et al., 2009; Cuadros et al., 2009). The ionizable surface AlOH has an amphoteric behaviour and can take up the protonation/deprotonation processes, $AlOH + H^{+} \rightarrow AlOH_{2}^{+}$ (-NH₃⁺) and $AlOH + OH^{-} \rightarrow AlO^{-} + H_{2}O$ (-COO⁻(H)). Regarding the AAs occupying outer-sphere free volumes and substituting the cation-bridge of the Ca-Ca bonds, the -COO⁻(H) and -NH₃⁺ combine with the surface O ions is explained by the PDOS curves for nearly degenerate conduction-band, see in Fig. 2. With the contact time increasing, the PDOS state shows the electron orbital variations arise from the fluctuating range shift to the Fermi point. One band (Ca-d⁰, O-2p⁴ orbital) shifts towards the low energy region in the conduction band (0.5-2.8 eV), while the other band (Ca-d⁰, Al-3p³, Ca-4 s² orbital) shifts to the low energy region in the valence band $(-0.5-2.5$ eV), as indicated by the two arrows; see Fig. 3b. The band gap is reduced from 0.83 eV to 0.80-0.81 eV. Therein, the high energy density O-2pz state creates a part of the electron-hole defect pair $(e^{-}-h^{+})$ in which the orbital degeneracy decreases by approximately 11 electron·eV⁻¹. The $Al^{3 + }$ states of AlOH can capture a part of the hole defect $(h^{+})$ that is consistent with the increase (0.06-0.11 e) of Mulliken charges (see Table 5). In short, the Al site charge balancing can be principally used to explain the change in the adsorption process.

For example, with the contact time increasing, the Mg impurity can modify the partial excitation levels of the O states (VB region) at the octahedral Al-sites when the $Mg^{2 + }$ ion captures one electron $(e^{-})$ from an O-2p⁴ state; as a result, the Mg charges will be reduced to 0.17-0.23 e as seen in Table 5. The $Mg^{2 + }$-O sp3 hybrid orbital rearranges to become a $Mg^{+}$-O sp2 hybrid orbital. Whereas the O-2p⁴ orbital provides 0.01-0.02 e to ionize the -COO⁻(H) group $(MgOH + e^{-} \rightarrow Mg(OH)^{-})$, the -NH₃⁺ group captures 0.01-0.07 e from the O-p state of the negatively charged layer $(MgOH_{2}^{+} + 2OH^{-} + h^{+} \rightarrow MgO^{-} + 2H_{2}O)$, which leads to a decrease of the effective hole mass $(23.26 \times 10^{-31} \rightarrow 19.84 \times 10^{-31}$ kg). Differently, Fe impurities in the surface Al-site modification reveal an AAs-driven adsorption based on CB holes increasing (effective hole mass: $7.87 \times 10^{-31} \rightarrow 71.23 \times 10^{-31}$ kg), see Table 6. The p-p degenerate levels of the interlayer Fe orbitals suddenly increase from 1.00 electron·eV⁻¹ to 2.00 electron·eV⁻¹. This originates from the Fe-O hybrid orbital transition (sp2d → sp3d) and the corresponding increase of 0.29-1.5 e from changing the Fe charge state according to $Fe^{2 + } + h^{+} \rightarrow Fe^{3 + }$. Furthermore, the occupied Fe-d⁰ orbital affects the O-2p⁴ orbital energy by capturing $0.05-0.11 h^{+}$. Consequently, the different electrostatic (or van-der-Waals) interaction with octahedral (Al-O) will be responsible for the different adsorption behaviours of the -COO⁻(H) and -NH₃⁺ groups in the VB region.

### 3.2. Cation exchange at the interface

In addition to the electrostatic (or van-der-Waals) interaction, the cation exchange between Ca and AAs is the second factor governing adsorption (Dong et al., 2018; Roa-Escamilla et al., 2017). Fig. 3a shows that the bottom of CB mainly consists of empty Ca-d⁰ states, which are partly filled by Ca-4 s² electrons, but mostly benefit from electronic contributions from O-2p⁴ states. A close-up of the band structure is provided near the Kohn-Sham band gap, where we can see the VB-maximum and the VB-minimum occur at the G point. The intercalation levels of AAs at the bottom of the CB create a level vacancy, weakening the electron transfer rate of O-2p⁴ → Ca-4 s². Such transition requires a charge compensation from the neighbouring active groups, which means that the -COO⁻(H) and -NH₃⁺ groups of various AAs molecules transfer the O-2p⁴ and N-2p³ electrons to surface O-2p⁴ states according to the sudden enhancement in the H-1 s¹ orbital. It should be noted that

<table><caption>Table 7 Mulliken charges (e) of Ca ions of Ca-Mt configurations.</caption>
<tbody><tr><td></td><td>Pure</td><td colspan="2">Glycine</td><td colspan="2">Serine</td><td colspan="2">Glutamate</td><td colspan="2">Arginine</td></tr>
<tr><td></td><td></td><td>$&lt;$ 10 ps</td><td>$&gt;$ 10 ps</td><td>$&lt;$ 10 ps</td><td>$&gt;$ 10 ps</td><td>$&lt;$ 10 ps</td><td>$&gt;$ 10 ps</td><td>$&lt;$ 10 ps</td><td>$&gt;$ 10 ps</td></tr>
<tr><td>Ca-Mt</td><td>0.02-0.08</td><td>1.01</td><td>0.39</td><td>0.99</td><td>0.15</td><td>0.35</td><td>0.39</td><td>0.57</td><td>0.01</td></tr>
<tr><td>Ca-Mt$_{Mg}$</td><td>0.03-0.03</td><td>0.56</td><td>1.44</td><td>0.59</td><td>0.95</td><td>1.00</td><td>0.92</td><td>1.41</td><td>0.21</td></tr>
<tr><td>Ca-Mt$_{Fe}$</td><td>1.09-0.84</td><td>0.03</td><td>0.02</td><td>0.27</td><td>0.97</td><td>1.05</td><td>0.80</td><td>0.61</td><td>0.98</td></tr>
</tbody></table>

<table><caption>Table 8 Mulliken charges (e) of water.</caption>
<tbody><tr><th></th><th>Pure</th><th colspan="2">Glycine</th><th colspan="2">Serine</th><th colspan="2">Glutamate</th><th colspan="2">Arginine</th></tr>
<tr><th></th><th></th><th>&lt; 10 ps</th><th>&gt; 10 ps</th><th>&lt; 10 ps</th><th>&gt; 10 ps</th><th>&lt; 10 ps</th><th>&gt; 10 ps</th><th>&lt; 10 ps</th><th>&gt; 10 ps</th></tr>
<tr><td>Ca-Mt</td><td>−0.12</td><td>−0.45</td><td>−0.34</td><td>−0.32</td><td>−0.30</td><td>−0.27</td><td>−0.24</td><td>−0.35</td><td>−0.22</td></tr>
<tr><td>Ca-Mt<sub>Mg</sub></td><td>−0.12</td><td>−0.38</td><td>−0.39</td><td>−0.22</td><td>−0.27</td><td>−0.24</td><td>−0.23</td><td>−0.20</td><td>−0.27</td></tr>
<tr><td>Ca-Mt<sub>Fe</sub></td><td>−0.12</td><td>−0.10</td><td>−0.26</td><td>−0.31</td><td>−0.16</td><td>−0.30</td><td>−0.46</td><td>−0.34</td><td>−0.17</td></tr>
</tbody></table>

the sharp PDOS peaks at the top of the VB and the bottom of the CB are related to the localization of the wave functions corresponding to the highest occupied and unoccupied molecular orbitals between surface Ca (and O) atoms and active groups (${-COO}^-$(H) and ${-NH_3}^+$), as shown in Fig. 3b. The free energy barrier is highly cut off by the negatively charged layer hybrid orbital, therefore allowing free electron transfer in the local electron states (Roa-Escamilla et al., 2017). Consequently, the second adsorption factor is attributed to the $Ca^+$-COO$^-$(H) p-p $\sigma$ (neutral: glycine and serine) and $Ca^+$-NH$_3^+$ p-p $\pi$ (charged: glutamate and arginine) hybrid orbitals at the CB region; see Fig. 3c.

To fully and quantitatively understand the cation exchange process, we calculated the synchronous ($\varphi_{(e1,e2)}$) and asynchronous ($\psi_{(e1,e2)}$) spectra using the DFT + 2D-CA technique, as shown in Fig. 4. It should be noted that the localized Ca-d⁰ state exhibits a band-position shift and the d⁰-orbital splitting at the bottom of CB is coupled with the contact time increasing. The Ca-d⁰ states show that the electron orbital variations are arising from the classical intensity changes of two highly overlapped bands with a fixed band position and a relatively linear shape. One band (1.8 eV) decreases in intensity quickly, while the other band (1.5 eV) increases in intensity gradually, as indicated by the two arrows. This splitting of the Ca-d⁰ orbital induces the O-2p⁴ orbital to move towards the high energy region of CB (1.0-3.0 eV), which in turn enhances the Ca-d⁰-O-2p⁴ d-p orbital hybridization. Due to the effect of orbital coupling, the suddenly enhanced H-1 s¹ orbital gradually induces the degenerate d$_{x2+y2}$ orbital to split into d$_{x2+y2}$ and d$_{z2}$ orbitals but with no net change of moment. This reflects that the integral intensity of the Ca-d⁰ energy level peak is kept at a constant value, so the peak height decreases gradually as the band width increases, as shown in Fig. 4a. It chiefly excites the O-2p⁴ orbital fluctuation to shift to the high energy region in VB, which in turn enhances the Ca-d⁰-O-2p⁴ d-p orbital hybridization. The corresponding synchronous and asynchronous spectra show the fluctuation intensity (−2.0-3.0 eV) and fluctuation range (−1.0-3.0 eV) of the Ca-d⁰ orbital, as seen in Fig. 4b, c. According to the minimum energy principle, the d$_{z2}$ and d$_{x2+y2}$ orbitals will be more favourable than the d$_{xy}$, d$_{yz}$ and d$_{xz}$ orbitals for containing the electron. With contact time < 10 ps, the Ca-d$_{x2+y2}$ orbital preferentially hybridizes with the O-2p$_z$ orbital, producing $\pi$ hybrid orbitals (Ca-d$_{x2+y2}$-O-2p$_z$ sp3d bonding orbital). The d-p bonding orbitals contain weaker bound electrons (low-angular-momentum Ca-d⁰ and O-2p$_z$ orbitals), which forms for increasing the electronic transitions path, and the broken bonds emerge in the charge transitions of the type (e.g. C=O → C-O-). With contact time > 10 ps, the Ca-d$_{x2+y2}$ orbital splits into d$_{x2+y2}$ and d$_{z2}$, and the new Ca-dz² orbital (approximately −0.5-0.5 eV) couples with O-2p$_z$ to form $\sigma$ hybrid orbitals (Ca-dz²-O- 2p$_z$ sp3d2 bonding orbital), as shown in Fig. 4d. The O-2p electrons transfer from the single orientation (d$_{x2+y2}$: 0.5-2.8 eV) to the two orientations of Ca-d⁰ (d$_{z2}$: −0.5-0.5 eV; d$_{x2+y2}$: 0.5-2.8 eV). Some portion of the Ca²⁺ electrons are annihilated in the O-2p$_z$ orbital, i.e.,

![](./images/812710361118539776_5.jpg)

Fig. 2. (a) 2D-CA patterns of the total DOS, (b) and (c) band structure (and PDOS) at 0-10 ps and 10-20 ps.

![](./images/812710361118539776_6.jpg)

Fig. 3. (a) PDOS curves and 2D-CA patterns of the Ca-d⁰ orbital and (b) aluminium-oxygen octahedron of Ca-Mt absorbing AAs, the corresponding intensities of the synchronous (Sy) and asynchronous (Asy) of 2D-CA patterns of the Ca-d⁰ orbital are shown in Supplementary material. (c) The illustration of orbital spitting behaviours and electron transfer characteristics between AAs and Ca-Mt.

![](./images/812710361118539776_7.jpg)

Fig. 4. (a) The PDOS of the Ca-d⁰ orbital at 0-20 ps, (b) and (c) 2D-CA patterns of the Ca-d⁰ orbital at 0-10 ps and 10-20 ps, respectively. (d) Shows the illustration of hybridized orbitals between AAs and Ca-Mt.

![](./images/812710361118539776_8.jpg)

Fig. 5. Local density of states and dielectric function of Ca states in the interlayer of AA-Mt systems. (a) and (b) correspond to that of Ca-Mt, Ca-Mt-Mg and Ca-Mt-Fe at 0-10 ps and 10-20 ps, respectively.

Ca-charge changes from 0.21-0.92 e to 0.95-1.41 e. The Ca-d$_{x2+y2}$-O-2p$_{z}$ and Ca-d$_{z2}$-O-2p$_{z}$ hybrid orbitals provide many electronic energy levels for the unpaired electronic transition from O-2p$^{4}$ (-COO$^{-}$(H)) and N-2p$^{3}$ (-NH$_{3}$ $^{+}$) to O-2p$^{4}$ (AlOH group) orbitals in the CB (0-3 eV), releasing effective electrons to annihilate hole defects. The corresponding inter-atomic distance (-COO$^{-}$(H) and -NH$_{3}$ $^{+}$-Ca) was decreased (0.8 Å→0.5 Å) and the surface potential (-COO$^{-}$(H) and -NH$_{3}$ $^{+}$-Ca) was increased (0.32 eV→0.38 eV) (see Fig. 1d), which was consistent with our previous studies of the interaction of lysine adsorbed on the Mt. surfaces (Dong et al., 2018).

To investigate the electronic transition in the interlayer of Ca-Mt, we calculated the dielectric constant via the Kohn-Sham inter-band energy gaps (Bian et al., 2015a, 2015b, 2015c). Therein, the effective interaction within the positively charged Mt. layers happens through divalent Ca$^{2 + }$ as charge-balancing ions. The Ca$^{2 + }$ ion (> 0.5 e) is offset by the mono-valent Ca$^{+}$ (< 0.5 e) ion and the -COO$^{-}$(H) and -NH$_{3}$ $^{+}$ groups, and this charge disproportion of surface Ca is a key factor for degeneration of the charge density. The calculated $\varepsilon$ in Fig. 5a shows that a partial Ca-s electron captures an outer sphere H-s (-COO$^{-}$(H) and -NH$_{3}$ $^{+}$) to jump into an empty d$^{0}$ orbital with the contact time increasing. As the contact time increases, the Ca-d$^{0}$ splitting into Ca-d$_{x2+y2}$ and Ca-d$_{z2}$ orbitals, some of the O-2p$^{4}$ electrons jump into the empty Ca-3d$^{0}$ orbitals. Such a split Ca-d$^{0}$ orbital can easily hybridize with an O-2p$^{4}$ orbitals, enhancing the d-p (Ca-3d$^{0}$-O-2p$^{4}$) orbital hybridization. The highly sensitive d-p hybrid orbital weakens the sp3 (Ca-Ca) hybrid orbital strength. Therefore, the empty d$^{0}$ orbital is populated to be a 2d$_{3/2}$ state of the Ca$^{+}$ ion. The energy of the sp3 hybrid orbital (-COO$^{-}$(H) and -NH$_{3}$ $^{+}$) is lifted, and electrons associated with H$^{+}$ prefer to fill the out-of-plane Ca-2p$_{1/2}$ orbital. The Ca-3p$^{6}$ levels (CB) transfer to the Fermi point, correlating with the results of band gaps decreasing from 1.15 eV to 0.81-0.82 eV. Typically, Mg impurities create an electron-hole pair that can offset the positive-negative ion recombination between the Ca and O atom.

Indeed, the electronic transition can be affected by octahedral Al-O due to the amphoteric behaviour of the AlOH. Fig. 5b, c shows that the Fe$^{2 + }$ (or Mg$^{2 + }$) impurity occupying the Al$^{3 + }$-site provides a hole defect to capture part of the active H$^{+}$ (0.01-0.05 e or 0.03-0.1 e) of the -COO$^{-}$(H) group, due to the appearance of a high excitation level (> Fermi point), whereas the -COO$^{-}$(H) sp3 hybrid orbital changes to a sp2 hybrid orbital. Compared to the charge changes in -COO$^{-}$(H), the active N$^{+}$ ions of charged AAs tend to be N$^{2 + }$, resulting from the change of surface hydrogen adsorption (< - 4180 kJ$\cdot$mol$^{-1}$) to double electric layer adsorption (> - 4180 kJ$\cdot$mol$^{-1}$). This explains why the intercalation levels of AAs increase at 0-2 eV. Typically, we find high adsorption energy (- 8986.5~ - 9420.72 kJ$\cdot$mol$^{-1}$) for the double electric layer (-NH$_{4}$ $^{+}$ + AlOH$^{-}$) of the glutamate-octahedral.

An overview of static electron transfer processes shows that the Fe valence electrons occupying Al levels produce a high energy density oxygen state where the O$^{2 - }$ loses approximately 0.02-0.07 e. The positive charges attract the electrons inside the outer-sphere Ca ions in a way such that the Ca$^{+}$ ions are rapidly replaced by the mono-valent Ca$^{2 + }$ ions and a captured 0.06-0.93 h$^{+}$, where the Ca-d$^{0}$→s charge transition appears, see Table 7. The 2d$_{3/2}$ states of the Ca$^{2 + }$ ions are then populated as a consequence of the Fe-addition. The rate constant for reactions out of the excited 2p$_{1/2}$ state of O-2p$^{4}$ is found to be two or three orders of magnitude larger than the rate coefficients for reactions out of the two other states. Hence, the Ca$^{+}$-NH$_{3}$ $^{+}$ p-p $\pi$ hybrid orbital has more effect on the van-der-Waals interaction than on the electrostatic interaction of the Ca$^{+}$-COO$^{-}$(H) p-p $\sigma$ hybrid orbital in Ca-Mt$_{Fe}$ + AAs systems.

### 3.3. Hydrophilic interaction at the interface

Additionally, the distribution of water throughout the models is

another interesting aspect of this investigation. Previous reports have suggested that hydrogen bonding and hydrophobic interaction also play important roles during the adsorption of small bio-molecules onto the Mt. (Lambert, 2008; Ramos and Javier Huertas, 2013; Suter et al., 2012). With relatively low absolute average adsorption energy of $\mathrm{H}_{2} \mathrm{O}$ ($\mathrm{dE}_{\mathrm{ad}} / \mathrm{dN}_{(\mathrm{H} 2 \mathrm{O})}$: $-64.87 \sim-4.72 \mathrm{kcal} \cdot \mathrm{mol}^{-1}$), the water molecules dissociate from the surface outer-layers in order to provide an adsorption site for AAs molecules. The polar water molecules cut off the electron transfer paths of long-range Ca-O bonds near 0.2 nm. Thus, two new $-\mathrm{NH}_{3}{ }^{+} \cdot\left(\mathrm{H}_{2} \mathrm{O}\right)$ and $-\mathrm{HOCO}^{-} \cdot\left(\mathrm{H}_{2} \mathrm{O}\right)$ hydrated clusters are formed, whose bond lengths are ~0.25 nm. In contrast, a high absolute average of $\mathrm{dE}_{\mathrm{ad}} / \mathrm{dN}_{(\mathrm{AAs})}$ ($-9354.8 \sim-3471.62 \mathrm{kcal} \cdot \mathrm{mol}^{-1}$, see in Table 3) was beneficial to partial ionization of the buried hydrophobic residues of AAs molecules, which leads to a greater unfolding of AAs due to the electrostatic repulsion. The enhancement of AAs-adsorption strength leads to more exposure of hydrophobic groups of AAs on the hydration surface of $\mathrm{Ca}-\mathrm{Mt}$, the water molecules and $-\mathrm{NH}_{3}{ }^{+}$(and $-\mathrm{HCOO}^{-}$) groups are close to each other with the distance between $\mathrm{H}_{2} \mathrm{O}$ and $-\mathrm{NH}_{3}{ }^{+}$(and $-\mathrm{HCOO}^{-}$) groups decreases $(3.89-4.12 \AA \rightarrow 1.76-2.14 \AA)$, and then hydrated $-\mathrm{NH}_{3}{ }^{+} \cdot\left(\mathrm{H}_{2} \mathrm{O}\right)$ and $-\mathrm{HOCO}^{-} \cdot\left(\mathrm{H}_{2} \mathrm{O}\right)$ clusters are formed. That promotes AAs close to the surface of $\mathrm{Ca}-\mathrm{Mt}$ (distance of $\mathrm{AAs} \sim \mathrm{Ca}-\mathrm{Mt}$: $7.72-7.95 \AA \rightarrow 6.94-7.16 \AA$ ). Therefore, the hydrophilic interaction decreases the adsorption energy ($\mathrm{dE}_{\mathrm{ad}} / \mathrm{dN}_{(\mathrm{H} 2 \mathrm{O})}$: $-64.87 \sim-4.72 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$) of the $-\mathrm{NH}_{3}{ }^{+}$and $-\mathrm{HCOO}^{-}(\mathrm{H})$ groups into the surface of the $\mathrm{Ca}-\mathrm{Mt}$.

As shown in Fig. 6, water replacing cations become electron donors for providing valence electrons to the $\mathrm{O}-2 \mathrm{p}^{4}$ level. They can obviously cut off the hydrogen-bonding networks between the Ca (or O) atoms and active groups $\left(-\mathrm{COO}^{-}(\mathrm{H})\right.$ and $\left.-\mathrm{NH}_{3}{ }^{+}\right)$. As the contact time increases, the $\mathrm{H}-1$ s state of $\mathrm{H}_{2} \mathrm{O}$ exhibits orbital degeneration at the bottom of the conduction $(-1.2-2.3 \mathrm{eV})$, and the intensity of the corresponding peak was increased from 1.2 electrons$\cdot \mathrm{eV}^{-1}$ to 1.5 electrons$\cdot \mathrm{eV}^{-1}$, as shown in Fig. 7a. This enhanced $\mathrm{H}-1$ s orbital of $\mathrm{H}_{2} \mathrm{O}$ at the Fermi point $(-1.5-1.5 \mathrm{eV}$, see Fig. 6b) enhances the sp. orbital hybridization of $\mathrm{H}_{2} \mathrm{O}$ with $-\mathrm{HOCO}\left(\mathrm{H}-1 \mathrm{~s}-\mathrm{O}-2 \mathrm{p}^{4}\right)$ and $-\mathrm{NH}_{3}\left(\mathrm{H}-1 \mathrm{~s}-\mathrm{N}-2 \mathrm{p}^{3}\right)$ group, respectively. The orbital hybridization form is then changed

![](./images/812710361118539776_9.jpg)

![](./images/812710361118539776_10.jpg)

![](./images/812710361118539776_11.jpg)

Fig. 6. (a) PDOS curves and 2D-CA patterns of $-\mathrm{COO}^{-}(\mathrm{H})$ and $-\mathrm{NH}^{3+}$ groups of various AAs and (b) $\mathrm{H}_{2} \mathrm{O}$ in the interlayer of $\mathrm{Ca}-\mathrm{Mt}$, the corresponding intensities of synchronous (Sy) and asynchronous (Asy) of 2D-CA patterns of $-\mathrm{COO}^{-}(\mathrm{H})$ and $-\mathrm{NH}^{3+}-\mathrm{p}$ orbitals; see also Supplementary material. (c) Illustrates the hydrophilic interaction.

![](./images/812710361118539776_12.jpg)

Fig. 7. (a) the PDOS of the $\mathrm{H}_{2} \mathrm{O}-1$ s orbital at $0-20$ ps, (b) 2D-CA patterns of the $\mathrm{H}_{2} \mathrm{O}-1$ s orbital at $0-10$ ps and $10-20$ ps, and the corresponding intensities of synchronous (Sy) and asynchronous (Asy) of 2D-CA patterns of the $\mathrm{H}_{2} \mathrm{O}-1 \mathrm{~s}$ orbital are shown in Supplementary material. (c) An illustration of the hybridized orbital between $\mathrm{H}_{2} \mathrm{O}-1 \mathrm{~s}$ and a $-\mathrm{COO}^{-}(\mathrm{H})$ (and $-\mathrm{NH}^{3+}$)-p orbital.

from sp. $(-\mathrm{NH}_{3})$ and sp2 $(-\mathrm{HOCO})$ to sp3 $(-\mathrm{NH}_{3}(\mathrm{H}_{2} \mathrm{O})^{+}$ and $-\mathrm{HOCO}(\mathrm{H}_{2} \mathrm{O})^{-})$ orbital hybridization, as illustrated in Fig. 7b, c. The corresponding transfer of electrons increases from 0.12 to 0.47 e, and the surface potential increases from 0.28 to 0.32 eV, while the inter-atomic distance decreases from $5.3 \mathring{A}$ to $1.8 \mathring{A}$. These active hydrogen states improve the ability of surface lone pair electrons of water molecules to adsorb an active electron from surface layer active groups of AAs molecules, being hydrated clusters: $-\mathrm{NH}_{3}(\mathrm{H}_{2} \mathrm{O})^{+}$ and $-\mathrm{HOCO}(\mathrm{H}_{2} \mathrm{O})^{-}$. Therein, the sp2 and sp. states in the $-\mathrm{C}=\mathrm{O}$ and -NH bonds hybridize to the $\mathrm{H}_{2} \mathrm{O}$ sp3 orbital, losing 0.11-0.47 e, see Table 8. These hydrated clusters can be seen as two adhesive layers, which are stabilized by electrostatic interaction with water and basal octahedral O atoms (Roa-Escamilla et al., 2017). Furthermore, they can capture some surface layer free electrons even when the band gaps of the systems are 0 eV. Hence, the outer-sphere water molecules are also strongly adsorbed by AAs in the surface layers of Ca-Mt, and two new hydrated clusters are beneficial for the adsorption of various AAs.

## 4. Conclusions
In summary, we investigated the interfacial interaction mechanism of Ca-Mt + AAs using DFT and 2D-CA methods. The calculation results indicated that the significant adsorption factors were attributed to the electrostatic (or van-der-Waals) interaction (AlOH+AAs), cation exchange (AlOH-Ca + AAs) and hydrophilic interaction (AlOH-$\mathrm{H}_{2} \mathrm{O}$ + AAs). The N atom of the $-\mathrm{NH}_{3}{ }^{+}$group and the $\mathrm{C}=\mathrm{O}$ bond of the -COOH⁻ group were mainly interacting with surface O atoms by short-range van-der-Waals force and long-range electrostatic interaction, respectively. With the contact time increasing, the Ca-$\mathrm{d}^{0}$ orbital splitting enhances the Ca-$\mathrm{d}^{0}$-O-2$\mathrm{p}^{4}$ p-d (Mt) orbital hybridization, as well as the $\mathrm{Ca}^{+}-\mathrm{COO}^{-}(\mathrm{H})$ p-$\sigma$ O (neutral glycine and serine) and $\mathrm{Ca}^{+}-\mathrm{NH}_{3}{ }^{+}$p-p $\pi$ (charged glutamate and arginine) orbital hybridization. This then enhanced the cation exchange between the interlayer Ca ions and the AAs, which mainly changed into short-range van-der-Waals interaction. In addition, the H-1 s state of $\mathrm{H}_{2} \mathrm{O}$ exhibited coupling of degenerated orbitals with increasing contact time, which leads to an enhancement of the s-p orbital hybridization of $\mathrm{H}_{2} \mathrm{O}$ with $-\mathrm{HOCO}$ and $-\mathrm{NH}_{3}$ to form hydrated clusters: $-\mathrm{NH}_{3}(\mathrm{H}_{2} \mathrm{O})^{+}$ and $-\mathrm{HOCO}(\mathrm{H}_{2} \mathrm{O})^{-}$. The adhesive hydrated clusters as hydrophilic factors improve the adsorption of AAs on Ca-Mt and affects the long-range electrostatic interaction. Thus, the transformation of interaction occurring at the Ca-Mt + AAs interfaces depended on the changes of the short-range van-der-Waals force induced by the cation exchange (AlOH-Ca + AAs) and long-range electrostatic interaction affected by the hydrophilic interaction (AlOH-$\mathrm{H}_{2} \mathrm{O}$ + AAs).

To better understand the adsorption kinetics of AAs onto clay minerals in soils and sediments, further investigation will be focused on the effects of pH and temperature on the interlayer interaction of the Mt. + AAs system via Car-Parrinello Molecular Dynamics. This work, however, provides useful information on how to determine the quantitative orbital coupling of the Mt. + AAs. This is important, not only from a theoretical point of view since it can also advance the practical understanding of the dynamic evolution process of AAs with clay mineral surfaces.

## Declaration of Competing Interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments
National Natural Science Foundation of China (41872039 and 41831285), the One-Thousand-Talents Scheme in Sichuan Province, Sichuan Science and Technology Program (2018JY0462), and Longshan Fund of Southwest University of Science and Technology (17QR004).

## Appendix A. Supplementary data
Supplementary data to this article can be found online at https://doi.org/10.1016/j.clay.2019.105356.

## References
Arora, A.K., Jaswal, V.S., Singh, K., Singh, R., 2016. Chemical evolution and origin of life: a review. Chem. Biol. Lett. 3 (1), 9-17.

Berghout, A., Tunega, D., Zaoui, A., 2008. Density Functional Theory (DFT) study of the Hydration steps of $\mathrm{Na}^{+}/\mathrm{Mg}^{2+}/\mathrm{Ca}^{2+}/\mathrm{Sr}^{2+}/\mathrm{Ba}^{2+}$-exchanged Montmorillonites. Clay Clay Miner. 58, 174-187.

Bian, L., Dong, F.Q., Song, M.X., Dong, H.L., Li, W.M., Duan, T., Xu, J.B., Zhang, X.Y., 2015a. DFT and two-dimensional correlation analysis methods for evaluating the $\mathrm{Pu}^{3+}$-$\mathrm{Pu}^{4+}$ electronic transition of plutonium-doped zircon. J. Hazard. Mater. 294 (8), 47-56.

Bian, L., Song, M.X., Dong, F.Q., Duan, T., Xu, J.B., Li, W.M., Zhang, X.Y., 2015b. DFT and two-dimensional correlation analysis for evaluating the oxygen defect mechanism of low-density 4f (or 5f) elements interacting with Ca-Mt. RSC Adv. 5 (36), 28601-28610.

Bian, L., Xu, J.B., Song, M.X., Dong, F.Q., Dong, H.L., Shi, F.N., Zhang, X.Y., Duan, T., 2015c. First principles simulation of temperature dependent electronic transition of FM-AFM phase BFO. J. Mol. Model. 21 (4), 91.

Bu, H.L., Yuan, P., Liu, H.M., Liu, D., Liu, J.Z., He, H.P., Zhou, J.M., Song, H.Z., Li, Z.H., 2017. Effects of complexation between organic matter (OM) and clay mineral on OM pyrolysis. Geochim. Cosmochim. Ac. 212, 1-15.

Bu, H.L., Yuan, P., Liu, H.M., Liu, D., H, Z., Qin, Zhong, M, X., Song, H.Z., Li, Y., 2019. Formation of macromolecules with peptide bonds via the thermal evolution of amino acids in the presence of montmorillonite: insight into prebiotic geochemistry on the early Earth. Chem. Geol. 510, 72-83.

Cuadros, J., Aldega, L., Vetterlein, J., Drickamer, K., Dubbin, W., 2009. Reactions of lysine with montmorillonite at $80^{\circ} \mathrm{c}$ : implications for optical activity, $\mathrm{h}^{+}$transfer and lysine- montmorillonite binding. J. Colloid Interface Sci. 333 (1), 78-84.

Ding, X.L., Henrichs, S.M., 2002. Adsorption and desorption of proteins and polyamino acids by clay minerals and marine sediments. Mar. Chem. 77, 225-237.

Dong, F.Q., Guo, Y.T., Liu, M.X., Zhou, L., Zhou, Q., Li, H.L., 2018. Spectroscopic evidence and molecular simulation investigation of the bonding interaction between lysine and montmorillonite: implications for the distribution of soil organic nitrogen. Appl. Clay Sci. 159, 3-9.

Farias, A.P.S.F., Tadayozi, Y.S., Carneiro, Cristine E.A., Zaia, Dimas A.M., 2014. Salinity and pH affect $\mathrm{Na}^{+}$-montmorillonite dissolution and amino acid adsorption: a prebiotic chemistry study. Int. J. Astrobiol. 13, 259-270.

Fonseca, C.G., Vaiss, V.S., Wypych, F., Diniz, R., Leitão, A.A., 2018. Investigation of the initial stages of the montmorillonite acid-activation process using DFT calculations. Appl. Clay Sci. 165, 170-178.

Friebele, E., Shimoyama, A., Ponnamperuma, C., 1980. Adsorption of Protein and Non-Protein Amino Acids on a Clay Mineral: a possible Role of selection in Chemical Evolution. J. Mol. Evol. 16, 269-278.

Gu, C., Liu, C., Johnston, C.T., Teppen, B.J., Li, H., Boyd, S.A., 2011. Pentachlorophenol radical cations generated on Fe(III)-montmorillonite initiate octachlorodibenzo-p-dioxin formation in clays: density functional theory and fourier transform infrared studies. Environ. Sci. Technol. 45 (4), 1399-1406.

Hedges, J.I., Hare, P.E., 1987. Amino Acid Adsorption by clay minerals in distilled water. Geochim. Cosmochim. Ac. 51, 255-259.

Ho, P.H., Mihaylov, T., Pierloot, K., Parac-Vogt, T.N., 2012. Hydrolytic activity of vanadate toward serine-containing peptides studied by kinetic experiments and DFT theory. Inorg. Chem. 51 (16), 8848-8859.

Jaber, M., Georgelin, T., Bazzi, H., Costa-Torro, F., Lambert, J.F., Bolbach, G., Clodic, G., 2014. Selectivities in Adsorption and Peptidic Condensation in the (Arginine and Glutamic Acid)/ Montmorillonite clay system. J. Phys. Chem. C 118, 25447-25455.

Joshi, P.C., Aldersley, M.F., 2013. Significance of mineral salts in Prebiotic RNA Synthesis Catalyzed by Montmorillonite. J. Mol. Evol. 76, 371-379.

Kalra, S., Pant, C.K., Pathak, H.D., Mehta, M.S., 2000. Adsorption of glycine and alanine on montmorillonite with or without coordinated divalent cations. Indian J. Biochem. Biophys. 37, 341-346.

Katti, D.R., Ghosh, P., Schmmidt, S., Katti, K.S., 2005. Mechanical properties of the sodium montmorillonite interlayer intercalated with amino acids. Biomacromolecules 6, 3276-3282.

Khoury, G.A., Gehris, T.C., Tribe, L., Sánchez, R.M.T., Afonso, M.S., 2010. Glyphosate adsorption on montmorillonite: an experimental and theoretical study of surface complexes. Appl. Clay Sci. 50, 167-175.

Kitadai, N., Yokoyama, T., Nakashima, S., 2009. In situ, ATR-IR investigation of L-lysine adsorption on montmorillonite. J. Colloid Interface Sci. 338 (2), 395-401.

Laby, Ralph-Henry, 1962. The adsorption of amino-acids and peptides by montmorillonite and illite. University of Adelaide, Adelaide, Australia.

Lambert, J.F., 2008. Adsorption and polymerization of amino acids on mineral surfaces: a review. Orig. Life Evol. Biosph. 38, 211-242.

Mignon, P., Sodupe, M., 2012. Theoretical study of the adsorption of DNA bases on the acidic external surface of montmorillonite. Phys. Chem. Chem. Phys. 14, 945-954.

Mignon, P., Ugliengo, P., Sodupe, M., 2009. Theoretical study of the adsorption of RNA/

DNA bases on the external surfaces of $Na^{+}$-Montmorillonite. J. Phys. Chem. C 113, 13741-13749.

Newman, S.P., Cristina, T.D., Coveney, P.V., 2002. Molecular dynamics simulation of Cationic and Anionic Clays containing Amino Acids. Langmuir 18, 2933-2939.

Pagel-Wieder, Sibylle, Niemeyer, Jürgen, Fischer, Walter R., Gessler, Frank, 2007. Effects of physical and chemical properties of soils on adsorption of the insecticidal protein (Cry1Ab) from Bacillus thuringiensis at Cry1Ab protein concentrations relevant for experimental field sites. Soil Biol. Biochem. 39, 3034-3042.

Parolo, M.E., Avena, M.J., Pettinari, G.R., Baschini, M.T., 2012. Influence of $Ca^{2+}$, on tetracycline adsorption on montmorillonite. J. Colloid Interface Sci. 368 (1), 420-426.

Polubesova, T., Eldad, S., Chefetz, B., 2010. Adsorption and Oxidative transformation of Phenolic Acids by Fe(III)-Montmorillonite. Environ. Sci. Technol. 44, 4203-4209.

Ramos, M.E., Javier Huertas, F., 2013. Adsorption of glycine on montmorillonite in aqueous solutions. Appl. Clay Sci. 80-81, 10-17.

Roa-Escamilla, E., Huertas, F.J., Hernández, L.A., Sainz-Diaz, C.I., 2017. A DFT study of the adsorption of glycine in the interlayer space of montmorillonite. Phys. Chem. Chem. Phys. 19 (23), 14961.

Shaker, A.M., Komy, Z.R., Heggy, S.E.M., El-Sayed, M.E.A., 2012. Kinetic study for adsorption humic acid on soil minerals. J. Phys. Chem. A 116, 10889-10896.

Shi, J., Liu, H.B., Lou, Z.Y., Zhang, Y., Meng, Y.F., Zeng, Q., Yang, N.Y., 2013. Effect of interlayer counterions on the structures of dry montmorillonites with $Si^{4+}$/$Al^{3+}$ substitution. Comput. Mater. Sci. 69 (1), 95-99.

Suter, J.L., Sprik, M., Boek, E.S., 2012. Free energies of absorption of alkali ions onto beidellite and montmorillonite surfaces from constrained molecular dynamics simulations. Geochim. Cosmochim. Ac. 91 (91), 109-119.

Swadling, J.B., Suter, J.L., Greenwell, H.C., Coveney, P.V., 2013. Influence of surface chemistry and charge on Mineral-RNA interactions. Langmuir 29, 1573-1583.

Tran, A.T.T., James, B.J., 2012. A study the interaction forces between the bovine serum albumin protein and montmorillonite surface. Colloids and Surfaces A: Physico-chemical and Engineering Aspects 414, 104-114.

Wang, X.C., Lee, C., 1993. Adsorption and desorption of aliphatic amines, amino acids and acetate by clay minerals and marine sediments. Mar. Chem. 44, 1-23.

Yu, C.H., Norman, M.A., Newton, S.Q., Miller, D.M., Teppen, B.J., Schafer, L., 2000. Molecular dynamics simulations of the adsorption of proteins on clay mineral surfaces. J. Mol. Struct. 556, 95-103.

Yu, W.H., Li, N., Tong, D.S.C., Zhou, H.C., Lin, X., Xu, C.Y., 2013. Adsorption of proteins and nucleic acids on clay minerals and their interactions: a review. Appl. Clay Sci. 80-81 (4), 443-452.

Yuan, P., Liu, H.M., Liu, D., Tan, D.Y., Yan, W.C., He, H.P., 2013. Role of the interlayer space of montmorillonite in hydrocarbon generation: an experimental study based on high temperature- pressure pyrolysis. Appl. Clay Sci. 75, 82-91.

Zaia, D.A.M., 2004. A review of adsorption of amino acids on minerals: was it important for origin of life. Amino Acids 27 (1), 113-118.

Zaia, D.A.M., Zaia, C.T.B.V., Santana, H.D., 2008. Which amino acids should be used in prebiotic chemistry studies? Origins. Life. Evol. B 38 (6), 469-488.

Zhang, B., Kang, J.T., Kang, T.H., 2018a. Monte Carlo and molecular dynamic simulations of $CH_4$ diffusion in kaolinite as functions of pressure and temperature. J. Nat. Gas. Sci. Eng. 54, 65-71.

Zhang, B., Kang, J.T., Kang, T.H., 2018b. Effect of water on methane adsorption on the kaolinite (001) surface based on molecular simulations. Appl. Clay Sci. 439, 792-800.

Zhao, Q., Burns, S.E., 2012. Microstructure of single chain quaternary ammonium cations intercalated into montmorillonite: a molecular dynamics study. Langmuir. 28 (47), 16393-16400.