# Adhesion of Sodium Dodecyl Sulfate Surfactant Monolayers with TiO₂ (Rutile and Anatase) Surfaces

Robert Darkins,† Maria L. Sushko,‡ Jun Liu,‡ and Dorothy M. Duffy*,†

†Department of Physics and Astronomy, University College London, Gower Street, London WC1E 6BT, U.K.
‡Pacific Northwest National Laboratory, Richland, Washington 99352, United States

**ABSTRACT:** Surfactants are widely used as templates to control the nucleation and growth of nanostructured metal oxides such as titania. To gain insight into the origin of the surfactant−titania interactions responsible for polymorph and orientation selection, we simulate the self-assembly of an anionic surfactant monolayer on various low-index titania surfaces, for a range of densities. We characterize the binding in each case and compute the adhesion energies, finding anatase (100) and rutile (110) to be the strongest-binding surfaces. The sodium counterions in the monolayer are found to dominate the adhesion. It is also observed that the assembly is directed predominantly by surface-monolayer electrostatic complementarity. Incorporating water displacement into the calculations does not alter the general findings but does cause the adhesion energies to fall within a smaller range.

![](./images/813205124120838145_1.jpg)

## INTRODUCTION

Titania ($\text{TiO}_2$) is a technologically important material with a wide range of applications, notably in solar cells,¹,² photocatalysis,³,⁴ biomaterials,⁵ pigments,⁶ and sunscreens.⁷ In many of these applications, the function demands that the titania be nanostructured, e.g., have large surface area, high porosity, and high crystallinity. Optimizing the performance of these materials requires precise control over the phase, crystallographic orientation, and size of titania nanostructures. Molecular templating has proven to be a powerful method for achieving such control.⁸⁻¹⁰ Two major templating routes used to direct nucleation and growth of specific crystallographic planes of two-dimensional inorganic materials are (1) epitaxial growth on an inorganic template with a good lattice match with the desired crystallographic plane of the overgrowing material and (2) crystallization on organic templates or in the presence of organic molecules or biomolecules. While the mechanism of epitaxial growth is fairly well understood, the method suffers from the limitation imposed by the high degree of symmetry of the templating substrate, which severely restricts the orientation of the overgrowing crystal. Organic templates are much more versatile in the choice of their two- and three-dimensional structures, nanopattern, and functionalities, which make them particularly attractive for the design of materials. However, despite successful applications of this method in directing metal oxide growth, the mechanism of crystallization on organic templates remains elusive. One of the main bottlenecks in understanding the mechanism of template crystal growth is a complex interplay among template structure, chemistry, stability, and its interactions with the growing crystal. For example, it has been shown both experimentally and theoretically that the structure of organic templates is not retained during crystal growth. Instead, soft templates adjust to accommodate the growth of certain crystallographic planes that are not necessarily commensurate with the original template structure.¹¹,¹²

The soft-templating approach to synthesizing mesoporous titania usually involves a co-assembly process of a titania precursor with a surfactant template, a common choice being sodium dodecyl sulfate (SDS) surfactants. For instance, Mitra et al.¹³ used SDS micelles self-assembled in an oil/water microemulsion as a template to produce titania with high surface area mesoporosity. Similarly, Wang et al.¹⁴,¹⁵ produced highly crystalline mesoporous metal oxides by using SDS, in the form of a functional surfactant matrix, as an organic template. Chen et al.¹⁶ took a slightly different approach in which SDS, adsorbed on anatase nanocrystalline building blocks, directed the assembly of the blocks into a three-dimensional mesoporous material.

The properties of nanoparticles, e.g., their photocatalytic properties, are sensitive to the size and morphology of the nanoparticle, and both of these attributes can be controlled with surfactants. For instance, Liao et al.¹⁷,¹⁸ have grown titania nanoparticles in the presence of various surfactants, generating a range of morphologies. Notably, when grown in the presence of SDS, the particles were found to take on cubic morphologies, irrespective of the precursor used.

The SDS surfactants have also been used to stabilize graphene sheets and facilitate the self-assembly of nanocrystalline titania, resulting in titania−graphene hybrid materials with the potential to be used as electrodes in Li ion batteries.¹⁹

Received: April 19, 2013
Revised: July 10, 2013
Published: August 12, 2013

