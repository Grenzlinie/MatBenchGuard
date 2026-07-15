![](./images/812771064261115905_1.jpg)
![](./images/812771064261115905_2.jpg)

Article

# Thermal Conductivity of Metal-Coated Tri-Walled Carbon Nanotubes in the Presence of Vacancies-Molecular Dynamics Simulations

Ravindra Sunil Dhumal ¹, Dinesh Bommidi ² and Iman Salehinia ¹,*

¹ Department of Mechanical Engineering, Northern Illinois University, DeKalb, IL 60115, USA;
rdhumal@niu.edu
² Department of Mechanical Engineering, University of Rochester, Rochester, NY 14627, USA;
dbommidi@ur.rochester.edu
* Correspondence: isalehinia@niu.edu

Received: 25 April 2019; Accepted: 24 May 2019; Published: 28 May 2019

![](./images/812771064261115905_3.jpg)

**Abstract:** Variation in the thermal conductivity of a metal-coated tri-walled carbon nanotube (3WCNT), in the presence of vacancies, was studied using non-equilibrium molecular dynamics simulations. A Two-Temperature model was used to account for electronic contribution to heat transfer. For 3WCNT with 0.5% and 1% random vacancies, there was 76%, and 86% decrease in the thermal conductivity, respectively. In that order, an overall ~66% and ~140% increase in the thermal conductivity was recorded when 3 nm thick coating of metal (nickel) was deposited around the defective models. We have also explored the effects of tube specific and random vacancies on thermal conductivity of the 3WCNT. The changes in thermal conductivity have also been justified by the changes in vibrational density of states of the 3WCNT and the individual tubes. The results obtained can prove to be useful for countering the detrimental effects of vacancies in carbon nanotubes.

**Keywords:** metallic coating; multi-walled carbon nanotubes; thermal conductivity; vacancy concentration; phonon and electron heat transfer; phonon density of states

## 1. Introduction

Recent advances in nanotechnology and material design have made it possible for the size of the electronic devices to be reduced to nano/micro level. This often leads to higher power densities, since heat dissipation is restricted to a very small region. Therefore, an efficient thermal management system is central to these small-scale devices. One way to effectively dissipate heat is to employ thermal interface materials (TIMs). Due to their quasi 1-D structure and considerably high thermal conductivity (~600–6000 W/mK) [1–9], carbon nanotubes (CNTs) qualify as good candidates for this application. To utilize CNTs as a TIM, the forest of CNTs must be fabricated and located between the heat source and the heat sink. Among various possible configurations, vertically aligned carbon nanotubes (VACNTs), also known as CNT turfs, stand out as the most promising candidate for heat dissipation purposes, due to one dimensional heat transfer.

Phonon scattering, due to inevitable defects that form during CNTs growth, results in significant reduction in their thermal conductivity, and to a larger extent in the overall heat transfer of a CNT turf [10–12]. Some of the common defects include 5-7 defect, 5-7-7-5 (Stone Wales), 5-8-5 defect, mono vacancies, di-vacancies, adatoms, etc. [10,13]. Defects in CNTs have been the center of various studies [8–10,13–19]. It has been consistently reported that the effect of vacancy defects on the thermal conductivity of SWCNT is more severe than that of other point defects, such as Stone-Wales (SW) defects and ad-atoms at the same concentration level [9,14,20]. Park et al. [10] and Chen et al. [19] both used reverse NEMD (RNEMD) simulations to report a drop in thermal conductivity of SWCNTs.

Nanomaterials 2019, 9, 809; doi:10.3390/nano9060809
www.mdpi.com/journal/nanomaterials

Park's study, however, included significant concentration(s) of vacancy defects (up to 2%) and reported over 80% reduction in thermal conductivity as opposed to maximum of three point defects in the study conducted by Chen [19]. A power law decrease in thermal conductivity has also been observed with inclusion of vacancies in CNTs [8,9]. All of the studies probing the effect of vacancies on the thermal conductivity of CNTs, have only been performed on single-walled carbon nanotubes, despite the fact that the majority of CNTs in a CNT turf are multi-walled CNTs (MWCNTs), with 7-10 concentric CNTs [21,22]. Also, as MWCNTs have a greater number of shells, they provide extra pathways for heat transfer [3]. To keep a balance between taking a step closer to reality and performing studies that were not computationally extensive, we have focused on the effect of vacancies on the thermal conductivity of tri-walled carbon nanotubes (3WCNT).

