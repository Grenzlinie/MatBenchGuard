OPEN

# Examining the Effects of Stiffness and Mass Difference on the Thermal Interface Conductance Between Lennard-Jones Solids

Kiarash Gordiz¹ & Asegun Henry¹,²

To date, the established methods that describe thermal interface conductance (TIC) and include mode-level dependence have not included anharmonicity. The current intuition is therefore based on the behavior in the harmonic limit, whereby the extent of overlap in the bulk phonon density of states (DoS) (e.g., frequency overlap) dictates the TIC and more frequency overlap leads to higher TIC. Here, we study over 2,000 interfaces described by the Lennard-Jones potential using equilibrium molecular dynamics simulations, whereby we systematically change the mass and stiffness of each side. We show that the trends in TIC do not generally follow that of the bulk phonon DoS overlap, but instead more closely follow the vibrational power spectrum overlap for the interfacial atoms. We then identify the frequency overlap in the interfacial power spectra as an improved descriptor for understanding the qualitative trends in TIC. Although improved, the results show that the basic intuition of frequency overlap is still insufficient to explain all of the features, as the remaining variations are shown to arise from anharmonicity, which is a critical effect to include in interface calculations above cryogenic temperatures.

Thermal transport properties in nanostructures are often significantly impacted by the introduction of interfaces to the system¹⁻³. Unlike the study of thermal conductivity in crystalline materials that has advanced tremendously in recent years⁴, many questions still remain regarding heat conduction through an interface between dissimilar materials. It is now possible to not only calculate thermal conductivity for existing crystalline materials from different methods⁵ including first-principles⁴⁶, but one can even predict the thermal conductivity of pure crystalline materials that have yet to be synthesized and experimentally measured⁷. For the study of heat transfer across interfaces, however, the situation is different, as no excellent agreement with experiment over a wide range of temperatures or for various material systems has ever been reported⁸⁻¹⁵.

The picture that is ubiquitously used for thermal interface conductance (TIC) is based on phonon gas model (PGM)¹⁶, which casts the problem as a transmission problem for phonons impinging on the interface: $G \propto Cv_g\tau$. Here, $C$ and $v_g$ are the heat capacity and group velocity of a phonon that impinges on an interface. The phonon energy can then either be transmitted or reflected with a specific transmission probability defined as $\tau$. The PGM treatment of TIC lumps all of the physics associated with the nature of the other material, the quality of the interface and the nature of the chemical bonding/interactions (e.g., everything other than heat capacity and group velocity) into the transmission probability $\tau$. Thus, different physical effects such as interface roughness, inter-diffusion, stress, and dislocations all manifest through $\tau$. It is this single descriptor that encompasses all of the dynamics of the interface and it is the only place where the properties of the other material (e.g., its stiffness, chemical composition, atomic level topography) enter the calculations.

To date, the methods that have been developed to describe $\tau$, or the mode level TIC contributions have been unable to include anharmonicity, with the exception of Hopkins and coworkers for the Diffuse Mismatch Model (DMM)¹¹ and Mingo's work developing the Atomistic Green's Function (AGF) method¹⁵. Nonetheless, the only guiding intuition we have is still based on the harmonic limit, where only elastic phonon interactions can occur, which restricts a mode with frequency $\omega$ to interactions with other modes of the same frequency. It is then intuitive

¹George W. Woodruff School of Mechanical Engineering, Georgia Institute of Technology, Atlanta GA, 30332. ²School of Materials Science and Engineering, Georgia Institute of Technology, Atlanta GA, 30332. Correspondence and requests for materials should be addressed to A.H. (email: ase@gatech.edu)

![](./images/814570610339348481_1.jpg)

Figure 1. Schematic of our model structure: the interface of two LJ solids. Different interfaces will be formed by keeping the left side of the interface constant and equal to solid argon (indicated by subscript Ar) and modifying $\varepsilon$ and $m$ on the right side of the interface.

to reason that if more modes of a given frequency are available on the other side, the probability of phonon transmission is higher and this general trend is reproduced by all of the previous methods that elucidate the mode level contributions $^{8,17,18}$. This basic principle gives rise to the idea that high TIC occurs when a large degree of frequency overlap between the phonon density of states (DoS) exists between the two materials. However, this intuition is only rigorously correct as one approaches absolute zero. At higher temperatures, several new and emerging methods have shown that anharmonic effects (e.g., inelastic interactions) become non-negligible at temperatures as low as $10\ \text{K}^{19,20}$. Nonetheless, even though anharmonicity is important, a remaining issue is the fact that the guiding intuition of whether or not frequency overlap is a truly useful descriptor for TIC, has yet to be verified independently i.e., by using an independent method to evaluate TIC that is not based on the same basic framework, such as an experiment or another type of calculation. Here, we used equilibrium molecular dynamics (EMD) to calculate TIC independent of models that yield results consistent with frequency overlap as a means of evaluating the conventional intuition. For simplicity, we used the Lennard-Jones (LJ) potential to systematically change the mass mismatch and stiffness mismatch at the interface, which then changes the degree of frequency overlap. The degree of overlap is then evaluated by calculating the phonon DoS for the atoms in each respective system and the TIC is calculated using DMM to assess if there is qualitative agreement with the EMD results.

