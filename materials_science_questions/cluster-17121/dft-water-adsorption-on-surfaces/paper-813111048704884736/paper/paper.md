Accepted Manuscript

Influence of water, dihydrogen and dioxygen on the Stability of the
$Cr_2O_3$ surface: a first-principles investigation

Sidi M.O. Souvi, Michael Badawi, François Virot, Sylvain Cristol,
Laurent Cantrel, Jean-François Paul

![](./images/813111048704884736_1.jpg)

| | |
|---|---|
|PII: |S0039-6028(17)30317-5|
|DOI: |10.1016/j.susc.2017.08.005|
|Reference: |SUSC 21069|

| | |
|---|---|
|To appear in: |*Surface Science*|

| | |
|---|---|
|Received date: |19 May 2017|
|Revised date: |21 July 2017|
|Accepted date: |1 August 2017|

Please cite this article as: Sidi M.O. Souvi, Michael Badawi, François Virot, Sylvain Cristol,
Laurent Cantrel, Jean-François Paul, Influence of water, dihydrogen and dioxygen on the
Stability of the $Cr_2O_3$ surface: a first-principles investigation, *Surface Science* (2017), doi:
10.1016/j.susc.2017.08.005

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service
to our customers we are providing this early version of the manuscript. The manuscript will undergo
copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please
note that during the production process errors may be discovered which could affect the content, and
all legal disclaimers that apply to the journal pertain.

### Highlights
- DFT study of $O_2$, $H_2O$ and $H_2$ interaction with (0001) $Cr_2O_3$ surfaces.
- Water adsorption on chromia surface: hydrated surface vs fully hydroxylation one.
- Surface reduction by $H_2$ is not thermodynamically possible.

# Influence of water, dihydrogen and dioxygen on the Stability of the $Cr_2O_3$ surface:
a first-principles investigation

Sidi M. O. SOUVI $^{a,b,*}$, Michael BADAWI $^{c}$, François VIROT $^{a}$, Sylvain CRISTOL $^{d}$, Laurent CANTREL $^{a,b}$,
Jean-François PAUL $^{d,**}$

$^{a}$ Laboratoire commun IRSN-CNRS-Lille1: "Cinétique Chimique, Combustion, Réactivité" $(C^3R)$, Centre de Cadarache, BP3, 13115 Saint Paul Lez Durance, Cedex, France
$^{b}$ Institut de Radioprotection et de Sûreté Nucléaire, PSN-RES, SAG, Centre de Cadarache, BP3, 13115 Saint Paul Lez Durance, Cedex, France
$^{c}$ Laboratoire LCP-A2MC, EA 4632, Institut Jean-Barriol FR2843 CNRS, Université de Lorraine – Rue Victor Demange, 57500 Saint Avold, France
$^{d}$ Unité de Catalyse et Chimie du Solide, Université Lille 1 - Sciences et Technologie, UMR CNRS 8181, 59650 Villeneuve d'Ascq, France

## Abstract
In this theoretical work, the stability of $\alpha$-$Cr_2O_3$ surfaces in various oxidizing and reducing environments has been investigated. The electronic structure calculations, the magnetic properties of the bulk and surfaces have been explored within the DFT+U framework. Investigating a large number of possible terminations we show that the oxidation promotes the formation of a chromyl surface in agreement with the existing literature. We show that the hydrogenation of bare chromia surface is not thermodynamically favored, however, adding hydrogen to the chromyl surface leads to a very stable hydroxide termination. Regarding water adsorption, we discuss the differences between the experiment results published in (M. A. Henderson, S. A. Chambers, Surf. Sci. 449 (2000) 135) leading to a fully hydrated surface and those published in (V. Maurice, S. Cadot, P. Marcus, Surf. Sci. 471 (2001) 43) leading to a fully hydroxylated surface. Finally we present a new hydrated surface (fully hydroxylated surface) noted [-$Cr_2$-(OH)$_3$], which is consistent with experimental observations.

## Keywords
Surface stability Chromium oxide, Chemical potential, Magnetism,

* Corresponding author. E-mail address: sidi.souvi@irsn.fr (Sidi M. O. SOUVI). Phone: +33442199167. Fax: +33442199167.
** Corresponding author. E-mail address: jean-francois.paul@univ-lille1.fr (J.-F. Paul). Phone: +33 320337734. Fax: +33 320436561.

## 1. Introduction
Chromium oxides are used in many applications, in catalysis, photocatalysis, and environmental chemistry [1-3]. They are employed as catalysts for polymerization of ethylene [1] and dehydrogenation reactions [3]. Besides, $Cr_2O_3$ is a protective overlayer in stainless steel against corrosion [4,5]. A good knowledge of the evolution of the surface state of chromium oxides upon various conditions (temperature, partial pressures of different gases) is a prerequisite to study the interactions of these materials with gas molecules. Indeed, various experimental and processing conditions can modify the surface structure. One example for which the surface state would be strongly altered is the stainless steel wall of the reactor coolant system (RCS) when a severe accident occurs in nuclear power plant. In fact, the severe accident induces an extreme change in conditions of RCS: in operating conditions the wall surfaces are submerged by liquid water (155-165 bars and 300-350°C) will in accidental conditions these surfaces may be in contact with a mixture of hydrogen/steam/air and the total pressure may decrease to 1 bar with an increase of the temperature up to 1200°C. The RCS are made of stainless steel 304 L and Inconel alloys for the steam generator tubes, covered by various oxide layers which exact composition is depending on experimental conditions. Indeed, the 304L external layer contains $Cr_2O_3$ and $Fe_2O_3$ according to XPS, TOF-Sims SEM and EDS characterizations [6-10], while Inconel exhibit also chromium oxides and mixed oxides like $FeCr_2O_4$ [8] or $(Fe_{1-x}Cr_x)_2O_3$ [11]. Therefore the adsorption, retention and desorption of iodine and cesium species over $Fe_2O_3$ and $Cr_2O_3$ surfaces in case of severe accident constitutes a key safety issue for modelling the fission products releases in severe accident conditions. Before considering the latter issue, the surface state of these oxides under these RCS-specific conditions mentioned above must be known.

