# Adsorption of argon on pure silica MEL. Volumetric experiments and grand canonical Monte Carlo simulations

Vicente Sánchez-Gil $^{a}$ , Eva G. Noya $^{a, *}$ , José María Guil $^{a}$ , Enrique Lomba $^{a}$ , Susana Valencia $^{b}$

$^{a}$ Instituto de Química Física Rocasolano, CSIC, Serrano 119, E-28006 Madrid, Spain
$^{b}$ Instituto de Tecnología Química (UPV - CSIC), Avda. de los Naranjos s/n, E-46022 Valencia, Spain

---

## ARTICLE INFO

**Article history:**
Received 7 August 2015
Received in revised form
16 October 2015
Accepted 20 October 2015
Available online 27 October 2015

**Keywords:**
Adsorption
Zeolites
Ar
MEL
Molecular simulation

---

## ABSTRACT

The adsorption isotherm of argon on the zeolite MFl at liquid nitrogen temperature exhibits a sub-step at high loading before saturation that, in spite of much theoretical and experimental effort, is still lacking a definitive microscopic interpretation. In this work, we try to get insight into this peculiar behaviour by investigating the adsorption of argon on MEL, a zeolite that is structurally very similar to the MFI. First, we performed volumetric experiments that confirm that the adsorption of argon on MEL presents the same qualitative behaviour as on the MFI, again a sub-step appearing at high loading before saturation. Subsequently, the microscopic origin of this behaviour was investigated by means of molecular simulation. The simulations indicate that, for loads lower than that of the experimental sub-step, argon atoms can accommodate at low energy positions within the zeolite pores, whereas, above this point, some reordering of the adsorbate is needed to host further argon atoms. Moreover, the flexibility of the zeolite can have a significant impact on the shape of the adsorption isotherm, although the magnitude of this change depends on the zeolite model potential.

---

## 1. Introduction

The adsorption of simple gases on the zeolite silicalite-1 (pure silica MFI) has attracted considerable attention over the last three decades. This is mainly motivated by the observation that some of them, such as argon, krypton and nitrogen, exhibit one or several sub-steps in the adsorption isotherm at liquid nitrogen temperature [1-3]. Interestingly, the appearance of the sub-step can coincide with an exothermic signature in the heat of adsorption, as in the case of argon, or an endothermic one, as for krypton [1,2]. This suggests that the microscopic origin of the sub-step might be different in these two cases.

For argon, the adsorption isotherm exhibits one step at loadings from about 20 to 25 atoms per unit cell [1,4]. Two main hypothesis have been put forward to explain the origin of this behaviour. According to the first one, the sub-step appears as a result of a liquid-solid-like transition of the adsorbate induced by the confinement [1]. This possibility is supported by the emergence of a number of high intensity peaks on the neutron diffraction patterns after the sub-step. Other authors argue that the sub-step is caused by a structural change of the zeolite [5]. The MFI zeolite is known to undergo reversible structural changes upon increasing the temperature or by adsorption of big aromatic molecules. Specifically, at low temperature the MFI adopts a monoclinic structure [6] which, above 380 K, transforms into an orthorhombic cell with group symmetry $Pnma$ [7] or, upon the adsorption of p-xylene, into the so-called PARA configuration with group symmetry $P2_12_12_1$ [8]. The splitting of some diffraction peaks after the sub-step might be indicative of such zeolite structural change [9,10].

Simulations using different argon models (including even three-body contributions [11]) and keeping the zeolite framework rigid, were not able to quantitatively reproduce the experimental adsorption behaviour. In some cases, they yield smooth isotherms without any sub-step and, in other cases, they predict a jump in the adsorption, but at pressures several orders of magnitude higher than in experiments [5,10,12]. Furthermore, simulated diffraction patterns were not able to reproduce the appearance of all the experimental peaks after the step. This could mean that the adsorbate is less ordered in the simulations than in the experiments. However, it could also be indicating a zeolite structural

---

* Corresponding author.
E-mail addresses: eva.noya@iqfr.csic.es, eva.noya@gmail.com (E.G. Noya).

http://dx.doi.org/10.1016/j.micromeso.2015.10.023
1387-1811/© 2015 Elsevier Inc. All rights reserved.
© 2015 Elsevier Inc. All rights reserved.

![](./images/814583254182002688_1.jpg)
![](./images/814583254182002688_2.jpg)
![](./images/814583254182002688_3.jpg)

change, a feature that, obviously, cannot be captured by simulations using a rigid framework. More recently, García-Pérez et al. [4] revisited these simulations, but explicitly incorporating the flexi- bility of the zeolite, an effect that had long been neglected in pre- vious studies. This approach led to a more faithful description of the adsorption isotherm, from which the authors concluded that the sub-step was due to a combined effect of a structural change of the zeolite and of the adsorbate. However, a detailed description of those atomic structural changes is still lacking.

In this work, we will further investigate this phenomenon from a different perspective, which is by focussing on the related pure silica MEL zeolite, structurally very similar to the MFI but some- what simpler (see Fig. 1). In particular, the MFI framework consists of parallel straight cylindrical pores that are intersected by sinu- soidal channels, exhibiting four of that intersections per unit cell. The MEL zeolite exhibits a very similar structure, with the only difference being that in this zeolite all the channels are straight and, consequently, its unit cell has a higher symmetry (with space group I-4m2) [13]. In addition to that, there are experimental evidences that, similarly to MFI, MEL might also undergo a structural change upon increasing the temperature (at roughly 320 K) [14-16]. However, as far as we know, such structural transformation has not yet been fully characterized [13]. Given the structural similarity between both zeolites, it seems reasonable to think that both of them should exhibit a similar adsorption behaviour.

