**Communication**

# Oxygen Self-Diffusion in Fluorite High Entropy Oxides

Alexander Chroneos ¹,²

¹ Department of Electrical and Computer Engineering, University of Thessaly, 38221 Volos, Greece; achronaios@uth.gr; Tel.: +30-6978775320
² Department of Materials, Imperial College London, London SW7 2BP, UK

**Abstract:** High-entropy oxides have recently attracted the interest of the community as a way of attuning the properties of oxides to energy applications. Here, we employ molecular dynamics simulations combined with empirical pair potential models to examine the predicted oxygen diffusivity of fluorite-structured high-entropy oxides. We show that lower levels of the dopants increase the overall diffusivity of the composition, but not to the levels of diffusion seen in yttria-doped zirconia. We attribute this to an increased resistance of the cation sublattice to the distortion that occurs through any multiple substitutions on the cation sublattice. To conclude, it is calculated that oxygen self-diffusion in high-entropy oxides is suppressed as compared to isostructural ternary oxides.

**Keywords:** high-entropy oxides; fluorites; density functional theory

---

## 1. Introduction

There is a drive to maximize ionic diffusion for more efficient performance of the energy materials presently considered for electrochemical solid-state devices (fuel cells and battery applications) [1,2]. For example, in solid oxide fuel cells (SOFC), the operation at intermediate temperatures requires materials with lower activation energies of diffusion to compensate [3,4]. This is because, typically in SOFCs, the oxygen vacancy content and the mobility of the electrode material are linked to the surface exchange kinetics and impact the cathode performance [3,4]. Accelerating ionic diffusion in ceramics can be achieved by doping, mechanical means (strain engineering), and designing the morphology (for example, grain boundary engineering and nanocomposites) [5–9]. In recent studies, Rost et al. [10] introduced the High-Entropy Oxides (HEO) concept, in which mixed oxides are stabilized by entropy. HEO are in essence analogous to the High-Entropy Alloys (HEA), which are alloys where high configurational entropy ($\Delta S_{config}$) that can stabilize metastable single phases (temperature is adequately high so as to account for the negative formation enthalpies of secondary phases) typically via high temperature sintering [11–13].

Several studies have examined the oxygen ion self-diffusion in fluorite-structured oxides [14–17]. Although the use of high-entropy compositions greatly expands the number of potential compounds, the values of oxygen diffusion have been shown to be relatively unremarkable and, in most cases, do not exceed the values reported for archetypal ternary oxides, such as $ZrO_2 + 8\% Y_2O_3$ (designated Z8Y). Characteristically, in the study of fluorite HEO, Gild et al. [15] synthesized numerous single-phase fluorite oxides. These solid solutions had equal molar fractions of $HfO_2$, $ZrO_2$, and $CeO_2$ as the base materials, whereas the oxides of yttrium (Y), gadolinium (Gd), ytterbium (Yb), titanium (Ti), magnesium (Mg), calcium (Ca), and lanthanum (La), in turn acted as fluorite structure stabilizers [15]. Irrespective of the composition, the determined activation energies of oxygen self-diffusion are unspectacular (1.14–1.29 eV) and the conductivity values are nearly an order of magnitude lower as compared to Z8Y [15]. The low values of ionic diffusivity are likely due to trapping of oxygen ion vacancies by the high concentrations of aliovalent cation dopants used in the construction of near-equimolar HEOs. Therefore, one strategy to improve the ionic diffusivity is to reduce the level of aliovalent doping, replacing it with mixed but isovalent dopants.

![](./images/1010729047040196643_1.jpg)

Citation: Chroneos, A. Oxygen Self-Diffusion in Fluorite High Entropy Oxides. *Appl. Sci.* 2024, 14, 5309. https://doi.org/10.3390/app14125309

Academic Editor: Roberto Zivieri

Received: 14 May 2024
Revised: 4 June 2024
Accepted: 17 June 2024
Published: 19 June 2024

![](./images/1010729047040196643_2.jpg)