Combining metals and VACNTs has been suggested as a way to improve the thermal properties of the VACNTs as TIMs. The metallization of the CNTs' ends in VACNTAs has been frequently applied to reduce the interface thermal resistance (ITR) between the VACNTAs and the substrate [23,24]. Despite an order of magnitude improvement on ITR, i.e., approaching 1-2 mm² K/W, metallization of the CNT tips in VACNTAs only affects the ITR between the TIM, the heat source, and the heat sink, hence not alleviating the reduced thermal conductivity, due to vacancies. Filling CNTs with metals has been suggested as another way of improving the thermal conductivity of VACNTAs. Stano et al. [25] outlined the procedure for procuring copper encapsulated VACNTAs and indicated that the resulting composite, by virtue of its superior thermal conductivity, was ideal for thermal management in electronic devices. A molecular dynamics study, conducted by Cui et al. [26], showed above 40% enhancement in the thermal conductivity of gold filled CNTs (nano-cables) over bare CNTs of identical dimensions. An important challenge for filling CNTs with metals is controlling the filling process. Furthermore, as the metal particles only fill in the inner tube, this method only offers a limited design space. To extend the design space, the deposition of metals on the outer tubes of CNTs has been pursued [25,27-30]. Using electroplating method, Smith et al. [27] and Hua et al. [28] deposited a uniform coating of nickel (Ni) on CNTs. Stano et al. [25] have reported the fabrication of core/shell metal-coated CNT arrays, using oxygen plasma treatment, followed by the infiltration of CNTs with an aqueous supersaturated Cu salt solution. They also claimed that the same procedure can be used to deposit Ni, Fe, Co, and Ag on CNTs in VACNTAs. Electroless deposition [29,31], and chemical vapor deposition [30], have been also reported as possible methods to create a conformal metal coating on a CNT surface. Bommidi et al. [32] have investigated the axial thermal conductivity of a nickel-coated tri-walled CNT using molecular dynamics simulations. The thermal conductivity of the composite material was 50% lower than pristine CNT when 1.2 nm of nickel coating was applied on the CNT. However, the decreasing rate of the thermal conductivity was insignificant for the metal thicker than 1.6 nm. The reduction in the axial thermal conductivity, and by adding metal, was justified by noting that the theoretical thermal conductivity of Ni is much lower than that for CNTs. However, adding a metallic coating on a defective CNT might result in higher axial thermal conductivity as in the presence of vacancies, the thermal conductivity of a CNT might be lower than that of the metal. This study intends to perform such investigation.

While we have only considered the application of metal-coated CNTs as TIMs, metal-coated CNT arrays are also promising in catalysis, energy storage, and sensing applications [33-36]. For example, while CNTs have been proved as promising materials for sensing applications, carbon may not be the material of choice to be exposed to various environments, resulting in less interest for this material as sensors. Metallic nano-foams show clear advantage in these applications over CNT turfs, however they suffer from microscopically brittle behavior [37]. Metal-coated CNT arrays may resolve the above-mentioned issues with the added benefit of lower density.

Molecular dynamics simulations were performed to study the axial thermal conductivity of tri-walled CNTs in the presence of vacancies. In addition, both phonon and electron contributions to thermal conductivity were considered to investigate the thermal conductivity of metal-coated CNTs when vacancies were present in the CNTs. Due to its ability to form uniform coating on CNTs [27],

nickel was chosen for conducting this study. The nickel coating was modeled free of defects, due to the fact that the effect of vacancies on the thermal conductivity of nickel is insignificant, as the heat transfer in metals is mostly controlled by electrons.

## 2. Materials and Methods

Non-equilibrium molecular dynamics (NEMD) simulations were performed in LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator) [38] to investigate the thermal conductivity of defective tri-walled CNTs coated with nickel. The results were then compared to those of the models without Ni coating.

The metal's major contribution to heat transfer would be by virtue of its free electrons. However, NEMD is not capable of considering the electronic heat transfer. Therefore, the two-temperature model (TTM) was implemented in the MD simulations, resulting in accounting for the interactions between phonons and electrons in the system. Wang et al. [39] successfully calculated the thermal conductivity of pure copper within good approximation of the actual value using this technique. Furthermore, they used MD-TTM to calculate the thermal resistance between CNT-Cu interface. NEMD coupled with TTM has also been used for calculating the variation in Thermal conductivity of pristine 3WCNTs with addition of metallic layers around it [32].

For carbon/carbon (C/C) interactions, adaptive intermolecular reactive empirical bond order (AIREBO) potential function was adopted [40]. Nickel/nickel (Ni/Ni) interactions were expressed by the embedded atom method (EAM) potential [41]. Nickel/carbon (Ni/C) interactions were modeled using the Morse type interatomic potential [42]. Detailed description of the interatomic potentials and also the TTM model is available in our recent publication [32].

Thermal conductivity was calculated using the Fourier's law:

$$
k=-\frac{J}{\left(A \cdot \frac{\Delta T}{\Delta x}\right)} \tag{1}
$$

where $J$ is the total heat flux per unit time, $A$ is the cross-sectional area, and $\frac{\Delta T}{\Delta x}$ is the temperature gradient. To implement this equation, cold and hot heat baths were applied on the two ends of each model and $J$ was calculated from Equation (2) [39,43]:

$$
J=\frac{Q_{h}-Q_{c}}{2 \Delta t}, \tag{2}
$$

where the heat current $Q_{h}$, and $Q_{c}$ are the transferred energy from the hot and cold regions, respectively, and $\Delta t$ is the time range within which the transferred energies are calculated. The cross-sectional area, $A$, corresponds to $A=\pi\left(R^{2}-r^{2}\right)$, where $R$ and $r$ are the average Van der Waals radii of the farthest, and the nearest atoms from the CNT axis, respectively [32].

Free boundary conditions were applied to both sides of the models and the structure was divided into 100 grids. Upon energy minimization using conjugate gradient method, the system was equilibrated to 300 K for 175 ps using Canonical (NVT) ensemble. Then, in a Micro-canonical (NVE) ensemble, the third grid, and the third last grid were maintained at 350 K and 250 K, using Langevin thermostat, simulating the thermal heat baths. The choice of the thermostatting method will not have a significant effect on the obtained results, provided that the thermostat regions are kept at their desired temperatures. For the models with the Ni coating, TTM was then enabled and the system was allowed to evolve for 1.25 ns. For using TTM with MD, it was assumed that the temperature of electronic subsystem did not change within a grid. To calculate the temperature gradient, the temperatures of grids between 20 and 80 were linearly fit [32] and averaged over the last 250 ps of each simulation. The grids between 20 and 80 were chosen to ascertain a minimal effect of nonlinearity due to extremely high thermal gradient in NEMD simulations [43]. Values of $J$ were calculated every 25 ps (i.e., $\Delta t$ in Equation (2)) and were averaged over 250 ps as well. The timestep of 0.5 fs was chosen for each

simulation. Figure 1a,c show the schematics of the CNT and the composite, respectively, having fixed ends and heat baths. Figure 1b,d show the respective gradients of temperature along the axis of the models. For the composite model, both electronic and phononic temperatures are plotted in Figure 1d.

![](./images/812771064261115905_4.jpg)

Figure 1. (a) Atomic model of a 3WCNT with heat baths and fixed ends, and (b) temperature profile along the axis of the 3WCNT due to the heat baths. (c) Atomic model of a (1 nm) Ni-coated 3WCNT with heat baths and fixed ends, and (d) phononic and electronic temperature profiles along the axis of the model due to the heat baths.

The selected tri-walled CNTs for this study were all 57 nm and composed of three coaxial armchair CNTs with chiralities (10,10), (15,15) and (20,20). The armchair CNTs were selected as those have higher thermal conductivity than other types of CNTs, i.e., zig-zag and chiral ones [44,45].

To introduce vacancies in the model, carbon atoms were deleted only from the CNT spanning the middle 20–80% of the its length. This was done to make sure that no atoms were being deleted from the heat baths, thereby not altering the number of thermostat atoms.

Phonon density of states (PDOS) have been used as a common tool for studying the effects of various parameters on the thermal conductivity of CNTs, and the thermal interface resistance between CNTs and other materials [10,46–49]. We, also used PDOS, in order to explain the observed behavior of the defective and metal-coated CNTs. Phonon density of states refers to the number of phononic modes available as a function of frequency per unit volume [48]. It is obtained by the Fourier transform of the velocity auto-correlation function (VACF), as shown in Equation (3):

$$
D(f)=F \int e^{-2 \pi i f t}\langle\vec{v}(t) \cdot \vec{v}(0)\rangle d t, \tag{3}
$$

where, $F$ is a normalization factor set equal to 1, $f$ is the frequency, and the term in the brackets is the VACF. VACF is obtained by calculating the autocorrelation of the atomic velocities on the consecutive timesteps. Since we are interested in finding axial thermal conductivity, only the velocities in axial direction of the CNT structure were considered for VACF.

## 3. Results and Discussion

Figure 2 shows the variation in thermal conductivity of 3WCNTs with 0.5% and 1% vacancies randomly distributed in the CNTs. To ensure that the distribution of vacancies had no effect on the results, three different distributions were considered for each vacancy concentration. The results show insignificant effect of the vacancy distribution on the thermal conductivities. The thermal conductivity of CNT models with 1% vacancies show almost 86% percent reduction when compared to pristine CNTs. This is in good agreement with the results obtained by Park et al. [10]. For 0.5% vacancies, around 76% drop was observed.

![](./images/812771064261115905_5.jpg)

Figure 2. Variation in thermal conductivity of 3WCNTs with various vacancy concentrations. Each data point shows the average of a set of three simulations having three different patterns of (same) vacancy concentration.