## 2. Experimental procedure

Measurements were performed on an expressly synthesized pure silica ZSM-11 sample. Details of the synthesis of the ZSM-11(Si) sample are reported elsewhere [17]. In a previous work, us- ing the "t"-method, we estimated that the micropore volume of the sample was $0.12~cm^{3}/g$ [17]. This value is agreement with the literature [18,19]. High purity Ar (99.999%, Air Liquide, Spain) was used as adsorbate.

### 2.1. Adsorption volumetry

In an adsorption experiment, small doses of Ar were succes- sively added at increasing pressures, measuring the increment of amount adsorbed to obtain the volumetric isotherm, $n^{\sigma}-p$. The amount adsorbed, $n^{\sigma}$, was determined in a volumetric apparatus, equipped with two pressure transducers (Baratron 310, MKS, USA) of 0-1.33 kPa and 0-133 kPa ranges, respectively. Dead volumes were determined by mercury weighting and helium expansions. Reproducibility in the measurement of amount adsorbed, deter- mined by successive helium expansions, was better than $0.2~\mu mol$.

![](./images/814583254182002688_4.jpg)

Fig. 1. Structure of the a) MEL and b) MFI zeolite frameworks. Two different views are shown for the MFI. The volume accessible to the argon atoms is shown in the bottom figures.

Before each experiment the samples were heated in oxygen flow, c.a. $30~cm^{3}/min$, up to 723 K, and kept at this temperature for4 h to eliminate any organic residue. After that, the sample was out- gassed overnight at 723 K in a vacuum better than 1 mPa. All ex- periments were carried out at 77 K with the sample cell immersed in a boiling liquid nitrogen bath. Bath temperature was determined with a home made oxygen vapour pressure thermometer. Second virial coefficient correction was applied to take into account the non-ideal behaviour of Ar vapour. For the case of argon this correction is negligible, but we still included it because it is our usual protocol for any adsorbent/adsorbate experiment. An exper- imental range of relative pressure, $p/p_{0}$, from $10^{-6}$ to 1 was covered in the measurements.

## 3. Modelling and simulation

### 3.1. Model potentials

In this work, interactions between argon atoms, and between argon and the zeolite, are described by the Lennard-Jones potential. The parameters for the argon-argon interaction are taken from Ref. [4], where they were fitted to the experimental liquid-vapour curve. The crossed argon-oxygen parameters were adjusted to reproduce the experimental adsorption isotherm, a usual approach in simulations of adsorption processes [4,20]. Given that silicon atoms are caged inside oxygen tetrahedra, only the oxygen atoms are considered when evaluating the van der Waals interactions between the adsorbate and the zeolite. Interactions with silicon atoms are thus implicitly incorporated in the crossed oxygen- -adsorbate interactions. The Ar-Ar and Ar-O parameters used in this work are summarized in Table 1.

As regards the zeolite intramolecular interactions, numerous model potentials can be found in the literature [21-27]. In this work, we focused on the popular models proposed by Demontis et al. [21] and by Nicholas et al. [22]. Our choice is motivated by a recent study that showed that both were able to reproduce reasonably well the experimental infrared spectra of a large variety of zeolites, including that of MEL [28]. In particular, the best results were obtained for the Nicholas model, that incorporates bonding, bending and torsional, as well as van der Waals and Coulombic non-bonded terms, and whose parameters were fitted to $ab$ initio and experimental data [22]. On the other hand, the Demontis model is rather simple, including only bonding terms between the O-O and Si-O atoms. Surprisingly, it was found to perform better than more sophisticated models, such as that proposed by Hill and Sauer [24]. The parameters for the Demontis model were fitted to experimental structural data and the infrared spectrum of zeolite LTA, but numerous studies have proven its transferability to study properties of other zeolites [28,29].

Besides using the original parameterization for these two models, we have also considered modified versions that, in what