### Model Details
The systems are constructed from two face-centered-cubic (FCC) LJ solids that are lattice matched, which is a structure that has been used extensively in other interfacial heat transfer studies $^{19,21-23}$. The LJ interatomic potential is taken as,

$$
\Phi = \sum_{i,j<i} 4\varepsilon \left[ \left( \frac{\sigma}{r_{ij}} \right)^{12} - \left( \frac{\sigma}{r_{ij}} \right)^6 \right] \tag{1}
$$

where $i$ and $j$ are atom indices and $r_{ij}$ is the distance between atoms $i$ and $j$. We have three tunable parameters on each side of the interface: the depth of the potential well ($\varepsilon$) (e.g., the stiffness), the location of the potential minimum ($2^{1/6}\sigma$), and the mass ($m$) of the atoms. For any set of LJ parameters for the materials 1 and 2 forming the interface (e.g., $\sigma_{1,2}$ and $\varepsilon_{1,2}$), we used mixing rules to define the LJ parameters for the cross-species interactions: $\sigma_{12} = (\sigma_1 + \sigma_2)/2$, $\varepsilon_{12} = \sqrt{\varepsilon_1 \cdot \varepsilon_2}^{24}$. As a result, the quantitative values for TIC and qualitative trends for TIC obtained herein are specific to these choices. However, as will be shown later, the conclusions are interesting and instructive for our intuition, and it is straightforward to reason that the conclusions are likely to still have meaning and relevance for more technologically relevant interfaces. Hence, the interest here in such a simplified system is to enable a systematic and independent evaluation of the effects of mass and stiffness mismatch. For other, more realistic interatomic potential choices, the interactions are typically more complicated and most often the stiffness and lattice parameter cannot be changed independently. This can make it difficult to isolate the effect of stiffness itself (e.g., over a large range of stiffness values), without inducing other effects such as lattice mismatch and its associated stress and defects. Here, however, by using LJ solids, we can isolate the effect of stiffness, by keeping the two sides lattice-matched. This is accomplished by simply selecting equal values of $\sigma$ for the two sides of the interface$^{22}$, which then allows us to independently explore the effects of $\varepsilon$ and $m$ on the TIC.

A schematic of the model structures is shown in Fig. 1. We start from the case of having solid argon on both sides of the interface. LJ parameters and mass of argon atom ($\sigma_{Ar}$, $\varepsilon_{Ar}$, and $m_{Ar}$) are chosen from Ref. 24. Then, keeping all the parameters constant on one side of the interface (e.g., solid Ar), we independently increase $\varepsilon$ and $m$ on the other side of the interface from $\varepsilon_{Ar}$ and $m_{Ar}$ to $10\varepsilon_{Ar}$ and $10m_{Ar}$. In this way, we examine the impact of a 10X difference in stiffness and mass. This allows us to generate many interfaces all having solid argon on one side and another solid with different properties on the other. Henceforth, we will refer to these two sides as the "constant" side and the "varying" side respectively. This allows us to study a broad range of distinct interfaces instead of evaluating interfaces by modifying only one parameter as has been done previously $^{19,21-23}$. The results can then be examined as two-dimensional maps of $m$ and $\varepsilon$ ($m-\varepsilon$ map) with x- and y-axis representing the changes in $m$ and $\varepsilon$ on the varying side and the height (z-axis) equal to the property of interest (e.g., TIC or frequency overlap). Each point on the $m-\varepsilon$ map therefore represents a distinct structure and interface. In this study, we changed the values of $m$ and $\varepsilon$ along the $m$ and $\varepsilon$ axes with a resolution of $0.2m_{Ar}$ and $0.2\varepsilon_{Ar}$, respectively, which resulted in a total of 2116 distinct interfaces. We considered $3 \times 3 \times 20$ (x, y, z) FCC unit cell systems, for both the constant and varying sides. Larger cross sections up to $5 \times 5$ unit cells and longer systems up to 40 unit cells exhibited less than 5% difference from the $3 \times 3 \times 20$ structures suggesting the $3 \times 3 \times 20$ structures are representative of the limiting behavior of contact between two bulk crystals. The z-direction is chosen along the [100] crystallographic direction and is perpendicular to the planar interface. Periodic boundary conditions are applied in all three dimensions.