In this context, the influence of $O_2$, $H_2O$ and $H_2$ partial pressures as well as the temperature on the surface state of hematite $Fe_2O_3$ has been investigated in our previous work [12]. We focus now on the $Cr_2O_3$ surface.
Several experimental and theoretical studies are available in the literature, investigating both bulk [13] and surface [14-20] of chromium oxide. Their main objective was to determine the surface termination of $\alpha$-(0001)-$Cr_2O_3$ as a function of the chemical potential (corresponding to the partial pressure) of oxygen [14,16] or water [17]. Rohrbach et al. [16] concluded that the most stable surface is Cr-terminated, which can be noted $Cr_2O_3$-Cr or Cr-$O_3$-Cr [14,16]. This surface exhibits 3-fold, under-coordinated Cr surface atoms (Cr has an octahedral, 6-fold coordination in the bulk) due to the loss of oxygen atoms above the surface plane. Wang and Smith [14] results agree with Rohrbach on the stability of the Cr-$O_3$-Cr termination but at high temperature. They also found other stables terminations, oxygen terminated (Cr-Cr-$O_3$) at room temperature, and a chromyl (Cr-$O_3$-Cr-O) one at higher temperature. More recently, SXRD experiments [21] at room temperature highlight other terminations more oxygenated and with chromyl, depending on the oxygen partial pressure. The nature of stable terminations depending on oxygen coverage is still a matter of debate, since previous studies are generally focused on a specific range of temperature and pressure. Besides, no adsorption study of reducing molecule such as dihydrogen on $\alpha$-(0001)-$Cr_2O_3$ surface was found in the literature. J. Fan et al [22], showed the ability of $Cr_2O_3$ amorphous phase to adsorb $H_2$ molecules. Regarding water coverage, Costa et al. [17] depicted an appropriate picture of

the hydroxylation of the chromia surface; however the water dissociation phenomena can raise some questions that we propose to address here. Very recently Lindsay et al. [15] investigated the reactivity of $\alpha$-(0001)-$\text{Cr}_2\text{O}_3$ surface with water and found some disagreements with Costa et al. predictions.

Therefore, we propose to provide here an overview of the evolution of the $\text{Cr}_2\text{O}_3$ (0001) surface over a wide range of temperatures (298.15 to 1200 K) and $\text{H}_2\text{O}$, $\text{H}_2$ and $\text{O}_2$ partial pressures. This study also aims to complete the data and address some issues from previous stability theoretical studies dealing with dioxygen [14,16] or water [17].

Computational methods are reported in Section (2) while the results of surface magnetization analysis, the bare surface stability, molecules adsorption and reaction onto the surfaces are presented and discussed in Section (3).

## 2. Computational Methods
Our calculations are based on the density-functional theory (DFT) [23,24] and the projector augmented plane wave (PAW) method [25,26] as implemented in the Vienna Ab initio Simulation Package (VASP) [27-29]. The Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional in the generalized gradient approximation (GGA) proposed by Perdew et al. [30] was employed. The plane wave cutoff energy was set to 600 eV. The Kohn-Sham equations were solved self-consistently until energy difference between cycles become lower than $10^{-6}$ eV. A Methfessel-Paxton [31] with $\sigma = 0.1$ eV was applied to band occupations.

The DFT + U method of Lichtenstein [32] has been employed to treat the strongly correlated electrons of chromia atoms, with values of U and J set to 4 and 1 eV, respectively. The atomic positions have been fully optimized until all forces were smaller than 0.02 eV/ Å per atom. A (7 7 7) k-point mesh has been used for bulk cells, and a (7 7 1) k-point mesh for surface cells. To avoid any dipolar effect, all calculations have been carried out within symmetric slabs containing 12 chromium layers (one Cr atom per layer) and separated by 21 Å of vacuum. The experimental parameters (a = b= 4.951 Å) have been used to define the slab cell parameters.

## 3. Results and Discussion
### 3.1.Bulk: Structure and Magnetization
The full systematic study of the magnetization has been performed in a hexagonal cell, within experimental parameters (a = b= 4.951 Å and c =13.566 Å) [33]. For the whole magnetic study, + stands for spin up ($\alpha$) and - for spin down ($\beta$).

The hexagonal unit cell derived from the rhombohedral one is presented on Figure 1. It contains 12 chromium atoms among which every four atoms are aligned and constitute a subunit corresponding to the rhombohedral primitive cell.

![](./images/813111048704884736_2.jpg)

Figure 1: Hexagonal unit cell showing the layered structure of chromium (III) oxide.

The structure within this triple unit cell can be described as a succession of one oxygen layer containing three oxygen atoms followed by two neighbouring chromium layers each of them containing one chromium atom. This unit is repeated six times in the hexagonal cell.

As has been shown in previous work [12], in a corundum hexagonal cell, due to symmetrical degeneracy only 38 antiferromagnetic and one ferromagnetic configurations have to be taken into account to perform a systematic magnetization study within the hexagonal cell. As we have mentioned earlier, the hexagonal lattice consists of three rhombohedral primitive cells. In such a primitive cell only three antiferromagnetic spin configurations are possible which we note here: A (+ + - -), B (+ - - +) and C (+ - + -). Every spin configuration of the 38 that we have to consider in the hexagonal cell can be expressed as a combination of primitive configurations A, B and C. These three "pure primitive configurations" are noted in the larger hexagonal cell as AAA, BBB and CCC respectively. More details about the construction of different configurations is given in [12]. The relative energies with respect to the spin ground state are presented in Table 1.

<table><thead><tr><th>Conf</th><th>$\Delta E$</th><th>Conf</th><th>$\Delta E$</th><th>Conf</th><th>$\Delta E$</th></tr></thead><tbody><tr><td>$CCC$</td><td>0</td><td>$BBB$</td><td>25</td><td>$\bar{A}AB$</td><td>36</td></tr><tr><td>$CC\bar{A}$</td><td>16</td><td>$\bar{B}BA$</td><td>26</td><td>$\bar{C}CB$</td><td>36</td></tr><tr><td>$CCA$</td><td>16</td><td>$BBC$</td><td>29</td><td>$\bar{C}\bar{C}B$</td><td>36</td></tr><tr><td>$\bar{A}AB$</td><td>16</td><td>$BB\bar{C}$</td><td>29</td><td>$A\bar{A}\bar{B}$</td><td>36</td></tr><tr><td>$\bar{A}AC$</td><td>17</td><td>$BBA$</td><td>29</td><td>$AC\bar{B}$</td><td>36</td></tr><tr><td>$\bar{A}AC$</td><td>17</td><td>$\bar{C}\bar{C}C$</td><td>31</td><td>$AAB$</td><td>37</td></tr><tr><td>$\bar{A}\bar{A}A$</td><td>17</td><td>$\bar{C}\bar{C}A$</td><td>31</td><td>$\bar{B}BC$</td><td>38</td></tr><tr><td>$CCB$</td><td>21</td><td>$\bar{C}CA$</td><td>31</td><td>$\bar{B}\bar{B}C$</td><td>38</td></tr><tr><td>$CC\bar{B}$</td><td>21</td><td>$AAC$</td><td>31</td><td>$B\bar{B}\bar{B}$</td><td>43</td></tr><tr><td>$\bar{A}BC$</td><td>22</td><td>$AA\bar{C}$</td><td>31</td><td>$AAA$</td><td>47</td></tr><tr><td>$ACB$</td><td>22</td><td>$\bar{A}CB$</td><td>36</td><td>$B\bar{B}\bar{A}$</td><td>47</td></tr><tr><td>$\bar{A}BC$</td><td>22</td><td>$AB\bar{C}$</td><td>36</td><td>$\bar{B}\bar{B}A$</td><td>52</td></tr><tr><td>$\bar{A}C\bar{B}$</td><td>22</td><td>$ABC$</td><td>36</td><td>$FM$</td><td>58</td></tr></tbody></table>