Table 1
Parameters of the Lennard-Jones model used for the argon-argon and argon-zeolite interactions. For comparison, the parameters used in Ref. [4] to study the adsorption of argon on MFI are also provided.

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">MEL (This work)</th>
<th colspan="2">MFI (Ref. [4])</th>
</tr>
<tr>
<th>$\varepsilon/k_{B}$ (K)</th>
<th>$\sigma$ (Å)</th>
<th>$\varepsilon/k_{B}$ (K)</th>
<th>$\sigma$ (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ar-Ar</td>
<td>124.07</td>
<td>3.380</td>
<td>124.07</td>
<td>3.380</td>
</tr>
<tr>
<td>Ar-O</td>
<td>114.81</td>
<td>3.1265</td>
<td>107.69</td>
<td>3.150</td>
</tr>
</tbody>
</table>

follows, will be designated as Nicholas modified and Demontis modified models, respectively. In those modified potentials, the equilibrium bond distances and bending angles, instead of being assigned to constant values for all the bonded pairs and triplets as in the original parameterization, are taken from the experimental structural data of the zeolite under investigation [13]. Note that the nearest neighbours' bond distances and angles show some dispersion in the experimental unit cell. For example, for MEL, the probability distribution of the Si-O-Si bending angle is quite broad (see Table 2 and Fig. S1 in the Supplementary material). This modification of the zeolite models has been commonly used in previous simulation studies [30,31]. In the case of the Demontis model, this guarantees that the experimental structure corre- sponds to the energy minimum. This is not necessarily true for the Nicholas model as, in this case, there are also non-bonded terms that come into play. Indeed, simulations of the empty zeolite at77 K, using both the original and modified versions of Nicholas model, yield average energies lower than that of the frozen experimental structure. In particular, for the original model, the energy of the experimental structure was -89.40 kcal/mol, whereas the average energy at 77 K is -89.81 kcal/mol. Similarly, for the modified model, the energy of experimental structure is -89.83 kcal/mol, slightly higher than the average energy at77 K, -89.96 kcal/mol. In both cases, the Coulombic contribution to the energy is responsible for the experimental structure not lying at the energy minimum.

To further investigate the effect of the modification of the model parameters on the structure of the empty zeolite, we also calculated the pair distribution functions and the bending angle distributions. We found that the four considered models, namely, the original and modified versions of Nicholas and Demontis potentials, yield very similar pair distribution functions (data not shown). Larger differ- ences appear in the bending angle distributions (see Fig. S1 in the Supplementary material). In particular, for the Si-O-Si bending angle, the distribution is significantly broader for the original models than for the modified versions. This broadening is seem- ingly unrealistic when compared to the distribution functions calculated with the experimental structure, even when considering the possible effect of thermal disorder (see Fig. S1 in the Supplementary material). Focussing now on the differences be- tween both models, the Nicholas model tends to preserve more faithfully the experimental Si-O-Si angles, exhibiting two clear peaks at approximately $\theta_{Si-O-Si}=155^{\circ}$ and $\theta_{Si-O-Si}=170^{\circ}$ , the first peak having a shoulder at $\theta_{Si-O-Si}=145^{\circ}$ . On the other hand, the modified Demontis model shows a tendency to widen the Si-O-Si angles, favouring values larger than $160^{\circ}$ . This is simply due to the absence of constraints on these angles in this model.

### 3.2. Simulation details

The adsorption isotherms were numerically evaluated by means of Grand Canonical Monte Carlo (GCMC) simulations. The simula- tion box contained $2 \times 2 \times 3$ replicas of the zeolite unit cell. We considered two structures for the rigid zeolite: one of them ob- tained from a measurement at room temperature [13] (below the hypothetical structural transition at 320 K), and the second one measured at 363 K [14] (i.e., above the transition). Periodic boundary conditions were used along the three dimensions of space. Ar-Ar and Ar-O interactions were truncated and shifted at12 Å, whereas the zeolite-zeolite van der Waals and Coulombicnon-bonded terms of the Nicholas model were truncated at $8.85 \AA$ [22]. Long range contributions to the Coulombic interaction were evaluated using Ewald summation [32]. Typically, simulations consisted of about a million Monte Carlo (MC) cycles, plus another one hundred thousand for equilibration. We defined a MC cycle as250 particle insertion/deletion attempts, plus 250 particle move attempts. For those simulations that incorporate the zeolite flexi- bility, one cycle includes also one movement attempt for each atom of the zeolite. A larger number of MC cycles was used at loadings close to saturation than at low loadings.

Besides evaluating the number of adsorbed atoms as a function of the pressure (or chemical potential), we also calculated the isosteric heat of adsorption, that measures the enthalpy change when a molecule in the gas phase is adsorbed into the porous material. Several approaches can be used in simulations to deter- mine this quantity [33]. Here, we used the energy/particle fluctu- ations route, according to which the isosteric heat of adsorption iscomputed as:
$$q_{s t}=R T+\left\langle U_{g}\right\rangle-\frac{\langle U N\rangle-\langle U\rangle\langle N\rangle}{\left\langle N^{2}\right\rangle-\langle N\rangle^{2}}\qquad(1)$$
 where U is the total energy of the system (adsorbent plus adsor- bate), N is the number of particles, R is the gas constant and T the temperature. The brackets indicate an ensemble average over a GCMC simulation. Assuming ideal gas behaviour, the potential energy of the gas phase $U_{g}$ can be equated to zero in the previous expression for Ar atoms [33,34].

Information about the distribution of the adsorbed atoms on the channels of the zeolite was obtained by evaluating the density profile along the x and y directions of space (that are chosen to be parallel to the directions of the channels of the zeolites). Thisquantity is simply defined by:
$$p_{N}(x)=\frac{n_{A r}(x)}{\Delta x}\qquad(2)$$
 where $n_{A r}(x)$ is the number of argon particles with x-coordinate between x and $x+\Delta x$ , and analogously for the y direction.

## 4. Results

### 4.1. Experimental measurements

Two isotherms of Ar on pure silica MEL were measured at 77 K up to a relative pressure of unity, $p / p_{0}=1$ . They are Type I + IV isotherms: an initial abrupt uptake increase, followed by a right angle knee at very low relative pressures corresponding to the filling of the zeolite's micropores. Afterwards, a large plateau ap- pears, followed by a hysteresis loop in the $p / p_{0}$ range of 0.3-1 (this

Table 2 Equilibrium bond distances and bending angles for the zeolite model potentials considered in this work. For the modified versions of the models, bond distances and bending angles do not adopt constant values across the unit cell [13]. In this case, only the upper and lower bounds are provided.
<table><thead><tr><th></th><th>$d_{Si-O}(\hat {A})$</th><th>$d_{O-(Si)-O}(\hat {A})$</th><th>$d_{Si-(O)-Si}(\hat {A})$</th><th>$θ_{O-Si-O}(degrees)$</th><th>$θ_{Si-O-Si}(degrees)$</th></tr></thead><tbody><tr><td>Nicholas</td><td>1.61</td><td></td><td>3.1261</td><td>109.5</td><td>149.5</td></tr><tr><td>Nicholas mod.</td><td>1.565-1.623</td><td>_</td><td>3.033-3.164</td><td>106.3-112.7</td><td>144.9-172.5</td></tr><tr><td>Demontis</td><td>1.605</td><td>2.61786</td><td></td><td></td><td></td></tr><tr><td>Demontis mod.</td><td>1.565-1.623</td><td>2.563-2.655</td><td></td><td></td><td></td></tr></tbody></table>

zone not shown here); the latter indicates mesoporosity of wide diameter range in the zeolite intermicrocrystallite voids. Results at low relative pressures are presented in Fig. 2. Good reproducibility is seen when comparing both isotherms. The noise observed at very low coverage, in Henry's law region, is attributed to experimental dispersion. As a test of the experimental setup, we have also per- formed measurements for the MFI, for which there are abundant experimental data for comparison. As can be seen, our adsorption isotherm on MFI is in very good agreement with one of the most recently reported measurements [4]. On the other hand, for MEL, as far as we know, this is the first time that the adsorption isotherm for the whole range of pressures is provided. We are aware of only one previous measurement of Ar adsorption for ZSM-11 (whose composition was not pure silica) that was restricted to pressures below the sub-step that we observe at a loading of ~24 molec./u.c. [35]. As shown in Fig. 2, the adsorption behaviour of Ar on the two zeolites is very similar, both exhibiting a sub-step at high loadings before saturation. The only significant differences are that MEL absorbs up to about 15% more Ar than MFI, both at the sub-step and at saturation, and that the sub-step occurs at a pressure about one order of magnitude higher. These differences can be interpreted using a simple geometric argument, as the diameters of the chan- nels and intersections are somewhat larger in MEL than in MFI (5.19 Å and 7.72 Å for MEL and 4.46-4.70 Å and 6.36 Å for MFI), leading to a higher porous volume in MEL [36].

