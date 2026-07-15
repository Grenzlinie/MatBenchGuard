
# Boosting the transparency of metallic SrNbO_{3} through Ti doping

Shammi Kumar \( ^{1,a)} \) , Liang Si \( ^{2,3,4,b)} \) , Karsten Held \( ^{4,c)} \) , Sankar Dhar \( ^{1} \) , Rakesh Kumar \( ^{1} \)  and Priya Johari \( ^{1,a)} \) 

 \( ^{1} \)  Department of Physics, School of Natural Sciences, Shiv Nadar Institution of Eminence (Deemed to be University), Gautam Buddha Nagar, Uttar Pradesh 201314, India

 \( ^{2} \)  School of Physics, Northwest University, Xi'an 710127, China

 \( ^{3} \)  Shaanxi Key Laboratory for Theoretical Physics Frontiers, Xi'an 710127, China

 \( ^{4} \)  Institute of Solid-State Physics, Vienna University of Technology, 1040 Vienna, Austria

a) Authors to whom correspondence should be addressed: priya.johari@snu.edu.in, sk657@snu.edu.in

b) siliang@nwu.edu.cn

c) held@ifp.tuwien.ac.at

## Abstract

In recent years, various materials have been developed to reduce the reliance of industries on Indium, a primary component of transparent conducting oxides (TCOs) used in the current generation of devices. The leading candidates for indium-free TCOs are strontium vanadates, niobates, and molybdates—strongly correlated perovskite systems that exhibit high intrinsic electrical conductivity and optimal transparency. In this work, we focus on the strontium niobate (SrNbO \( _{3} \) ) thin films and manipulate its optical conductivity by Ti doping which shifts the plasma frequency and reduces electronic correlations. This allows us to achieve a low resistance of SrNb \( _{1-x} \) Ti \( _{x} \) O \( _{3} \)  (x = 0 - 0.5) thin films while maintaining a high transparency in the visible light region. We obtain the optimal figure-of-merit (FOM) of 10.3 (10 \( ^{-3} \)  \( \Omega \)  \( ^{-1} \) ) for x = 0.3. This FOM significantly outperforms the optoelectronic capabilities of Tin-doped Indium oxide (ITO) and several other proposed transparent conductor materials. Our research paves a way for designing the next generation of transparent conductors, guided by insights from density-functional theory (DFT) and dynamical mean-field theory (DMFT).
 

## Introduction

The demand for transparent electronics has surged in recent decades, driven by the widespread use of consumer electronics like smartphones, televisions, LEDs etc. \( ^{1-3} \) . It is also one of the primary requirements for the fabrication of solar cells \( ^{4-7} \) . At the heart of all such display devices are thin film transparent conducting electrodes which are, as the name suggests, simultaneously transparent to the visible light as well as electrically conducting. The ideal transparent conductors are ones which have a high band gap ( \( E_{g} > 3.1eV \) ), exhibit high transparency (T > 85%) in the visible light range and, at the same time, a high conductivity ( \( \sigma > 10^{3} \)  S/cm) \( ^{8,9} \) . Among several candidates, Tin-doped Indium oxide (ITO) has become the standard transparent conductive oxide (TCO) globally due to its outstanding optoelectronic performance. It has a high transparency (>85%) and a low sheet resistance (10-100  \( \Omega \square^{-1} \) ), making it suitable for a wide variety of optoelectronic devices \( ^{1,5,10} \) . However, due to the high cost and scarcity of Indium, a better alternative to reduce our reliance on ITO is urgently needed \( ^{11} \) . Significant progress has been made in this area, and several alternatives are currently being explored.

One of the primary candidates to replace Indium based TCOs is correlated perovskite oxides, such as  \( SrVO_{3} \)  (SVO),  \( SrMoO_{3} \)   \( (SMO) \) , and  \( SrNbO_{3} \)   \( (SNO) \) , which are correlated metals that exhibit low resistivity (30-200  \( \mu\Omega \)  cm \( ^{-1} \) ) \( ^{12} \) . Their transparencies are quite low (40-70%) and can be explained by the plasma frequency  \( \omega_{p} = \sqrt{\frac{(4\pi e^{2}n)}{(\epsilon_{r}m^{*})}} \) , where e is the electronic charge, n the density of conduction electrons,  \( m^{*} \)  the effective mass, and  \( \epsilon_{r} \)  the static screening \( ^{13} \) . All these oxides have a relatively high  \( n \)  ( \( \sim10^{22} \)  cm \( ^{-3} \) ), correspondingly the plasma frequency is expected to be quite high. Moreover, for correlated systems, the effectively mass renormalization factor  \( Z^{-1} = m^{*}/m_{b} \) , where  \( m_{b} \)  is the band mass obtained from DFT calculations,
 

must be taken into account to better understand the observed trends of the plasmon frequency \( ^{14} \) . Here Z = 1 for non-interacting electrons and Z = 0 for fully localized electrons, i.e., Mott-insulator. Light that has a frequency smaller than  \( \omega_{p} \)  is mostly reflected back whereas light with a frequency greater than  \( \omega_{p} \)  is able to penetrate deeper into the sample, leading to the optical transparency. The visible light has the energy range of 1.75 - 3.10 eV, meaning the plasmon frequency of a given material should be smaller than 1.75 eV to be transparent to the visible spectrum. Among the above-mentioned perovskites, only SVO has a  \( \omega_{p} \)  ( \( \sim \) 1.3 eV) which lies below the visible range making it an effective transparent conductor \( ^{11,15,16} \) . However, the small  \( \omega_{p} \)  of SVO occurs due to a large band mass-enhancement (Z  \( \sim \)  0.33,  \( m^{*} = 3m_{b} \) ) that, reduces the electronic lifetime  \( \tau \)  (enhances the scattering rate  \( \tau^{-1} \) ); as a result of which it has still a quite high absorbance above 2.25 eV \( ^{17} \) . This scattering is further increased at  \( \sim \) 2.7 eV, where interband transitions dominate which results in an enhancement in the absorption, thereby reducing the transparency \( ^{13,17} \) . The potential for usage of SVO as a transparent conductor is limited due to this shortcoming.

On the other hand, the  \( \omega_{p} \)  of SMO (Z ~ 0.48) lies within the visible range ( \( \sim \)  2 eV) which decreases the transparency at low energies in the visible spectrum, limiting their use till date \( ^{14,18-20} \) . Several notable strategies have been proposed recently to shift either  \( E_{g} \)  or  \( \omega_{p} \)  of SVO and SMO to enhance their transparency, such as, thickness modulation, A and B site cationic substitution, or strain modulation \( ^{21-26} \) . In particular, the cationic substitution of V by Mo, performed by Mohammadi et al. has been successfully reported to regulate  \( \omega_{p} \)  as well as  \( E_{g} \)  and established  \( SrMo_{1-x}V_{x}O_{3} \)  as an alternative to the current TCOs \( ^{27} \) .

In this work, we focus on another material, SNO, and investigate its potential as a TCO. SNO has a larger transparency range than SVO and SMO, and has fantastic properties for plasmonics, photocatalysis, two dimensional electron gases (2DEGs), and metal-insulator
 

