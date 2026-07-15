This article was downloaded by: [University of Southern Queensland]
On: 18 October 2014, At: 06:58
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](./images/812308713040773121_1.jpg)

# Molecular Physics: An International Journal at the Interface Between Chemistry and Physics
Publication details, including instructions for authors and subscription information:
http://www.tandfonline.com/loi/tmph20

## Multiplet splittings and other properties from density functional theory: an assessment in iron-porphyrin systems
Dayle M. A. Smith $^{a c}$ , Michel Dupuis $^{b}$ \& T. P. Straatsma $^{c}$

$^{a}$ Department of Physics, Whitman College Walla Walla, WA 99362 USA
$^{b}$ Molecular Interactions and Transformations, Chemical Sciences Division, WA 99352 USA
$^{c}$ Computational Biosciences, Biological Sciences Division Pacific Northwest National Laboratory Richland, WA 99352 USA
$^{d}$ Department of Physics, Whitman College Walla Walla, WA 99362 USA E-mail:
Published online: 21 Feb 2007.

To cite this article: Dayle M. A. Smith, Michel Dupuis & T. P. Straatsma (2005) Multiplet splittings and other properties from density functional theory: an assessment in iron-porphyrin systems, Molecular Physics: An International Journal at the Interface Between Chemistry and Physics, 103:2-3, 273-278, DOI: 10.1080/00268970512331317309

To link to this article: http://dx.doi.org/10.1080/00268970512331317309

---

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the "Content") contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

# Multiplet splittings and other properties from density functional theory: an assessment in iron–porphyrin systems

DAYLE M. A. SMITH†¶*, MICHEL DUPUIS‡ and T. P. STRAATSMA¶

†Department of Physics, Whitman College Walla Walla, WA 99362 USA
‡Molecular Interactions and Transformations, Chemical Sciences Division
¶Computational Biosciences, Biological Sciences Division Pacific Northwest National Laboratory Richland, WA 99352 USA

(Received July 2004, accepted 15 August 2004)

In transition metal compounds with spin states close in energy, the magnitude and sign of the energy splitting calculated with density functional theory depends strongly on the functional used. Therefore we must turn to additional criteria to assess the level of accuracy and reliability of predictions based on this level of theory. We report optimized geometries, total energies, and Mössbauer quadrupole splitting values for low-spin and high-spin, ferric and ferrous model hemes using a variety of gradient-corrected and hybrid functionals. In one model, the iron–porphyrin is axially ligated by two strong-field imidazole ligands [FeP(Im)₂] and has a low-spin ground state. In the other model complex the axial ligands are two weak-field, water molecules [FeP(H₂O)₂], and have a high-spin ground state. Among all the functionals used (UHF, B3LYP, B3LYP*, BLYP, half-and-half, LSDA), the B3LYP hybrid functional most consistently reproduced the experimental geometry, Mössbauer, and spin state data for the two model hemes. Simply gradient-corrected functionals exhibit strong biases towards low spin states, while Hartree–Fock favours strongly high spin states. These findings suggest that for systems with similar characteristics of several accessible electronic spin configurations, it is imperative to include properties other than just the energy in the assessment of the DFT predictions.

## 1. Introduction

In heme proteins, at least one iron–porphyrin complex is present and is involved in the activity of the biological system. Examples include oxygen transport agents such as hemoglobin, metabolizing enzymes such as peroxidases, and electron transfer agents such as cytochromes [1]. The functions of heme proteins are modulated by the oxidation state of the iron, and the spin multiplicity of the ground and low-lying excited states. For instance, oxygen transport heme proteins function only in a ferrous state, switching between high- and low-spin ground states, and electron transfer agents function by reversible oxidation/reduction of the ferric–ferrous state [2]. Much of the biological activity centres on the heme unit, and even more specifically, on the 3d-orbitals of the central iron atom in the complex.

The preferred multiplicity of hemes is determined by the nature of the iron’s axial ligands, and results from the competition between ligand field splitting and spin pairing energy. Ferrous iron has six electrons in its 3d shell, which can adopt a low-spin configuration ($S=0$), intermediate-spin configuration, or a high-spin configuration ($S=2$), which follows Hund’s rule. Similarly, ferric iron’s five 3d electrons can adopt $S=1/2$, $S=3/2$ or $S=5/2$ configurations. Weak-field ligands (such as water) yield a small ligand field splitting, so the electron pairing energy dominates and a high-spin configuration results. Likewise, a low-spin configuration will be preferred with strong-field ligands such as histidine or imidazole.

