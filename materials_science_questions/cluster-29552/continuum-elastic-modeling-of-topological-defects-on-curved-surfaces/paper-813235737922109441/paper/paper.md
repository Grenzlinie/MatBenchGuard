# Defectivity study of directed self-assembly of cylindrical diblock copolymers in laterally confined thin channels

Bongkeun Kim$^{\rm a,c}$, Nabil Laachi$^{\rm a}$, Glenn H. Fredrickson$^{*,\rm a,b}$

$^{\rm a}$Materials Research Laboratory, University of California, Santa Barbara CA, USA 93106-5121;
$^{\rm b}$Mitsubishi Chemical Center for Advanced Materials, 3105 MRL Building, University of California Santa Barbara, CA 93106-5150; $^{\rm c}$Dow Materials Institute, University of California, Santa Barbara, CA, USA 93106-5121

## ABSTRACT

We use self-consistent field theory (SCFT) to study the directed self-assembly of cylinder-forming diblock copolymers laterally confined in narrow channels. The side walls and top/bottom surfaces of the channel are either all major block attractive, all minor block attractive, or a combination of major block attractive on the top surface and minor block attractive on the remaining film surfaces. We focus on systems in which the self-assembled cylinders form a monolayer oriented parallel to the sidewalls in a thin channel. Experimentally and theoretically, well-ordered perfect cylinders are observed in narrow channels, but undesirable defective structures are also found. We investigate the energetics of isolated, meta-stable defects and compare them with two types of defects (dislocations and disclinations) recently investigated in laterally confined lamellar block copolymer systems using SCFT. Our simulation results are also compared with defect energy estimates for lying down cylinder monolayers extracted from experimental work by Mishra and coworkers. Parametric studies include the effects of film thickness, domain spacing, $\chi N$, and composition on defect energies with various wall wetting conditions in narrow channels of varying widths. A major finding is that defects of cylindrical directed self-assembly in a confined channel have a smaller free energy cost (tens of kT) in comparison with defects in laterally confined, vertically oriented lamellae (many tens of kT). We also discovered a novel vertically branched cylinder defect in the case of neutral top and bottom surfaces with significantly lower defect energy than a corresponding dislocation defect. More broadly, this study reveals unexpected dependences of equilibrium defect densities on a wide range of parameters that must be carefully controlled in order to successfully implement a directed self-assembly process with block-copolymers.

**Keywords:** Self-Consistent Field Theory (SCFT), graphoepitaxy, directed self-assembly, defects, Graphic Processing Unit (GPU)

## 1. INTRODUCTION

Nanofabrication is gradually depending on the development of alternative patterning strategies as the optical lithography rapidly approaches its scaling limits. The self-assembly of different block copolymers has been considered as one of the most promising high resolution patterning alternatives that can overcome the $\sim40$ nm (half-pitch) limit of the current state-of-the-art optical lithography-based technologies. But thin films of block copolymers should be carefully controlled to avoid randomly oriented grains of the self-assembly showing poor long-range order of patterns.$^{1-3}$ Reducing the density of undesirable defective structures is therefore a major challenge to achieve the required performance of the technique and guarantee its viability.$^{3}$ To overcome this challenge, directed self-assembly (DSA) of block copolymers, with graphoepitaxy (or lateral confinement) for example, can offer a method to produce well-oriented patterns with very low defect populations. In a previous study,$^{4}$ lamella-forming block copolymers were studied theoretically and compared to experimental results,$^{5}$ resulting in defects with a formation energy in the order of 50-100kT. The monolayer of the cylindrical DSA in a confined thin film will be presented here. Similar to the lamellar case, we use self-consistent field theory to study the effects of various conditions of wetting surfaces and compare our results to available experiments as well.$^{6}$

In our simulations, the boundaries of the confining cell are assumed to have an affinity for A and B segments that is tunable, but homogeneous, along the perimeter. An experimental realization of such a system could be obtained by the "lift-off" technique$^{7}$ or by use of a bilayer substrate.$^{8}$ In the lift-off method, a resist is patterned in a square shape onto a neutral surface using optical or e-beam lithography, and then material that has selectivity for A or B segments is

