**ION HYDRATION STUDIED BY X-RAY COMPTON SCATTERING**

K. Nygård,^{*} M. Hakala, S. Manninen, and K. Hämäläinen
Division of X-ray Physics, Department of Physical Sciences, P.O.B. 64, University of Helsinki, FI-00014, Helsinki, Finland

M. Itou, A. Andrejczuk, and Y. Sakurai
Japan Synchrotron Radiation Research Institute (JASRI), SPring-8, 1-1-1 Kouto, Sayo, Mikazuki, Hyogo 679-5198, Japan

(Received 31 August 2005; revised manuscript received 14 November 2005; published 27 January 2006)

We present an x-ray Compton scattering study on aqueous lithium chloride as a function of concentration, ranging from dilute solutions to saturation. The experimental observations are analyzed by simulations based on model cluster calculations within the density functional theory. The Compton scattering technique is found to be sensitive predominantly to the ion-ion and ion-oxygen bond-length distributions as well as to the hydration number and ion pairing. We explain the concentration-induced changes in the ground-state electron momentum densities by formation of hydration shells around the ions, providing upper limits for the average ion-oxygen bond lengths. In particular, this study provides stringent constraints on the hydration shells of chloride ions.

DOI: 10.1103/PhysRevB.73.024208
PACS number(s): 78.70.Ck, 71.15.Mb, 61.25.Em, 33.15.Dj

### I. INTRODUCTION

Ion hydration is of vast importance in, e.g., chemistry, biophysics and environmental sciences, closely related to chemical reactions in aqueous solutions, and thus it has been studied widely. Nevertheless, our knowledge of ion hydration, for example, the structure and dynamics of hydration shells, is far from complete.^{1,2} For instance, although several structural studies on lithium and chloride ions solvated in liquid water have been reported, details concerning the local arrangement of water molecules around these ions is still somewhat diffuse. Concerning the structure of their hydration shells, there is a relatively large variation in reported values of both hydration numbers as well as ion-ion and ion-oxygen distances.^{1,2}

The traditional experimental techniques for studying the local structure of molecular liquids are neutron and x-ray diffraction. Since the diffraction study of aqueous lithium chloride by Narten, Vaslow, and Levy,^{3} using both neutrons and x rays, there have been several subsequent studies.^{4-10} As aqueous LiCl is composed of four elements, it is characterized by a total of ten partial radial distribution functions (RDFs), complicating the experimental characterization. In fact, there is a variation in experimental results and today there seems to be no consensus on the detailed local structure of aqueous LiCl. Similarly, numerous simulations have been reported in which an equally large variation in the local structures is found.^{11-18} *Ab initio* molecular dynamics (MD) simulations are currently limited by the size of the simulation box while classical MD simulations suffer less from such limitations. In the latter case, however, the large variation of the simulation results can be attributed to the parameters used, e.g., the acquired partial RDFs strongly depend on the empirical force fields used in the simulations.^{19} Due to these insufficiencies, complementary methods are clearly needed for the study of ion hydration.

X-ray Compton scattering, i.e., inelastic scattering at large energy and momentum transfers, probes the ground-state electron momentum density.^{20,21} Traditionally the technique has been applied to investigations on the electronic structure of hard condensed materials, including studies on, e.g., fermiology,^{22} correlation effects^{23} and novel materials such as superconductors.^{24} As Compton scattering probes the electron density in momentum space, it is a complementary technique to neutron and x-ray diffraction. Subsequent to the early study by Narten and co-workers,^{3} Compton scattering studies were performed on aqueous LiCl.^{25,26} However, due to experimental limitations proper structural information was not obtained. In recent years, with the development of synchrotron radiation sources, Compton scattering has emerged as a tool for studying subtle bonding effects^{27-31} as well as coordination and local geometry in liquid water.^{32,33} The connection between the features in the Compton scattering spectrum and chemical bonding should, however, be made with care. The initial suggestion of a partly covalent nature of the hydrogen bond (H bond) in ice Ih^{28} was not supported by subsequent theoretical analysis.^{27,29,30} Rather, Compton scattering is sensitive to H bonding in water mainly through the exchange interaction.^{32} The sensitivity of the technique to chemical bonds can be stated as the "bond oscillation principle" (BOP), i.e., the electron momentum densities associated with chemical bonds exhibit damped oscillations in the direction of the bond, explaining the experimental observations in Compton scattering studies on molecular systems.^{34}

In the present work we apply x-ray Compton scattering to study the local structure of aqueous LiCl at various concentrations, ranging from dilute solutions to saturation. The experimental spectra are compared to electronic structure calculations utilizing model clusters, thereby extending the ideas of a previous study^{32} to the case of hydrated ions. Such a computational scheme is preferred over using snapshot structures derived from MD simulations, in order to specifically study which geometrical quantities are observed in the Compton scattering experiment. The experiment and model computations show that Compton scattering indeed is a sensitive tool for studies of ion hydration and that it is sensitive to both the ion-ion and ion-oxygen distances as well as to the coordination number and ion pairing. Thus Compton scatter-


ing data can be regarded as a critical test of both classical and *ab initio* MD simulation results on hydrated ions and, more generally, ion solvation.

## II. THEORY AND MODEL SYSTEMS

### A. Theory and computations

The theory of Compton scattering is well known. $^{20,35}$ Within the impulse approximation, $^{36}$ the double-differential cross section is given by
$$
\frac{d^{2} \sigma}{d \Omega d \omega_{2}}=C\left(\omega_{1}, \omega_{2}, \phi\right) J(q), \quad(1)
$$
where $\omega_{1}$ ($\omega_{2}$) is the energy of the incident (scattered) photon, $\phi$ the scattering angle and $q$ a scalar electron momentum variable. The cross section separates into the quantity $C(\omega_{1},\omega_{2},\phi)$, which depends only on the experimental setup, and the Compton profile $J(q)$, which depends only on the ground state of the electronic system under study. For isotropic systems the Compton profile can be expressed as $^{35}$
$$
J(q)=\frac{1}{2} \int_{|q|}^{\infty} \frac{I(p)}{p} d p. \quad(2)
$$