A characteristic property of protein-bound hemes is the presence of low-lying spin states in close energetic proximity [2, 3]. Because of this small energy separation between spin states, their relative ordering, as well as their electronic properties, are particularly sensitive to the axial ligands bound to the central iron. In fact, the proximity of the different spin states can be essential to protein function. For instance, in the proposed enzymatic cycle of cytochrome P450, the iron starts from the resting low-spin ferric form and converts to high-spin upon substrate binding, after what one-electron reduction occurs, yielding a high-spin ferrous state [2].

Density functional theory (DFT) is widely used to model the properties of molecular system and has

*Corresponding author. Email: smithdm@whitman.edu

---

Molecular Physics
ISSN 0026-8976 print/ISSN 1362-3028 online © 2005
Taylor & Francis Group Ltd
http://www.tandf.co.uk/journals
DOI: 10.1080/00268970512331317309

proved attractive to model hemes, including the relative energies of high-spin and low-spin states [2–4], opti- mized geometries [3, 5–10], Mössbauer parameters [3, 5, 6, 10–13], harmonic frequencies [3, 9] and even the electronic structure of an entire cytochrome [14]. The DFT functionals used in these studies include LSDA, BPW91, and, most commonly, B3LYP. The electron correlation that is accounted for in DFT makes the level of theory appealing. In many cases, these functionals have provided calculated data in apparent accord with experimental data for many systems and their proper- ties, including for hemes. However, there are examples of studies that reveal that some functionals fail to reproduce certain heme properties. A well documented case involves the relative energies of low-lying spin [3, 5–10] states in a model of the resting low-spin ferric heme of cytochrome P450 [2]. Undoubtedly other observations of such findings are likely to involve metallo-systems with their electronic configurations that have many open shells accessible. It is fair to note that at the start these DFT functionals were not parameterized for metal-containing systems, so that their level of accuracy and reliability remains to be critically assessed.

Recent studies, which compare unrestricted Hartree– Fock (UHF) with DFT functionals such as B3LYP, BLYP and half-and-half, provide ample evidence that both the sign and magnitude of energy differences between spin states are very sensitive to the choice of functional [2, 4, 15]. The results of the present study, and those of others [4], indicate that UHF favours high-spin states, GGA functionals favour low-spin states, and hybrid functionals that include a fraction of the exact exchange yield small energy differences between low- and high-spin states. The sensitivity of the spin state ordering to the functionals, particularly the fraction of the exact exchange, indicates that, at present, there is no such thing as a ‘right’ functional for predicting spin state splitting energies. For example, Scherlis and Estrin [4] showed that the Becke half-and-half functional predicts the correct spin state for a penta-coordinate heme while B3LYP works best for a closely related hexa-coordinate heme [4]. It is natural then that one might consider adjusting the mixture of correlation and exchange functionals to create a functional such as B3LYP* [15, 16], with the intend to reproduce experimental data for selected organometallic systems that have states of different multiplicity close in energy. Until there are a large number of detailed comparisons with experimental energy data and a number of predictions with critically assessed levels of accuracy and reliability, it will not be possible to unequivocally predict energy splittings for heme systems and other systems of similar character- istics. Such a systematic study is beyond the scope of this paper. Rather, our aim is to illustrate that molecular properties such as optimized geometries, Mössbauer quadrupole splitting values, and others, ought to be used in a critical assessment of the quality of Kohn– Sham wavefunctions and of the functionals.

We chose two model hemes for this study. Since bis(histidine) hemes are present in many cytochrome proteins [17] there is an abundance of experimental data available. Therefore, we chose bis(imidazole) iron porphyrin [FeP(Im)₂] as one model complex, in which the imidazoles are representative of the histidine side chains. The strong-field imidazole ligands give the complex a low-spin ground state, which has been observed experimentally in the bis(histidine) hemes of cytochromes CymA and OmcA. The EPR spectrum of fully oxidized CymA at 10 K included features typical of a low-spin $(S=1/2)$ ferric heme with bis- ligated histidines in a parallel orientation, and high-spin $(S=5/2)$ ferric heme was also detected at very low levels (estimated 2% of total heme) [18]. In our second model heme the iron is axially ligated by two parallel water molecules $[FeP(H_{2}O)_{2}]$, and has a high-spin ground state. There are structural and Mössbauer data for this complex, although only for high-spin ferric state. For both $FeP(Im)_{2}$ and $FeP(H_{2}O)_{2}$ the net charges of the ferric and ferrous model hemes are +1 and 0, respectively.

## Computational methods