The fact that the same qualitative behaviour is found for both zeolites suggests a general mechanism that does not depend on the specific structural details of the pores. This is an interesting observation, as the origin of the sub-step at intermediate loading has often been attributed to the characteristic structure of the MFI framework with straight and sinusoidal channels [10,37]. Here, we show that this phenomenon can also appear in the absence of si- nusoidal channels.

### 4.2. Simulation results

The simulated adsorption isotherm of argon on MEL is compared to the experimental data in Fig. 3. The first observation is that simulations with a frozen framework are not able to quanti- tatively reproduce the experimental results. The simulated curve does not exhibit a clear sub-step at half loading. Instead, there is a change of slope at a loading of about ~24 argon atoms per unit cell, after which the argon uptake occurs continuously without more abrupt changes up to saturation. Besides, the curve is very similar both when using the zeolite atomic coordinates measured at room temperature [13] and at high temperatures [14] (see Fig. 3).

![](./images/814583254182002688_5.jpg)

Fig. 2. Experimental adsorption isotherm of Ar on MEL and MFI at 77 K. Results from Ref. [4] are also shown for comparison.

![](./images/814583254182002688_6.jpg)

Fig. 3. Simulated and experimental adsorption isotherms of Ar on MEL at 77 K.

Dubbeldam et al. [20] showed that the sub-steps in the adsorption isotherms are usually related to the accessibility of the adsorbate to different sites within the zeolite. As a consequence, their location, or even their appearance, can be tuned by modifying the size parameters of the crossed adsorbate-zeolite interactions. The energy strength can then be adjusted to match the experi- mental data at low loadings. Following these guidelines, we investigated the effect of the size parameter $\sigma_{Ar-O}$ on the adsorp tion isotherm of Ar on MEL. Although we did observe a certain dependence of the slope in the region from half to high loading on $\sigma_{Ar-O}$, an abrupt jump similar to that found in experiments was never obtained (see Fig. S3 in the Supplementary material). This is in line with the results obtained by García Pérez et al. [4], who also found that simulations with a frozen framework do not provide a satisfactory description of argon on the related MFI zeolite (either using the monoclinic or orthorhombic unit cells).

Our next step was then to incorporate the zeolite flexibility in the simulations. As can be seen in Fig. 3, the adsorption behaviour at low loadings and up to half loading (about 24 atoms per unit cell) is rather similar, regardless of whether the flexibility is included or not. However, in the region from half to high loading, all the flexible models predict a higher adsorption of argon than the rigid model at the same pressure. Note that the behaviour is also different depending on the model used to describe the flexibility of the zeolite.

Focussing first on the differences between the original and modified Nicholas models, both give rather similar results at low pressures. However, at a loading of about 24 molecules per unit cell, the uptake of argon with pressure becomes somewhat more moderate for the modified model, exhibiting a sub-step from about 30 to 37 atoms per unit cell. Comparing now these results to the experimental data, the shape of the sub-step for the modified Nicholas model is rather similar to the experimental one, although it appears at a loading significantly higher than in experiments.

Using a different functional form for the zeolite model has an even higher impact. Indeed, using the simpler modified Demontis model (whose geometric parameters are adjusted to the experi- mental structure of the MEL), the isotherm does not show any step at half loading, although, curiously, it quantitatively reproduces the experimental data, both at low loading and at saturation. Differ- ences in the adsorption behaviour depending on the zeolite model

have already been noted in previous studies (see, for example, Ref. [31]).