Here $I(p)$ is the radial electron momentum distribution, which can be expressed in terms of the three-dimensional ground-state electron momentum density $N(\mathbf{p})$ as
$$
I(p)=\int_{0}^{2 \pi} \int_{0}^{\pi} N(\mathbf{p}) p^{2} \sin \theta d \theta d \phi. \quad(3)
$$

Thus the isotropic Compton profile is a spherically averaged one-dimensional projection of the ground-state electron momentum density. As a consequence, the Compton profile normalizes to the number of electrons in the system. The isotropic Compton profile was recently shown to contain fundamental information on the coordination and local geometry of liquid water. $^{32,33}$

In the present work we determine the momentum density $N(\mathbf{p})$, and hence the Compton profile $J(q)$, by solving the real-space electronic structure of model clusters within the density functional theory (DFT). $^{37,38}$ In this scheme the electron momentum density is given by $^{32}$
$$
N(\mathbf{p})=\sum_{i}(2 \pi)^{-3}\left|\int \mathrm{e}^{-i \mathbf{p} \cdot \mathbf{r}} \psi_{i}^{\mathrm{KS}}(\mathbf{r}) d \mathbf{r}\right|^{2}, \quad(4)
$$
where $\psi_{i}^{\mathrm{KS}}(\mathbf{r})$ is the Kohn-Sham (KS) orbital and the sum is over the occupied states. It should be noted that although the KS orbitals are formally merely auxiliary functions, they can be regarded as approximations to the true wave functions when computing momentum densities. $^{39}$ Moreover, by comparison to Hartree-Fock (HF) and Møller-Plesset second-order perturbation theory (MP2) calculations, the approximation of using KS orbitals in Compton scattering simulations on water clusters has been shown to be reasonable. $^{27,32}$

All electronic-structure calculations are performed using the computer program STOBE-DEMON, $^{40}$ utilizing linear combinations of contracted Gaussian basis functions for the KS orbitals. The exchange and correlation parts of the gradient-corrected exchange-correlation functional used in the computations are given by Hammer, Hansen, and Norskov $^{41}$ and Perdew, Burke, and Ernzerhof, $^{42}$ respectively. For oxygen atoms and chloride (lithium) ions we use a triple-zeta (double-zeta) valence plus polarization-type basis set. For hydrogen atoms we employ a primitive set $^{43}$ augmented by one $p$ function in a $[3s,1p]$ contraction.

![](./images/812117110258925569_1.jpg)

FIG. 1. Schematic geometry of model clusters used to simulate the hydration shell of (a) lithium (light gray) and (b) chloride ions (dark gray). The black spheres correspond to water molecules.

### B. Model clusters

In the present work we analyze our experimental results by employing computations utilizing model clusters. In particular, effects of ion-ion and ion-water distances on the Compton profile are studied. Furthermore, since we subtract the Compton profile of polycrystalline LiCl in the experimental analysis (see Sec. III for details), the Compton profile of polycrystalline LiCl is also simulated. Based on earlier neutron scattering experiments, angular bond distortions and concentration-dependent intramolecular effects on the water molecules are neglected. $^{4,6}$ For the intramolecular geometry of the water molecule we use the O-H bond length of $0.970\ \mathring{A}$ and the H-O-H angle of $106.06^{\circ}$, based on neutron diffraction data of heavy water. $^{44}$

Extending the ideas of a previous study $^{32}$ to ion hydration, the contribution of the first ion hydration shell to the Compton profile is studied using model clusters. The symmetry of the oxygen positions in the hydration shell of chloride (lithium) ions is assumed to be $O_{h}$ ($T_{d}$). $^{2,3}$ The chloride (lithium) ion is surrounded by a hydration shell of $n=0...6$ ($n=0...4$) water molecules at a distance of $R_{\text{OCl}}^{\text{short}}$ ($R_{\text{OLi}}^{\text{short}}$) and $6-n$ ($4-n$) water molecules at a distance of $R_{\text{OCl}}^{\text{long}}=8.0\ \mathring{A}$ ($R_{\text{OLi}}^{\text{long}}=8.0\ \mathring{A}$). The definitions of these geometrical quantities are shown in Fig. 1. For the shorter ion-water distances ($R_{\text{OX}}^{\text{short}}$, X=Li,Cl) we make use of two models with the short distances representing the approximate lower and upper values reported in earlier studies. $^{1,2}$ The two models are denoted A and B, respectively. In the case of chloride ions, one of the hydrogen atoms of each coordinating water molecule is directed towards the ion. For lithium both hydrogen atoms of the coordinating water molecules are symmetrically directed away from the ion. For chloride (lithium) ions the models are labeled 1A and 1B (2A and 2B). The relevant distances of the model clusters (1A, 1B, 2A and 2B) are summarized in Table I.