Our six-coordinate model hemes are oriented, according to the convention, with the iron at the origin and porphyrin nitrogen atoms aligned along the x- and y-axes. The axial ligand planes are parallel and are perpendicular to the porphyrin, bisecting its N-Fe-N angles. Figures 1 and 2 show the molecular structures of the bis(imidazole) and bis(aquo) hemes.

Both model hemes are symmetric about the porphyrin plane ($C_{s}$ symmetry). For each model heme, the Fe(3d) electron configuration of the ferrous $^{1}A'$ state is $d_{xy}^{2}d_{xz}^{2}d_{yz}^{2}$, and the configuration of the ferric $^{6}A'$ has each orbital singly occupied. The ferric $^{2}A''$ and ferrous $^{5}A''$ states, however, can have unique occupations of either the $d_{xy}$ or $(d_{\pi}=d_{xz},d_{yz})$ orbitals [19–21]. The more common configuration for hemes with parallel axial ligands is $d_{xy}^{2}(d_{xz},d_{yz})^{3}$ [19]. This is consistent with the $(\pi,d_{\pi})$ charge transfer bands observed for low-spin ferric hemes such as cytochrome c [21] and high-spin ferrous heme proteins [22]. The Fe(3d) orbital occupa- tion numbers used in the initial density guess for all four oxidation/spin states are shown in table 1.

We used the Ahlrich VTZ basis set for iron, and 6-31G* for the porphyrin and axial ligands (imidazole

![](./images/812308713040773121_2.jpg)

Figure 1. FeP(Im)₂.

![](./images/812308713040773121_3.jpg)

Figure 2. FeP(H₂O)₂.

or water). A reasonable starting guess for the open-shell density of the model heme complexes was generated from UHF orbitals of atomic iron, isolated porphyrin, and imidazole or water fragments. Using this initial guess for the density, geometry optimizations were initiated for the ferric low-spin (²A''), ferric high-spin (⁶A'), ferrous low-spin (¹A') and ferrous high-spin (⁵A'') states. All calculations were performed using the NWChem [23] software package on a Hewlett- Packard supercomputer using up to 32 Itanium-2 processors.

Once the geometry optimizations converged, the resulting orbitals were used to calculate the electric field gradient (EFG) tensor, which was then used to calculate Mössbauer parameters. Quadrupole splitting measured with Mössbauer spectroscopy is useful for measuring the oxidation and spin state of iron atoms in heme proteins, and theoretical verification of the Mössbauer quadrupole splitting ($\Delta E_{\rm Q}$) is an effective means of validating the calculated electron density at and around the central iron atom. $\Delta E_{\rm Q}$ and $\eta$, the

<table>
<caption>Table 1. Fe(3d) orbital occupation numbers for model hemes.</caption>
<thead>
<tr><th rowspan="3">Orbital</th><th colspan="4">L = Im, H₂O</th></tr>
<tr><th colspan="2">[Fe(II)PL₂]⁰</th><th colspan="2">[Fe(III)PL₂]⁺¹</th></tr>
<tr><th>¹A'</th><th>⁵A'</th><th>²A''</th><th>⁶A'</th></tr>
</thead>
<tbody>
<tr><td>$n(d_{xy})$</td><td>2</td><td>1</td><td>2</td><td>1</td></tr>
<tr><td>$n(d_{xz}, d_{yz})$</td><td>4</td><td>3</td><td>3</td><td>2</td></tr>
<tr><td>$n(d_{x^2-y^2}^2)$</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>
<tr><td>$n(d_{z}^2)$</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>
</tbody>
</table>

asymmetry parameter, are related to the components of the EFG tensor as follows:

$$
\eta=\frac{V_{x x}-V_{y y}}{V_{z z}} \tag{1}
$$

$$
\Delta E_{Q}=\frac{1}{2} e Q V_{Z Z}\left(1+\frac{\eta^{2}}{3}\right)^{1 / 2}, \tag{2}
$$

where the $V$ values are the principal components of the EFG at the iron nucleus (using the convention $V_{Z Z}>V_{Y Y}>V_{X X}$), $e$ is the electron charge, and $Q$ is the iron quadrupole moment, equal to 0.16 barn $\pm 5\%$ (1 barn $=10^{-28} \mathrm{~m}^{2}$).

The Mössbauer parameters $\Delta E_{\rm Q}$ and $\eta$ reflect the spatial distribution of electrons around the iron. The EFG has two parts; the largest is a valence contribution which results from the unequal electronic population of the valence orbitals, particularly the Fe(3d) orbitals. The valence contribution to the EFG can be described in terms of the Fe(3d) orbital anisotropy [3, 11], $\Delta n_d$:

