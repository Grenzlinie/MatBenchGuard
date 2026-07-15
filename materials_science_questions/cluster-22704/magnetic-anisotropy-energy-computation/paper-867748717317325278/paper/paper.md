
# Spin excitations of individual Fe atoms on Pt(111): impact of the site-dependent giant substrate polarization

A. A. Khajetoorians, \( ^{1,*} \)  T. Schlenk, \( ^{1} \)  B. Schweflinghaus, \( ^{2} \)  M. dos Santos Dias, \( ^{2}M. \) 

Steinbrecher, \( ^{1} \)  M. Bouhassoune, \( ^{2} \)  S. Lounis, \( ^{2,\dagger} \)  J. Wiebe, \( ^{1,\ddagger} \)  and R. Wiesendanger \( ^{1} \) 

 \( ^{1} \) Institute for Applied Physics, Universität Hamburg, D-20355 Hamburg, Germany

 \( ^{2} \) Peter Grünberg Institut and Institute for Advanced Simulation,

Forschungszentrum Jülich & JARA, Jülich, Germany

(Dated: June 14, 2018)

## Abstract

We demonstrate using inelastic scanning tunneling spectroscopy (ISTS) and simulations based on density functional theory that the amplitude and sign of the magnetic anisotropy energy for a single Fe atom adsorbed onto the Pt(111) surface can be manipulated by modifying the adatom binding site. Since the magnitude of the measured anisotropy is remarkably small, up to an order of magnitude smaller than previously reported, electron-hole excitations are weak and thus the spin-excitation exhibits long lived precessional lifetimes compared to the values found for the same adatom on noble metal surfaces.
 

The ability to encode magnetic information in the limit of single atoms deposited on surfaces (adatoms) relies crucially on understanding and controlling the magnetic anisotropy energy (MAE) and the underlying magnetization dynamics. The observation of giant MAE of Co adatoms on the Pt(111) surface [1] has spurred many experimental and theoretical investigations of this property in different nanosystems, towards the final goal of stabilizing a single magnetic adatom. Two techniques have emerged over the last decade which allow for single atomic spin detection, namely inelastic scanning tunneling spectroscopy (ISTS) [2–6] and spin-resolved STS [6–8]. While hysteresis has yet to be found for an isolated single adatom on a non-magnetic surface, it has recently been shown by these techniques that artificially constructed ensembles of a few magnetic atoms show evidence of stability as a result of either ferromagnetic or antiferromagnetic exchange interactions within the ensemble [9, 10]. In these examples the substrate is paramount for establishing the magnetic properties of the ensemble and can dramatically affect the spin dynamics. Ultimately, tailoring the magnetic properties on such length scales requires a proper description of the strong hybridization between the adatoms and the surface, and how this affects the static and dynamic properties of the magnetic moments.

It remains an open question how to appropriately describe the magnetization dynamics of atomic spins placed on non-magnetic surfaces, as hybridization can dramatically alter the magnetism of the adatom. A simple approximation is to describe the impurity as a molecular magnet, namely to treat the magnetic moment as a quantized spin, and approximate the crystal field produced by the substrate in terms of powers of spin operators [11]. While these approaches describe transition metal adatoms on substrates where the atomic 3d states are well localized [3, 5, 12], they fail to capture the importance of itinerant effects, like electron-hole excitations, which arise when the magnetic moment is strongly coupled to conduction electrons, as on a metallic surface [13, 14]. As we have previously shown, the itinerant character of metallic surfaces must be considered in order to account for the measured precessional lifetimes and the g-shifts of Fe adatoms [6, 15].

We report here on a surprising behavior: by monitoring the magnetic excitations of individual atoms with ISTS, we show that Fe adatoms on Pt(111) exhibit a relatively low MAE and long precessional lifetime. Moreover, these properties are strongly dependent on which hollow site the adatom occupies. These findings are in stark contrast to those of Ref. [4]: inelastic excitations, seen in the absence of a magnetic field, with characteristic energies of
 