Table 1: Energies (meV per Cr atom) of configurations in the hexagonal cell relative to the spin ground state (CCC).

We notice that the spin ground state is (CCC), in agreement with Rohrbach et al. [16] and Costa et al. [17]. All antiferromagnetic configurations are energetically lower than the ferromagnetic one (FM). Compared with hematite [12], the atomic spin orientation has only a small effect on

the total energy in chromia; the difference between the ground state and the highest configuration is 58 meV/(Cr atom).

### 3.2.Surface spin configurations
We study here the effect of the surface creation on the spin configurations. The nature and stability of surface terminations will be discussed later. Here we consider the only symmetric and stoichiometric possible slab which is actually chromium terminated. We adopt the approach used in our previous paper [12]. This approach consists in building a bigger cell containing 24 oxygen atoms and 16 chromium atoms by adding one chromium double layer on each surface (Figure 2) to keep the same bulk spin description as in the previous part. Thus, the spin configuration of the slab core (5 internal chromium double layers) is CCC as in the bulk, and then all possible configurations were tested symmetrically for the external layers (one chromium double layer and one chromium single layer, noted as $CCC-\infty-\sigma ; \sigma \equiv \alpha(+), \beta(-)$ . Thus, 8 configurations are possible in this reduced surface space, see Figure 2.

![](./images/813111048704884736_3.jpg)

Figure 2: Large hexagonal cell, in order to determine the surface spin configuration, a=b=4.951 Å and c=35 Å.

Table 2: Energies (meV/Å²) relative to the bulk spin ground state configuration $(CCC)$ of configurations near to the surface and the magnetic momentum.

<table>
  <thead>
    <tr>
      <th>Configuration</th>
      <th>ΔE</th>
      <th>Magnetic momentum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CCC-αβ-α</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>CCC-ββ-α</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <td>CCC-βα-β</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <td>CCC-aa-β</td>
      <td>8</td>
      <td>0</td>
    </tr>
    <tr>
      <td>CCC-αβ-β</td>
      <td>15</td>
      <td>-12</td>
    </tr>
    <tr>
      <td>CCC-αα-α</td>
      <td>15</td>
      <td>12</td>
    </tr>
    <tr>
      <td>CCC-ββ-β</td>
      <td>15</td>
      <td>-12</td>
    </tr>
    <tr>
      <td>CCC-βα-α</td>
      <td>15</td>
      <td>12</td>
    </tr>
  </tbody>
</table>

The most stable surface spin configuration is obtained by continuing the most stable bulk configuration (CCC). The creation of the surface does not affect the spin state and thus the molecule absorption could be studied on the previous stable spin state.

### 3.3.Stable surface terminations:
#### 3.3.1. Bare stoichiometric surfaces definition
We investigated the surface terminations in a fixed stoichiometry $Cr_{2}O_{3}$ to define the stable ones. The existence of one chromium termination noted $-Cr-O_{3}-Cr$ is well established in the literature [15-19]. Such a surface is naturally stoichiometric and symmetric in an archetypal hexagonal cell. However, it is not possible to conserve these two constraints, (symmetry and stoichiometry), for oxygen termination within a simple hexagonal cell. An easy way to build a symmetric and stoichiometric oxygen terminated surface is to (i) start with a stoichiometric, but non-stoichiometric, cell $Cr_{12}O_{21},-Cr_{2}-O_{3}$ terminated, (ii) double the cell (in 2x1 form with $Cr_{24}O_{42}$) and then (iii) remove 3 oxygen atoms from both sides of the double cell to obtain a stoichiometric double cell $(Cr_{24}O_{36}$ with $-Cr_{2}-O_{3/2}$ termination), Figure 3.

![](./images/813111048704884736_4.jpg)

Figure 3 : Construction of a symmetric and stoichiometric oxygen terminated surface, with atom positions before relaxation.

The calculations have been performed in a double hexagonal cell for both terminations, i.e. chromium and oxygen ones (Figure 4).

![](./images/813111048704884736_5.jpg)

Figure 4 : Double hexagonal cell: Cr termination on the left, O termination on the right.

The oxygen terminated surface energy is $(80\ \text{meV}/\mathring{A}^{2})$ higher than the chromium terminated one. We are aware that this oxygen termination in double cell is not very usual, since it consists of two neighbouring simple cells with different terminations (one is simply oxygen terminated and the other is doubly oxygen terminated) but it is a classical way to cancel dipolar moment, by dividing the surface charge by two.

#### 3.3.2. Oxygen adsorption on Cr-O3-Cr and Cr-Cr-3/2O surfaces.

Depending on oxygen partial pressure, the $O_2$ molecule can adsorb on the chromium oxide surface or desorb from the $Cr_2O_3$ surfaces. It is necessary to study these processes to determine the most stable surface in different experimental conditions. The two previous stoichiometric terminations, i.e., the chromium and the oxygen ones are noted (I) and (VI) respectively. Their stoichiometries are $Cr_{12}O_{18}$. We have Added/extracted oxygen atoms to/from these stoichiometric terminations (I) and (VI), to define the new terminations see Figure 5. The $Cr-O_3-Cr-O$ (II), $Cr-O_3-Cr-O_2$ (III) and $Cr-O_3-Cr-O_3$ (IV) can be formed by adding 1, 2 and 3 oxygen atoms respectively to $Cr-O_3-Cr$ (I) on both cell sides. The $Cr-O_2-Cr$ (V) surface is defined by extracting an oxygen atom from the (I) second layer (on both sides). Cr-Cr (VII) and Cr-Cr-O (VIII) can be created by removing 1.5 and 0.5 atoms respectively, from the Cr-Cr-3/2O (VI) first oxygen layer (3 and 1 atoms from both sides of the double cell). Finally, Cr-Cr-O2 (IX) and Cr-Cr-O3 (X) are generated by the symmetrical addition of 0.5 and 1.5 oxygen atoms to the (VI) $1^{st}$ oxygen layer. We should mention here that in Figure 5, the terminations are presented before ionic relaxations.

![](./images/813111048704884736_6.jpg)

Figure 5: Different terminations generated from the previous stoichiometric ones (II to V from I and VII to X from VI)

Relative surface energies are summarized in
Table 3.

<table>
<caption>Table 3 : Surface energies compared to the (I) one, N : number of $O_2$ molecule added/extracted per hexagonal cell.</caption>
<thead>
<tr>
<th colspan="2">Termination</th>
<th>Stoichiometry</th>
<th>N[$O_2$]</th>
<th>$\Delta$E (meV/Å²)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">$Cr-O_3-Cr$ (I)</td>
<td>$Cr_{12}O_{18}$</td>
<td>0</td>
<td>00</td>
</tr>
<tr>
<td rowspan="4">From Cr-O-Cr</td>
<td>$Cr-O_2-Cr$ (V)</td>
<td>$Cr_{12}O_{16}$</td>
<td>-1</td>
<td>202</td>
</tr>
<tr>
<td>$Cr-O_3-Cr-O_1$ (II)</td>
<td>$Cr_{12}O_{20}$</td>
<td>1</td>
<td>-50</td>
</tr>
<tr>
<td>$Cr-O_3-Cr-O_2$ (III)</td>
<td>$Cr_{12}O_{22}$</td>
<td>2</td>
<td>-27</td>
</tr>
<tr>
<td>$Cr-O_3-Cr-O_3$ (IV)</td>
<td>$Cr_{12}O_{24}$</td>
<td>3</td>
<td>-32</td>
</tr>
<tr>
<td colspan="2">$Cr-Cr-O_{3/2}$ (VI)</td>
<td>$Cr_{12}O_{18}$</td>
<td>0</td>
<td>80</td>
</tr>
<tr>
<td rowspan="4">From $Cr2-O_{3/2}$</td>
<td>Cr-Cr (VII)</td>
<td>$Cr_{12}O_{15}$</td>
<td>-3/2</td>
<td>321</td>
</tr>
<tr>
<td>$Cr-Cr-O_1$ (VIII)</td>
<td>$Cr_{12}O_{17}$</td>
<td>-1/2</td>
<td>135</td>
</tr>
<tr>
<td>$Cr-Cr-O_2$ (IX)</td>
<td>$Cr_{12}O_{19}$</td>
<td>1/2</td>
<td>21</td>
</tr>
<tr>
<td>$Cr-Cr-O_3$ (X)</td>
<td>$Cr_{12}O_{21}$</td>
<td>3/2</td>
<td>-20</td>
</tr>
</tbody>
</table>

The energy difference $\Delta E$ is obtained according to the following reaction/equation:
$$
\underbrace{\underbrace{Cr_{12}O_{18}}_{baresurface}}_{Cr-O3-Cr} + N \cdot O_2 \to \underbrace{Cr_{12}O_{(18+2N)}}_{surfaceoxygenated}
$$
$$
\Delta E = \left(E_{Cr_{12}O_{(18+2N)}} - E_{Cr_{12}O_{18}} - N \times E_{O_2}\right) / 2A
$$
where $A$ is the surface area and $N$ is the number of $O_2$ molecules added to (positive $N$ values) or subtract (negative $N$ values) from the slab. At zero temperature, the oxygen addition reactions on the chromium terminated surface (I) are always exothermic, see terminations II, III, and IV. The formation of terminations IX and X by addition of oxygen atoms to the termination VI (oxygen terminated $Cr_{12}O_{18}$ cell) is also exothermic with respect to this termination. Comparing to termination (I), the formation of termination IX is endothermic while the termination X formation is exothermic. On the other hand, the extraction of oxygen is a strongly endothermic process, whatever the termination considered.

Thermodynamic correction proposed by Reuter et al. [34] and Rohrbach et al. [16] have been added to take into account temperature and pressure effects. This formalism

has been already applied to many surfaces [12,35]. Here we present the final equations:

$$
R E(T)=R E(0)-\frac{N}{2 A}\left(\mu_{O_{2}}(T)-\mu_{O_{2}}(0)\right) \text { (1) }
$$

$$
R E(T)=R E(0)-\frac{N}{2 A}\left(\mu_{O_{2}}^{o}(T)-\mu_{O_{2}}^{o}(0)+k_{B} T \ln \left(\frac{P_{O_{2}}}{P^{o}}\right)\right) \text { (2) }
$$

Where $RE(T)$ is the relative surface energy with respect to the reference surface (Cr-O₃-Cr: Cr₁₂O₁₈).
At the equilibrium, the RE(T) equals zero and the equilibrium partial pressure can be expressed as a function of temperature :

$$
\ln \left(\frac{P_{O_{2}}^{e q}}{P^{o}}\right)=\frac{1}{k_{B} T}\left(\frac{2 A}{N} R E(0)-\left(\mu_{O_{2}}^{o}(T)-\mu_{O_{2}}^{o}(0)\right)\right) \text { (3) }
$$

The Equation (3) allows obtaining (P,T) phase diagram.

Plotting Equation (1) as a function of the oxygen chemical potential, allows us to evaluate the variation of the relative energy depending on experimental conditions, Figure 6.

![](./images/813111048704884736_7.jpg)

Figure 6: Relative energy surfaces as a function of the oxygen chemical potential. (i) solid line for terminations built from chromium terminated surface -Cr-O₃-Cr, (ii) dashed line for these built from oxygen terminated surface -Cr-Cr-O₃/₂.

Surfaces (I), (II), (VII) and (X) have been studied by Rohrbach et al. [16] using DFT + U. Both studies matches as (I) crosses (II) at μ-μ₀ = -1 eV and (II) and (X) intersect at μ-μ₀ = 0.5 eV. In the low oxygen partial pressure conditions (for low oxygen chemical potentials), the Cr-terminated Cr-O₃-Cr (I) is found to be stable.
When -1 < μ-μ₀ < 0.2 eV, the termination (II) is the most stable. Above μ-μ₀ = 0.2 eV (oxygen rich region), the termination (IV), which has not been proposed previously in the literature, is the most stable. We should mention that μ-μ₀ = 0 is the limit between Cr₂O₃ and CrO₂ phases, according to [16].
In order to have more familiar representation of surfaces stability diagrams we plot in the next figures the surface relative energies versus the oxygen partial pressure at different temperatures, according to equation 2.

![](./images/813111048704884736_8.jpg)

Figure 7: Relative energy as a function of pressure for the most stable terminations: a) 298.15 K, b) 600 K and c) 900 K. (i) solid line for terminations built from chromium terminated surface -Cr-O₃-Cr, (ii) dashed line for these built from oxygen terminated surface -Cr-Cr-O₃/₂.