$$
\begin{aligned}
\Delta n_{d}=n\left(d_{x^{2}-y^{2}}\right)+n\left(d_{x y}\right)-n\left(d_{z^{2}}\right)-\frac{1}{2} n\left(d_{x z}\right)-\frac{1}{2} n\left(d_{y z}\right),
\tag{3}
\end{aligned}
$$

where the $n$ are the orbital occupation numbers (see table 1). The second, smaller, term is the contribution of the external lattice, which contributes if the iron nucleus is in a non-cubic environment. In the present study, the lattice component will have a significant effect on the EFG, and therefore the quadrupole splitting, if the iron- porphyrin and iron-imidazole (or iron-water) distances are significantly different (see tables 2 and 3). The lattice component depends on the molecular geometry, so it is necessary to optimize the geometry using the same method as in the calculation of EFG. A recent DFT study of hemes showed that the error in $\Delta E_{\rm Q}$, calculated using un-optimized X-ray structures, depends on the quality of the crystal structure [12]. Both valence and lattice effects contribute to $\eta$ and $V_{zz}$, the largest component of the EFG, and therefore to $\Delta E_{\rm Q}$.

Both $\Delta E_{\rm Q}$ and the spin splitting energy $\Delta E_{\rm hs/l}$ will vary with the quantum mechanical method used. This

<table><caption>Table 2. Bis(imidazole) heme iron-ligand distances (Å), high-spin/low-spin energy differences (kcal mol⁻¹), and quadrupole splitting parameters (mm s⁻¹).</caption>
<tbody><tr><th></th><th colspan="2">$\lbrack\text{Fe(II)P(Im)}_2\rbrack^0$</th><th colspan="2">$\lbrack\text{Fe(III)P(Im)}_2\rbrack^1$</th></tr>
<tr><th></th><td>¹A′</td><td>⁵A′</td><td>²A″</td><td>⁶A′</td></tr>
<tr><th colspan="5">$\text{Fe-N}_\varepsilon/\text{Fe-N}_\text{p}$ (Å)</th></tr>
<tr><th>Experiment</th><td>2.00/2.00ᵃ</td><td></td><td>1.97/2.01ᵇ</td><td>2.25/2.05ᶜ</td></tr>
<tr><th>B3LYP</th><td>2.05/2.03</td><td>2.36/2.09</td><td>2.02/2.02</td><td>2.24/2.07</td></tr>
<tr><th>B3LYP*</th><td>2.03/2.02</td><td>2.31/2.08</td><td>2.02/2.01</td><td>2.21/2.06</td></tr>
<tr><th>Half-and-half</th><td>2.05/2.02</td><td>2.30/2.08</td><td>2.01/2.00</td><td>2.17/2.05</td></tr>
<tr><th>BLYP</th><td>2.03/2.02</td><td>2.33/2.09</td><td>2.03/2.02</td><td>2.26/2.08</td></tr>
<tr><th>LSDA</th><td>1.91/1.96</td><td>2.13/2.05</td><td>1.92/1.97</td><td>2.11/2.04</td></tr>
<tr><th>UHF</th><td>2.42/2.14</td><td>2.48/2.11</td><td>2.14/2.03</td><td>2.25/2.07</td></tr>
<tr><th colspan="5">$\Delta E_{\text{hs/lis}}$ (kcal mol⁻¹)</th></tr>
<tr><th>B3LYP</th><td>9</td><td></td><td></td><td>7</td></tr>
<tr><th>B3LYP*</th><td>15</td><td></td><td></td><td>13</td></tr>
<tr><th>Half-and-half</th><td>−19</td><td></td><td></td><td>−29</td></tr>
<tr><th>BLYP</th><td>28</td><td></td><td></td><td>26</td></tr>
<tr><th>LSDA</th><td>55</td><td></td><td></td><td>46</td></tr>
<tr><th>UHF</th><td>−55</td><td></td><td></td><td>−83</td></tr>
<tr><th colspan="5">$\Delta E_{\text{Q}}$ (mm s⁻¹)</th></tr>
<tr><th>Expt.</th><td>0.97–1.07ᵃ</td><td></td><td>2.31ᵇ</td><td></td></tr>
<tr><th>B3LYP</th><td>0.92</td><td>2.81</td><td>2.78</td><td>1.04</td></tr>
<tr><th>B3LYP*</th><td>0.93</td><td>2.54</td><td>2.73</td><td>0.95</td></tr>
<tr><th>Half-and-half</th><td>0.53</td><td>3.02</td><td>2.70</td><td>1.05</td></tr>
<tr><th>BLYP</th><td>1.27</td><td>2.28</td><td>2.47</td><td>0.82</td></tr>
<tr><th>LSDA</th><td>1.41</td><td>1.60</td><td>2.94</td><td>0.26</td></tr>
<tr><th>UHF</th><td>1.37</td><td>2.69</td><td>2.00</td><td>1.69</td></tr>
</tbody>
</table>