Copyright: © 2024 by the author. Licensee MDPI, Basel, Switzerland.
This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

What is evident in the literature is that irrespective of a number of high-level experi-
mental and theoretical studies (for example, Refs. [18–27] and the references therein), there
is no understanding on the impact of entropy stabilization on the oxygen self-diffusion in
fluorite HEO. The key question is as follows: Does it improve the oxygen self-diffusion or
not? In an attempt to address this in the present study, we use molecular dynamics (MD)
simulations coupled with classical interatomic potentials to study the impact of composition
and, in particular, the influence of the level of trivalent rare-earth dopants upon the oxygen
ion diffusivity of a series of high-entropy alloy compositions. The focus will be on the HEOs
of $Zr_{(1-x)/3}Hf_{(1-x)/3}Ce_{(1-x)/3}Gd_{x/2}Y_{x/2}O_{2-x}$, $Zr_{(1-x)/3}Hf_{(1-x)/3}Ce_{(1-x)/3}Y_{x/2}La_{x/2}O_{2-x}$ at $x =$
0.14 ($8\% RE_2O_3$) compared with predicted oxygen ion diffusivity for Z8Y and C8Y.

## 2. Methodology
Molecular dynamics calculations were performed using the Large-scale Atomic/Molecular
Massively Parallel Simulator (LAMMPS) code [28,29]. We employed classical molecular
statics and dynamic simulations using the Buckingham empirical potentials [30,31], the
transferability of which has been tested in previous studies [32,33]. Static transition state
atomistic simulations were performed using the GULP code [34,35]. Entropy-stabilized ox-
ides posed challenges for the atomic scale simulation methods as the many different cations
led to a great number of potential configurations, all of which may have influence over the
overall bulk properties. Although classical potentials are of the order $10^4$ times faster than
the electronic structure calculations, automated methods for producing simulation data are
still necessary.

For the materials considered here, the following method was adopted to provide an
estimate of the mean squared displacement at an average temperature $T$:
1. An $8 \times 8 \times 8$ supercell of the fluorite structure is created with a random assignment of
cations according to a specified stoichiometry. Oxygen ion vacancies are introduced
onto the oxygen ion sublattice to provide charge balance.
2. An equilibration series of simulations which consist of the following:
   a. Annealing is at a set temperature of 1500 K to equilibrate the distribution of
oxygen vacancies.
   b. A 2 ns simulation at constant (zero) pressure a set temperature of $T_{set}$ is used to
establish the equilibrium cell parameters at temperature.
   c. The cell is then set to the average value of the lattice parameters, and a further
50 ps of simulation time is run to allow the vacancy distribution to adapt to the
altered cell volume.
3. The statistics run is calculated in a constant volume, a constant energy ensemble (i.e.,
without the thermostat) for a simulation time of 10 ns or the time required for the
mean squared displacement of the oxygen ions to reach $10\ \mathring{A}^2$. The latter condition
allows for efficient early termination of compositions with clear values of diffusivity.
The simulation time and displacement of the ions $R(t)$ is recorded in this last step and
used to calculate the average temperature $T$ ($\sim T_{set}$) and mean squared displacement
($\langle R^2(t)\rangle$) of the oxygen ions.

The oxygen ion diffusivity, $D(T,\text{conf}.)$ of each configuration is then estimated by a
least squares fit of the Einstein relation to the long timescale behavior of the displacement
$R(t)$ at time $t$ as follows:

$$
\left\langle R^{2}(t)\right\rangle=6 D(T, \text { conf. }) t
$$

From these data, we can now characterize each composition by fitting an Arrhenius
relationship to each set of $T$, configuration data point to obtain a value for the activation energy
$E_a$ and preexponential $D_0$ for a given composition assuming the following:

$$
D=D_{0} \exp \left(\frac{-E_{a}}{k_{B} T}\right)
$$

## 3. Results and Discussion