transition (MIT) device \( ^{28-38} \) . SNO is a large (optical) band gap material ( \( E_{g} \sim 4.1 - 4.5 \)  eV) with the reported resistivity of 50-200  \( \mu\Omega \) -cm making it a promising candidate to replace ITO \( ^{29,39,40} \) . However, the transparency of the metallic SNO is quite low (40-70%), due to the relatively high  \( \omega_{p} \)  (1.8 - 2.0 eV) as well as the free carrier absorption (FCA), which impedes its intended application as a TCO \( ^{29,39,40} \) . A significant amount of work has been dedicated to enhancing the optical transmittance of SNO through various techniques. For example, Roth et al. grew SNO thin films of different thicknesses (t ~ 10 - 55 nm) on  \( (\mathrm{La}_{0.3}\mathrm{Sr}_{0.7})(\mathrm{Al}_{0.65}\mathrm{Ta}_{0.35})\mathrm{O}_{3} \)  (LSAT) and successfully improved the transparency to 86% by using sputtering deposition technique \( ^{41} \) . However, the cost of this is the sheet resistance of thin films increased from 74  \( \Omega \)  to 370  \( \Omega \) , which is unfavorable for TCO. Another technique to increase transparency is by inducing off-stoichiometry \( ^{8,39,42,43} \) . However, this method has also only succeeded in raising optical transparency to 75%, with a slight trade-off in conductivity. Recently, Jeong et al. were able to optimize the growth conditions of SNO on  \( DyScO_{3} \)  (110) substrates, to achieve a reported  \( R_{s} \)  of 10  \( \Omega \)  and maximum transparency,  \( T_{max} \sim 87\% \) , marking a significant increase in the figure of merit \( ^{44} \) . However, the transparency falls rapidly at lower energy ranges ( \( \sim 2 \)  eV), possibly due to  \( \omega_{p} \) . These various approaches highlight a significant inconsistency in finding an effective method to optimize the optoelectronic properties of SNO. Additionally, other theoretical strategies, such as strain tuning and cationic substitution, have been reported to have minimal impact on the plasmon frequency and, consequently, on the transparency of SNO \( ^{22,24} \) .

A promising approach to enhancing the properties of SNO was recently proposed by Si et al.: Ti ( \( d^{0} \) ) doping of SNO (STNO) was identified as a viable strategy to improve the optoelectronic properties of SNO \( ^{17} \) . Ti doping has a dual effect: First, it reduces the number of free carriers in STNO, reducing  \( \omega_{p} \)  and FCA. Secondly, going away from an integer Nb  \( d^{l} \)  configuration, correlation effects are reduced. This results in a larger, less strongly renormalized quasiparticle weight (Z), which would typically increase  \( \omega_{p} \) . However, the overall trend is a decrease  \( \omega_{p} \)  due
 

to Ti (hole) doping. Reduced correlations also lead to less scattering and longer carrier lifetimes, which are crucial for enhancing conductivity. Together, these effects may shift the absorption edge below the visible light spectrum, while maintaining high conductivity in the material.

Here, we verify the direct and simple approach proposed by Si et al. on the  \( SN_{1-x}Ti_{x}O \)  system, by varying the Ti concentration from 0 - 0.5. In our DFT+DMFT calculations \( ^{45} \) , we observe that 25-50% Ti doping does not significantly affect the electronic conductivity but successfully shifts  \( \omega_{p} \)  below the visible spectrum. We then confirm this experimentally by growing epitaxial thin films of  \( SN_{1-x}Ti_{x}O \)  (t ~ 70 nm) on  \( LaAlO_{3} \)  (LAO) substrates (schematic Figure 1(a)). It is seen from the photographs of thin films in Figure 1(b) that, as the composition of Ti is increased, the films become increasingly transparent, even almost completely transparent at higher Ti composition (x = 0.5). In Figure 1(c), we plot the FOM of these films and find that it increases drastically upon increasing the concentration of Ti in these films up to x = 0.3 and decreases slightly for x = 0.5. As we mentioned earlier, the optoelectronic properties are highly tunable by growth conditions as shown by the recent improvement in FOM of  \( SNO^{44} \) . The same applies to  \( SN_{1-x}Ti_{x}O \)  thin films, which are highly sensitive to growth conditions. The FOM can be further enhanced by optimizing factors such as substrate selection, film thickness,  \( pO_{2} \)  levels, and growth temperature. To show this variation in our results, we also display the highest achieved FOM (shown by star) for individual concentration by varying the growth oxygen partial pressure ( \( pO_{2} \) ) and the thickness in Figure 1(c). To simplify the optimization process, we focus on improving transparency solely through Ti substitution, while maintaining consistent growth conditions for all thin films in this study.
 

(a)

![](./images/1050293411485057031_1.jpg)

(c)

![](./images/1050293411485057031_2.jpg)

(b)

![](./images/1050293411485057031_3.jpg)

Figure 1: (a) Schematic of  \( SN_{1-x}Ti_{x}O \)  films grown on LAO. (b) Photograph of the thin films as a function of doping showing an enhancement in the transparency upon Ti doping; LAO is given on the right as a reference. (c) FOM of thin films of  \( \sim70 \)  nm at three wavelengths covering the entire visible range. The FOM is highly improved, especially for 30-50% Ti doped SNO (solid circles). The half-filled stars represent the best achieved FOM for each individual concentration obtained for the conditions given on the right. Unless explicitly mentioned, the thin films in Figure 1(b), (c) (solid circles) and throughout the manuscript are grown under the same conditions  \( pO_{2}=10^{-5} \)  mbar and  \( t\sim70 \)  nm.
 

## Results

## Theoretical Calculations

## (a) Electronic Properties

![](./images/1050293411485057031_4.jpg)

![](./images/1050293411485057031_5.jpg)

![](./images/1050293411485057031_6.jpg)

![](./images/1050293411485057031_7.jpg)

![](./images/1050293411485057031_8.jpg)

![](./images/1050293411485057031_9.jpg)

Figure 2: Band structure and partial density of states (bottom) for different supercells (top), and unfolded band structures of the  \( SN_{1-x}T_{x}O \)  system for (a,b) x = 0, (c,d) x = 0.25, and (e,f) x = 0,5. The yellow polyhedral represents the  \( NbO_{6} \)  octahedra and  \( TiO_{6} \)  octahedra are shown by the green polyhedral. The Fermi level shifts downwards indicating a decrease in the band gap but still remains well within the conduction band indicating a metallic-like conductivity.

To investigate the impact of Ti doping on the electronic features of the  \( SN_{1-x}T_{x}O \)  system, we perform DFT calculations. For these, we first construct a  \( 2\times2\times2 \)  supercell of SNO and then substitute 0, 2, and 4 Nb atoms with Ti atoms, resulting in effective compositions of x = 0, 0.25, and 0.50 in the  \( SN_{1-x}T_{x}O \)  system. Band structure calculations are then performed to obtain the crystal structures with lowest total energy. This setup aims to reduce the strong scattering resulting from the disorder caused by the introduction of doped atoms. In order to study the band changes induced by the doping of Ti atoms, we employ the band unfolding methodology as outlined by Popescu and Zunger to accurately determine the electronic properties \( ^{46-48} \) .
 

Figure 2 (a), (c), and (e) represent the supercell structure of  \( SN_{1-x}T_{x}O \)  used for the calculation of the band structure, while Figure 2 (b), (d), and (f) show the full and unfolded band structure and partial density of states (pDOS) for x = 0, 0.25, and 0.5, respectively. Here, the  \( NbO_{6} \)  octahedra are shown in yellow color and the  \( TiO_{6} \)  octahedra in green; the Fermi level is set to 0 in each case. From the pDOS, we see that the valence band maxima (VBM) in each case is dominated by O 2p orbitals, while the conduction band minima (CBM) is mainly composed of Nb 3d orbitals for x = 0 and 0.25, whereas for x = 0.5 both Nb and Ti 3d orbitals have equal contribution to the conduction band. Upon doping Ti into the system, the Fermi level shifts downward within the conduction band, indicating a reduction in the number of free carriers (electrons) in the system. Also, the position of CBM changes from  \( \sim \)  -1.3 eV to  \( \sim \) -0.8 eV from x = 0 to 0.5, indicating a Fermi level shift of  \( \sim \) 0.5 eV. Despite this huge shift, the Fermi level remains well within the conduction band, thus indicating a metallic character even for a large amount of Ti doping. From the unfolded band structure, one can see clearly that the nature of the band gap remains the same, i.e., the interband transition (O 2p  \( \rightarrow \)  Nb/Ti 3d) is indirect for all cases (along the A \( \rightarrow \)  \( \Gamma \)  direction).

