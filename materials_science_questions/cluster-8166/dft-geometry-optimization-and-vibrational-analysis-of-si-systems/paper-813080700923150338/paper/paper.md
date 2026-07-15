![](./images/813080700923150338_1.jpg)

Surface Science 375 (1997) 45-54

![](./images/813080700923150338_2.jpg)

# A molecular dynamics study of the chemisorption of $C_2H_2$ and $CH_3$ on the $Si(001)$-(2 × 1) surface

A.J. Dyson, P.V. Smith *

Department of Physics, University of Newcastle, Callaghan, Australia, 2308

Received 7 August 1996; accepted for publication 17 October 1996

## Abstract

Chemisorption of $C_2H_2$ and $CH_3$ molecules onto the dimerized (001) surface of silicon has been simulated using the extended Brenner potential. For reference, chemisorption energies and minimum-energy geometries have also been obtained from Hartree-Fock and Becke3LYP DFT calculations performed with the Gaussian-94 suite. Various chemisorption sites have been identified. Optimal $C_2H_2$ chemisorption was found to occur in a cross-dimer configuration, parallel to the dimer rows. Optimal $CH_3$ chemisorption occurred with the $CH_3$ bonding directly to the surface dangling bonds. A second-layer chemisorption site for $CH_3$ has also been identified, which may be important in the formation of diamond films on a silicon substrate. © 1997 Elsevier Science B.V. All rights reserved.

Keywords: Alkynes; Chemisorption; Construction and use of effective interatomic interactions; Molecular dynamics; Low index single crystal surfaces; Methyl radical; Silicon

## 1. Introduction

Heteroepitaxial growth of diamond on silicon is a desirable but elusive goal. One promising method for achieving single-crystal diamond growth is chemical vapor deposition (CVD). Initially, the CVD process involves the chemisorption of small hydrocarbon molecules and fragments onto the clean silicon surface. The determination of the chemisorption mechanisms and configurations involved at these initial stages will provide valuable information contributing to a thorough description of the entire growth process.

CVD diamond is often grown using methane gas, which is introduced into the chamber and then activated by a hot filament or microwave plasma. This activation is thought to produce methyl radicals and acetylene molecules, which then diffuse to the surface and become the primary species involved in deposition. Both of these species have been shown experimentally to bond readily to the clean silicon (001) surface [1,2]. In the current study we have performed molecular dynamics simulations using the extended Brenner (XB) empirical potential in order to identify pos- sible chemisorption sites for acetylene and the methyl radical on the Si(001) dimerized surface. We have then determined the optimal chemisorp- tion configurations at these sites using both the XB potential and accurate Hartree-Fock DFT techniques as described below.

The XB potential is a multi-particle interatomic potential of the cluster-functional type. Following

*Corresponding author. Fax: +61 49 216907;
e-mail: phpvs@cc.newcastle.edu.au

0039-6028/97/$17.00 Copyright © 1997 Elsevier Science B.V. All rights reserved
PII S0039-6028(96)01261-7

the Tersoff formalism, it takes into account the chemical environment of each bond when calculat- ing the bond energy. The original Brenner potential was developed for C-H systems [3], and parame- ters have since been reported which extend its capabilities to C-H-Si systems [4].

As with all empirical potentials, the XB potential is computationally inexpensive. This allows simula- tions to be performed which model quite long atomic time scales, using only a few hours on a typical workstation. The XB potential incorporates carbon, silicon and hydrogen within the same functional framework, hence providing a means of modelling the interactions between hydrocarbon molecules in the gas phase and a silicon surface without the computational demands of the more sophisticated ab-initio techniques. For these reasons, we have elected to use the XB potential in our investigations of this system.

Initially, a large number of simulations were carried out allowing individual molecules to impinge upon the clean Si(001)-(2 × 1) surface. The starting point, aiming point and rotational orienta- tion were all randomly chosen. In each case the incident molecule was rotationally and vibration- ally cold, and the translational energy was set at between 0.20 and 1.0 eV.