In the present work, we studied three general compositions of high-entropy oxides based upon reported experimental synthesis and the availability of oxygen ion potentials to describe their behavior. These are $\text{Zr}_{(1-x)/3}\text{Hf}_{(1-x)/3}\text{Ce}_{(1-x)/3}\text{Gd}_{x/2}\text{Y}_{x/2}\text{O}_{2-x}$ (HEO_A), $\text{Zr}_{(1-x)/3}\text{Hf}_{(1-x)/3}\text{Ce}_{(1-x)/3}\text{Y}_{x/2}\text{La}_{x/2}\text{O}_{2-x}$ (HEO_B) and $\text{Zr}_{(1-x)/2}\text{Hf}_{(1-x)/2}\text{Y}_{x/3}\text{La}_{x/3}\text{Pr}_{x/3}\text{O}_{2-x}$ (HEO_C).

Figure 1 shows the calculated values of diffusivity against temperature for the two considered HEOs compared with the calculated values for $\text{CeO}_2 + 8\% \text{Y}_2\text{O}_3$, C8Y, and $\text{ZrO}_2 + 8\% \text{Y}_2\text{O}_3$, Z8Y. At these compositions, the oxygen ion diffusivity is generally lower than the ternary oxides. We see generally good agreement with the Arrhenius behavior, and the fitted values of activation energy are in agreement with those reported in the literature. Figure 1 also shows the importance of a statistical approach to the calculations. For a given temperature, there is a scatter in the range of values. For Z8Y, this is quite small but for the HEO compositions, there are significant differences in diffusivity for different configurations within a single composition, and this is evident even with the quite large 6000 atom cells considered here.

![](./images/1010729047040196643_3.jpg)

Figure 1. Oxygen ion diffusivities and calculated activation energies for two ESOs HEO_A, $\text{Zr}_{(1-x)/3}\text{Hf}_{(1-x)/3}\text{Ce}_{(1-x)/3}\text{Gd}_{x/2}\text{Y}_{x/2}\text{O}_{2-x}$, HEO_B $\text{Zr}_{(1-x)/3}\text{Hf}_{(1-x)/3}\text{Ce}_{(1-x)/3}\text{Y}_{x/2}\text{La}_{x/2}\text{O}_{2-x}$ at $x = 0.14$ ($8\% RE_2O_3$) compared with predicted oxygen ion diffusivity for Z8Y and C8Y.

Top image of Figure 2 shows the ionic diffusivity values at 1000 K for the three HEO compositions and $\text{ZrO}_2 + \text{Y}_2\text{O}_3$ for comparison as a function of the total trivalent dopant

concentration, i.e., the sum of the La, Y, Pr and Gd molar fractions. The datapoints for ZY show a rapid increase with Y-doping, a maximum around 10% molar fraction Y (~6% Y₂O₃), and a slow decrease in diffusivity. This behavior has been extensively described in the literature as a balance between the creation of charge compensation oxygen vacancies and the trapping of the vacancies through the addition of large densities of trivalent ions. Similar curves are observed for the HEO compositions; however, in these cases, the overall diffusivity is generally lower, particularly for the maximum peak value of diffusivity at around 10% dopant concentration. We explored this behavior in middle and bottom images of Figure 2, where the points show the predicted values of D₀ and Eₐ for the different compositions. Middle image of Figure 2 indicates that the activation energy for diffusion for ZY decreases to a value of 0.4 eV, comparable with that of oxygen vacancy diffusion in the dilute limit. For the HEOs, however, the activation energy for diffusion tends to be a significantly higher value of around 0.6-0.75 eV, depending upon the composition. The value of D₀ calculated from the simulations varies with total aliovalent doping concentration but is relatively unchanged between the different compositions considered. The decrease in the diffusivity in the HEOs as compared with the ZY is therefore due to this increased activation energy, particularly when comparing the data up to ~10% molar dopant concentration.