Figure 3 shows the variation of the PDOS with frequency for the pristine and defective 3WCNT, indicating the characteristic peak at around 53.1 THz, being in an excellent agreement to the reported value in other literature [26,47,48,50]. There is a significant drop in PDOS peaks, justifying the reduction in the thermal conductivity of the CNTs in the presence of vacancies [51]. The peak's frequency shows no sign of dependency on the vacancy concentration that is also in alignment with [10].

![](./images/812771064261115905_6.jpg)

Figure 3. Normalized phonon density of states (PDOS) curves for 3WCNTs with various vacancy concentrations.

To better understand the effect of vacancies on the thermal conductivity of 3WCNTs, the heat transfer in each tube in a pristine 3WCNT was evaluated. To perform this study, each nanotube was imposed with a pair of heat baths (hot and cold) of its own. This was done to find out the heat current in each tube separately. These simulations resulted in the lowest heat current for the inner tube, followed by the middle tube, and the highest heat current for the inner tube, i.e., 51.5 eV, 84.85 eV, and 118.1 eV, respectively. The PDOS curves shown in Figure 4 confirm these results as the inner tube possesses the lowest peak and the outer tube has the highest peak. We have found that these individual heat currents are additive, i.e., their summation yields the heat current passing through the 3WCNT as a whole, under the imposition of heat baths at once on all the nanotubes.

![](./images/812771064261115905_7.jpg)

Figure 4. Normalized PDOS curves for each tube in a 3WCNT. The inset shows the curves for the frequency of 50–55 THz.

The study continues with the inclusion of vacancies in each individual tube to investigate the fundamental effect of the vacancies on the thermal conductivity of 3WCNTs. Two types of simulations were performed; for type-I simulations, the number of vacancies in each individual tube was kept constant, while for type-II simulations, the vacancy concentration in each tube was fixed at 0.5%. Figure 5a shows the variation of the PDOS with the frequency for the 3WCNT when 47 vacancies were positioned in each individual tube. This creates the lowest vacancy concentration in the outer tube, while the vacancy concentration in the entire 3WCNT remains constant. The calculated thermal conductivities for the models with 47 vacancies in inner, middle, and outer tubes are 170.0 W/mK, 154.0 W/mK, and 150.8 W/mK, respectively. PDOS of the 3WCNT when 47 vacancies are in the outer tube shows the lowest peak among other models indicating that this model results in the lowest thermal conductivity. These trends are due to the highest contribution of the outer tube to the heat transfer in a 3WCNT. PDOS for type-II simulations show the same trends as those for type-I's as illustrated in Figure 5b. The same vacancy concentration in each individual tube resulted in the highest number of vacancies in the outer tube, reducing the thermal conductivity of the 3WCNT the most. The calculated thermal conductivities for the models with 0.5% vacancy concentration in inner, middle, and outer tubes are 170.0 W/mK, 149.0 W/mK, and 125.5 W/mK, respectively. Table 1 lists the values of the thermal conductivity for the considered cases.

As mentioned in the introduction, we intend to check if adding a metallic coating on the outer surface of a defective 3WCNT, can alleviate the deteriorating effect of vacancies on the thermal conductivity of the CNT. To that end, models with metal coatings of various thicknesses on defective 3WCNTs were generated and their thermal conductivities were calculated.

Figure 6 shows the variation of the thermal conductivity with the number of atomic layers of Nickel coating for various vacancy concentrations, i.e., pristine 3WCNT, 0.5%, and 1%. The curve for the models with a pristine 3WCNT is taken from our recent publication [32]. The thermal conductivity of a bulk nickel is also included in this figure. It is interesting that the thermal conductivity of nickel is size dependent on nano size-scale. This is in good agreement with [52], where the thermal conductivity of Ni nanoparticles was shown to be size-dependent. As a result of the rule of mixture, the thermal conductivity of the metal-coated 3WCNT is between that for 3WCNT, and the thermal conductivity of the nickel tube. A drop in the thermal conductivity, with the coating thickness is linked to the rule of mixture, and also impeding of vibrations of the carbon atoms in the outer tube by the heavier Ni atoms deposited on them, which leads to phonon scattering at the interface of the two elements [32,53]. Figure 7 shows the variation of PDOS for the 3WCNT and also for the nickel coating when 3 atomic layers of nickel was deposited on the CNT. A significant drop is seen for the PDOS of the 3WCNT, when compared to a CNT, without any coating (see Figure 3). Also, there is almost no region of significant shared PDOS for the metal and the 3WCNT to imply phonon-phonon coupling between them [46,49].

Noting that the phonon scattering remains constant with the coating thickness [54], the decrease in the thermal conductivity of the composite with additional nickel is attributed to the intrinsic lower thermal conductivity of the nickel coating [32].

![](./images/812771064261115905_8.jpg)