As mentioned above, due to the scattering potential as well as the lost translational symmetry, the band structure unfolding results in several spurious bands for the doped compounds, owing to the incommensurability between the supercell and primitive cell and can be ignored. With these caveats, it is seen that the bands around the Fermi level retain their parabolic shape in all cases, which indicates that the effective mass and hence the mobility of the carriers is not expected to vary much from the mobility of SNO. Moreover, due to the shift in the Fermi level, the band gap ( \( E_{g} \) ) between the fully filled levels in the valence band to the conduction band decreases with increasing Ti doping. This should not come as a surprise, since the end products of  \( SN_{1-x}T_{x}O \)  (x = 0 and 1) have  \( E_{g} \approx -4.1 \)  eV (SNO) and 3.2 eV (STO), respectively. It can thus be expected that for intermediate composition,  \( E_{g} \)  remains between these values. This is
 

verified by the band structure properties shown in Figure 1 (see supplementary information Figure S1 for the band structure of STO).

(a)

![](./images/1050293411485057031_10.jpg)

(b)

![](./images/1050293411485057031_11.jpg)

(c)

![](./images/1050293411485057031_12.jpg)

Figure 3: (a) Absorption coefficient, (b) reflectivity, and (c) optical conductivity for  \( SN_{1-x}T_{x}O \)  in DFT (x = 0, 0.25, and 0.5). Ti doping shifts the absorbance and reflectivity minima below the visible range thus predicting an enhancement of transparency in the visible range. In (a), p-d transition represents the interband transition and d-d transition shows intraband transitions.

## (b) Optical Properties

While SNO has a large band gap ( \( \sim \)  4.1 to 4.5 eV), the transparency of SNO is not optimal due to strong intraband absorption and high  \( \omega_{p} \) . The intraband transition in  \( SN_{1-x}T_{x}O \)  cannot be explained by band structure studies alone, as it only provides meaningful insight for edge-to-edge transition and does not consider other effects such as Hubbard bands at higher energies, multiband effects etc. Hence, in order to get a deeper insight into the optical properties, we further calculate the frequency-dependent optical properties by DFT to simulate the behavior of light across the UV-Vis-NIR spectrum to take care of these effects.

Figure 3 (a) presents the DFT-calculated absorption coefficient of the  \( SN_{1-x}T_{x}O \)  system. While the absorption coefficient ( \( \alpha \) ) for the entire  \( SN_{1-x}T_{x}O \)  system is suppressed in the visible region ( \( \sim10^{5}~cm^{-1} \) ), it increases quite significantly on both sides of the visible spectrum. At high energies ( \( \geq4.0~eV \) ),  \( \alpha \)  increases quite significantly which is due to the p-d transition as shown. This is the familiar edge-to-edge transition (or  \( E_{g} \) ) which we get from band structure calculations (Figure 2) and which are very far from the visible region. However, an enhancement of  \( \alpha \)  also occurs on the lower energy side which is marked as d-d transition in the
 

figure and is the intraband absorption. As can be seen from Figure 3(a), doping with Ti mitigates this problem and enhances the transparency of the material. The effect of large doping is seen in the visible region as well, since the  \( \alpha \)  of  \( SN_{0.5}T_{0.5}O \)  is very low compared to the other two cases. Another important understanding of the optical property of  \( SN_{1-x}T_{x}O \)  is seen from the reflectivity data in Figure 3(b): the reflectivity drops to zero at  \( \sim2.4 \)  eV for SNO and increases suddenly at lower energies. When doping with Ti, the reflectivity edge begins however to gradually shift towards the lower energies until finally at x = 0.5 this reflectivity edge shifts entirely out of the visible spectrum, making  \( SN_{0.5}T_{0.5}O \)  highly transparent as compared to SNO. The shift of the absorption edge to lower energies as seen in the optical conductivity plot Figure 3(c) is consistent with the DFT band structure of Figure 2, where, as the concentration of Ti is increased, the CBM shifts upwards resulting in a smaller p-d transition energy.

The DFT obtained optical properties are helpful to gain insight into the effect of doping on the optical properties of  \( SN_{1-x}T_{x}O \) . However, due to strong correlations in the d orbitals of SNO, the simplistic Drude model used to calculate the optical properties does not fully agree with the experimental results. Further, including correlations by DMFT, in particular the mass enhancement ( \( Z^{-1} = m^{*}/m_{b} \) ) and scattering rate ( \( \tau^{-1} \) ) is essential \( ^{17} \) .

(a)

![](./images/1050293411485057031_13.jpg)

(b)

![](./images/1050293411485057031_14.jpg)

(c)

![](./images/1050293411485057031_15.jpg)

Figure 4: DMFT obtained optical properties of  \( SN_{1-x}T_{x}O \) : (a) absorption coefficient and (b) reflectivity. In both (a) and (b), the absorbance and reflectivity minima have a finite value, as opposed to the DFT obtained results, but are shifted below the visible spectrum, showing the same trend as DFT. (c) DMFT calculated optical conductivity.
 

In Figure 4 we present the DMFT obtained optical properties for x = 0 and 0.5 to get an accurate description of the inter- and intraband transitions across the spectrum. Comparing Figure 3(a) and 4(a), it is seen clearly that the inclusion of electron correlation results in enhanced scattering at low energies which further increases the absorption coefficient at lower energies. When comparing the DFT and DMFT results with the experimentally obtained  \( \alpha \)  (See SI-Figure S2), it is seen clearly that DMFT produces the correct behavior of  \( \alpha \) . Furthermore, the reflectivity minimum shown in Figure 4(b) is no longer zero, but finite, due to correlation-enhanced scattering at low energies. The resulting optical conductivity in Figure 4(c) shows a non-zero conductivity in the visible region even at higher doping concentrations. Nonetheless, the general trend is similar to DFT, i.e., Ti doping shifts the absorption edge and reflectivity edge towards the lower energy side of the visible spectrum.

What does this mean in terms of TCO properties? For a start, the shift in  \( \omega_{p} \)  results in the shift of the reflectivity and absorption edge below the visible spectrum. For a given material to be transparent to the visible light, its plasmon frequency should be lower than 1.75 eV and its band gap higher than 3.1 eV. By performing DFT+DMFT calculations, we have shown that we can shift the plasmon frequency below the visible spectrum whilst keeping the band gap higher than 3.1 eV by Ti doping of SNO.  \( SN_{1-x}T_{x}O \)  is expected to exhibit a metallic-like conductivity even for larger Ti doping. Let us now turn to the experimental results to verify the theoretical results.
 

## Experimental results

(a) Structural properties:

(a)

![](./images/1050293411485057031_16.jpg)

(b)

![](./images/1050293411485057031_17.jpg)

![](./images/1050293411485057031_18.jpg)

Figure 5: (a) HR-XRD spectrum of the (002) peak of  \( SN_{1-x}T_{x}O \)  system for x = (0, 0.15, 0.3, 0.5) grown epitaxially on (001) LAO. The peaks corresponding to the film and substrate are indicated by a dashed blue line. A shift in peak towards higher  \( 2\theta \)  values is seen as the composition of Ti is increased in the system. (b) Change of the out-of-plane lattice parameter of the thin films as a function of Ti composition shows a shrinkage in the lattice parameters of the  \( SN_{1-x}T_{x}O \)  system. Due to the compressive strain induced by LAO,  \( a_{oop} \)  is always larger than the lattice parameters obtained from Vegard's law. (c)  \( a_{oop}/a_{ip} \)  ratio, demonstrating that Ti doping reduces the compressive strain within the unit cell.

The structural characterization of the epitaxial  \( SN_{1-x}T_{x}O \)  system (x = 0, 0.15, 0.3, 0.5) grown on (001) LAO is studied with the help of high-resolution x-ray diffraction (HR-XRD). In each instance, only the (001) family of peaks corresponding to the  \( SN_{1-x}T_{x}O \)  system is observed, confirming the epitaxial nature of the thin films. In figure 5(a) we show the  \( \omega-2\theta \)  scans around the (002) diffraction peak for the thin films and the substrate to show the variation of peaks with Ti composition. The thin films are grown on (001) LAO single crystal substrates, with a lattice constant of 3.79 Å. As a result of the large lattice mismatch between the film and the substrate, a compressive strain is seen in all the films, which elongates the out of plane lattice parameter ( \( a_{oop} \) ). Further, when Nb (0.64 Å) is replaced by Ti (0.605 Å), the lattice shrinks due
 

