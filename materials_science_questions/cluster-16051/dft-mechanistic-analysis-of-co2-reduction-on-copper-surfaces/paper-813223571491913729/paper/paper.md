# Electroreduction of Methanediol on Copper

Heine A. Hansen · Joseph H. Montoya ·
Yin-Jia Zhang · Chuan Shi · Andrew A. Peterson ·
Jens K. Nørskov

Received: 5 March 2013 / Accepted: 7 May 2013 / Published online: 24 May 2013
© Springer Science+Business Media New York 2013

## Abstract
We have used density functional theory calculations to study intermediates in the electroreduction of methanediol on copper. We find that methanediol, which is the hydrated form of formaldehyde, may be reduced to methanol with a limiting potential close to the experimental onset for reduction of aqueous formaldehyde.

## Keywords
Carbon dioxide · DFT · Electrocatalysis ·
Reaction intermediates

The electroreduction of $CO_2$ has received great interest recently, as it could provide a sustainable route to carbon-based energy carriers and feedstocks for the chemical industry [1]. For this reaction, copper stands out as a unique electrocatalyst that exhibits a high Faradaic yield of hydrocarbons and alcohols, although high overpotentials close to 1 V are required to drive the reaction [2]. The electrochemistry of $CO_2$ reduction on copper is rich and at least 16 different products, including $CO$, $CH_4$, $C_2H_4$ and $CH_3CH_2OH$ have been experimentally observed [3].

It is generally accepted that the reduction of $CO_2$ to methane and hydrocarbons proceeds through a carbon monoxide intermediate, because the reduction of CO leads to a similar product distribution as the reduction of $CO_2$ [4]. Several different pathways have been suggested in the reduction of CO to $CH_4$. Some authors have suggested that the C–O bond is broken early in the reaction path resulting in $CH_n$ adsorbates which are hydrogenated further to $CH_4$ [5–8]. Others have suggested, based on a transfer coefficient analysis, that the rate-determining step for CO reduction to $CH_4$ is the second electron transfer [8]. A theoretical analysis based on density functional theory (DFT) calculations of the energy of the intermediates in CO reduction has suggested that the lowest free energy pathway from CO to $CH_4$ proceeds through the adsorbed intermediates $CHO$, $CH_2O$ and $OCH_3$ before the C–O bond is broken [9, 10]. If the lowest free energy pathway is followed then this also leads to methane rather than methanol being the predominant product in the last hydrogenation step, in agreement with experiment [5]. This pathway is in apparent contradiction to experiments showing that formaldehyde, which is an intermediate in the lowest free energy pathway, is reduced to methanol in addition to methane [5, 8].

We see several possible explanations for this apparent contradiction. One possibility is the free energy pathways to methane and methanol are affected by the presence of adsorbate species. These adsorbates may be different during the reduction of $CO(CO_2)$ and formaldehyde. Another possibility, which we investigate in this Letter, is that methanol is formed by the reduction of methanediol rather than formaldehyde. We show that the different product

---

Electronic supplementary material The online version of this article (doi:10.1007/s10562-013-1023-5) contains supplementary material, which is available to authorized users.

H. A. Hansen · J. H. Montoya · C. Shi ·
A. A. Peterson · J. K. Nørskov (⊗)
SUNCAT Center for Interface Science and Catalysis,
Department of Chemical Engineering, Stanford University,
Stanford, CA 94305, USA
e-mail: norskov@stanford.edu

H. A. Hansen · J. H. Montoya · C. Shi ·
A. A. Peterson · J. K. Nørskov
SLAC National Accelerator Laboratory, 2575 Sand Hill Road,
Menlo Park, CA 94025, USA

Y.-J. Zhang · A. A. Peterson
School of Engineering, Brown University, Providence,
RI 02912, USA

![](./images/813223571491913729_1.jpg)

distribution in the reduction of $CO(CO_2)$ and formaldehyde is not in disagreement with the lowest free energy pathway if one realizes that formaldehyde as a reactant in aqueous solution is largely in the form of methanediol [11].

