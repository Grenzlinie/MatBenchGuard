![](./images/814677935238676481_1.jpg)

On the dependence of effective mechanical properties of ceramics on partial concentrations of different size pores in its structure

Igor S. Konovalenko, Alexey Yu. Smolin, Ivan S. Konovalenko, Vladimir V. Promakhov, and Sergey G. Psakhie

Citation: AIP Conference Proceedings 1623, 287 (2014); doi: 10.1063/1.4898938

View online: http://dx.doi.org/10.1063/1.4898938

View Table of Contents: http://scitation.aip.org/content/aip/proceeding/aipcp/1623?ver=pdfcov

Published by the AIP Publishing

Articles you may be interested in
3D modeling of the mechanical behavior of ceramics with pores of different size
AIP Conf. Proc. 1623, 591 (2014); 10.1063/1.4899014

Mechanical properties of ultralow-dielectric-constant mesoporous amorphous silica structures: Effects of pore morphology and loading mode
Appl. Phys. Lett. 98, 121902 (2011); 10.1063/1.3567537

Experimental investigation on pore size effect on the linear viscoelastic properties of acoustic foams
J. Acoust. Soc. Am. 126, EL93 (2009); 10.1121/1.3186799

Size-dependent mechanical properties of molybdenum nanopillars
Appl. Phys. Lett. 93, 101916 (2008); 10.1063/1.2979684

Evidence for size-dependent mechanical properties from simulations of nanoscopic polymeric structures
J. Chem. Phys. 116, 9939 (2002); 10.1063/1.1476315

# On the Dependence of Effective Mechanical Properties of Ceramics on Partial Concentrations of Different Size Pores in its Structure

Igor S. Konovalenko $^{1, a)}$, Alexey Yu. Smolin $^{1,2}$, Ivan S. Konovalenko $^{1}$, Vladimir V. Promakhov $^{1,2}$, and Sergey G. Psakhie $^{1,3}$

$^{1}$ Institute of Strength Physics and Materials Science SB RAS, Tomsk, 634055, Russia
$^{2}$ National Research Tomsk State University, Tomsk, 634050, Russia,
$^{3}$ Institute of High Technology Physics, National Research Tomsk Polytechnic University, Tomsk, 634050, Russia

$^{a)}$ Corresponding author: igkon@ispms.tsc.ru

Abstract. In the framework of the movable cellular automata method we have developed a plane/2D model of mechanical behavior of brittle porous material under shear loading. The work considers the material characterized by a function of pore size distribution with two maxima. Based on simulation results, the authors proposed the analytical estimation of the dependence of strength and elastic properties of the material on its total porosity and partial porosities that correspond to the pores with different sizes.

Keywords: numerical simulation, movable cellular automata method, strength and elastic properties, ceramics

## INTRODUCTION

Ceramics based on nanocrystalline metal oxides are widely used for the manufacture of critical parts in many industries [1–4]. It is well known that such ceramics are characterized by a complex pore structure. Usually the pore size distribution of the said materials has several maxima. In the simplest case, there are two maxima. The height and the width of each maximum determines the pore volume fraction that corresponds to pores with the relevant size. Thus, even the ceramics with the bimodal pore size distribution and the certain total porosity value can be characterized by a great number of combinations of the pore structure parameters: correlation of the pore space volumes that correspond to the pores of the first and the second maxima of the distribution. From this point of view, ceramics is no longer just a porous material, but some construction having its mechanical behavior and properties determined by the aforementioned parameters of its structure [3–5]. In practice, the combination of pore structure parameters and mechanical properties of the material largely determine the scope of its functional application. In this connection, studying the mechanical properties of the ceramics in the entire range of its pore structure parameters is of great relevance and demand [1–4]. Therefore, the goal of this paper is the numerical study of the dependence of strength and elastic properties of ceramic materials on the pore volume fraction that corresponds to the pores of the second maximum of the pore size distribution regarding the total porosity of material. The calculations were carried out using a model material having the mechanical properties equivalent to those of nanocrystalline $ZrO_{2}(Y_{2}O_{3})$ (yttria-stabilized zirconia) with the average pore size greater than the average grain size and with bimodal pore size distribution [2–4]. Numerical investigations were conducted on the basis of multilevel approach developed within the framework of the movable cellular automaton method [6–8].

International Conference on Physical Mesomechanics of Multilevel Systems 2014
AIP Conf. Proc. 1623, 287-290 (2014); doi: 10.1063/1.4898938
© 2014 AIP Publishing LLC 978-0-7354-1260-6/$30.00

![](./images/814677935238676481_2.jpg)

**FIGURE 1.** Initial structures of specimens with different values of total porosity $C_{\mathrm{t}}$ and partial porosities $C_{1}$ and $C_{2}$

