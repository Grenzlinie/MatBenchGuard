# Elastic response of mesoporous silicon to capillary pressures in the pores

Gennady Y. Gor' , Luca Bertinetti, Noam Bernstein, Tommy Hofmann, Peter Fratzl, and Patrick Huber

Citation: *Appl. Phys. Lett.* **106**, 261901 (2015); doi: 10.1063/1.4923240
View online: http://dx.doi.org/10.1063/1.4923240
View Table of Contents: http://aip.scitation.org/toc/apl/106/26
Published by the American Institute of Physics

![](./images/814617826672246785_1.jpg)

![](./images/814617826672246785_2.jpg)

# Elastic response of mesoporous silicon to capillary pressures in the pores

Gennady Y. Gor, $^{1,a)}$ Luca Bertinetti, $^{2}$ Noam Bernstein, $^{3}$ Tommy Hofmann, $^{4}$ Peter Fratzl, $^{2}$ 
and Patrick Huber $^{2,5}$

$^{1}$NRC Research Associate, resident at Center for Computational Materials Science, Naval Research Laboratory,
Washington, DC 20375, USA
$^{2}$Department of Biomaterials, Max-Planck Institute of Colloids and Interfaces, Research Campus Golm,
14424 Potsdam, Germany
$^{3}$Center for Computational Materials Science, Naval Research Laboratory, Washington, DC 20375, USA
$^{4}$Helmholtz-Centre Berlin for Materials and Energy, D-14109 Berlin, Germany
$^{5}$Institute of Materials Physics and Technology, Hamburg University of Technology (TUHH),
Eißendorfer Str. 42, D-21073 Hamburg-Harburg, Germany

(Received 23 April 2015; accepted 16 June 2015; published online 29 June 2015)

We study water adsorption-induced deformation of a monolithic, mesoporous silicon membrane traversed by independent channels of $\sim8$ nm diameter. We focus on the elastic constant associated with the Laplace pressure-induced deformation of the membrane upon capillary condensation, i.e., the pore-load modulus. We perform finite-element method (FEM) simulations of the adsorption-induced deformation of hexagonal and square lattices of cylindrical pores representing the membrane. We find that the pore-load modulus weakly depends on the geometrical arrangement of pores, and can be expressed as a function of porosity. We propose an analytical model which relates the pore-load modulus to the porosity and to the elastic properties of bulk silicon (Young's modulus and Poisson's ratio), and provides an excellent agreement with FEM results. We find good agreement between our experimental data and the predictions of the analytical model, with the Young's modulus of the pore walls slightly lower than the bulk value. This model is applicable to a large class of materials with morphologies similar to mesoporous silicon. Moreover, our findings suggest that liquid condensation experiments allow one to elegantly access the elastic constants of a mesoporous medium. © 2015 AIP Publishing LLC. [http://dx.doi.org/10.1063/1.4923240]

Mesoporous silicon (pSi) prepared by electrochemical etching of bulk silicon has been attracting much attention from both fundamental and applied sciences owing to its unique optical, electrical, and thermal properties. $^{1-6}$ While control over mechanical properties of pSi is necessary for its applications, the understanding of its response to mechanical loads is mainly limited to measuring Young's modulus of porous samples. $^{7,8}$

Since pSi can be prepared as a bulk (monolithic) mesoporous system with parallel, channel-like independent pores, it has been of a particular interest for studies of fluid adsorption. $^{4}$ On the one hand, this matrix allows one to study the influence of spatial confinement on the physics and chemistry of liquids. $^{9-15}$ On the other hand, it is possible to synthesize composite materials with finely tuned optical and electrical properties by liquid adsorption or infiltration. $^{4,16}$ Therefore, exploration of the mechanical properties of silicon relevant to interactions with liquids, the topic of this Letter, is also of high importance.