We construct free energy diagrams from DFT calculations employing the computational hydrogen electrode (CHE) model [12]. In this CHE methodology, a free energy diagram is initially produced for the corresponding chemical process where proton and electron pairs are replaced by $1/2\ H_2$ at standard conditions. Here we can include solvation effects and the effect of electrical fields present at the solid-electrolyte interface. By definition, this free energy diagram corresponds to the electrochemical free energy diagram at a potential of 0 V versus the reversible hydrogen electrode (RHE). The free energy diagram at an arbitrary potential, $U$ (vs. the RHE), may be constructed by shifting the energy levels by the amount $-neU$, where $e$ is the elementary charge and $n$ is the number of electrons transferred to the respective intermediate. If protons, water and hydroxide are at equilibrium at the interface, the free energy diagram is unaffected by whether the proton donor is $H_3O^+$ or $H_2O$ when the potential is calculated on the RHE scale [13].

As the potential is made more negative (more reducing), the thermodynamic driving force for reduction is increased. The last step to become exergonic as the overpotential is increased is known as the potential-limiting step and the potential where this happens is referred to as the "limiting potential", $U_L$. It has been found that variations in the limiting potential capture measured trends in electrocatalytic activity (exchange current densities and overpotentials) of different materials for oxygen evolution [14], hydrogen evolution [15] and oxygen $2e^-$ and $4e^-$ reduction [16] and for $CO/CO_2$ reduction [17]. It has also been found to explain trends in onset potential for the formation of various products $H_2, HCOOH, CO, CH_4$ on copper surfaces [10, 18].

The observation that the trends in catalytic activity and selectivity can be understood to a large extend by looking at the free energy diagram of the intermediates mirrors a similar observation in heterogeneous catalysis [19]. An analysis including only the free energy of intermediates and not the activation energies separating them is of course not complete; large variations in activation energies can change the reaction pathway. The fact that it seems to hold in a number of cases is most likely related to two important factors about potential energy diagrams for surface chemical reactions. The first is that having a smooth and downhill variation in the free energy along the reaction pathway is a necessary condition to a high rate on any material. If there are large increases of the free energy along a pathway, such a free energy increase will enter directly into the activation energy and will, in itself, make the rate small. One can say that a smooth free energy pathway is a necessary but not sufficient criterion for a good activity (or selectivity). Second, activation energies and reaction energies are generally found to be strongly correlated in so-called Brønsted-Evans-Polayni (BEP) relations [20]. These relations suggest that the more exothermic a reaction step is, the smaller the barrier. This also means that trends in the energy of intermediates determine trends in reactivity. We note that the observation that electrochemical reaction rates obtain values corresponding to a current density in the range $0.1-1\ mA/cm^2$ when the potential is close to the limiting potential suggest that activation free energies at the potential where the reaction has zero free energy change must be of the order 0.7 eV. The origin of this barrier is very far from clear, but it appears to be ubiquitous for the reactions above.

The DFT calculations in this letter are performed using the dacapo electronic structure code and the atomic simulation environment (ASE) [21]. The ionic cores are described using Vanderbilt ultrasoft pseudo potentials [22], the Kohn-Sham one-electron states are expanded in plane waves with a kinetic energy cutoff of 340.15 eV, and the density is described using plane waves with a cutoff corresponding to 500 eV. The effects of exchange and correlation are described using the RPBE functional [23], which typically gives a better description of chemisorption energies than other GGA functionals such as PBE. The free energy of methanediol is calculated relative to $CO_2$ from experimental values [24, 25] in order to avoid the computational difficulties associated with solvation free energies. Further details are given in the supplementary material.

The free energy diagram for $CO_2$ reduction to $CH_4$ on Cu(211) at 0 V versus RHE is shown in Fig. 1, based on free energies from [17]. A stepped Cu surface is chosen here since it has been found to give the lowest free energy path [10], and may be taken to represent the active sites for $CO_2$ reduction of a polycrystalline surface [18]. The reduction of $CO_2$ proceeds through the following intermediates $COOH^*, CO^*, CHO^*, CH_2O^*, OCH_3^*, O^*$, and $OH^*$.