![](./images/813205124120838145_2.jpg)

© 2013 American Chemical Society
11609
dx.doi.org/10.1021/la401469f | Langmuir 2013, 29, 11609−11614

![](./images/813205124120838145_3.jpg)

Figure 1. Top-down view of the eight titania surfaces upon which the SDS monolayers are adsorbed. Each atom is represented by its van der Waals surface, with oxygen colored red and titanium gray.

Despite the manifest interest in organically directed inorganic nucleation, the computational literature remains sparse. Part of the difficulty with studying nucleation computationally, even for very simple systems, is that the time scales involved are generally inaccessible to atomistic simulation. As such, rather than simulate the nucleation event itself, a circumventing approach is to compute the relevant interfacial free energies that typically dictate the orientation and polymorph that are selected during nucleation. Adopting this approach, we simulate the adsorption of SDS monolayers of various densities on the (100), (110), (011), and (001) surfaces for both the anatase and rutile polymorphs (see Figure 1); the notations R($hkl$) and A($hkl$) shall be used to refer to the ($hkl$) surfaces of rutile and anatase, respectively. Initial simulations are performed in vacuo allowing us to more easily characterize the monolayer−crystal interactions. However, experimentally the nucleation events occur in the presence of water, so calculations that accommodate the displacement of water molecules by the crystal ions are also included.

### COMPUTATIONAL DETAILS

We employed molecular dynamics to model the adsorption of SDS monolayers on the eight titania surfaces illustrated in Figure 1. For each surface, these simulations were repeated for various surfactant densities, ranging from ~2.2 to ~4.4 nm⁻². For a density much below this range, the surfactants are too sparse, leading to behavior uncharacteristic of monolayers, such as local aggregation of surfactants and tails interacting with the surface. A density above this range is too high and results in the ejection of surfactants from the surface. All stable monolayer configurations are therefore expected to fall within this range.

Each titania surface had dimensions as close as possible to 3 nm × 3 nm × 1.5 nm, with periodic boundary conditions. A vacuum slab of 7 nm was added to attenuate any self-interaction between the images in the z-dimension. In the initial configuration of each simulation, the surfactants were placed 0.4 nm clear of the surface in an all-trans configuration with their tails aligned normal to the surface and each sodium cation positioned between the sulfate and the surface. They were randomly distributed across the surface (using a Poisson disk sampling algorithm to prevent overlap). Two further interfaces were constructed, each with an initially stable coverage rather than a random configuration. These were a hollow c(2 × 2) coverage on an A(001) surface and a bridged (2 × 1) coverage on an R(110) surface. The relaxed configuration of the latter is illustrated in Figure 2. These stable coverages allowed us to determine the effect, if any, that the initial monolayer configuration had on the final adhesion. Each system was equilibrated at 300 K for 60 ps (the configurational energy, which is the energy associated with the various inter- and intramolecular forces, converged well within this time) followed by a production period of 40 ps.

![](./images/813205124120838145_4.jpg)

Figure 2. Monolayer with a bridged (2 × 1) coverage relaxed on the rutile (110) surface at 300 K. Oxygen is colored red, titanium light gray, sodium purple, and sulfur yellow, and the united carbon chains are colored dark gray.

In this paper, we present the adhesion energies between the various monolayers and the various surfaces. The adhesion energy between a titania surface and some component X of the monolayer, at one particular time point t, is computed as follows

$$
\beta(\mathrm{X}, t)=\frac{1}{A}\{E(\mathrm{X}+\mathrm{TiO}_{2}, t)-[E(\mathrm{X}, t)+E(\mathrm{TiO}_{2}, t)]\} \tag{1}
$$

where $E(\mathrm{TiO}_{2},t)$ and $E(\mathrm{X},t)$ are the configurational energies of the titania surface and the X component at time t, respectively, each in isolation, and $E(\mathrm{X+TiO_{2}},t)$ is that when they are combined. A is the surface area. The adhesion energies reported here were obtained by averaging $\beta(\mathrm{X},t)$ over the 40 ps production period

$$
\beta(\mathrm{X})=\frac{1}{100} \sum_{k=1}^{100} \beta\left(\mathrm{X}, k \frac{40 \mathrm{ps}}{100}\right) \tag{2}
$$

