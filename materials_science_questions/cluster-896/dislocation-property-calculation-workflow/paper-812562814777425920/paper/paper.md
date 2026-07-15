![](./images/812562814777425920_1.jpg)

Computer Physics Communications 259 (2021) 107573

Contents lists available at ScienceDirect

Computer Physics Communications

journal homepage: www.elsevier.com/locate/cpc

![](./images/812562814777425920_2.jpg)

# Materials analysis applying thermodynamic (MAAT) software:
A friendly and free tool to analyze the formation of solid solutions,
amorphous phases and intermetallic compounds $^{☆,☆☆}$

![](./images/812562814777425920_3.jpg)

C. Aguilar $^{a,*}$, P. Martin $^{b}$, E. Pio $^{a}$, C. Salvo $^{c}$, G.O. Neves $^{d}$

$^{a}$ Departamento de Ingeniería Metalúrgica y de Materiales, Universidad Técnica Federico Santa María, Valparaíso, Chile
$^{b}$ Department of Materials Science and Engineering, Universitat Politecnica de Catalunya-Barcelona Tech, Barcelona, España, Spain
$^{c}$ Departamento de Ingeniería Mecánica, Universidad del Bío-Bío, Concepción, Chile
$^{d}$ Universidade Federal de Santa Catarina, Laboratorio de Materiais, Campus Trindade, Florianopolis, SC, 88040-900, Brazil

---

## ARTICLE INFO

**Article history:**
Received 9 April 2020
Received in revised form 6 August 2020
Accepted 20 August 2020
Available online 24 September 2020

**Keywords:**
Gibbs free energy
Thermodynamic modeling
Miedema's models
Crystalline defects
Amorphous phase
Solid solution

---

## ABSTRACT

Experimental thermodynamic measurements in multicomponent systems exhibit high complexity. Theoretical calculations by extrapolation of constitutive binary systems are an excellent tool to estimate the thermodynamic properties in ternary or quaternary systems. In this context, the Miedema and Bakker semi-empirical models are good to estimate the enthalpy of mixing or formation. This work presents a new software, MAAT (Materials Analysis Applying Thermodynamics), designed to calculate selected thermodynamic properties of binary and ternary systems. The MAAT is a free software that can be download from www.rpm.usm.cl. The MAAT software is a platform, written in MATLAB, which runs in 32/64 bits Windows systems. The main characteristics of the software are: i) calculation and plotting Gibbs free energy of mixing curves of random solid solutions, amorphous and intermetallic compounds, ii) calculation and plotting the activity of components in solid solutions, and iii) analysis of the effect of additional terms over the Gibbs free energy of mixing of random solid solutions, such as centrifugal field, grain size and dislocations. In this work, the thermodynamic calculations performed with MAAT are compared with experimental data in four cases: formation of solid solution (Cu-Mo-Cr system), formation of amorphous phase (Ti-Ta-Sn system), formation of intermetallic compound (Cu-Nb-Co system) and effect of centrifugal field on formation of solid solution (Cu-Cr system). For all systems analyzed, the calculations made using MAAT gave results that are comparable with experimental data.

---

## Program summary
**Program title:** MAAT
**CPC Library link to program files:** http://dx.doi.org/10.17632/56wydw5wf5.1
**Developer's repository link:** www.rpm.usm.cl
**Licensing provisions:** Creative Commons Zero (CC0)
**Programming language:** MATLAB
**Nature of problem:** Although there is a variety of codes and graphic interfaces to compute the Gibbs free energy of binary and ternary systems, most of them have strong restrictions, such as the knowledge of specific programming languages, complex routines of computation, closed source codes, or are paid softwares/databases.
**Solution method:** MAAT is an user-friendly free software written in MATLAB that computes the Gibbs free energy of binary and ternary systems, applied to solid solutions, amorphous structures and intermetallic compounds, based on Miedema's model for the calculation of the enthalpy of formation. The software integrates by default the required data of 58 elements to compute the thermodynamical terms.

---