ᵃBis(1-substituted imidazoles)(tetraphenylporphinato)iron(II) [25].
ᵇBis(1-methylimidazole)(meso-tetramesitylporphinato)iron(III) [26].
ᶜBis(2-methylimidazole)(octaethylporphinato)iron(III) [27].

discrepancy can be traced to the Hartree–Fock exchange which systematically favors high-spin states [3, 15]. Godbout and co-workers [5] calculated $\Delta E_{\text{Q}}$ for $\text{Fe(CO)}_5$ and found that when exact exchange is used (B3LYP, B3PW91, B3P86) the calculated value is $2.55\ \text{mm}\ \text{s}^{-1}$ within $0.04\ \text{mm}\ \text{s}^{-1}$ of the experimental value $(2.51\ \text{mm}\ \text{s}^{-1})$. When no exact exchange is used (BLYP, BP86) the splitting is $\sim 0.3\ \text{mm}\ \text{s}^{-1}$ too low. When too much exact exchange is used (Half-and-Half) the splitting is $\sim 0.3\ \text{mm}\ \text{s}^{-1}$ too high.

## 3. Results and discussion

### 3.1. $\text{FeP(Im)}_2$

Using the B3LYP, BLYP, B3LYP*, half-and-half, LSDA and UHF methods we performed full optimizations of the geometries of all four heme spin/oxidation states of the bis(imidazole) model heme. The optimized geometries, high-spin/low-spin energy splittings, and Mössbauer quadrupole splitting parameters will be compared to available experimental values to asses the quality of these methods for modelling hemes.

<table><caption>Table 3. Bis(aquo) heme iron-ligand distances (Å), high-spin/low-spin energy differences (kcal mol⁻¹), and quadrupole splitting parameters (mm s⁻¹).</caption>
<tbody><tr><th></th><th colspan="2">$\lbrack\text{Fe(II)P(H}_2\text{O)}_2\rbrack^0$</th><th colspan="2">$\lbrack\text{Fe(III)P(H}_2\text{O)}_2\rbrack^1$</th></tr>
<tr><th></th><td>¹A′</td><td>⁵A″</td><td>²A″</td><td>⁶A″</td></tr>
<tr><th colspan="5">$\text{Fe-OH}_2/\text{Fe-N}_\text{p}$ (Å)</th></tr>
<tr><th>Experiment</th><td></td><td>2.3/2.07ᵃ</td><td></td><td>2.10/2.05ᵇ</td></tr>
<tr><th>B3LYP</th><td>2.04/2.02</td><td>2.33/2.08</td><td>2.03/2.00</td><td>2.18/2.05</td></tr>
<tr><th>B3LYP*</th><td>2.04/2.01</td><td>2.32/2.07</td><td>2.03/2.00</td><td>2.18/2.05</td></tr>
<tr><th>BLYP</th><td>2.04/2.02</td><td>2.27/2.08</td><td>2.04/2.01</td><td>2.22/2.07</td></tr>
<tr><th>UHF</th><td>2.24/2.05</td><td>2.43/2.09</td><td>2.18/2.05</td><td>2.20/2.05</td></tr>
<tr><th colspan="5">$\Delta E_{\text{hs/lis}}$ (kcal mol⁻¹)</th></tr>
<tr><th>B3LYP</th><td></td><td>−2</td><td></td><td>−6</td></tr>
<tr><th>B3LYP*</th><td></td><td>2</td><td></td><td>−2</td></tr>
<tr><th>BLYP</th><td></td><td>11</td><td></td><td>7</td></tr>
<tr><th>UHF</th><td></td><td>−61</td><td></td><td>−87</td></tr>
<tr><th colspan="5">$\Delta E_{\text{Q}}$</th></tr>
<tr><th>Experiment</th><td></td><td>2.75ᶜ</td><td></td><td>1.53ᵇ</td></tr>
<tr><th>B3LYP</th><td>2.04</td><td>3.02</td><td>3.33</td><td>2.13</td></tr>
<tr><th>B3LYP*</th><td>2.22</td><td>2.91</td><td>3.46</td><td>2.01</td></tr>
<tr><th>BLYP</th><td>2.63</td><td>2.59</td><td>3.40</td><td>1.73</td></tr>
<tr><th>UHF</th><td>0.12</td><td>3.49</td><td>2.05</td><td>2.54</td></tr>
</tbody>
</table>