With this method, we computed the adhesion energy between the surface and the individual components of the monolayer, e.g., $\beta(\mathrm{Na})$. The total adhesion energy between the surface and the monolayer was obtained by summing over all components of the monolayer

$$
\beta = \sum_{\mathrm{X}} \beta(\mathrm{X})
\tag{3}
$$

Experimentally, the nucleation process includes the displacement of water by the crystal ions. To account for this, we performed a second batch of simulations analogous to those performed in a previous study of carboxylic acids on calcite surfaces. $^{20}$ For each surface, and for each monolayer density, the two simulations depicted in Figure 3 were performed. Simulation I consisted of a slab of water on either side of the crystal slab, with the monolayer adsorbed at one end. In simulation II, the monolayer was adsorbed directly onto the crystal while the water was repositioned on the other side of the crystal. Because both simulations had an equal number of ions, the difference in configurational energies, $E_{\mathrm{I}}$ and $E_{\mathrm{II}}$, gives

$$
\beta' = \frac{1}{A}(E_{\mathrm{II}} - E_{\mathrm{I}}) = \beta_{\mathrm{cm}} - \beta_{\mathrm{mw}} - \beta_{\mathrm{cw}}
\tag{4}
$$

where $\beta_{\mathrm{cm}}, \beta_{\mathrm{mw}}$, and $\beta_{\mathrm{cw}}$ are the crystal-monolayer, monolayer-water, and crystal-water adhesion energies, respectively, and $A$ is the surface area. Note that $\beta_{\mathrm{cm}} \equiv \beta$ as defined in eq 3. This modified adhesion energy, $\beta'$, accounts for the displacement of water during nucleation and was averaged over a 40 ps production period having been equilibrated for 100 ps.

![](./images/813205124120838145_5.jpg)

Figure 3. Schematic representation of the two simulations performed to account for the displacement of water during nucleation.

The SDS molecules and their interaction with the titania surfaces were described using the force field of Domínguez et al. $^{21,22}$ This model consists of 12 united carbon atoms attached to an explicitly modeled sulfate headgroup, and the sodium counterion. The bond lengths and the angles are constrained by harmonic potentials, while the torsional angles in the tail and the headgroup are described by the Ryckeart and Bellemans potential and the cosine-form potential, respectively. SDS and titania interact via a Lennard-Jones (LJ) potential. The water interactions were also taken from the work of Domínguez et al. and consist of SPC-water with Lennard-Jones potentials acting between the water and all other ions in the system.

To model the titania, we diverge from the work of Domínguez and use the force field of Matsui and Akaogi, $^{23}$ which is considered the most suitable titania force field for use in molecular dynamics simulations. $^{24-26}$ The electric charges assigned to the titanium and oxygen ions in this force field, however, are 1.91 times larger than in the model of Domínguez. To retain the correct interatomic spacing, the $\varepsilon$-LJ parameters assigned to the titanium and oxygen ions in ref 22 each had to be scaled by $1.91^{2}$.

The molecular dynamics simulations were conducted using the DL_POLY Classic $^{27}$ software package in the canonical ensemble. The smooth particle mesh Ewald summation method was employed to handle long-range electrostatics with a precision of $10^{-4}$. The Nosé-Hoover thermostat maintained the desired temperature with a relaxation constant of 0.05 ps. The Verlet algorithm with a time step of 1 fs was used to integrate the equations of motion.

### RESULTS AND DISCUSSION

The adhesion energies $(\beta)$ between the monolayers and the surfaces were computed as previously described and are presented in Figure 4 (top). It can be seen that they range from $-0.7$ to $-1.6 \mathrm{~J} / \mathrm{m}^{2}$. The three main contributions to the adhesion energies come from the interaction between the titania and the sodium cations, the sulfur cations, and the three superficial oxygen anions in the $\mathrm{OSO}_{3}$ functional group of the

![](./images/813205124120838145_6.jpg)

Figure 4. Total adhesion energy (top) between the various titania surfaces and the SDS monolayers for a range of densities. The squares correspond to the labeled coverages (see the text). The bottom panels show the three main components of the adhesion energies.

surfactants. These three contributions are also plotted in Figure 4 (bottom).