At room temperature (Figure 7a), we notice that the oxygenated surface (II) Cr-O₃-Cr-O, chromyl, is the most

stable regardless of the $O_2$ partial pressure. This termination remains stable at 600K and 900K for partial pressure above $10^{-8}$ and $10^{-1}$ bars, respectively (Figure 7 b and c). Below these pressures the bare surface (I) is the most stable termination.

The domains of predominance of each termination are presented in the next (P,T) phase diagram, Figure 8.

![](./images/813111048704884736_9.jpg)

Experimentally, $\alpha$-Cr$_2$O$_3$ (0001) has been studied using LEED and STM. Maurice et al. [36] found a chromium-terminated surface using STM for an oxygen partial pressure of $10^{-11}$ bar at 825-925 K, which is consistent with the theoretical results. This observation is confirmed by Rohr et al. [37] (temperature between 780 and 1000 K and for a larger range of oxygen partial pressure). Dillmann et al. [38] found that heat treatments under an oxygen environment led to the formation of chromyl (O=Cr) on the Cr-terminated $\alpha$-Cr$_2$O$_3$(0001) surface. Bikondoa et al. [21] also demonstrated, using X-ray diffraction at room temperature, that in the ultrahigh vacuum the chromia surface exhibits a partially occupied double layer of Cr atoms. At oxygen partial pressure of $10^{-5}$ bar, the surface is terminated by chromyl species. The novelty of their work is that they propose surface stoichiometries, Cr$_{0.22}$-Cr$_{0.31}$-O$_3$ and O$_{0.38}$=Cr$_{0.38}$-O$_3$ which have not been predicted yet by theoretical calculations. However, as mentioned by Bikondoa et al. [21], it is difficult to reproduce vacancy formation in a periodic cell. It must be added that the experiments have been performed after annealing a high temperature 1200 K in UHV conditions which favor vacancy formation and important surface reconstructions.