When a fluid is adsorbed in a mesopore, it exerts a pressure on the pore walls, which is typically of the order of $10^{7}$ Pa. $^{17}$ This pressure causes deformation of the pore, and as a result, deformation of the porous material as a whole. This effect, known as adsorption-induced deformation, has been experimentally observed for various mesoporous materials: Vycor glass, $^{18,19}$ templated silica, $^{20-22}$ low-k films, $^{23,24}$ aerogels, $^{25,26}$ porous gold, $^{27}$ and pSi. $^{28}$ There are two ways to measure the adsorption strains experimentally: for materials which can be prepared as macroscopic samples, the dilatometric technique can be used, and the reported strain is the relative change of the length of the sample. $^{18,19,25,27}$ For crystalline materials or materials which have periodic pore structure, X-ray diffraction can be used, and the strain is calculated as a change of the crystal $^{27,28}$ or pore-spacing lattice constant. $^{20,21}$ Irrespective of the technique, the measured strains for all these materials (except for aerogels) are of the order of $10^{-4}-10^{-3}$. Such small strains are in the linear elastic regime, and it is reasonable to assume a linear relation between the pressure in the pore and the experimentally observed strain with a proportionality constant $M$, called the pore-load modulus. $^{21}$ If the pore-load modulus for a certain porous material is known, it is possible to calculate the fluid pressure in the pores based on the experimental data on adsorption-induced strain, providing information on the thermodynamics of the confined fluid. Also, understanding of elastic response of a porous material to adsorption is useful for its application to sensing and actuation. $^{29,30}$

The pore-load modulus relates the pressure inside the pore to the overall deformation of the sample, rather than relating an external load to a deformation, like Young's or bulk moduli. Therefore, an important question is how to relate the pore-load modulus to the material properties of the matrix and the pore geometry. In general, for a material with a wide pore size distribution (PSD) and arbitrary pore morphology and orientation, this question may be complicated. However, for systems such as pSi considered in this work, where the geometry is regular, it can be resolved.

$^{a)}$ggor@princeton.edu

Here, we present a dilatometric study of the deformation of a macroscopic pSi membrane induced by adsorption of water vapor. From the experimental strain isotherm, we cal- culate the pore-load modulus. We perform finite element method (FEM) simulations of adsorption-induced deforma- tion of samples with hexagonal and square lattices of cylin- drical pores. We find that the pore-load modulus weakly depends on the geometrical arrangement of pores, and can be expressed as a function of porosity. Therefore, we relate the deformation of a porous sample to the deformation of a single cylindrical tube from the pressure applied to its inner surface. Based on this model, we derive an analytical expression for the pore-load modulus as a function of the porosity and the elastic properties of the non-porous material (Young's modu- lus and Poisson's ratio). The predictions of our analytical model are in excellent agreement with FEM results. We also achieve good agreement between our experiment and our an- alytical model for adsorption-induced deformation of pSi, suggesting that the Young's modulus of silicon pore walls could be only slightly lower than the Young's modulus of bulk silicon.

Adsorption-induced deformation of pSi has previously been studied by Dolino et al. $^{28}$ They obtained the strain nor mal to the plane of the sample from the shifts of X-ray dif- fraction peaks of the crystalline lattice of the silicon matrix, and calculated the normal-to-the-plane pore-load modulus from a comparison of the experimental strain to the fluid pressure in the gas pressure region, where the pores are filled with capillary condensate and the fluid pressure in the pore has a simple form. They also proposed an analytical expres- sion for the pore-load modulus as a function of material pa- rameters based on Scherer's model for porous glasses $^{31}$ and the theory of elasticity for cellular materials. $^{32}$ However, their model did not agree with the experimental data. Recently, Grosman et al. reported a dilatometric study of both the in-plane and normal-to-the-plane deformation of pSi induced by n-heptane adsorption. $^{33}$ In this work, the authors calculated the pore-load moduli for two samples, and proposed their own mechanical model to relate these moduli to the Young's modulus of silicon. By applying their model to their experimental data, the authors came to the conclu- sion that the Young's modulus of silicon walls is lower than the Young's modulus of bulk silicon by a factor of five.