Figure 5. (a) Normalized PDOS curves for 3WCNTs with 47 vacancies in each tube (type-I), (b) Normalized PDOS curves for 3WCNTs with 0.5% vacancies in each tube (type-II). The insets show the curves for the frequency of 50-55 THz.

<table>
<thead>
<tr>
<th colspan="3">Type-I (Same Number of Vacancies on Each Tube)</th>
<th colspan="3">Type-II (0.5% Vacancy Concentration on Each Tube)</th>
</tr>
<tr>
<th>Inner (47)</th>
<th>Middle (47)</th>
<th>Outer (47)</th>
<th>Inner (47)</th>
<th>Middle (72)</th>
<th>Outer (94)</th>
</tr>
</thead>
<tbody>
<tr>
<td>170.4335</td>
<td>153.993</td>
<td>150.8788</td>
<td>170.4335</td>
<td>148.9752</td>
<td>125.5104</td>
</tr>
</tbody>
</table>

![](./images/812771064261115905_9.jpg)

Figure 6. Variation in thermal conductivity of a Ni-coated 3WCNT with varying Ni thickness. Each data point shows the average of a set of three simulations implying three different patterns of (same) vacancy concentration.

![](./images/812771064261115905_10.jpg)

Figure 7. Separate PDOS curves for Carbon and Nickel atoms in the composite with three layers on Nickel.

The thermal conductivity of the samples with vacancies increases with the coating thickness. Vacancies in a CNT, with no coating, have resulted in a reduction in the thermal conductivity to a value that is even lesser than the intrinsic thermal conductivity of nickel. Therefore, as per rule of mixture, the addition of nickel helps increase the thermal transport across the structure, thereby, increasing the thermal conductivity of the composite. For 3WCNT models with 0.5% and 1% vacancies, an overall increase of ~66%, and ~140%, respectively, was observed when 3 nm thick nickel coating (18 layers) was deposited around them.

Noting that the models in this work are much shorter than the actual CNTs in a turf of vertically aligned carbon nanotubes, we need to discuss the significance of the length effect on the reported results. It has been repeatedly shown that the thermal conductivity of CNTs increase with length, due to the inclusion of phonons of greater wavelengths [9,10,47,50,55]. However, Park et al. [10] showed that the length dependence of the thermal conductivity vanishes in the presence of vacancies, as no significant change in thermal conductivity was observed even when the length was increased by an order of magnitude, i.e., tenth of micrometer. For such cases, application of metallic coatings can be justified as a means to improve thermal conductivity. Also, the thermal conductivity of the nickel tube is length independent as the mean free path of the thermal transfer in metals is very short. Therefore, the reported results in this work can be applied to CNTs of longer length.

## 4. Conclusions

In this work, we have used non-equilibrium molecular dynamics simulations with two-temperature model (TTM) to study the variation in the thermal conductivity of a metal-coated tri-walled CNT (3WCNT), for different vacancy concentrations. TTM has been specifically employed to capture the electronic contributions to heat transfer in the metallic coatings.

We have found that the outermost tube in the 3WCNT, by virtue of the highest heat current carrying capacity, contributes the most towards heat transfer. The effect of tube specific vacancies on the thermal conductivity of 3WCNT was explored, by imposing the same number of vacancies (type I), and the same vacancy concentration (type II) on each tube. For both cases, the thermal conductivity of the 3WCNT was found to be the most sensitive to the vacancies in the outermost tube. On the other hand, the thermal conductivity of 3WCNT was affected the least when vacancies were only distributed in the innermost tube. To better understand the variation in thermal conductivity, we have also looked into changes in phonon density of states with the frequency of individual tubes and for the entire 3WCNT.

For the standalone 3WCNT model, the introduction of 0.5% and 1% random vacancies (throughout the three tubes) depreciated the thermal conductivity by over 76%, and 86%, respectively. The thermal

conductivities of the defective CNT were lower than the thermal conductivity for the metal coating and thus, the addition of metallic coatings steadily increased the thermal conductivity of the metal-CNT composite. There was an overall ~66% and ~140% increase in the thermal conductivity, with the addition of 3 nm (18 layers) thick metallic coating for 3WCNT, with 0.5%, and 1% vacancies, respectively. Since, the intrinsic thermal conductivities of the metal coating and the defective CNT are understood not to change with length, the obtained results can also be applied to longer CNTs.

Author Contributions: Conceptualization, I.S.; methodology, D.B. and R.S.D.; software, D.B. and R.S.D.; writing—original draft preparation, R.S.D.; writing—review and editing, I.S., R.S.D., and D.B.; supervision, I.S.; project administration, I.S.

Funding: This research received no external funding.

Acknowledgments: This work was supported by the Research and Artistry Award from Northern Illinois University (NIU). Atomistic Simulations were performed in the High-Performance Computing Cluster, GAEA at Northern Illinois University (NIU). The authors acknowledge David. F. Bahr (Purdue University), Yan Wang (University of Nevada, Reno), and John Shelton (Northern Illinois University) for providing us valuable inputs.

