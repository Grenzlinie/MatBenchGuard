2nd Int'l Conf. on Electrical Engineering and Information & Communication Technology (ICEEICT) 2015
Jahangirnagar University, Dhaka-1342, Bangladesh, 21-23 May 2015

# Numerical Analysis on Vibrational Properties of Vacancy-type Disordered Graphane

Md. Sherajul Islam, Ashraful G. Bhuiyan, Md. Fahim-Al-Fattah
Department of Electrical & Electronic Engineering
Khulna university of Engineering and Technology
Khulna-9203, Bangladesh
sheraj_ruet@yahoo.com

Akihiro Hashimoto
Department of Electrical & Electronic Engineering
University of Fukui
Fukui 910-8507, Japan
akihirohashimoto@hotmail.com

**Abstract**—We theoretically explore the vacancy induced vibrational properties of graphane using the forced vibrational method. We find strong changes in the phonon density of states for vacancy-type disordered graphane, revealing the significant impacts on the electron transport properties. The phonon eigenvectors estimated for the K point in-plane transverse optical mode for the defective graphane show the strongly localized vibrations. The localization effects manifest themselves in the projected temperature behavior of the constant-volume specific heat capacity of pristine and disordered graphane samples.

**Keywords**—phonon density of states; disordered graphane; localized vibrations; specific heat capacity

## I. INTRODUCTION

Graphane, an extended two-dimensional covalently bonded hydrocarbon by reversible hydrogenation of graphene has attracted immense interest recently [1]-[2]. It has been demonstrated that the hydrogenation of graphene is controllable and the original properties of graphene can be largely restored by annealing the graphene samples at high temperature. In contrast to the perfect graphene, a fully hydrogenated graphene, i.e. graphane is a wide band gap material [1], [3]. This engenders an alternative avenue for tuning the energy gap of graphene that could open the gate for enormous technological and industrial applications for graphane, such as hydrogen storage and two dimensional nano-electronics. In any carbon-based material, the motion of valence electrons will create significant changes in equilibrium structures and give rise to electron-phonon coupling [4]. Therefore, the study of the vibrational properties is of fundamental importance for electron transport in graphene-based materials.

It is well-known that various types of disorders such as topological defects, impurity states, ripples, cracks etc. may present in graphene. Quite clearly such types of disorders are also expected to be present in graphane. These disorders have a striking effect on the electronic structure of graphane. Pujari et al. [5] carried out an ab initio electronic structure calculation on graphane having single and double vacancy defects. Their analysis of the density of states reveals that such vacancies induce the mid-gap states and modify the band gap.

Like graphene, even small concentrations of defects such as vacancies in graphane may also alter the vibrational properties significantly and thus change their optical absorption, low temperature specific heat and transport properties. Hence, it is particularly imperative to uncover the detail information about the defects effects on the vibrational properties of graphane as they govern electron transport, and hence the performance of graphane-based devices.

To date, very few works have been performed on the vibrational properties of graphane [6]. Some works have considered the influence of the H vacancies on the thermal properties of graphane [7]. To the best of our knowledge, there are no reports of systematic investigations of the defects effects on the vibrational properties of graphane. The defects induce the symmetry breakdown of elemental topological arrangements, which generate more complex lattice structures. Therefore, the dynamical matrix calculation requires huge computational resources. These long computational times and convergence problems in the dynamical matrix calculations limit the systems of interest to benchmark molecules. However, the finite-size effects influence the result of the vibration modes in the low-frequency regime significantly. Thus, the numerical study of the phonon modes for very large clusters is necessary in order to obtain correct insight into the vibrational properties of disordered graphane.