The LJ cutoff radius is chosen to be equal to $3\sigma_{Ar}$, and a small time step of 0.15 fs is used for all EMD simulations to properly model the dynamics of the highest frequency systems on the $m-\varepsilon$ map. To reach equilibrium, we simulated each structure successively in the isothermal-isobaric (NPT) ensemble for 0.5 ns and in canonical (NVT) ensemble for another 0.5 ns. Then, using Eq. 3, we outputted the values of interfacial heat flow under the microcanonical (NVE) ensemble for 3 ns and used Eq. 2 to calculate the TIC value. We averaged the results over 20 ensembles²⁵ with different initial random velocities, which reduced the statistical variation to less than 4% for all the interfaces on the $m-\varepsilon$ map (a total of 42,320 independent EMD simulations). All simulations were conducted using the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) package²⁶ and the force routine was modified to include the interfacial heat flux calculation concurrently with the trajectory evolution.

In EMD, the TIC is calculated from the autocorrelation function of the interfacial heat flow, using the fluctuation-dissipation theorem²⁷ and can be written as²⁸,²⁹,

$$
G = \frac{1}{k_BAT^2} \int \langle Q(0) \cdot Q(t) \rangle dt
\tag{2}
$$

where $A$, $T$, $k_B$, and $Q$ are the cross-section, simulation temperature, Boltzmann constant, and instantaneous interfacial heat flow across the interface, respectively, and $\langle \cdot \cdot \cdot \rangle$ represents the ensemble average. For a pair-wise inter-atomic potential such as LJ, $Q$ can be defined as²⁸,

$$
Q = \frac{1}{2} \sum_{i \in A, j \in B} \vec{f}_{ij} \cdot \left( \vec{v}_i + \vec{v}_j \right)
\tag{3}
$$

where $i$ and $j$ represent atomic indices, $A$ and $B$ represent the two sides of the interface, $\vec{f}_{ij}$ is the force from atom $j$ on atom $i$, and $\vec{v}_i$ and $\vec{v}_j$ are the velocities of the atoms $i$ and $j$.

## Results and Discussion
We first determined the frequency content of each structure by lattice dynamics (LD) calculations³⁰. No negative frequencies were observed for any of the structures indicating that all of them are stable³⁰. Using the LD derived DoS for the bulk of each material (*constant* and *varying*) we quantified the degree of overlap between the DoS of the two sides as³¹,

$$
S = \frac{\int DoS_1(\omega) DoS_2(\omega) d\omega}{\int DoS_1(\omega) d\omega \int DoS_2(\omega) d\omega}
\tag{4}
$$

where 1 and 2 subscripts represent *constant* and *varying* sides, respectively. The degree of DoS overlap for the entire $m-\varepsilon$ interval under consideration is shown in Fig. 2a. It can be seen that the maximum values of DoS overlap between the two sides are present along the diagonal, which is expected since individual oscillator frequencies scale as $\omega = \sqrt{K/m}$, where for a monatomic LJ solid $m$ is the mass of the atoms in the system and $K \approx 57.15\varepsilon/\sigma^2$ is the approximate characteristic spring constant between two first nearest neighbor atoms in the FCC lattice. The systems corresponding to the diagonal in Fig. 2a have the same $\varepsilon/m$ ratio as the *constant* side therefore these systems have the same characteristic frequencies and identical dispersion curves, which leads to the maximum DoS overlap. The ratio of the characteristic frequency of the *varying* side to the characteristic frequency of the *constant* side is also shown in Fig. 2b and is another way of visualizing the trends in DoS overlap (Fig. 2a). Figure 2a,b suggest that the highest contrast in vibrational properties between the bulk of the two sides occurs when the stiffness is the same with maximum mass difference (bottom right) and when the mass is the same and but the stiffness difference is maximum (top left). The guiding intuition of frequency overlap would then suggest that these systems should exhibit the lowest values of TIC for the interval considered.