Conflicts of Interest: The authors declare no conflict of interest.

References

1.  Fujii, M.; Zhang, X.; Xie, H.; Ago, H.; Takahashi, K.; Ikuta, T.; Abe, H.; Shimizu, T. Measuring the Thermal Conductivity of a Single Carbon Nanotube. *Phys. Rev. Lett.* 2005, 95, 065502. [CrossRef]

2.  Marconnet, A.M.; Panzer, M.A.; Goodson, K.E. Thermal conduction phenomena in carbon nanotubes and related nanostructured materials. *Rev. Modern Phys.* 2013, 85, 1295–1326. [CrossRef]

3.  Aliev, A.E.; Lima, M.H.; Silverman, E.M.; Baughman, R.H. Thermal conductivity of multi-walled carbon nanotube sheets: Radiation losses and quenching of phonon modes. *Nanotechnology* 2010, 21, 035709. [CrossRef]

4.  Lindsay, L.; Broido, D.A.; Mingo, N. Diameter dependence of carbon nanotube thermal conductivity and extension to the graphene limit. *Phys. Rev. B* 2010, 82, 161402. [CrossRef]

5.  Berber, S.; Kwon, Y.K.; Tománek, D. Unusually High Thermal Conductivity of Carbon Nanotubes. *Phys. Rev. Lett.* 2000, 84, 4613–4616. [CrossRef] [PubMed]

6.  Osman, M.A.; Srivastava, D. Temperature dependence of the thermal conductivity of single-wall carbon nanotubes. *Nanotechnology* 2001, 12, 21–24. [CrossRef]

7.  Zhang, W.; Zhu, Z.; Wang, F.; Wang, T.; Sun, L.; Wang, Z. Chirality dependence of the thermal conductivity of carbon nanotubes. *Nanotechnology* 2004, 15, 936. [CrossRef]

8.  Che, J.; Çagin, T.; Goddard, W.A., III. Thermal conductivity of carbon nanotubes. *Nanotechnology* 2000, 11, 65. [CrossRef]

9.  Ohnishi, M.; Shiga, T.; Shiomi, J. Effects of defects on thermoelectric properties of carbon nanotubes. *Phys. Rev. B* 2017, 95, 155405. [CrossRef]

10. Park, J.; Bifano, M.F.P.; Prakash, V. Sensitivity of thermal conductivity of carbon nanotubes to defect concentrations and heat-treatment. *J. Appl. Phys.* 2013, 113, 034312. [CrossRef]

11. Pierret, R.F. *Advanced Semiconductor Fundamentals*, 2nd ed.; Neudeck, G.W., Pierret, R.F., Eds.; Pearson Education, Inc.: Bergen County, NJ, USA, 2002; Volume VI.

12. Chen, G. *Nanoscale Energy Transport and Conversion: A Parallel Treatment of Electrons, Molecules, Phonons, and Photons*; Oxford University Press: Oxford, UK, 2005.

13. Collins, P.G. *Defects and Disorder in Carbon Nanotubes*; Narlikar, A.V., Fu, Y.Y., Eds.; Oxford University Press: Oxford, UK, 2017; Volume 1.

14. Fan, H.; Zhang, K.; Yuen, M.M.F. Effect of defects on thermal performance of carbon nanotube investigated by molecular dynamics simulation. In Proceedings of the 2006 International Conference on Electronic Materials and Packaging, Kowloon, China, 11–14 December 2006; pp. 1–4.

15. Charlier, J.C. Defects in Carbon Nanotubes. *Acc. Chem. Res.* 2002, 35, 1063–1069. [CrossRef]

16. Kotakoski, J.; Krasheninnikov, A.V.; Nordlund, K. Energetics, structure, and long-range interaction of vacancy-type defects in carbon nanotubes: Atomistic simulations. *Phys. Rev. B* 2006, 74, 245420. [CrossRef]

17. Fan, Y.; Goldsmith, B.R.; Collins, P.G. Identifying and counting point defects in carbon nanotubes. *Nat. Mater.* 2005, **4**, 906–911. [CrossRef] [PubMed]

18. Marconnet, A.M.; Yamamoto, N.; Panzer, M.A.; Wardle, B.L.; Goodson, K.E. Thermal Conduction in Aligned Carbon Nanotube–Polymer Nanocomposites with High Packing Density. *ACS Nano* 2011, **5**, 4818–4825. [CrossRef]

19. Chien, S.K.; Yang, Y.T.; Chen, C.K. The effects of vacancy defects and nitrogen doping on the thermal conductivity of armchair (10, 10) single-wall carbon nanotubes. *Solid State Commun.* 2011, **151**, 1004–1008. [CrossRef]