In this work, we focus on the vibrational properties of graphane with vacancy-type defects created by removal of different concentrations of carbon and hydrogen atoms. Such defects are experimentally realized by using high-energy ion beams as demonstrated by Jin et al. [8] by creating a stable carbon chain from a graphene sheet. We employ the forced vibrational method, which is a powerful technique for computing the eigenvalues and the corresponding eigenvectors of large-scale systems. We calculate the change of the phonon density of states for different concentrations of vacancy-type defects in the graphane. If there is a high density of scatterers in the medium, exponential localization of eigenmodes can be induced, i.e. the amplitudes decay exponentially along the medium with a rate of decay inversely proportional to a certain localization length [9]. The extent of localization due to the defects is quantified by the typical mode patterns. Differences of the temperature dependence of specific heat

978-1-4673-6676-2/15/$31.00 ©2015 IEEE

capacity calculated from the phonon density of states between the pristine and disordered graphane structures has also been discussed.

## II. COMPUTATIONAL DETAILS

The forced vibrational (FV) method introduced by Williams and Marris [10] has been used in the theoretical investigation of the vibrational properties of graphane with vacancies. This method is based on the principle that a linear mechanical system when driven by a periodic external force of frequency $\Omega$ will respond with large amplitudes in those eigenmodes close to this frequency. By counting the number of excited eigenmodes, we can obtain the density of states around the frequency of the applied field. According to the formalism of FV method, a random force given by
$$F_{l}=F_{0}\sqrt{M_{l}}\cos(\varphi_{l})\cos(\Omega t)$$
is applied to the each atom of a system consists of $N$ atoms connected by linear springs between nearest-neighbors. Here $F_{0}$ is a constant and $\varphi_{l}$ is a random quantity distributed uniformly in the range $[0,2\pi]$. After a sufficiently large time $T$, the system gives the averaged value of energy by the forced vibration over as:
$$\langle E(\Omega,T)\rangle\approx\frac{\pi tF_{0}^{2}}{8}\sum_{\lambda}\delta(\omega_{\lambda}-\Omega)=\frac{\pi tNF_{0}^{2}}{8}g(\Omega)(1)$$
where $\omega_{\lambda}$ is an eigenfrequency of mode $\lambda$. Therefore, the density of states (DOS) of the system can be related to the total energy as given by:
$$g(\Omega)=\frac{8\langle E(\Omega,T)\rangle}{F_{0}^{2}\pi tN}\tag{2}$$

In order to obtain the DOS, our task is to compute the averaged total energy, $\langle E(\Omega,T)\rangle$. Mode patterns can also be obtained by applying iteratively the external periodic force proportional to the displacements of atoms at each step. We can calculate numerically the averaged energy or displacements from the difference equation corresponding to the equation of motion for the forced vibration.

All the calculations in the present work have been performed on a single layer graphane, having geometry as described by Sofo et al. [1]. Graphane is known to have two distinct conformations depending upon the position of hydrogen atoms with respect to the graphene plane. In the chair conformer the hydrogen atoms are attached to carbon atoms in alternating manner on both sides of the plane while in the boat conformer the pairs of hydrogen atoms are attached in an alternating manner. Out of these two the chair conformer is energetically more favorable [11], hence in the present work we have used the chair conformer only. The simulations were performed under the free boundary conditions (FBCs). The total number of atoms used in our calculations was $N$=21,000. Vacancies were introduced randomly into the graphane honeycomb lattices using site percolation procedures. In the whole calculations, 10% vacancy means removing of 10% carbon atoms along with the attached hydrogen atoms and so

![](./images/814583569023238144_1.jpg)

Fig. 1 Chair-like conformation of graphane with percolation network structure.

on. It is well known that the site percolation threshold for a honeycomb lattice is 0.697 [12]. Therefore, vacancy concentrations (i.e., the defect density) up to 30% are used in the present simulation. Fig. 1 shows the disordered graphane with percolation network structures. Only interactions up to the fourth nearest neighbor atoms are used and the force constant tensors between two carbon atoms are taken from the report by Jishi et al. [13]. The force constant of the C-H bond is 445 N/m estimated from the frequency in the infrared absorption spectra of the hydrocarbon.

## III. RESULTS AND DISCUSSION