# MODEL CONSTRUCTION AT MESOSCALE

At the mesoscale, a modeling of the behavior of three groups of porous ceramics specimens under simple shear was performed. The total porosity of the specimens $C_{\mathrm{t}}$ in each group was equal to 0.075, 0.15 and 0.223, respectively. We studied plane square specimens with the side $h$ of $60\ \mathrm{\mu m}$. Each group consisted of several subgroups. Samples of each subgroup were characterized by a unique (within a group) number of pores for the first and the second maximum of the pore size distribution and their corresponding partial porosity values $C_{1}$ and $C_{2}$. In addition, the porosity of all specimens in each subgroup (within one group) obeyed the following equality: $C_{1}+C_{2}=C_{\mathrm{t}}$, i.e. $0\leq C_{1}\leq C_{\mathrm{t}}$ and $0\leq C_{2}\leq C_{\mathrm{t}}$. Each subgroup consisted of nine specimens with the same value of $C_{1}$ and $C_{2}$ but different pore space distribution. It was assumed that all pores in the ceramic samples under investigation, as well as in the model material, were equiaxed, and that the pore size of the model material was equal to 1.2 and $3.6\ \mathrm{\mu m}$ according to two maxima in pore size distribution of ceramics [2-4]. The size of the movable cellular automata was $1.2\ \mathrm{\mu m}$. The pore structure of the specimens was shaped by random removal of certain automata (for pores corresponding to the first maximum of the distribution) and their six nearest neighbors (for the pores corresponding to the second maximum). Figure 1 demonstrates the initial structure of model specimens with different values of pore structure parameters $C_{1}$, $C_{2}$ and $C_{\mathrm{t}}$.

The shear loading was simulated by setting the equal horizontal velocity to all automata in the upper layer of a specimen, with the automata of the lower layer being rigidly fixed. At the initial stage, the velocity of automata of the upper layer sinusoidally increased from 0 to 0.5 m/s and then was assumed to be constant. Such scheme ensured the fast achievement of a quasi-steady loading mode and allowed the elimination of dynamic effects until the occurrence of the first failures. Duration of the loading increase depended on the size of the specimen and was estimated by preliminary calculations. All specimens had periodic boundary conditions set for their side surfaces. The problem was solved considering the plane strain conditions.

The response function of the automata was linear and corresponded to the loading diagram of nanocrystalline ceramics on the basis of zirconium dioxide with the porosity of 10% and the average pore size commeasurable to the grain size [2-4]. Shear modulus $G$, Poisson ratio $v$ and compression strength of the movable cellular automaton were equal to 32 GPa, 0.3 and 1750 MPa, respectively [2-4]. Inter-automaton bond rupture criterion used in the calculations was formulated as a threshold value for intensity of shear stresses.

Strength and elastic properties of each model specimen were characterized by their effective shear strength $(\tau_{i})$ and shear modulus $(G_{i})$. They were determined from the simulated "shear stress-shear angle" diagrams of the specimen and corresponded to its maximum specific force of resistance to loading and the slope angle of linear part of the diagram. Strength and elastic properties of the model ceramics ($\tau$ and $G$) for each combination of $C_{\mathrm{t}}$, $C_{2}$ were determined on the basis of characteristics $(\tau_{i}$ and $G_{i})$ of nine model specimens with the corresponding values of $C_{\mathrm{t}}$, $C_{2}$ (belonging to the same subgroup). The values of $\tau$ and $G$ were calculated as the arithmetic average of $\tau_{i}$ and $G_{i}$.

![](./images/814677935238676481_3.jpg)

FIGURE 2. Dependences of shear strength $\tau$ and shear modulus $G$ of porous specimens on parameter $C_{2}/C_{t}$, characterizing fraction of partial porosity $C_{2}$ in total porosity $C_{t}$ for the following values of $C_{t}$: 0.075, 0.15, and 0.223

# SIMULATION RESULTS

The results of simulation (Fig. 2) showed that the strength and the elastic properties of the model specimens depended on both the total porosity $C_{t}$ and the porosity fractions of corresponding to one of the pore size distribution maxima, e.g. $C_{2}/C_{t}$. The dependencies revealing the said trends for model specimens are shown in Fig. 2. Calculations were performed for the case of minimum, maximum and intermediate values of total porosity $C_{t}$.

One can see (Fig. 2(b)) that the shear modulus $G$ of the model specimens decreases with the increase of the parameter $C_{2}/C_{t}$. In the case of small values of the porosity $C_{t}$ this dependence is weak. For instance, the maximum difference in elastic properties of the specimens with $C_{t}=0.075$ and different values of $C_{2}/C_{t}$ did not exceed 0.6%. With increasing porosity $C_{t}$ the dependence $G=G(C_{2}/C_{t})$ becomes stronger. In particular, the difference in elastic properties of the samples with $C_{t}=0.223$ and various values of $C_{2}/C_{t}$ became equal to 9.2%. For strength properties, this difference reaches 30.4% (Fig. 2(a)). The obtained results are in good agreement with the experimental data [2-4].