Another attempt to relate the pore-load modulus to ma- terial parameters was made by Prass et al. $^{21}$ They studied adsorption strains in MCM-41 and SBA-15 silica, which have morphologies similar to pSi, and proposed that the strain, derived from the change of the pore lattice parameter, behaves similar to the hoop stress in thin-walled cylinders. Although that model provided good agreement with their ex- perimental data, it was not consistent with their FEM calcu- lations. Our model does not employ the thin-wall assumption and is fully supported with FEM calculations.

Mesoporous silicon was prepared by electrochemical etching of highly boron-doped (100) silicon wafers (pro- ducer: SiMat, Landsberg, Germany; specific conductivity: $\rho=0.01-0.025$ Ω cm). After an etching depth of 30 $\mu$m, a high voltage was applied in order to remove the mesoporous part from the bulk silicon underneath. The resulting parallel, non-interconnected, tubular pores have a short-range hexag- onal order. A scanning electron microscope (SEM) image of the sample is shown in Fig. 1.

The sample was cut in a rectangular shape with $4\,\text{mm} \times 7\,\text{mm}$ and a thickness of $30\,\mu\text{m}$. The sample's long axis was parallel to the crystallographic $\langle 010 \rangle$ direction. As prepared, the inner pore walls are Si-H terminated. A 30 min infiltration of a peroxide/water solution and subsequent rins- ing with Millipore water rendered the inner pore space Si- OH terminated, and thus hydrophilic. A volumetric nitrogen adsorption isotherm measurement performed at 77 K and analysed within the NLDFT (non-local density functional theory) model $^{34}$ indicated a mean pore diameter of 8 nm (width of the PSD 15%) and a volume porosity of 60%.

The measurements of the adsorption-induced strains were performed using a custom-made dilatometric setup, Fig. 2. The samples were tested in a sealed chamber, kept at a constant temperature of $24^\circ\text{C}$ by means of a water circula- tion thermostat (Huber). The humidity inside the chamber was controlled by means of a Wetsys (Setaram) humidity generator, which was working with a flow of 200 ml/min. The samples were clamped to two aluminium holders. The macroscopic deformation was measured by one of the hold- ers that connects to a Physics Instruments M-404 linear motor stage (resolution of $2\,\mu\text{m}$), while the axial tensile force was measured using a Honeywell R-30 load cell (50 N max. load), attached to the other holder. The standard deviation of the measured force background noise over more than 100 000 points was 10 mN. The strain of the sample was measured by driving the motors to keep a constant (small) force of 100 mN, while the humidity was continuously

![](./images/814617826672246785_3.jpg)

FIG. 1. SEM image of the pSi structure. Two-dimensional finite element representation of a porous material consisting of parallel cylindrical pores distributed on a hexagonal lattice. The mesh shown here is much coarser than the mesh used for the FEM calculations. Our FEM analysis shows that the deformation of the porous sample can be reduced to the deformation of the cylindrical domains in the $R_e$ vicinity of each pore; the latter problem can be solved analytically.

![](./images/814617826672246785_4.jpg)

FIG. 2. Schematic of the experimental setup used for measuring the adsorption-induced deformation of porous silicon. The sample holder (dark grey, on the left) is connected to a load cell, and the sample holder on the right is connected to a linear motor stage to measure the length change $\Delta l$. Thick arrows (yellow online) indicate the force on the pore walls due to Laplace pressure upon water condensation.

changed between 5% and 95% RH at a rate of 10% RH/h.
The stress on the sample under these conditions is estimated to be lower than 0.5 MPa.