With the aim of trying to identify a possible structural change on the zeolite upon the adsorption of Ar in our simulations, we calculated the average positions of the framework atoms along simulations of the empty and full loaded zeolite. Comparison of those average structures by visual inspection showed only subtle differences between them (see Fig. S2 in the Supplementary material). However, a better way to characterize the adsorption properties of these two average structures is to evaluate their adsorption isotherms by GCMC simulations (keeping the average structures frozen). Then, if the average structure of the fully loaded zeolite is able to absorb significantly more than that of the empty one, this would indicate a structural change in the zeolite. The results of these simulations are shown in Fig. 4. Surprisingly, for the modified Nicholas model (Fig. 4, top panel), the adsorption isotherms for both average structures (empty and fully loaded) are almost indistinguishable from that for the flexible model. This, together with the fact that the experimental atomic MEL structure is not an energy minimum for the modified Nicholas model, suggests that the adsorption isotherm for this flexible model differs from that for the rigid zeolite (using the experimental atomic coordinates), not because of the incorporation of flexibility, but, instead, because it slightly deforms the zeolite structure, seemingly opening somewhat the pores. Completely analogous results were obtained for the original Nicholas model (data not shown).

![](./images/814583254182002688_7.jpg)

Fig. 4. Adsorption isotherms of Ar on MEL at 77 K obtained from simulations using average structures of the zeolite along simulations of the empty and full loaded zeolite. The top panel shows the results using the average positions for the modified Nicholas model and the low panel for the modified Demontis model.

By performing the same study for the modified Demontis model (for which the experimental structure corresponds to the minimum of energy by construction), a completely different scenario is obtained. In this case, the adsorption isotherms for the average structures of the empty and fully loaded zeolite are very similar to that obtained using the rigid experimental structure and, thus, different from that for the flexible zeolite. Contrary to the Nicholas model, the flexibility now plays an important role, changing the adsorption isotherm form above a loading of roughly 20 molec./u.c. However, the fact that the isotherm for the empty and fully loaded structures are almost indistinguishable, indicates that the atomic average positions are the same. This rules out the possibility of a structural transition upon the adsorption of Ar in the simulations with the modified Demontis model.

Taking all these results together, it is clear that none of the considered models is able to provide a full quantitative description of the experimental data. We think that this can be due both to a poor description of the flexibility of the zeolite upon the adsorption of the adsorbate, and to the need to improve the crossed Ar-zeolite interactions. In relation to the latter, even though MEL and MFI have the same chemical composition (pure silica), the parameters fitted in Ref. [4] to reproduce the experimental isotherm of Ar on MFI do not describe properly the adsorption on MEL at low pressures (see Fig. S3 in the Supplementary material). The fact that a different set of parameters has to be used for each of the zeolite models suggests that the functional form of the Lennard-Jones model does not reproduce properly the interaction between argon and the zeolite.

With the aim of providing a detailed description of the mechanism behind the simulated adsorption isotherms, we have analyzed the isosteric heat of adsorption and the distribution of the adsorbate atoms within the pores. To keep the discussion simple, we present only results for the rigid zeolite [13] and for the flexible zeolite described with the modified Demontis model, as this model predicts that flexibility plays an important role in the adsorption properties.

As can be seen in Fig. 5, the isosteric heat of adsorption is rather similar at low loadings regardless of whether the zeolite is rigid or flexible, increasing moderately with the amount of adsorbed argon up to a loading of about 24 molecules per unit cell. By looking at the different contributions to the isosteric heat of adsorption, we can

![](./images/814583254182002688_8.jpg)

Fig. 5. Isosteric heat of adsorption calculated for the rigid and the flexible zeolite modelled with the modified Demontis model. Full symbols and solid lines correspond to data from simulations for the flexible zeolite, whereas open symbols and dashed lines are for the rigid zeolite.

see that the Ar–Ar contribution increases in this region, simply because more Ar–Ar interactions come into play as the density of the adsorbate increases. On the other hand, the heat due to the Ar–zeolite contribution decreases, reflecting, in this case, that argon atoms occupy first the most energetically favourable positions within the zeolite pores and, once those are occupied, the new adsorbed atoms go to slightly less energetically favoured positions.

Visual inspection of the configurations reveals that, from very low loadings (~2–3 atoms per unit cell), argon atoms are found both at the channels and at the intersections. At a loading of ~24 atoms per unit cell, we found two atoms per channel and other two at the junctions (note that there are 8 channels and 4 junctions per unit cell). A typical snapshot of the system at this loading is shown in Fig. 6. The distribution of the atoms within the pores can be quantified by calculating the density profiles along the directions parallel to the channels (Eq. (2)). The profile along the x-direction, depicted in Fig. 6, is in agreement with the description just provided. It shows two peaks within the channels and a broader, more pronounced peak, at the positions of the intersections ($x \approx 0, 10$, 20, 30 Å). Note, however, that these peaks result from the addition of the contribution of the intersections as well as the perpendicular channels that run along the y-axis. As can be seen in Fig. 6, the distribution of the adsorbate is almost indistinguishable for the rigid and flexible zeolite cases.

The distribution of argon within the zeolite pores up to a loading of 24 molec./u.c. can be more clearly visualized in the probability map depicted in Fig. 7. This figure shows the Boltzmann factor ($\exp(-U/kT)$) for a probe argon atom at a $x-z$ cross section of the MEL zeolite. As can be seen, the most energetically favoured positions are located at the channels, with two sites with approximately the same probability per channel. In the junctions, there are another two regions with enhanced probabilities, located at the top and bottom edges, the Boltzmann factor diminishing considerably at the centre of the intersections. In all, there are 24 sites (2 in each of the 8 channels and another 2 in each of the 4 intersections) that exhibit a high occupation probability, so that the 24 first adsorbed molecules will go to sit preferentially around those locations. Given that those sites are sufficiently apart from each other, the argon atoms can be easily accommodated up to a loading of 24 atoms per unit cell, resulting in a net energy gain of the zeolite–argon system. At this loading, the isosteric heat presents a maximum that is coincident with a change of slope of the adsorption isotherm (see Fig. 3).