In this pathway, the carbon atom in CO is hydrogenated 4 times to produce $CH_4$ by following the lowest free energy pathway. The intermediates in alternate pathways involving a hydrogenated oxygen are also shown for comparison. It is 0.76 eV more favorable to form $CHO^*$ than $COH^*$, 0.27 eV more favorable to form $CH_2O^*$ than $CHOH^*$, and 0.59 eV more favorable to form $OCH_3^*$ than $CH_2OH^*$. $OCH_3^*$ may then be protonated to give either $CH_4 + O^*$ or $CH_3OH$. The path to $CH_4 + O^*$ is more exergonic than the path to $CH_3OH$, consistent with the observed selectivity towards $CH_4$ rather than $CH_3OH$ on Cu [9].

Formaldehyde is hydrated in aqueous solution to produce methanediol

![](./images/813223571491913729_2.jpg)

![](./images/813223571491913729_3.jpg)

Fig. 1 Free energy diagram at 0 V versus RHE for intermediates discussed in the reduction of CO₂ and methanediol on Cu(211)

$$\mathrm{CH}_{2} \mathrm{O}+\mathrm{H}_{2} \mathrm{O} \leftrightarrow \mathrm{H}_{2} \mathrm{C}(\mathrm{OH})_{2}$$

with an equilibrium constant reported around $2 \times 10^{3}$ [11,
26]. The $\mathrm{p}K_{\mathrm{a}}$ of methanediol is suggested to be in the range
13.05–13.55 [27], so methanediol is only deprotonated in
strongly alkaline solutions.

A free energy diagram for the reduction of methanediol
is also shown in Fig. 1. Methanediol is most likely pro-
tonated at an oxygen atom, because the carbon atom
already has four bonds

$$\begin{aligned}
*+\mathrm{H}_{2} \mathrm{C}(\mathrm{OH})_{2}+\mathrm{H}^{+}+\mathrm{e}^{-} & \rightarrow \mathrm{CH}_{2} \mathrm{OH}^{*}+\mathrm{H}_{2} \mathrm{O}, \\
\mathrm{U}_{\mathrm{L}}= & -0.33 \mathrm{~V}.
\end{aligned}$$

$\mathrm{CH}_{2} \mathrm{OH}^{*}$ could be further protonated at either the
oxygen atom

$$\mathrm{CH}_{2} \mathrm{OH}^{*}+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{CH}_{2}{ }^{*}+\mathrm{H}_{2} \mathrm{O},$$

or the carbon atom

$$\mathrm{CH}_{2} \mathrm{OH}^{*}+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow *+\mathrm{CH}_{3} \mathrm{OH}.$$

As shown in the free energy diagram, protonation
of the carbon atom leading to methanol is favored
thermodynamically over protonation of the oxygen atom,
so we expect that the selectivity for methanol is higher than
the selectivity for $\mathrm{CH}_{2}{ }^{*}$. $\mathrm{CH}_{2}{ }^{*}$ could potentially lead to
$\mathrm{CH}_{4}$ or $\mathrm{C}_{2} \mathrm{H}_{4}$, as we will discuss in more detail below.

An alternative pathway in the first protonation step of
methanediol initiates with the protonation of the carbon
atom. This would likely be coupled to the breaking of a
C–O bond in order to avoid a carbon atom with five bonds

$$*+\mathrm{H}_{2} \mathrm{C}(\mathrm{OH})_{2}+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{CH}_{3} \mathrm{OH}+\mathrm{OH}^{*},$$

although this might not be an elementary step. In this
pathway the limiting potential would be determined by OH
removal

$$\mathrm{OH}^{*}+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow *+\mathrm{H}_{2} \mathrm{O}, \quad \mathrm{U}_{\mathrm{L}}=-0.31 \mathrm{eV}.$$

A third possibility is direct dissociation of methanediol
on the step

$$2 *+\mathrm{H}_{2} \mathrm{C}(\mathrm{OH})_{2} \rightarrow \mathrm{CH}_{2} \mathrm{OH}^{*}+\mathrm{OH}^{*}, \Delta \mathrm{G}=-0.02 \mathrm{eV},$$

followed by reduction of $\mathrm{CH}_{2} \mathrm{OH}^{*}$ and $\mathrm{OH}^{*}$ to $\mathrm{CH}_{3} \mathrm{OH}$ and
$\mathrm{H}_{2} \mathrm{O}$ respectively. The pathways above yield $\mathrm{CH}_{3} \mathrm{OH}$ with
a limiting potential of $-0.33$ or $-0.31\ \mathrm{V}$ related to the
formation of $\mathrm{CH}_{2} \mathrm{OH}^{*}$ or removal of $\mathrm{OH}^{*}$ respectively.
Free energy diagrams comparing the different pathways are
shown in Figure S2 in the supplementary material.