---
Alternative Lithographic Technologies V, edited by William M. Tong, Douglas J. Resnick,
Proc. of SPIE Vol. 8680, 868016 · © 2013 SPIE · CCC code: 0277-786X/13/$18 · doi: 10.1117/12.2011178

Proc. of SPIE Vol. 8680 868016-1

deposited onto the patterned resist. After removing the resist, the material not on the resist remains to form mesas surrounding the well, and its sides attract either the A or B blocks. In the second approach of using a bilayer substrate, by etching through just the top layer to define a square well, the four sides of the well would have selectivity for A and B segments set by the surface chemistry of the top layer, while the chemistry of the bottom layer would dictate the selectivity of the bottom surface of the square well. For both methods, by choosing the bottom layer appropriately, e.g., a random copolymer of A and B segments, it should be possible to create a neutral bottom surface.

The model equations for a melt of AB block copolymers in confinement are built on the standard Gaussian-chain model, with a Flory-type monomer-monomer interaction parameter, $\chi$, describing interactions between dissimilar segments and a Flory-like monomer-wall interaction parameter, $\chi_{\mathrm{w}}$, describing interactions between polymer segments and the confining walls. A particle-based model for a system of interacting polymer chains is converted into a field-based model of a single chain in an external field through formally exact methods related to the Hubbard-Stratonovich transformation. The resulting statistical field theory is simplified by imposing a mean-field approximation, resulting in the well-known equations of self-consistent-field theory (SCFT). Here we consider a square domain of side length $L$ (in units of the unperturbed radius of gyration of an AB diblock copolymer, $R_{\mathrm{g}}$, typically on the order of 4-12 nm). Two defective structures, dislocation (DL, Figure 1(a)) and disclination (DC, Figure 1(b)) are studied and compared to our previous work $^{4}$ and available experimental studies $^{6}$. Details of the simulation method including calculations of defect free energy can be found in References. $^{4,9-12}$

![](./images/813235737922109441_1.jpg)

Figure 1 Density plot of the minor component in block copolymer of 4 periods of cylindrical DSA, (a) dislocation (DL) and (b) disclination (DC)

Before we present our results, we should mention that, in all the figures, the free energies are computed for PS/PMMA melts, which enables a comparison with the previously studied PS/PMMA-based lamellar systems $^{4}$. In order to compare with available experimental results for PS/P2VP cylinder-forming confined melts, the defect energies presented here must be rescaled using a multiplying factor of 0.58. This conversion factor arises from differences in the atomic weight and density of the monomers forming PMMA and P2VP. Note also that all the results of maximum formation free energies of dislocations and disclinations for different segregation strengths, block fraction and wetting conditions are summarized in Figure 6.

## 2. SINGLE LAYER OF CYLINDERS FORMED IN A CONFINED CHANNEL WITH MINOR-BLOCK WETTING SIDE-WALLS

### 2.1 Neutral top/bottom surfaces

We first consider a confining channel with minor block attractive sidewalls and neutral top and bottom surfaces. The minor block wetting induces cylinder formation very easily from a random initial condition and helps to find suitable conditions that favor perfectly aligned cylinders. Dislocation and disclination free energies for this wetting set-up are shown in Figure 2.

Calculated defect free energies of dislocation defects range from 3.5 kT to 7.2 Kt, which are significantly lower than 50-100 kT for the lamellar case⁴ and smaller smaller than the experimental values⁶, 10-14 kT for PS-P2VP block copolymers. We also studied disclination defect free energies with minor block composition fₐ= 0.258. When the depth of the channel on z axis is at z= 3.75 Rg, the maximum of defect free energies is about 20 kT and the defect starts relaxing to the perfect cylindrical state with deep channel at z= 3.9 Rg. For smaller depths or if the initial defect structures (with vertical cylinders branched from disconnected horizontal cylinders) are taken from a larger fraction fₐ= 0.3, the defect free energies significantly decrease to less than 7.5 kT. So we can conclude that formation of vertical cylinders in a horizontally confined wall system stabilizes the defect and thus lower the defect free energy (see Figure 2(a)). Varying the minor block composition from 0.232 to 0.3 clearly shows the same trend of increasing free energy with increasing volume fraction, fₐ, as shown on Figure 11 from Mishra et al⁶. But if the vertical cylinders form at the end of disconnected horizontal cylinders, these additional branched cylinders hinder the relaxation of defects and lower the free energy (see Figure 2(b)).