<table>
<caption>TABLE I. Specification of the model clusters of the first hydration shell around chloride (Cl⁻) and lithium (Li⁺) ions; $n$ water molecules are at a distance of $R_{OCl}^{\text{short}}$ ($R_{OLi}^{\text{short}}$) from the chloride (lithium) ion and $6-n$ ($4-n$) water molecules at a distance of $R_{OCl}^{\text{long}}$ ($R_{OLi}^{\text{long}}$) from the chloride (lithium) ion.</caption>
<tr><th>Model</th><th>System</th><th>$R_{OCl}^{\text{short}}$ or $R_{OLi}^{\text{short}}$</th><th>$R_{OCl}^{\text{long}}$ or $R_{OLi}^{\text{long}}$</th></tr>
<tr><td>1A</td><td>Cl⁻(H₂O)ₙ</td><td>3.0 Å</td><td>8.0 Å</td></tr>
<tr><td>1B</td><td>Cl⁻(H₂O)ₙ</td><td>4.0 Å</td><td>8.0 Å</td></tr>
<tr><td>2A</td><td>Li⁺(H₂O)ₙ</td><td>2.0 Å</td><td>8.0 Å</td></tr>
<tr><td>2B</td><td>Li⁺(H₂O)ₙ</td><td>2.5 Å</td><td>8.0 Å</td></tr>
</table>

Ion pairing is studied using larger Li⁺Cl⁻(H₂O)ₙ clusters, where $n{=}8$–10 (see Fig. 2). For $n{=}10$, this constitutes a fourfold coordinated lithium ion and a sixfold coordinated chloride ion, the geometrical arrangement of both hydration shells being as above. The hydration shells are arranged such that two water molecules are on a straight line between the ions. The oxygen-oxygen distance between these boundary water molecules is chosen to be $R_{OO}{=}3.0$ Å, slightly longer than the average distance in room temperature water.⁴⁵ This cluster is taken to represent a solvent-separated ion pair (denoted SSIP-A) (Fig. 2). For $n{=}9$, one molecule in the hydration shell is shared, i.e., there is only one water molecule between the ions (denoted SSIP-B). One of the hydrogen atoms of the shared water molecule is directed towards the chloride ion, i.e., the H bond between the chloride ion and the shared water molecule is kept intact. Finally for $n{=}8$, there are no water molecules between the ions, i.e., the ions

![](./images/812117110258925569_2.jpg)

FIG. 2. Schematic geometry of Li⁺Cl⁻(H₂O)ₙ model clusters used to simulate ion pairing. The dark (light) gray spheres correspond to chloride (lithium) ions and the black spheres to water molecules. (a) $n{=}10$ (SSIP-A), (b) $n{=}9$ (SSIP-B) and (c) $n{=}8$ (CIP).

<table>
<caption>TABLE II. Parameters for the Li⁺Cl⁻(H₂O)ₙ, $n{=}8$–10, model clusters used to simulate ion pairing.</caption>
<tr><th>Model</th><th>$R_{OO}$ (Å)</th><th>$R_{OCl}$ (Å)</th><th>$R_{OLi}$ (Å)</th><th>$R_{LiCl}$ (Å)</th></tr>
<tr><td>3A</td><td>3.0</td><td>3.0</td><td>2.0</td><td>2.0</td></tr>
<tr><td>3B</td><td>3.0</td><td>3.0</td><td>2.5</td><td>2.5</td></tr>
<tr><td>3C</td><td>3.0</td><td>4.0</td><td>2.5</td><td>2.5</td></tr>
</table>

are in direct contact. The distance between the ions in this cluster is denoted by $R_{LiCl}$. Again, this cluster is identified as a contact ion pair (CIP). As for the models of hydration shells, several clusters (labeled 3A, 3B and 3C) with different ion-ion and ion-oxygen distances are constructed. The relevant distances of the model clusters (3A, 3B and 3C) are summarized in Table II.

In Figs. 4–8 to be discussed in Sec. IV, we plot differences of Compton profiles in the form $J_{\text{bond}}(q){=}J(q){-}J_{\text{ref}}(q)$, where the reference profiles $J_{\text{ref}}(q)$ are those of free ions and water monomers. The notation $J_{\text{bond}}(q)$ is used to emphasize that the plotted quantity is the total effect on the Compton profile of the interaction between the ions and/or water molecules. Furthermore, in order to compare the different model calculations with each other quantitatively, we have also plotted them on a common scale, as a fraction of the peak value [at $q{=}0$ atomic units (a.u.) of momentum] of the water monomer Compton profile. The common scale is shown in the right-hand $y$ axis of Figs. 4–8.

### III. EXPERIMENT

The experiment was conducted at the beamline BL08W at SPring-8 (Hyogo, Japan). The 115 keV incident radiation was produced by an elliptic multipole wiggler and monochromatized by a doubly bent Si monochromator, utilizing the (400) reflection. The size of the incident beam at the sample was $1(\text{H}){\times}2(\text{V})$ mm². The scattering angle was $\phi{=}165^\circ$ and the scattered radiation was analyzed using the standard Cauchois-type high-resolution spectrometer, utilizing the Si(620) reflection of a triply layered bent-crystal analyzer. The position-sensitive detection system consisted of an x-ray image intensifier, optical lenses and a digital charge coupled device (CCD) camera, working in single-photon counting mode. Details about the beamline and the spectrometer can be found elsewhere.⁴⁶⁻⁴⁸

The total momentum resolution of the spectrometer was $\Delta q{=}0.20$ a.u. The count rate was about 30 cps at $J(0)$ within a 0.03 a.u. momentum bin. At the Compton peak a minimum of $6{\times}10^{5}$ counts were collected in each spectrum, leading to a statistical inaccuracy of 0.13% or smaller. However, since the changes in the Compton profiles are smooth, a larger momentum bin was used in the final part of the data analysis without affecting either the shape or the amplitude of the Compton profile difference. Hence the final statistical inaccuracy in each spectrum was about 0.05% at the Compton peak in a 0.18 a.u. momentum bin. As the changes in the Compton profiles are very small, care has to be taken to