We considered why the HEO compositions exhibited these levels of oxygen ion dif- fusion, focusing specifically on the reduced diffusion because of the increased activation energy exhibited in top and middle images of Figure 2. Oxygen diffusion is mediated via vacancies moving through the fluorite lattice, a process that, in the doped materials, is hindered both by vacancy-vacancy interactions, Coulomb attraction, and trapping by the trivalent dopant ions. Figure 3a shows an illustration of the fluorite lattice with an example oxygen vacancy in the nearest neighbor position to a Y³⁺ ion, and the minimum energy pathway for this cell as the vacancy exchanges places with an adjacent oxygen ion. Figure 3b shows both the energy maxima at the transition point and the finite reaction energy, Eᵣ, as the sites are not symmetrically equivalent.

To help us understand the effect of multiple substitutions at the cation sites, we defined the barrier energy Eᵦ, which is a first-order approximation to the transition barrier if Eᵣ was zero, and there were no energetic difference between the two sites.

$$
E_{\mathrm{b}}=E_{\mathrm{ts}}-\frac{1}{2} E_{\mathrm{r}}
$$

where Eₜₛ is taken as the maximum energy difference from the lower end of the transition start or end points. Physically Eᵦ corresponds to the maximum energy required to deform the lattice that is required to accommodate the ion as it moves through the transition pathway, and ½ Eᵣ represents the trapping of the oxygen vacancies by the host cations.

Figure 4 shows plots of the averages and spread of values of Eᵦ and ½ Eᵣ for the oxygen vacancy transition state calculations performed at random configurations of cations, with 6.25% Y and various levels of isovalent cation doping from zero Ce + Hf to a total of 66%, i.e., an equimolar amount of Zr, Hf, and Ce. These data show that the value of the activation energy increases with isovalent doping, in agreement with the low Y-doping MD simulation results shown in Figure 2. The increase in activation energy is, however, driven primarily by an increase in the trapping of oxygen vacancies by the host lattice, Eᵣ, such that the average and spread of the Eᵦ values remain relatively unchanged with increasing amount of cation mixing.

![](./images/1010729047040196643_4.jpg)

Figure 2. The plots show (top) the overall diffusivity of the three HEOs and Z8Y as a function of the doping concentration together with (middle) the activation energy and (bottom) the pre-exponent. In each plot, the colored points show the individual data points and the solid lines show the data fitted to the activation energy and pre-exponent.

For many years, simple interatomic potentials have proven their transferability and potential to describe diffusion properties in oxides with higher accuracy as compared to experiment. At any rate, many of the classical interatomic potentials used may not capture all the subtleties of interatomic interactions in complicated systems such as HEOs. In that respect, ab initio calculations should be used to clarify if these subtleties will lead to a better understanding of diffusion properties [36,37]. The advantage of classical simulation is the ability to perform simulations on extended systems that capture the dopant-defect interactions with respect to the local environments. Conversely, ab initio molecular dynamics (AIMD) simulations are typically limited to smaller systems (up to a few hundreds of atoms at best) and sub-nanosecond timescales. This, in turn, can result in far fewer diffusion events (particularly in high activation of diffusion systems) and poor statistics [37]. At any rate, present and near future computational resources will allow more rigorous AIMD calculations, which can enrich our understanding of these systems with electronic structure details and insights that cannot be obtained by classical MD studies. Furthermore, there is grounds for further analysis of the simulation results via the appropriate thermodynamic models that to link microscopic and macroscopic properties, such as the cBΩ model by Varotsos and Alexopoulos [38–40].

![](./images/1010729047040196643_6.jpg)

Figure 4. Box and whisker diagram of the population of (a) reaction energies (Eᵣ) and (b) barrier energies for oxygen vacancy diffusion for 6.25% Y doping in ZrO₂ with progressively greater amount of Ce and Hf additions.

## 4. Conclusions

In this paper, we have examined the oxygen ion diffusivity as predicted from a series
of molecular dynamics simulations of typical fluorite-structured high-entropy oxides.
We have shown that the values of diffusivity are predicted to be generally lower than
isostructural ternary oxides such as $ZrO_2 + Y_2O_3$. This is reflected by the oxygen diffusion
activation energy of HEO, which is more than 0.2 eV higher as compared to the ternary
oxides. Therefore, the present results show that the formation of HEOs are not beneficial
for oxygen self-diffusion. The present study aims to motivate further experimental work on
the direct comparison between HEO and comparable fluorite compositions to conclusively
determine whether HEOs provide any benefit.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: Data is contained within the article.