In Fig. 3, we show the experimentally measured, macroscopic strain of the sample $\epsilon_m = \Delta l/l_0$ as a function of relative vapor pressure (=relative humidity) $p/p_0 = \text{RH}$ ($p_0$ is the saturation pressure of water at $24\,^\circ\text{C}$). Here, $\Delta l$ is the measured length change of the membrane and $l_0$ the length of the sample at $\text{RH}=0\%$. The behavior observed is typical of adsorption-induced deformations of mesoporous materials and is due to the change of the pressure $P$ of the confined fluid (adsorption stress) in the mesopores. $^{17}$ The shape of the strain at low pressures (before the hysteresis loop related to capillary condensation) may differ and depends on the strength of the solid-fluid interactions. $^{35}$ At higher pressures, when the pores are filled with capillary condensate, the strain changes linearly with $\ln(p/p_0)$. This trend is not specific to pSi and has been observed for all mesoporous materials investigated so far. $^{18-26,28,33}$ In our case, this region corresponds to pressures $p/p_0 \sim 0.83 - 0.93$. The strain for this region is shown in the inset of Fig. 3.

![](./images/814617826672246785_5.jpg)

FIG. 3. Measured strain of a monolithic mesoporous silicon membrane as a function of relative water vapor pressure $p/p_0$. Inset: Measured strain in the capillary condensation regime, where the strain depends logarithmically on $p/p_0$ and thus linearly on the Laplace pressures in the pores. The solid line represents a linear fit of the strain as a function of log relative pressure, and its slope corresponds to the pore-load modulus $M$.

When a pore is filled with fluid, the pressure $P$ that the fluid exerts on a pore wall is given by $^{17}$
$$
P = -\gamma_{sl}/R + P_L, \tag{1}
$$
where $\gamma_{sl}$ is the solid-liquid surface energy, $R$ is the pore radius, and $P_L$ is the Laplace pressure at the liquid meniscus. The latter can be written as (Kelvin-Laplace equation)
$$
P_L = \frac{R_g T}{V_l} \ln\left(\frac{p}{p_0}\right), \tag{2}
$$
where $R_g$ is the gas constant, $T$ is the temperature, and $V_l$ is the molar volume of the fluid. Since both the pressure in the pore and the experimentally measured strain of the porous sample as a whole vary linearly with $\ln(p/p_0)$, it is easy to get the pore-load modulus from the following relation $P = M\epsilon_m + C$, where $C$ is a constant, related to the surface energy of the solid-fluid interface. Although the value of $C$ is important for studying the thermodynamics of confined fluids, $^{36}$ it does not affect the present discussion. Fitting of the data shown in the inset of Fig. 3 gives $M=34.5$ GPa.

The key problem is to find the relation between the pore-load modulus $M$ and the elastic constants of the non-porous material: Young's modulus $E$ and Poisson's ratio $\nu$. We assume isotropic elasticity. Note that by the Young's modulus $E$, we mean the modulus of the pore walls, and not the effective Young's modulus of a pSi sample as a whole $(E_p)$, often reported in the pSi literature. $^{37}$ These two moduli should not be confused, since the latter is a property of a solid-void composite and is a strong function of the porosity. $^{7,38}$

The deformation of a system with multiple pores can be calculated numerically using FEM. $^{39}$ Since for the considered material the PSD is narrow, the pores are parallel and distributed with a short-range hexagonal order; the pore-load modulus can be approximately calculated from deformation of a two-dimensional hexagonal lattice. The FEM representation of the problem is shown in Fig. 1. The left and bottom surfaces are constrained in the $x$ and $y$ directions, respectively, while the right and top surface move freely. The pressure $P$ is applied in every pore, and the pore load modulus is estimated as the ratio of the applied pressure to the average engineering strain in the vertical direction. Poisson ratio $\nu=0.28$ was used, corresponding to bulk silicon properties. $^{40}$ Systems of two different sizes, $5 \times 8$ (68 pores) and $10 \times 16$ (295 pores), were used to check for finite size effects. We found that the results for the larger system differs from the results for the smaller one by $2.5\%$ at most. To evaluate the role of the lattice geometry, we also performed the simulations on a square lattice $14 \times 14$ (296 pores); the difference between the modulus calculated for square and hexagonal lattices is $4\%$ at porosities $\phi=35\%$ and $14\%$ at $\phi=65\%$.