<table>
<caption>TABLE III. Concentrations of the aqueous LiCl samples studied, determined from fits to the experimental Compton profiles.</caption>
<thead>
<tr>
<th>Mole fraction ratio
($x_{\text{H}_2\text{O}}/x_{\text{LiCl}}$)</th>
<th>Molality
(m)</th>
</tr>
</thead>
<tbody>
<tr>
<td>131</td>
<td>0.424</td>
</tr>
<tr>
<td>23.6</td>
<td>2.35</td>
</tr>
<tr>
<td>11.7</td>
<td>4.74</td>
</tr>
<tr>
<td>5.63</td>
<td>9.86</td>
</tr>
<tr>
<td>2.43</td>
<td>22.8</td>
</tr>
</tbody>
</table>

ensure a good quality and consistency of the data. Therefore, during the experiment spectra were measured several times for each concentration and verified to be identical within the statistical accuracy, before adding them together using the associated statistical accuracy as a weight. Thus nonstatistical fluctuations could be minimized.

During the experiment, Compton profiles of aqueous LiCl were acquired at five different concentrations, ranging from a dilute solution ($\text{LiCl·131H}_2\text{O}$, 0.424 m, i.e., 0.424 moles of LiCl per 1 kg of $\text{H}_2\text{O}$) to saturation ($\text{LiCl·2.43H}_2\text{O}$, 22.8 m). The samples were mixtures of commercially available LiCl and purified and ion exchanged $\text{H}_2\text{O}$. The samples were prepared by first dissolving LiCl into $\text{H}_2\text{O}$ until full saturation was achieved, then the samples with lower concentrations were obtained by diluting the saturated sample. Due to the sample preparation technique, the nominal concentrations are not known precisely enough for proper data analysis. The concentrations are, however, given to a good accuracy by the data analysis procedure.⁴⁹ The experimentally determined different sample concentrations (see the last two paragraphs of this section for details), are shown in Table III. Furthermore, Compton profiles of liquid $\text{H}_2\text{O}$ and polycrystalline LiCl were acquired for data analysis. The solutions were confined in a 10-mm-thick sample cell with kapton windows and the cell was inserted in a vacuum chamber to minimize the background. All spectra were acquired at room temperature.

The data processing consisted of subtraction of Compton scattering from the empty cell as well as energy-dependent corrections for the relativistic Compton cross section⁵⁰ and efficiency of the analyzer and detection system. Furthermore, the data were corrected for absorption in the sample and in the path of the radiation. Multiple scattering was studied both by simulations⁵¹,⁵² and experimentally by acquiring spectra from liquid $\text{H}_2\text{O}$ and polycrystalline LiCl confined in 5-, 10- and 15-mm-thick sample cells. The amount of multiple scattering was estimated to be approximately 15% of the signal for both $\text{H}_2\text{O}$ and LiCl, since thick samples were used. Nevertheless, the multiple scattering correction of the experimental spectra turned out to have a negligible effect on the final experimental difference data compared to the experimental inaccuracy.

Upon varying the concentration, a large modification of the Compton profile of aqueous LiCl is induced by the change in the relative amount of ions compared to water molecules. This trivial effect is of no interest to us, thus the most critical part of the data refining procedure is to subtract it. We define the quantity of interest, the Compton profile difference $\Delta J_x(q)$, as
$$\Delta J_x(q)=J_x(q)-xJ_{\text{H}_2\text{O}}(q)-(1-x)J_{\text{LiCl}}(q).\tag{5}$$

Here $J_{\text{H}_2\text{O}}(q)$, $J_{\text{LiCl}}(q)$ and $J_x(q)$ are the Compton profiles of liquid $\text{H}_2\text{O}$ as well as polycrystalline and aqueous LiCl, respectively, and $x$ denotes the mole fraction of water. The fractions of liquid $\text{H}_2\text{O}$ and polycrystalline LiCl Compton profiles are determined by fitting the tails of the Compton profiles, assuming the far reaching core-electron profiles are unaltered by hydration. Thus only the background due to scattering from the empty cell was explicitly subtracted, while the possible remaining background is corrected self-consistently by subtracting the Compton profiles of liquid $\text{H}_2\text{O}$ and polycrystalline LiCl.

Possible sources of error in the data analysis are the moderate statistical accuracy and using only a limited range of the scattered spectrum (sampled between $q=\pm 10$ a.u.) in the fitting. This problem would be circumvented by using a multi-element solid-state detector (SSD), as done in our previous study on liquid water,³³ which would provide both excellent statistical accuracy and spectra including the Compton profile, the quasielastic line and the Cl K edge. Nevertheless, the experimental profile differences reported here are in concord with previous test measurements using a different experimental setup with such a multi-element SSD.⁴⁹

## IV. RESULTS AND DISCUSSION

### A. General considerations

Figure 3 shows the experimental Compton profile difference according to Eq. (5), as a function of concentration. There is a striking similarity, within the experimental accuracy, between the profile differences at different concentrations, albeit the amplitude is concentration dependent. The spectral shape is the same for all the concentrations, with minima at $q$=0 a.u. and maxima at $q\sim 1.3$ a.u. The strength of the signal as a function of concentration is shown in the inset as the area of the absolute profile difference. Clearly, the features in the Compton profile difference behave nontrivially with concentration. We emphasize that the effect in Fig. 3 is solely due to the changes in the local coordination around the ions and water molecules.

A qualitative explanation of the signal can be given in terms of energy, since the Compton profile is connected to the radial momentum distribution of the electronic system. The expectation value of the electronic kinetic energy $\langle T\rangle$ for isotropic systems is given by³⁵
$$\langle T\rangle=\frac{3}{m}\int_{0}^{\infty} q^2 J(q)dq,\tag{6}$$
where $m$ is the electron mass. Thus the expectation value of the kinetic energy of the electrons is observed to increase as a function of concentration, the signal being in the order of 1 eV. This is of the same order of magnitude as the enthalpy of solvation, $H_{\text{solv}}$=-0.38 eV/ion pair.⁵³ However, the ex-