to the smaller size of the Ti ion. This corresponds to the peak shift of (002) SN \( _{1-x} \) TxO to a higher 2θ value which increases as the amount of Ti increases in the composition. In Figure 5(b), we have calculated  \( a_{oop} \)  as a function of composition of Ti on SN \( _{1-x} \) TxO. The in-plane lattice parameter ( \( a_{ip} \) ) for all the films remains constant at 4.003 Å and, as seen in supplementary figure S3, the films are four-fold symmetric which implies that these films have a tetragonal structure. Moreover, we observe that there is a slight deviation from Vegard's law in all the cases ( \( a_{SNO} = 4.1\AA \) ,  \( a_{STO} = 3.94\AA \) ) \( ^{49} \) . It is known that both Nb and Ti ions have two valence states. When Nb \( ^{4+} \)  is replaced by Ti \( ^{4+} $ , the substitution is isovalent, whereas when two Ti \( ^{4+} \)  ions are replaced by Ti \( ^{3+} \)  and Nb \( ^{5+} \)  ions it is heterovalent \( ^{50} \) . The valency of Nb and Ti is highly dictated by the growth condition and in the case of isovalent substitution the  \( a_{oop} \)  should follow Vegard's law. Since our films do not follow Vegard's law ideally, it evidences that there is some intermixing of the different valence states amongst the Ti and Nb ions. These conclusions are consistent with the DFT and DMFT calculations, and we have shown in our previous work how the deposition condition affects the valency of Nb \( ^{43} \) . The  \( a_{oop}/a_{ip} \)  ratio in Figure 5(c) shows that the tetragonal distortion of thin films is reduced as the content of Ti is increased. This is further complemented by Figure S3(d), in which we see that the full width half maxima (FWHM) of the rocking curve in the case of SN \( _{0.5} \) Tx \( _{0.5\} \) O is reduced as compared to that of pure SNO, indicating a better epitaxial matching with the substrate.
 

## (b) Electronic Properties

(a)

![](./images/1050293411485057031_19.jpg)

(b)

![](./images/1050293411485057031_20.jpg)

Figure 6: (a) Measured sheet resistance for different compositions of Ti in  \( SN_{1-x}TxO \)  thin films. The sheet resistance increases gradually as the amount of Ti increases. The films exhibit a metallic nature for x = 0 - 0.3 but show a semiconductor type of behaviour for x = 0.5. However, the sheet resistance remains below  \( 100 \Omega \)  at RT (b) Experimentally obtained Hall mobility and carrier concentration for  \( SN_{1-x}TxO \)  thin films compared with theoretical carrier concentration.

The sheet resistance of the  \( SN_{1-x}TxO \)  thin films is shown in Figure 6 (a), demonstrating that all films are metallic. The room-temperature sheet resistance ( \( R_{s} \) ) increases from 18 to 89  \( \Omega\square^{-1} \)  as the concentration of Ti is increased; and the  \( SN_{1-x}TxO \)  films exhibit a metallic-type (d \( R_{s}/dT > 0 \) ) character up to x = 0.3 Ti doping but a semiconductor-like (d \( R_{s}/dT < 0 \) ) behaviour at x = 0.5. Since all the films are  \( \sim \) 70-80 nm thick, this yields a resistivity value ranging from  \( \sim \)  200-900  \( \mu\Omega\cdotcm \)  at room temperature (RT). In Figure 6(b), we show the calculated Hall mobility and carrier concentration for  \( SN_{1-x}TxO \)  thin films. For completeness, we have also included the theoretically calculated carrier concentration, using the formula  \( n^{theory} = n_{f.u.}/V_{f.u} \) . Here,  \( n_{f.u} \)  represents the number of electrons per formula unit,  \( V_{f.u} \)  is the volume and  \( n^{theory} \)  is the theoretically calculated carrier concentration. It is seen that the observed carrier concentration is consistently less than the expected carrier concentration. We attribute this change to heterovalent mixing of  \( Nb^{5+}/Nb^{4+} \)  and  \( Ti^{4+}/Ti^{3+} \)  ions for our deposition condition. However,
 

the mobility of the  \( SN_{1-x}T_{x}O \)  shows a reverse trend to the carrier concentration. We observe that the mobility ( \( \mu \) ) of the system increases unexpectedly from  \( \sim 3 \)  to  \( 7~cm^{2}V^{-1}s^{-1} \)  which is closer to the range of mobilities reported earlier for  \( SN_{1-x}T_{x}O \)  thin films \( ^{50} \) . This change in mobility cannot be explained easily as there might be several factors at play. One prospective explanation is the non-integer occupations of Ti  \( d^{0.58} \)  and Nb  \( d^{0,42} \) . This means weaker correlations between electrons, a reduced electron-electron scattering, and thus a higher mobility. A second factor increasing the mobility can be possibly attributed to the better epitaxy and reduced residual strain of the unit cell in Ti doped SNO system. This might suppress the scattering and increase the relaxation time of the electrons. In summary, all the films exhibit metallic character with a maximum sheet resistance of  \( 89~\Omega \)  at RT for x = 0.5 which is consistent with the electronic properties obtained theoretically. We next perform the optical characterization to evaluate the performance of  \( SN_{1-x}T_{x}O \)  as a TCO.

## (c) Optical Properties

(a)

![](./images/1050293411485057031_21.jpg)

(b)

![](./images/1050293411485057031_22.jpg)

Figure 7: (a) Optical transmittance spectra of  \( SN_{1-x}T_{x}O \)  thin films. The transmittance of the thin films increases from  \( \sim60\% \)  to 95% as x changes from 0 to 0.5. (b) Experimentally observed band gap and plasmon frequency as a function of Ti composition. The band gap remains well above 3.2 eV while decreasing the plasmon frequency below 1.75 eV.

Figure 7(a) shows the optical transmittance of  \( SN_{1-x}T_{x}O \)  thin films. As we predicted theoretically, the optical transmittance of the thin films increases as the amount of the Ti is
 

increased. For x = 0.3 and 0.5, the optical transmittance of the thin films reaches 87% and 95% at 550 nm (or 2.25 eV), the wavelength at which our eyes are most sensitive to. Moreover, it is seen that the transmittance of  \( SN_{1-x}T_{x}O \)  in the UV range ( \( \sim \) 300 nm) is 80-90%, whereas in the IR range ( \( \sim \) 1000 nm) it is around 60-70% (for x = 0.3 and 0.5). These transmittances significantly improve upon previously reported results for such strongly correlated systems and confirm the prediction made by DFT+DMFT that we showed earlier.

In figure 7(b) we have calculated the band gap and the plasmon frequency of these thin films. The band gap of the thin films is calculated with the help of Tauc's plot by considering an indirect transition (as seen in band unfolding results). The Tauc's plot and the calculated band gaps are shown in Figure S4. The plasmon frequency of the thin films is extracted through variable angle ellipsometry (VASE) by considering the zero crossover of the real part of the dielectric function. The VASE data along with the real and imaginary part of the dielectric function is given in Figure S5. For x = 0.3,  \( \omega_{p} \)  falls just inside the visible region, while for x = 0.5 it is completely outside. As a result of this, the optical transmittance of  \( SN_{0.5}T_{0.5}O \)  is further improved compared to  \( SN_{0.7}T_{0.3}O \) . The other condition for maintaining high transparency i.e., a band gap greater than 3.1eV, is observed across the entire doping range.

## (d) Figure of Merit

We finally evaluate the performance of  \( SN_{1-x}T_{x}O \)  as transparent conductor by invoking Haacke's FOM formula \( ^{17} \) :

 \[ FOM=\frac{T^{10}}{R_{s}}. \] 