The total adhesion energies for the two systems that were initially in stable configurations are also shown in Figure 4 (top), represented by squares. Via comparison of their values to the corresponding curves, it can be seen that they offer only a very small increase in adhesion energy of approximately 0.05 J/ m² over those of the initially random configurations at the same densities. We conclude that the starting monolayer config- uration in our simulations has a negligible effect on the final adhesion.

The components of the adhesion energies reveal that the sodium cations, which bind to the undercoordinated oxygen anions on the surfaces, invariably dominate the adhesion. Accordingly, it is apparent that the stronger the sodium cations bind to a surface, the stronger the entire monolayer binds. This role of the cations in the binding is supported experimentally by the observed linear uptake in SDS adsorption on titania films when the pH is decreased below $7.^{28}$

The monolayers bind more strongly to surfaces A(100) and R(110) than to the others by quite a significant amount, approximately 0.4 and 0.2 J/m², respectively, for all densities. The components of the adhesion energies reveal the features that make these two surfaces distinct from the rest. The first point to note is that the sodium cations bind more strongly to these two surfaces than to the rest, especially for A(100). The second point is that the $O_3$ anions bind to these two surfaces more strongly than the sulfur cations do, which is not the case for the other surfaces. It follows that there are both anionic- and cationic-friendly regions on these two surfaces, in contrast to the predominantly cationic-friendly nature of the other surfaces. This lateral polarity of A(100) and R(110) is evident in the x- density plots of the sodium and sulfur ions for each surface, as shown in Figure 5. It can be seen in each case that the sodium cations are concentrated around the undercoordinated oxygen anions while the sulfur ions, and therefore the sulfate functional groups, bestride the undercoordinated titanium cations. The monolayers organize themselves to achieve electrostatic complementarity with the surfaces. Moreover, they are able to match the charge periodicity of these two surfaces. This matching of charge periodicity is known to maximize adhesion.²⁹

On the A(100) surface, two rows of sulfates are forced next to each other with negligibly few sodium cations between them to act as an adhesive. This is an undesirable configuration and suggests that electrostatic complementarity with the surface predominates over the intramonolayer interactions in directing the assembly.

The modified adhesion energies $(\beta')$, which account for water displacement, are presented in Figure 6. Comparing them to the data in Figure 4 (top) reveals that the process of displacing water has little qualitative effect on the conclusions: A(100) remains the strongest-binding surface (−0.2 to −0.5 J/ m²) with R(110) mostly second (−0.1 to −0.3 J/m²) and A(001) the weakest (0 to −0.2 J/m²). The water does, however, reduce the difference between the adhesion energies of all of the surfaces quite significantly. This is presumably because the strengths with which the water and monolayers bind to each surface are roughly proportional. The fact that all of the adhesion energies $(\beta')$ are negative suggests that the monolayers will indeed enhance nucleation irrespective of the surface that forms.

The findings of this paper help to rationalize those of Núñez- Rojas and Domínguez.²² In their simulations, it was found that when SDS was adsorbed at the titania-water interface, it formed micelles on R(001) and hemimicelles on R(100); in each case, the SDS was bound to the surface mainly through the hydrophobic tails that were shielded from the water. However, on R(110), they found that the headgroups bound predominantly to the surface while the hydrophobic tails were exposed to the water. The favorable binding of SDS to R(110) found here explains this result; we would predict similar behavior for A(100), and the other anatase surfaces will likely give rise to (hemi)micelles.

![](./images/813205124120838145_7.jpg)

Figure 5. Normalized x-density of the sodium (—) and sulfur (---) ions on the (a) A(100) and (b) R(110) surfaces with respect to the surface features shown. Compare to Figure 1. These distributions were computed for a surfactant density of $\sim$3.3 nm⁻².

## CONCLUSIONS

Monolayers of the anionic SDS surfactant have been adsorbed on the (100), (110), (011), and (001) surfaces for both rutile and anatase polymorphs, and for densities ranging from $\sim$2.2 to 4.4 nm⁻². The adhesion energies have been computed in each case, revealing that these monolayers bind most strongly to anatase (100), with an adhesion energy of up to $-1.56\ \text{J}/\text{m}^2$, while rutile (110) is in second place with an adhesion energy of up to $-1.27\ \text{J}/\text{m}^2$. These findings were rationalized on the basis of the lateral charge polarity exhibited by these particular surfaces. Furthermore, the monolayer configurations formed on the A(100) and R(110) surfaces would suggest that surface– monolayer electrostatic complementarity primarily directs the assembly.