![](./images/812117110258925569_3.jpg)

FIG. 3. (Color online) Experimental Compton profile differ- ences of aqueous LiCl, according to Eq. (5), as a function of con- centration. Linear combinations of $H_{2}O$ and polycrystalline LiCl profiles are used as reference. The spectra are offset vertically for clarity. The inset shows the areas of the absolute profile differences (filled circles, in % of electron) and a guide for the eye (solid line).

perimental inaccuracy, most strongly manifested at high mo- menta due to the $q^{2}$ weighting, is too large for extraction of quantitative numbers for the change in kinetic energy. It is tempting to apply the virial theorem, stating the relation be- tween total and kinetic energy of the system as $E=-\langle T\rangle$ . Thus the experimental profile differences would be a mani- festation of a total energy decrease upon crystal breaking and ion hydration. It should be noted, however, that whereas Eq. (6) holds for the electronic part, the virial theorem also in- cludes the thermal motion of the nuclei. Since relatively small profile differences are considered, the contribution of the nuclei can be significant. Therefore the virial theorem should be applied with caution.

In the following we turn our attention to the model cluster computations. Our strategy is to compare the relative sizes of the different interactions (breaking up the LiCl crystal as well as the ion-ion and ion-water interactions) and correlate these to the experimental findings.

### B. Elementary bonding effects
In Fig. 4 we estimate the effect on the Compton profile upon breaking up the LiCl crystal into free $Li^{+}$ and $Cl^{-}$ ions.

![](./images/812117110258925569_4.jpg)

FIG. 4. The influence on the Compton profile of polycrystalline LiCl upon breaking the crystal, shown as a function of $(LiCl)_{N}$ cluster size. The signal is normalized to the Compton profile of one ion pair.

This is presented for isolated ions from which the Compton profiles of polycrystalline $(LiCl)_{N}$ clusters $(R_{LiCl}=2.56\mathring{A})$ are subtracted, i.e., the plotted quantity corresponds to $-J_{bond}(q)$. It should be noted that the average ionic bond contribution determined from the cluster simulation is further rescaled to the number of ionic bonds in the crystal (six per ion pair) and normalized to one ion pair. Although the am- plitude of the bond oscillation is not quite converged for the case $N=48$ due to the finite cluster size, the oscillatory signal relevant to ionic bonding in the LiCl crystal can be recog- nized.

The signal in Fig. 4 for $N=48$ thus approximates the ef- fect in the Compton profile difference of Eq. (5) when the LiCl crystal breaks up. Comparison of this feature to Fig. 3 reveals, however, that it is of the opposite sign compared to the experimentally observed total effect. Thus the contribu- tion to the Compton profile of the hydration shells and a possible rearrangement of the ions $^{12}$ has to both cancel the feature of Fig. 4 and give rise to the observed profile differ- ences of Fig. 3.

In Fig. 5 the contribution of bonding to the Compton pro- file of pairs of ions as well as pairs of ions and water mol- ecules is shown as a function of the ion-ion and ion-oxygen distance, respectively. The distances are chosen to span the typical ion-ion and ion-oxygen distances of interest in aque- ous $LiCl^{1,2,12}$ Already from this simplistic simulation, the essential features can be recognized. In particular, we ob- serve an oscillating signal which can be interpreted as arising from the exchange repulsion. $^{32}$ The signal changes system atically upon shortening the ion-ion and ion-oxygen dis- tances. This leads to a broadening of the Compton profile, reflecting the sensitivity of the technique to bond lengths through the BOP. $^{34}$ The large impact of the distances on the bond oscillation indicates the importance of using realistic bond-length distribution functions, as in our previous study on the temperature-dependent H-bond geometry in liquid water. $^{33}$

The bond oscillation is observed to be strongest for the bare ion pairs [Fig. 5(c)]. It should be noted, though, that the

![](./images/812117110258925569_5.jpg)

FIG. 5. (a) Differences of simulated Compton profiles of lithium ions and water molecules as a function of ion-oxygen distance. The reference profile consists of a free ion and a water monomer. (b) As (a), except for chloride ions and water molecules. (c) As (a), except for lithium and chloride ions.

ion pairs in the solution are not free, but rather their profiles are affected by the interaction of the ions with their hydration shells. Furthermore, by comparison to Fig. 4, the contribution of pairwise ion bonding to the Compton profile differs significantly from the larger $(LiCl)_N$ clusters. Concerning ion-water interactions, the interaction between chloride ions and water molecules is observed more strongly in the Compton profile compared to the interaction between lithium ions and water molecules [Figs. 5(a) and 5(b)]. A possible explanation for the larger signal is given by the larger overlap of the chloride ion and the water molecule wave functions due to the larger ionic radius of the chloride anion compared to the lithium cation.

### C. Ion hydration

The influence of the hydration shells is presented in Figs. 6 and 7 for chloride (models 1A and 1B) and lithium ions (models 2A and 2B), respectively. The most striking aspect is the difference between models 1A and 1B (2A and 2B) of Fig. 6 (Fig. 7), the difference being due to different ion-oxygen distances in the models. For models 1A and 2A, representing the approximate lower limit for the ion-oxygen distances, the profile differences are *negative* at $J(0)$ with maxima at $q\sim1.0$ a.u. In comparison, the profile differences are *positive* at $J(0)$ for models 1B and 2B, representing the approximate upper limit of the ion-oxygen distances. This is explained by bond elongation which systematically alters the amplitudes at the extrema and gradually changes the sign of the profile difference. Interestingly, only models 1A and 2A show the desired behavior [*negative* at $J(0)$] with respect to the experimental data. This implies the necessity of strongly bound ion hydration shells to explain our experimental findings.

![](./images/812117110258925569_6.jpg)