![](./images/813235737922109441_2.jpg)

Figure 2 (a) Defect free energies of dislocation defects with a minor block composition f=0.258 for a various wall depth z.
(b) Defect free energies of disclination defects with χN=30 for a various minor block fraction fₐ.

### 2.2 Major block wetting top and bottom surfaces

The main reason for the vertical cylinder formation is the use of neutral wetting conditions at the top and bottom surfaces. In this section, major block wetting conditions will be applied to both top and bottom surfaces and the effect of the wetting strength will be investigated. As shown in Figure 3(a), when the wetting condition at the top/bottom surface is neutral ($\chi$Wall = 0), the vertically branched cylinder forms oval-shaped columns and the edge of this column becomes sharper as $\chi$Wall strength is increased and the free energy of dislocation defect formation also significantly increases. At the position of the maximum free energy, $\chi$Wall = 42, the contact area of the vertical cylinder at the top/bottom surface is at its minimum and stronger $\chi$Wall values remove this contact and no vertical cylinder can be found. Above $\chi$Wall= 44, defects with vertical cylinders are not found and so the maximum of free energy of defect formation remains constant. Changing the wetting strength does not affect the magnitude of the defect free energy once the vertically branched cylinders disappear. The difference in the defect free energy is 3.5 kT between the maximum at $\chi$Wall = 42 and $\chi$Wall > 42 (no vertical cylinder) and 12.2 kT between $\chi$Wall = 0 (neutral with vertical cylinder) and $\chi$Wall > 42. Relatively strong major block wetting condition ($\chi$Wall > 42) will be required to avoid the vertically branched cylinder formation when the sidewalls are minor block attractive. More detailed studies were done to investigate the effect of strong $\chi$Wall attraction to major block wetting top and bottom surfaces by calculating the free energies of a dislocation defect as a function of the channel width (see Figure 3(b)). When the channel widths are near the free energy maxima for different $\chi$Wall, the trend of increasing free energy with increasing $\chi$Wall is the same as the trend on Figure 3(a). But the $\chi$Wall is around its maximum on Figure 3(a), $\chi$Wall= 40 and 42, and removal of the vertical column can occur when the channel width is too small or too large (in this region conversion of the number of cylinders occurs to one smaller or larger period of global horizontal cylindrical DSA). The region of sharp edged vertical cylinder formation is reduced when $\chi$Wall increases from 40 to 42 to the maximum of free energy on Figure 3(b)).

![](./images/813235737922109441_3.jpg)

Figure 3 (a) The effect of the major block wetting $\chi$Wall on the free energy of "dislocation" defect formation. The channel width and $\chi$N were kept 21.0 Rg and 30.0 respectively. The cross-section images were taken from $\chi$Wall=0 (neutral), $\chi$Wall= 42 (at the maximum of free energy) and $\chi$Wall= 64 (no vertical cylinder). (b) The free energy curves of "dislocation" defect formation as a function of channel width with different strengths of major block wetting on top and bottom surface. When $\chi$Wall = 40 and 42, the free energy curves step down to the one of higher $\chi$Wall (>42) and vertical cylinder is removed at the smaller/larger channel widths which are the boundaries for forming one cylinder smaller/larger period.

### 2.3 Minor-block wetting bottom surface and major-block wetting top surface.

In addition to minor-block wetting conditions on the masking side walls, we consider in this section bottom surfaces that are minor block attractive and top surfaces that are major block attractive. Our results for this configuration are summarized on Figure 6 (DL: A (side+ bottom) + B (top)).