The surface itself was modelled by a 128-atom slab eight layers deep, with two-dimensional peri- odic boundary conditions applied in the surface plane. The unit cell is shown in Fig. 1, complete with a chemisorbed acetylene molecule. During the simulations the bottom two layers were held fixed, and the next two layers used as a thermal buffer layer with the velocities rescaled after every times- tep. This rescaling was necessary to simulate dissi- pation of the molecular translational energy into the bulk, as well as to correct for thermal drift. Velocity rescaling was not applied to the remainder of the slab, or to the adsorbate molecules.

The simulation trajectories were examined in order to identify important chemisorption sites. Once these were located, minimum-energy chemi- sorption geometries were obtained by allowing all of the atomic coordinates of the adsorbate and the top six substrate layers to relax until the forces were in equilibrium.

To further characterise the chemisorption, ab- initio Hartree-Fock calculations were performed with GAUSSIAN-94 [5], using an unrestricted Hartree-Fock Hamiltonian and the 3-21g* basis set, as well as applying the Becke3LYP [6-9] density-functional correlation correction. Struc- tures involving a single silicon dimer were mod- elled using a cluster of nine silicon atoms, with 12 hydrogen atoms used to terminate the bonds at the edges of the cluster.

## 2. Results and discussion

### 2.1. $C_2H_2$

On the Si(001)-(2 × 1) surface there are singly occupied dangling bonds at the ends of each surface dimer which provide easily accessible bonding sites for gas molecules incident on the surface. A thor- ough description of the chemistry of the various surfaces of silicon can be found in Ref. [10]. Acetylene, due to its reactive triple bond, has a high probability of reacting with a surface dangling bond, undergoing electronic rehybridization, and sticking to the surface.

Molecular dynamics simulations, both in this study and that of Carmer et al. [11], have shown that initially the most likely scenario is for one of the carbon atoms to bond at a single dangling bond site. This gives rise to mono-$\sigma$ structures such as that shown in Fig. 1.

In the mono-$\sigma$ configuration, only one new bond is formed between the adsorbate molecule and the

![](./images/813080700923150338_3.jpg)

Fig. 1. Si(001) 128-atom unit cell used for the XB calculations, illustrating the mono-$\sigma$ structure observed for initial $C_2H_2$ chemisorption.

surface. Energetically it is more favourable for the acetylene molecule to bond in such a way that both of the carbon atoms form bonds to one or more surface silicon atoms. In this study we have examined several di-$\sigma$ structures for $\text{C}_2\text{H}_2$ chemi- sorption on Si(001), in which each carbon atom is bonded to a single surface atom. A structure in which the carbon atoms are each bonded to two surface atoms was also investigated.

Fig. 2 is a top view of the Si(001) dimerized surface, showing seven locations where $\text{C}_2\text{H}_2$ could conceivably be chemisorbed. These are the dimer bridge site (B), cave site (C1, C2), pedestal site (P), dimer row site (R), and valley site (A). During the molecular dynamics simulations carried out in this study, chemisorption at sites B, R and D was observed, as well as the mono-$\sigma$ structure described earlier. Chemisorption at sites A, C1, C2 and P did not occur. Examination of the cave sites, C1 and C2, shows that the minimum possible Si–C distance is too great to allow bonds to form between the adsorbate molecule and the silicon dimer atoms. Chemisorption at the pedestal site (P) involves great distortion of the dimer dangling bonds, and because the pedestal site is so close to the much-preferred dimer bridge site, chemisorp- tion at P is unlikely. For the valley site (cross- dimer site A), if the neighbouring silicon dimers are in their usual relaxed positions, then the Si–C distance is too great to allow bond formation. If, however, the dimers happen to move laterally toward one another, perhaps as a result of thermal vibration, it is possible for a $\text{C}_2\text{H}_2$ molecule to bond at this site.

In this study we have found minimum energy structures corresponding to $\text{C}_2\text{H}_2$ chemisorption at sites A, B, D and R. The binding energies are listed in Table 1. We will now describe each of the chemisorption structures in turn.

The first of the di-$\sigma$ structures results from chemisorption at site B, the dimer bridge site. In this case, the acetylene molecule lies with its carbon–carbon bond directly above and parallel to the silicon surface dimer. The silicon dimer itself can remain intact, as shown in Fig. 3, or it can be broken, as shown in Fig. 4. Figs. 3 and 4 also show the optimized geometries we have obtained for these structures. The geometry and energy pre- dicted by the XB potential for $\text{C}_2\text{H}_2$ chemisorption at the dimer bridge site with the dimer remaining