![](./images/814583254182002688_9.jpg)

Fig. 7. Boltzmann factor at a $x-z$ cross section intersecting the centre of the channels. The zeolite was kept frozen to build this map.

At higher loadings, differences between the results for the rigid and the flexible zeolite become evident, also in keeping with the distinct behaviour of the adsorption isotherm in this region. In the case of the rigid zeolite, the heat decreases for loadings higher than 24 atoms per unit cell. However, for the flexible zeolite, the curve remains roughly constant from about ~24 molec./u.c. to ~31 molec./u.c., after which undergoes a subtle drop. In the region between ~24 and ~28 atoms per unit cell, the different behaviour arises mainly from the Ar–zeolite contribution, as the Ar–Ar is rather similar for both the rigid and the flexible zeolite. The Ar–zeolite term undergoes a sudden decrease from ~24 to ~28 atoms per unit cell, this decrease being significantly more abrupt for the rigid zeolite. As can be seen in the probability map depicted in Fig. 7, once that 24 atoms per unit cell have been adsorbed, the unoccupied positions are no longer energetically favourable. As a result, the new argon atoms can only go to the available higher energetic positions (usually displacing a bit some of the previously loaded atoms to leave room for the extra load), causing the change of slope of the adsorption isotherm. Indeed, the distribution of argon atoms is rather similar when 24 or 28 argon atoms are adsorbed, the four extra atoms being placed at the intersections. The fact that the drop of the

![](./images/814583254182002688_10.jpg)

Fig. 6. Density profile of Ar in the zeolite MEL along the x-axis at different loadings at 77 K. Density profiles along the y-axis are identical and for that reason are not shown. The black line shows the results for the simulations using a rigid zeolite framework, whereas the red line corresponds to simulations with the flexible modified Demontis model. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

Ar–zeolite contribution is less pronounced for the flexible framework indicates that the atomic vibrations alleviate the energetic cost of inserting particles, i.e., subtle displacement of the atoms of the zeolite can lead to lower repulsions in the argon–zeolite interactions.

Beyond a loading of ~30 atoms per unit cell, differences between the rigid and the flexible zeolite extend also to the Ar–Ar contribution. Whereas this contribution starts to decrease at this point for the rigid zeolite, for the flexible framework it continues to increase up to a slightly higher loading (~32–33 molec./u.c.), after which it also drops. This is just reflecting that the vibration of the zeolite can also lead to lower repulsion between the adsorbate atoms at high loadings.

In spite of the different energetics of the adsorption process, the distribution of the argon atoms within the pores is rather similar for both the rigid and the flexible zeolite (see Fig. 6). At a load of ~30 molec./u.c., the density profile again shows two peaks at the channels (that become narrower and taller than at ~24 molec./u.c., as a result of the lower mobility of the adsorbate at higher loads), whereas the peaks corresponding to the intersections develop two lower peaks, one at each side. A typical configuration is depicted in Fig. 6.

This tendency to host the extra atoms in the intersections extends up to saturation. The density profile at a load of ~36 molec./u.c. exhibits peaks at the same positions as that for ~30 molec./u.c., although, obviously, these peaks become even narrower and taller for loads close to saturation, indicating that the adsorbed fluid presents a solid-like behaviour. At these high loadings, the atoms tend to adopt highly ordered configurations imposed by the geometry of the zeolite pores. Specifically, the argon atoms are distributed in zig–zag configurations along the channels and up to 6 atoms can be packed at each intersection (see Fig. 6). In this way, the MEL can host up to 40 atoms per unit cell. However, this very high load is only attained at unrealistically high pressures.

Curiously, the contribution to the isosteric heat arising from the zeolite flexibility is negligible at all coverages (only subtle oscillations are observed at high loading, a region more prone to statistical uncertainty). This means that the slight distortion of the zeolite framework to better accommodate the argon atoms occurs without a relevant energetic penalty. Note, however, that it is important to incorporate the flexibility, because it affects the Ar–Ar and Ar–zeolite contributions and, thus, the total isosteric heat, specially after the sub-step.

Focussing now on the differences between the structure of the adsorbed fluid, as mentioned before, the density profiles along the x-axis are rather similar for both the rigid and the flexible zeolite. Only minor changes are observed at the highest load, namely, ~36 molec./u.c.. In this case, the profile for the rigid zeolite exhibits somewhat sharper peaks, making evident the tighter confinement of the adsorbate when the adsorbent is kept frozen. Analysis of the Ar–Ar and Ar–O average pair distribution functions corroborate this view (see Fig. S4 in the Supplementary material). Those curves are again very similar in both cases, the largest differences appearing for the Ar–O distributions, as expected. The Ar–Ar functions are very similar at all loadings, except for a slight sharpening of the peaks at the highest loadings. All these results evidence that the incorporation of the zeolite flexibility does not lead to significant changes in the structure of the adsorbate.

Unfortunately, we could not measure the isosteric heat of adsorption experimentally, so that a comparison between simulations and experiments is not possible in this case. However, given the similar adsorption isotherms for MFI and MEL, it is expected that the isosteric heat will behave similarly in both systems. According to the experimental data reported in Ref. [5], the heat of adsorption remains constant up to a loading of about ~22–23 molec./u.c. At that point, it suffers a rather abrupt increase, after which it remains again constant up to a loading of about ~27–28 molec./u.c. Assuming that the isosteric heat of adsorption of Ar on MEL may well exhibit a similar behaviour, the results using the flexible zeolite should then provide a better description of the experimental data.