With fixed $\chi$N = 30, when changing the minor block fraction from 0.232 to 0.275, the maximum defect free energy increases from 17.2 kT to 24.1 kT for dislocations (Figure 4 (a)) and from 30.9 kT to 43.1 kT for disclinations (Figure 5(a)). The converted values for PS/P2VP of dislocation defects range from 9.3 kT to 13.0 kT which are close to the experimental values⁶ (10 kT to 14.0 kT). The position of the maximum free energy also increases from 19.2 Rg to 20.9 Rg for dislocations and from 19.2 Rg to 20.7 Rg for disclinations. When the composition fₐ further decreases below 0.23, the free energy significantly decreases. This is also found experimentally⁶. A possible explanation is the conversion of the defect structure from a dislocation to a disconnected defect because of the small fraction of the minor block. No vertically branched cylinder formations can be found using our model with this wetting condition, hence the predicted defect free energies are matched well to the experimental values. For a minor block fraction, fₐ = 0.258 and when $\chi$N is increased from 25 to 30, the maximum defect free energy increases from 13.1 kT to 26.1 kT (7.1 kT to 14.1 kT for PS/P2VP) for dislocations (Figure 4(b)) and from 23.9 kT to 37.7 kT (12.9 kT to 20.4 kT for PS/P2VP) for disclinations (Figure 5(b)). These results are again similar to the experimental values of PS/P2VP block copolymer (10 kT to 14.0 kT respectively). The position of the maximum free energy only increases from 19.9 Rg to 20.7 Rg for dislocations and from 19.6 Rg to 20.1 Rg for disclinations. This is a smaller change than that observed when the composition is varied. We also observed that the major difference between dislocation structures is the size of minor block bridge between two parallel cylinders. When $\chi$N is small ($\chi$N= 25) the bridged minor block is thinner than when $\chi$N is large ($\chi$N= 33).


![](./images/813235737922109441_4.jpg)

Figure 4 (a) The defect free energy curves of dislocation defects with various minor block compositions. The $\chi$N is fixed to 30. The density plot of minor bock of dislocation defect is shown from the maximum point of f= 0.275. (b) The defect free energy curves of dislocation defects as $\chi$N is varied. The defect structures taken from the maximum position of $\chi$N= 25 and $\chi$N= 33.

![](./images/813235737922109441_5.jpg)

Figure 5 (a) The defect free energy curves of disclination defects with various minor block compositions. The $\chi$N is fixed to 30. The density plot of minor bock of dislocation defect is shown from the maximum point of f= 0.275. (b) The defect free energy curves of dislocation defects as $\chi$N is varied. The defect structures taken from the maximum position of $\chi$N= 25 and $\chi$N= 33.

### 2.4 Minor block wetting on top and bottom surfaces.

Similar to the results above in the case of the major block wetting on the top surface, the defect free energy of dislocations with minor block wetting conditions at all surfaces is relatively low and in the order of 10-30 kT for dislocations and disclinations. When $\chi$N is fixed to 30, changing the minor block composition from 0.258 to 0.305

increases the maximum defect free energy from 18.7 kT to 24.0 kT for dislocations and from 20.6 to 34.4 kT for disclinations when the fraction changes from 0.245 to 0.305. The position of the maximum free energy also increases from $19.1\ \mathrm{R_g}$ to $20.2\ \mathrm{R_g}$ for dislocations and from $18.7\ \mathrm{R_g}$ to $20.2\ \mathrm{R_g}$ for disclinations. When $\chi$ increased from 27 to 38 with fixed $\mathrm{f_A}=0.258$, the maximum free energy increases from 16.6 kT to 30.3 kT for dislocations and from 18.1 kT to 32.9 kT for disclinations. Similar to the case above, the increase in $\chi\mathrm{N}$ affects the defect free energy more than increasing the minor block fraction for both dislocations and disclinations.

## 3. A SINGLE LAYER OF CYLINDERS FORMED IN A CONFINED CHANNEL WITH MAJOR BLOCK WETTING SIDEWALLS

### 3.1 All major block wetting surfaces