20. Bi, K.; Chen, Y.; Yang, J.; Wang, Y.; Chen, M. Molecular dynamics simulation of thermal conductivity of single-wall carbon nanotubes. *Phys. Lett. A* 2006, **350**, 150–153. [CrossRef]

21. Eres, G.; Puretzky, A.A.; Geohegan, D.B.; Cui, H. In situ control of the catalyst efficiency in chemical vapor deposition of vertically aligned carbon nanotubes on predeposited metal catalyst films. *Appl. Phys. Lett.* 2004, **84**, 1759–1761. [CrossRef]

22. Varshney, V.; Lee, J.; Li, D.; Brown, J.S.; Farmer, B.L.; Voevodin, A.A.; Roy, A.K. Understanding thermal conductance across multi-wall carbon nanotube contacts: Role of nanotube curvature. *Carbon* 2017, **114**, 15–22. [CrossRef]

23. Cross, R.; Cola, B.A.; Fisher, T.; Xu, X.; Gall, K.; Graham, S. A metallization and bonding approach for high performance carbon nanotube thermal interface materials. *Nanotechnology* 2010, **21**, 445705. [CrossRef]

24. Hu, X.; Pan, L.S.; Gu, G.; Goodson, K.E. Superior Thermal Interfaces Made by Metallically Anchored Carbon Nanotube Arrays. In Proceedings of the ASME 2009 InterPACK Conference Collocated with the ASME 2009 Summer Heat Transfer Conference and the ASME 2009 3rd International Conference on Energy Sustainability, San Francisco, CA, USA, 19–23 July 2009; pp. 597–603.

25. Stano, K.L.; Chapla, R.; Carroll, M.; Nowak, J.; McCord, M.; Bradford, P.D. Copper-Encapsulated Vertically Aligned Carbon Nanotube Arrays. *ACS Appl. Mater. Interfaces* 2013, **5**, 10774–10781. [CrossRef]

26. Cui, L.; Feng, Y.; Tang, J.; Tan, P.; Zhang, X. Heat conduction in coaxial nanocables of Au nanowire core and carbon nanotube shell: A molecular dynamics simulation. *Int. J. Therm. Sci.* 2016, **99**, 64–70. [CrossRef]

27. Smith, K.A.; Zbib, M.B.; Bahr, D.F.; Guinel, M.J.F. Elastic behavior of a core–shell metal–carbon nanotube composite foam. *MRS Commun.* 2014, **4**, 77–81. [CrossRef]

28. Hua, Z.; Liu, Y.; Yao, G.; Wang, L.; Ma, J.; Liang, L. Preparation and Characterization of Nickel-Coated Carbon Fibers by Electroplating. *J. Mater. Eng. Perform.* 2012, **21**, 324–330. [CrossRef]

29. Byeon, J.H.; Yoon, H.S.; Yoon, K.Y.; Ryu, S.K.; Hwang, J. Electroless copper deposition on a pitch-based activated carbon fiber and an application for NO removal. *Surf. Coat. Technol.* 2008, **202**, 3571–3578. [CrossRef]

30. Hildreth, O.; Cola, B.; Graham, S.; Wong, C.P. Conformally coating vertically aligned carbon nanotube arrays using thermal decomposition of iron pentacarbonyl. *J. Vac. Sci. Technol. B Nanotechnol. Microelectron. Mater. Process. Meas. Phenom.* 2012, **30**, 03D101. [CrossRef]

31. Zhang, Y.P.; Zhou, H.; Ren, C.L. Research on Surface Metallization of Carbon Fiber Based on Electroless Plating. *Adv. Mater. Res.* 2011, **189**, 1301–1306. [CrossRef]

32. Bommidi, D.; Dhumal, R.S.; Salehinia, I. Study of the thermal conductivity of a metal-coated multi-walled carbon nanotube using molecular dynamics atomistic simulations. *MRS Adv.* 2019, **4**, 507–513. [CrossRef]

33. Che, G.; Lakshmi, B.B.; Martin, C.R.; Fisher, E.R. Metal-Nanocluster-Filled Carbon Nanotubes: Catalytic Properties and Possible Applications in Electrochemical Energy Storage and Production. *Langmuir* 1999, **15**, 750–758. [CrossRef]

34. Wildgoose, G.G.; Banks, C.E.; Compton, R.G. Metal Nanoparticles and Related Materials Supported on Carbon Nanotubes: Methods and Applications. *Small* 2006, **2**, 182–193. [CrossRef]

35. Georgakilas, V.; Gournis, D.; Tzitzios, V.; Pasquato, L.; Guldi, D.M.; Prato, M. Decorating carbon nanotubes with metal or semiconductor nanoparticles. *J. Mater. Chem.* 2007, **17**, 2679–2694. [CrossRef]