Contrary to the case of hematite [12], the mono-oxygenated termination is thermodynamically stable and should be, with the bare surface, taken into consideration for further chromia reactivity studies. From this point of view, we treat in the next sections the addition of H$_2$ and H$_2$O to the bare surface (Cr-O$_3$-Cr) and chromyl surface (Cr-O$_3$-Cr-O).

### 3.3.3. Hydrogen adsorption on Cr-O3-Cr surface

We have seen that the chromia (0001) surface could be easily oxidized in presence of oxygen. We have seen also that the reduction by extracting oxygen atoms from the stoichiometric surfaces is not thermodynamically favoured.

However, the reduction may be done by adding reductants in the gas phase. We investigate here the reduction by hydrogenation according to the following reaction:

$$\text{Cr-O}_3\text{-Cr} + \text{n H}_2 = \text{Cr-O}_3\text{-H}_{2\text{n}}\text{-Cr} \tag{3}$$

The hydrogen atoms, created by the molecule dissociation, are bonded to the oxygen atoms of the second layer. Under a hydrogen environment, the chromia behaves very similarly to hematite [12], concerning rearrangement and reconstruction of the surface ( Figure 9).

![](./images/813111048704884736_10.jpg)
Figure 9: Optimized geometries with a) one, b) two and c) three hydrogen atoms adsorbed on the chromium-terminated surface.

The first hydrogen molecule addition (Cr-O$_3$-H-Cr: $E_{\text{ads}}$ = 0.22 eV per hydrogen atom, $E_{\text{ads}} = E_{(\text{molecule+surface})} - E_{(\text{molecule})} - E_{(\text{surface},)}$) and the second addition (Cr-O$_3$-H$_2$-Cr: $E_{\text{ads}}$ = 0.50 eV per hydrogen atom) are endothermic but the addition of the second molecule breaks a bond between the chromium atom of the fourth layer an oxygen atom located on the second layer. The formed OH group is moved outward and is located on the level of external chromium atom. The addition the following hydrogen atom (Cr-O$_3$-3H-Cr: 0.29 eV per hydrogen atom) displace the OH groups on the surface. Actually, by adding progressively 1, 2 and 3 hydrogen atoms to the oxygen of the second layer that increases the insulation of the external chromium atom reducing it, at the end, to a Cr(0). Obviously, such a degree of oxidation is not stable and the system tends to push out the hydroxides allowing progressively the external chromium atom to create bonds with the internal layer and having three Cr(II) atoms. We should note that these hydrogen adsorptions are endothermic, Table 4.

Table 4: Energies hydrogenated terminations, N: number of hydrogen molecules added per hexagonal cell.

<table>
  <thead>
    <tr>
      <th>Termination</th>
      <th>Stoichiometry</th>
      <th>N</th>
      <th>$\Delta$E (meV/$\mathring{\text{A}}^2$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cr-O$_3$-Cr</td>
      <td>$Cr_{12}O_{18}$</td>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>Cr-O$_3$-H-Cr</td>
      <td>$Cr_{12}O_{18}H_2$</td>
      <td>1</td>
      <td>10.57</td>
    </tr>
    <tr>
      <td>Cr-O$_3$-2H-Cr</td>
      <td>$Cr_{12}O_{18}H_4$</td>
      <td>2</td>
      <td>46.83</td>
    </tr>
    <tr>
      <td>Cr-O$_3$-3H-Cr</td>
      <td>$Cr_{12}O_{18}H_6$</td>
      <td>3</td>
      <td>40.92</td>
    </tr>
  </tbody>
</table>

The thermodynamic extrapolation confirms the fact that these adsorptions cannot take place at any higher temperatures. This confirms the fact that unlike hematite, the chromia surfaces favors the oxidation over the reduction.

### 3.3.4. Water adsorption on the bare surfaces

Both chromium-terminated ($\text{Cr-O}_3\text{-Cr}$ : I) and oxygen-terminated ($\text{Cr-Cr-O}_{3/2}$ : VI) surfaces have been used to investigate water adsorption and to build different terminations. On the oxygen terminated surface, the dissociative adsorption of 0.5 and 1.5 molecules per side (i.e. one and three $\text{H}_2\text{O}$ in the double cell, the molecules are adsorbed on both sides) was investigated, see Figure 10.

![](./images/813111048704884736_11.jpg)

Figure 10: Dissociative addition on the oxygen terminated surface; a)
1.5 molecule per side $-\text{Cr-Cr-O}_3\text{-H}_3$, b) 0.5 molecule per side $-\text{Cr-Cr-}\text{O}_2\text{-H}$.

![](./images/813111048704884736_12.jpg)

Figure 11: One, two and three water molecules added to chromium termination: the first (a) is added dissociatively [$-\text{Cr-O}_3\text{-H-Cr-OH}$] whereas the second (b) [$-\text{Cr-O}_3\text{-H-Cr-OH-H}_2\text{O}$] and the third (c) [$-\text{Cr-}\text{O}_3\text{-H-Cr-OH-(H}_2\text{O)}_2$] are added associatively.

Relative energies at 0K are presented in Table 5, and extended to 298K, 600K and 900K in Figure 13a,b, Figure 13c and Figure 13d respectively.

<table>
  <thead>
    <tr>
      <th colspan="2">Termination</th>
      <th>Stoichiometry</th>
      <th>N</th>
      <th>$\Delta\text{E}$: $\text{meV/Å}^2$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">From $\text{Cr-O-Cr}$</td>
      <td>$\text{Cr-O}_3\text{-Cr}$</td>
      <td>$\text{Cr}_{12}\text{O}_{18}$</td>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>$\text{Cr-O}_3\text{-H-Cr-OH}$</td>
      <td>$\text{Cr}_{12}\text{O}_{20}\text{H}_4$</td>
      <td>2</td>
      <td>-39.2</td>
    </tr>
    <tr>
      <td>$\text{Cr-O}_3\text{-H-Cr-OH-H}_2\text{O}$</td>
      <td>$\text{Cr}_{12}\text{O}_{22}\text{H}_8$</td>
      <td>4</td>
      <td>-91.1</td>
    </tr>
    <tr>
      <td>$\text{Cr-O}_3\text{-H-Cr-OH-2(H}_2\text{O)}$</td>
      <td>$\text{Cr}_{12}\text{O}_{24}\text{H}_{12}$</td>
      <td>6</td>
      <td>-132.</td>
    </tr>
    <tr>
      <td rowspan="3">From $\text{Cr2-O}_{3/2}$</td>
      <td>$\text{Cr-Cr-O}_{3/2}$</td>
      <td>$\text{Cr}_{12}\text{O}_{18}$</td>
      <td>0</td>
      <td>80.0</td>
    </tr>
    <tr>
      <td>$\text{Cr-Cr-O2-H}$</td>
      <td>$\text{Cr}_{12}\text{O19H}_2$</td>
      <td>1</td>
      <td>9.77</td>
    </tr>
    <tr>
      <td>$\text{Cr-Cr-O3-H3}$</td>
      <td>$\text{Cr}_{12}\text{O}_{21}\text{H}_6$</td>
      <td>3</td>
      <td>-99.4</td>
    </tr>
  </tbody>