With an optimal wall depth of $3.94\ \mathrm{R_g}$, only the disclination defect is meta-stable under these wetting conditions. With fixed $\chi\mathrm{N}=30$, changing the minor block composition from 0.232 to 0.275 increases the maximum defect free energy from 33.4 kT to 49.7 kT for a PS/PMMA melt. The position of the maximum free energy also increases from $16.0\ \mathrm{R_g}\ (\mathrm{f_A}$ $=0.232)$ to $16.8\ \mathrm{R_g}\ (\mathrm{f_A}=0.275)$. When the segregation strength is increased from 25 to 33 the maximum disclination defect free energy increases from 26.2 kT to 51.7 kT for PS/PMMA. The position of the maximum free energy only increases from $15.6\ \mathrm{R_g}$ to $16.8\ \mathrm{R_g}$. The increase in $\chi\mathrm{N}$ affects the magnitude of the defect free energies more than increasing the minor block composition. The maximum of defect free energies is also about 1/3 to 1/2 of the defect free energies of lamella. $^{4}$ The maxima of defect free energies on all major block wetting surfaces are plotted on Figure 6 (DC: All B)

### 3.2 Major block wetting on the bottom surface and the minor block wetting on the top surface

With increased optimal wall depth of $6.0\ \mathrm{R_g}$, a planar layer of the minor block can be found near the top surface. With a fixed fraction, $\mathrm{f_A}$= 0.258, the maximum of defect free energy increases from 24.3 kT to 38.9 kT for dislocations when $\chi\mathrm{N}$ changes 30 to 38. In the case of disclinations, the free energy increases from 36.1 kT to 46.8 kT when $\chi\mathrm{N}$ changes from 27 to 35. The position of the maximum free energy also increases from $16.4\ \mathrm{R_g}$ to $17.3\ \mathrm{R_g}$ for dislocations and from 16.1 $\mathrm{R_g}$ to $16.8\ \mathrm{R_g}$ for disclinations. When $\chi\mathrm{N}$ is fixed to 30, changing the minor block composition from 0.232 to 0.275 increases the maximum defect free energy from 20.9 kT to 27.1 kT for dislocations and from 36.1 kT to 46.8 kT for disclinations. The position of the maximum free energy also increases from $16.0\ \mathrm{R_g}$ to $16.8\ \mathrm{R_g}$ for both dislocations disclinations, similar to the result from the all major block wetting condition. The maximum of defect free energies is also about 1/3 to 1/2 of that of the dislocation defect in the lamella system $^{4}$. The results are depicted on Figure 6 (DL and DC: A (top) + B (side + bottom))

## 4. CONCLUSIONS

We use SCFT to elucidate conditions in terms of the segregation strength, polymer composition and wetting conditions that successfully induce the defect free formation of a monolayer of cylinders of pure diblock co-polymers in thin, laterally confining channels. Using GPU-accelerated SCFT simulations, the free energy of dislocations and disclinations can be calculated efficiently in three-dimensional space. Our current results indicate that using higher composition fractions of the minor block and higher $\chi\mathrm{N}$ parameters enables cylindrical DSA with higher free energies of defect formation (see Figure 6). However, the minor block composition cannot exceed $\mathrm{f_A}=0.33$ which is the upper boundary before lamellar structures are formed according to the mean-field diagram. $^{13}$ The increase of defect free energy with $\chi\mathrm{N}$ is much greater than the increase when the minor block fraction $\mathrm{f_A}$ increases. But the increase of $\chi\mathrm{N}$ also causes the radius of gyration, $\mathrm{R_g}$, of block copolymers to be longer, with changes in $\chi\mathrm{N}$ from 25 to 35, the $\mathrm{R_g}$ can be varied from 7.3 nm to 8.7 nm for a PS/PMMA diblock. Choosing a different diblock copolymer which has a high $\chi$ value such as PS/P2VP or PS/PDMS for example, can alleviate this problem and enables larger $\chi\mathrm{N}$ while maintaining relatively low $\mathrm{R_g}$ values.