The reduction of methanediol is summarized in Fig. 2a
showing the potential free energy diagram at a limiting
potential of $-0.33\ \mathrm{V}$. The selectivity for $\mathrm{CH}_{3} \mathrm{OH}$ is con-
sistent with a pathway consisting of consecutive interme-
diates related by single proton-electron transfer steps
coupled with bond dissociation when a stable molecule
such as $\mathrm{H}_{2} \mathrm{O}$ or $\mathrm{CH}_{4}$ is produced. If more than one inter-
mediate is available, the one with the lowest free energy is
preferred.

The selectivity for $\mathrm{CH}_{4}$ in reduction of $\mathrm{CO}_{2}$ and $\mathrm{CO}$ may
be understood in a similar way. Figure 2b shows the
potential energy diagram for CO reduction at the limiting
potential for reduction of CO to CHO ($U_L=0.7$ eV)
where CO reduction becomes exergonic. At this potential,
CHO* reduction to $\mathrm{CH}_{2} \mathrm{O}^{*}$ is highly exergonic. We con-
sider the direct formation of $\mathrm{H}_{2} \mathrm{C}(\mathrm{OH})_{2}$ from protons, water
and CHO* to be unlikely as it would require the formation
of several bonds simultaneously. $\mathrm{CH}_{2} \mathrm{O}^{*}$ can then either be
reduced to $\mathrm{OCH}_{3}{ }^{*}$ or be hydrated to form $\mathrm{H}_{2} \mathrm{C}(\mathrm{OH})_{2}$. At
this potential, formation of $\mathrm{OCH}_{3}{ }^{*}$ is thermodynamically
favored and we hypothesize it therefore is the kinetically
favored pathway. At $-0.74\ \mathrm{V}$ versus RHE the equilibrium
pressure of desorbing $\mathrm{CH}_{2} \mathrm{O}$ that would be $2 \times 10^{-13}\ \mathrm{Pa}$
[9]. From $\mathrm{OCH}_{3}{ }^{*}$ the formation of $\mathrm{CH}_{4}$ is then kinetically
favored over $\mathrm{CH}_{3} \mathrm{OH}$.

Figure 3 shows a free energy diagram for hydrogenation
of $\mathrm{CH}_{2}{ }^{*}$ to $\mathrm{CH}_{4}$ and the association of two $\mathrm{CH}_{2}{ }^{*}$ to form
$\mathrm{C}_{2} \mathrm{H}_{4}$. The hydrogenation steps to $\mathrm{CH}_{4}$ is exergonic by
almost one 1 eV at 0 V versus RHE. However, we also find
that association of $\mathrm{CH}_{2}{ }^{*}$ may happen with a barrier of
0.54 eV on the (211) step, see Fig. S3 in the supplementary

![](./images/813223571491913729_4.jpg)

![](./images/813223571491913729_5.jpg)

Fig. 2 a Free energy diagram at -0.33 V versus RHE where reduction of methanediol to $\mathrm{CH}_{2} \mathrm{OH}^{*}$ becomes exergonic. b Free energy diagram at -0.7 V versus RHE, where reduction of $\mathrm{CO}^{*}$ to $\mathrm{CHO}^{*}$ is exergonic. At this potential, reduction of $\mathrm{CH}_{2} \mathrm{O}^{*}$ to $\mathrm{OCH}_{3}{ }^{*}$ is thermodynamically favored over the formation of $\mathrm{H}_{2} \mathrm{C}(\mathrm{OH})_{2}$ leading to high selectivity for $\mathrm{CH}_{4}$

![](./images/813223571491913729_6.jpg)

Fig. 3 Free energy diagram for $\mathrm{CH}_{2}{ }^{*}$ pathways to $\mathrm{CH}_{4}$ and $\mathrm{C}_{2} \mathrm{H}_{4}$ at $0 \mathrm{~V}$ versus RHE. $\mathrm{CH}_{2}{ }^{*}$ may be further hydrogenated to $\mathrm{CH}_{4}$ via proton coupled electron transfers, or two $\mathrm{CH}_{2}$ may associate in a chemical step to $\mathrm{C}_{2} \mathrm{H}_{4}$ with a 0.54 eV barrier