ᵃBis(tetrahydrofuran)(tetraphenylporphinato)iron(II) [28].
ᵇBis(aquo)(meso-tetraphenylporphinato)iron(III) [29].
ᶜBis(tetrahydrofuran)(meso-tetramesitylporphinato)iron(II) [24].

### 3.1.1. Geometries.
Table 2 shows the optimized iron-ligand distances for the bis(imidazole) heme calculated with different methods, as well as available experimental values. $\text{Fe-N}_\varepsilon$ is the average distance between iron and the imidazole nitrogens, and $\text{Fe-N}_\text{p}$ is the distance between iron and the porphyrin nitrogen. It is clear from table 2 that UHF fails to reproduce the experimental geometries of the low-spin bis(imidazole) hemes. The singlet iron-imidazole distance is very long, and the same distance in the doublet is also much too long. The iron-imidazole distance in the sextet, however, is in excellent agreement the experimental value. This is consistent with the Hartree-Fock preference towards high-spin states.

The B3LYP, B3LYP* and BLYP functionals perform equally well in reproducing the experimental iron-imidazole distances, and the half-and-half functional is nearly as good. The LSDA iron-imidazole distances are

too short by approximately 0.1 Å for all oxidation/spin states.

3.1.2. Spin state energy differences. Ligand field theory predicts that the bis(imidazole) heme should have a low-spin ground state. Table 2 shows the calculated spin state splitting energies, which are the differences in total energy (nuclear + electronic) between the high-spin and low-spin hemes at their respective optimized geometries. A positive value means that the low-spin energy is lower than high-spin energy.

The bis(imidazole) hemes should have small, positive $\Delta \mathrm{E}_{\mathrm{hs} / \mathrm{ls}}$, in order to be consistent with the experimentally observed low-spin state in equilibrium with approxi- mately 2% high-spin [18]. Although the splitting energies calculated with B3LYP, B3LYP*, BLYP and LSDA all have the correct sign, B3LYP gives the smallest positive value. The negative sign of the splitting calculated with UHF and Half-and-Half (which includes the greatest fraction of exact HF exchange) is indicative of their preference for high-spin states.

3.1.3. Mössbauer quadrupole splitting. Recall from the earlier comment that $\Delta E_{\mathrm{Q}}$ includes both valence and lattice contributions. The valence contribution depends on the Fe(3d) orbital occupations (see table 1), and according to equation (3), only the ferric doublet and ferrous quintet have Fe(3d) valence asymmetry. The lattice contribution is significant when the electron density surrounding the iron is non-cubic, so the high- spin hemes, in which $\mathrm{Fe}-\mathrm{N}_{\varepsilon}>\mathrm{Fe}-\mathrm{N}_{\mathrm{p}}$, have lattice contributions to the EFG. The ordering for these oxidation/spin states is then $\Delta E_{\mathrm{Q}}({}^5\mathrm{A}'')>\Delta E_{\mathrm{Q}}({}^2\mathrm{A}'')>$ $\Delta E_{\mathrm{Q}}({}^6\mathrm{A}')>\Delta E_{\mathrm{Q}}({}^1\mathrm{A}')$. Of all the methods used, B3LYP, half-and-half and UHF get the correct trend for $\Delta E_{\mathrm{Q}}$.

### 3.2. $\mathrm{FeP}(\mathrm{H}_{2}\mathrm{O})_{2}$

Results for the bis(imidazole) model heme indicate that B3LYP best meets our quality criteria (geometry, spin state relative energies, and quadrupole splitting). In order to determine how the amount of Hartree-Fock exchange affects the properties of a high-spin heme, we chose the B3LYP, B3LYP*, BLYP and UHF methods for the bis(aquo) heme. These methods include 20%, 15%, 0% and 100% HF exchange, respectively.

3.2.1. Geometries. Since no ferrous high-spin bis(aquo) heme data was found, the ferrous quintet bis(aquo) heme geometry is compared to a bis(tetrahydrofuran) heme. All three functionals reproduce the $\mathrm{Fe-O}$ and $\mathrm{Fe-N_{p}}$ distances surprisingly well. The ferric sextet heme, which has one electron in each of the five Fe(3d) orbitals, should be easier to reproduce, but all three functionals and UHF give $\mathrm{Fe-O}$ distances which are too long by $\sim 0.1$ Å.