We then used the DMM to calculate the values of TIC for the interfaces on the $m-\varepsilon$ map (see Fig. 3). The details associated with using the DMM are available in the original work of Swartz and Pohl⁹ and works by Hopkins *et al.*¹⁰,¹¹,³². Here, we used the DMM with the following assumptions: (1) isotropic properties for both sides of the interface, (2) Debye model for the phonon dispersion and DoS, and (3) elastic interactions between phonons across the interface. In addition, the TIC integral in the DMM should be performed on the softer side of the interface for all the structures on the $m-\varepsilon$ map and we evaluated the TIC values at T = 40 K. It should be mentioned that solid argon has a melting temperature of around 86 K and it is the softest structure among all of the solids considered. Therefore, none of the structures melt at T = 40 K. It should be noted that, even the approaches that can incorporate anharmonic interactions into DMM calculations¹¹ would not yield qualitatively different predictions, since all of them are based on the vibrational modes calculated from the bulk of the materials. Even if we relax all of our earlier assumptions associated with performing the DMM calculations, the TIC for systems along the diagonal will not change. TIC remains constant because DMM fundamentally utilizes the vibrational information of the bulk of the materials, which are indeed the same for both sides in systems located on the diagonal. Therefore, the DMM in any of its current incarnations does not yield different predictions for drastically different materials that ultimately have the same phonon dispersion.

It should be noted that one should also consider the Acoustic Mismatch Model (AMM) since the interfaces are smooth. Fundamentally, the AMM is arguably more applicable than the DMM, because for such smooth interfaces one also has to take into account momentum conservation in the directions parallel to the interface³³. Thus we also examine the AMM, as we have calculated the TIC values it predicts on the $m-\varepsilon$ map in Fig. 4. The details associated with usage of the AMM can be found in Ref. 34. In Fig. 4 the AMM trend is drastically different from the DMM calculations (Fig. 3), which signifies the fundamental contrast between the two approaches. Interestingly,

![](./images/814570610339348481_2.jpg)

Figure 2. (a) Degree of overlap between the DoS of the two sides of the interface and (b) ratio of the
characteristic frequency of the varying side to the one of the constant side.

![](./images/814570610339348481_3.jpg)

Figure 3. Values of TIC calculated at $T=40$ K using DMM. TIC values have units of $(MW\ m^{-2}\ K^{-1})$.

although the AMM technique is still based on the bulk vibrational information³⁴, unlike the DMM approach, it
can distinguish the different interfaces located on the diagonal of the $m-\varepsilon$ map. The reason is that the definition
of transmission coefficient in AMM is based on the acoustic impedance (i.e., $\rho c$, where $\rho$ is the density and $c$ is the
speed of sound in the material), and because of the large difference in mass on the $m-\varepsilon$ map, there is a large

![](./images/814570610339348481_4.jpg)

Figure 4. Values of TIC calculated at T = 40 K using AMM. TIC values have units of (MW m⁻² K⁻¹).

![](./images/814570610339348481_5.jpg)

Figure 5. Values of TIC calculated using the EMD simulations at (a) T = 40 K, and (b) T = 5 K. TIC values have units of (MW m⁻² K⁻¹). The region that exhibits the strongest anharmonic effects is illustrated in panel (a) through the dashed rectangular region.

difference in density. As a result the AMM predicts that the acoustic impedance and therefore the TIC should vary along the diagonal of the $m - \varepsilon$ map.

The EMD values of TIC are shown in Fig. 5a and they are in qualitative disagreement with the guiding intuition obtained from both frequency overlap analysis (Figs 2 and 3) and the AMM calculations (Fig. 4). This disagreement

![](./images/814570610339348481_6.jpg)

Figure 6. Degree of overlap between the DoS of the two sides of the interface based on the vibrations of atoms in the interface region at T = 40 K. The calculated degrees of overlap have negligible temperature dependence and show similar trends for T = 5 K, too.

raises significant questions around the applicability of the harmonic analyses based on the bulk vibrational characteristics of materials. Clearly, utilizing the bulk vibrational information from sides of the interface in DMM and AMM fails to properly describe the trends in TIC for the systems on the $m - \varepsilon$ map. One interesting insight that can in general be obtained from the observed trends in Fig. 5a is that the mass-mismatch between the two sides of the interface seems to have a much stronger effect on the TIC than the stiffness mismatch. The significance of mass mismatch alone on TIC has also been noted in other reports²², but the $m - \varepsilon$ map also reveals a deviation from this trend at the upper ridge of the map.

Instead of using system properties that reflect the bulk vibrations, it was postulated that what may serve as more useful descriptors are the properties that are specifically related to the interfacial region's vibrations. As a first hypothesis, we examined the spectrum of the vibrations near the interface (i.e., interfacial power spectra (IPS)), which have been previously observed to differ from the bulk in some structures³⁵,³⁶. We determined the power spectrum of the interfacial atoms at each side of the interface by calculating the averaged power spectrum of velocities³⁷,³⁸. The atomic velocities ($v_{\alpha=x,y,z}$) are extracted every 10 time steps (e.g., 1.5 fs), and the power spectrum is calculated using³⁷,³⁸,