Fig. 2 (a) shows the calculated phonon density of states (PDOSs) of graphane with different concentrations of vacancy-type defects. It is apparent that the phonons of hydrogenated graphene sheets can be divided into low-, intermediate- and high-frequency groups of phonons. From the estimated PDOSS, one can immediately identify the high-frequency modes as dominantly H modes, as can be expected from the C-H stretching modes. The defect causes changes in the vibrational spectrum of crystals; namely, most substantial spectrum changes due to defects were expected near the Van-Hove singularities. Due to the vacancy-type defect, the PDOSs of the graphane change significantly. In the intermediate-frequency region, the PDOSs for the defective graphane are shifted down with the increase of the vacancy concentrations. As the defect density increases, we observe the broadening and softening of the PDOS peaks at the $\Gamma$ point of the LO and TO mode ($E_{2\text{g}}$ mode) phonons. More importantly, we can see that for vacancy concentrations of 10% and higher, the Raman active $E_{2\text{g}}$ peak has been reduced into a shoulder or it has completely disappeared. This disappearance of the $E_{2\text{g}}$ peak at high vacancy concentrations implies the defect-induced collapse of the long-range order in graphane at vacancy concentrations beyond a critical level.

In the presence of vacancy-type defects, the translational symmetry of the lattice is broken. Furthermore, hydrogenation

of graphene, which results in the formation of C-H $sp^3$ bonds as well as the breaking of the translational symmetry of C-C $sp^2$ bonds [1]-[3]. In these cases, the wave vectors associated with the unit cell are no longer good quantum numbers. The phonons are scattered into other states and thus it is expected that phonon wave functions are localized in real space. When the phonon wave function is localized, the phonon mean free path should be finite and consequently a decrease of the phonon lifetime. As an effect the PDOS peaks are broadened and softened with the increase of defects. To see the defect effects more clearly, the softening of the $E_{2g}$ mode with the increasing defect concentrations is also plotted as shown in Fig. 2 (b). From this Fig., it is clearly observed that the downshift of the $E_{2g}$ peak increases almost linearly with the increasing vacancy concentrations, indicating significant impacts on the electron transport properties.

Due to the random impurities, it has been shown that all states become localized in the 1D crystals [14]-[15], a similar behavior is expected in the case of 2D crystals as in the 1D case. In the case of 3D crystals, however, a transition from extended to localized states is expected as the energy is moved toward the band edge energies [16]. It is found that graphene displays the effect of weak localization or coherent backscattering when some disorder is present. Nevertheless, the phonons in disordered graphane are rarely discussed. Although graphene-related materials have excellent intrinsic thermal conductance, disordered regions interrupt the crystallinity and impede the flow of thermal energy. Since localization virtually immobilizes phonons and makes them non-conducting, these phonons lose their nature as heat carriers. To quantify these localization properties, defects induced eigenvectors have been computed. As the disordered graphane show an additional peak in the Raman spectra near to the $1340\ \text{cm}^{-1}$ [2], comes from double-resonance processes through the activation of phonons at interior $K$ points of the Brillouin zone, therefore, in this study, we mainly focus on the eigenmodes of the $K$ point in-plane transverse optical iTO phonons.

Fig. 3 depicts the typical mode patterns for the $K$ point iTO mode phonon of perfect and 20% vacancy-type disordered graphane at $1340\ \text{cm}^{-1}$. This calculation is for $N=759$ atoms. As the modes are strongly localized within this range of lattice spaces, there is no need to study of the system with a large number of atoms. In Fig. 3, each circle denotes the position of an atom, and the color denotes the displacement. We can clearly observe in Fig. 3 (a) that all the modes are extended or no localized modes are found in perfect graphane structure. However, if we insert vacancies into the perfect structure, we observe a spatially localized eigenmodes, originate from the resonant vibration of the randomly arranged atoms in the percolation network structures of defective graphane. This result is conceptually very good agreement with the large D

![](./images/814583569023238144_2.jpg)

Fig. 2 (a) Phonon density of states of graphane with different concentration of vacancy-type defects. (b) Defect dependent Raman active $E_{2g}$ mode frequencies.