</table>
Table 5: Relative surface energies. N: number of water molecules added per hexagonal cell.

Our calculations (Table 5) show that at zero temperature the water adsorption on chromium terminated surface is always exothermic (thermodynamically favoured) while on the oxygen terminated surface only the formation of fully hydroxylated surface, $\text{Cr-Cr-O}_3\text{-H}_3$, is exothermic.

D. Costa et al. [17] investigated the water adsorption on Cr-O-Cr surface. They predicted that the dissociative and associative addition of the first water molecule are energetically quasi degenerated (-82.2 and -82.6 kJ/mol respectively in 1x1 hexagonal cell). In our calculations only dissociative adsorption has been found as energy minimum on this surface, with -80.3 kJ/mol as adsorption energy. We should mention the difference in several calculation parameters used in this work and these used by Costa et al., particularly the functional (PBE here vs PW91 in [17]). The second adsorption happens associatively rather than dissociatively (with $\Delta\text{E}_{\text{ads}}$ of -93.3 kJ/mol per water molecule) with an energy difference smaller than 1.0 kJ/mol between the two adsorption modes. The third adsorption is also associative with $\Delta\text{E}_{\text{ads}}$ of -90.2 kJ/mol per water molecule. In summary, our calculations predict single water molecule dissociation on the chrome terminated surface against two dissociations predicted in [17]. However, this difference in predictions should not be considered as a real disagreement since, in our calculations, the associative and dissociative adsorptions of the second molecule are almost energetically degenerated and may be present at the same time on the surface.

The adsorption on the oxygen-terminated ($\text{Cr-Cr-O}_{3/2}$) surface always takes place dissociatively, in our knowledge these terminations have not been modelled elsewhere yet.

![](./images/813111048704884736_13.jpg)

Figure 12: Stability diagram of different hydrated surface across water chemical potential. (i) solid line for terminations built from chromium terminated surface $\text{-Cr-O}_3\text{-Cr}$, (ii) dashed line for these built from oxygen terminated surface $\text{-Cr-Cr-O}_{3/2}$.

Figure 12 shows that three surfaces are thermodynamically stable depending on the water chemical potential: from poor, through moderately rich to very rich regions the most stable terminations are bare surface ($-\text{Cr-O}_3\text{-Cr}$), fully hydroxylated surface ($-\text{Cr-Cr-O}_3\text{-H}_3$) and fully hydrated surface ($-\text{Cr-O}_3\text{-H-Cr-OH(H}_2\text{O)}_2$), respectively. We should note that, given the fact that in absence of water the bare surface is chromium terminated ($-\text{Cr-O}_3\text{-Cr}$), the formation of $-\text{Cr-Cr-O}_3\text{-H}_3$ surface (built from oxygen-terminated)

should require particular conditions (allowing cation migration end/or surface reorganization). In another words, we may expect the evolution of the surface termination while increasing the water partial pressure to be as in the inset to Figure 12 (the zoomed region) : bare surface (-Cr-$\mathrm{O_3}$-Cr), double hydrated surface (-Cr-$\mathrm{O_3}$-H-Cr-OH($\mathrm{H_2O}$)$_1$) and fully hydrated surface (-Cr-$\mathrm{O_3}$-H-Cr-OH($\mathrm{H_2O}$)$_2$), respectively. These terminations are also plotted in Figure 13b.

![](./images/813111048704884736_14.jpg)

Figure 13: Stability diagram of different hydrated surfaces at a) 298.15 K, b) zoom 298.15 K, c) 600K and d) 900 K. (i) solid line for terminations built from chromium terminated surface -Cr-$\mathrm{O_3}$-Cr, (ii) dashed line for these built from oxygen terminated surface -Cr-Cr-$\mathrm{O_{3/2}}$.

At room temperature (Figure 13a) the adsorption of water is thermodynamically favored, the number of water molecules per cell being 1, 1.5, 2 or even 3. The fully hydroxylated surface (-Cr-Cr-$\mathrm{O_3}$-$\mathrm{H_3}$, obtained from adsorption of 1.5 water molecules per side on the oxygen terminated surface, -Cr-O-Cr-$\mathrm{O_{3/2}}$) is the most stable termination for partial pressures lower than 3 bars. At 600K (Figure 13c) the bare chromium terminated surface is the most stable for partial pressures lower than $3.10^{-3}$ bar where it crosses the Cr-Cr-$\mathrm{O_3}$-$\mathrm{H_3}$ surface, which becomes the most stable for higher pressures. When the temperature exceeds 900K, the bare chromium terminated surface remains thermodynamically the lowest termination, even for relatively high water partial pressure (Figure 13d).

The domains of predominance of each termination are presented in the next (P,T) phase diagram, Figure 14.

![](./images/813111048704884736_15.jpg)

Figure 14: a) (P,T) phase diagram of chromia in presence of $\mathrm{H_2O}$ and b) a zoom to show the narrow domain of (-Cr-$\mathrm{O_3}$-H-Cr-OH($\mathrm{H_2O}$)$_1$) predominance.

At this stage, our predictions nicely agree with the proposition made by Henderson and Chambers based on TPD, HREELS and XPS analysis of a $\alpha$-$\mathrm{Cr_2O_3}$(0001) thin film grown on $\alpha$-$\mathrm{Al_2O_3}$(001) and $\alpha$-$\mathrm{Fe_2O_3}$[19]: they suggest that the first water molecule adsorption on the $\alpha$-$\mathrm{Cr_2O_3}$(0001) surface should take place dissociatively whereas the second adsorption should be associative. This suggestion is consolidated by Ahmed *et al.* results [15] in which the surface structure of $\alpha$-$\mathrm{Cr_2O_3}$(0001) of an oriented single crystal as a function of water partial pressure at room temperature has been investigated using Surface X-Ray Diffraction (SXRD). They concluded that at room temperature and 30 mbar a single $\mathrm{OH/H_2O}$ specie is found bonded a top of each surface chrome atom. In both studies [15] and [19] there is no evidence of the existence of fully hydroxylated surface such (-Cr-Cr-$\mathrm{O_3}$-$\mathrm{H_3}$) predicted here.