36. Ang, L.M.; Hor, T.S.A.; Xu, G.Q.; Tung, C.H.; Zhao, S.P.; Wang, J.L.S. Decoration of activated carbon nanotubes with copper and nickel. *Carbon* 2000, **38**, 363–372. [CrossRef]

37. Biener, J.; Hodge, A.M.; Hamza, A.V. Microscopic failure behavior of nanoporous gold. *Appl. Phys. Lett.* 2005, **87**, 121908. [CrossRef]

38. Plimpton, S. Fast Parallel Algorithms for Short-Range Molecular Dynamics. *J. Comput. Phys.* 1995, **117**, 1–19. [CrossRef]

39. Wang, Y.; Ruan, X.; Roy, A.K. Two-temperature nonequilibrium molecular dynamics simulation of thermal transport across metal-nonmetal interfaces. *Phys. Rev. B* **2012**, *85*, 205311. [CrossRef]

40. Stuart, S.J.; Tutein, A.B.; Harrison, J.A. A reactive potential for hydrocarbons with intermolecular interactions. *J. Chem. Phys.* **2000**, *112*, 6472–6486. [CrossRef]

41. Mishin, Y.; Farkas, D.; Mehl, M.J.; Papaconstantopoulos, D.A. Interatomic potentials for monoatomic metals from experimental data and ab initio calculations. *Phys. Rev. B* **1999**, *59*, 3393–3407. [CrossRef]

42. Tang, X.; Xie, Z.; Yin, T.; Wang, J.W.; Yang, P.; Huang, Q. Classical molecular dynamics simulations of carbon nanofiber nucleation: The effect of carbon concentration in Ni carbide. *Phys. Chem. Chem. Phys.* **2013**, *15*, 16314–16320. [CrossRef]

43. Schelling, P.K.; Phillpot, S.R.; Keblinski, P. Comparison of atomic-level simulation methods for computing thermal conductivity. *Phys. Rev. B* **2002**, *65*, 144306. [CrossRef]

44. Stetter, A.; Vancea, J.; Back, C.H. Conductivity of multiwall carbon nanotubes: Role of multiple shells and defects. *Phys. Rev. B* **2010**, *82*, 115451. [CrossRef]

45. Banhart, F. Interactions between metals and carbon nanotubes: At the interface between old and new materials. *Nanoscale* **2009**, *1*, 201–213. [CrossRef]

46. Zhong, H.; Lukes, J.R. Interfacial thermal resistance between carbon nanotubes: Molecular dynamics simulations and analytical thermal modeling. *Phys. Rev. B* **2006**, *74*, 125403. [CrossRef]

47. Lukes, J.R.; Zhong, H. Thermal Conductivity of Individual Single-Wall Carbon Nanotubes. *J. Heat Transf.* **2007**, *129*, 705. [CrossRef]

48. Rogers, D.J. Molecular Dynamics Simulation of the Carbon Nanotube—Substrate Thermal Interface Resistance. Ph.D. Thesis, Georgia Institute of Technology, Atlanta, GA, USA, 2009.

49. Gao, F.; Qu, J.; Yao, M. Interfacial thermal resistance between metallic carbon nanotube and Cu substrate. *J. Appl. Phys.* **2011**, *110*, 124314. [CrossRef]

50. Maruyama, S. A molecular dynamics simulation of heat conduction in finite length SWNTs. *Phys. B Condens. Matter* **2002**, *323*, 193–195. [CrossRef]

51. Hone, J. Phonons and Thermal Properties of Carbon Nanotubes. In *Carbon Nanotubes: Synthesis, Structure, Properties, and Applications*; Dresselhaus, M.S., Dresselhaus, G., Avouris, P., Eds.; Topics in Applied Physics; Springer: Berlin/Heidelberg, Germany, 2001; pp. 273–286.

52. Yuan, S.P.; Jiang, P.X. Thermal Conductivity of Small Nickel Particles. *Int. J. Thermophys.* **2006**, *27*, 581–595. [CrossRef]

53. Thomas, J.A.; Iutzi, R.M.; McGaughey, A.J.H. Thermal conductivity and phonon transport in empty and water-filled carbon nanotubes. *Phys. Rev. B* **2010**, *81*, 045413. [CrossRef]

54. Ju, S.; Liang, X.; Wang, S. Investigation of interfacial thermal resistance of bi-layer nanofilms by nonequilibrium molecular dynamics. *J. Phys. D Appl. Phys.* **2010**, *43*, 085407. [CrossRef]

55. Salaway, R.N.; Zhigilei, L.V. Molecular dynamics simulations of thermal conductivity of carbon nanotubes: Resolving the effects of computational parameters. *Int. J. Heat Mass Transf.* **2014**, *70*, 954–964. [CrossRef]

![](./images/812771064261115905_11.jpg)

© 2019 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/).