material. We therefore predict the formation of both $\mathrm{CH}_{4}$ and $\mathrm{C}_{2} \mathrm{H}_{4}$ are kinetically feasible from $\mathrm{CH}_{2}{ }^{*}$, with $\mathrm{CH}_{4}$ being kinetically preferred over $\mathrm{C}_{2} \mathrm{H}_{4}$ because $\mathrm{CH}_{2}$ hydrogenation is more exergonic than $\mathrm{CH}_{2}$ association.

The experimental onset for reduction of 0.05 M form- aldehyde to methanol is reported to be -0.3 V versus RHE based on online electrochemical mass spectrometry (OLEMS) [5], in agreement with our limiting potential of -0.31 to -0.33 V versus RHE related to either $\mathrm{OH}^{*}$ removal or $\mathrm{CH}_{2} \mathrm{OH}^{*}$ formation. The quantitative agree- ment at this level is fortuitous, because no current scale is related to the OLEMS signal and because we have assumed standard activity of methanediol, rather than the activity of a 0.05 M formaldehyde solution. Some methane is also reported as a product of formaldehyde reduction with a maximum around -0.5 V [5], while both $\mathrm{CH}_{4}$ and $\mathrm{C}_{2} \mathrm{H}_{4}$ has been reported at small Faradaic efficiencies of 0.7 and 0.1 %, respectively at -0.71 V versus RHE [8]. We note that the suggested reactivity of methanediol does not pre- clude the direct reaction of $\mathrm{CH}_{2} \mathrm{O}$ with the surface, as we note that $\mathrm{CH}_{2} \mathrm{O}$ and methanediol have identical chemical potentials in solution when in equilibrium. We speculate that the formation of methane and ethylene in these experiments [9, 28] could result from the reduction of the non-hydrated formaldehyde $\mathrm{CH}_{2} \mathrm{O}^{*}$ formed at a low cov erage, or possibly from a $\mathrm{CH}_{2}{ }^{*}$ intermediate as described above.

It has been observed that $\mathrm{CH}_{3} \mathrm{OH}$ is not further reduced to e.g. $\mathrm{CH}_{4}$ on $\mathrm{Cu}$ [5]. In alkaline solution $\mathrm{CH}_{3} \mathrm{OH}$ is deprotonated to $\mathrm{CH}_{3} \mathrm{O}^{-}$and it has been proposed $\mathrm{CH}_{3} \mathrm{O}^{-}$ should be reduced further to $\mathrm{CH}_{4}$ according to the CHE model for $\mathrm{CO}_{2}$ reduction on copper [5]. However, it is likely difficult to get the negatively charged $\mathrm{CH}_{3} \mathrm{O}^{-}$to adsorb on the copper electrode at negative potentials. Indeed, from Fig. 2a, it is seen the formation of $\mathrm{OCH}_{3}{ }^{*}$ from $\mathrm{CH}_{3} \mathrm{OH}$ is endothermic by 0.69 eV at -0.33 V versus RHE—the potential necessary to remove $\mathrm{OH}^{*}$ from the step and operate catalytically. The high endothermicity of $\mathrm{OCH}_{3}{ }^{*}$ formation from methanol may result in a very low prefactor for the reduction of methanol to methane. Since the potential energy surface is calculated versus the RHE, it is clear it is even more difficult to form $\mathrm{OCH}_{3}{ }^{*}$ from $\mathrm{CH}_{3} \mathrm{O}^{-}$at alkaline conditions were $\mathrm{CH}_{3} \mathrm{O}^{-}$is more stable than $\mathrm{CH}_{3} \mathrm{OH}$.

In summary, we have analyzed the electroreduction of methanediol on Cu(211) using the CHE model. We find that methanediol may be selectively reduced to methanol rather than methane. The limiting potential for methanediol reduction is found to be -0.31 to -0.33 V versus RHE and related to either removal of $\mathrm{OH}^{*}$ or formation of $\mathrm{CH}_{2} \mathrm{OH}^{*}$. The limiting potential matches well with the experimental onset for reduction of methanediol.