Here T is the transparency and  \( R_{s} \)  is the sheet resistance. Taking the values of  \( R_{s} \)  and T at three different wavelengths, we cover the performance of  \( SN_{1-x}T_{x}O \)  in the entire visible region. Figure 1(c) shows the FOM obtained for thin films at 380, 550 and 700 nm. It is seen that
 

doping improves the optoelectronic properties of the thin films, especially at high wavelengths (low energies) due to the shift of the plasmon frequency below the visible region. The FOM of thin films increases from  \( \sim10^{-1} \)  (x = 0) to  \( 10^{1} \)  (x = 0.30) at  \( \lambda = 550 \)  nm which is a 100 times improvement in the performance of the parent transparent conductor SNO (and a  \( \sim1000 \)  times improvement at  \( \lambda=700 \)  nm). At higher doping concentration (x = 0.5), the sheet resistance of the thin film becomes quite large, still it manages to outperform SVO, ITO, SMO etc. All these studies validate the usefulness and potential of Ti doped SNO thin films for transparent electrodes.

As a final note, let us emphasize again that the film growth conditions, strain, deposition temperature, laser fluence, target to substrate distance, background partial pressure, thickness, etc. have a huge impact on the optoelectronic properties. These variations can even result in a metal to insulator transition (MIT) in strongly correlated systems, can make the films highly transparent or highly absorbing, depending on the use case. For example, the use of substrates like DyScO \( _{3} \) /KTaO \( _{3} \)/LSAT show a resistivity in the range of 10  \( \mu\Omega \) -cm while obtaining  \( \sim \) 50-80% transparency \( ^{29,42,51,52} \) , whereas for samples grown on LAO under different conditions SNO films exhibit a resistivity of  \( 10^{2} \) - \( 10^{7} \)   \( \mu\Omega \) -cm and transparency of 40-90% \( ^{39,43} \) . Therefore, to properly compare the optoelectronic properties of these films, we have kept the same conditions for each film and have not performed individual optimization for each doping concentration. However, in our previous work, we demonstrated that the optoelectronic properties of SNO thin films are also highly dependent on  \( pO_{2}^{43} \) . To verify the effect of  \( pO_{2} \)  on SN \( _{1-x} \) TxO thin films, we further grew films at different background partial pressures to show the variation in the optoelectronic properties. This partial optimization is displayed as stars in Figure 1(c) and reveals that the sheet resistance (as well as optical transparency) can be further tuned to the application of choice. Moreover, the trend of increasing FOM by Ti doping is maintained across the entire doping range. The complete list of samples, with their sheet resistance and FOM is given in Figure S6 of the supplementary information. It shows that we
 

can further enhance the FOM by performing individual optimization (i.e. by varying thickness, change of substrate, growth temperature, or changing) for every concentration.

## Discussion and Conclusion

![](./images/1050293411485057031_23.jpg)

Figure 8: Best achieved FOM obtained for  \( SN_{1-x}T_{x}O \)  (x = 0.3 and 0.5) thin films compared to other commonly studied transparent materials in the visible and UV spectrum showing that  \( {}^{13,18,27,29,41,44,52-59} \) .

In this work, we explored the unconventional design strategy to enhance the optical transparency of the strongly correlated material  \( SrNbO_{3} \)  by Ti doping and studied its potential as a new TCO, using a combined theoretical and experimental approach. The design principle employed here is focused on reducing the amount of carrier concentration through Ti doping, which is in contrast to conventional doping that focuses on inducing electronic conductivity in wide-band gap oxides through a Moss-Burstein shift. We observed here that Ti doping reduces the plasma frequency  \( \omega_{p} \) , shifting the reflection and absorption edge below the visible range. This boosts the transparency of  \( SN_{1-x}T_{x}O \)  from  \( \sim50\% \)  to 95% while keeping the sheet resistance below  \( 100\Omega \) , one of the basic requirements of a TCO. Our  \( SN_{1-x}T_{x}O \)  films also show a
 

remarkable improvement of optical transparency in the ultraviolet (UV) and near infrared (NIR) range of the spectrum, making it highly transparent across the whole UV-Vis-NIR spectrum.

In Figure 8, we compare the FOM of  \( SN_{1-x}T_{x}O \)  (x = 0.3 and 0.5) thin films with other widely studied transparent conductors. It is seen from the figure that  \( SN_{1-x}T_{x}O \)  outperforms ITO in both the visible and UV spectrum. This makes  \( SN_{1-x}T_{x}O \)  a particularly attractive option for solar cells, which requires high transparency across a large electromagnetic spectrum. In the visible range, it also outperforms the recently revealed series of strongly correlated materials (SVO, SMO,  \( SV_{0.5}M_{0.5}O \)  etc.) as well as other reported values of  \( SNO^{13,18,27,29,52,52,53} \) . The FOM can be further optimized by an appropriate choice of the substrate and should then even surpass the record FOM achieved by Jeong et al. \( ^{44} \)  for our parent compound SNO. Our calculated FOM in the UV spectrum is 3.1 and  \( 3.9 \times 10^{-3} \Omega^{-1} \)  for x = 0.3 and 0.5, which is comparable to La doped (Ba, Sr) \( SnO_{3} \)  reported recently as a promising TCO in the UV range \( ^{55-59} \) . Figure 8 clearly shows that Ti doped SNO system outperforms other materials as it covers a wider electromagnetic spectrum.

In conclusion, we shed light on hole doping of strongly correlated systems and find that it is an excellent way to enhance the optoelectronic properties. This strategy is straightforward and requires little to no optimization while boosting the FOM. The growth of thin films via other commonly used methods such as sputtering and molecular beam epitaxy (MBE) will further increase the FOM. Thus Ti-doped SNO bears excellent prospects for adaptation in industry. The good agreement of our DFT+DMFT and experimental results emphasizes the power of such a combined approach for identifying new materials for optoelectronics.

## Acknowledgements

The research funding from Shiv Nadar Institution of Eminence (Deemed to be University) (Grant No. SNS/PHY/2013-20) and DST-Science and Engineering Research Board (SERB)
 

India (Grant No. SR/FST/PS-I/2017/6C) and the Austrian Science Funds (FWF) through P 36213 is acknowledged. The high-performance computing facility offered by the School of Natural Sciences at Shiv Nadar Institution of Eminence (Deemed to be University) is used for theoretical calculations; DFT+DMFT calculations have been done on the Vienna Scientific Cluster (VSC). L. S. is supported by the National Natural Science Foundation of China (Grants No. 12422407). We acknowledge Prof. S. Dhar from IIT Bombay for performing HR-XRD measurements.

## Methods:

(a) Epitaxial growth of thin films: High purity powders of  \( SrCO_{3} \)  (Alfa Aesar, 99.9%),  \( Nb_{2}O_{5} \)  (Alfa Aesar, 99.9985%) and  \( TiO_{2} \)  (rutile, Alfa Aesar 99.9%) are mixed in proper molar ratio to get an effective Ti doping of 0, 15, 30, and 50%. These powders are then hand grounded using mortar pestle and calcined at 1473 K till we get a single orthorhombic phase of  \( Sr_{2}Nb_{2-x}Ti_{x}O_{7} \)  (x = 0 to 1). These are then pressed into pellets by applying a pressure of 20 metric tons using hydraulic press in a die set, before calcination in air at 1623K for 96 hours with intermediate grinding every 24 hours. These pellets are subsequently loaded in the PLD chamber (Neocera, USA) to be used as targets for the growth of thin film of appropriate concentration. Next, double side polished single crystal substrates of  \( LaAlO_{3} \)  (001) (MTI, USA) are loaded into the chamber. Once the base pressure drops to  \( 1 \times 10^{-7} \)  mbar we begin the thin film deposition by setting Oxygen partial pressure ( \( pO_{2} \) ) of  \( 1 \times 10^{-5} \)  mbar by supplying gas through the mass flow controller (MFC). The substrate is then heated to 1023 K in the same background pressure before starting the pulsed laser deposition (Coherent Excimer KrF laser,  \( \lambda = 248 \)  nm, Coherent GmbH, Germany). The target to substrate distance is kept constant at 50 mm. The laser fluence chosen for our deposition is  \( 0.8 Jcm^{-2} \)  at a repetition rate of 5Hz. The deposition for each set of doped films takes place under the same conditions until we get thin films of the desired thickness. The sample is finally
 