The pore-load modulus calculated from FEM simulations is shown in Fig. 4. We see that the moduli for different lattice geometries are close, and for a given $E$ and $\nu$ depend mainly on porosity $\phi$—the ratio of the volume of the voids to the total volume of the sample. For an analytical estimate of this dependence, we use the following considerations based on classical theory of elasticity. A single cylindrical pore with inner radius $R$ and pressure $P$ induces a purely

![](./images/814617826672246785_6.jpg)

FIG. 4. Ratio of the pore-load modulus to the Young's modulus of non-porous material as a function of porosity $\phi$ (at $\nu=0.28$). The results of FEM simulations of deformation of samples with hexagonal and square lat- tice show that the pore-load modulus weakly depends on the geometrical arrangement of pores, and can be expressed as a function of porosity. The proposed analytical model is in excellent agreement with FEM results. It also shows reasonably good agreement with the pore-load modulus calcu- lated from the experimental data presented in this work. For comparison, theYoung's modulus of silicon was taken (100) $E=130 GPa^{40}$

deviatoric stress in an infinite plate, not leading to any swel- ling. Swelling is a consequence of the interaction of the pres- surized pore with a free surface (where the normal stress must be zero). This is well known for the swelling of a pres- surized cylinder with outer radius $R_{e}$ (Fig. 1), where the engineering strain is calculated from the increase of $R_{e}^{41,42}$

$$
\epsilon_{e}=\frac{u\left(R_{e}\right)}{R_{e}}=\frac{2 \xi\left(1-\nu^{2}\right)}{E(1-\xi)} P, \quad(3)
$$

where $\xi \equiv R^{2} / R_{e}^{2}$ . In a large plate containing many pores arranged, e.g., on a hexagonal or a square lattice, symmetry implies that the stress must vanish at half the distance between neighboring pores. Hence, the forces compensate at this point making it actually equivalent to a free surface. This suggests that the dilatational strain in the plate with many pores can be approximated by Eq. (3), where $R_{e}$ is taken as half the nearest neighbor distance in the pore lattice. The remaining question is how to relate $\xi$ to $\phi$ . One possibility would be to use the lat tice geometry to relate nearest neighbor distance to pore frac- tion, although this neglects the mechanical influence of bits of material outside the symmetry planes. This would give therelation $\xi=(2 \sqrt{3} / \pi) \phi$ for the hexagonal and $\xi=(4 / \pi) \phi$  for the square lattice, respectively. The best fit to the FEM data, however, is obtained with $\xi=\phi$ , and, in the absence of a more detailed analytical theory, we use this and write the pore-load modulus approximately as

$$
M_{e}=\frac{E}{2\left(1-\nu^{2}\right)}\left(\phi^{-1}-1\right). \quad(4)
$$

Note that Eq. (4) gives the the modulus in terms of the basic material properties $E, \nu$ and porosity $\phi$ .

The results for the pore-load modulus of porous silicon are shown in Fig. 4. The solid line shows the analytical model Eq. (4), which is in excellent agreement with the modulus $M$ derived from our FEM calculations for a porous body. Fig. 4 also shows that our model predicts a higher pore-load modulus than the model by Prass et al., $^{21}$ espe cially at porosities below $\sim 60 \%$ . Such deviation is related to the thin wall approximation used in Ref. 21, which fails when the porosity decreases.

Comparison of the model to our experimental data (Fig.4) shows that if we assume that the Young's modulus of pSi walls equals to the bulk $\langle 100\rangle$ value, the experimental data are close to the theoretical predictions, yet slightly below them. This deviation can be due to the irregularity of the pSi struc- ture. Both the deviation of pore sizes from the mean size (i.e., PSD) and deviation of the pore arrangement from a perfect lat- tice lead to presence of thinner pore walls, which reduces the pore-load modulus of the structure. Also, the Young's modulus of the walls can be somewhat lower than the modulus for bulk silicon; applying our model to calculate the Young's modulus from our experimental value of $M$ , we get $E=95 GPa$ . Note, however, that here the deviation of Young's modulus of the pore walls from the Young's modulus of bulk silicon is only $27 \%$ and not a factor of five as reported in Ref. 33.