3.2.2. Spin state energy differences. Ligand field theory predicts that the bis(aquo) heme will have a high-spin ground state, which is consistent with the crystal field interpretation of the X-ray data for Bis(tetrahydrofuran)(meso-tetramesitylporphinato)iron(II) [24] which predicted a high-spin/low-spin energy differ- ence of $-1667\ \mathrm{cm}^{-1}\ (-4.8\ \mathrm{kcal\ mol}^{-1})$. B3LYP is the only functional which yields a small, negative spin state splitting calculated for both ferric and ferrous bis(aquo) hemes. UHF predicts the correct energetic ordering, but the separation is much too large. B3LYP* predicts nearly degenerate low-spin and high-spin states, and BLYP incorrectly predicts low-spin ground states.

3.2.3. Mössbauer quadrupole splitting. In the ${}^6\mathrm{A}'$ bis(aquo) model heme, five electrons are evenly dis- tributed in the Fe(3d) shell, so it has no anisotropy and therefore no valence contribution to the EFG. The distance between the iron and the porphyrin nitrogen atoms is shorter than the distance to the waters, so only lattice effects to contribute to the EFG and the quadrupole splitting is small. The experimentally measured quadrupole splitting for $\mathrm{Fe(TPP)(H_{2}O)_{2}}$ of $1.53\ \mathrm{mm\ s}^{-1}$ is much smaller than the calculated values, because of the calculated versus experimental geometry discrepancy (longer $\mathrm{Fe-O}$ distances increase the lattice asymmetry). However, the $\mathrm{Fe(TPP)(H_{2}O)_{2}}\ \Delta E_{\mathrm{Q}}$ is temperature dependent, and so is the $\mathrm{Fe-O}$ distance in the bis(THF) heme. Therefore, as the temperature increases, so does the $\mathrm{Fe-O}$ bond length and $\Delta E_{\mathrm{Q}}$, which makes comparison difficult.

## 4. Conclusions

The B3LYP hybrid functional appears to be the best one for modeling the bis(imidazole) heme, since it best meets all of the quality criteria we have used here (high-spin/ low-spin relative energies, optimized geometries, and quadrupole splitting). This is consistent with previous B3LYP calculations of hemes (see introduction). The bis(aquo) heme results are rather unsatisfying; none of the methods used (UHF, B3LYP, B3LYP*, BLYP) reproduced the iron-water distance measured experi- mentally, although comparison is difficult because of the temperature dependence of the experimental structure. However, B3LYP did get the spin state splitting correct,whereas the other methods did not. In summary:

1. B3LYP predicts correct geometries, spin state energy differences, and quadrupole splitting for the bis(imidazole) heme.

2. B3LYP predicts correct spin state energy differ- ences for the bis(aquo) heme.

3. B3LYP* predictions correlate with experimental results nearly as well as B3LYP.

4. BLYP geometries are good and spin state splittings are of the correct sign, but are too large in magnitude, and quadrupole splittings are wrong.

5. Half-and-half geometries are good, but spin state ordering is wrong.

6. LSDA iron-axial ligand bonds are too short, and quadrupole splitting is too large.

7. UHF Fe-axial ligand bonds are too long, and spin state ordering is wrong.

## Acknowledgments

This work was supported in part by the Office of Advanced Scientific Computing Research, Office of Science, Department of Energy. Computational resources for this work were provided by the Molecular Sciences Computing Facility of the Environmental Molecular Sciences Laboratory at Pacific Northwest National Laboratory. Pacific Northwest National Laboratory is operated for the U.S. Department of Energy by the Battelle Memorial Institute.

## References

[1] A.C. Cotton, G. Wilkinson, *Advanced Inorganic Chemistry*, John Wiley & Sons, New York (1999).

[2] G.H. Loew, D.L. Harris, *Chem. Rev.*, **100**, 407 (2000).

[3] D.M.A. Smith, M. Dupuis, E.R. Vorpagel, T.P. Straatsma, *J. Am. Chem. Soc.*, **125**, 2711 (2003).

[4] D.A. Scherlis, D.A. Estrin, *Int. J. Quantum Chem.*, **87**, 158 (2002).

[5] N. Godbout, R. Havlin, R. Salzmann, P.G. Debrunner, E. Oldfield, *J. Phys. Chem. A*, **102**, 2342 (1998).