allowed to cool to room-temperature in the same background pressure as it was fabricated and taken out of the chamber for characterization.

(b) Film Characterization: The structural properties of the thin films are measured by high resolution X-ray diffraction at the Industrial Research and Consultancy Centre at IIT Bombay using a Rigaku Smart Lab diffractometer equipped with Cu Kα radiation ( \( \lambda = 1.54 \, \AA \) ). A  \( \vartheta - 2\vartheta \)  and  \( 2\vartheta_{x} \)  scan is conducted over a range of  \( 20^{\circ} \)  to  \( 80^{\circ} \)  with a step increment of  \( 0.001^{\circ} \) . The electrical properties of the thin films to determine resistivity, Hall mobility, and carrier concentrations are characterized with the help of physical property measurement system (Quantum Design Inc., USA). The resistance measurements are performed in van der Pauw geometry. The optical transmittance of the thin films is studied by ultraviolet-visible-near infrared spectrophotometer (Shimadzu Solidspec -3700, Japan). The thickness of the thin films and the dielectric functions are determined ex-situ using variable angle spectroscopic ellipsometry (VASE) (M-2000-UI, J. A. Woollam, USA). For fitting the data, we have used a combination of Drude and Lorentz oscillator models in CompleteEASE software till the root mean square error between our model and raw data is less than 5.

(c) DFT simulation: We perform first-principles calculations with the Vienna ab initio simulation package (VASP) based on projector augmented wave (PAW) pseudopotentials \( ^{60,61} \) . The atomic and electronic structure are investigated by employing the Perdew-Burke-Ernzerhof (PBE) exchange correlation potential \( ^{62} \) . To simulate the effect of Ti doping on SNO, we construct a  \( 2 \times 2 \times 3 \)  supercell of SNO and replace 0, 2, and 4 Nb ions to effectively get 0, 25, and 50% Ti doped SNO using a dense k-mesh of  \( 7 \times 7 \times 1 \) . The lattice constants were set to the experimental values. We choose a cut-off kinetic energy of 600 eV, which is 1.5 times the energy cutoff for O-ions. The bond lengths are relaxed until the energy convergence requirement of  \( 10^{-6} \)  eV.
 

with Hellman-Feynman forces on each atom at  \( 10^{-3} \)  eV/ \( \AA \)  is met. To improve total energy accuracy, a gamma-centered Monkhorst-Pack grid with 0.02  \( \AA \)  resolution was adopted. Once the bond length and angles are optimized, we perform band unfolding methods as implemented in vaspkit \( ^{63} \) .

(d) DMFT simulation: The DFT-level electronic band structures and optical properties of  \( SrNb_{1-x}Ti_{x}O_{3} \)  are recalculated using Wien2k \( ^{64-66} \)  with the PBE version of the generalized gradient approximation \( ^{62} \)  and the mBJ potential \( ^{67} \) . A dense k-mesh of  \( 13\times13\times13 \)  ( \( 7\times7\times7 \) ) for the  \( 2\times2\times2 \)  supercell of (doped)  \( SrNbO_{3} \)  ensures convergence. As before, Ti atoms are introduced into a  \( 2\times2\times2 \)  supercell of  \( SrNbO_{3} \)  to simulate doping. All lattice constants and atomic positions are obtained from structural relaxations performed using the VASP code \( ^{60,68,69} \) . The d-bands of the doped Ti and  \( t_{2g} \)  orbitals of Nb are wannierized \( ^{70,71} \)  using wien2wannier \( ^{72,73} \)  and supplemented by local density-density interactions with standard values \( ^{74-76} \)  of intra-orbital U = 5.5 eV, inter-orbital V = U-2J = 3.5 eV, and Hund's exchange J = 1.0 eV for Ti 3d-orbitals; as well as 3.0 eV, 2.4 eV, and 0.3 eV for Nb 4d-orbitals. The Nb orbitals are excluded from Wannier projections and subsequent DMFT calculations as they are far above the Fermi level. The generated Hamiltonian is solved at room temperature (300K) using continuous-time quantum Monte Carlo in the hybridization expansion \( ^{77} \)  as implemented in w2dynamics \( ^{78,79} \) . Spectra are analytically continued with the maximum entropy method \( ^{80,81} \) . Optical conductivities, and other optical properties such as reflectivity and absorption spectra are calculated using the WOPTIC code \( ^{82} \) .
 

## References:

1. Shi, J. et al. Wide Bandgap Oxide Semiconductors: from Materials Physics to Optoelectronic Devices. Adv. Mater. 33, 2006230 (2021).

2. Cortie, M. B., Arnold, M. D. & Keast, V. J. The Quest for Zero Loss: Unconventional Materials for Plasmonics. Adv. Mater. 32, 1904532 (2020).

3. Yu, X., Marks, T. J. & Facchetti, A. Metal oxides for optoelectronic applications. Nature Mater. 15, 383–396 (2016).

4. Altuntepe, A. et al. Hybrid transparent conductive electrode structure for solar cell application. Renewable Energy 180, 178–185 (2021).

5. Fonoll-Rubio, R. et al. Characterization of the Stability of Indium Tin Oxide and Functional Layers for Semitransparent Back-Contact Applications on Cu(In,Ga)Se \( _{2} \)  Solar Cells. Solar RRL 6, 2101071 (2022).

6. Azani, M., Hassanpour, A. & Torres, T. Benefits, Problems, and Solutions of Silver Nanowire Transparent Conductive Electrodes in Indium Tin Oxide (ITO)-Free Flexible Solar Cells. Adv. Energy Mater. 10, 2002536 (2020).

7. Rosli, N. N., Ibrahim, M. A., Ahmad Ludin, N., Mat Teridi, M. A. & Sopian, K. A review of graphene based transparent conducting films for use in solar photovoltaic applications. Renewable and Sustainable Energy Reviews 99, 83–99 (2019).

8. Khan, M. R., Gopidi, H. R. & Malyi, O. I. Optical properties and electronic structures of intrinsic gapped metals: Inverse materials design principles for transparent conductors. Applied Physics Letters 123, 061101 (2023).

9. Willis, J. & Scanlon, D. O. Latest directions in p-type transparent conductor design. J. Mater. Chem. C 9, 11995–12009 (2021).
 

10. Wang, J. et al. Application of Indium Tin Oxide/Aluminum-Doped Zinc Oxide Transparent Conductive Oxide Stack Films in Silicon Heterojunction Solar Cells. ACS Appl. Energy Mater. 4, 13586–13592 (2021).

11. Boileau, A. et al. Highly Transparent and Conductive Indium-Free Vanadates Crystallized at Reduced Temperature on Glass Using a 2D Transparent Nanosheet Seed Layer. Adv Functional Materials 32, 2108047 (2022).

12. Zhang, L. et al. Correlated metals as transparent conductors. Nature Mater. 15, 204–210 (2016).

13. Ha, Y., Byun, J., Lee, J. & Lee, S. Design Principles for the Enhanced Transparency Range of Correlated Transparent Conductors. Laser & Photonics Reviews 15, 2000444 (2021).

14. Stoner, J. L. et al. Chemical Control of Correlated Metals as Transparent Conductors. Adv Funct. Materials 29, 1808609 (2019).

15. Brahlek, M. et al. Opportunities in vanadium-based strongly correlated electron systems. MRS Communications 7, 27–52 (2017).

16. Mirjole, M., Sánchez, F. & Fontcuberta, J. High Carrier Mobility, Electrical Conductivity, and Optical Transmittance in Epitaxial SrVO \( _{3} \)  Thin Films. Advanced Functional Materials 29, 1808432 (2019).