## 5. Conclusions and outlook

To summarize, in this work, we have measured the experimental adsorption isotherm of argon into MEL zeolite. We find a sub-step at a loading of ~24 argon molecules per unit cell, similar to that observed for the MFI framework (although, in this case, it appears at ~20 molec./u.c.). Our simulations indicate that the sub-step at half loading can simply originate from the occupation of different "energetic sites" within the pores. Initially, adsorbate atoms go to the most energetically favoured positions. Once all those sites are occupied, roughly at half loading, the new adsorbed argon molecules necessarily have to go to higher energy positions (often leading to small displacements of the already adsorbed atoms).

In addition, we have seen that the flexibility of the zeolite can have some influence on the energy of these less favourable sites and, as a consequence, also on the shape of the adsorption isotherm above half loading. However, different zeolite models attribute different relevance to flexibility. For the Nicholas model, flexibility does not seem to affect the adsorption isotherm. In this case, the experimental structure is not at the energy minimum and the zeolite structure is somewhat deformed. The change in the adsorption properties is a consequence of this deformation of the zeolite, not of having incorporated the zeolite flexibility. On the contrary, the simpler Demontis model (for which the experimental structure corresponds to an energy minimum by construction) predicts that the explicit incorporation of zeolite flexibility does change the shape of the adsorption isotherm. Finally, we have also found that the structure of the adsorbate within the pores seems to be little influenced by the flexibility of the framework.

When comparing the simulated adsorption isotherms with experimental data, it is evident that none of the proposed models leads to a quantitative agreement. In our opinion, these discrepancies can be due to the deficiencies of the modelling of the zeolite flexibility and/or the argon–zeolite interactions. The fact that different flexible models yield different results points to the importance of having an accurate model for the zeolite that is able to faithfully reproduce the zeolite vibrations in the presence of high adsorbate loadings. On the other hand, we have seen that parameters of the crossed argon interactions fitted to reproduce the adsorption isotherm on MFI had to be slightly modified to obtain a good agreement also for MEL. This might indicate that the Lennard-Jones functional form used to describe the argon–zeolite interactions also needs to be improved.

As mentioned in the Introduction, information about the microscopic structure of adsorbed argon can be obtained by neutron diffraction experiments. Indeed, there are plenty of instances in the bibliography in which this technique has been used to investigate the structure of a variety of adsorbed molecules within zeolite frameworks (see, for example, Ref. [37]). Following a similar protocol as that used by Llewellyn et al. [1], we have performed measurements of a MEL sample at different loadings, before and after the sub-step. The experiment was carried out using two different argon isotopes, $^{40}$Ar and $^{36}$Ar, with scattering lengths differing by an order of magnitude, which allows us to separately visualize the structure of the zeolite and of the adsorbate. These data will be analyzed in a forthcoming article. Besides comparing the experimental data to theoretical spectra calculated from

configurations of the simulations of this work, we will also try to obtain a structural model compatible with the experimental spectra by using the Reverse Monte Carlo method. In a previous work, we showed theoretically that this method can provide a satisfactory description of the adsorbed fluid up to the level of three body correlations [38,39]. In that theoretical work, the zeolite was kept frozen, but its flexibility can easily be incorporated in the Reverse Monte Carlo method, being also possible to investigate possible deformations of the zeolite. The structural models ob- tained in this subsequent study could be also potentially used to get a better modelling of the argon-zeolite interactions using a nu- merical inversion procedure [40].

Improving the zeolite models, so that they are able to properly predict structural deformations upon adsorption of different mol- ecules, is probably a more difficult goal. Most of the models pro- posed so far have been fitted to dynamical properties (such as the infrared vibrational spectrum) and structural properties in the presence of cations. However, there is no guarantee that these models will work for adsorbates under tight confinement condi- tions, as those considered in this work. We speculate that a more reasonable approach for our purposes will be to fit the zeolite model to try to predict the very well characterized structural changes on MFI. Given that these structural changes are really subtle, consisting simply on small modifications of the group symmetry, we anticipate that this will be a challenging goal.

## Acknowledgement
This work was funded by Dirección General de Investigación Científica y Técnica under Grants No. FIS2013-47350-C5-4-R, MAT2012-38567-C02-01 and Severo Ochoa SEV-2012-0267. The authors are thankful to Y. Mejia for performing the adsorption measurements. VSG also thanks the CSIC for support by means of a JAE program Ph.D. fellowship. Fruitful discussions with Noé G. Almarza are also gratefully acknowledged.

## Appendix A. Supplementary data
Supplementary data related to this article can be found at http:// dx.doi.org/10.1016/j.micromeso.2015.10.023.