![](./images/814583569023238144_3.jpg)

Fig. 3 Typical mode patterns for in-plane TO mode phonon of graphane with (a) pristine structure and (b) 20% vacancy-type disordered structure.

![](./images/814583569023238144_4.jpg)

![](./images/814583569023238144_5.jpg)

Fig. 4 Temperature dependent specific heat capacity of (a) pristine graphane in comparison with pristine graphene and (b) vacancy-type disordered graphane.

peak in the defected graphene. Although the mode patterns show a localized vibration, the centers of the localized modes are not in a fixed position with different time development. To extract the eigenmode, we have applied a random force to the each atom of the system. Therefore, we predict that the center of the localized modes has been moved with each time development.

Using the PDOSs, we have calculated the temperature dependent constant-volume specific heat capacity ($C_V$) of both perfect and disordered graphanes. This is achieved using the expressions described in [17]. Generally, the specific heat is stored by the lattice vibrations and the free conduction electrons of a material. However, phonons dominate the specific heat of graphene-related materials at all practical temperatures [18]-[19] (>1 K), and the phonon specific heat increases with temperature. In Fig. 4 (a), we depict the specific heat capacity as a function of the temperature for the pristine graphene and graphane structures. The hydrogenation of graphane has been found to be reversible at 700 K [2], therefore, we present only the behavior in the region of stability of this material. The specific heat of graphane at high-temperature is larger than that of the graphene as expected from the Dulong-Petit law. Because the molar mass of graphene is larger than that of graphane, the value of the specific heat will be smaller at high temperature. This is also a very good agreement with the calculated results by Mounet et al. [20] and Peelaer's et al. [6]. The heat capacity of the disordered graphane is presented in Fig. 4 (b). As the temperature goes up, the heat capacity for the defective graphane also increases monotonically due to higher phonon modes excited. However, with the increase of the defect density of graphane, the value of heat capacity is decreased. As the phonon modes become localized due to the defects which make them non-conducting as heat carriers, resulting in a decrease of heat capacity of the system. Moreover, from the PDOS figure, the phonon modes are broadened and softened with the increase of the vacancy concentrations. The broadening of the phonon modes indicates a reduction of the lifetime of the corresponding modes. Therefore, the mean free path of those modes as well as their contribution to the specific heat is reduced.

## IV. CONCLUSIONS

In summary, we have discussed systematically the details of the vacancy-type defect effects on the vibrational properties of the single layer graphane in use of the forced vibrational method. The calculated phonon density of states strongly depends on the defect density. We have found a broadening and softening of the PDOSs peaks with the increase of vacancy concentrations. It is found that the disordered graphane shows the remarkably localized vibrational eigenmodes. The temperature dependent constant volume specific heat capacity strongly reflects the localization feature of the phonons. These results promise to be very important for the future experiments on Raman, infrared, and neutron-diffraction spectra of this novel material, and may lead to stimulate further studies aimed at a better understanding of specific heat, thermal expansion, heat conduction, and electron-phonon interaction.

## ACKNOWLEDGMENT

This work was supported by a Grant-in-Aid of Basic Research (A) from the Ministry of Education, Culture, Sports, Science, and Technology, Japan.

## REFERENCES

[1] J. O. Sofo, A. S. Chaudhari, and G. D. Barber, "Graphane: A two dimensional hydrocarbon," Phys. Rev. B, vol. 75, pp. 153401-4, April 2007.

[2] D. C. Elias, R. R. Nair, T. M. G. Mohiuddin, S. V. Morozov, P. Blake, M.P.Halsall, A. C. Ferrari, D. W. Boukhvalov, M. I. Katsnelson, A. K. Geim, and K. S. Novoselov, "Control of Graphene's Properties by Reversible Hydrogenation: Evidence for Graphane," Science, vol. 323, pp. 610-613, Jan.2009.