Acknowledgments: The author acknowledges calculations and discussions with David Parfitt. The communications with Federico Baiutti and Albert Tarancon are also acknowledged. Open access fee was paid from the Imperial College London Open Access Fund.

Conflicts of Interest: The author declares no conflicts of interest.

References

1.  Steele, B.C.H.; Heinzel, A. Materials for fuel-cell technologies. Nature 2001, 414, 345–352. [CrossRef]
2.  Tarascon, J.M. Key challenges in future Li-battery research. Philos. Trans. R. Soc. Lond. A 2010, 368, 3227–3241. [CrossRef]
3.  Brett, D.J.L.; Atkinson, A.; Brandon, N.P.; Skinner, S.J. Intermediate temperature solid oxide fuel cells. Chem. Soc. Rev. 2008, 37, 1568–1578. [CrossRef]
4.  Tarancón, A.; Burriel, M.; Santiso, J.; Skinner, S.J.; Kilner, J.A. Advances in layered oxide cathodes for intermediate temperature solid oxide fuel cells. J. Mater. Chem. 2010, 20, 3799–3813. [CrossRef]
5.  Kushima, A.; Yildiz, B. Oxygen ion diffusivity in strained yttria stabilized zirconia: Where is the fastest strain? J. Mater. Chem. 2010, 20, 4809–4819. [CrossRef]
6.  Souza, R.A.D.; Ramadan, A.; Hörner, S. Modifying the barriers for oxygen-vacancy migration in fluorite-structured CeO₂ electrolytes through strain: A computer simulation study. Energy Environ. Sci. 2012, 5, 5445–5453. [CrossRef]
7.  Rushton, M.J.D.; Chroneos, A. Impact of uniaxial strain and doping on oxygen diffusion in CeO₂. Sci. Rep. 2014, 4, 6068. [CrossRef]
8.  Chiabrera, F.; Garbayo, I.; López-Conesa, L.; Martín, G.; Ruiz-Caridad, A.; Walls, M.; Ruiz-González, L.; Kordatos, A.; Núñez, M.; Morata, A.; et al. Engineering transport in manganites by tuning local nonstoichiometry in grain boundaries. Adv. Mater. 2019, 31, 1805360. [CrossRef]
9.  Baiutti, F.; Chiabrera, F.; Acosta, M.; Diercks, D.; Parfitt, D.; Santiso, J.; Wang, X.; Cavallaro, A.; Morata, A.; Wang, H.; et al. A high-entropy manganite in an ordered nanocomposite for long-term application in solid oxide cells. Nat. Commun. 2021, 12, 2660. [CrossRef]
10. Rost, C.M.; Sachet, E.; Borman, T.; Moballegh, A.; Dickey, E.C.; Hou, D.; Jones, J.L.; Curtarolo, S.; Maria, J.-P. Entropy-stabilized oxides. Nat. Commun. 2015, 6, 8485. [CrossRef]
11. Yeh, J.-W.; Chen, S.-K.; Lin, S.-J.; Gan, J.-Y.; Chin, T.-S.; Shun, T.-T.; Tsau, C.-H.; Chang, S.-Y. Nanostructured high-entropy alloys with multiple principal elements: Novel alloy design concepts and outcomes. Adv. Eng. Mater. 2004, 6, 299–303. [CrossRef]
12. Gali, A.; George, E.P. Tensile properties of high- and medium-entropy alloys. Intermetallics 2013, 39, 74–78. [CrossRef]
13. Gludovatz, B.; Hohenwarter, A.; Catoor, D.; Chang, E.H.; George, E.P.; Ritchie, R.O. A fracture-resistant high-entropy alloy for cryogenic applications. Science 2014, 345, 1153–1158. [CrossRef]
14. Bonnet, E.; Grenier, J.C.; Bassat, J.M.; Jacob, A.; Delatouche, B.; Bourdais, S. On the ionic conductivity of some zirconia-derived high-entropy oxides. J. Eur. Ceram. Soc. 2021, 41, 4505–4515. [CrossRef]
15. Gild, J.; Samiee, M.; Braun, J.L.; Harrington, T.; Vega, H.; Hopkins, P.E.; Vecchio, K.; Luo, J. High-entropy fluorite oxides. J. Eur. Ceram. Soc. 2018, 38, 3578–3584. [CrossRef]
16. Sarkar, A.; Wang, Q.; Schiele, A.; Chellali, M.R.; Bhattacharya, S.S.; Wang, D.; Brezesinski, T.; Hahn, H.; Velasco, L.; Breitung, B. High-entropy oxides: Fundamental aspects and electrochemical properties. Adv. Mater. 2019, 31, 1806236. [CrossRef]
17. Akrami, S.; Edalati, P.; Fuji, M.; Edalati, K. High-entropy ceramics: Review of principles, production and applications. Mater. Sci. Eng. R Rep. 2021, 146, 100644. [CrossRef]
18. Chen, K.P.; Pei, X.T.; Tang, L.; Cheng, H.R.; Li, Z.M.; Li, C.W.; Zhang, X.W.; An, L.A. A five-component entropy-stabilized fluorite oxide. J. Eur. Ceram. Soc. 2018, 38, 4161–4164. [CrossRef]
19. Chellali, M.R.; Sarkar, A.; Nandam, S.H.; Bhattacharya, S.S.; Breitung, B.; Hahn, H.; Velasco, L. On the homogeneity of high entropy oxides: An investigation at the atomic scale. Scipta Mater. 2019, 166, 58–63. [CrossRef]
20. Wright, A.J.; Wang, Q.Y.; Huang, C.Y.; Nieto, A.; Chen, R.K.; Luo, J. From high-entropy ceramics to compositionally-complex ceramics: A case study of fluorite oxides. J. Eur. Ceram. Soc. 2020, 40, 2120–2129. [CrossRef]
21. Dabrowa, J.; Szymczak, M.; Zajusz, M.; Mikula, A.; Mozdzierz, M.; Berent, K.; Wytwal-Sarna, M.; Bernasik, A.; Stygar, M.; Swierczek, K. Stabilizing fluorite structure in ceria-based high-entropy oxides: Influence of Mo addition on crystal structure and transport properties. J. Eur. Ceram. Soc. 2020, 40, 5870–5881. [CrossRef]
22. Spiridigliozzi, L.; Ferone, C.; Cioffi, R.; Dell'Agli, G. A simple and effective predictor to design novel fluorite-structured High Entropy Oxides (HEOs). Acta. Mater. 2021, 202, 181–189. [CrossRef]
23. Chen, K.P.; Ma, J.X.; Tan, C.A.X.; Li, C.W.; An, L.A. An anion-deficient high-entropy fluorite oxide with very low density. Ceram. Inter. 2021, 47, 21207–21211. [CrossRef]
24. Su, L.; Chen, X.; Xu, L.; Eldred, T.; Smith, J.; DellaRova, C.; Wang, H.J.; Gao, W.P. Visualizing the formation of high-entropy fluorite oxides from an amorphous precursor at atomic resolution. ACS Nano 2022, 16, 21397–21496. [CrossRef]