The adhesion energies were decomposed to reveal the contributions made from the individual components of the monolayers. It was found that the sodium counterions dominate the adhesion with the titania surfaces. However, it is noted that in an experimental setting the SDS typically encounters titania in the presence of a solvent such as water. Calculations that incorporated the displacement of water and thus accounted for the prenucleation water–crystal and water– monolayer interactions were therefore also conducted. The main effect that the inclusion of water had was to reduce the differences in adhesion energies between the surfaces.

![](./images/813205124120838145_8.jpg)

Figure 6. Modified adhesion energies $(\beta')$ as defined in eq 4. This quantity accounts for the displacement of water during nucleation.

## AUTHOR INFORMATION

### Corresponding Author
*E-mail: d.duffy@ucl.ac.uk.

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
R.D. acknowledges funding from EPSRC under the Molecular Modelling and Materials Science Industrial Doctorate Centre and the U.S. Department of Energy (DOE), Office of Basic Energy Sciences, Division of Materials Sciences and Engineering, via Grant KC020105-FWP12152. M.L.S. and J.L. acknowledge DOE support under the same award. Pacific Northwest National Laboratory is a multiprogram national laboratory operated for the DOE by Battelle under Contract DE-AC05-76RL01830.

## REFERENCES
(1) Phani, G.; Tulloch, G.; Vittorio, D.; Skryabin, I. Titania solar cells: New photovoltaic technology. Renewable Energy 2001, 22, 303−309.

(2) Gratzel, M. Molecular photovoltaics that mimic photosynthesis. Pure Appl. Chem. 2001, 73, 459−468.

(3) Tryk, D.; Fujishima, A.; Honda, K. Recent topics in photoelectrochemistry: Achievements and future prospects. Electrochim. Acta 2000, 45, 2363−2376.

(4) Fujishima, A.; Honda, K. Photolysis: Decomposition of water at the surface of an irradiated semiconductor. Nature 1972, 238, 37−38.

(5) Kokubo, T.; Kim, H.; Kawashita, M. Novel bioactive materials with different mechanical properties. Biomaterials 2003, 24, 2161−2175.

(6) Farrokhpay, S. A review of polymeric dispersant stabilisation of titania pigment. Adv. Colloid Interface Sci. 2009, 151, 24−32.

(7) Wakefield, G.; Green, M.; Lipscomb, S.; Flutter, B. Modified titania nanomaterials for sunscreen applications: Reducing free radical generation and DNA damage. Mater. Sci. Technol. 2004, 20, 985−988.

(8) Gower, L. B. Biomimetic model systems for investigating the amorphous precursor pathway and its role in biomineralization. Chem. Rev. 2008, 108, 4551.

(9) Choi, K.-S. Shape effect and shape control of polycrystalline semiconductor electrodes for use in photoelectrochemical cells. J. Phys. Chem. Lett. 2010, 1, 2244−2250.

(10) Li, X.; Qi, W.; Mei, D.; Sushko, M. L.; Aksay, I.; Liu, J. Functionalized graphene sheets as molecular templates for controlled nucleation and self-assembly of metal oxide-graphene nanocomposites. Adv. Mater. 2012, 24, 5136−5141.

(11) Lee, J. R.; Han, T. Y.-J.; Willey, T. M.; Wang, D.; Meulenberg, R. W.; Nilsson, J.; Dove, P. M.; Terminello, L. J.; van Buuren, T.; De Yoreo, J. J. Structural development of mercaptophenol self-assembled monolayers and the overlying mineral phase during templated $CaCO_3$ crystallization from a transient amorphous film. J. Am. Chem. Soc. 2007, 129, 10370−10381.

(12) Duffy, D. M.; Travaille, A. M.; van Kempen, H.; Harding, J. H. Effect of bicarbonate ions on the crystallization of calcite on self-assembled monolayers. J. Phys. Chem. B 2005, 109, 5713−5718.

(13) Mitra, A.; Bhaumik, A.; Paul, B. Synthesis and characterization of mesoporous titanium dioxide using self-assembly of sodium dodecyl sulfate and benzyl alcohol systems as templates. Microporous Mesoporous Mater. 2008, 109, 66−72.

(14) Wang, D.; Ma, Z.; Dai, S.; Liu, J.; Nie, Z.; Engelhard, M.; Huo, Q.; Wang, C.; Kou, R. Low-temperature synthesis of tunable mesoporous crystalline transition metal oxides and applications as Au catalyst supports. J. Phys. Chem. C 2008, 112, 13499−13509.

(15) Wang, D.; Choi, D.; Yang, Z.; Viswanathan, V.; Nie, Z.; Wang, C.; Song, Y.; Zhang, J.; Liu, J. Synthesis and Li-ion insertion properties of highly crystalline mesoporous rutile $TiO_2$. Chem. Mater. 2008, 20, 3435−3442.

(16) Chen, C.; Liu, C.; Su, Y.; Yang, C. Surface-modified anatase nanocrystalline building blocks for constructing catalytically highly active nanoporous titania materials. Appl. Catal., B 2012, 123−124, 36−42.

(17) Liao, D.; Liao, B. Shape, size and photocatalytic activity control of $TiO_2$ nanoparticles with surfactants. J. Photochem. Photobiol., A 2007, 187, 363−369.

(18) Liao, D.; Wu, G.; Liao, B. Zeta potential of shape-controlled $TiO_2$ nanoparticles with surfactants. Colloids Surf., A 2009, 348, 270−275.

(19) Wang, D.; Choi, D.; Li, J.; Yang, Z.; Nie, Z.; Kou, R.; Hu, D.; Wang, C.; Saraf, L.; Zhang, J.; Wang, D.; Choi, D.; Li, J.; Yang, Z.; Nie, Z.; Kou, R.; Hu, D.; Wang, C.; Saraf, L. V.; Zhang, J.; et al. Self-assembled $TiO_2$-graphene hybrid nanostructures for enhanced Li-ion insertion. ACS Nano 2009, 3, 907−914.

(20) Duffy, D.; Harding, J. Simulation of organic monolayers as templates for the nucleation of calcite crystals. Langmuir 2004, 20, 7630−7636.

(21) Domínguez, H. Structural transition of the sodium dodecyl sulfate (SDS) surfactant induced by changes in surfactant concentrations. J. Phys. Chem. B 2011, 115, 12422−12428.

(22) Núñez-Rojas, E.; Domínguez, H. Computational studies on the behavior of sodium dodecyl sulfate (SDS) at $TiO_2$(rutile)/water interfaces. J. Colloid Interface Sci. 2011, 364, 417−427.

(23) Matsui, M.; Akaogi, M. Molecular dynamics simulation of the structural and physical properties of the four polymorphs of $TiO_2$. Mol. Simul. 1991, 6, 239−244.

(24) Collins, D. R.; Smith, W. Technical Report DL-TR-96-001: Evaluation of $TiO_2$ Force Fields; Council for the Central Laboratory of Research Councils: Cheshire, U.K., 1996.

(25) Swamy, V.; Gale, J.; Dubrovinsky, L. Atomistic simulation of the crystal structures and bulk moduli of $TiO_2$ polymorphs. J. Phys. Chem. Solids 2001, 62, 887−895.

(26) Swamy, V.; Gale, J. Transferable variable-charge interatomic potential for atomistic simulation of titanium oxides. Phys. Rev. B 2000, 62, 5406.

(27) Smith, W.; Forester, T. The DL_POLY Classic User Manual; STFU Daresbury Laboratory: Cheshire, U.K., 2010.

(28) Dobson, K.; Roddick-Lanzilotta, A.; McQuillan, A. An in situ infrared spectroscopic investigation of adsorption of sodium dodecylsulfate and of cetyltrimethylammonium bromide surfactants to $TiO_2$, $ZrO_2$, $Al_2O_3$, and $Ta_2O_5$ particle films from aqueous solutions. Vib. Spectrosc. 2000, 24, 287−295.

(29) Jin, C.; Bai, Y.; Jagota, A.; Hui, C. Adhesion selectivity by electrostatic complementarity. II. Two-dimensional analysis. J. Appl. Phys. 2011, 110, 054903.