[3] D. V. Boukhvalov, M. I. Katsnelson, and A. I. Lichtenstein, "Hydrogen on graphene: Electronic structure, total energy, structural distortions and magnetism from first-principles calculations," Phys. Rev. B, vol. 77, pp. 035427-7, Jan. 2008.

[4] S. Piscanec, M. Lazzeri, F. Mauri, A. C. Ferrari, and J. Robertson, "Kohn Anomalies and Electron-Phonon Interactions in Graphite," Phys. Rev. Lett., vol. 93, pp. 185503-4, Oct. 2004.

[5] B. S. Pujari and D. G. Kanhere, "Density Functional Investigations of Defect-Induced Mid-Gap States in Graphane," J. Phys. Chem. C, vol. 113, pp. 21063-21067, Nov. 2009.

[6] H. Peelaers, A. D. Hernandez-Nieves, O. Leenaerts, B. Partoens, and F.M. Peeters, "Vibrational properties of graphene fluoride and graphane," Appl. Phys. Lett., vol. 98, pp. 051914-3, Jan. 2011.

[7] Q. X. Pei, Z. D. Sha, and Y. W. Zhang, "A theoretical analysis of the thermal conductivity of hydrogenated graphene," Carbon, vol. 49, pp. 4752-4759, Nov. 2011.

[8] C. Jin, H. Lan, L. Peng, K. Suenaga, and S. Iijima,"Deriving Carbon Atomic Chains from Graphene," Phys. Rev. Lett., vol. 102, pp. 205501-4, May 2009.

[9] N. Nishiguchi, S. Tamura, and F. Nori, "Phonon-transmission rate, fluctuations, and localization in random semiconductor super lattices: Green's function approach," Phys. Rev. B, vol. 48, pp. 2515-2528, Jul. 1993.

[10] M. L. Williams and H. J. Maris, "Numerical study of phonon localization in disordered systems," Phys. Rev. B, vol. 31, pp. 4508-4515, April 1985.

[11] O. Leenaerts, H. Peelaers, A. D. Hernandez-Nieves, B. Partoens, and F. M. Peeters, "First-principles investigation of graphene fluoride and graphane," Phys. Rev. B, vol. 82, pp. 195436-6, Nov. 2010.

[12] P. N. Suding and R. M. Ziff, "Site percolation thresholds for Archimedean lattices," Phys. Rev. E, vol. 60, pp. 275-283, Jul. 1999.

[13] R. A. Jishi, L. Venkataraman, M. S. Dresselhaus and G. Dresselhaus, "Phonon modes in carbon nanotubules," Chem. Phys. Lett., vol. 209, pp.77-82, Jun. 1993.

[14] N. F. Mott and W. D. Twose, "The theory of impurity conduction," Adv. Phys., vol. 10, pp. 107-163, April 1961.

[15] R. E. Borland, "The Nature of the Electronic States in Disordered One- Dimensional System," Proc. R. Soc. Lond. Ser. A, vol. 274, pp. 529-545, Aug. 1963.

[16] P. A. Lee and T. V. Ramakrishnan, "Disordered electronic systems," Rev. Mod. Phys., vol. 57, pp. 287-337, April 1985.

[17] C. Lee and X. Gonze, "Ab initio calculation of the thermodynamic properties and atomic temperature factors of SiO2 α-quartz and stishovite," Phys. Rev. B, vol. 51, pp. 8610-8613, April 1995.

[18] T. Nihira and T. Iwata, "Temperature dependence of lattice vibrations and analysis of the specific heat of graphite," Phys. Rev. B vol. 68, pp. 134305-16, Oct. 2003.

[19] L.X. Benedict, S.G. Louie, and M.L. Cohen, "Heat capacity of carbon nanotubes," Solid State Commun. vol. 100, pp. 177-180, Oct. 1996.

[20] N. Mounet and N. Marzari, "First-principles determination of the structural, vibrational and thermodynamic properties of diamond, graphite, and derivatives," Phys. Rev. B, vol. 71, pp. 205214-14, May 2005.