25. Nundy, S.; Tatar, D.; Kojcinovic, J.; Ullah, H.; Chosh, A.; Mallick, T.K.; Meinusch, R.; Smarsly, B.M.; Tahir, A.A.; Djerdj, I. Bandgap engineering in novel fluorite-type rare earth high-entropy oxides (RE-HEOs) with computational and experimental validation for photocatalytic water splitting applications. *Adv. Sustain. Syst.* 2022, 6, 2200067. [CrossRef]

26. Kotsonis, G.N.; Almishal, S.S.I.; Vieira, F.M.D.; Crespi, V.H.; Dabo, I.; Rost, C.M.; Maria, J.P. High-entropy oxides: Harnessing crystalline disorder for emergent functionality. *J. Am. Ceram. Soc.* 2023, 106, 5587–5611. [CrossRef]

27. Ma, B.; Wen, Z.Q.; Qin, J.D.; Wu, Z.Y.; Liu, J.X.; Lv, Y.M.; Yu, J.J.; Zhao, Y.H. Synthesis and microstructure of (Ce₀.₂Zr₀.₂La₀.₂Sm₀.₂Nd₀.₂)O₂-δ high-entropy oxides characterized by fluorite structure. *Ceram. Inter.* 2024, 50, 1981–1989. [CrossRef]