$$
P_{\alpha}(\omega)=\int\left|v_{\alpha}(t) e^{-i \omega t} d t\right|^{2}. \tag{5}
$$

Then, using Eq. 4, the degree of overlap between the interfacial DoS at the two sides of the interface is calculated for each structure and the results are shown in Fig 6. It can be seen that if we use the frequency content of the interfacial atoms, the frequency overlap (Fig. 6) differs significantly from the bulk vibrational information (Fig. 2a) and the trends are much closer to the TIC values on the $m - \varepsilon$ map (Fig. 5a). The fact that IPS presents a better description for heat transfer at the interface of two solids has also been reported by Chen *et al.* for the heat transport across SiGe interface, where more complex many-body potential is used in the MD simulation³⁶. However, a recent study by Alexeev *et al.*³⁹ showed that for the solid-liquid interface, the liquid layering effect near the interface, rather than the frequency overlap, plays an important role in determining the interfacial heat transport.

Figures 5a and 6 show that the mass ratio plays the dominant role in determining the TIC and degree of interfacial region DoS overlap on the $m - \varepsilon$ map. It was then realized that this is because even though the mass and stiffness affect the characteristic frequency in the same way, they do not affect the interfacial interactions in the same way. Most notably, as one moves from one side of the interface to the other, there is a continuous transition in the stiffness, but the transition in mass is discontinuous. Consider for example, when the stiffness on the other side of the interface is 2X larger, the atoms on the softer side, due to the use of mixing rules, experience stiffer long ranged interactions with atoms from the stiffer side that become increasingly strong as one moves toward the interface. At the interface itself, the last plane of softer atoms experiences weaker bond strength on one side, and a much stiffer bond strength on the other. Thus, as one increases the stiffness of the stiffer side of the interface, the increased stiffness also affects the atoms in the softer material and consequently makes them vibrate at higher frequencies. The net effect is that it keeps the frequency content of the atoms in the interfacial region matched for any choice of stiffness. This then leads to a fixed amount of interfacial DoS overlap, regardless of the difference in stiffness. The mass difference, on the other hand, is fundamentally different, because it does not penetrate into the other material the way the strength of interaction does. Since changing the mass difference is independent, one can decrease the frequencies of vibration for one side of the interface without changing the frequencies on the other side, thereby explaining why Figs. 5a and 6 seem to only show trends with respect to mass, but nearly constant TIC vs. stiffness ratio. Prior to this investigation, this behavior would have been non-intuitive and thus the results are highly corrective for our intuition.

The remaining discrepancy between Figs 5a and 6 is the higher TIC observed for systems with a high stiffness mismatch, for all mass ratios (e.g., the top horizontal region). It was postulated that this region of increased TIC could be a result of anharmonic effects. Testing whether this is true is straightforward, as one can suppress anhar- monic effects, by probing the behavior at lower temperatures. Interestingly, when the EMD calculations are repeated at lower temperatures (5 K) the aforementioned region of higher TIC disappears and the trends are in better agreement with the trends predicted by the interfacial power spectra (IPS) overlap (see Figs 5b and 6). Thus, it appears evident that the upper ridge of higher TIC on the $m-\varepsilon$ map is the result of anharmonicity (Fig. 5a). This is presumably enabled by the large asymmetry in bond strength experienced by atoms in the interfacial region. When there is a large asymmetry in stiffness, the atoms near the interface in the softer material are likely to sample the more anharmonic portions of their potential energy landscape. This is because their net forces are primarily dictated by the much higher forces from the stiffer side.

### Interfacial Power Spectrum Approximation (IPSA)
Given that the interfacial power spectrum (IPS) appears to be a more appropriate descriptor for the TIC, it is straightforward to then utilize the IPS within the DMM approach to then make improved TIC predictions. Our modification which is simply termed the interfacial power spectrum approximation (IPSA) can be employed in the traditional DMM approach $^{9,10}$ as follows,

$$
G=\frac{1}{4} \sum_{j} v_{1, j} \int_{0}^{\omega_{1, j}^{c}} \alpha_{1}(\omega) \hbar \omega D_{1, j}(\omega) \frac{\partial n(\omega, T)}{\partial T} d \omega
\tag{6}
$$