Approximation of the simulation results (for several values of porosity $C_{t}$) using linear functions gave the analytical expression for its strength and elastic properties ($\tau$ and $G$, respectively) in the entire considered range of parameters $C_{t}$ and $C_{2}/C_{t}$:
$$
\tau_{\mathrm{c}}=-(49.7457 \ln C_{\mathrm{t}}+165.004)(C_{2} / C_{\mathrm{t}})+174.65(C_{\mathrm{t}})^{-0.3405}, \tag{1}
$$

$$
E=-(7.233 C_{\mathrm{t}}-0.384)(C_{2} / C_{\mathrm{t}})+32.729 e^{-3.673 C_{\mathrm{t}}}, \tag{2}
$$
where $C_{1}+C_{2}=C_{\mathrm{t}}, 0 \leq C_{1} \leq C_{\mathrm{t}}, 0 \leq C_{2} \leq C_{\mathrm{t}}, 0.075 \leq C_{\mathrm{t}} \leq 0.223$.

It should be noted that the model of ceramics developed herein is a multiparametric one. Namely, it is characterized by the following parameters: a) shape of the pores, b) their spatial orientation, c) pore size distribution, d) value of the total porosity. The validity of the proposed assessments is shown only for the case of two varying parameters $C_{2}$ and $C_{\mathrm{t}}$, and only for their considered value range. The choice of $C_{2}$, $C_{\mathrm{t}}$ and their range was stipulated by their importance for the investigation of mechanical properties of ceramics on the basis of numerical 2D models. In case of 3D models the range of porosity parameters can be wider. The additional investigations are required for finding the boundaries of the entire range of parameters, where the proposed dependencies are valid, as well as to take into account the influence of other parameters on the strength and elastic properties of ceramics.

# SUMMARY

Computer calculations performed and the analytical estimates obtained show that the strength and elastic properties of ceramics with a bimodal pore size distribution function are defined both by the value of its total porosity and partial porosities, corresponding to pores of different size. It is shown that difference in the effective strength and elastic properties of ceramics with the same value of total porosity but different values of partial porosities, can reach values of 44% and 9% respectively.

# ACKNOWLEDGEMENT

The investigation was partially funded by the Program for the Basic Research of State Academies of Sciences for 2013–2016 (project No. III.23.2.5), the Grant of the Russian Foundation for Basic Research (project No. 12-08-00379-a), the Grant of the President of the Russian Federation for the state support of young Russian scientists (project MK-5883.2014.8), Tomsk State University Competitiveness Improvement Program and the Federal Targeted Program "Scientific and Scientific-Pedagogical Personnel of the Innovative Russia for 2014–2020" (Governmental Contract No. 14.577.21.0007).

# REFERENCES

1.  J. Rödel, A. B.N. Kounga, M. Weissenberger-Eibl, D. Koch, A. Bierwisch, W. Rossner, M. J. Hoffmann, R. Danzer, and G. Schneider, J. Eur. Ceramic Soc. **29**, 1549 (2009).
2.  *Global Roadmap for Ceramics*, edited by A. Belosi and G. N. Babini (Institute of Science and Technology for Ceramics, National Research Council, Verona, 2008).
3.  *Ceramic Matrix Composites. Fiber Reinforced Ceramics and their Applications*, edited by Krenkel and Walter (Wiley-VCH, Weinheim, 2008).
4.  S. P. Bujakova, Properties, Structure, Phase Composition and Patterns of Formation of Porous Nanosystems Based on $ZrO_2$, Doc. Eng. Sci. Diss., ISPMS SB RAS, Tomsk, 2008.
5.  A. Yu. Smolin, Ig. S. Konovalenko, S. N. Kul'kov, and S. G. Psakhie, Tech. Phys. Lett. **32**(9), 738 (2006).
6.  S. G. Psakhie, E. V. Shilko, A. Yu. Smolin, and S. V. Astafurov, Fract. Int. Struct. **24**, 26 (2013).
7.  S. G. Psakhie, E. V. Shilko, A. Yu. Smolin, A. V. Dimaki, A. I. Dmitriev, Ig. S. Konovalenko, S. V. Astafurov, and S. Zavshek, Phys. Mesomech. **14**(5–6), 224 (2011).
8.  Ig. S. Konovalenko, A. Yu. Smolin, and S. G. Psakhie, Fract. Int. Struct. **24**, 75 (2013).
290