![](./images/813080700923150338_4.jpg)

Fig. 2. Top view of the Si(001)-(2×1) surface. The hatched circles represent the silicon dimer atoms in their relaxed positions. Also shown are the $\text{C}_2\text{H}_2$ chemisorption sites investigated in this study.

Table 1
Binding energies for $\text{C}_2\text{H}_2$ chemisorbed on the Si(001) surface (in eV per adsorbate molecule); the chemisorption sites are clearly identified in Fig. 2

<table>
  <thead>
    <tr>
      <th>Structure</th>
      <th>Fig.</th>
      <th>XB (eV)</th>
      <th>UHF/3-21 g* (eV)</th>
      <th>Becke3LYP/3-21 g* (eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bridge site, dimer intact</td>
      <td>3</td>
      <td>3.35</td>
      <td>3.39</td>
      <td>3.17</td>
    </tr>
    <tr>
      <td>Bridge site, dimer broken</td>
      <td>4</td>
      <td>3.63</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cross-dimer site R</td>
      <td>6</td>
      <td>3.75</td>
      <td>2.13</td>
      <td>2.57</td>
    </tr>
    <tr>
      <td>Cross-dimer site A</td>
      <td>7</td>
      <td>3.60</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cross-dimer site D</td>
      <td>8</td>
      <td>3.50</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

![](./images/813080700923150338_5.jpg)

Fig. 3. Si(001)-(2×1): $\text{C}_2\text{H}_2$ bridge site structure with intact dimer: (a) XB geometry, (b) Becke3LYP geometry. Only the immediate geometry of the chemisorption site has been shown for the sake of clarity.

intact is seen to be in good agreement with that given by the ab-initio calculations. Such a comparison can not be made for the cleaved-dimer structure, because a local energy minimum for this structure could not be obtained in our cluster Hartree–Fock calculations.

Previously published studies largely agree that the optimal site for acetylene chemisorption is at the dimer bridge site. There is, however, some dispute regarding whether the underlying silicon dimer remains intact after chemisorption or whether it is cleaved. Taylor et al. [2] promote a cleaved dimer on the basis of their TPD and AES studies. Huang et al. [12] support the findings of Taylor et al. based on HREELS analysis of the $\text{Si(001):C}_2\text{H}_2$ surface. The AM1 calculations of Carmer et al. [11] have also yielded a cleaved dimer for the optimal bridge site structure.

On the other hand, Nishijima et al. [13] have proposed, on the basis of an experimental study involving HREELS and LEED, a structure with the dimer maintained. The semi-empirical Hartree–Fock calculations of Craig and Smith [14], and the ab-initio DFT calculations of Imamura et al. [15], both give a minimum-energy structure which has the silicon dimer bond maintained, although in a slightly stretched and weakened state. Using a model with an intact dimer, Imamura et al. [15] calculated the vibrational mode frequencies of the molecule–dimer system.

![](./images/813080700923150338_6.jpg)

Fig. 4. Si(001)-(2×1):C₂H₂ bridge site structure with broken dimer (XB geometry).

Their theoretically determined vibrational-mode frequencies agree very well with the HREELS measurements of Nishijima et al. [13].

Liu and Hoffmann [16] performed a number of calculations investigating acetylene chemisorption on a Si(001) dimer, using both cluster and periodic models. All of the calculations which they have reported yield an optimal structure with an intact dimer. These authors have described chemical reaction mechanisms by which the bridge-site chemisorption process may proceed, and have discussed the interesting changes in the electronic structure of the surface which would occur during these reactions.

In this current study we have found that the two possible bridge-site structures have quite similar binding energies; 3.35 eV for the dimerized structure, and 3.63 eV for the dimer-cleaved structure. The variation of binding energy versus dimer length is plotted in Fig. 5. To calculate these energies, we performed partial geometry optimizations in which the dimer length was held fixed whilst all of the other coordinates were allowed to relax. Clear minima exist for both structures, with an activation barrier of around 0.4 eV to transform from the dimer-cleaved structure to the dimerized structure.

The other structures we have investigated involve the molecule bridging across two silicon dimers. Fig. 6 illustrates a structure where the chemisorbed acetylene molecule bridges at the side of two neighbouring dimers from the same row, referred to here as structure R. A second possibility is that shown in Fig. 7, where the molecule bridges across dimers from adjacent dimer rows, which we denote structure A. Thirdly, if the acetylene molecule is incident over the midpoint of two adjacent dimers from the same dimer row, a structure can occur where each of the carbon atoms is bonded to two top-layer silicon atoms. The carbon atoms now occupy sites corresponding to a diamond overlayer. In the following discussion we refer to this structure, which is illustrated in Fig. 8, as structure D.

![](./images/813080700923150338_7.jpg)

Fig. 5. Plot of binding energy versus Si dimer length for C₂H₂ chemisorption at the dimer bridge site.

![](./images/813080700923150338_8.jpg)

Fig. 6. Si(001)-(2×1):C₂H₂ cross-dimer structure R, with the C₂H₂ molecule bonded to one side of two dimers from the same dimer row.

![](./images/813080700923150338_9.jpg)

Fig. 7. Si(001)-(2×1):C₂H₂ cross-dimer structure A, with the C₂H₂ molecule bonded to two dimers from adjacent dimer rows.

The XB binding energies for these three structures were 3.75 eV for structure R, 3.60 eV for structure A and 3.50 eV for structure D. All of these binding energies are very close to the binding energy of 3.68 eV which was found for bridge-site chemisorption. In principle, we could expect to see all four structures appearing in the course of MD simulations. In practice, although structures R and D have been obtained from simulations performed with randomly chosen starting conditions, we have not observed the formation of structure A at all within the simulations we have performed. If the incident trajectory of the molecule is such that it is aimed directly at the point midway between two adjacent dimers in the $[\overline{1}10]$ direction, the molecule tends to move toward one of the dimers and bond to it alone. The optimized geometry for structure A was achieved by placing the molecule initially between two such dimers at approximately the final configuration and allowing the system to relax.

Comparing the binding energies of all of the Si(001):C₂H₂ configurations which we have examined in this study, the overall minimum energy structure predicted by the XB potential is the row-parallel structure R. This structure has a binding energy of 3.75 eV, as compared to 3.63 eV for chemisorption at the bridge site. All of the previous studies cited in the discussion above have concluded that the dimer bridge site is the energetically preferred site for C₂H₂ chemisorption on Si(001). Of these, however, only two theoretical studies have examined the cross-dimer sites.

Carmer et al. [11] have reported studies of Si(001):C₂H₂ utilising a hybrid technique which combines the semi-empirical AM1 method [17] with the Stillinger-Weber empirical potential for Si [18]. Within the substrate slab, the atoms immediately surrounding the chemisorption site are represented using AM1, whilst the remainder of the slab is modelled with the SW potential. In this way the AM1 calculation is restricted to a manageable size, and at the same time lattice strain effects are included due to the relaxation of the top eight substrate layers. Chemisorption configurations were investigated using MD simulations, with the molecule impinging on the surface at normal incidence. Optimized structures were

![](./images/813080700923150338_10.jpg)

Fig. 8. Si(001)-(2×1):C₂H₂ cross-dimer structure D, with the C₂H₂ molecule situated above the centre of two dimers from the same dimer row. Hatched circles indicate the positions of the atoms before C₂H₂ chemisorption.

obtained by dynamically quenching the system; kinetic energy was rapidly removed by setting atomic velocities to zero when passing through a maximum value, as described fully in Ref. [11].

In their study, Carmer et al. chose aiming points for the $C_2H_2$ molecule corresponding to chemisorption at the bridge site and the two cross-dimer sites, R and A. Optimal chemisorption occurred at the bridge site with the underlying silicon dimer broken, and with a binding energy of 2.98 eV. Chemisorption at the cross-dimer site R was also observed, with a binding energy of 2.67 eV. When the aiming point was midway between the dimer rows, corresponding to a cross-dimer site A, the molecule was seen to deviate from its straight-line path and stick to just one of the dimers in a mono-$\sigma$ configuration. The observations made by Carmer et al. are thus qualitatively very similar to those which we have made in the course of this study.

Craig and Smith [14] have used the periodic SLAB-MINDO technique to study $C_2H_2$ chemisorption on Si(001)-(2×1), and have included in their study the cross-dimer structures A and D. They reported that at monolayer coverage, structure A does not form. Instead the silicon dimers break, leading to the formation of the bridge-site dimer-cleaved structure shown in Fig. 4. With regard to structure D, Craig and Smith report that the binding energy for $C_2H_2$ at this site is 1.50 eV less than that for optimal chemisorption at the bridge site.

The calculations of Craig and Smith [14] were performed for an acetylene coverage of one monolayer. This imposes certain symmetry constraints on the system which do not apply to our current single-molecule chemisorption structures. For example, in the cross-dimer structure A shown in Fig. 7, the silicon dimers have moved laterally towards one other by a significant amount. At a coverage of one monolayer, acetylene molecules would be present on both sides of each dimer, so this asymmetrical sideways movement of the dimers is not possible. Craig and Smith did not examine the cross-dimer structure R.

We have optimized the top two layers of the cluster illustrated in Fig. 9 with Becke3LYP/3-21g*, and obtained a binding energy of 2.57 eV for $C_2H_2$ at site R, compared with the XB binding energy at that site of 3.75 eV. It is likely that the ab-initio calculation has substantially underestimated the binding energy for this structure. Chemisorption at site R involves large displacements of the substrate atoms from their clean-surface positions, and the cluster that has been used to model the chemisorption site is too small to allow for the amount of relaxation necessary to describe the structure properly. In principle a larger cluster could be employed, but this was beyond the capacity of the computational facilities available for this study. Previously published ab-initio studies have not addressed any of the cross-dimer sites.

![](./images/813080700923150338_11.jpg)

Fig. 9. Cluster used to model the cross-dimer structure R in Becke3LYP/3-21g* calculations of $C_2H_2$ chemisorption on Si(001)-(2×1). The hatched circles represent the hydrogen atoms employed to saturate the dangling bonds at the extremities of the cluster.

### 2.2. $CH_3$

The $CH_3$ radical is thought to be produced by the activation of $CH_4$ by microwaves or by contact

with a hot filament. It is extremely reactive, and hence any methyl radical reaching the surface can be expected to stick.

In the course of our MD simulations we observed two important sites for $\mathrm{CH}_{3}$ chemisorption on $\mathrm{Si}(001)$. The binding energies for $\mathrm{CH}_{3}$ chemisorption at these sites are given in Table 2.

The most commonly observed structure was the chemisorption of the $\mathrm{CH}_{3}$ radical directly onto a dangling bond, as illustrated in Fig. 10. Also shown in Fig. 10 are the optimized geometries obtained from the XB and Becke3LYP/3-21g* methods. Good agreement between the XB and Becke3LYP/3-21g* geometries is again observed, although there is clearly more tilting of the Si-Si dimer bond for the XB potential. Fig. 11 presents the corresponding geometries obtained for methyl radicals chemisorbed at both ends of a single silicon dimer.

In this study we have found that the dangling- bond site is clearly the optimal site for $\mathrm{CH}_{3}$ chemisorption. The binding energy was calculated with the XB potential, and found to be 3.28 eV for the first $\mathrm{CH}_{3}$ and 3.14 eV for the second $\mathrm{CH}_{3}$. This is comparable to the binding energy for $\mathrm{CH}_{3}$ on the unreconstructed $\mathrm{Si}(111)$ surface, which was calculated to be 3.38 eV by Yang et al. [19] using ab-initio configuration interaction methods.

The other observed site involved the bonding of the carbon atom to a second-layer silicon atom in between the dimer rows, as shown in Fig. 12. For second-layer chemisorption onto a clean surface we have calculated the binding energy to be 2.36 eV. We also find that after all the surface dangling bonds are saturated, $\mathrm{CH}_{3}$ can still bond to the second-layer silicon atoms with a binding energy of 2.25 eV. This site may be quite important for the formation of a diamond film, as the large

Table 2
Binding energies for $\mathrm{CH}_{3}$ chemisorption on $\mathrm{Si}(001)$, in eV per adsorbate molecule

<table><thead>
  <tr>
    <th>Structure</th>
    <th>Fig.</th>
    <th>XB (eV)</th>
    <th>UHF/3-21 g* (eV)</th>
    <th>Becke3LYP/3-21 g* (eV)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Dangling bond, one</td>
    <td>10</td>
    <td>3.28</td>
    <td>3.44</td>
    <td>3.33</td>
  </tr>
  <tr>
    <td>Dangling bond, two</td>
    <td>11</td>
    <td>3.21</td>
    <td>2.69</td>
    <td>3.51</td>
  </tr>
  <tr>
    <td>Dangling bond, 1 ML</td>
    <td></td>
    <td>3.18</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Second-layer site</td>
    <td>12</td>
    <td>2.36</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>1 ML+second-layer site</td>
    <td></td>
    <td>2.25 for the second-layer site</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

![](./images/813080700923150338_12.jpg)

Fig. 10. $\mathrm{Si}(001)-(2 \times 1): \mathrm{CH}_{3}$ chemisorption at a dangling bond: (a) XB geometry, (b) Becke3LYP geometry.

![](./images/813080700923150338_13.jpg)
![](./images/813080700923150338_14.jpg)

Fig. 11. Si(001)-(2×1):2CH₃ chemisorption at both ends of a dangling bond: (a) XB geometry, (b) Becke3LYP geometry.

![](./images/813080700923150338_15.jpg)

Fig. 12. Si(001)-(2×1):CH₃ chemisorption at a second-layer silicon atom.

lattice mismatch between silicon and diamond necessitates greater than 1 ML coverage of carbon in order to obtain such a film. Chemisorption at the second layer is one way in which this could be achieved.

Although the methyl radical is thought to be very significant in diamond CVD growth generally [20,21], few theoretical studies of CH₃ chemisorption on silicon have so far appeared in the literature.

Feng et al. [22] have performed $X_α$ calculations on the Si(001)-(2×1):CH₃ system, choosing four positions on the surface and in each case allowing the adsorbate to relax in only the vertical direction [22]. Only the bridge, cave, pedestal and valley-bridge sites were examined, and the possibility of CH₃ chemisorption directly onto a dangling bond was not discussed. The bridge site was found to be the most energetically favourable, and no chemisorption was observed at the cave site. In these calculations the substrate atoms were fixed in position, allowing for no surface relaxation or reconstruction during the chemisorption process.

Feng et al. [22] have reported a binding energy of 2.86 eV for chemisorption at the bridge site, with the carbon atom at a height of 2.38 Å from the surface plane. Such a structure has a minimum Si–C distance of 2.69 Å, much longer than the equilibrium Si–C bond length of 1.88 Å predicted by Hartree–Fock calculations of the SiH₃CH₃ molecule. It is difficult to compare the results of Feng et al. with other theoretical results, or indeed with experimental measurements, due to the very limited number of degrees of freedom in their geometry optimizations. Without imposing unrealistic constraints upon relaxation of the molecule/substrate system, we have been unable to obtain the structures reported in Ref. [22].

### 3. Concluding remarks

The diamond thin-film growth experiments reported to date mostly involve acetylene or the methyl radical as the primary growth species. In our MD simulations, both C₂H₂ and CH₃ have been shown to bond to the clean Si(001) dimerized surface very readily and at a number of different sites.

Our theoretical results show that of these two species, the methyl radical is the better choice for carbon deposition on the clean Si(001) surface. Firstly, the binding energy per carbon atom is almost twice that for acetylene. Secondly, greater than 1.0 monolayer coverage can be achieved using $CH_3$, due to the possibility that it may to chemi- sorb at the second layer between the dimer rows.

Following the deposition of the first adsorbate layer, the next stage of diamond growth is highly dependent upon the creation of new chemisorption sites by the removal of surface hydrogen. Further calculations are underway to investigate such events, by simulating the incidence of both atomic hydrogen and further $CH_3$ radicals on the fully saturated Si(001) surface. The (001) surface of silicon carbide is also of interest, and similar calcu- lations will soon be reported for chemisorption of small hydrocarbons on this surface.

## Acknowledgements

We would like to thank the Australian National University Supercomputer Facility for enabling us to perform some of the calculations for this study on the Fujitsu VP-2200 supercomputer. A.J.D. wishes to acknowledge the Australian Government and the University of Newcastle for the award of a postgraduate research scholarship.

## References

[1] J.A. Stroscio, S.R. Bare and W.H. Ho, Surf. Sci. 154 (1985) 35.

[2] P.A. Taylor, R.M. Wallace, C.C. Cheng, W.H. Weinberg, M.J. Dresser, W.J. Choyke and J.T. Yates, Jr., J. Am. Chem. Soc. 114 (1992) 6754.

[3] D.W. Brenner, Phys. Rev. B 42 (1990) 9458; Erratum, Phys. Rev. B 46 (1992) 1948.

[4] A.J. Dyson and P.V. Smith, Surf. Sci. 355 (1996) 140.

[5] M.J. Frisch, G.W. Trucks, H.B. Schlegel, P.M.W. Gill, B.G. Johnson, M.A. Robb, J.R. Cheeseman, T.A. Keith, G.A. Petersson, J.A. Montgomery, K. Raghavachari, M.A. Al-Laham, V.G. Zakrzewski, J.V. Ortiz, J.B. Foresman, J. Cioslowski, B.B. Stefanov, A. Nanayakkara, M. Challacombe, C.Y. Peng, P.Y. Ayala, W. Chen, M.W. Wong, J.L. Andres, E.S. Replogle, R. Gomperts, R.L. Martin, D.J. Fox, J.S. Binkley, D.J. Defrees, J. Baker, J.P. Stewart, M. Head-Gordon, C. Gonzalez and J.A. Pople, Gaussian 94 (Revision B.1) (GAUSSIAN Inc., Pittsburgh, 1994).

[6] A.D. Becke, J. Chem. Phys. 98 (1993) 5648.

[7] C. Lee, W. Yang and R.G. Parr, Phys. Rev. B 37 (1988) 785.

[8] A.D. Becke, Phys. Rev. A 38 (1988) 3098.

[9] B. Miehlich, A. Savin, H. Stoll and H. Preuss, Chem. Phys. Lett. 157 (1989) 200.

[10] H.N. Waltenburg and J.T. Yates, Jr., Chem. Rev. 95 (1995) 1589.

[11] C.S. Carmer, B. Weiner and M. Frenklach, J. Chem. Phys. 99 (1993) 1356.

[12] C. Huang, W. Widdra, X.S. Wang and W.H. Weinberg, J. Vac. Sci. Technol. A 11 (1993) 2250.

[13] M. Nishijima, J. Yoshinobu, H. Tsuda and M. Onchi, Surf. Sci. 192 (1987) 383.

[14] B.I. Craig and P.V. Smith, Surf. Sci. 276 (1992) 174; Erratum, Surf. Sci. 285 (1993) 295.

[15] Y. Imamura, Y. Morikawa, T. Yamasaki and H. Nakatsuji, Surf. Sci. 341 (1995) L1091.

[16] Q. Liu and R. Hoffmann, J. Am. Chem. Soc. 117 (1995) 4082.

[17] M.J.S. Dewar, E.G. Zoebisch, E.F. Healy and J.J.P. Stewart, J. Am. Chem. Soc. 107 (1985) 3902.

[18] F.H. Stillinger and T.A. Weber, Phys. Rev. B 31 (1985) 5262.

[19] H. Yang, Z. Jing and J.L. Whitten, J. Electron Spectrosc. Relat. Phenom. 69 (1994) 23.

[20] K. Feng and Z. Lin, in: The Structure of Surfaces, Vol. IV, Eds. X. Xie, S.Y. Tong and M.A. van Hove (World Scientific, Singapore, 1994) pp. 195-200.

[21] K.A. Brown and W. Ho, Surf. Sci. 338 (1995) 111.

[22] K. Feng, Z.H. Liu and Z. Lin, Surf. Sci. 329 (1995) 77.