Because methanediol is formed by hydration of form- aldehyde in aqueous solution, the experimental observation that aqueous formaldehyde is reduced to methanol, does not necessarily contradict the suggestion that reduction of $\mathrm{CO}_{2}$ and $\mathrm{CO}$ proceeds through adsorbed formaldehyde to

form methane. The observed methanol may simply be formed through reduction of methanediol rather than reduction of adsorbed formaldehyde.

Acknowledgments This material is based on work supported by the Air Force Office of Scientific Research through the MURI program under AFOSR Award No. FA9550-10-1-0572 (H.A.H. and C.S.), by the Office of Naval Research under the Young Investigators Program, award N00014-12-1-0851 (A.A.P. and Y.Z.), and by the NSF GFRP (J.H.M.).

References

1. Finn C, Schnittger S, Yellowlees LJ, Love JB (2012) Chem Commun 48:1392
2. Hori Y (2008) Mod Aspects Electrochem 42:89
3. Kuhl KP, Cave E, Abram DN, Jaramillo TF (2012) Energy Environ Sci 5:7050
4. Hori Y, Murata A, Takahashi R (1989) J Chem Soc Faraday Trans 1(85):2309
5. Schouten KJP, Kwon Y, Van der Ham CJM, Qin Z, Koper MTM (2011) Chem Sci 2:1902
6. Gattrell M, Gupta N, Co A (2006) J Electroanal Chem 594:1
7. Kim JJ, Summers DP, Frese KW (1988) J Electroanal Chem Interfacial Electrochem 245:223
8. Hori Y, Takahashi R, Yoshinami Y, Murata A (1997) J Phys Chem B 101:7075
9. Peterson AA, Abild-Pedersen F, Studt F, Rossmeisl J, Nørskov JK (2010) Energy Environ Sci 3:1311
10. Durand WJ, Peterson AA, Studt F, Abild-Pedersen F, Nørskov JK (2011) Surf Sci 605:1354

11. Greenzaid P, Luz Z, Samuel D (1967) J Am Chem Soc 89:749
12. Nørskov JK, Rossmeisl J, Logadottir A, Lindqvist L, Kitchin JR, Bligaard T, Jónsson H (2004) J Phys Chem B 108:17886
13. Hansen HA, Rossmeisl J, Nørskov JK (2008) Phys Chem Chem Phys 10:3722
14. Man IC, Su H-Y, Calle-Vallejo F, Hansen HA, Martínez JI, I- noglu NG, Kitchin J, Jaramillo TF, Nørskov JK, Rossmeisl J (2011) ChemCatChem 3:1159
15. Nørskov JK, Bligaard T, Logadottir A, Kitchin JR, Chen JG, Pandelov S, Stimming U (2005) J Electrochem Soc 152:23
16. Viswanathan V, Hansen HA, Rossmeisl J, Nørskov JK (2012) J Phys Chem Lett 3:2948
17. Peterson AA, Nørskov JK (2012) J Phys Chem Lett 3:251
18. Tang W, Peterson AA, Varela AS, Jovanov ZP, Bech L, Durand WJ, Dahl S, Nørskov JK, Chorkendorff I (2012) Phys Chem Chem Phys 14:76
19. Jones G, Bligaard T, Abild-Pedersen F, Nørskov JK (2008) J Phys Condens Matter 20:064239
20. Koper MTM (2013) J Solid State Electrochem 17:339
21. Bahn SR, Jacobsen KW (2002) Comput Sci Eng 4:56
22. Vanderbilt D (1990) Phys Rev B 41:7892
23. Hammer B, Hansen L, Nørskov JK (1999) Phys Rev B 59:7413
24. Haynes WM, Bruno TJ, Lide DR (2013) CRC handbook of chemistry and physics, 93rd edn. CRC Press/Taylor and Francis, Boca Raton
25. Betterton EA, Hoffmann MR (1988) Environ Sci Technol 22:1415
26. Cluşaru A, Crişan I, Kůta J (1973) J Electroanal Chem Interfacial Electrochem 46:51
27. Norkus E, Pauliukaite R, Vaskelis A, Butkus E, Jusys Z, Kreneviciene M (1998) J Chem Res (S) 4:320
28. Montoya JH, Peterson AA, Nørskov JK (2013) ChemCatChem 5:737

![](./images/813223571491913729_7.jpg)