The system of hexagonally ordered parallel cylindrical pores is not unique to mesoporous silicon: A number of tem- plated mesoporous materials have similar morphology; among them MCM-41 and SBA-15 silica, and silica mono- liths with hierarchical pores, synthesized recently. $^{22}$ The model for the pore-load modulus proposed in this work can be applied to develop quantitative models of adsorption- induced deformation of these materials. It should providebetter predictions than the earlier model $^{21}$ at porosities $60 \%$  and below, typical for mesoporous silica.

To summarize, we have presented an experimental study of water adsorption-induced deformations of a monolithic, mesoporous silicon membrane, and extracted the pore-load modulus. We have proposed an analytical model which relates the pore-load modulus to the porosity and to the elas- tic properties of bulk silicon, and justified it by comparing with FEM simulations. We have found good agreement between our experimental data and the predictions of our model, with the Young's modulus of the pore walls slightly lower than the bulk value for silicon. Our model can be applied to a large class of materials with morphologies simi- lar to mesoporous silicon. Moreover, our findings suggest that liquid condensation experiments allow one to access the elastic constants of a mesoporous medium.

This research was performed while one of the authors(G.G.) held a National Research Council Research Associateship Award at Naval Research Laboratory. G.G. thanks John Michopoulos for insightful discussions of the FEM representation of the problem. The work of G.G. and N.B. was funded by the Office of Naval Research through the Naval Research Laboratory's basic research program. P.H. acknowledges support by the German Research Foundation (DFG) within the collaborative research initiative "Tailor-made Multi-Scale Materials Systems"(SFB 986, Project area B, Hamburg).

$^{1}$ L. Canham, Appl. Phys. Lett. 57, 1046 (1990)
$^{2}$ V. Lehmann and U. Gösele, Appl. Phys. Lett. 58, 856 (1991).

$^{3}$M. J. Sailor, *Porous Silicon in Practice: Preparation, Characterization and Applications* (John Wiley & Sons, 2012).

$^{4}$*Handbook of Porous Silicon*, edited by L. Canham (Springer, 2015).

$^{5}$J. Henstock, L. Canham, and S. Anderson, *Acta Biomater.* **11**, 17 (2015).

$^{6}$P. Huber, *J. Phys.: Condens. Matter* **27**, 103102 (2015).

$^{7}$D. Bellet, P. Lamagnere, A. Vincent, and Y. Brechet, *J. Appl. Phys.* **80**, 3772 (1996).

$^{8}$C. Populaire, B. Remaki, V. Lysenko, D. Barbier, H. Artmann, and T. Pannek, *Appl. Phys. Lett.* **83**, 1370 (2003).

$^{9}$B. Coasne, A. Grosman, C. Ortega, and M. Simon, *Phys. Rev. Lett.* **88**, 256102 (2002).

$^{10}$D. Wallacher, N. Künzner, D. Kovalev, N. Knorr, and K. Knorr, *Phys. Rev. Lett.* **92**, 195704 (2004).

$^{11}$T. Hofmann, D. Wallacher, P. Huber, and K. Knorr, *J. Low Temp. Phys.* **140**, 91 (2005).

$^{12}$S. Naumov, A. Khokhlov, R. Valiullin, J. Kärger, and P. A. Monson, *Phys. Rev. E* **78**, 060601 (2008).

$^{13}$P. Kumar, T. Hofmann, K. Knorr, P. Huber, P. Scheib, and P. Lemmens, *J. Appl. Phys.* **103**, 024303 (2008).

$^{14}$A. Henschel, P. Kumar, T. Hofmann, K. Knorr, and P. Huber, *Phys. Rev. B* **79**, 032601 (2009).

$^{15}$J. Kärger and R. Valiullin, in *Handbook of Porous Silicon*, edited by L. Canham (Springer, 2014), pp. 1–10.