where index 1 represents the softer material, index $j$ refers to the phonon polarization, $\omega$ is the phonon frequency, $v$ is the phonon velocity, $\omega^{c}$ is the cutoff frequency, $D(\omega)$ is the density of states, $\alpha$ is the phonon transmission probability and $n(\omega, T)$ is the phonon distribution function for a mode with frequency $\omega$ at temperature $T$. Here, specifically for comparison with the classical MD simulations, we have taken $n(\omega, T)$ to be the classical distribution, but it should be noted that when comparing to experiments, one should use the Bose-Einstein distribution. The definition of transmission probability for a phonon with frequency $\omega$ is then based on the vibrational characteristics at the interface region as opposed to the bulk,

$$
\alpha_{1}(\omega)=\frac{\sum_{j} v_{2, j} D_{2, j}^{\text {int }}(\omega)}{\sum_{j} v_{2, j} D_{2, j}^{\text {int }}(\omega)+\sum_{j} v_{1, j} D_{1, j}^{\text {int }}(\omega)}
\tag{7}
$$

where, in addition to the parameters defined for Eq. 6 (i.e., $v$ still referring to the bulk phonon velocities), index 2 represents the stiffer material, and $D^{\text {int }}(\omega)$ refers to the interfacial power spectra. More details on the implemen- tation of IPSA method are provided in supplementary note 1. Information about the bulk DoS can be acquired from experiments $^{40}$ or first-principles calculations $^{41}$, but it is not clear how one could use these techniques to calculate the power spectra at the interface for sufficiently large systems. Thus, for the IPSA, LD calculations or MD simulations of the interface structure based on an accurate inter-atomic potential serve as the most tractable tool for determining the interfacial power spectra for a desired structure.

An interesting point, associated with defining the IPS, is determining the effective region that should be termed the interfacial region. A simple approach to managing this issue is to define the vibrational power spectrum cal- culated for each atom with a weighting factor that is proportional to the magnitude of the force it experiences from the atoms on the other side of the interface. Figure 7 illustrates this idea by showing the forces experienced by an atom according to the LJ potential as a function of the distance between the two atoms. Although, in this study the cutoff radius has been taken as $3 \sigma_{A r}$, it can be seen that the first and second nearest neighbors in the FCC lattice experience much stronger interactions than subsequent neighbor shells and as a result they constitute more than95% to the calculated interfacial power spectra. It should further be emphasized that an appropriate weighting scheme is crucial, because the vibrational spectrum quickly returns to the bulk spectrum just 2-3 layers away from the interface.

As an initial test of this approach, we calculated the TIC values on the $m-\varepsilon$ map using Eqs 6 and 7 (see Fig. 8). Compared to the traditional DMM that is based on the bulk vibrational characteristics (see Fig. 3), incorporating the IPS to calculate the transmission probabilities leads to much better qualitative agreement between the DMM calculations and the MD (see Fig. 5). However, since the rationale for why one would use frequency overlap at all, is still based on the physics of elastic interactions, even the IPSA is unable to account for the anharmonic effects observed on the upper ridge of the $m-\varepsilon$ map (see Fig. 5a). Thus, although IPS is an improved descriptor as compared to bulk DoS, even for such a simple LJ system, the physics of TIC still involves anharmonicity, which is currently only well described by more involved methodologies such as the Interface Conductance Modal Analysis(ICMA) technique $^{20}$ or recently developed spectral decomposition methods $^{19,42,43}$ .

### Summary
In this study, using equilibrium molecular dynamics (EMD), we calculated the thermal interface conductance(TIC) for over 2,000 interfaces formed at the junction of two Lennard-Jones solids. The interfaces were changed by systematically modifying the mass and stiffness on only one side of the interface, whereby the parameters on other side were held constant and corresponded to solid argon. The TIC values were also calculated using the DMM and AMM approaches, however, both of these techniques predicted drastically different trends for the variations in TIC than what was obtained by EMD simulations. Both of these approaches are based on the bulk vibrational information, and the discrepancies in the results clearly show that using the bulk vibrational information may be inaccurate for predicting interfacial transport properties. Following the postulate that interfacial vibrational

![](./images/814570610339348481_7.jpg)

Figure 7. LJ force as a function of interatomic separation distance (r). The calculated forces are normalized based on the maximum attractive force. First, second, third, and fourth nearest neighbors in an FCC lattice are approximately located at $1.1\sigma, 1.56\sigma, 1.9\sigma$, and $2.2\sigma$, respectively⁴⁴. The proportionality of forces at these separation distances determine the factors used to weight the power spectra of atoms at the interface in the calculation of the total averaged interfacial power spectra. For the LJ interatomic potential and FCC lattice, the weighting factors for the first, second, third, and fourth nearest neighbors were approximately 0.64, 0.31, 0.04, and 0.01, respectively.

![](./images/814570610339348481_8.jpg)