FIG. 6. Differences of simulated Compton profiles of chloride ions plus hydration shells as a function of hydration number for two different models 1A and 1B. The reference profiles consist of free ions and water monomers. The insets show the values of the Compton profile differences at the extrema of $q\sim0.5-1$ a.u. as a function of the hydration number.

It is worth noting that even with all the coordinating water molecules at a relatively large distance of $R_{OX}^{\text{long}}=8.0$ Å (X =Li,Cl), i.e., $n=0$, we observe a residual effect in the Compton profile difference. This is in contrast to the reported results on water and mixed water-neon clusters.³² However, the residual signal, which is most strongly observed for the chloride ions, is mainly concentrated at low momentum values and does not affect the results of the present study.

A prominent feature observed in Fig. 6 is the change in the Compton profile upon bringing water molecules to the hydration shell of the chloride ion. For $n\geqslant1$, oscillations with distinct extrema are observed. Furthermore, the magni-

![](./images/812117110258925569_7.jpg)

FIG. 7. As Fig. 6, except for lithium ions and models 2A and 2B.

tude of the oscillations depends linearly on the hydration number, as shown in the inset as the value of $J_{\text{bond}}(q_{\text{max}})$ [$J_{\text{bond}}(q_{\text{min}})$] for model 1A (1B). Here $q_{\text{max}}$ ($q_{\text{min}}$) denotes the momentum position of the first maximum (minimum) around $q\sim0.5-1$ a.u. of model 1A (1B). It should be noted that a similar effect was observed earlier for the Compton profiles of water and mixed water-neon clusters. $^{32}$ A qualitative explanation is given by the BOP; $^{34}$ as the $n$ water molecules in the hydration shell are all at the same distance from the chloride ion, they give rise to isoamplitude- and frequency oscillations in the momentum density along the direction of the bond. Our simulations indicate that a similar buildup of the oscillations is expected for all the chloride-oxygen distances of interest.

An analogous buildup of the bond oscillations is also expected for hydrated lithium ions. This is not the case, however, as seen in Fig. 7, neither concerning the position nor the amplitude of the extrema. Our simulations indicate that the nonlinearity in the values of the extrema could be induced by the (repulsive) interactions between the water molecules in the hydration shell, the interatomic distance being $R_{\text{OO}}\approx3.3$ $\mathring{\text{A}}$ ($R_{\text{OO}}\approx4.1$ $\mathring{\text{A}}$) in model 2A (2B). Nevertheless, as for water and mixed water-neon clusters, $^{32}$ the effect of hydration number still resembles a buildup of the bond oscillations observed in the Compton profiles, as long as the next-nearest-neighbor interactions can be neglected.

![](./images/812117110258925569_8.jpg)

FIG. 8. Differences of simulated Compton profiles of $\text{Li}^{+}\text{Cl}^{-}(\text{H}_{2}\text{O})_{n}$, $n{=}8$-$10$, for three different models 3A, 3B and 3C. The reference profiles consists of free ions and water monomers.

### D. Ion pairing
Next we turn our attention to ion pairing in aqueous LiCl, in order to shed some light on the concentration-induced changes in the Compton profiles of strong solutions. This question is expected to be relevant at the high concentrations of the present study, although a recent reverse Monte Carlo study showed no signs of ion pairing. $^{9}$ The results are presented in Fig. 8 for the three different models 3A, 3B and 3C. A clear difference in the bonding-induced changes on the Compton profile is observed for the different models, albeit the magnitudes of the induced changes are roughly model independent. Since the Compton profile differences in Fig. 8 include the effects of hydration shells, the overall effect is dominated by the signal related to chloride hydration.

The effect of ion pairing is revealed by the comparison between the different $\text{Li}^{+}\text{Cl}^{-}(\text{H}_{2}\text{O})_{n}$ clusters. Sharing one water molecule in the hydration shell ($n{=}9$, SSIP-B) induces no appreciable change in the signal related to bonding, as compared to having two complete hydration shells ($n{=}10$, SSIP-A). However, upon removing the water molecule shared by the ions, thus allowing direct contact between the ions ($n{=}8$, CIP), a substantial change in the Compton profile difference is induced. This demonstrates that transitions from

SSIP to CIP structures are in principle observable by Comp- ton scattering. By comparison to Fig. 5 this change is, how- ever, smaller than the one induced by bonding two free ions. Moreover, a simple addition of signals (Figs. 6 and 7) shows that the possible effect of ion pairing induces a weaker signal compared to the effect of hydration.

The difference between the Compton profiles of SSIP and CIP structures is found to be due to both ion-ion interactions and reduction of the hydration number, including the break- ing of the H bond between the chloride ion and the water molecule. Interestingly, only model 3A is qualitatively in ac- cordance with both position and sign of the experimental bond oscillations. This shows that ion pairing can, in prin- ciple, enhance the oscillatory signal as observed in the present experimental data. However, the changes in the pro- files induced by the SSIP to CIP transitions are strongly de- pendent on the hydration shell structures. Therefore no de- finitive conclusions on these transitions can be drawn regarding aqueous LiCl at strong concentrations.

### E. Qualitative interpretation
Finally, we make a qualitative interpretation of the experi- mental data. By comparing signal strengths of Figs. 4, 6, and7, the observed changes in the experimental Compton pro- files of Fig. 3 induced by ion hydration can be explained by the forming of hydration shells. However, this necessarily requires that the average Compton profile differences of the hydration shells are negative at $J(0)$, as models $1 ~A$ and $2 ~A$ of Figs. 6 and 7. Thus we obtain upper limits for the ion-oxygen bond length distributions in these models; in aqueous LiClthe ions must be centered at approximately $R_{OCl} \leqslant 3.15 \AA$  and $R_{OLi} \leqslant 2.10 \AA$ . Whereas this is in very good agreement with previous studies on lithium ions, it provides a much stronger restriction on the (less distinct $^{12,13,16,17}$ ) hydrationshells of chloride ions. $^{1,2}$