28. Plimpton, S. Fast Parallel algorithms for short-range molecular dynamics. *J. Comput. Phys.* 1995, 117, 1–19. [CrossRef]

29. Thompson, A.P.; Aktulga, H.M.; Berger, R.; Bolintineanu, D.S.; Brown, W.M.; Crozier, P.S.; in 't Veld, P.J.; Kohlmeyer, A.; Moore, S.G.; Nguyen, T.D.; et al. LAMMPS—A flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum Scales. *Comp. Phys. Commun.* 2022, 271, 108171. [CrossRef]

30. Buckingham, R.A.; Lennard-Jones, J.E. The classical equation of state of gaseous helium, neon and argon. *Proc. R. Soc. London A* 1938, 168, 264–283.

31. Grimes, R.W.; Busker, G.; McCoy, M.A.; Chroneos, A.; Kilner, J.A.; Chen, S.P. The Effect of Ion Size on Solution Mechanism and Defect Cluster Geometry. *Ber. Bunsenges. Phys. Chem.* 1997, 101, 1204. [CrossRef]

32. Rupasov, D.; Chroneos, A.; Parfitt, D.; Kilner, J.A.; Grimes, R.W.; Istomin, S.Y.; Antipov, E.V. Oxygen diffusion in Sr₀.₇₅Y₀.₂₅CoO₂.₆₂₅: A molecular dynamics study. *Phys. Rev. B* 2009, 79, 172102. [CrossRef]

33. Ebmeyer, W.; Dholabhai, P.P. High-throughput prediction of oxygen vacancy defect migration near misfit dislocations in SrTiO₃/BaZrO₃ heterostructures. *Mater. Adv.* 2024, 5, 315–328.

34. Gale, J.D. GULP: Capabilities and prospects. *Z. Für Krist.-Cryst. Mater.* 2005, 220, 552–554. [CrossRef]

35. Gale, J.D. GULP: A Computer Program for the Symmetry-Adapted Simulation of Solids. *J. Chem. Soc. Faraday Trans.* 1997, 93, 629–637. [CrossRef]

36. Kushima, A.; Parfitt, D.; Chroneos, A.; Yildiz, B.; Kilner, J.A.; Grimes, R.W. Interstitialcy diffusion of oxygen in tetragonal La₂CoO₄+δ. *Phys. Chem. Chem. Phys.* 2011, 13, 2242–2249. [CrossRef]

37. He, X.; Zhu, X.; Epstein, A.; Mo, Y. Statistical variances of diffusional properties from ab initio molecular dynamics simulations. *npj Comput. Mater.* 2018, 4, 18. [CrossRef]

38. Varotsos, P.; Alexopoulos, K. *Thermodynamics of Point Defects and their Relation with the Bulk Properties*; North-Holland: Amsterdam, The Netherlands, 1986.

39. Cooper, M.W.D.; Grimes, R.W.; Fitzpatrick, M.E.; Chroneos, A. Modeling oxygen self-diffusion in UO₂ under pressure. *Solid State Ionics* 2015, 282, 26–30. [CrossRef]

40. Chroneos, A. Connecting point defect parameters with bulk properties to describe diffusion in solids. *Appl. Phys. Rev.* 2016, 3, 041304. [CrossRef]

Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