10 meV and 6 meV for Co and Fe respectively, were interpreted as magnetic excitations with extremely short precessional lifetimes. After carefully reexamining the case of Fe adatoms, we conclude that the MAE is an order of magnitude weaker and the precessional lifetimes are up to two orders of magnitude longer than originally reported. Magnetic field dependent measurements confirm these findings and reveal that the type of binding site can totally reorient the preferred orientation of the magnetic moment (parallel/perpendicular to the surface), and affect the strength of the MAE ( \( E_{a} \) ), the precessional lifetime ( \( \tau \) ), and g-factor, as demonstrated by atomic manipulation. We recapture these experimental observations utilizing first-principles approaches based upon time-dependent density functional theory (TD-DFT), from which we compute the MAE and magnetic excitations, and compare them with effective spin Hamiltonian model calculations of the magnetic excitation spectra. We show that the binding site dependence of the giant Pt polarization cloud created by the Fe adatoms is crucial for describing the MAE and the spin dynamics, revealing the itinerant nature of the system.

Scanning tunneling spectroscopy (STS) was performed in a home-built UHV STM facility at a base temperature of  \( T = 0.3 \, K \)  and in magnetic fields, B, up to 12 T applied perpendicular to the sample surface [16]. The STM tip was etched from tungsten wire and in-situ flashed to remove residual contaminants. The Pt(111) surface was cleaned in-situ by repeated cycles of  \( Ar^{+} \) sputtering and annealing to  \( T = 740^{\circ}C \) , with a final flash at  \( T = 1000^{\circ}C \) . Subsequently, the clean surface was cooled to  \( T \approx 4 \, K \)  and exposed to Fe resulting in a distribution of single Fe atoms on the surface residing at two surface hollow sites (fcc, hcp) [17]. The differential conductance (dI/dV) was recorded with the feedback off via a lock-in technique with a modulation voltage of  \( V_{mod} = 40 - 200 \, \muV \)  and modulation frequency  \( f_{mod} = 4.1 \, kHz \) .

Fig. 1(a-b) illustrates atomic manipulation [8, 17, 18] of an Fe adatom residing on the Pt(111) surface induced by the STM tip between an fcc hollow site ( \( Fe_{fcc} \) ) to an hcp hollow site ( \( Fe_{\text{hcp}} \) ). STS recorded on top of both  \( Fe_{fcc} \)  and  \( Fe_{hcp} \)  (Fig. 1(c)), before and after manipulation, exhibits strong step-like features symmetric to  \( E_{F} \)  below  \( |V_{S}| < 1 \)  meV for each binding site. These steps are characterized by their position (E), width (W) and intensity ( \( J \) ).  \( Fe_{hcp} \)  shows a stronger excitation intensity and a narrower width as compared to  \( Fe_{fcc} \)  at B = 0 T. STS done on many other Fe adatoms display the same behavior. The step intensities are typically  \( J_{fcc} \approx 8\% \)  and  \( J_{hcp} \approx 12\% \) . Such features can be identified as
 

a tunneling-induced excitation of the adatom, when compared to the substrate [19]. Both types of spectra can be reproduced by manipulating the same atom between different binding sites, anywhere on the clean surface, demonstrating that the E, W, and J are binding site dependent.

To confirm that we measure inelastic magnetic excitations, we apply a magnetic field [2] and follow the behavior of the dI/dV spectra and their numerical derivatives  \( d^{2}I/dV^{2} \)  (Fig. 2(a-d)). The finite zero-field excitation energy ( \( E_{gap} \) ), is typically  \( E_{gap}^{fcc} \approx 0.75 \)  meV and  \( E_{gap}^{thcp} \approx 0.19 \)  meV. For  \( Fe_{fcc} \) , E shows a linear increase as the magnetic field increases (Fig. 3(a)), like seen for Fe atoms on both Cu(111) and Ag(111) [6, 15]. On the other hand,  \( Fe_{hcp} \)  shows an interesting non-linear behavior in E, W, and J as the field is increased (Fig. 3(b)). For magnetic fields in the range of B = 0 - 3.5 T, there is a plateau-like behavior, namely E, W, and J only change slightly. For B > 3.5 T, the magnetic excitation shows a linearly increasing trend in E, J, W similar to  \( Fe_{fcc} \) . In the following, these disparate trends are interpreted as consequences of an out-of-plane MAE for  \( Fe_{fcc} \)  and an easy plane MAE for  \( Fe_{hcp} \) .