On the other hand, Maurice et al. [39] investigated the surface of few monolayer thick anhydrous films of $\alpha$-$\mathrm{Cr_2O_3}$(0001), epitaxially grown on Cr(110) single-crystal surfaces and exposed to water vapour at 300 K, using XPS, TDS, LEED and STM. The main observations were : (i) the oxidation of more Cr(0) into Cr(III) resulting in an increase of the thickness of the film by 0.5-1 monolayer, (ii) a disordered and corrugated surface is produced by hydroxylation which suggests significant OH-induced surface diffusion and rearrangement of the surface cation and anion planes and (iii) the formation of fully hydroxylated surface which is in agreement with the surface (-Cr-Cr-O3-H3) predicted here as the most stable one.

In order to reconcile these experimental results ([39] vs [15] and [19]), our understanding is that the difference is due to the thickness of the substrate and the Cr chemical potential in these three systems. As mentioned earlier, the formation of fully hydroxylated surface (-Cr-Cr-$\mathrm{O_3}$-$\mathrm{H_3}$) by direct hydration of the bare surface (Cr-$\mathrm{O_3}$-Cr) is expected to be very expensive energetically (requiring cations migration and/or surface reorganization). Such a cation migration and surface reorganization seems to be allowed in Maurice et al. experiment [39] thanks to the thickness (<1.5 nm) of their film and its contact with a Cr(0) "reservoir", while in the other experiments the samples were too thick (50 nm [19] and single crystal [15] ) without any Cr(0) "reservoir".

### 3.3.5. Hydrogen adsorption onto chromyl surface

As we have seen earlier, the formation of chromyl termination (-Cr-O₃-Cr-O) is thermodynamically very favorable: at room temperature, it remains stable even for oxygen partial pressure lower than 10⁻¹⁰ bar. In this surface, the external chromium atom is formally fivefold oxidized, Cr(V), whereas the internal chromium atoms are Cr(III). Further oxidation of this surface seems to not be thermodynamically favored; the addition of a second oxygen molecule is endothermic. We can wonder about the existence of a stable surface with an intermediate oxidation degree.

To address this issue, we have studied the reactivity of chromyl surface with respect to hydrogen as we have done with bare surface, by adding hydrogen atoms to the chromyl (formation of hydroxyl termination). The two following reactions have been investigated:

$$\mathrm{R-O + 0.5H_2 \leftrightarrow R-OH} \tag{4}$$

$$\mathrm{R-O + H_2 \leftrightarrow R-H_2O} \tag{5}$$

These two reactions lead to a hydroxide-terminated surface and a hydrated surface respectively. The reaction energies of both reactions at 0K are shown in Table 6.

**Table 6 : Reaction energies; N: number of gas molecules added per hexagonal cell.**
<table>
  <thead>
    <tr>
      <th>Reactions ($R$: stands for $\mathrm{Cr_{12}O_{18}}$)</th>
      <th>N[Gas]</th>
      <th>$\Delta\mathrm{E}\ (\mathrm{meV/\mathring{A}^2})$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$I: \ R+\frac{1}{2}O_2 \to R-O$</td>
      <td>1</td>
      <td>-50</td>
    </tr>
    <tr>
      <td>$II: \ R-O+\frac{1}{2}H_2 \to R-OH$</td>
      <td>1</td>
      <td>-74</td>
    </tr>
    <tr>
      <td>$III: \ R-O+H_2 \to R-H_2O$</td>
      <td>2</td>
      <td>-92</td>
    </tr>
  </tbody>
</table>

Under these conditions (0K) we notice that all these reactions are energetically possible. After some thermodynamic extrapolations one obtains:

![](./images/813111048704884736_16.jpg)

![](./images/813111048704884736_17.jpg)

**Figure 15: The Gibbs energies of different reactions.**

At room temperature both hydrogenations can take place. At very low hydrogen partial pressure ($<10^{-8}$) one forms a hydroxide termination while for higher pressure the adsorption of one hydrogen molecule per cell side becomes more favored leading to an earlier seen termination: the Cr-O₃-H-Cr-OH is identical to the one obtained by dissociative addition of one water molecule on chromia bare surface (see Figure 11a). When the temperature increases the simply hydroxide terminated surface (Cr-O₃-Cr-OH, obtained from reaction II) becomes the only stable one over almost all the pressure range. At 1200K, this termination is not stable for hydrogen pressure lower than 10⁻⁶ bar. We should remember that the chromyl termination itself is not stable either in such conditions. In another words, in presence of hydrogen, the chromyl surface turns to Cr(IV) instead of Cr(V) and then to Cr(III) when the temperature becomes very high (>1200K). The overall message from this is that the surface seems to be more stable when the external chromium atom is fourthly oxidized Cr(IV). However, such an oxidation degree is expected to be easier obtained by reducing Cr(V) rather than by oxidizing Cr(III).

These data strengthen the agreement with the earlier cited experimental observations, about the stability of the hydroxide terminations.

### 3.3.6. Water adsorption onto chromyl surface.

We have seen earlier that the bare surface has a relatively strong "Lewis acidity" character, since it interacts strongly with water molecules. The variation of the acid character due to the formation of chromyl could be legitimately questioned. We investigate here the hydration of chromyl surface. Both associative and dissociative adsorptions on chromyl surface have been studied. Although different initial geometries have been tested for the dissociative adsorption, the calculations converge always to a (-Cr-O₃-H-Cr-O₂-H) termination in which the two external oxygen atoms are bonded to each other, d₀₋₀=1.484Å, see Figure 16b.

![](./images/813111048704884736_18.jpg)

Figure 16: water adsorption on chromyl surface: a) associative and b) dissociative.

In our calculations, at 0K temperature, the energies of associative and dissociative adsorptions are $-19.2$ meV/Å² and $49.2$ meV/Å² respectively. In another words, the dissociative water adsorption on the chromyl surface is thermodynamically impossible. At this point, our calculations are in good agreement with the Henderson *et al.* conclusions about the absence of dissociative adsorption of water on chromyl surface [19]. However, according to our calculations the associative adsorption should be thermodynamically possible until 200 K and water partial pressure over $10^{-2}$ bar. This stability is lower than the one observed by Henderson *et al.* where the associative adsorption remains possible for temperatures lower than 380 K.