17. Si, L., Kaufmann, J., Zhong, Z., Tomczak, J. M. & Held, K. Pitfalls and solutions for perovskite transparent conductors. Phys. Rev. B 104, L041112 (2021).

18. Ha, Y. & Lee, S. Oxygen-Vacancy-Endurable Conductors with Enhanced Transparency Using Correlated  \( 4d^{2} \)  SrMoO \( _{3} \)  Thin Films. Adv. Funct. Mater. 30, 2001489 (2020).

19. Zhu, M. et al. Thickness dependence of metal–insulator transition in  \( SrMoO_{3} \)  thin films. Journal of Applied Physics 132, 075303 (2022).

20. Wells, M. P. et al. Tunable, Low Optical Loss Strontium Molybdate Thin Films for Plasmonic Applications. Advanced Optical Materials 5, 1700622 (2017).
 

21. Biswas, M., Misra, D. & Kundu, T. K. Strain induced variations in transport and optical properties of  \( SrVO_{3} \) : a DFT+U study. Eur. Phys. J. B 96, 74 (2023)

22. Paul, A. & Birol, T. Strain tuning of plasma frequency in vanadate, niobate, and molybdate perovskite oxides. Phys. Rev. Materials 3, 085001 (2019).

23. Wang, C. et al. Tuning the metal-insulator transition in epitaxial  \( SrVO_{3} \)  films by uniaxial strain. Phys. Rev. Materials 3, 115001 (2019).

24. Paul, A. & Birol, T. Cation order control of correlations in double perovskite  \( Sr_{2}VNbO_{6} \) . Physical Review Research 2, 033156 (2020).

25. Gu, M., Wolf, S. A. & Lu, J. Metal-insulator transition in  \( SrTi_{1-x}V_{x}O_{3} \)  thin films. Appl. Phys. Lett. 103, 223110 (2013).

26. Kanda, T. et al. Electronic structure of  \( SrTi_{1-x}V_{x}O_{3} \)  films studied by in situ photoemission spectroscopy: Screening for a transparent electrode material. Phys. Rev. B 104, 115121 (2021).

27. Mohammadi, M. et al. Tailoring Optical Properties in Transparent Highly Conducting Perovskites by Cationic Substitution. Advanced Materials 35, 2206605 (2023).

28. Wan, D. et al. New Family of Plasmonic Photocatalysts without Noble Metals. Chem. Mater. 31, 2320–2327 (2019).

29. Mirjolet, M. et al. Optical Plasmon Excitation in Transparent Conducting  \( SrNbO_{3} \)  and  \( SrVO_{3} \)  Thin Films. Adv. Optical Mater. 9, 2100520 (2021)

30. Asmara, T. C. et al. Tunable and low-loss correlated plasmons in Mott-like insulating oxides. Nat. Commun. 8, 15271 (2017).

31. Asmara, T. C. et al. Photoinduced metastable dd exciton-driven metal-insulator transitions in quasi-one-dimensional transition metal oxides. Commun. Phys. 3, 206 (2020).

32. Zhang, Y. et al. Low thermal conductivity of  \( SrTiO_{3}-LaTi_{3} \)  and  \( SrTiO_{2}-SrNbO_{3} \)  thermoelectric oxide solid solutions. J. Am. Ceram. Soc. 104, 4075–4085 (2021).
 

33. Zhang, J. et al. Extremely large magnetoresistance in high-mobility  \( SrNbO_{3}/SrTiO_{3} \)  heterostructures. Phys. Rev. B 104, L161404 (2021).

34. Ok, J. M. et al. Correlated oxide Dirac semimetal in the extreme quantum limit. Sci. Adv. 7, eabf9631 (2021).

35. Sun, C. & Searles, D. J. Electronics, Vacancies, Optical Properties, and Band Engineering of Red Photocatalyst  \( SrNbO_{3} \) : A Computational Investigation. J. Phys. Chem. C 118, 11267–11270 (2014).

36. Song, D. et al. Electronic and plasmonic phenomena at nonstoichiometric grain boundaries in metallic  \( SrNbO_{3} \) . Nanoscale 12, 6844–6851 (2020).

37. Xu, X., Random, C., Efstathiou, P. & Irvine, J. T. S. A red metallic oxide photocatalyst. Nature Mater. 11, 595–598 (2012).

38. Chen, C. et al. Atomic-Scale Origin of the Quasi-One-Dimensional Metallic Conductivity in Strontium Niobates with Perovskite-Related Layered Structures. ACS Nano 11, 12519–12525 (2017).

39. Wan, D. Y. et al. Electron transport and visible light absorption in a plasmonic photocatalyst based on strontium niobate. Nat. Commun. 8, 15070 (2017).

40. Oka, D., Hirose, Y., Nakao, S., Fukumura, T. & Hasegawa, T. Intrinsic high electrical conductivity of stoichiometric  \( SrNbO_{3} \)  epitaxial thin films. Phys. Rev. B 92, 205102 (2015).

41. Roth, J. et al. Sputtered  \( Sr_{x}NbO_{3} \)  as a UV-Transparent Conducting Film. ACS Appl. Mater. Interfaces 12, 30520–30529 (2020).

42. Di Pietro, P. et al. Oxygen-Driven Metal–Insulator Transition in  \( SrNbO_{3} \)  Thin Films Probed by Infrared Spectroscopy. Adv Elect Materials 8, 2101338 (2022).

43. Kumar, S. et al. Modulation of the optical and transport properties of epitaxial  \( SrNbO_{3} \)  thin films by defect engineering. Journal of Applied Physics 135, 015303 (2024).

44. Jeong, J. Transparent conducting oxides  \( SrNbO_{3} \)  thin film with record high figure of merit.
J. Eur. Ceram. Soc. 44, 6764 - 6760 (2024)
 

45. Georges, A., Kotliar, G., Krauth, W. & Rozenberg, M. J. Dynamical mean-field theory of strongly correlated fermion systems and the limit of infinite dimensions. Rev. Mod. Phys. 68, 13–125 (1996).

46. Popescu, V. & Zunger, A. Extracting E versus  \( \overrightarrow{k} \)  effective band structure from supercell calculations on alloys and impurities. Phys. Rev. B 85, 085201 (2012).

47. Ngo, T. D., Dao, T. D., Cuong, N. T., Umezawa, N. & Nagao, T. Combined first-principles and electromagnetic simulation study of n-type doped anatase  \( TiO_{2} \)  for the applications in infrared surface plasmon photonics. Phys. Rev. Materials 4, 055201 (2020).

48. Medeiros, P. V. C., Stafström, S. & Björk, J. Effects of extrinsic and intrinsic perturbations on the electronic structure of graphene: Retaining an effective primitive cell band structure by band unfolding. Phys. Rev. B 89, 041407 (2014).

49. Arya, M. et al. Combining experimental and modelling approaches to understand the expansion of lattice parameter of epitaxial  \( SrTi_{1-x}Ta_{x}O_{3} \)  (x = 0–0.1) films. Computational Materials Science 217, 111917 (2023).

50. Zhang, Y. et al. Thermoelectric phase diagram of the  \( SrTiO_{3}-SrNbO_{3} \)  solid solution system. Journal of Applied Physics 121, 185102 (2017).

51. Bigi, C. et al. Direct insight into the band structure of  \( SrNbO_{3} \) . Phys. Rev. Materials 4, 025006 (2020).

52. Park, Y. et al.  \( SrNbO_{3} \)  as a transparent conductor in the visible and ultraviolet spectra. Commun. Phys. 3, 1–7 (2020).

53. Liu, J. All-inorganic flexible epitaxial  \( SrNbO_{3}/mica \)  thin films with ultrahigh figure of merit as indium-free transparent conductors. Ceramics International 50, 6580–6586 (2024).