$^{☆}$ The review of this paper was arranged by Prof. Stephan Fritzsche.
$^{☆☆}$ This paper and its associated computer program are available via the Computer Physics Communication homepage on ScienceDirect (http://www.sciencedirect.com/science/journal/00104655).
$^{*}$ Correspondence to: Avenida España 1680, Universidad Técnica Federico Santa María, Valparaíso, Chile.
E-mail address: claudio.aguilar@usm.cl (C. Aguilar).

https://doi.org/10.1016/j.cpc.2020.107573
0010-4655/© 2020 Elsevier B.V. All rights reserved.

Additional comments including restrictions and unusual features: MAAT allows users to compute the effect of additional energy sources - grain size effect, dislocation effect and centrifugal field effect - in order to study how these affect the Gibbs free energy of a solid solution.
All the parameters of the database have been calculated at 298 K and the input temperature is exclusively considered for the calculation of the entropic term. It is recommended to do calculations at or near this temperature.

© 2020 Elsevier B.V. All rights reserved.

## 1. Introduction

Metals are intensively utilized in diverse scientific, engineering and domestic uses due its intrinsic properties (mechanical, physical, thermal, chemical and electrical). Nowadays, scientific and technological advances need high performance materials with a good balance in their physical, mechanical and chemical properties. In this context, engineers and materials scientists have focused their attention on the development of advanced materials with tailored properties for demanding applications by controlling their crystal structure and microstructure [1]. These structural characteristics could be better controlled by using non-equilibrium processes [2], such as; rapid solidification processing (RSP), plasma and laser processing, mechanical alloying (MA), spray forming (SF), ion-mixing, physical and chemical vapor deposition (PVD and CVP) and thermal plasma processing (TPP) [3]. The effectivity of the non-equilibrium processes to synthesize advanced materials are evaluated by measuring the maximum energy that could be stored in excess compared with equilibrium structure (i.e. the achieved departure from equilibrium). Some energy values of departure from equilibrium are (in kJ mol⁻¹): solid state quench (16), rapid solidification (24), mechanical alloying (30), mechanical cold work (1), irradiation/ion implantation (30) and condensation from vapor (160) [4].

Mechanical alloying (MA) is a powder processing technique applied to synthesize nanocrystalline powders, extended solid solution, high entropy alloys, oxide-dispersion-strengthened alloys and amorphous phases [5–7]. MA has been defined as "dry, solid-state powder processing technique (a liquid medium can also be used sometimes during milling operations) which involves repeated welding, fracturing and re-welding of powder particles in a high-energy ball mill" [2]. During MA, high kinetic energy is transferred from the milling media to the powders producing severe plastic deformation and increasing the crystalline defects density (mainly crystallite boundaries and dislocations) [8]. The higher crystalline defects density changes the thermodynamic properties of the material, such as the Gibbs free energy, activities and solubility. In this context, there are few studies about the effect of crystalline defects produced during MA on the thermodynamic properties. Pelegrina et al. [9] analyzed the influence of particle size on crystalline/amorphous relative phase stability of the Cu–Zn system processed by MA. They reported that the minimum particle size calculated by considering the surface effect was in agreement with the experimental results assessed by high-resolution transmission electron microscopy (HR-TEM) and X-ray diffraction (XRD) patterns analysis. Bera et al. [10] reported that when the grain size decreases, the Gibbs free energy values increase and influence the stability of the phases in the pseudo-binary (Ti–Zr)(Fe–Cr)2 and pseudo-ternary (Ti–Zr)(Fe–Cr)2–H systems. Aguilar et al. [8,11,12] studied the effect of some crystalline defects (crystallite boundaries and dislocations) on the Gibbs free energy of mixing in Cu-based alloys. At 50 h of milling, the Gibbs free energy values increased up to around 6.5 kJ mol⁻¹ from surface energy (crystallite size) and 1.6 kJ mol⁻¹ from elastic deformation (dislocation) in a Cu–8%Cr (wt. %). For Cu–15%Cr–15%Mo (wt. %) the Gibbs free energy value storage was around 20 kJ mol⁻¹ at 120 h of milling.

Current attempts to estimate the Gibbs free energy values on multicomponent alloy phases use different ways, such as analytical and/or numerical methods. The analytical methods are difficult for multicomponent systems because the mathematics formulism is very complex. On the other hand, in most cases of multicomponent systems it is very difficult to measure thermodynamic properties experimentally. Therefore, to address this problem, theoretical models could be used to perform thermodynamic calculations. The Calculation of Phase Diagrams (CAL-PHAD) [13] technique is used to estimate the phases stability of a great number of systems minimizing the Gibbs free energy from experimental phase equilibrium data. If the experimental information is not available, Miedema's method [14] is a simple method to determine the enthalpy of formation of intermetallic compounds and enthalpy of mixing of solid solutions and amorphous phases [15]. An important aspect of the model for determining enthalpy values is that the electron density changes when two different elements are in contact. The simplicity of the method is that it uses only three parameters: (a) the electronegativity difference ($\Delta \phi$), (b) the electron density discontinuity ($\Delta n_{WS}^{1/3}$) and (c) the R parameter, which considers the additional hybridization contribution when transition and non-transition metals are combined. The values of the parameters mentioned are available in Miedema's work [14].

Miedema's method has been applied in a wide number of binary, ternary and quaternary systems [16–20]. Arzpeyma et al. [21] studied the enthalpy of mixing of 50 binary liquid alloys using Miedema's model, the Engel–Brewer method, the hard-sphere model and Witusiewicz, Sommer, Faber relations, and observed a better agreement between Miedema's model and experimental data. King et al. [22] determined that the estimated formation enthalpy values of single phase high-entropy alloys are close to experimental values reported. Ke-sheng et al. [23] studied the effect of temperature on mechanical alloying of Cu–Zn and Cu–Cr systems and estimated the Gibbs free energy as around 20 and –6.5 kJ mol⁻¹ (equimolar composition), respectively. Ouyang et al. [24] estimated the enthalpies of formation of Al–Cu–Ni–Zr alloys and compared results with experimental data found reasonable agreement in both values. Nagase et al. [25] studied the formation of amorphous phase with crystalline globules in Fe–Cu–Nb–B immiscible alloys through the determination of enthalpy of mixing of binary systems (Nb–B, B–Fe, Fe–Nb, B–Cu, Cu–Nb and Fe–Cu) and Liu et al. [18] determined the formation enthalpy of amorphous Mg–Cu–Ti–Y alloys. Herbst [17] estimated the enthalpy of formation and hydrogen content of quaternary $AB_nC_mH_x$ hydrides and found that results are close to experimental data for a variety of materials, including complex hydrides. Aguilar et al. estimated the enthalpy of mixing of the synthesis of amorphous phase and random solid solution in Cu-based alloys [8] and Ti-based alloys [26]. They found that Midema's model gives reasonable results compared with experimental data. On the other hand, Neves et al. [27] studied the Silicon Carbide disso-ciation in Fe matrix during sintering at 1100 °C. They reported a good agreement between calculations and experiments.

The great majority of the works that use the Miedema's model just report the enthalpy values but not the Gibbs free energy

values. Also, there is no friendly software available to calculate the Gibbs free energy of binary and ternary systems.

This work introduces the use of the MAAT software to calcu- late selected thermodynamic properties of solid solutions, amor- phous phases and intermetallic compounds. The MAAT is a free user-friendly graphical software available at the webpage www. rpm.usm.cl. The experimental data of four systems, which were subjected to high-energy ball milling, are compared with the calculated thermodynamic data by using the MAAT software:

(i) for the analysis of the synthesis of solid solution: the Cu-Mo-Cr ternary system was chosen because it does not exhibit solid solubility in the temperature range between 298 and 398 K. A composition of Cu-7Cr-7Mo (at. %) was chosen because a planetary mill could give the required energy to obtain a random solid solution

(ii) for the analysis of the formation of an amorphous phase: the Ti-Ta-Sn system was chosen because our group has reported previously the formation of an amorphous phase. The composition Ti-13Ta-12Sn (at. %) was used according to Inoue's rules [6,28]

(iii) for the analysis of the formation of intermetallic com- pound: the Cu-Nb-Co system was chosen with Cu-7Nb-7Co (at. %) due to its tendency to form intermetal- lic compounds

(iv) for the analysis of the effect of a centrifugal field on the formation of solid solution: the Cu-Cr system was studied. The composition Cu-50Cr (wt. %) was used according to previous results of our group [29].

## 2. Thermodynamic theory

### 2.1. Gibbs free energy of mixing, $\Delta G^{m}$

The Gibbs free energy of mixing of random solid solution is calculated by Eq. (1), where; T is the temperature, $\Delta S^{m}$ is the entropy of mixing, $\Delta H^{m}$ is the enthalpy of mixing. This equation does not consider the influence of the surface, crystalline defects or external potential fields. The entropy term is calculated using the expression of the configurational entropy of a random solid solution by Eq. (2), where $x_{i}$ is the molar fraction of the species i and R is the universal gas constant. Also the ideal Gibbs free energy of mixing can be computed by Eq. (3), where $\Delta S^{m,id}$ is the ideal entropy of mixing or configurational entropy.

$$
\Delta \mathrm{G}^{\mathrm{m}}=\Delta \mathrm{H}^{\mathrm{m}}-\mathrm{T} \Delta \mathrm{S}^{\mathrm{m}} \tag{1}
$$

$$
\Delta \mathrm{S}^{\mathrm{m}}=-\mathrm{R} \sum_{\mathrm{i}=1}^{\mathrm{n}} \mathrm{x}_{\mathrm{i}} \mathrm{lnx}_{\mathrm{i}} \tag{2}
$$

$$
\Delta \mathrm{G}^{\mathrm{m}, \mathrm{id}}=-\mathrm{T} \Delta \mathrm{S}^{\mathrm{m}, \mathrm{id}} \tag{3}
$$

The enthalpy of mixing can be computed using Miedema's model [14], which will be discussed in Section 2.2. When plastic defor- mation is applied to metals, crystalline defects are produced, such as dislocations, grain boundaries, stacking fault, twins, and vacan- cies, so the Gibbs free energy increases when crystalline defects increase [26,30]. Other effect that influences the Gibbs free energy is the application of external field on the system, whereby the thermodynamic intensive properties change within the system as a function of the position until a new thermodynamic equilibrium is achieved. Therefore, Gibbs free energy changes when metallic systems are subjected to plastic deformation and/or an external potential field. Thus, Eq. (1) can be modified by adding a term that considers the mentioned effects. This term takes into account the extra energy added to the system, $G^{ad}$, therefore, the modified Gibbs free energy can be obtained using equation remains as:

$$
\Delta \mathrm{G}^{\mathrm{mod}}=\Delta \mathrm{H}^{\mathrm{m}}-\mathrm{T} \Delta \mathrm{S}^{\mathrm{m}}+\mathrm{G}^{\mathrm{ad}} \tag{4}
$$

The $G^{ad}$ term can be estimated as $G^{ad}=G_{gb}^{ad}+G_{dis}^{ad}+G_{ef}^{ad}$, where the terms $G_{gb}^{ad}$, $G_{dis}^{ad}$ and $G_{ef}^{ad}$ correspond to the energies added to the system by grain boundaries, dislocation and external field, respectively. Those terms will be discussed in Section 2.4.

### 2.2. Miedema's model theory

Miedema's model is a powerful tool to estimate the enthalpy values for some metallurgical phenomena, such as; (a) enthalpy of formation of compounds, (b) enthalpy of mixing in random solid solution and (c) enthalpy of formation of amorphous phase. Miedema's model was formulated originally for estimating the enthalpy in binary systems but has been extended to the ternary and quaternary systems [15,24,31,32]. This model is a semi- empirical model [33] in which atoms are considered as "blocks" of the element. If A and B atoms are in contact, the enthalpy is produced at the A-B interface. The enthalpy value is obtained considering the following parameters, (i) the electron density discontinuity $\Delta nWS^{1/3}((n_{WS}^{A})^{1/3}-(n_{WS}^{B})^{1/3}$, (ii) the electroneg- ativity difference $\Delta \phi$ ($\phi_{\mathrm{A}}-\phi_{\mathrm{B}}$) and (iii) an additional parameter R (hybridization contribution) which considers the combination between transition and non-transition elements. The values of these parameters can be found in Miedema's work [14].

The enthalpy of mixing of random solid solution can be ob- tained using Eq. (5), where $\Delta H_{chem}^{m}$ is the chemical enthalpy, $\Delta H_{elast}^{m}$ is the elastic enthalpy related with the elastic mismatch energy between solute atoms and solvent atoms, and $\Delta H_{struct}^{m}$ is the lattice stability enthalpy produced by the difference in va- lence electrons and crystal structure of solvent and solute atoms.

$$
\Delta H^{m}=\Delta H_{chem}^{m}+\Delta H_{elast}^{m}+\Delta H_{struct}^{m} \tag{5}
$$

#### (a) Chemical contribution, $\Delta H_{chem}^{m}$

A model to compute the chemical contribution was proposed by Miedema et al. [14] which is widely used because of its sim- plicity. The $\Delta H_{chem}^{m}$ term depends on some physical parameters given by expression (6), where; $x_{A}$ and $x_{B}$ are the atomic fractions of species A and B, respectively, $V_{A}$ is the molar volumes of A, $V_{B}$ is the molar volumes of B, $n_{ws}$ is the electron density, $\phi^{*}$ is the work function of the constituent elements, P, Q and R' are constants related to the constituent elements and $\mathrm{f}\left(\mathrm{C}^{\mathrm{S}}\right)=\mathrm{C}_{\mathrm{A}}^{\mathrm{S}} \mathrm{C}_{\mathrm{B}}^{\mathrm{S}}$,where $\mathrm{C}_{\mathrm{A}}^{\mathrm{S}}$ and $\mathrm{C}_{\mathrm{B}}^{\mathrm{S}}$ are determined by Eq. (7). Differences between $\Delta \mathrm{H}^{\mathrm{m}}$ val- ues (calculated by Eq. (4)) and experimental measurements have been found in some binary and ternary systems [34]. In order to overcome this, a correction factor of volume S(x) was introduced by Wang et al. [34]. This factor considers the difference of atomic size between solvent atoms and solute atoms, Eq. (7). The M factor varies according to the difference between atomic sizes. This factor is considered equal to 1 for a random solid solution, whereas for the liquid alloy and ordered compounds is equal to 0.5 and 2.0, respectively.

$$
\begin{aligned}
\Delta \mathrm{H}_{\text {chemical }}= & 2 \mathrm{Pf}\left(\mathrm{C}^{\mathrm{S}}\right) \mathrm{S}(\mathrm{x}) \frac{\left(\mathrm{x}_{\mathrm{A}} \mathrm{V}_{\mathrm{A}}^{2 / 3}+\mathrm{x}_{\mathrm{B}} \mathrm{V}_{\mathrm{B}}^{2 / 3}\right)}{\left(\mathrm{n}_{\mathrm{ws}}^{\mathrm{A}}\right)^{-1 / 3}+\left(\mathrm{n}_{\mathrm{ws}}^{\mathrm{B}}\right)^{-1 / 3}} \mathrm{x} \\
& \times\left[-\left(\Delta \phi^{*}\right)^{2}+\mathrm{Q} / \mathrm{P}\left(\Delta \mathrm{n}_{\mathrm{ws}}^{1 / 3}\right)^{2}-\mathrm{R}^{\cdot} / \mathrm{P}\right]
\end{aligned} \tag{6}
$$

$$
\mathrm{C}_{\mathrm{A}}^{\mathrm{S}}=\frac{\mathrm{x}_{\mathrm{A}} \mathrm{V}_{\mathrm{A}}^{2 / 3}}{\mathrm{x}_{\mathrm{A}} \mathrm{V}_{\mathrm{A}}^{2 / 3}+\mathrm{x}_{\mathrm{B}} \mathrm{V}_{\mathrm{B}}^{2 / 3}} \quad \mathrm{C}_{\mathrm{B}}^{\mathrm{S}}=\frac{\mathrm{x}_{\mathrm{B}} \mathrm{V}_{\mathrm{B}}^{2 / 3}}{\mathrm{x}_{\mathrm{A}} \mathrm{V}_{\mathrm{A}}^{2 / 3}+\mathrm{x}_{\mathrm{B}} \mathrm{V}_{\mathrm{B}}^{2 / 3}} \tag{7}
$$

$$
\mathrm{S}(\mathrm{x})=1-\mathrm{M} \frac{\mathrm{x}_{\mathrm{A}} \mathrm{x}_{\mathrm{B}}\left|\mathrm{V}_{\mathrm{A}}-\mathrm{V}_{\mathrm{B}}\right|}{\mathrm{x}_{\mathrm{A}}^{2} \mathrm{V}_{\mathrm{A}}+\mathrm{x}_{\mathrm{B}}^{2} \mathrm{V}_{\mathrm{B}}} \tag{8}
$$

#### (b) Elastic contribution, $\Delta H_{elast}^{m}$

Bakker et al. [35] proposed an expression to estimate the elastic contribution as a function of the elastic energy mismatch,

$\Delta E_{\text{i in j}}$, caused by solute (i) dissolved in solvent (j) Eq. (9). For example, $\Delta E_{\text{A in B}}$ is the elastic energy mismatch caused by the element A dissolved in the element B. $\Delta E_{\text{A in B}}$ and $\Delta E_{\text{B in A}}$ terms are obtained using Eq. (20), where; G is the shear modulus and K the bulk modulus of A or B.

$$\Delta H_{\text{elastic}} = \mathrm{x_A x_B} (\mathrm{x_A} \Delta E_{\text{A in B}} + \mathrm{x_B} \Delta E_{\text{B in A}}) \tag{9}$$

$$\Delta E_{\text{A in B}} = \frac{2\mathrm{K_A G_B} (\mathrm{V_B} - \mathrm{V_A})^2}{3\mathrm{K_A V_B} + 4\mathrm{G_B V_A}} \quad \Delta E_{\text{B in A}} = \frac{2\mathrm{K_B G_A} (\mathrm{V_A} - \mathrm{V_B})^2}{3\mathrm{K_B V_A} + 4\mathrm{G_A V_B}} \tag{10}$$

### (c) Structural contribution, $\Delta H_{struct}^m$
This term could have a minor effect compared with $\Delta H_{chem}^m$ and $\Delta H_{elast}^m$ terms, so in some systems is no considered [36]. The crystal structure of a transition element depends on the number of valence electrons (Z) of the metal. Face-centered cubic or hexagonal closest packed crystal structures are stable for transition metals with valence electron of 3 and 4, respectively. The body-centered cubic crystal structure is stable for metals with valence electron of 5 or 6. The $\Delta H_{struct}^m$ term gives the stability of crystal structure of one phase with the concentration of solute. This term depends on two factors; (a) the change in the slope of the curve of energy of atomic bond as a function of the number of valence electrons and (b) the difference of number of valence electrons of solute and solvent ($Z_A - Z_B$). The $\Delta H_{struct}^m$ term can be estimated by Eq. (11) [37,38], where $\langle z \rangle = \mathrm{c_A Z_A} + \mathrm{c_B Z_B}$ and $E^{\text{struct}}(z)$ is the lattice stability of the crystal structure. $E^{\text{struct}}(\langle z \rangle)$ considers the most negative values of energy of the three crystal structures, face-centered cubic, hexagonal close-packed and body-centered cubic as a function of the number of valence electrons [37,38].

$$\Delta H^{\text{struct}} = E^{\text{struct}}(\langle z \rangle) - c_A E_A^{\text{struct}}(z) - c_B E_B^{\text{struct}}(z) \tag{11}$$

### (d) Enthalpy of formation of an amorphous phase, $\Delta H_{am}^m$
In a great variety of metallurgical processes, such as, severe plastic deformation, mechanical alloying, rapid solidification [28], the crystalline defects density in metallic powders increases. The crystalline defects increase the Gibbs free energy promoting the formation of an amorphous phase. The formation enthalpy of the amorphous state is higher than the crystalline state, because the amorphous is a metastable state [39]. The enthalpy of amorphization ($\Delta H_{am}^m$) is estimated by Eq. (12), where; $\Delta H_{am}^{topo}$ is the topological enthalpy which considers the difference between the crystalline and amorphous states. An amorphous phase has no crystal structure, so elastic ($\Delta H_{elast}^m$) and structural ($\Delta H_{struct}^m$) terms are not considered in calculations. Therefore, $\Delta H_{am}^{topo} = 3.5 \ (\mathrm{x_A T_A^m} + \mathrm{x_B T_B^m})$ [39], where $\mathrm{T^m}$ is the melting temperature of elements A and B, $\mathrm{x_A}$ and $\mathrm{x_B}$ are the atomic fractions of species A and B, respectively.

$$\Delta H_{am}^m = \Delta H_{chem, am}^m + \Delta H_{am}^{topo} \tag{12}$$

### (e) Enthalpy of formation of intermetallic compounds, $\Delta H_{AB}^f$
In opposition to random solid solutions, intermetallic compounds crystallize in a new crystal structure, which accommodates both A and B atoms in fixed positions into the lattice [39]. Thus, both elastic and structural contributions are not considered in the calculation of enthalpy of formation of intermetallic compounds $\Delta H_{AB}^f$. However, the surface contact may be affected by size atomic differences, hence a correction factor is required for the calculation of $\Delta H_{AB}^f$ [40]. Due to the poor fitting between experimental data of $\Delta H_{AB}^f$ and calculated values using the original Miedema's model, several correction factors have been proposed to achieve a better adjustment [34,40-44]. The S(x) factor, Eq. (8), proposed by Wang et al. [34] incorporates the effect of the atomic size difference of constituents on the contact interface, exhibiting good fitting with experimental values in binary alloys. The S(x) term considers the empirical parameter M, which is taken as 2.0 for ordered compounds. Therefore, the enthalpy of formation of intermetallic compounds can be calculated by Eq. (13),

$$\Delta H_{AB}^f = \Delta H_{chem}^m \tag{13}$$

## 2.3. Extended Miedema's model for ternary alloys
Geometrical methods can be used to calculate the thermodynamic properties of ternary systems from information of binary systems. Some works have shown that extension to ternary systems has given acceptable results [26,34,45]. In regard, two ways can be followed; (i) symmetrical models or (ii) asymmetrical models [46]. It is preferable to use asymmetric models because considering the effect of third atom reduce the deviance in calculations compared with experimental data. Some asymmetrical models have been proposed by Hillert [46], Toop [47] and Bonnier [48], and symmetrical models by Kohler [49], Muggianu [50] and Colinet [51]. The equations for the mentioned models are given in Appendix A.

## 2.4. Calculation of the activity
The activity of the species i ($a_i$) can be computed using the method of tangential intercepts when the partial molar Gibbs free values ($\Delta \overline{G}_i^m$) are known. The partial molar Gibbs free energy can be determined using Eq. (14) and the activities values are obtained from $\Delta \overline{G}_i^m$ using Eq. (15).

$$\Delta \overline{G}_i^m = \Delta G^m + x_{1-i} \frac{d \Delta G^m}{d x_i} \tag{14}$$

$$a_i = \exp \left( \frac{\Delta \overline{G}_i}{RT} \right) \tag{15}$$

## 2.5. Energy sources added to the system
### (a) Grain size contribution, $G_{gb}^{ad}$
As mentioned previously, in materials subjected to severe plastic deformation, grain (or crystallite) size is reduced and new grain boundaries or surfaces are created, and consequently an increment in Gibbs free energy is produced. The energy increases as a function of the surface created because of the higher number of unsatisfied atomic bonds. The energy change can be obtained by Eq. (16) [11], where; $\mathrm{Vm_i}$ is the molar volume of the species i, $\gamma_i$ is the surface energy per unit area of the species i, $\iint dA$ is the surface area and $\iiint dV$ is the volume. The expressions for the area (A) and the volume (V) depend principally of the grain shape. The equations for A and V for three different grain shapes are given in Appendix B. From these equations, the $\iint dA / \iiint dV$ ratio value can be obtained. The MAAT has three grain shapes available: spherical, cubic and dodecahedral.

$$G_{gb}^{ad} = \left( \frac{\iint dA}{\iiint dV} \right) \gamma_i (T, x, r) Vm_i \tag{16}$$

The $\gamma$ parameter varies as a function of the temperature (T), composition (x) and curvature of the grain or particle (r). Several expressions have been proposed for the curvature dependence of the surface energy for solid/liquid interface [52-54] but for solid/solid interface the most used expression is given by Eq. (17) [55], where $\gamma_\infty$ is the bulk solid/solid interface energy which is temperature- and composition-dependent (, $d_o$ is the width of the solid/solid interface and d is the diameter of the grains. The $\gamma$(T,x,r) values as a function of $d_0$/d can be obtained from previously works of Jiang and Lu [55], Wang et al. [56] and

Pelegrina et al. [9]. Details of the dependence of the temperature and composition of $\gamma_\infty$ are given by the following works [57-59].

$$
\gamma(T, x, r)=\gamma_{\infty}(T, x)\left(1-\frac{d_{o}}{4 d}\right)
\tag{17}
$$

### (b) Dislocations contribution, $G_{dis}^{ad}$
Crystalline defects (dislocations, stacking fault, twins, vacancies) are created during severe plastic deformation. All of them increase the Gibbs free energy but dislocations have a higher effect due to the larger elastic energy stored. The effect of elastic energy produced by dislocations can be obtained [11] using Eq. (18), where; $\xi_{average}$ is the average dislocation elastic energy per unit length of dislocation lines, Eq. (19) and $\rho$ is the dislocation density. The $\xi_{average}$ considers elastic energies of screw and edge dislocations, Eq. (17) and Eq. (21), respectively, where $\eta$ varies between 0 and 1, G is the shear modulus, b is the Burgers vector, Re is the outer cutoff of dislocation, $r_0$ is the inner cutoff radius and $v$ is Poisson's ratio.

$$
G_{d i s}^{a d}=\xi_{a v e r a g e} \rho \mathrm{Vm}_{i}
\tag{18}
$$

$$
\xi_{\text {average }}=\eta \xi_{\text {screw }}+(1-\eta) \xi_{\text {edge }}
\tag{19}
$$

$$
\xi_{\text {screw }}=\left(\frac{\mathrm{Gb}^{2}}{4 \pi}\right) \ln \left(\frac{\mathrm{Re}}{\mathrm{r}_{0}}\right)
\tag{20}
$$

$$
\xi_{\text {edge }}=\left(\frac{\mathrm{Gb}^{2}}{4 \pi(1-v)}\right) \ln \left(\frac{\mathrm{Re}}{\mathrm{r}_{0}}\right)
\tag{21}
$$

### (c) External field contribution, $G_{ef}^{ad}$
A system reaches the thermodynamic equilibrium when there are no gradients of temperature (T), pressure (p) and chemical potential ($\mu$), (: $\Delta \mathrm{T}=0, \Delta \mathrm{p}=0$ and $\Delta \mu_{i}=0$ ). Nevertheless, when a system is subjected to the action of an external potential field $(\varphi)$, it evolves until it achieves other thermodynamic equilibrium conditions, as Eqs. (22), (23) and (24) show, where $\varphi(x, y, z)$ is the potential energy/mass at the coordinate point (x,y,z), $d_v$ is the density and $\mathrm{PA}_{i}$ the atomic weight of the species i.

$$
\nabla T=0
\tag{22}
$$

$$
\nabla P=-d_{v} \nabla \varphi(x, y, z)
\tag{23}
$$

$$
\nabla \mu_{i}=-P A_{i} \nabla \varphi(x, y, z)
\tag{24}
$$

Eq. (24) can be solved taking into account a centrifugal field, so, in this case the contribution to Gibbs energy is given by Eq. (22). More details can be consulted in the work of Aguilar et al. [29].

$$
G_{e f}^{a d}=\frac{1}{2} P A_{i} \rho^{2} \omega^{2}
\tag{25}
$$

## 3. Materials Analysis Applying Thermodynamic (MAAT) software

### 3.1. Algorithm
MAAT (Material Analysis Applying Thermodynamics) is a thermodynamic platform, written in MATLAB 2019b as a graphical user interface GUI, which runs in 32/64 bits Windows systems. The main features of the software, are (i) calculation and plotting Gibbs Free Energy of mixing curves of binary and ternary systems, of random solid solutions, amorphous and intermetallic compounds, (ii) calculation and plotting activity of components in both binary and ternary systems in solid solutions and amorphous phases, and (iii) the possibility to compute the effect of additional terms (Section 2.4) over the Gibbs free energy of mixing of solid solutions, in binary and ternary systems.

A scheme of the algorithms of the software is presented in Fig. 1. A database of properties and parameters of each element is incorporated in the software, so no additional data is required, except in the case of additional energy sources (Section 2.4). There are four fundamental options that the user must define: (i) the number of components of the system (binary or ternary), (ii) the model of interaction between elements (solid solution, amorphous or intermetallic compound), (iii) the chemical elements and (iv) the curves or surfaces of interest. The software does not require a fixed path of instructions; therefore, the different options may be defined in any order without affecting the calculation. A description of the code is presented below.

### 3.2. Code description
The MAAT software was designed as a user-friendly graphical user interface GUI, however, the MATLAB script MAAT.m may also be used to obtain the same results. Besides, the script additionally gives access to more options that are unavailable with the GUI. According to Fig. 1, to obtain a curve/surface of a specific thermodynamic term, the user must define certain characteristics that may be summarized in six steps. The steps (a) to (f) must be conducted in any order, with no effect on the calculation.

#### (a) System selection
A panel situated at the top of the interface contains two radio buttons: 'Binary' - for a system constituted by two elements, selected by default - and 'Ternary' - constituted by three elements. The function `system_selectionChangedFcn` is called whenever an option is selected, indexing a numerical value to the global variable `handles.sis`: 1 for 'Binary', and 2 for 'Ternary'.

#### (b) Model selection
A second panel constituted by three radio buttons: 'Solid solution', 'Amorphous', and 'Intermetallic' is located below. Each of them corresponds to the different interactions between atoms, according to the models described in Section 2.2. The function `mod_selectionChangedFcn` is called whenever an option is selected, and then assigned a value to the global variable `handles.mode`: 1 for 'Solid solution, 2 for 'Amorphous', and 3 for 'Intermetallic'.

#### (c) Elements selection
There are 58 buttons displayed under the two previously mentioned panels, each of which corresponds to an element whose order is based on the periodic table arrangement. For binary systems, only two elements must be selected and for ternary systems, three elements must be selected. A global variable `handles.contador` stores the number of elements that are selected; thus, if an extra element is mistakenly selected - according to the system chosen - an error message will appear and the instruction will be annulled. When an element-button is pressed, the function `E_Callback` is called, where E corresponds to the respective element, e.g. `Li_Callback` for Lithium. The `E_Callback` function indexes the properties of the 'E' element selected - all the necessary elemental properties for calculations are already contained in the code - onto global variables of virtual elements `a`, `b`, and `c` - this lasts only in ternary systems - to preserve the defined order of elements.

#### (d) Plot options
MAAT performs calculations of enthalpy, entropy, Gibbs free energy, and activity terms, results that are plotted as curves for binary systems. Additionally, multiple curves may be plotted in the same figure, for comparison purposes, except for activity curves which are displayed individually. The 'Plot options' panel is located next to the plot space, in a checkbox format. Oppositely, for ternary systems, results are displayed as individual surfaces, each of them corresponding to their respective radial button. When a surface is selected, the function `g1_SelectionChangedFcn`

![](./images/812562814777425920_4.jpg)

Fig. 1. Flowchart of the algorithms for calculation in MAAT.

is called, indexing the corresponding numerical value onto the global variable handles.graph.

### (e) Advanced options
An optional set of effects is available for the user, located on the left side of the graphic interface. First, the temperature of the system in K. Secondly, three additional effects are available to be included in the calculations. If the 'Centrifugal field' checkbox is selected, the function c8_Callback is called, setting the global variable handles.cent equals '1', and enabling the necessary user-defined variables to perform the calculation. If the 'Grain Size effect' checkbox is selected, the function c9_Callback is called, enabling the necessary user-defined variables to perform the calculation. If the 'Dislocation effect' checkbox is selected, the function c10_Callback is called, setting the global variable handles.dislocaciones equal to '1', and enabling the necessary user-defined variables to perform the calculation. If any of these checkboxes are not selected, their effect will not be considered in the calculations, even if the user previously defined values for the respective variables. Also, consider that the 'Centrifugal field', 'Grain size', and 'Dislocation effect' are only available for calculations of the 'Solid solution' model.

The ternary extrapolation is enabled only in the ternary system. The available options are listed in a popup menu and stored in a global variable handles.p1 as a corresponding numerical value.

### (f) Calculate
Located under the 'Plot options' panel, the 'Calculate' button performs the necessary calculations to display the results requested by the user. In this part of the code, all the user-defined options are called and stored in local variables, in order to perform only the necessary calculations. If-conditions are used to verify the model, system, and other options.

First, local variables related to the Miedema's model are defined, as well as global variables are indexed into easy-to-access local variables. The $n$ local variable defines the n+1 points that will be calculated in binary systems. Next, the code exhibits two subroutines according to the corresponding system - binary or ternary. For binary systems, the calculation is simple and only particular attention must be put when the composition of an element is $x=0$ and $x=1$, due that to certain terms of models used will become undefined. If the 'Intermetallic' option is selected, only one calculation must be required; for 'Solid solution' and 'Amorphous' models, in opposition, n+1 computations must be performed using well-defined loops.

For the calculation of activity, two MATLAB integrated routines are used: fit and differentiate [60]. Gibbs free energy's curves are fitted using a 9th-grade linear polynomial equation; subsequently, these expressions are differentiated to obtain the activity, according to Eq. (15).

Finally, curves are displayed in the plot area - called handles.g2 - according to the user's instructions. The color and line style of curves only may be modified in the script.

In ternary computations, the code redefines the local variable $n$ to the number of points to be evaluated to create the composition surface. Additionally, using the function alIVL1 - well-documented in [61] - the composition matrix is created and stored in the vectors comp1, comp2, and comp3. A particular difference between binary and ternary systems computation is the requirement of a geometric extrapolation. The selected geometric extrapolation is indexed into the local variable ternextr. Hence, using if-conditions only the user-defined model is computed. For the activity computation, the fitnlm [62] function is used to fit the Gibbs free energy surface into a non-linear polynomial equation of 33 coefficients. To plot the surface of the computed term, the tersurf and terlabel functions [63] are used.

The default interface of MAAT is depicted in Fig. 2. The default setup consists of a binary system, a solid solution model, no additional sources of energy (so nor grain size/shape, dislocation density, or potential field are considered), and room temperature of 298 K to display the Modified Gibbs free energy curve.

![](./images/812562814777425920_5.jpg)

Fig. 2. Default graphics user interface of MAAT.

### 3.3. Restrictions
The MAAT software computes the temperature of the system as an input variable. However, the input value is exclusively considered for the calculation of the entropic term in Eqs. (1) and (4). Hence, the temperature value does not affect the enthalpy of mixing calculation, since it does not affect the particular parameter of the chemical elements. The default value for temperature is 298 K. All the parameters incorporated to the MAAT database are based on this default temperature.

For the entropy of mixing, an ideal configurational entropy, corresponding to random solid solutions, is incorporated. This may be generally applied to solid solutions, but it must be done with caution in amorphous, and especially, in intermetallic compounds calculations. In this last case, it is strongly recommended to consider additional data or expressions for the calculation of entropy.

### 3.4. Installation
To use MAAT, two different pathways may be used. The first one consists to download the code from Datasets in Mendeley MAAT.m, this code could be compiled directly from in MATLAB 2019b forward. For correct execution of this code, the MATLAB packages Statistical and Machine Learning Toolbox™ and Curve Fitting Toolbox™ will be required. Additionally, two additional sets of programs will be used: "Ternary Plots" [63] and "All Permutations of integers with sum criteria" [61]. These packages may be downloaded from https://www.mathworks.com/matlabcentral. After all the required files have been downloaded and put into the same folder, the MAAT.m code could be run using MATLAB.

The second option is to use the graphical user interface. For this purpose, the user must download the MAAT installation file from the web page https://www.rpm.usm.cl/download. MATLAB 2019b or any version of MATLAB is not necessary for the correct execution of MAAT. MAAT will be run directly through the MAAT executable file.

### 3.5. Comparison with other codes
Some thermodynamic softwares allow solving problems of materials and metallurgy. They are based on experimental or theoretical data published in the literature. Some of them are Thermocalc, ATAT, CaTCalc, ExTherm 2, TEST, PANDAT, GEMINI, FactSage, Miedema Calculator. These softwares work by minimizing the Gibbs free energy at a certain specific temperature, pressure, and composition. Some computational packages work using codes and others with a graphical user interface, and most of them are paid softwares or require a level of knowledge of the respective programming language. At the best of our knowledge, the existing computer programs do not have the option to include additional effects of "Centrifugal field', 'Grain size', and 'Dislocations' on the calculation of Gibbs free energy of binary or ternary systems, which is an important advantage of MAAT.

## 4. Materials and methods
### 4.1. Synthesis of materials
#### (a) Cu-Cr-Mo and Cu-Nb-Co systems
Two compositions of Cu-7Cr-7Mo (at. %) and Cu-7Nb-7Co (at. %) were synthesized by mechanical alloying. Table 1 gives the characteristics of powders used in milling. Each of the alloys was placed in hardened steel jars (250 mL) in a planetary mill (Retsch PM400), using 2 wt. % of stearic acid to prevent cold-welding phenomena and an ultra-pure Argon gas atmosphere to prevent oxidation. The milling times used were 10, 40, 70 and 130 h with a ball/powder ratio of 10/1. Two hardened steel ball sizes were used (6 balls of 12.5 mm and 24 balls of 8.0 mm diameter). To maintain a stable temperature of the vials and of the process on/off cycles of 30 and 30 min, respectively, were used.

#### (b) Ti-Ta-Sn system
A composition of Ti-13Ta-12Sn (at. %) was processed by mechanical alloying. Table 1 gives the characteristics of powders

<table>
<caption>Table 1 Characteristics of the elemental powders.</caption>
<thead>
<tr>
<th>Powder</th>
<th>Purity, at%</th>
<th>Size, µm</th>
<th>Company</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cu</td>
<td>99</td>
<td>&lt; 74</td>
<td>Sigma Aldrich</td>
</tr>
<tr>
<td>Mo</td>
<td>99.9</td>
<td>&lt; 150</td>
<td>Sigma Aldrich</td>
</tr>
<tr>
<td>Cr</td>
<td>99.5</td>
<td>&lt; 44</td>
<td>Merck</td>
</tr>
<tr>
<td>Ti</td>
<td>Grade IV</td>
<td>&lt; 150</td>
<td>Noah company</td>
</tr>
<tr>
<td>Ta</td>
<td>99.9</td>
<td>&lt; 44</td>
<td>Sigma Aldrich</td>
</tr>
<tr>
<td>Sn</td>
<td>99.8</td>
<td>&lt; 150</td>
<td>Aldrich company</td>
</tr>
<tr>
<td>Nb</td>
<td>99.85</td>
<td>&lt; 74</td>
<td>GoodFellow</td>
</tr>
<tr>
<td>Co</td>
<td>99.8</td>
<td>&lt; 2</td>
<td>Sigma Aldrich</td>
</tr>
</tbody>
</table>

used in milling. Jars (250 mL) and balls of yttrium stabilized zirconium were used in a planetary mill Retsch PM400. Two sizes of balls (10 and 5 mm diameter) with a constant ball/powder ratio of 10/1 were used. Milling was performed under an ultra-pure Argon atmosphere with 2 wt. % of stearic acid as process control agent. To maintain a stable temperature of the vials and of the process on/off cycles of 30 and 30 min, respectively, were used.

### (c) Cu-Cr system
A Cu-50Cr (wt.%) composition was studied. Initially, the Cop- per and Chromium powders were milled in a SPEX 8000D mill in separate jars. The milling time used was 8 h because at this time particles with nanocrystalline grains are obtained. Samples were obtained in disk form by mixing 50% Cu and 50% Cr and a compaction stress of 25 MPa. A centrifugal field was applied to the samples with the following experimental conditions; (i) the radius of the centrifugal field was 150 mm, (ii) two temperatures were used, 25 ad 230 °C, (iii) rotation speed of 6000 rpm (~628 rad/s) and (iv) 4 h of application of centrifugal field. The samples were subjected to two routes; (a) sample subjected to action of centrifugal field and (b) sample of reference maintained at room temperature. More information can be obtained from Aguilar et al. [29].

### 4.2. Characterization of the milled powders
The X-ray diffraction (XRD) patterns were collected using a STOE STADI-MP with a Cu $K_{\alpha 1}$ radiation source ($\lambda = 1.54056$ Å), a DETRIS MYTHEN 1K detector and a curved Germanium (111) monochromator of the Johann-type). The XRD patterns were measured in the angular range $2\theta$ between 38 and 120 degrees in the transmission mode. The microstructural infor- mation was obtained by doing Rietveld refinement using the software Materials Analysis Using Diffraction (MAUD) [64]. The instrumental broadening was determined by using $LaB_6$ as exter- nal standard. High resolution Transmission electron microscopy (HRTEM) characterization was performed using a 200 kV FEI Tecnai (FEG Philips Tecnai F20). The size and morphology of the milled powders were characterized using scanning electron mi- croscopy (JEOL JSM-7600F). Moreover, the chemical composition of the powders was measured by electron dispersive energy (EDS) Bruker X flash 6/30.

## 5. Results and discussions
The information obtained from the MAAT software was eval- uated and discussed with four experimental cases in this section: (i) synthesis of solid solution in the Cu-Mo-Cr ternary system, (ii) formation of amorphous phase in the Ti-Ta-Sn system, (iii) formation of intermetallic compound in the Cu-Nb-Co system and (iv) formation of solid solution applying a centrifugal field in the Cu-Cr system.

### 5.1. Synthesis of a solid solution in the Cu-7Cr-7Mo (at. %) system
The Cu-Mo, Cu-Cr and Mo-Cr binary systems show a positive mixing enthalpy at solid state and exhibit a very limited mutual solubility in equilibrium [65]. The solubility of Mo and Cr in Cu at room temperature is negligible [66,67]. The extension of solid solution could be achieved by non-equilibrium processing methods, such as mechanical alloying (MA), rapid solidification processing (RSP), vapor deposition, laser processing, sputtering and ion beam mixing [3]. The Gibbs free energy curves as a function of composition to form solid solution in the Cu-Mo, Cu-Cr and Mo-Cr systems are given in Fig. 3. It is possible to observe that they are positive for all composition values. The Cu-Mo system exhibits higher $\Delta G^{m}$ values than the Cu-Cr and the Mo-Cr systems. The $\Delta G^{m}$ and $\Delta G^{am}$ values for the Cu-Mo-Cr ternary system are given in Fig. 4. The enthalpy of mixing using Hillert's model [68] and configurational entropy were used to determine the $\Delta G^{m}$. There are no driving forces to obtain random solid solution and amorphous phase from pure Cu, Cr and Mo powders in the whole composition range because $\Delta G^{m}$ are higher than ideal Gibbs free energy of mixing values ($\Delta G^{m,id}$), Fig. 5. This figure gives $\Delta G^{m,id}$ values for binary and ternary systems at 298 K. This system exhibits a positive deviation from ideality, so in order to synthesize a random solid solution and especially an amorphous phase, external energy is required. Thereby, energy values around 8 and 15 kJ mol⁻¹ are necessary, respectively for a composition of Cu-7Mo-7Cr (at. %). The simulated phase diagram using ThermoCalc corroborated that there is no solid solubility in the Cu-Mo-Cr system at room temperature (Fig. 4c).

The evolution of size and morphology of the particles as a function of milling time is shown in Fig. 6. At 10 h, the par- ticles exhibited a flake morphology with a narrow particle size distribution and a size smaller than 50 µm with a few particles with a size around 100 µm. At 40 h, powders exhibit an irregular morphology with a size smaller than 120 µm. For 70, 100 and 130 h, the morphology is irregular with particle size smaller than 150, 200 and 400 µm, respectively. Despite, the particle morphology shows a little change between 70 and 130 h, in which the particles milled at 130 h are more equiaxial. During the milling two processes compete, fracture and cold welding [2]. When milling time increases, it promotes an increase in particle size, showing that cold welding is more important than fracture process, Fig. 6.

The XRD patterns of milled powders are shown in Fig. 7. At higher milling times, the patterns exhibit typical shapes of alloys subjected to severe plastic deformation: the reflections are broadened, are shifted in positions, their intensities decreased, and the peaks of solute atoms vanish (Mo and Cr). The strongest Mo (110) and Cr (110) peaks located in 40.5 and 44.3 ($2\theta$) dis- appeared at 130 h, which suggest the synthesis of a random solid solution [2]. The Cr peaks disappeared earlier than the Mo peaks, which is in agreement with the $\Delta G^{m}$ values obtained from Fig. 3 for both binary systems (Cu-Mo and Cu-Cr). The $\Delta G^{m}$ required to obtain a random solid solution between Cu and Cr is smaller than the required between Cu and Mo. This shows that the milling process transferred enough energy (~8 kJ mol⁻¹) to the Cu-7Mo-7Cr powders, thus promoting the formation of a solid solution. Moreover, the formation of an amorphous phase was not observed, which is in agreement with their higher Gibbs free energy in the whole range composition (Fig. 4b). For the amorphous phase formation, a $\Delta G^{am}$~ 15 kJ mol⁻¹ is required, which is twice the energy required to form a solid solution. As it is possible to see, there is agreement between the thermodynamic data provided by MAAT software and the experimental data of XRD patterns analysis.

![](./images/812562814777425920_6.jpg)

Fig. 3. Gibbs free energy of mixing as a function of composition of the binary systems, (a) Cu-Mo, (b) Cu-Cr and (c) Mo-Cr.

![](./images/812562814777425920_7.jpg)

Fig. 4. (a) Gibbs free energy of mixing as a function of composition for the formation of solid solutions, (b) Gibbs free energy values required to form amorphous phase and (c) simulated phase diagram of Cu-Mo-Cr system using ThermoCalc. All calculations were made at 298 K.

### 5.2. Synthesis of an amorphous phase in the Ti-13Ta-12Sn (at. %) system

Pure Ti and Ti-based alloys exhibit an allotropy change at the $\beta$-transus temperature. At lower temperature they exhibit a hexagonal close packed (hcp) crystalline structure (called $\alpha$-phase) and above this temperature they possess a body centered cubic (bcc) crystalline structure (called $\beta$-phase). The $\beta$-transus temperature for pure Ti is $882\ \pm\ 2\ ^{\circ}\text{C}$ and for Ti-based alloys depends on the type and amount of alloying elements [69].

There is no available information of the Ti-Ta-Sn ternary phase diagram at room temperature, however, a preliminary in-formation can be obtained by observing the binary systems Ti-Ta, Ti-Sn and Ta-Sn. At temperatures lower than $882\ ^{\circ}\text{C}$, the Ti-Ta phase diagram shows a binary zone with two solid solutions, $\alpha$ and $\beta$. The Ti-Sn system exhibits six phases at temperatures lower than $400\ ^{\circ}\text{C}$: $\alpha$-Ti, $\text{Ti}_3\text{Sn}$, $\text{Ti}_2\text{Sn}$, $\text{Ti}_6\text{Sn}_5$, $\text{Ti}_2\text{Sn}_3$, and Sn [70]. The Ta-Sn system shows five phases at temperatures lower than $232\ ^{\circ}\text{C}$: Ta, $\text{Ta}_3\text{Sn}$, $\text{TaSn}_2$, $\alpha$-Sn and $\beta$-Sn [71]. The Gibbs free energy curves to form solid solution as a function of composition in the Ti-Ta, Ti-Sn and Ta-Sn systems are given in Fig. 8. The three systems show negative $\Delta\text{G}^\text{m}$ values in the whole range composition. The Ti-Ta system exhibits higher energy values and the curve has two minimal points near to $x_{\text{Ta}}$~0.2 and x~0.8. There is no driving force to synthesize a solid solution from elemental powders because the $\Delta\text{G}^\text{m}$ values are higher than $\Delta\text{G}^{\text{m,id}}$ values, Fig. 8d. However, the Ti-Sn and Ta-Sn systems do exhibit enough driving force to form a solid solution because the $\Delta\text{G}^\text{m}$ values are more negative than the Gibbs free energy values of an ideal solid solution (Fig. 8b, c and d). The $\Delta\text{G}^\text{m}$ curves of the Ti-Ta, Ti-Sn and Ta-Sn binary systems have an asymmetric shape, which is

![](./images/812562814777425920_8.jpg)
![](./images/812562814777425920_9.jpg)

Fig. 5. Ideal Gibbs free energy of mixing as a function of compositions for the formation of solid solutions in: (a) A-B binary systems and (b) A-B-C ternary systems at 298 K.

![](./images/812562814777425920_10.jpg)

Fig. 6. SEM images of the milled powders (Cu-7Mo-7Cr, at. %) for all milling times.

![](./images/812562814777425920_11.jpg)

Fig. 7. XRD patterns of the Cu-7Mo-7Cr (at. %) system for all milling times.

associated to the different contributions of enthalpy (chemical, elastic and structural) of the elements.

The enthalpy of mixing was determined using Hillert's model [68] and for the Gibbs free energy calculations, a configurational entropy was considered. The Gibbs free energy surface to form solid solution $(\Delta \mathrm{G}^{\mathrm{m}})$, as a function of composition for the Ti-Ta-Sn system is shown in Fig. 9a, whereas that to form an amorphous phase $(\Delta \mathrm{G}^{\mathrm{am}})$ is shown in Fig. 9b. The specific composition studied in this work is indicated with a black dot. The $\Delta \mathrm{G}^{\mathrm{m}}$ and $\Delta \mathrm{G}^{\mathrm{am}}$ values for this composition are $\sim 9.8$ and $\sim-5 \mathrm{~kJ} \mathrm{~mol}^{-1}$, respectively. There is a driving force to form a solid solution in the zone close to the binary Ti-Sn system (Fig. 9a) according to the results obtained from binary systems (Fig. 8). The $\Delta \mathrm{G}^{\mathrm{m}}$ values are smaller than $\Delta \mathrm{G}^{\mathrm{m}, \text { id }}$ values, Fig. 5. Instead, the Gibbs free energy values to synthesize an amorphous phase $(\Delta \mathrm{G}^{\mathrm{am}})$ at room temperature are more negative towards to the binary Ti-Sn system and positive towards the Ta-rich corner. Those values suggested that there is a driving force to form an amorphous phase from elemental powders close to the Ti-Sn binary system. It is noticed that the higher $\Delta \mathrm{G}^{\mathrm{am}}$ values are at the $\mathrm{Ta}, \mathrm{Ti}$ and $\mathrm{Sn}$ corners $(\sim 23,7$ and $3 \mathrm{~kJ} \mathrm{~mol}^{-1}$, respectively) and smaller $\Delta \mathrm{G}^{\mathrm{am}}$ values are found near the $\mathrm{Sn}-65 \% \mathrm{Ti}$ composition and with low amounts of $\mathrm{Ta}\left(\sim-20 \mathrm{~kJ} \mathrm{~mol}^{-1}\right)$.

![](./images/812562814777425920_12.jpg)

Fig. 8. Gibbs free energy of mixing as a function of composition of the binary systems, (a) Ti-Ta, (b) Ti-Sn and (c) Ta-Sn at 298 K.

![](./images/812562814777425920_13.jpg)

Fig. 9. (a) $\Delta G^{\text{m}}$ of the formation of solid solutions and (b) $\Delta G^{\text{am}}$ of the formation of amorphous phase of the Ti-Ta-Sn system at 298 K.

The evolution of size and morphology of Ti-13Ta-12Sn as a function of milling time is given by Fig. 10. The observed particle size decreased from earliest milling times (~5 h) until 15 h, then increases at 50 h and finally decreases for 100 h. For milling times smaller than 15 h, the particles exhibited an irregular morphology, at 50 h the morphology is equiaxial and for 100 h particles show angular morphology.

The XRD patterns as a function of milling time are shown in Fig. 11. As it is observed, the reflections of the elemental powders ($\alpha$-Ti, Ta and Sn) remain at 2 h of milling, which indicates that they have not yet entered into solid solution. At 10 h of milling, the absence of the strongest Ta and Sn reflections is associated to the formation of a solid solution. The reflections show a high level of broadening, diminution of intensities and peak shift due to the high plastic deformation. The typical effects when powders are subject to severe plastic deformation, are increment of crystalline defects (e.g. dislocations) and diminution of crystallite size, which promote the formation of a solid solution and phase transformation ($\alpha$-Ti-based to $\beta$-based and fcc-Ti based alloys). Some authors have previously reported the formation of this metastable fcc-Ti phase [72-74]. To obtain the fcc-Ti-based alloy two conditions are required, high deformation and nanocrystalline grain size [75]. From XRD patterns, it is possible to observe that the fcc-phase is present only at 50 and 100 h of milling. The structural characteristics the Ti-13Ta-12Sn powders (at 50 and 100 h) were determined by the Rietveld refinements using the MAUD software [76] and are presented in Table 2. A refinement is considered excellent when 1<Goff<2 and Rwp<10% [77], therefore the values of Goff and $R_{\text{wp}}$ revealed that the quality of refinements is good. From Table 2, it is observed that Ti-Ta-Sn powders meet the both conditions indicated at 50 and 100 h. The microstrain value at 100 h decreases possibly because there is dynamic recrystallization.

<table>
<caption>Table 2<br>Microstructural parameters of fcc-Ti phase determined by Rietveld refinement.</caption>
<thead>
<tr>
<th>Milling time, h</th>
<th>$<\varepsilon^{2}>^{1/2}$</th>
<th>Crystallite size, nm</th>
<th>Goff</th>
</tr>
</thead>
<tbody>
<tr>
<td>50</td>
<td>0.00492 (5 × 10⁻⁵)</td>
<td>3.2 (0.03)</td>
<td>1.21</td>
</tr>
<tr>
<td>100</td>
<td>0.00165 (2 × 10⁻⁵)</td>
<td>4.1 (0.04)</td>
<td>1.43</td>
</tr>
</tbody>
</table>

The formation of the $\beta$-Ti solid solution is related to the fact that the Ta acts as $\beta$ stabilizer [78]. Moreover, by observing the Ti-Ta phase diagram, the $\beta$-transition temperature decreases when the amount of Ta increases [65]. On the other hand, the Sn showed no effects on $\beta$-transition temperature; in fact, it is considered a neutral element [69].

Finally, the broader reflections located between 30 and 50° for milling times higher than 10 h indicates the presence of a mixture of partially amorphous phase and nanocrystalline phase. By MA it is possible to obtain an amorphous phase when a large strain into the solid solution is produced by the great difference in the atomic sizes of the constituent elements [79]. The Ti atom (0.2 nm) has a size difference of ~14% with the Ta atom (0.209 nm) and ~36% with Sn atom (0.172 nm) [80].

The HRTEM images for the milling times of 50 and 100 h are shown in Fig. 12a and c, Fig. 12b and d show simulated electron diffraction images obtained by fast Fourier Transform (FFT). From HRTEM images it is possible to observe the presence of two phases, amorphous and nanocrystalline, but amorphous zones were observed in major quantity. At 50 and 100 h of milling, only spots of $\alpha$-Ti and $\beta$-Ti were observed. The images show that the crystallite sizes of the fcc-Ti solid solution are smaller than 6 nm, which is in agreement with the DRX patterns analysis. The difference between these crystallite sizes determined by XRD patterns analysis and HRTEM images is due to: (i) on nanocrystalline materials, the crystallite size follows a log-normal size

![](./images/812562814777425920_14.jpg)

Fig. 10. SEM images of powders (Ti-13Ta-12Sn) as a function of milling time.

![](./images/812562814777425920_15.jpg)

Fig. 11. Evolution of the XRD patterns of Ti-13Ta-12Sn powders as a function of the milling time.

distribution function [81], (ii) only a few images were available to be analyzed by the HRTEM, so size measurements can be from any part of the log-normal size distribution function and (iii) the X-ray spot size is very large compared with the observed HRTEM area, at least five order of magnitude larger. Finally, the results show that the milling process transferred enough energy to the Ti-13Ta-12Sn powders, which promotes the synthesis of an amorphous phase and a solid solution. Also, it is remarkable that the results obtained from the XRD patterns analysis and the HRTEM images are in well agreement with the data computed by MAAT related to the formation of amorphous phase.

### 5.3. Formation of intermetallic compounds in the cu-7nb-7co (at. %) system

The Gibbs free energy curves for the formation of solid so- lution in the binary Cu-Co, Cu-Nb and Co-Nb systems are de- picted in Fig. 13. The Cu-Co and Cu-Nb systems exhibit positive mixing enthalpy and a negligible mutual solubility at room tem- perature [65]. Meanwhile, the Co-Nb system exhibits negative enthalpy of mixing in all compositions, with a minimal value at $x{\sim}0.22$ of Co. The binary phase diagram presents very low mutual solubility and the presence of several intermetallic compounds, such as $Nb_{6}Co_{7}$, $\beta$-NbCo$_{2}$, $\alpha$-NbCo$_{2}$ and NbCo$_{3}$ [65]. The estimated $\Delta G^{m}$ and $\Delta G^{am}$ for this ternary system are depicted in Fig. 14. The Cu-depleted zone shows negative values for the formation of solid solution, while the $\Delta G^{am}$ values are positive in the whole composition range, showing that there is no driving force for the formation of an amorphous phase. For the specific Cu-7Nb-7Co (at. %) composition, the required energy values for the synthe- sis of solid solution and amorphous phase are around $\sim 3$ and $6\ \text{kJ}\ \text{mol}^{-1}$, respectively. The simulated ternary phase diagram (Fig. 14c) obtained using ThermoCalc, is in agreement with these calculations and the tendencies observed in the binary systems.

The evolution of size and morphology of Cu-7Co-7Nb pow- ders as a function of milling time is depicted in Fig. 15. At 10 h, the particles exhibited flake morphology with a wide size distribution. At 40 h, the milled powders presented an equiaxial morphology and a mean particle size of $\sim 20\ \mu\text{m}$. At 70 h, the size increased up to $\sim 70\ \mu\text{m}$, while the morphology tends to be equiaxial. At 100 and 130 h, not remarkable changes in morphol- ogy or size are noticed. From the images, it is stated that the cold welding prevailed over fracture, which after 10 h of milling was clearly observed.

The XRD patterns of the Cu-7Nb-7Co milled powders as func- tion of milling time are shown in Fig. 16. At 10 h, the reflections of Nb and Co remain and the reflections of the $Nb_{6}Co_{7}$ intermetallic compound were indexed as (JCPDS N°: 00-018-0417), indicating

![](./images/812562814777425920_16.jpg)

Fig. 12. HRTEM images and FFT of Ti-13Ta-12Sn, (a)-(b) powder milled at 50 h, (c)-(d) powders milled 100 h.

![](./images/812562814777425920_17.jpg)

Fig. 13. Gibbs free energy of mixing as a function of composition of binary systems, (a) Cu-Co, (b) Cu-Nb and (c) Co-Nb.

no solid solution formation at this milling time. The Gibbs free energy of intermetallic compounds formation at the Cu-7Nb-7Co (at. %) system was determined by MAAT as $-14.5$ kJ mol$^{-1}$. This Gibbs free energy is smaller than the determined $\Delta G^{\text{m}}$ ($\sim 3$ kJ mol$^{-1}$) and $\Delta G^{\text{am}}$ ($\sim 6$ kJ mol$^{-1}$) values, which would explain the formation of the $\text{Nb}_6\text{Co}_7$ phase. Further milling time induced the formation of a metastable fcc-solid solution, with main reflections located at: $\sim 43.3, 50.3, 74.1, 89.7$ and $95.1$ in $2\theta$. The formation of this solid solution is associated to the well-known non-equilibrium character of the mechanical alloying, which provides the required energy to extend the null mutual solubility between Cu with Nb and Cu with Co.

From 70 h, the reflections of fcc-Nb are observed and remain until 130 h. Salvo et al. [78] studied the crystallization of fcc-Nb phase by mechanical alloying and determined that above 20 h of milling this phase is formed in a Ti-30Nb-13Ta-2Mn (wt. %) alloy. Peng et al. [82] and Nandi et al. [83] proposed a transformation reaction where the formation of an amorphous phase is necessary before the formation of fcc-Nb; accordingly:
$\text{bcc-Nb} \rightarrow \text{amorphous phase} \rightarrow \text{fcc-Nb}$.

### 5.4. Effect of centrifugal field on the formation of solid solution of Cu-Cr system

More details of the effect of the centrifugal field on the formation of solid solution of Cu-Cr system can be found in Aguilar et al. [29]. The Cu-Cr system exhibits null mutual solubility at temperatures below $1077\ ^\circ\text{C}$ (eutectic temperature). At $1077\ ^\circ\text{C}$, the solubility of Cr in fcc-Cu is 0.8 at. %, but the solubility of

![](./images/812562814777425920_18.jpg)

Fig. 14. (a) $\Delta G^{\mathrm{m}}$ as a function of composition for the formation of solid solutions, (b) $\Delta G^{\mathrm{am}}$ of the formation of amorphous phase and (c) simulated phase diagram of Cu-Mo-Cr system at 298 K using ThermoCalc of the Cu-Co-Nb system at 298 K.

![](./images/812562814777425920_19.jpg)

Fig. 15. SEM images of milled powders (Cu-7Nb-7Co) for all milling times.

Cu in bcc-Cr is negligible. The estimated Gibbs free energy of mixing for the Cu-Cr system as a function of composition at two temperatures (25 and $230\ ^{\circ}\text{C}$) is shown in Fig. 17. The $\Delta G^{\mathrm{m}}$ values are positive in the whole composition range, observing maximum values around 11 and $9.5\ \text{kJ}\ \text{mol}^{-1}$ at 25 and $230\ ^{\circ}\text{C}$, respectively. These $\Delta G^{\mathrm{m}}$ values correspond to the equimolar compositions and evidenced that there are no driving forces to obtain a random solid solution from pure Copper and Chromium powders at the two temperatures. The $\Delta G^{\mathrm{m,cf}}$ value changes with temperature, at $230\ ^{\circ}\text{C}$ is $8.0\ \text{kJ}\ \text{mol}^{-1}$ and at $25\ ^{\circ}\text{C}$ is $9.2\ \text{kJ}\ \text{mol}^{-1}$. The $\Delta G^{\mathrm{m}}$ values are modified according Eq. (26), where $\Delta G^{\mathrm{m,cf}}$ is to the Gibbs free energy of mixing when a centrifugal field is applied,

![](./images/812562814777425920_20.jpg)

Fig. 16. XRD patterns evolution of Cu-7Nb-7Co (at. %) for all milling times.

$\Delta G^{\text{m}}$ is the Gibbs free energy of mixing without centrifugal field and $G_{ef}^{ad}$ is the centrifugal field per unit of mass. This term depends on the radius $(\rho)$ and the angular velocity $(\omega)$ in the same way, according to Eq. (22).

$$
\Delta G^{M, c f}=\Delta G^{M}-G_{e f}^{ad} \tag{26}
$$

The short XRD patterns of the standard sample (without treatments) and of the samples subjected to a centrifugal field at 180 °C and 230 °C for 4 h are shown in Fig. 18. After application of centrifugal field, it is observed a shift of the strongest Cu reflection (111), towards lower $2\theta$ angles and a shift of the strongest Cr reflection (110) towards higher $2\theta$ angles. Moreover, the relative intensity of the strongest Cr reflection (110) decreases with the application of a centrifugal field and temperature. When the Cu-based solid solution is stated, Cu(Cr), the lattice parameter of the Cu increases, because the atomic radius of Cr (1.85 Å) is larger than the atomic radius of Cu (1.57 Å) [80]. The effect of the centrifugal field on the lattice parameters of Cr and Cu is shown in Fig. 19. The lattice parameters were determined using Rietveld refinements with MAUD software. The figures of merit of the Rietveld refinements are low and show the good quality of fitting [29]. The lattice parameter of Cu for the samples subjected to a centrifugal field (0.36168 and 0.36179 nm at 180 and 230 °C, respectively) are higher than the standard sample (0.36149 nm). The lattice parameter of Cr decreases for the samples with centrifugal field (0.28869 and 0.28866 nm at 180 and 230 °C, respectively) in comparison with the standard sample (0.28873 nm). From these results, it can be observed the influence of the centrifugal field on the variation of lattice parameters of Cr and Cu. Fig. 20 gives a comparison between $\Delta G^{\text{m}}$ and $\Delta G^{\text{m,cf}}$ values at two temperatures (25 and 230 °C) with energy storage as crystalline defects such as, crystallite boundary $(G_{gb}^{ad})$ Eq. (16) and dislocation density $(G_{dis}^{ad})$, Eq. (18). The parameters used were crystallite size (4 nm), shape of crystallite (spherical), dislocation density $(10^{17}\ \text{m}^{-2})$ and molar volume $(7 \times 10^{-6}\ \text{m}^3\ \text{mol}^{-1})$. After milling, the powders stored a mechanical energy $(G_{gb}^{ad}+G_{dis}^{ad})$ of around 9.0 kJ mol⁻¹ which is smaller than $\Delta G^{\text{m}}$, but is higher than $\Delta G^{\text{m,cf}}$ at 230 °C. This shows that the combined effect of milling and centrifugal field is to promote the formation of solid solutions.

![](./images/812562814777425920_21.jpg)

Fig. 18. Short XRD patterns of samples, (a) reference and subjected to a centrifugal field at (b) at 180 °C for 4 h and (c) at 230 °C for 4 h [29].

![](./images/812562814777425920_22.jpg)

Fig. 17. $\Delta G^{\text{m}}$ values for the synthesis of a solution formation in the Cu-Cr system at two temperatures: (a) room temperature and (c) 230 °C [29].

## 6. Conclusions
The Materials Analysis Applying Thermodynamic (MAAT) software is a platform, written in MATLAB, which runs in 32/64 bits Windows systems and is based on the Miedema and Bakker models. The main features of the software, are (i) calculation and plotting Gibbs free energy of mixing curves of binary and ternary systems, of random solid solutions, amorphous and intermetallic compounds, (ii) calculation and plotting of the activity of components in both binary and ternary systems in solid solutions, and (iii) the possibility to compute the effect of additional terms over the Gibbs free energy of mixing of solid solutions, in binary and ternary systems. The additional terms are: centrifugal field, grain size and dislocations.

The calculations were analyzed with experimental data in four situations, formation of solid solution (Cu-Mo-Cr system), formation of amorphous phase (Ti-Ta-Sn system), formation of

![](./images/812562814777425920_23.jpg)

Fig. 19. Variation of the lattice parameter of Cr and Cu of reference sample and samples subjected to a centrifugal field for 4 h at 180 °C and c 230 °C [29].

![](./images/812562814777425920_24.jpg)

Fig. 20. Variation of the Gibbs free energy of mixing when a centrifugal field is applied for 4 h at 25 °C and 230 °C (values were obtained by MAAT).

intermetallic compound (Cu-Nb-Co system) and effect of centrifugal field on formation of solid solution (Cu-Cr system). For all cases, MAAT gives thermodynamic results comparable with experimental data from XRD, SEM and TEM. Considering that experimental thermodynamic measurements for ternary systems exhibit high complexity due to the multicomponent characteris- tic, the theoretical calculations given by MAAT are excellent tools to estimate thermodynamic properties. The MAAT is a free soft- ware that can be download from www.rpm.usm.cl. We hope that the MAAT software can be useful for all members of the materials science and engineering community, professors, researchers and especially undergraduate and graduate students.

### Declaration of competing interest

The authors declare that they have no known competing finan- cial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Acknowledgments

The authors would like to thank the financial support provided by FONDECYT, Chile grant n° 1190797 and FONDEQUIP, Chile grant n° EQM140095. We also want to thank Professor Dr. Juan Donoso for the critical revision of the manuscript.

## Appendix A. Expressions for the extension of Miedema's model to ternary systems

Below are the equations to extend the Miedema's model to ternary systems, where $\Delta H_{ABC}^{m}$ is the enthalpy of mixing of the ternary system, $x_A$, $x_B$, $x_C$ are the molar fractions of elements A, B and C, respectively and $\Delta H_{i-j}^{m}$ are the enthalpy of mixing of binaries A-B, A-C and B-C.

### A.1. Toop's model [47]

$$
\begin{aligned}
\Delta \mathrm{H}_{A B C}^{m}= & \left(x_{B / X_{A}+x_{B}}\right) \Delta \mathrm{H}_{A B}^{m}\left(\mathrm{x}_{A}, 1-x_{A}\right)+\left(\frac{\mathrm{x}_{C}}{x_{A}+x_{C}}\right) \Delta \mathrm{H}_{A C}^{m}\left(\mathrm{x}_{A}, 1-x_{A}\right) \\
& +\left(x_{B}+x_{C}\right)^{2} \Delta \mathrm{H}_{B C}^{m}\left(x_{B / x_{B}+x_{C}}, x_{C / x_{B}+x_{C}}\right)
\end{aligned}
$$

### A.2. Bonnier's model [48]

$$
\begin{aligned}
\Delta H_{A B C}^{m} & =\frac{x_{B}}{1-x_{A}} \Delta H_{A B}^{m}\left(x_{A}, 1-x_{A}\right)+\frac{x_{C}}{1-x_{A}} \Delta H_{A C}^{m}\left(x_{A}, 1-x_{A}\right) \\
+ & \left(x_{B}+x_{C}\right) \Delta H_{B C}^{m}\left(\frac{x_{B}}{x_{B}+x_{C}}, \frac{x_{C}}{x_{B}+x_{C}}\right)
\end{aligned}
$$

### A.3. Hillert's model [68]

$$
\begin{aligned}
\Delta H_{A B C}^{m} & =\frac{x_{B}}{1-x_{A}} \Delta H_{A B}^{m}\left(x_{A}, 1-x_{A}\right)+\frac{x_{C}}{1-x_{A}} \Delta H_{A C}^{m}\left(x_{A}, 1-x_{A}\right) \\
+ & \left(\frac{x_{B} x_{C}}{C_{B C} C_{C B}}\right) \Delta H_{B C}^{m}\left(C_{B C}, C_{C B}\right)
\end{aligned}
$$

where $C_{B C}=\frac{\left(1+x_{B}-x_{C}\right)}{2}$ and $C_{C B}=\frac{\left(1+x_{C}-x_{B}\right)}{2}$.

### A.4. Kohler's model [68]

$$
\begin{aligned}
\Delta H_{A B C}^{m} & =\left(x_{A}+x_{B}\right)^{2} \Delta H_{A B}^{m}\left(\frac{x_{A}}{x_{A}+x_{B}}, \frac{x_{B}}{x_{A}+x_{B}}\right) \\
+ & \left(x_{B}+x_{C}\right)^{2} \Delta H_{B C}^{m}\left(\frac{x_{B}}{x_{B}+x_{C}}, \frac{x_{C}}{x_{B}+x_{C}}\right) \\
+ & \left(x_{C}+x_{A}\right)^{2} \Delta H_{C A}^{m}\left(\frac{x_{C}}{x_{C}+x_{A}}, \frac{x_{A}}{x_{C}+x_{A}}\right)
\end{aligned}
$$

### A.5. Muggianu's model [68]

$$
\begin{aligned}
\Delta H_{A B C}^{m} & =\frac{x_{A} x_{B}}{C_{A B} C_{B A}} \Delta H_{A B}^{m}\left(C_{A B}, C_{B A}\right)+\frac{x_{B} x_{C}}{C_{B C} C_{C B}} \Delta H_{B C}^{m}\left(C_{B C}, C_{C B}\right) \\
+ & \frac{x_{C} x_{A}}{C_{C A} C_{A C}} \Delta H_{C A}^{m}\left(C_{C A}, C_{A C}\right)
\end{aligned}
$$

where $C_{i j}=\frac{\left(1+x_{i}-x_{j}\right)}{2}$.

### A.6. Miedema's model [14]

$$
\begin{aligned}
\Delta H_{A B C}^{m} & =\left(x_{A}+x_{B}\right) \frac{x_{A} V_{A}^{2 / 3}+x_{B} V_{B}^{2 / 3}}{x_{A} V_{A}^{2 / 3}+x_{B} V_{B}^{2 / 3}+x_{C} V_{C}^{2 / 3}} \\
& \times \Delta H_{A B}^{m}\left(\frac{x_{A}}{x_{A}+x_{B}}, \frac{x_{B}}{x_{A}+x_{B}}\right) \\
& +\left(x_{A}+x_{C}\right) \frac{x_{A} V_{A}^{2 / 3}+x_{C} V_{C}^{2 / 3}}{x_{A} V_{A}^{2 / 3}+x_{B} V_{B}^{2 / 3}+x_{C} V_{C}^{2 / 3}} \times \Delta H_{A C}^{m}\left(\frac{x_{A}}{x_{A}+x_{C}}, \frac{x_{C}}{x_{A}+x_{C}}\right) \\
& +\left(x_{B}+x_{C}\right) \frac{x_{B} V_{B}^{2 / 3}+x_{C} V_{C}^{2 / 3}}{x_{A} V_{A}^{2 / 3}+x_{B} V_{B}^{2 / 3}+x_{C} V_{C}^{2 / 3}} \times \Delta H_{B C}^{m}\left(\frac{x_{B}}{x_{B}+x_{C}}, \frac{x_{C}}{x_{B}+x_{C}}\right)
\end{aligned}
$$

### A.7. Colinet's model [51]

$$
\begin{aligned}
\Delta H_{A B C}^{m} & =\frac{1}{2}\left[\frac{X_{B}}{1-X_{A}} \Delta H_{A B}^{m}\left(x_{A}, 1-x_{A}\right)+\frac{X_{A}}{1-x_{B}} \Delta H_{A B}^{m}\left(1-x_{B}, x_{B}\right)\right] \\
+ & \frac{1}{2}\left[\frac{X_{C}}{1-x_{B}} \Delta H_{B C}^{m}\left(x_{B}, 1-x_{B}\right)+\frac{X_{B}}{1-x_{C}} \Delta H_{B C}^{m}\left(1-x_{C}, x_{C}\right)\right] \\
+ & \frac{1}{2}\left[\frac{x_{A}}{1-x_{C}} \Delta H_{C A}^{m}\left(x_{C}, 1-x_{C}\right)+\frac{x_{A}}{1-x_{A}} \Delta H_{C A}^{m}\left(1-x_{A}, x_{A}\right)\right]
\end{aligned}
$$

(33)

## Appendix B. Expressions for the grain shape

### Sphere with radius r

$$
\text { Area }=4 \pi r^{2} \quad(34)
$$

$$
\text { Volume }=\frac{4}{3} \pi r^{3} \quad(35)
$$

### Cubic with edge a:

$$
\text { Area }=6 a^{2} \quad(36)
$$

$$
\text { Volume }=a^{3} \quad(37)
$$

### Dodecahedral with edge a

$$
\text { Area }=3 a^{2} \sqrt{25+10 \sqrt{5}} \quad(38)
$$

$$
\text { Volume }=\frac{a^{3}}{4}\left(15+7 \sqrt{5}\right) \quad(39)
$$

## Appendix C. Supplementary data

Supplementary material related to this article can be found online at https://doi.org/10.1016/j.cpc.2020.107573.

## References

[1] D. Bloor, R.J. Brook, M.C. Flemings, S. Mahajan, The Encyclopedia of Advanced Materials, Oxford UK Pergamon, Oxford, 1994.
[2] C. Suryanarayana, Prog. Mater. Sci. 46 (2001) 1-184.
[3] C. Suryanarayna, Non-Equilibrium Processing of Materials, Pergamon Press, 1999.
[4] C. Suryanarayna, Mechanical Alloying and Milling, Marcel Dekker, New York, 2004.
[5] B.S. Murty, J.W. Yeh, S. Ranganathan, High-Entropy Alloys (2014).
[6] C. Suryanarayna, I. Seki, A. Inoue, J. Non. Cryst. Solids 355 (2009) 355-360.
[7] C. Suryanarayana, N. Al-aqeeli, Prog. Mater. Sci. 58 (2013) 383-502.
[8] C. Aguilar, D. Guzman, P. Martinez, V. Martinez, F. De Las Cuevas, S. Lascano, T. Muthiah, Mater. Chem. Phys. 146 (2014) 493-502.
[9] J.L. Pelegrina, F.C. Gennari, A.M. Condó, A. Ferández-Guillermet, 689 (2016) 161-168.
[10] S. Bera, S. Mazumdar, M. Ramgopal, S. Bhattacharyya, I. Manna, J. Mater. Sci. 42 (2007) 3645-3650.
[11] C. Aguilar, V. de P. Martinez, J.M. Palacios, S. Ordoñez, O. Pavez, Scr. Mater. 57 (2007) 213-216.
[12] C. Aguilar, V. Martinez, L. Navea, O. Pavez, M. Santander, J. Alloys Compd. 471 (2009) 336-340.
[13] L. H.L., F. S.G., S. B., Computational Thermodynamics. The Calphad Method, Cambridge University Press, New York, 2007.
[14] A.R. Miedema, P.F. Chatel, F.R. Boer, Phys. B Condens. Matter (1980) 1-28.
[15] R.F. Zhang, S.H. Zhang, Z.J. He, J. Jing, S.H. Sheng, Comput. Phys. Commun. 209 (2016) 58-69.
[16] Z. Wang, X. Wang, H. Yue, G. Shi, S. Wang, Mater. Sci. Eng. A 627 (2015) 391-398.
[17] J.F. Herbst, J. Alloys Compd. 368 (2004) 221-228.
[18] G.B. Liu, P. Gao, Z. Xue, S.Q. Yang, M.L. Zhang, J. Non. Cryst. Solids 358 (2012) 3084-3088.
[19] Y. f. Ouyang, X.P. Zhong, Z.P.J.Y. Du, Y.H. He, Z.H. Yuan, J. Alloy. Compd. 416 (2006) 148-154.
[20] R.H. De Tendler, M.R. Soriano, M.E. Pepe, J.A. Kovacs, E.E. Vicente, J.A. Alonso, 14 (2006) 297-307.
[21] G. Arzpeyma, A.E. Gheribi, M. Medraj, J. Chem. Thermodyn. 57 (2013) 82-91.
[22] D.J.M. King, S.C. Middleburgh, A.G. McGregor, M.B. Cortie, Acta Mater. 104 (2016) 172-179.
[23] Z.U.O. Ke-sheng, X.I. Sheng-qi, Z. Jing-en, 6326 (2009).
[24] Y. Ouyang, X. Zhong, Y. Du, Y. Feng, Y. He, 420 (2006) 175-181.
[25] T. Nagase, M. Suzuki, T. Tanaka, J. Alloys Compd. 619 (2015) 267-274.
[26] C. Aguilar, P. Guzman, S. Lascano, C. Parra, L. Bejar, A. Medina, D. Guzman, J. Alloys Compd. 670 (2016).
[27] G.O. Neves, E. Pio, P. Martin, C. Aguilar, C. Binder, A.N. Klein, Mater. Chem. Phys. 240 (2020) 122313.
[28] C. Suryanarayana, A. Inoue, Bulk Metalic Glasses (2011).
[29] C. Aguilar, N. Araya, A.N. Klein, R. Cardoso-Gil, P. Vargas, Phys. Status Solidi Basic Res. (2017).
[30] C. Aguilar, J. Marín, S. Ordóñez, D. Celentano, F. Castro, V. Martínez, Rev. Metal. 42 (2006) 334-344.
[31] P.K. Ray, M. Akinc, M.J. Kramer, Proceeding 22nd Anu. Conf. Fosil Energy Mater., Pittsburgh, 2008.
[32] E Physica 228 (1996) 289-294.
[33] A.R. Miedema, P.F. de Chatel, F.R. de Boer, Phys. B+ C 100 (1980) 1-28.
[34] W.C. Wang, J.H. Li, H.F. Yan, B.X. Liu, Scr. Mater. 56 (2007) 975-978.
[35] H. Bakker, G.F. Zhou, H. Yang, Prog. Mater. Sci. 39 (1995) 159-241.
[36] J.M. Lapez, J.A. Alonso, L.J. Gallego, Phys. Rev. B 36 (1987) 3716-3722.
[37] A.R. Miedema, A.K. Niessen, Calphad 7 (1983) 27-36.
[38] P.I. Loeff, A.W. Weeber, A.R. Miedema, J. Less-Common Met. 140 (1988) 299-305.
[39] H. Bakker, Enthalpies in Alloys, Miedema's Semi-Empirical Model, Trans Tech Publications Ltd, Zurich, 1998.
[40] R.F. Zhang, B.X. Liu, Appl. Phys. Lett. 81 (2002) 1219-1221.
[41] R.F. Zhang, S.H. Sheng, B.X. Liu, Chem. Phys. Lett. 442 (2007) 511-514.
[42] X.Q. Chen, R. Podloucky, P. Rogl, W. Wolf, R.F. Zhang, B.X. Liu, Appl. Phys. Lett. 86 (2005) 21-23.
[43] R.F. Zhang, K. Rajan, Chem. Phys. Lett. 612 (2014) 177-181.
[44] S.P. Sun, D.Q. Yi, Y. Jiang, B. Zang, C.H. Xu, Y. Li, 513 (2011) 149-153.
[45] M. Rafiei, M.H. Enayati, F. Karimzadeh, J. Chem. Thermodyn. 59 (2013) 243-249.
[46] M. Hillert, Calphad 4 (1980) 1-12.
[47] G. Toop, Trans. Metall. Soci-Ety AIME. 233 (1965) 850-854.
[48] E. Bonnier, R. Caboz, C.R. Hebd, Seances Acad. Sci. 250 (1960) 527-529.
[49] K. F, Monatshefte Für Chemie Und Verwandte Teile Anderer Wis- senschaften, Vol. 91, 1960, pp. 738-740.
[50] Y.M. Muggianu, M. Gambino, J. Bros, J. Chim. Phys. Physico-Chimie Biol. 72 (1975) 83-88.
[51] C. C, No Title, University of Grenoble, 1967.
[52] B. Sonderegger, E. Kozeschnik, Scr. Mater. 60 (2009) 635-638.
[53] G. Kaptay, J. Mater. Sci. 47 (2012) 8320-8335.
[54] V.M. Fokin, E.D. Zanotto, 265 (2000) 105-112.
[55] Q. Jiang, H.M. Lu, Surf. Sci. Rep. 63 (2008) 427-464.
[56] J. Wang, D. Wolf, S.R. Phillpot, H. Gleiter, Philos. Mag. a-Phys. Condens. Matter Struct. Defects Mech. Prop. 73 (1996) 517-555.
[57] G. Kaptay, Langmuir 31 (2015) 5796-5804.
[58] J. Brillo, G. Kolland, J. Mater. Sci. 51 (2016) 4888-4901.
[59] R. Benedictus, A. Böttger, E. Mittemeijer, Phys. Rev. B - Condens. Matter Mater. Phys. 54 (1996) 9109-9125.
[60] I, The MathWorks (2015) 754.
[61] B. Luong, 2020.
[62] C. Mathworks, 1993.
[63] U. Theune, 2020.
[64] L. Lutterotti, P. Scardi, J. Appl. Crystallogr. 23 (1990) 246-252.
[65] A. International, ASM Handbook: Alloy Phase Diagrams, in: Alloy Phase Diagrams, vol. 3, ASM, Metals Park, OH, 1992.
[66] S. P.R., L. D.E., Bull. Alloy Phase Diagr. 11 (1990) 169-172.
[67] E. Ma, Prog. Mater. Sci. 50 (2005) 413-509.
[68] M. Hillert, CALPHAD 4 (1980) 1-12.
[69] M. Peters, Titanium and Titanium Alloys Edited By, n.d.
[70] T.B. Massalski, H. Okamoto, P.R. Subramanian, L. Kacprzak, Binary Alloy Phase Diagrams, second ed., ASM International, 1992.
[71] O. H, J. Phase Equilib. Diffus. 38 (2017) 929-941.
[72] I. Manna, P.P. Chattopadhyay, P. Nandi, F. Banhart, H.J. Fecht, J. Appl. Phys. 93 (2003) 1520-1524.
[73] A.S. Bolokang, M.J. Phasha, D.E. Motaung, F.R. Cummings, T.F.G. Muller, C.J. Arendse, Mater. Lett. 132 (2014) 157-161.

[74] D.L. Zhang, D.Y. Ying, Mater. Lett. 50 (2001) 149–153.

[75] C. Aguilar, E. Pio, A. Medina, L. Bejar, D. Guzma, Metall. Mater. Trans. A 50 (2019) 2061–2065.

[76] L. Lutterotti, S. Matthies, H.R. Wenk, Newsl. CDP 21 (1999) 14–15.

[77] L.B. Mccusker, R.B. Von Dreele, D.E. Cox, D. Loue, P. Scardi, J. Appl. Phys. 32 (1999) 36–50.

[78] C. Salvo, C. Aguilar, R. Cardoso-Gil, A. Medina, L. Bejar, R.V. Mangalaraja, J. Alloys Compd. 720 (2017).

[79] N. Al-Aqeeli, C. Suryanarayana, M. Hussein, J. Appl. Physics. 114 (2013) 153512.

[80] R. A, 2006.

[81] C.E. Krill, R. Birringer, Philos. Mag. A 77 (1998) 621–640.

[82] Z. Peng, C. Suryanarayana, F.H. Froes, Metall. Mater. Trans. A 27 (1996) 41–48.

[83] P. Nandi, P.P. Chattopadhyay, S.K. Pabi, I. Manna, Mater. Sci. Eng. A 359 (2003) 11–17.