## Conclusion
In the present work, the structure and thermodynamic stability of (0001) $\alpha$-Cr₂O₃ surfaces, as a function of the temperature and the coverage/partial pressures in oxygen, hydrogen and water, have been investigated within the DFT + U approach.
According to the thermodynamic diagrams, below 600 K, the adsorption of oxygen is favored whatever the oxygen partial pressure, leading to the formation of a Cr-O₃-Cr-O chromyl termination. At 600 K, this termination becomes stable only in the oxygen rich region. For low oxygen partial pressures, the Cr-terminated surface, Cr-O₃-Cr, remains the most stable one. At higher temperature (> 1200 K), whatever the oxygen pressure is, the only stable termination surface is Cr-O₃-Cr. Adsorption of hydrogen on bare surface is not thermodynamically favoured. Nevertheless, it does adsorb on chromyl terminated surface to form a very stable hydroxide termination. Concerning steam, its adsorption is not thermodynamically stable above 900 K. In the 300-900 K range, hydrated surfaces have to be considered, and a new termination Cr-Cr-O₃-H₃ was identified as the most stable one. The two outermost chromium atoms will be saturated with OH groups, decreasing the acidic (Lewis) character of the surface. In this case, hydrogen bonds will play a major role on the surface chemistry. The Cr-Cr-O₃-H₃ surface will be the most stable in large part of the RCS under severe accident conditions with a gas mixture rich in steam. The presence of air in the gas phase and a moderate pressure will favour the formation of a chromyl termination, with the possible formation of OH groups on the surface for a gas mixture of steam/air/hydrogen. In a broader context, considering the stable surfaces found in the present work should be a relevant choice to investigate adsorption and catalytic processes over Cr₂O₃-based materials.

## Acknowledgments
Numerical results presented in this paper were carried out using the HPC resources from GENCI-IDRIS (Grant 2014 - project number x2014086731) and the regional computational cluster supported by Université Lille 1, CPER Nord-Pas-de-Calais/CRDER, France Grille CNRS and Feder, to whom we address our acknowledgements. This work has been supported by the French State under the program "Investissements d'Avenir MiRE managed by the ANR under grant agreement ANR-11-RSNR-0013-01.

## References
[1] G.A. Somerjai (Ed.), Introduction to Surface Chemistry and Catalysis, Wiley, New York, 1994.
[2] M.P. McDaniel, Adv. Catal. 33 (1985) 47.
[3] M.W. Mensch, C.M. Byrd, D.F. Cox, Catal. Today 85 (2003) 279.
[4] P. Marcus, V. Maurice, Passivity of metals and alloys (Corrosion and Environmental Degradation (Materials Science and Technology, A Comprehensive Treatment) vol 19 (2000) ed M Schütze (Weinheim: Wiley-VCH)
[5] P. Marcus, Corrosion Mechanisms in Theory and Practice, Second ed., Marcel Dekker Inc., New York, 2002.
[6]A. Vesel, M. Mozetic, A. Drenik, N. Hauptman, M. Balat- Michelin, Appl. Surf. Sci. 255(5) (2008) 1759..
[7] N. Zacchetti, S. Bellini, A. Adrover, M. Giona, Materials at high temperatures 26 (2009) 31.
[8] J.-H. Liu, R. Mendonça, R.-W. Bosch, M.J. Konstantinovic, J. Nucl. Mater. 393 (2009) 242.
[9] M. Fulger, M. Mihalache, D. Ohai, S. Fulger, S. C. Valeca, J. Nucl. Mater. 415 (2011) 147.
[10] A.-S. Mamede, Nicolas Nuns, A.-L. Cristol, L. Cantrel, S. Souvi, S. Cristol, J.-F. Paul, App. Surf. Sci.369 (2016) 510.
[11] K. Segerdahl, J.-E. Svensson, M. Havarsson, I. Panas, L.G. Johansson, Materials at high temperature 21(3) (2005) 69.
[12] S.M.O. Souvi, M. Badawi, J.-F. Paul, S. Cristol, L. Cantrel, Surf. Sci. 610 (2013) 7.
[13] N. J. Mosey, E. A. Carter, Phys. Rev. B 76 (2007) 155123
[14] X.-G. Wang, J.R. Smith, Phys. Rev. B 68 (2003) 201402.
[15] M. H. M. Ahmed, X. Torrelles, J.P.W. Treacy, H. Hussain, C. Nicklin, P. L. Wincott, D. J. Vaughan, G. Thornton, R. Lindsay, J. Phys. Chem. C 119 (2015) 21426.
[16] A. Rohrbach, J. Hafner, G. Kresse, Phys. Rev. B 70 (2004) 125426.
[17] D. Costa, K. Sharkas, M.M. Islam, P. Marcus, Surf. Sci. 603 (2009) 2484.
[18] D. Costa, P. Marcus, Surf. Sci. 604 (2010) 932.
[19] M. A. Henderson, S. A. Chambers, Surf. Sci. 449 (2000) 135.
[20] T. C. Kasper, S. E. Chamerlin, S. A. Chambers, Surf. Sci. 618 (2013) 159.
[21] O. Bikondoa, W. Moritz, X. Torrelles, H. J. Kim, G. Thornton, R. Lindsay, Phys. Rev. B 81 (2010) 205439.

[22] Jinglian Fan, Yongxiang Cheng, Zunyun Xie, Lingyun Jin, Gengshen Hu, Jiqing Lu, Mengfei Luo, Yuejuan Wang, Phys. Status Solidi A, 210 (2013) 1920.

[23] P. Hohenberg, W. Kohn, Phys. Rev. 136 (1964) B864.

[24] W. Kohn, L.J. Sham, Phys. Rev. A 140 (1965) A1133.

[25] P.E. Blochl, Phys. Rev. B 50 (1994) 17953.

[26] G. Kresse, J. Joubert, Phys. Rev. B 59 (1999) 1758.

[27] J. Hafner, Comput. Chem. 29 (2008) 2044.

[28] G. Kresse, J. Hafner, Phys. Rev. B 47 (1993) 558.

[29] G. Kresse, J. Furthmüller, Comput. Mater. Sci. 6 (1996) 15.

[30] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865-3868.

[31] M. Methfessel, A.T. Paxton, Phys. Rev. B 40 (1989) 3616.

[32] A. I. Liechtenstein, V. I. Anisimov and J. Zaane, Phys. Rev. B 52, (1995) R5467.

[33] L. Finger and R. Hazen, J. Appl. Phys. 51, (1980) 5362.

[34] K. Reuter, M. Scheffler, Phys. Rev. B, 65 (2002) 035406.

[35] A. Tougerti, C. Méthivier, S. Cristol, F. Tielens, M. Che, X. Carrier, Phys. Chem. Chem. Phys. 13, (2011) 6531.

[36] V. Maurice, S. Cadot, P. Marcus, Surf. Sci. 458 (2000) 195.

[37] F. Rohr, M. Baumer, H.-J. Freund, J.A. Meijias, V. Staemmler, S. Muller, L. Hammer, and K. Heinz, Surf. Sci. 372 (1997) L291.

[38] B. Dillmann, F. Rohr, O. Seiferth, G. Klivenyi, M. Bender, K. Homann, I.N. Yakovkin, D. Ehrlich, M. Baumer, H. Kuhlenbeck, H.-J. Freund, Faraday Discuss. 105 (1996) 295.

[39] V. Maurice, S. Cadot, P. Marcus, Surf. Sci. 471 (2001) 43.