It should be noted that the possible rearrangement of the H-bonded water molecule network, specifically the possible change in the strength of the $H$ bonds, is neglected in this study. This can be motivated by a neutron diffraction study, in which no difference between either $H-H$ or $O-H$ partial radial pair correlation functions of pure water and a dilute solution $(1 ~m)$ was observed. $^{6}$ It is interesting, though, that a possible weakening or breaking of the $H$ bonds in the water network induces a signal in the Compton profile of opposite sign compared to the experimental findings of Fig. $3.^{32}$ This provides further support for the strongly bound ion hydration shells. Therefore, when extracting quantitative information from Compton scattering studies this effect should be incor- porated, preferably using local structures derived from ab initio MD simulations.

It is clear that the structural changes expected in liquid water upon ion hydration are too complex to be completely incorporated in model cluster simulations. Moreover, the contributions in the Compton profile from the different struc- tural properties might be difficult to distinguish from each other. For example, changing the hydration number and the ion-oxygen distance produces (partly) overlapping features in the profile. Thus a natural step in the future will be the incorporation of snapshot structures derived from ab initio MD simulations in our Compton profile computations. How- ever, the present approach provides qualitative trends on ion hydration, which should give guidelines for future studies.

### V. CONCLUSIONS
We have conducted a high-resolution Compton scattering study on aqueous $LiCl$ as a function of concentration. Upon increasing the concentration, a systematic increase of the electronic kinetic energy is observed in the experimental Compton profile, indicating an average strengthening of the bonding in the system. The observed systematic changes in the Compton profiles are analyzed by simulations based on model clusters, on the level of gradient-corrected DFT. We find the observed change to be related to the strength of the bonding between the ions themselves as well as ions and water molecules in the system, thus reflecting changes in the local structure of the hydration shells.

The oscillating Compton profile difference is found to de- pend predominantly on the ion-ion and ion-oxygen distances, in concord with the BOP. $^{34}$ Thus Compton scattering pro vides information on the different bond-length distributions in the system. Furthermore, the signal is found to be linearly dependent on hydration number for the ion-oxygen distances relevant to chloride hydration.

Most importantly, the experimentally observed Compton profile difference can be interpreted as the forming of hydra- tion shells, provided that within the studied models the ion- oxygen bond-length distributions are centered at distances of approximately $R_{OCl} \leqslant 3.15 \AA$ and $R_{OLi} \leqslant 2.10 \AA$ .

Concerning our model for ion pairing, we find Compton scattering to be sensitive to possible transitions from SSIP to CIP structures. This signal is found to be due to ion-ion interactions and reduction of the hydration number, including the breaking of the $H$ bond between the chloride ion and the water molecule. However, since the signal due to the SSIP to CIP transition depends strongly on the individual model clus- ter structures, no quantitative conclusions about the local structure of concentrated solutions can be drawn from the present model cluster simulations.

In this study we employed simplified models in order to specifically study which geometrical quantities related to ion hydration affect the Compton profile. Since the Compton profile is sensitive to the local structure, proper bond-length distributions are of major importance when extracting quan- titative information by Compton scattering. Therefore, we propose Compton scattering to be used as a critical test of snapshot structures or bond-length distributions derived from classical and ab initio MD simulations.

### ACKNOWLEDGMENTS
We would like to thank Lars G. M. Pettersson for invalu- able discussions. This work was supported by the Academy of Finland (Contract No. 201291/205967) and the Research Funds of the University of Helsinki. The experiment was performed with the approval of the Japan Synchrotron Ra- diation Research Institute (JASRI), SPring-8 Proposal No.2004A0174-ND3a-np.

ION HYDRATION STUDIED BY X-RAY COMPTON SCATTERING
PHYSICAL REVIEW B 73, 024208 (2006)

*Electronic address: kim.nygard@helsinki.fi

$^{1}$Y. Marcus, Chem. Rev. (Washington, D.C.) 88, 1475 (1988).

$^{2}$H. Ohtaki and T. Radnai, Chem. Rev. (Washington, D.C.) 93, 1157 (1993).

$^{3}$A. H. Narten, F. Vaslow, and H. A. Levy, J. Chem. Phys. 11, 5017 (1973).

$^{4}$S. Cummings, J. E. Enderby, G. W. Neilson, J. R. Newsome, R. A. Howe, W. S. Howells, and A. K. Soper, Nature (London) 287, 714 (1980).

$^{5}$A. P. Copestake, G. W. Neilson, and J. E. Enderby, J. Phys. C 18, 4211 (1985).

$^{6}$R. H. Tromp, G. W. Neilson, and A. K. Soper, J. Chem. Phys. 96, 8460 (1992).

$^{7}$S. Ansell and G. W. Neilson, J. Chem. Phys. 112, 3942 (2000).

$^{8}$I. Howell and G. W. Neilson, J. Phys.: Condens. Matter 8, 4455 (1996).

$^{9}$I. Harsányi and L. Pusztai, J. Chem. Phys. 122, 124512 (2005).

$^{10}$M. Kotbi and H. Xu, Mol. Phys. 94, 373 (1998).

$^{11}$A. V. Egorov, A. V. Komolkin, and V. I. Chizhik, J. Mol. Liq. 89, 47 (2000).

$^{12}$L. Degréve and F. M. Mazzè, Mol. Phys. 101, 1443 (2003).

$^{13}$A. Tongraar and B. M. Rode, Phys. Chem. Chem. Phys. 5, 357 (2003).

$^{14}$T. Asada and K. Nishimoto, Chem. Phys. Lett. 232, 518 (1995).