54. Jeon, H. M. et al. Homoepitaxial  \( \beta \) -Ga \( _{2} \) O \( _{3} \)  transparent conducting oxide with conductivity  \( \sigma = 2323 \, S cm^{-1} \) . APL Materials 9, 101105 (2021).
 

55. Seo, J., Kim, J., Kim, H., Kim, J. H. & Char, K. Fully Deep-UV Transparent Thin Film Transistors Based on SrSnO \( _{3} \) . Adv Elect Materials 10, 2300547 (2024).

56. Liu, F. et al. Deep-ultraviolet transparent conducting  \( SrSnO_{3} \)  via heterostructure design. Preprint at https://doi.org/10.48550/arXiv.2405.08915 (2024).

57. Kim, J. et al. Deep-UV Transparent Conducting Oxide La-Doped  \( SrSnO_{3} \)  with a High Figure of Merit. ACS Appl. Electron. Mater. 4, 3623–3631 (2022).

58. Zhang, J. et al. Deep UV transparent conductive oxide thin films realized through degenerately doped wide-bandgap gallium oxide. Cell Reports Physical Science 3, 100801 (2022).

59. Nagashima, Y. et al. Deep Ultraviolet Transparent Electrode: Ta-Doped Rutile  \( Sn_{1-x}Ge_{x}O_{2} \) . Chem. Mater. 34, 10842–10848 (2022).

60. Kresse, G. & Joubert, D. From ultrasoft pseudopotentials to the projector augmented-wave method. Phys. Rev. B 59, 1758–1775 (1999).

61. Blöchl, P. E. Projector augmented-wave method. Phys. Rev. B 50, 17953–17979 (1994).

62. Perdew, J. P., Burke, K. & Ernzerhof, M. Generalized Gradient Approximation Made Simple. Phys. Rev. Lett. 77, 3865–3868 (1996).

63. Wang, V., Xu, N., Liu, J.-C., Tang, G. & Geng, W.-T. VASPKIT: A user-friendly interface facilitating high-throughput computing and analysis using VASP code. Computer Physics Communications 267, 108033 (2021).

64. Schwarz, D. K. An Augmented Plane Wave + Local Orbitals Program for Calculating Crystal Properties. (Technische Universität, Vienna, 2001)

65. Blaha, P. et al. WIEN2k: An APW+lo program for calculating the properties of solids. The Journal of Chemical Physics 152, 074101 (2020).

66. Ambrosch-Draxl, C. & Sofo, J. O. Linear optical properties of solids within the full-potential linearized augmented planewave method. Computer Physics Communications 175, 1–14 (2006).
 

67. Tran, F. & Blaha, P. Accurate Band Gaps of Semiconductors and Insulators with a Semilocal Exchange-Correlation Potential. Phys. Rev. Lett. 102, 226401 (2009).

68. Kresse, G. & Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B 54, 11169–11186 (1996).

69. Kresse, G. & Furthmüller, J. Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set. Computational Materials Science 6, 15–50 (1996).

70. Wannier, G. H. The Structure of Electronic Excitation Levels in Insulating Crystals. Phys. Rev. 52, 191–197 (1937).

71. Marzari, N., Mostofi, A. A., Yates, J. R., Souza, I. & Vanderbilt, D. Maximally localized Wannier functions: Theory and applications. Rev. Mod. Phys. 84, 1419–1475 (2012).

72. Mostofi, A. A. et al. wannier90: A tool for obtaining maximally-localised Wannier functions. Computer Physics Communications 178, 685–699 (2008).

73. Kuneš, J. et al. Wien2wannier: From linearized augmented plane waves to maximally localized Wannier functions. Computer Physics Communications 181, 1888–1895 (2010).

74. Nekrasov, I. A. et al. Momentum-resolved spectral functions of  \( SrVO_{3} \)  calculated by LDA + DMFT. Phys. Rev. B 73, 155112 (2006).

75. Si, L. et al. Quantum Anomalous Hall State in Ferromagnetic  \( SrRuO_{3} \)  (111) Bilayers. Phys. Rev. Lett. 119, 026402 (2017).

76. Okamoto, S. et al. Correlation effects in (111) bilayers of perovskite transition-metal oxides. Phys. Rev. B 89, 195121 (2014).

77. Gull, E. et al. Continuous-time Monte Carlo methods for quantum impurity models. Rev. Mod. Phys. 83, 349–404 (2011).

78. Parragh, N. et al. Effective crystal field and Fermi surface topology: A comparison of d- and dp- orbital models. Phys. Rev. B 88, 195116 (2013).
 

79. Wallerberger, M. et al. w2dynamics: Local one- and two-particle quantities from dynamical mean field theory. Computer Physics Communications 235, 388–399 (2019).

80. Gubernatis, J. E., Jarrell, M., Silver, R. N. & Sivia, D. S. Quantum Monte Carlo simulations and maximum entropy: Dynamics from imaginary-time data. Phys. Rev. B 44, 6011–6029 (1991).

81. Sandvik, A. W. Stochastic method for analytic continuation of quantum Monte Carlo data. Phys. Rev. B 57, 10287–10290 (1998).

82. Assmann, E. et al. woptic: Optical conductivity with Wannier functions and adaptive k-mesh refinement. Computer Physics Communications 202, 1–11 (2016).
 

# Supplementary Information for

# Boosting the transparency of metallic SrNbO_{3} through Ti doping

## Contents:

Figure S1: Band structure and density of states for  \( SrTiO_{3} \) 

Figure S2: Comparison of experimentally obtained absorption coefficient with DFT and DMFT results

Figure S3: In plane XRD spectrum,  \( a_{oop} \)  and  \( a_{ip} \) , rocking curve, and phi scan of thin films

Figure S4: Tauc's plot for calculation of band gap.

Figure S5: Ellipsometry data for calculation of plasmon frequency

Figure S6: Sheet resistance and FOM for thin films as a function of  \( pO_{2} \)
 
![](./images/1050293411485057031_24.jpg)

Figure S1: Band structure of pure STO which is an insulator with the Fermi level in the band gap.

(a)

![](./images/1050293411485057031_25.jpg)

(b)

![](./images/1050293411485057031_26.jpg)

Figure S2: Comparison of DFT and DMFT obtained absorption spectra for (a) SNO and (b) \( SN_{0.5}T_{0.5}O \)  with the experimental results.
 

(a)

![](./images/1050293411485057031_27.jpg)

(b)

![](./images/1050293411485057031_28.jpg)

(c)

![](./images/1050293411485057031_29.jpg)

![](./images/1050293411485057031_30.jpg)

Figure S3: (a) In-plane  \( 2\theta_{x} \)  scan (b) calculated in-plane and out-of-plane lattice parameter (c) Phi scan around (103) peak of  \( SN_{1-x}T_{x}O \)  (x=0 and 0.5) (d) Variation in the rocking curve around (002) peak for x=0 and 0.5.

(a)

![](./images/1050293411485057031_31.jpg)

(b)

![](./images/1050293411485057031_32.jpg)

Figure S4: (a) Tauc’s plot for calculating the indirect band gap. (b) Calculated band gap of the  \( SN_{1-x}T_{x}O \)  thin films as function of Ti doping.
 

(a)

![](./images/1050293411485057031_33.jpg)

(b)

![](./images/1050293411485057031_34.jpg)

(c)

![](./images/1050293411485057031_35.jpg)

(d)

![](./images/1050293411485057031_36.jpg)

Figure S5: Representative (a)  \( \Psi \)  and (b)  \( \Delta \)  of the ellisometric data at  \( 65^{\circ} \)  angle of incidence. The open circles represent the raw data, and the black solid line represents the fitting model. (c) Real and (d) imaginary part of the extracted dielectric constants by ellipsometry.
 

(a)

![](./images/1050293411485057031_37.jpg)

(b)

![](./images/1050293411485057031_38.jpg)

Figure S6: (a) Sheet resistance and (b) figure of merit obtained for thin films grown at different oxygen partial pressure. The shaded portions in each curve represent the growth conditions we have chosen in the main manuscript.
 