For $\chi\mathrm{N}$ values ranging from 25 to 35, defect free energies are in the order of 10-30 kT for dislocations and disclinations for PS-PMMA systems and 10-30kT for PS/P2VP systems. Choosing different wetting models can further increase the magnitude of defect free energies. Turning on either major block or minor block wetting on the top and bottom surfaces whilst maintaining A block (minor) wetting conditions only on the side walls (DL: A (side) and DC: A (side) in Figure (a) and (b)) enables an additional free energy gain of about 10 kT for both dislocation and disclination defects. This is

Proc. of SPIE Vol. 8680 868016-6

mainly the result of the wetting conditions that remove the formation of vertically branched cylinders at the end of the defect area as shown in section 2.2. A (top) + B (side + bottom) wetting model generates the highest defect free energies and A (side) + B (top + bottom) wetting gives higher defect free energy than A (side + bottom) + B (top) wetting, which in turn has greater free energy than A (side) wetting for dislocation defects. Furthermore, B (all) wetting model and A (top) + B (side + bottom) wetting model give higher defect free energies than any other wetting model for disclination defects. A (all) wetting model shows the lowest defect free energy (except when vertically branched cylinders are formed), with a relatively close defect free energies of dislocations and disclinations.

Our results can provide useful guidelines for wetting condition, copolymer composition, commensurability and segregation strengths for the design of optimized graphoepitaxial processes where the probability of defect formation is limited to very low concentration.

![](./images/813235737922109441_6.jpg)

Figure 6 (a) The free energy curves of “dislocation (DL)” and “disclination (DC)” defect formation as a function of the minor block (A) fraction for three different wetting conditions of the surfaces of a confining channel. The $\chi$N was set to 30. (b) The free energy curves of “dislocation (DL)” and “disclination (DC)” defect formation as a function of the $\chi$N parameter for three different wetting conditions of the surfaces of a confining channel. The block fraction fA was set to 0.258.

## ACKNOWLEDGMENTS

We thank the Dow Chemical Company and the Dow Materials Institute at the University of California, Santa Barbara for financial support. The computer simulations presented in this work were performed using computational facilities at the California NanoSystems Institute (CNSI) and Materials Research Laboratory (MRL) at the University of California- Santa Barbara. The MRL Central Facilities are supported by the MRSEC Program of the NSF under Award No. DMR 1121053; a member of the NSF-funded Materials Research Facilities Network (www.mrfn.org).

## REFERENCES

[1] Segalman, R. A., Mat Sci Eng R 48, 191 2005.
[2] Park, C.; Yoon, J.; Thomas, E. L., Polymer 44, 6725 2003.
[3] Herr, D. J. C., J Mater Res 26, 122 2011.

Proc. of SPIE Vol. 8680 868016-7

[4] Takahashi, H.; Laachi, N.; Delaney, K. T.; Hur, S.-M.; Weinheimer, C. J.; Shykind, D.; Fredrickson, G. H., Macromolecules 45, 6253 2012.

[5] Hammond, M. R.; Cochran, E.; Fredrickson, G. H.; Kramer, E. J., Macromolecules 38, 6575 2005.

[6] Mishra, V.; Fredrickson, G. H.; Kramer, E. J., ACS nano 6, 2629 2012.

[7] Park, S.; Stoykovich, M. P.; Ruiz, R.; Zhang, Y.; Black, C. T.; Nealey, P. F., Adv. Mater. 19, 607 2007.

[8] Stewart, M. D.; Johnson, S. C.; Sreenivasan, S. V.; Resnick, D. J.; Willson, C. G., J Microlith Microfab 42005.

[9] Bosse, A. W.; Garcia-Cervera, C. J.; Fredrickson, G. H., Macromolecules 40, 9570 2007.

[10] Fredrickson, G. H., The Equilibrium Theory of Inhomogeneous Polymers; Clarendon Press: Oxford, 2006.

[11] Fredrickson, G. H.; Ganesan, V.; Drolet, F., Macromolecules 35, 16 2002.

[12] Hur, S.-M.; Garcia-Cervera, C. J.; Kramer, E. J.; Fredrickson, G. H., Macromolecules 42, 5861 2009.

[13] Matsen, M. W.; Bates, F. S., Macromolecules 29, 1091 1996.