Figure 8. Values of TIC calculated using DMM and the interfacial DoS overlap to calculate the transmission probabilities of phonons at the interface.

properties play a key role in the interfacial heat transfer, we then showed that incorporating the vibrational power spectra of atoms at the interface into the calculation of the transmission coefficient in the DMM (i.e., interfacial power spectra approximation (IPSA) approach) significantly improved the predicted TIC values. The remaining differences between the EMD and IPSA predictions are attributed to anharmonic interactions at the interface. Incorporating such effects demands more involved techniques, such as MD based approaches²⁰, that allow the inclusion of inelastic coupling between different modes of vibration.

### References
1. Wilson, R. & Cahill, D. G. Experimental validation of the interfacial form of the Wiedemann-Franz law. *Phys. Rev. Lett.* **108**, 255901 (2012).
2. Davis, B. L. & Hussein, M. I. Nanophononic metamaterial: Thermal conductivity reduction by local resonance. *Phys. Rev. Lett.* **112**, 055505 (2014).
3. Cahill, D. G. *et al.* Nanoscale thermal transport. *J. Appl. Phys.* **93**, 793–818 (2002).
4. Broido, D., Malorny, M., Birner, G., Mingo, N. & Stewart, D. Intrinsic lattice thermal conductivity of semiconductors from first principles. *Appl. Phys. Lett.* **91**, 231922 (2007).
5. Henry. A. & Chen, G. High Thermal Conductivity of Single Polyethylene Chains Using Molecular Dynamics Simulations. *Phys. Rev. Lett.* **101** (2008).
6. Garg, J., Bonini, N. & Marzari, N. In *Length-Scale Dependent Phonon Interactions* 115–136 (Springer, 2014).
7. Lindsay, L., Broido, D. & Reinecke, T. First-principles determination of ultrahigh thermal conductivity of boron arsenide: a competitor for diamond? *Phys. Rev. Lett.* **111**, 025901 (2013).

8. Little, W. The transport of heat between dissimilar solids at low temperatures. *Can. J. Phys.* **37**, 334–349 (1959).

9. Swartz, E. T. & Pohl, R. O. Thermal boundary resistance. *Rev. Mod. Phys.* **61**, 605 (1989).

10. Hopkins, P. E. & Norris, P. M. Effects of joint vibrational states on thermal boundary conductance. *Nanosc. Microsc. Therm.* **11**, 247–257 (2007).

11. Hopkins, P. E., Norris, P. M. & Duda, J. C. Anharmonic phonon interactions at interfaces and contributions to thermal boundary conductance. *J. Heat Transfer* **133**, 062401 (2011).

12. Schelling, P. K., Phillpot, S. R. & Keblinski, P. Phonon wave-packet dynamics at semiconductor interfaces by molecular-dynamics simulation. *Appl. Phys. Lett.* **80**, 2484–2486 (2002).

13. Roberts, N. A. & Walker, D. Phonon wave-packet simulations of Ar/Kr interfaces for thermal rectification. *J. Appl. Phys.* **108**, 123515 (2010).

14. Zhang, W., Fisher, T. & Mingo, N. The atomistic Green's function method: An efficient simulation approach for nanoscale phonon transport. *Numer. Heat Transfer B-Fund.* **51**, 333–349 (2007).

15. Mingo, N. Anharmonic phonon flow through molecular-sized junctions. *Phys. Rev. B* **74**, 125402 (2006).

16. Chen, G. *Nanoscale energy transport and conversion: a parallel treatment of electrons, molecules, phonons, and photons*. (Oxford University Press, USA, 2005).

17. Huang, Z., Murthy, J. Y. & Fisher, T. S. Modeling of polarization-specific phonon transmission through interfaces. *J. Heat Transfer* **133**, 114502 (2011).

18. Ong, Z.-Y. & Zhang, G. Efficient approach for modeling phonon transmission probability in nanoscale interfacial thermal transport. *Phys. Rev. B* **91**, 174302 (2015).

19. Sääskilahti, K., Oksanen, J., Tulkki, J. & Volz, S. Role of anharmonic phonon scattering in the spectrally decomposed thermal conductance at planar interfaces. *Phys. Rev. B* **90**, 134312 (2014).

20. Gordiz, K. & Henry, A. A formalism for calculating the modal contributions to thermal interface conductance. *New J. Phys.* **17**, 103002 (2015).

21. Liang, Z., Evans, W. & Keblinski, P. Equilibrium and nonequilibrium molecular dynamics simulations of thermal conductance at solid-gas interfaces. *Phys. Rev. E* **87**, 022119 (2013).