To analyze the connection between the MAE and the binding site, we performed DFT calculations with the Korringa–Kohn–Rostoker Green function method (KKR–GF) in a real-space approach [20, 21]. Pt(111) is notoriously challenging because of its high magnetic polarizability [22, 23], owing to an extended polarization cloud which surrounds the magnetic adatom, like seen for Pd [24–26]. In this light, we carefully checked all calculations. For computational details see [17]. The computed spin moments are  \( 3.40 \mu_{B} \)  ( \( 4.42 \mu_{B} $ ) for  \( Fe_{fcc} \)  and  \( 3.42 \mu_{B} \)  ( \( 4.57 \mu_{B} $ ) for  \( Fe_{hcp} \) , where the values refer to the adatom (whole 3D cluster — 62 Pt atoms), respectively. The orbital moments are for  \( Fe_{fcc} \)   \( 0.11 \mu_{B} \)  ( \( 0.23 \mu_{B} $ );  \( Fe_{hcp} \)   \( 0.08 \mu_{B} \)  ( \( 0.22 \mu_{B} $ ). The MAE yields  \( E_{a}^{fcc} = -2.05 \)  meV (out-of-plane) and  \( E_{a}^{hcp} = +0.50 \)  meV (easy plane). Here, it was crucial to include a large number of substrate atoms in order to converge the calculation [17]. For a small cluster with 10-12 Pt atoms, calculations of both  \( Fe_{hcp} \)  and  \( Fe_{fcc} \)  yield an out-of-plane easy axis with values for the MAE in-line with those calculations based on a supercell KKR-GF method [4]. However, only after including more than 60 Pt atoms, the calculated MAE finally converges and reveals a reorientation of the MAE of  \( Fe_{hcp} \)  into the easy-plane configuration. This shows that the spin polarization of the substrate generated by each Fe adatom type effectively reduces the total MAE, as similarly discussed in Ref. [26].
 

Fig. 3(a-b) show results of magnetic field-dependent spectra with high energy resolution, at smaller field steps  \( \Delta B = 0.5 \)  T. A subset of this data was already shown in Fig. 2 for clarity. Following [3, 5, 12], an effective spin Hamiltonian model is used for phenomenological analysis:  \( \hat{H}_{J} = D\hat{J}_{z}^{2} + g\mu_{\mathrm{B}}B\hat{J}_{z} \)  [11, 17, 27]. This is the sum of the anisotropy energy and the Zeeman energy. The model parameters are eigenvalue J, the anisotropy constant D (negative for out-of-plane easy axis and positive for easy plane) and the g-factor. B is the applied magnetic field which is out-of-plane here. The theoretical excitation spectra shown in Fig. 3(c-d) are derived by considering an interaction  \( \hat{s} \cdot \hat{J} + u\hat{1} \)  between the tunneling electron and the impurity [28–31]. While the first term describes the exchange interaction between the tunneling electron spin  \( \hat{s} \)  and the atomic spin  \( \hat{J} \) , u quantifies the strength of elastic tunneling. As the hybridization of the moment with the substrate is strong, the assumption of an isolated effective spin is not justified. Therefore, we mimic the effect of the substrate electrons by introducing an artificial broadening of the excitation steps using an effective temperature  \( T_{eff} \)  to fit the experimental W, where  \( T_{eff}^{fcc} = 2 \)  K and  \( T_{eff}^{hcp} = 0.8 \)  K. The value of J was chosen to be closest to the DFT calculated total magnetic moments of the whole cluster which includes the surrounding substrate, namely J = 5/2 for both  \( F_{fcc} \)  and  \( F_{hecp} \) . However, the qualitative behavior is the same for other values of J, as the sign of D determines the phenomenology.

The results of modeling the data in Fig. 3(a-b) are shown in Fig. 3(c-d). Taking  \( D_{fcc} = -0.19 \)  meV,  \( F_{fcc} \)  is understood to be always in an out-of-plane (maximum  \( M_{J} \) ) ground state, as the excitation energy increases linearly with B. For  \( D_{hcp} = 0.08 \)  meV,  \( F_{hecp} \)  has an in-plane (minimum  \( M_{J} \) ) ground state when B = 0. The plateau region corresponds to the eventual transition of the ground state to out-of-plane (increasing  \( M_{J} \) ). Once this is reached, at the indicated crossing point (gray arrow), the same linear behavior at higher fields is observed like for  \( F_{fcc} \) . It is important to note that, in addition to the spin excitation, we cannot rule out a Kondo effect masked below the spin excitation for  \( F_{hecp} \) . However, the Kondo temperature is most likely below our measurement temperature [17] and is neglected since we recapture the measurement in the modeling without considering a significant Kondo effect. To compare the modeled spectra and the values of D to the DFT calculated values the magnetic anisotropy energy  \( E_{a} \)  and the model anisotropy parameter D are connected by the correspondence principle:  \( D(J) = E_{a}/J(J + 1) \) . From the DFT calculations, we extract the values,  \( D_{\mathrm{fcc}}(5/2) = -0.23 \)  meV and  \( D_{\mathrm{hcp}}(5/2) = 0.06 \)  meV, which are consistent with
 

the experimentally determined model parameters. Itinerant effects such as the broadened linewidth, the observed shift in g for  \( Fe_{fcc} \) , and the field dependence of the linewidth are beyond the scope of the model and will be discussed below in the context of TD-DFT calculations of the dynamical magnetic susceptibility.

The precessional lifetime  \( \tau \)  and g-factor were extracted by measuring E and W (FWHM) as a function of magnetic field for many Fe atoms (Fig. 4(a-b)). We extract  \( \tau \)  at zero field by considering  \( \tau = \hbar/(2W_{0}) \) , where  \( W_{0} \)  is the intrinsic linewidth [32] derived from gaussian fitting the numerically derived  \( d^{2}I/dV^{2} \)  spectra (Fig. 2(c-d)). The g-factor, where  \( g = \mathrm{d}E/\mathrm{d}(\mu_{\mathrm{B}}B) \) , was determined from a linear fit to  \( E(B) \)  (after the plateau, in the case of  \( Fe_{hcp} \) ). For  \( Fe_{fcc} \)  an enhanced g-factor is measured,  \( g_{fcc} = 2.4 \pm 0.1 \) , and  \( \tau_{\mathrm{fcc}}(B = 0\mathrm{T}) = 0.70 \pm 0.12 \)  ps. The g-factor of  \( Fe_{hcp} \)  was fitted for B > 3.5 T, yielding  \( g_{hcp} = 2.0 \pm 0.15 \) . The measured precessional lifetime is as large as  \( \tau_{\mathrm{hcp}}(B = 0\mathrm{T}) \approx 2.5 \)  ps [33].

The measured values are in good agreement with the dynamical transverse magnetic susceptibility  \( \chi \)  computed from TD-DFT combined with the KKR-GF method [14, 34]. The effect of spin-orbit coupling is approximated by including an additional magnetic field which mimics  \( E_{gap} \) . From the imaginary part of  \( \chi \) , which gives the density of states for spin excitations, we extract the calculated excitation energy and width as a function of B, shown in Fig. 4(c-d) [17]. By linear fits, we then extract g and  \( \tau \) . We obtain  \( g_{fcc} = 2.24 \)  and  \( g_{hcp} = 2.18 \) , illustrating the trend that  \( Fe_{fcc} \)  maintains a higher g-value as compared to  \( Fe_{hcp} \) . Inputting the experimental  \( E_{gap} \)  for both cases, the calculated  \( \tau \)  is found to be larger for  \( Fe_{hcp} \)  (4.8 ps) than for  \( Fe_{fcc} \)  (1.2 ps), as experimentally observed. As spin-orbit coupling was not included in these calculations, it is possible that it can modify the computed values of the g-factor and of  \( \tau \) . The shift in g and the reduction of  \( \tau_{fcc}(B > 0\mathrm{T}) \) ,  \( \tau_{\mathrm{hcp}}(B > 3.5\mathrm{T}) \)  for increasing magnetic field result from spin-dependent scattering by conduction electrons (Stoner excitations) which damp the spin precession, as previously observed in related systems [6, 14, 15, 34]. Unlike Fe atoms on both the Cu(111) and Ag(111) surfaces, Fe atoms on Pt(111) show comparatively larger precessional lifetimes (due to the lower excitation energies), which decrease more weakly ( \( d\tau/dB \) ) in a magnetic field than in the aforementioned systems.

Previous measurements of inelastic excitations of single Fe atoms on Pt(111) [4], done in the absence of a magnetic field, reported only one adsorption site, unlike the two observed here, which exhibits a much smaller excitation intensity (dashed line Fig. 2(c-d)) occurring at
 

energies 7 – 30 times higher than the energies at which we unambiguously observe magnetic excitations. Measurements performed as a function of temperature,  \( T = 0.3 - 4.3 \, K \)  [17] do not exhibit any inelastic excitations for clean Fe adatoms, up to tunneling currents  \( I_{t} \leq 30 \, nA \) , that resemble those seen in Ref. 4. They do reveal, however, that at  \( T = 4.3 \, K \)  only  \( Fe_{fcc} \)  displays a clear magnetic excitation but at an energy much lower than the previously reported value. The effect of temperature simply broadens the excitation but does not shift it. Aside from the striking dependence of the magnetism on the binding site dependence, the values of  \( \tau \)  measured here are two orders of magnitude larger than those reported in ref. [4].

In conclusion, we find that Fe adatoms on Pt(111) exhibit a remarkably small MAE, in stark contrast to Co atoms on Pt(111) [1]. The measured values are substantially lower compared to what was previously reported [4], as well as compared to lighter substrates [6, 15]. Previous XMCD measurements of Fe/Pt(111) suggested small values of the MAE [35], but the site dependence and magnitude of this quantity could not be extracted. Moreover, the surprising finding that the type of occupied hollow site can completely alter the orientation of the magnetic moment is illuminated by DFT when considering the contribution of the large polarization cloud induced in the Pt substrate. A similar binding site dependence of the MAE was previously predicted for Fe adatoms on Pd(111) [26]. Our measurements and calculations reveal that, while Pt(111) sustains such a large polarization cloud (we consider a radius  \( \approx 0.75 \)  nm), it also gives rise to longer lifetimes and relatively weak damping due to Stoner excitations for the Fe adatoms as compared to magnetic excitations of Fe on other noble metal surfaces [6, 15]. This goes against what might be expected from the stronger hybridization between the d-states of the adatoms and the d-states of Pt, as compared with the sp-states near the Fermi energy from the Cu and Ag substrates. Given that the lifetime of the spin precession is inversely proportional to the excitation energy, the much smaller zero field magnetic excitation gap, controlled by the low MAE, is responsible for this behavior. These results illustrate that the behavior of Fe/Pt(111), a typical system used for out-of-plane device technology, can dramatically change when scaled to the atomic limit.

We would like to thank H. Brune, W. Wulfhekel, A. Lichtenstein, V. Caciuc, G. Bihlmayer, and S. Blügel for fruitful discussions. A. A. K., T. S., M. S., J. W. and R. W. acknowledge funding from SFB668-A1 and GrK1286 of the DFG and from the ERC Advanced Grant “FURORE.” A.A.K. also acknowledges Project no. KH324/1-1 from the
 

Emmy-Noether-Program of the DFG. B. S., M. S. D., M. B. and S. L. acknowledge support of the HGF-YIG Programme VH-NG-717 (Functional Nanoscale Structure and Probe Simulation Laboratory-Funsilab).

* Corresponding author: akhajeto@physnet.uni-hamburg.de

† s.lounis@fz-juelich.de

‡ jwiebe@physnet.uni-hamburg.de

[1] P. Gambardella et al., Science 300, 1130 (2003).

[2] A. J. Heinrich et al., Science 306, 466 (2004).

[3] C. F. Hirjibehedin et al., Science 317, 1199 (2007).

[4] T. Balashov et al., Phys. Rev. Lett. 102, 257203 (2009).

[5] A. A. Khajetoorians et al., Nature 467, 1084 (2010).

[6] A. A. Khajetoorians, et al., Itinerant nature of atom-magnetization excitation by tunneling electrons, Phys. Rev. Lett. 106, 037205 (2011).

[7] F. Meier et al., Science 320, 82 (2008).

[8] A. A. Khajetoorians et al., Nature Physics 497, 497 (2012).

[9] S. Loth et al., Science 335, 196 (2012).

[10] A. A. Khajetoorians et al., Science 339, 55 (2013).

[11] D. Gatteschi, R. Sessoli, Molecular nanomagnets (Oxford Uni. Press, Oxford, ed. 1, 2006)

[12] S. Loth et al., Nature Phys. 6, 340 (2010).

[13] D. L. Mills and P. Lederer, Phys. Rev. 160, 590 (1967).

[14] S. Lounis, A. T. Costa, R. B. Muniz, D. L. Mills, Dynamical Magnetic Excitations of Nanostructures from First Principles, Phys. Rev. Lett. 105, 187205 (2010).

[15] B. Chilian, A. A. Khajetoorians, S. Lounis, A. T. Costa, D. L. Mills, J. Wiebe, R. Wiesendanger, Anomalously large g factor of single atoms adsorbed on a metal substrate, Phys. Rev. B 84, 212401 (2011).

[16] J. Wiebe et al., Rev. Sci. Inst. 75, 4871 (2004).

[17] See online supplemental material.

[18] D. M. Eigler, E. K. Schweizer, Positioning single atoms with a scanning tunneling microscope, Nature 344, 524 (1990).
 

[19] B. C. Stipe, M. A. Rezaei, and W. Ho, Science 280, 1732 (1998).

[20] N. Papanikolau, R. Zeller, P. H. Dederichs, J. Phys.: Condens. Matter 14, 2799 (2002).

[21] D.S.G. Bauer, Rheinisch-Westfälische Technische Hochschule (RWTH), Aachen (2013).

[22] O. Sipr, S. Bornemann, J. Minar, H. Ebert, Phys. Rev. B 82, 174414 (2010).

[23] F. Meier, S. Lounis, J. Wiebe, L. Zhou, S. Heers, P. Mavropoulos, P. H. Dederichs, S. Blügel, R. Wiesendanger, Spin polarization of platinum (111) induced by the proximity to cobalt nanostripes, Phys. Rev. B 83, 075407 (2011).

[24] G. J. Nieuwenhuys, Magnetic behaviour of cobalt, iron and manganese dissolved in palladium, Advances in Physics 24, 515 (1975).

[25] A. Oswald, R. Zeller, P. H. Dederichs, Giant moments in Palladium, Phys. Rev. Lett 56, 1419 (1986).

[26] P. Blonski, A. Lehnert, S. Dennler, S. Rusponi, M. Etzkorn, G. Moulas, P. Bencok, P. Gambardella, H. Brune, J. Hafner, Magnetocrystalline anisotropy energy of Co and Fe adatoms on the (111) surfaces of Pd and Rh, Phys. Rev. B 81, 104426 (2010).

[27] D. Dai, H. Xiang, M. H. Whangbo, Effects of spin-orbit coupling on magnetic properties of discrete and extended magnetic systems, Journal of Computational Chemistry 29, 2187 (2008).

[28] J. P. Gauyacq, N. Lorente, F. D. Novaes, Excitation of local magnetic moments by tunneling electrons, Progress in Surface Science 87, 73 (2012).

[29] J. Fernández-Rossier, Theory of Single-Spin Inelastic Tunneling Spectroscopy, Phys. Rev. Lett. 102, 256802 (2009).

[30] J. Fransson, Spin inelastic electron tunneling spectroscopy on local spin adsorbed on surface, Nano. Lett. 9, 2414-2417 (2009).

[31] B. Chilian, A. A. Khajetoorians, J. Wiebe, R. Wiesendanger, Experimental variation and theoretical analysis of the inelastic contribution to atomic spin excitation spectroscopy, Phys. Rev. B 83, 195431 (2011).

 \[ \left[32\right]\ W=\sqrt{\left(1.7V_{\mathrm{mod}}\right)^{2}+\left(5.4k_{\mathrm{B}}T\right)^{2}+\left(W_{0}\right)^{2}} \] 

[33] Values up to  \( E_{gap}^{hcp} \approx 0.3 \)  meV and lifetimes down to  \( \tau_{hcp} \approx 1.2 \)  ps are measured because of energy resolution broadening resulting from an increased  \( V_{mod} \)  utilized during particular measurements.

[34] S. Lounis, A. T. Costa, R. B. Muniz, D. L. Mills, Theory of local dynamical magnetic suscep-
 

tibilities from the Korringa-Kohn-Rostoker Green function method, Phys. Rev. B 83, 035109 (2011).

[35] A. Lehnert, Swiss Federal Institute of Technology, Lausanne (2009).
 
![](./images/867748717317325278_1.jpg)

![](./images/867748717317325278_2.jpg)

![](./images/867748717317325278_3.jpg)

FIG. 1. STM constant-current images (a) before and (b) after manipulating the top left Fe adatom from an fcc to an hcp hollow site on Pt(111). The center of the drawn black atomic lattice corresponds to one of two possible hollow sites. ( \( V_{S} = 6 \)  mV,  \( I_{t} = 500 \)  pA,  \( T = 0.3 \)  K; manipulation parameters:  \( V_{S} = 2 \)  mV,  \( I_{t} = 50 \)  nA). The colorscale represents  \( \Delta z = 0.12 \)  nm. (c) ISTS of an Fe adatom at an hcp site (red) and an fcc site (blue) as compared to the background spectrum on the Pt(111) substrate (black). Each spectrum is vertically offset for clarity (stabilization:  \( V_{S} = 6 \)  mV,  \( I_{t} = 3 \)  nA,  \( V_{mod} = 40 \)   \( \mu \) V,  \( T = 0.3 \)  K)
 
![](./images/867748717317325278_4.jpg)

![](./images/867748717317325278_5.jpg)

![](./images/867748717317325278_6.jpg)

![](./images/867748717317325278_7.jpg)

FIG. 2. Magnetic field dependent ISTS (dI/dV and numerical d²I/dV²) of an Fe adatom on an fcc site (a-c, normalized to the substrate) and hcp site (b-d, unnormalized). The spectra in (a) and (b) are offset for clarity. The dashed line indicates the previously reported excitation spectra for comparison [4]. (stabilization:  \( V_{S} = 6 \)  mV,  \( I_{t} = 3 \)  nA,  \( V_{mod} = 40 \)  μV, T = 0.3 K)
 
![](./images/867748717317325278_8.jpg)

![](./images/867748717317325278_9.jpg)

![](./images/867748717317325278_10.jpg)

FIG. 3. Magnetic field dependence of the measured ISTS intensity for (a)  \( Fe_{fcc} \)  (b)  \( Fe_{hcp} \)  and the simulated ISTS intensity based on the effective spin Hamiltonian (see text) assuming: (c)  \( D_{fcc} = -0.19 \)  meV,  \( J_{fcc} = 5/2 \) ,  \( g_{fcc} = -2.4 \) ,  \( u_{fcc} = 2.3 \) ,  \( T_{eff}^{fcc} = 2 \)  K (d)  \( D_{hcp} = 0.08 \)  meV,  \( J_{hcp} = 5/2 \) ,  \( g_{hcp} = -2.3 \) ,  \( T_{eff}^{hcp} = 0.8 \)  K. Level diagrams for (e)  \( Fe_{fcc} \)  and (f)  \( Fe_{hcp} \) . The eigenvalues  \( M_{J} \)  of  \( \hat{J}_{z} \)  are indicated by numbers. (stabilization:  \( V_{S} = 6 \)  mV,  \( I_{t} = 3 \)  nA,  \( V_{mod} = 40 \)  μV, T = 0.3 K)
 
![](./images/867748717317325278_11.jpg)

![](./images/867748717317325278_12.jpg)

![](./images/867748717317325278_13.jpg)

![](./images/867748717317325278_14.jpg)

FIG. 4. The experimental excitation energy (E: red) and FWHM (W: blue) of the linewidth for (a)  \( Fe_{fcc} \) , (b)  \( Fe_{hcp} \) , and the calculated excitation energy (red) and FWHM (blue) for (c)  \( Fe_{fcc} \)  and (d)  \( Fe_{hcp} \)  extracted from the  \( \operatorname{Im}(\chi) \)  (the gray rectangle represents the magnetic field range where the  \( Fe_{hcp} \)  ground state is not the maximum  \( M_{J} \)  state). Dashed lines represent the linear fit and the error bars represent the largest range of measured values. The effective energy resolution in (a-b) was  \( \Delta E \approx 0.12 - 0.3 \)  meV.
 