[6] N. Godbout, L.K. Sanders, R. Salzmann, R.H. Havlin, M. Wojdelski, E. Oldfield, *J. Am. Chem. Soc.*, **121**, 3829 (1999).

[7] M.P. Johansson, D. Sundholm, G. Gerfen, M. Wikstrom, *J. Am. Chem. Soc.*, **124**, 11771 (2002).

[8] M.P. Johansson, M.R.A. Blomberg, D. Sundholm, M. Wilkstron, *Biochim. Biophys. Acta*, **1553**, 183 (2002).

[9] P.M. Kozlowski, T.G. Spiro, M.Z. Zgierski, *J. Phys. Chem. B*, **104**, 10659 (2000).

[10] H. Kuramochi, L. Noodleman, D.A. Case, *J. Am. Chem. Soc.*, **119**, 11442 (1997).

[11] M. Grodzicki, H. Flint, H. Winkler, F.A. Walker, A.X. Trautwein, *J. Phys. Chem. A*, **101**, 4202 (1997).

[12] Y. Zhang, J.H. Mao, N. Godbout, E. Oldfield, *J. Am. Chem. Soc.*, **124**, 13921 (2002).

[13] Y. Zhang, J.H. Mao, E. Oldfield, *J. Am. Chem. Soc.*, **124**, 7829 (2002).

[14] F. Sato, T. Yoshihiro, M. Era, H. Kashiwagi, *Chem. Phys. Lett.*, **341**, 645 (2001).

[15] M. Reiher, O. Salomon, B.A. Hess, *Theoretical Chem. Accounts*, **107**, 48 (2001).

[16] O. Salomon, M. Reiher, B.A. Hess, *J. Chem. Phys.*, **117**, 4729 (2002).

[17] S.D. Zaric, D.M. Popovic, E.W. Knapp, *Biochemistry*, **40**, 7914 (2001).

[18] S.J. Field, P.S. Dobbin, M.R. Cheesman, N.J. Watmough, A.J. Thomson, D.J. Richardson, *J. Biol. Chem.*, **275**, 8515 (2000).

[19] F.A. Walker, *Coord. Chem. Rev.*, **186**, 471 (1999).

[20] F.U. Axe, C. Flowers, G.H. Loew, A. Waleh, *J. Am. Chem. Soc.*, **111**, 7333 (1989).

[21] P. Du, G.H. Loew, S. Canuto, M.C. Zerner, *J. Am. Chem. Soc.* **113(23)**, 8614–8621 (1991).

[22] V.S. Oganesyan, Y.A. Sharonov, *Spectrochim. Acta, Part a-Mol. Biomol. Spectrosc.*, **53**, 433 (1997).

[23] R.J. Harrison, J.A. Nichols, T.P. Straatsma, M. Dupuis, E.J. Bylaska, G.I. Fann, T.L. Windus, E. Apra, W. de Jong, S. Hirata, M.T. Hackler, J. Anchell, D. Bernholdt, P. Borowski, T. Clark, D. Clerc, H. Dachsel, M. Deegan, K. Dyall, D. Elwood, H. Fruchtl, E. Glendening, M. Gutowski, K. Hirao, A. Hess, J. Jaffe, B. Johnson, J. Ju, R. Kendall, R. Kobayashi, R. Kutteh, Z. Lin, R. Littlefield, X. Long, B. Meng, T. Nakajima, J. Nieplocha, S. Niu, M. Rosing, G. Sandrone, S. Stave, H. Taylor, G. Thomas, J. van Lenthe, K. Wolinski, A. Wong, Z. Zhang, N.W. Chem, A Computational Chemistry Package for Parallel Computers, Version 4.6, Pacific Northwest National Laboratory, Richland, Washington 99352-0999, USA (2004).

[24] B. Boso, G. Lang, C.A. Reed, *J. Chem. Phys.*, **78**, 2561 (1983).

[25] M.K. Safo, W.R. Scheidt, G.P. Gupta, *Inorg. Chem.*, **29**, 626 (1990).

[26] M.K. Safo, G.P. Gupta, F.A. Walker, W.R. Scheidt, *J. Am. Chem. Soc.*, **113**, 5497 (1991).

[27] E. Elkaim, K. Tanaka, P. Coppens, W.R. Scheidt, *Acta Crystallogr. B Struct. Commun.*, **43**, 457 (1987).

[28] C. Lecomte, R.H. Blessing, P. Coppens, A. Tabard, *J. Am. Chem. Soc.*, **108**, 6942 (1986).

[29] W.R. Scheidt, I.A. Cohen, and M.E. Kastner, *Biochemistry*, **18**, 3546 (1979).