22. Shen, M., Evans, W. J., Cahill, D. & Keblinski, P. Bonding and pressure-tunable interfacial thermal conductance. *Phys. Rev. B* **84**, 195432 (2011).

23. Wu, X. & Luo, T. The importance of anharmonicity in thermal transport across solid-solid interfaces. *J. Appl. Phys.* **115**, 014901 (2014).

24. Sarkar, S. & Selvam, R. P. Molecular dynamics simulation of effective thermal conductivity and study of enhanced thermal transport mechanism in nanofluids. *J. Appl. Phys.* **102**, 074302 (2007).

25. Gordiz, K., Singh, D. J. & Henry, A. Ensemble averaging vs. time averaging in molecular dynamics simulations of thermal conductivity. *J. Appl. Phys.* **117**, 045104 (2015).

26. Plimpton, S. Fast parallel algorithms for short-range molecular dynamics. *J. Comput. Phys.* **117**, 1–19 (1995).

27. Kubo, R. The fluctuation-dissipation theorem. *Rep. Prog. Phys.* **29**, 255 (1966).

28. Domingues, G., Volz, S., Joulain, K. & Greffet, J.-J. Heat transfer between two nanoparticles through near field interaction. *Phys. Rev. Lett.* **94**, 085901 (2005).

29. Barrat, J.-L. & Chiaruttini, F. Kapitza resistance at the liquid—solid interface. *Mol. Phys.* **101**, 1605–1610 (2003).

30. Dove, M. T. *Introduction to lattice dynamics*. Vol. 4 (Cambridge university press, 1993).

31. Yang, N., Zhang, G. & Li, B. Carbon nanocone: a promising thermal rectifier. *Appl. Phys. Lett.* **93**, 243111 (2008).

32. Cheaito, R. *et al.* Thermal boundary conductance accumulation and interfacial phonon transmission: Measurements and theory. *Phys. Rev. B* **91**, 035432 (2015).

33. Polanco, C. A. *et al.* Role of crystal structure and junction morphology on interface thermal conductance. *Phys. Rev. B* **92**, 144302 (2015).

34. Srivastava, G. P. *The physics of phonons*. (CRC Press, 1990).

35. Yang, N. *et al.* Thermal Interface Conductance Between Aluminum and Silicon by Molecular Dynamics Simulations. *J. Comput. Theor. Nanos.* **12**, 168–174 (2015).

36. Chen, J., Zhang, G. & Li, B. Tunable thermal conductivity of Si Ge x nanowires. *Appl. Phys. Lett.* **95**, 073117 (2009).

37. Gordiz, K. & Allaei, S. M. V. Thermal rectification in pristine-hydrogenated carbon nanotube junction: A molecular dynamics study. *J. Appl. Phys.* **115**, 163512 (2014).

38. Padgett, C. W. & Brenner, D. W. Influence of chemisorption on the thermal conductivity of single-wall carbon nanotubes. *Nano Lett.* **4**, 1051–1053 (2004).

39. Alexeev, D. *et al.* Kapitza Resistance between Few-Layer Graphene and Water: Liquid Layering Effects. *Nano Lett.* **15**, 5744–5749 (2015).

40. Nilsson, G. & Nelin, G. Study of the homology between silicon and germanium by thermal-neutron spectrometry. *Phys. Rev. B* **6**, 3777 (1972).

41. Wei, S. & Chou, M. Phonon dispersions of silicon and germanium from first-principles calculations. *Phys. Rev. B* **50**, 2221 (1994).

42. Chalopin, Y., Mingo, N., Diao, J., Srivastava, D. & Volz, S. Large effects of pressure induced inelastic channels on interface thermal conductance. *Appl. Phys. Lett.* **101**, 221903 (2012).

43. Chalopin, Y. & Volz, S. A microscopic formulation of the phonon transmission at the nanoscale. *Appl. Phys. Lett.* **103**, 051602 (2013).

44. Kelly, A. A. & Knowles, K. M. *Crystallography and crystal defects*. (John Wiley & Sons, 2012).

## Author Contributions
K.G. and A.H. conceived this project. K.G. designed the algorithm and performed the calculations. K.G. and A.H. analyzed the data. K.G. and A.H. discussed the results. K.G. and A.H. wrote the manuscript.

## Additional Information
Supplementary information accompanies this paper at http://www.nature.com/srep

Competing financial interests: The authors declare no competing financial interests.

How to cite this article: Gordiz, K. and Henry, A. Examining the Effects of Stiffness and Mass Difference on the Thermal Interface Conductance Between Lennard-Jones Solids. *Sci. Rep.* **5**, 18361; doi: 10.1038/srep18361 (2015).

![](./images/814570610339348481_9.jpg)
This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/