## References
[1] P.L. Llewellyn, J.-P. Coulomb, Y. Grillet, J. Patarin, H. Lauter, H. Reichert, J. Rouquerol, Langmuir 9 (1998) 1846.
[2] P.L. Llewellyn, J.-P. Coulomb, Y. Grillet, J. Patarin, H. Lauter, H. Reichert, J. Rouquerol, Langmuir 9 (1998) 1852.
[3] U. Müller, H. Reichert, E. Robens, K.K. Unger, Y. Grillet, F. Rouquerol, J. Rouquerol, D.F. Pan, A. Mermann, Fresenius Z. Anal. Chem. 333 (1989) 433.
[4] E. García-Pérez, J.B. Parra, C.O. Ania, D. Dubbeldam, T.J.H. Vlugt, J.M. Castillo, P.J. Merkling, S. Calero, J. Phys. Chem. C 112 (2008) 9976.
[5] R.J.-M. Pellenq, D. Nicholson, Langmuir 95 (1995) 1626.
[6] H. van Koningsveld, J.C. Jansen, H. van Bekkum, Zeolites 10 (1990) 235.
[7] H. van Koningsveld, H. van Bekkum, J.C. Jansen, Acta Crystallogr. B43 (1987) 127.
[8] H. van Koningsveld, F. Tuinstra, H. van Bekkum, J.C. Jansen, Acta Crystallogr. B45 (1989) 423.
[9] J.P. Coulomb, P. Llewellyn, Y. Grillet, J. Rouquerol, Stud. Surf. Sci. Catal. 87 (1994) 535.
[10] D. Douguet, R.J.-M. Pellenq, A. Boutin, A.H. Fuchs, D. Nicholson, Mol. Sim. 17 (1996) 1255.
[11] R.J.-M. Pellenq, D. Nicholson, J. Phys. Chem. 98 (1994) 13339.
[12] D. Nicholson, R.J.-M. Pellenq, Adv. Coll. Interface Sci. 76 (1998) 179.
[13] O. Terasaki, T. Ohsuna, H. Sakuma, D. Watanabe, Y. Nakagawa, R.C. Medrud, Chem. Mater. 8 (1996) 463.
[14] C.A. Fyfe, H. Gies, G.T. Kokotailo, C. Pasztor, H. Strobl, D.E. Cox, J. Am. Chem. Soc. 111 (1989) 2470.
[15] C.A. Fyfe, Y. Feng, H. Grondey, G.T. Kokotailo, A. Mar, J. Phys. Chem. 95 (1991) 3747.
[16] H. Gies, B. Marler, C. Fyfe, G. Kokotailo, Y. Feng, D.E. Cox, J. Phys. Chem. Solids 52 (1991) 1235.
[17] R. Marguta, S.J. Khatib, J.M. Guil, E. Lomba, E.G. Noya, J.A. Perdigión-Melón, S. Valencia, Micropor. Mesopor. Mater. 142 (2011) 258.
[18] L. Zhang, H. Liu, X. Li, S. Xie, Y. Wang, W. Xin, S. Liu, L. Xua, Fuel Process. Technol. 91 (2010) 449.
[19] M.Y. Kustova, P. Hasselriis, C.H. Christensen, Catal. Lett. 96 (2004) 205.
[20] D. Dubbeldam, S. Calero, T.J.H. Vlugt, R. Krishna, T.L.M. Maesen, E. Beerdsen, B. Smit, Phys. Rev. Lett. 93 (2004) 088302.
[21] P. Demontis, G.B. Suffritti, S. Quartieri, E.S. Fois, A. Gamba, J. Phys. Chem. 92 (1988) 867-871.
[22] J.B. Nicholas, A.J. Hopfinger, F.R. Trouw, L.E. Iton, J. Am. Chem. Soc. 113 (1991) 4792-4800.
[23] G.J. Kramer, N.P. Farragher, B.W. van Beest, R.A. van Santen, Phys. Rev. B 43 (1991) 5068.
[24] J.R. Hill, J. Sauer, J. Phys. Chem. 99 (1995) 9536.
[25] N.A. Ramsahye, R.G. Bell, J. Phys. Chem. B 109 (2005) 4738-4747.
[26] A. Gabrieli, M. Sant, P. Demontis, G.B. Suffritti, J. Phys. Chem. C 117 (2013) 503.
[27] M. Jeffroy, C. Nieto-Draghi, A. Boutin, Mol. Sim. 40 (2014) 6-15.
[28] R. Bueno-Pérez, S. Calero, D. Dubbeldam, C.O. Ania, J.B. Parra, A.P. Zaderenko, P.J. Merkling, J. Phys. Chem. C 116 (2012) 25797-25805.
[29] P. Demontis, G.B. Suffritti, S. Quartieri, A. Gamba, E.S. Fois, J. Chem. Soc. Faraday Trans. 87 (1991) 1657-1663.
[30] T.J.H. Vlugt, M. Schenk, J. Phys. Chem. B 106 (2002) 12757-12763.
[31] A.G. Sánchez, D. Dubbeldam, S. Calero, J. Phys. Chem. C 114 (2010) 15068.
[32] D. Frenkel, B. Smit, Understanding Molecular Simulation. From Algorithms to Applications, Academic Press, Boston, 1996.
[33] T.J.H. Vlugt, E. García-Pérez, D. Dubbeldam, S. Bam, S. Calero, J. Chem. Theor. Comput. 4 (2008) 1107.
[34] F. Karavias, A.L. Meyer, Langmuir 7 (1991) 3118.
[35] E. Maglara, A. Pullen, D. Sullivan, W.C. Conner, Langmuir 10 (1994) 4167.
[36] L.E. First, C.E. Gounaris, J. Wei, C.A. Floudas, Phys. Chem. Chem. Phys. 13 (2011) 17339.
[37] N. Floquet, J.P. Coulomb, J.P. Bellat, J.M. Simon, G. Weber, G. Andre, J. Phys. Chem. C 111 (2007) 18182.
[38] V. Sánchez-Gil, E.G. Noya, E. Lomba, J. Chem. Phys. 140 (2014) 024504.
[39] V. Sánchez-Gil, E.G. Noya, L. Temleitner, L. Pusztai, J. Mol. Liq. 207 (2015) 211.
[40] N.G. Almarza, E. Lomba, Phys. Rev. E 68 (2003) 011202.