$^{16}$A. S. Westover, J. W. Tian, S. Bernath, L. Oakes, R. Edwards, F. N. Shabab, S. Chatterjee, A. V. Anilkumar, and C. L. Pint, *Nano Lett.* **14**, 3197 (2014).

$^{17}$G. Y. Gor and A. V. Neimark, *Langmuir* **26**, 13021 (2010).

$^{18}$C. Amberg and R. McIntosh, *Can. J. Chem.* **30**, 1012 (1952).

$^{19}$K. Schappert and R. Pelster, *Langmuir* **30**, 14004 (2014).

$^{20}$G. Günther, J. Prass, O. Paris, and M. Schoen, *Phys. Rev. Lett.* **101**, 086104 (2008).

$^{21}$J. Prass, D. Müter, P. Fratzl, and O. Paris, *Appl. Phys. Lett.* **95**, 083121 (2009).

$^{22}$C. Balzer, R. Morak, M. Erko, C. Triantafillidis, N. Hüsing, and O. Paris, *Z. Phys. Chem.* (published online).

$^{23}$K. Mogilnikov and M. Baklanov, *Electrochem. Solid-State Lett.* **5**, F29 (2002).

$^{24}$S. Dourdain, D. Britton, H. Reichert, and A. Gibaud, *Appl. Phys. Lett.* **93**, 183108 (2008).

$^{25}$G. Reichenauer and G. Scherer, *J. Non-Cryst. Solids* **285**, 167 (2001).

$^{26}$T. Herman, J. Day, and J. Beamish, *Phys. Rev. B* **73**, 094127 (2006).

$^{27}$L.-H. Shao, H.-J. Jin, R. N. Viswanath, and J. Weissmüller, *EPL* **89**, 66001 (2010).

$^{28}$G. Dolino, D. Bellet, and C. Faivre, *Phys. Rev. B* **54**, 17919 (1996).

$^{29}$L. Bertinetti, F. Fischer, and P. Fratzl, *Phys. Rev. Lett.* **111**, 238001 (2013).

$^{30}$Q. Zhao, J. W. Dunlop, X. Qiu, F. Huang, Z. Zhang, J. Heyda, J. Dzubiella, M. Antonietti, and J. Yuan, *Nat. Commun.* **5**, 4293 (2014).

$^{31}$G. W. Scherer, *J. Am. Ceram. Soc.* **69**, 473 (1986).

$^{32}$L. J. Gibson and M. F. Ashby, *Cellular Solids: Structure and Properties* (Cambridge University Press, 1999).

$^{33}$A. Grosman, J. Puibasset, and E. Rolley, *EPL* **109**, 56002 (2015).

$^{34}$J. Landers, G. Y. Gor, and A. V. Neimark, *Colloids Surf., A* **437**, 3 (2013).

$^{35}$G. Y. Gor, O. Paris, J. Prass, P. A. Russo, M. M. L. Ribeiro Carrott, and A. V. Neimark, *Langmuir* **29**, 8601 (2013).

$^{36}$G. Y. Gor, *Langmuir* **30**, 13564 (2014).

$^{37}$L. Canham, "Mechanical properties of porous silicon," *Handbook of Porous Silicon* (Springer, 2015), pp. 213–220.

$^{38}$H. Magoariec and A. Danescu, *Phys. Status Solidi C* **6**, 1680 (2009).

$^{39}$F. Hecht, *J. Numer. Math.* **20**, 251 (2012).

$^{40}$M. A. Hopcroft, W. D. Nix, and T. W. Kenny, *J. Microelectromech. Syst.* **19**, 229 (2010).

$^{41}$S. Timoshenko and J. Goodier, *Theory of Elasticity*, 3rd ed. (McGraw-Hill, New York, 1970).

$^{42}$L. D. Landau and E. Lifshitz, *Theory of Elasticity, Course of Theoretical Physics* Vol. 7, 3rd ed. (Elsevier, 1986).

![](./images/814617826672246785_7.jpg)