$^{15}$K. Hermansson and M. Wojcik, J. Phys. Chem. B 102, 6089 (1998).

$^{16}$A. P. Lyubartsev, K. Laasonen, and A. Laaksonen, J. Chem. Phys. 114, 3120 (2001).

$^{17}$J. M. Heuft and E. J. Meijer, J. Chem. Phys. 119, 11788 (2003).

$^{18}$X. Li and Z.-Z. Yang, J. Chem. Phys. 122, 084514 (2005).

$^{19}$M. Patra and M. Karttunen, J. Comput. Chem. 25, 678 (2004).

$^{20}$M. J. Cooper, Rep. Prog. Phys. 48, 415 (1985).

$^{21}$M. J. Cooper, P. E. Mijnarends, N. Shiotani, N. Sakai, and A. Bansil, *X-Ray Compton Scattering* (Oxford University Press, Oxford, 2004).

$^{22}$C. Blaas, J. Redinger, S. Manninen, V. Honkimäki, K. Hämäläinen, and P. Suortti, Phys. Rev. Lett. 75, 1984 (1995).

$^{23}$Y. Sakurai, Y. Tanaka, A. Bansil, S. Kaprzyk, A. T. Stewart, Y. Nagashima, T. Hyodo, S. Nanao, H. Kawata, and N. Shiotani, Phys. Rev. Lett. 74, 2252 (1995).

$^{24}$K. Nygård, S. Huotari, K. Hämäläinen, S. Manninen, T. Buslaps, N. H. Babu, M. Kambara, and D. A. Cardwell, Phys. Rev. B 69, 020501(R) (2004).

$^{25}$T. Paakkari, Chem. Phys. Lett. 55, 160 (1978).

$^{26}$A. Seth and E. J. Baerends, Chem. Phys. Lett. 64, 165 (1979).

$^{27}$T. K. Ghanty, V. N. Staroverov, P. R. Koren, and E. R. Davidson, J. Am. Chem. Soc. 122, 1210 (2000).

$^{28}$E. D. Isaacs, A. Shukla, P. M. Platzman, D. R. Hamann, B. Barbiellini, and C. A. Tulk, Phys. Rev. Lett. 82, 600 (1999).

$^{29}$A. H. Romero, P. L. Silvestrelli, and M. Parrinello, J. Chem. Phys. 115, 115 (2001).

$^{30}$S. Ragot, J.-M. Gillet, and P. J. Becker, Phys. Rev. B 65, 235115 (2002).

$^{31}$B. Barbiellini and A. Shukla, Phys. Rev. B 66, 235101 (2002).

$^{32}$M. Hakala, S. Huotari, K. Hämäläinen, S. Manninen, P. Wernet, A. Nilsson, and L. G. M. Pettersson, Phys. Rev. B 70, 125413 (2004).

$^{33}$M. Hakala, K. Nygård, S. Manninen, S. Huotari, T. Buslaps, A. Nilsson, L. G. M. Pettersson, and K. Hämäläinen (unpublished).

$^{34}$I. R. Epstein and A. C. Tanner, in *Compton Scattering*, edited by B. G. Williams (McGraw–Hill, London, 1977), Chap. 7, p. 209.

$^{35}$W. Schülke, in *X-Ray Compton Scattering*, edited by M. J. Cooper, P. E. Mijnarends, N. Shiotani, N. Sakai, and A. Bansil (Oxford University Press, Oxford, 2004), Chap. 2, p. 22.

$^{36}$P. Eisenberger and P. M. Platzman, Phys. Rev. A 2, 415 (1970).

$^{37}$P. Hohenberg and W. Kohn, Phys. Rev. 136, B864 (1964).

$^{38}$W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 (1965).

$^{39}$P. Duffy, D. P. Chong, M. E. Casida, and D. R. Salahub, Phys. Rev. A 50, 4707 (1994).

$^{40}$K. Hermann, L. G. M. Pettersson, M. E. Casida, C. Daul, A. Goursot, A. Koester, E. P. A. St-Amant, and D. R. Salahub, *StoBe-deMon version 1.0* (2002), contributing authors: V. Carravetta, H. Duarte, N. Godbout, J. Guan, C. Jamorski, M. Leboeuf, V. Malkin, O. Malkina, M. Nyberg, L. Pedocchi, F. Sim, L. Triguero, and A. Vela, StoBe Software.

$^{41}$B. Hammer, L. B. Hansen, and J. K. Norskov, Phys. Rev. B 59, 7413 (1999).

$^{42}$J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1999).

$^{43}$S. Huzinaga, J. Chem. Phys. 42, 1293 (1965).

$^{44}$K. Ichikawa, Y. Kameda, T. Yamaguchi, H. Wakita, and M. Misawa, Mol. Phys. 73, 79 (1991).

$^{45}$K. Modig, B. G. Pfrommer, and B. Halle, Phys. Rev. Lett. 90, 075502 (2003).

$^{46}$Y. Sakurai, J. Synchrotron Radiat. 5, 208 (1998).

$^{47}$N. Hiraoka, M. Itou, T. Ohata, M. Mizumaki, Y. Sakurai, and N. Sakai, J. Synchrotron Radiat. 8, 26 (2001).

$^{48}$Y. Sakurai and M. Itou, J. Phys. Chem. Solids 65, 2061 (2004).

$^{49}$K. Nygård (unpublished).

$^{50}$P. Holm, Phys. Rev. A 37, 3706 (1988).

$^{51}$N. Sakai, J. Phys. Soc. Jpn. 56, 2477 (1987).

$^{52}$Y. Kakutani and N. Sakai, J. Phys. Chem. Solids 65, 2071 (2004).

$^{53}$D. R. Linde, *CRC Handbook of Chemistry and Physics*, 82nd ed. (CRC, Boca Raton, FL, 2001).

024208-9