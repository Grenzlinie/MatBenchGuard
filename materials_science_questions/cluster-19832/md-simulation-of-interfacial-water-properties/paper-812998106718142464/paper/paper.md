![](./images/812998106718142464_1.jpg)

Subscriber access provided by Kaohsiung Medical University

New Concepts at the Interface: Novel Viewpoints and Interpretations, Theory and Computations

# Molecular dynamics study on wettability of poly(vinylidene fluoride) (PVDF) crystalline and amorphous surfaces

Masahiro Kitabata, Tseden Taddese, and Susumu Okazaki

Langmuir, Just Accepted Manuscript • DOI: 10.1021/acs.langmuir.8b02286 • Publication Date (Web): 06 Sep 2018

Downloaded from http://pubs.acs.org on September 7, 2018

Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

![](./images/812998106718142464_2.jpg)

is published by the American Chemical Society. 1155 Sixteenth Street N.W.,
Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works
produced by employees of any Commonwealth realm Crown government in the course
of their duties.

# Molecular dynamics study on wettability of poly(vinylidene fluoride) (PVDF) crystalline and amorphous surfaces

Masahiro Kitabata, $^{\dagger,\ddagger,\P}$ Tseden Taddese, $^{\ddagger}$ and Susumu Okazaki$^{*, \ddagger}$

$^\dagger$Research Association of High-Throughput Design and Development for Advanced Functional Materials (ADMAT), 2266-98 Anagahora, Shimo-Shidami, Moriyama-Ku, Nagoya, Aichi, 463-8560, Japan

$^\ddagger$Department of Materials Chemistry, Graduate School of Engineering, Nagoya University, Furo-Cho, Chikusa-Ku, Nagoya, Aichi, 464-8603, Japan

$^\P$Advanced Materials Research Laboratories, Toray Industries, Inc., 2-1 Sonoyama 3-Chome, Otsu, Shiga, 520-0842, Japan

E-mail: okazaki@chembio.nagoya-u.ac.jp

Phone: +81 (0)52 7895828

## Abstract

The present study investigates the effect of microscopic structure on the wettability of Poly(vinylidene fluoride) (PVDF) surfaces using all-atom molecular dynamics (MD) simulations of water droplets brought into contact with both crystal and amorphous PVDF surfaces. For each case computations were performed using five different droplet diameters and the corresponding water droplet contact angles $\theta$ were obtained. Using the fact that the cosine of these contact angles for both surfaces are inversely proportional to the radius of the droplet contact surface $(r_{dr}(Z_0))$, the contact angle $\theta_\infty$ of

the macroscopic water droplet was obtained by extrapolating $\cos\theta$ to $1/r_{dr}(Z_0)=0$.

The estimated values of $\theta_\infty$ on the crystal and amorphous surfaces were $96^\circ$ and $86^\circ$, respectively, showing that the amorphous surface is less hydrophobic than the crystal surface. The contact angle of the crystalline/amorphous mixed surface was estimated using the Cassie equation to be $91^\circ$. This value agrees well with experimental measurement of the water contact angle on the PVDF film. Furthermore, the interaction energy, interface structure and electrostatic potential were analyzed to clarify the reason for the lower hydrophobicity of the amorphous surface. This surface interacts more favorably with water than the crystal surface. Such an interaction reduces the excess free energy (interfacial tension) at the PVDF and water interface and makes the amorphous surface less hydrophobic. The amorphous interfacial region contains more water molecules than the crystal one and water molecules are oriented toward the PVDF. This interface structure makes water strongly interact with the PVDF.

## Introduction

Incorporation of synthetic membranes into industrial processes, such as gas/liquid and liquid/liquid separation, has been increasing over the past 20 years.$^1$ This has various advantages over other production methods such as distillation, for example a reduction in energy consumption and ease to scale up due to their modular structure. The two types of synthetic membranes used in the separation process are inorganic and polymer membranes, and one of the most commonly used polymeric membrane is poly(vinylidene fluoride) (PVDF).

PVDF is a semi-crystalline polymer widely used in industrial applications because it has desirable characteristics such as high mechanical strength, chemical stability and high heat resistance. PVDF has mainly been applied as a piezoelectric material$^2$ by making use of the ferroelectricity of the crystal, and as a separation membrane$^1$ due to its porous structure. Examples of PVDF membrane applications in industrial processes include in the water treatment process$^1$ , the separation of acid gases, such as $\text{CO}_2{}^3$ and $\text{H}_2\text{S}^4$ , and as a

separator in lithium-ion batteries⁵.

Wettability is a well-known factor that determines the separation performance of polymer membranes. A great effort has therefore been made to improve this performance by changing the wettability of PVDF membrane surfaces both chemically and physically.¹,⁶⁻¹¹ In water treatment processes, many trials have been made to improve the wettability⁶⁻⁸ of hydrophobic PVDF membranes in order to suppress fouling, a phenomenon where organic compounds, such as proteins, contained in treated water are absorbed on the surface. In addition, an increase in wettability would prevent deterioration of the separation function due to long-term use of the membrane. In contrast, high wettability may reduce the membrane efficiency in other applications because of the decrease in the mass mobility, and thus great efforts have also been made to reduce the wettability of the membrane in these cases.⁹⁻¹¹

In a robust approach to characterize the wettability of the polymer surface, a water droplet is put on the membrane or film surface and the contact angle between the two is measured. This contact angle strongly depends on the chemical properties and the roughness of the surface.¹² Since it is hard to produce chemically uniform and smooth surfaces of polymer membranes and films, it is difficult to experimentally analyze how certain microscopic surface structures influence the contact angle. In order to clarify this, studies using molecular dynamics (MD) simulations have been conducted in recent years.¹³⁻²⁵ Many previous studies have revealed the relation between the contact angle of droplets, composed of Lennard-Jones (LJ) particles¹⁴⁻¹⁷ and water (including aqueous solutions),¹⁸,¹⁹ and the interaction between uniform solid walls and the droplet. Several studies have also reported²⁰⁻²³ the contact angle on polymer surfaces, which is a more realistic system than the uniform solid wall. However, the number of studies of the contact angle on the polymer is smaller than that on the uniform solid surface. In the case of PVDF surfaces, Darvishi and Foroutan²³ computed the contact angle of water and oil on an ideal amorphous surface constructed of short PVDF chains. To the best of our knowledge, only this molecular simulation study on the wettability of PVDF membranes has been reported and no work on PVDF crystal surfaces has been undertaken.

This is important since bulk PVDF is a semi-crystalline polymer and the surface of the real PVDF membrane or film is known to be a mixture of crystal and amorphous surfaces. Due to the lack of research on this topic, the effect of microscopic structure of PVDF (crystal and amorphous surfaces) on its wettability is not well understood.

Contact angle calculations on surfaces of inorganic materials have also been reported. $^{24,25}$ In many contact angle calculations found in the literature, the motion of the substrate molecules are treated as frozen. This means that the influence of structural relaxation of the substrate surface, due to thermal motion and interaction with droplet molecules, is not taken into account.

The contact angle of macroscopic droplets can be determined by the balance of interfacial tension at liquid-vapor (lv), solid-liquid (sl), and solid-vapor (sv) interfaces following the Young's equation,

$$
\gamma_{s v}=\gamma_{l v} \cos \theta_{\infty}+\gamma_{s l} \tag{1}
$$

where $\theta_{\infty}$ is the contact angle of the macroscopic droplet. However, it is well known from MD simulations that the contact angle of microdroplets depends largely on their size $^{15,16,19,20,24,25}$ , which is typically of the order of nanometers. Therefore, in order to investigate the influence of the microscopic surface state on the macroscopic contact angle, it is necessary to consider the droplet size. The modified Young's equation $^{26,27}$ that takes into account this size dependence is given by

$$
\cos \theta=\cos \theta_{\infty}-\frac{\tau}{\gamma_{l v}} \frac{1}{r_{d r}} \tag{2}
$$

where $\theta$ is the contact angle of a microdroplet, $\tau$ is the line tension, and $r_{d r}$ is the radius of a contact surface between the droplet and substrate. Several studies have obtained the macroscopic contact angle by combining equation (2) with the microdroplet contact angle calculation from MD simulation for various droplet sizes. $^{16,20,25}$ Many of these studies have shown the droplet size dependence of the contact angle on a simple solid surface with LJ potential. Hirvi and Pakkanen $^{20}$ reported the droplet size dependence of the contact angle

of water on polymer surfaces with frozen molecular motion.

The purpose of this work is to reveal the influence of the microscopic structure on the wettability of PVDF membranes or film surfaces at a molecular level. To do this, we conducted all-atom MD simulations of water droplets on PVDF crystal and amorphous surfaces and analyzed the relation between microscopic structure and the wettability at a molecular level. In order to make the polymer surface closer to the real system, the motion of PVDF molecules was not fixed and the relaxation of the surface structure was incorporated. Five water droplets of different sizes were prepared and the droplet size dependence, within the order of nm, on the micro contact angle were evaluated. Furthermore, the contact angle of the macroscopic droplet was calculated using equation (2) and the wettability of the ideal crystal and amorphous surface was discussed. We also conducted MD simulations of crystal and amorphous PVDF/water/vacuum slab systems. Interaction energy, structure and electrostatic potential analyses of these systems were carried out. The results revealed that the change in solid-liquid interfacial tension coming from the difference in the interface structure between the crystal and amorphous surfaces caused the difference in hydrophilicity (wettability).

# METHODOLOGY

## Computational models

To study the wettability of PVDF we conducted MD simulations of water droplets on crystal and amorphous PVDF surfaces and calculated the contact angle by analyzing their trajectories. Water droplets with different diameters $D$ ($D = 4$ nm, 5.5 nm, 7 nm, 10 nm and 13 nm) were performed. Table 1 gives a summary of the different systems and Figure 1 shows an example of the initial configuration used for this contact angle calculation. In addition, we performed MD calculations for PVDF/water/vacuum slab both for crystal and amorphous PVDF. The difference between the PVDF/water/vacuum slab systems and the contact angle

calculation systems is that, in the former, the curvature of the gas-liquid interface is zero and there is no three-phase interface of vapor-liquid-polymer at the contact line.

In order to construct these systems, the all-atom force field parameters proposed by Lachet et al. $^{28}$ were adopted for PVDF, where the OPLS type function $^{29}$ was used for bond, angle, dihedral, LJ and electrostatic potentials. The TIP4P/2005 $^{30}$ water model was chosen since it can reproduce interfacial tension well. All the MD simulations were performed using GROMACS 5.1.4, $^{31}$ with the VMD $^{32}$ software package used to visualize the structures.

For the contact angle calculation, the crystal or amorphous PVDF was placed at the bottom of a rectangular parallelepiped unit cell and a water droplet was placed on the surface. Furthermore, an LJ wall was installed to prevent water molecules from adhering to the backside of the PVDF through the periodic boundary condition and to prevent the PVDF substrate from curving due to thermal motion. This was done by placing two layers of 12-6 LJ particles having the fcc (face centered cubic) (100) surface structure on the top of the basic cell. The LJ parameters applied were $\sigma_{\text{wall}} = 0.35$ nm and $\varepsilon_{\text{wall}} = 0.0657$ kJ/mol.

Once an equilibrated system is set up as described in the following section, MD simulations with $NVT$ ensemble were conducted, solving the equation of motion with the time step of $dt = 2$ fs, for both the contact angle calculation and the planar interface system. Periodic boundary conditions were applied in all simulation directions. The Nosé-Hoover thermostat $^{33}$ was used to maintain the temperature at 298.15 K with the coupling time constant $\tau_{T}$ = 1 ps. Short-ranged LJ interactions were handled using the switch function $^{34}$ implemented in GROMACS from 1.0 nm to the cutoff 1.2 nm, while the long-range Coulombic interactions were computed with the Particle Mesh Ewald $^{35}$ (PME) method. Interaction in the real space was cut off at 1.2 nm, and the reciprocal space calculation used a sixth-order B-spline and grids with side length of 0.12 nm or lower. The neighbor lists were generated with 1.2 nm cut-off distance and were updated every 10 MD steps. The bond lengths of water and PVDF were constrained by the SETTLE $^{36}$ and LINCS $^{37}$ algorithms, respectively. To keep the LJ wall particles in place, a position restraint was applied using a harmonic potential.

6
ACS Paragon Plus Environment

### Preparation of initial configuration

To construct the PVDF crystal surface we selected the (020) plane of $\alpha$-phase crystal structure. This is because spherulites composed of lamella $\alpha$-phase are the main component of the crystalline phase of the PVDF film, though there exist other crystal polymorphs $\beta$- and $\gamma$-phase$^{2,38}$ crystal. Furthermore, the spherulites consist of mainly lamella structures with their lateral (020) plane growing in the radial direction.$^{39,40}$ Therefore, in this study, the $\alpha$(020) plane was prepared utilizing the Materials Studio 2017 R2 software package$^{41}$ and the X-ray diffraction data by Hasegawa *et al.*$^{42}$ We used $a = 0.4985$ nm, $b = 0.964$ nm, $c = 0.482$ nm as lattice constants instead of $a = 0.496$ nm, $b = 0.964$ nm, $c = 0.462$ nm proposed by Hasegawa *et al.* This is because the crystal structure collapsed when combining the force field parameters with the experimental lattice constants, as shown in section 1 of the Supporting Information. For this reason, we selected optimum lattice constants to keep the $\alpha$-type crystal structure, which is close to the stable experimental structure.

The PVDF amorphous surface was constructed following the same steps taken by Hirvi and Pakkanen.$^{20}$ A PVDF film was prepared by replicating an equilibrated bulk system of PVDF in the $X$ and $Y$ directions of the simulation box so as to reproduce the experimental density in a melt state ($T = 493.15$ K, $P = 1$ bar, melting point of PVDF is $444.15$ K$^{43}$). The PVDF amorphous surface was prepared by gradually placing an LJ wall in the upper and lower side of the film while maintaining PVDF at the melting temperature (details of modeling are given in the Supporting Information, section 2). The resulting PVDF amorphous surface was quite smooth, meaning changes in contact angle due to surface roughness can reasonably be ignored. The LJ walls were placed to spatially confine the PVDF chains due to the repulsive force from LJ particles. Therefore, a very small value (0.0657 kJ/mol) was chosen for the value of $\varepsilon_{\text{wall}}$. The influence of the attractive interaction on the structure of PVDF surfaces can be negligible when such a small value is used. Thus, the surface properties of the present PVDF does not depend on LJ parameters.

In the case of the water droplets, the molecules are randomly placed in a sphere with

diameter $D$ using the packmol software package⁴⁴ so that the density is $1000\ \text{kg/m}^3$. LJ wall particles were also arranged using the packmol package. In order to reduce calculation time, the size of the PVDF crystal and amorphous models was varied according to the size of the water droplet. The sizes of the unit cells for the contact angle calculations are summarized in Table 1.

In the contact angle calculations shown in Table 1, the initial structures obtained by packmol were structurally optimized using the method of steepest descent. Next, the MD simulation in the $NVT$ ensemble was carried out where the temperature was raised gradually from 0 K to 278.15 K, and the droplet was brought into sufficient contact with the PVDF surface. The reason for this stepwise temperature rise after the structural optimization is to obtain an equilibrium droplet state in a short simulation time. The duration of this rise depended on the system size, for example being set to 10.7 ns for a droplet size of $D=13\ \text{nm}$ (largest system) and 0.7 ns for $D=4\ \text{nm}$ (smallest system). Details of the heating process are given in section 3 of the Supporting Information. MD simulations were conducted for 20 ns for the $D=4\ \text{nm}$, $5.5\ \text{nm}$ and $7\ \text{nm}$ droplet systems, and for 40 ns for the $D=10\ \text{nm}$ and $13\ \text{nm}$ droplet systems. The last 15 ns of the trajectories were used to calculate the contact angle. The simulation time was determined from the time when the radius of the contact surface $r_{dr}$ between the water droplet and the PVDF surface reached equilibrium. This depends on droplet size, and details of the relationship are shown in section 4 of the Supporting Information. In addition, to examine the dependence of the initial structure on the contact angle calculation, the above MD simulations were performed starting from four independent initial configurations and the resulting contact angles were evaluated. These four independent initial configurations were prepared as follows. The initial configurations of the amorphous surface were obtained by moving the LJ walls closer to the surface four times independently. Four kinds of initial water droplet configurations were also obtained by setting the position and direction of the water molecules arbitrarily. By combining these structures, four independent initial configurations used for calculating the contact angle on

the amorphous surface were constructed. On the other hand, in the crystal surface system, four initial configurations were obtained by changing only the initial configuration of water droplets, since the surface structures were identical in this case.

In the planar interface system shown in Table 2, the initial structure, set up using packmol, was first subjected to structural optimization using the steepest descent method. Next, MD simulation in the $NVT$ ensemble at $T = 298.15$ K was performed for 20 ns. The interaction energy, the number density distribution, the orientation of the dipole moment of water, and the electrostatic potential were analyzed using the trajectory for the last 15 ns.

## Calculation of contact angle

The contact angle was obtained using the method proposed by Ingebrigsten and Txvaerd¹⁵ (hereinafter referred to as the IT method) from MD simulation of water droplets without assuming spherical shapes. The initial stage of this method involves the application of the Stillinger criterion⁴⁵ to judge whether one water molecule is located in the droplet or not. If the distance between the mass centers of single water molecules in the system is within $1.5\sigma_O$, where $\sigma_O$ is an LJ size parameter of the O atom of water, then it is assumed to be in the liquid state. At certain simulation time, a small number of water molecules are adsorbed on the PVDF surface and form small droplets. In this case, the droplet with the largest number of water molecules was used for the contact angle calculation. The center of gravity $(X_{\rm g},\ Y_{\rm g},\ Z_{\rm g})$ of the droplet was then obtained, which was later used for the contact angle calculation.

Next, the water density distribution in the direction of the $Z$-axis (normal to the surface) was calculated to determine the contact position $Z_0$ between the droplet and the substrate. Since outside of the droplet is a vacuum, the density of water shows a peak where the substrate and droplet meet, becoming zero at the top of the droplet. However, at any given instant the position of the maximum density is not clearly the contact position, due to the fluctuating nature of the droplet structure caused by thermal motion. In order to avoid this,

$Z_0$ was chosen to be the closest position to the substrate where the water density is greater than 0.9 times its maximum value. Such a choice of $Z_0$ includes some level of arbitrariness, but we have found from reference position trials that 0.9 times the maximum density is optimal. The lateral and radial distance $r_{dr}(Z)$ from the center $(X_{\text{g}}, Y_{\text{g}}, Z_0)$ to the gas-liquid interface was obtained by fitting the calculated lateral water density distribution to a function of the form

$$
\rho(r, Z)=\frac{1}{2}(\rho_{l}+\rho_{g})-\frac{1}{2}(\rho_{l}-\rho_{g}) \tanh \left(\frac{2(r-r_{dr}(Z)))}{d}\right) \tag{3}
$$

Here, $r_{dr}(Z)$ was obtained as a fitting parameter in the equation for each $Z$. Then, two $r_{dr}(Z)$ values were obtained at $Z=Z_0$ and $Z_0+\Delta z$. Using these two values $r_{dr}(Z_0)$ and $r_{dr}(Z_0+\Delta z)$, the contact angle was determined using

$$
\theta=\lim_{\Delta z \to 0} \tan^{-1} \left(\frac{\Delta z}{r_{dr}(Z_0+\Delta z)-r_{dr}(Z_0)}\right) \tag{4}
$$

According to this equation, the value of $\Delta z$ should be as small as possible. However, if we adopt a smaller value than the size of the water molecule we lose the physical meaning of the contact angle. Therefore, in this work, we applied $0.9\sigma_O$ for $\Delta z$ as in the investigation by Ingebrigsten and Txvaerd. $^{15}$ The calculated contact angle was observed to depend on $\Delta z$ for values of $\Delta z$ greater than $1.2\sigma_O$, but for $\Delta z$ smaller than $1.2\sigma_O$ was approximately constant. Thus, the value of $0.9\sigma_O$ was adopted in our calculations.

## Results

### Contact angle of water on PVDF surfaces

Contact angle calculations of water droplets on PVDF surfaces were conducted as described in the methodology section. Figure 2 (a) shows the calculated contact angle of water droplets of various sizes on the PVDF crystal and amorphous surfaces. Figure 2 (b) shows the rela-

tionship between $\cos\theta$ and $1/r_{dr}(Z_0)$ for both the crystal and the amorphous surfaces. In both cases, the value of $\cos\theta$ decreases as the water droplet size increases, and is found to be proportional to $1/r_{dr}(Z_0)$, in agreement with the modified Young's equation (2). Furthermore, this result is consistent with previous MD calculations$^{16,17,20,24,25}$ that have found the same proportionality in various systems. Thus, we can obtain the macroscopic contact angle $\theta_\infty$ by extrapolating $\cos\theta$ to $1/r_{dr}(Z_0)=0$. The macroscopic contact angle $\theta_\infty$ and the line tension $\tau$ obtained for the crystal and amorphous surfaces from the regression line and modified Young's equation were $96^\circ$ and $-3.6\times10^{-11}$ N for the crystal surface and $86^\circ$ and $-6.2\times10^{-11}$ N for the amorphous surface.

Influence of the PVDF structure on its wettability is clearly found. The value of $\cos\theta$ on the amorphous surface for all droplet sizes is larger than that on the crystal surface. Furthermore, the value of $\cos\theta_\infty$ for the macroscopic water droplet is also larger on the amorphous surface than that on the crystal surface. Hence, the contact angle $\theta_\infty$ of the macroscopic water droplet on the amorphous surface is smaller. Negative line tensions were obtained in this calculation, which is unexpected from a purely thermodynamics point of view because negative line tension destabilizes the liquid/vapor/solid interface. However, simulations$^{15-17}$ and experiments$^{46-48}$ have reported both positive and negative line tensions, with various reasons being discussed. The main explanation is that $\tau$ in equation (2) is not a pure line tension introduced by thermodynamics but is a correction term to account for the size dependence of the droplet$^{15}$.

As mentioned before, PVDF is a semi-crystalline polymer with about 50% crystallinity, meaning the actual PVDF film surface is expected to consist of mixed crystal/amorphous regions. In this work, however, the contact angles were only calculated for the pure surfaces, with $\theta_\infty$ (crystal) corresponding to 100% crystallinity and $\theta_\infty$ (amorphous) to 0%. This is due to practical difficulties of modeling such mixed surfaces in MD simulations, with the calculated contact angles being strongly dependent upon the size of the computational domain, which is necessarily smaller than the real system. The angle is also sensitive to

the way the surface is constructed, for example the lateral arrangement of the crystal and amorphous domains. These issues, together with the fact that our current understanding of the interfacial region is very limited, warrant further independent investigation. Nevertheless, the information gathered from the pure surfaces can be used to deduce the contact angle of the crystal/amorphous mixed surfaces using the Cassie equation⁴⁹,

$$
\cos \theta_{f}=A^{1} \cos \theta^{1}+A^{2} \cos \theta^{2} \tag{5}
$$

where $\theta^{f}$ is the contact angle on the composite surface, superscripts 1 and 2 represent the type of the material constituting the composite surface, $A^{1 \text { or } 2}$ is the area ratio, and $\theta^{1 \text { or } 2}$ is the contact angle on the surface of pure material 1 or 2. If materials 1 and 2 represent crystalline and amorphous surfaces, respectively, the macroscopic contact angle of the mixed surface can easily be estimated from equation (5). Assuming the degree of crystallinity of the PVDF film surface to be $50 \%$ (meaning $A^{\text{crystal}} = A^{\text{amorphous}} = 0.5$), $\theta^{f}$ was calculated to be $91^{\circ}$.

In the literature, several different measurements of the contact angle of water droplets on a normal PVDF film have been reported. For example, the measured contact angles were $82^{\circ}$ by $W u$ et $a l .{ }^{50}, 86^{\circ}$ by Petermann et al. $^{51}$, and $90^{\circ}$ by Vasile et al. ${ }^{52}$ Thus, the calculated $\theta^{f}$ in this work agrees well with the experimental range. Now, it is interesting to note that these experimental values were closer to $\theta_{\infty}$ (amorphous) than $\theta_{\infty}$ (crystal) suggesting that, in the real PVDF film, the surface is more amorphous. In other words, the ratio of the crystal surface may actually be lower than $50 \%$. Crystallinity of the film surface in crystalline $^{53,54}$ or semi-crystalline $^{55}$ polymers has been reported based on grazing incidence X-ray diffraction (GIXD) measurements, where it is concluded that the crystallinity of the outermost surface is lower than that in the bulk. Although the crystallinity of the PVDF film surface has not yet been reported, the present situation may be similar.

# Interfacial tension between water and PVDF surfaces

The interfacial tension $\gamma_{sl}$ (interfacial excess free energy per unit area), which represents the affinity between water and PVDF at the interface, can be obtained by applying the calculated contact angle to equation (1). Using the experimental air/PVDF interfacial tension of $\gamma_{sv} = 33.2\mathrm{mJ/m^2}^{50}$ and the air/water interfacial tension of $\gamma_{lv} = 69.3\ \mathrm{mJ/m^2}$ (TIP4P/2005 water)$^{56}$ the value for $\gamma_{sl}$ (for $A^{\text{crystal}} = A^{\text{amorphous}_\text{S}} = 0.5$) was estimated to be $34\ \mathrm{mJ/m^2}$.

As stated in the previous section, it is clear that the contact angle of water droplets on the amorphous surface is smaller than that on the crystal surface, which indicates that the PVDF amorphous surface is less hydrophobic than the crystal analogue. The difference in hydrophobicity found for these surfaces can also be estimated using equation (1), which gives the values of $\gamma_{sl}$ (crystal) and $\gamma_{sl}$ (amorphous) as $40\ \mathrm{mJ/m^2}$ and $28\ \mathrm{mJ/m^2}$, respectively. Finally, the experimental value for the real PVDF surface was used for the interfacial tension for both amorphous/air and crystal/air interfaces. This is because the interfacial tension of these interfaces is not expected to be so different from each other since the density of air in contact with the solid surface is low.

# Discussion

In order to find the molecular origin of the hydrophobicity differences between the crystal and amorphous surfaces, we examined the systems in which the PVDF film is fully covered by water molecules (crystal/water/vacuum and amorphous/water/vacuum). The interaction energy, the number density distribution, the orientation of the dipole moment of water, and the electrostatic potential were analyzed based on the trajectories from MD simulations as described in the methodology section.

## Interaction energy

First, we analyzed the difference in intermolecular interaction energy between crystal/water/vacuum and amorphous/water/vacuum by calculating the non-bonded energy with 2.0 nm cutoff, based on trajectories obtained from MD simulations. The total interaction energy of the whole system and the interaction energy between PVDF and water are shown in Table 3. Since Coulombic interactions in the reciprocal space calculated by the PME method cannot be divided into intermolecular interactions, we calculated these interactions directly with a cutoff scheme. Furthermore, since the size of the crystal and amorphous systems is different, the total interaction energy and the PVDF-water interaction energy were normalized by the volume of the system and the area of the interface, respectively.

In both crystal and amorphous systems, the total interaction energy is favorable, where the contribution from Coulombic interactions is large. The magnitude of the interaction energy is almost the same for both systems. In the case of the PVDF-water interaction energy, it is also favorable for both crystal and amorphous systems. However, in contrast to the total interaction energy, the magnitude of the PVDF-water interaction energy is significantly different between the crystalline and amorphous systems, with the amorphous surface having more favorable interactions with water than the crystal surface. Thus, the interactions between PVDF and water reduce the excess free energy (interfacial tension) at their interface, making the amorphous surface less hydrophobic. In addition, the difference in the PVDF-water interactions in the crystal and amorphous systems is caused mainly by the Coulombic interactions.

## Density distribution and orientation of water

Next, we discuss the difference in equilibrium structure between crystal/water/vacuum and amorphous/water/vacuum systems by analyzing the number density distribution in space and the orientation of the dipole moment of water. A snapshot of the final structure of the crystal PVDF/water/vacuum system and the corresponding number density distribution of

atoms and the orientation of water dipole moment for this system are shown in Figure 3.
The same results for the amorphous PVDF/water/vacuum system are shown in Figure 4.
The orientation of water dipole moment is defined by $\langle\cos\phi\rangle$, the ensemble average of the cosine of the angle formed between the dipole moment and the $Z$-axis, where the $Z$-axis is chosen to be normal to the surface. The probability distribution of orientation of the water dipole moment is also shown in Figure 5 for a few particular $Z$ values.

Focusing on the number density of O and H atoms of water on the crystal surface, shown in Figure 3(b), a sharp peak is observed near the outermost surface ($Z = 2.9$ nm) of PVDF. However, in the case of the amorphous surface, such a peak is not found (Figure 4(b)). Thus, the number density of water near the interface shows a rapid increase on the crystal surface but a relatively slow increase on the amorphous surface. This indicates that on the crystal surface water is not able to penetrate into the PVDF film and forms a very thin and clear interface region. In contrast, water is able to form a thick interfacial region in the amorphous PVDF.

Formation of the thick interfacial region suggests water penetration into PVDF, but it may originate from the roughness of the amorphous PVDF surface. In order to confirm the penetration of water inside the PVDF, the detailed interface structure was analyzed by the Connolly surface method$^{57}$ . The relationship between the interface structure and the positions of water molecules is given in section 5 of the Supporting Information. Many water molecules in the interfacial region are found in dimples produced by the roughness of the amorphous surface. However, several water molecules also exist below the Connolly surface in the PVDF region. Such an analysis of an interface structure is known as the "instantaneous interface" approach and has also been applied to other polymer interfaces.$^{58}$

In the amorphous system, there are many water molecules that are contacted with PVDF molecules at the interface, and this interfacial structure makes the PVDF-water interaction stronger than in the crystal system. The interface positions between PVDF and water given by the Gibbs dividing surface determined from the density distribution of water molecules

were 2.9 nm and 2.7 nm for the crystal and the amorphous surfaces, respectively.

Orientation of the water dipole moment also shows a clear difference between crystal and amorphous surfaces. For the case of the crystal surface, shown in Figure 3 (c), we focus our attention on the orientation at $Z = 7.1$ nm (position I: bulk region) and $Z = 2.9$ nm (position II: interface). As can be seen, the value of $\langle\cos\phi\rangle$ is almost zero at position I, suggesting that the dipole moment of water in the bulk has a random orientation. As shown by the red line in Figure 5(a), the probability distribution of $\cos\phi$ at position I is almost constant over the range from -1 to 1. This implies that water has a completely random orientation. In contrast, a large peak is found at position II, the interfacial position between PVDF and water defined by the Gibbs dividing surface. The value of $\cos\phi$ at this peak corresponds to the angle $\phi$ of $79^\circ$. The distribution of $\cos\phi$ at position II has large values at $\cos\phi > 0$, as shown by the black line in Figure 5 (a). Thus, water molecules on the crystal surface tend to orient O atoms towards PVDF and H atoms towards the bulk water.

Orientation of the dipole moment of water on the amorphous surface is presented in Figure 4 (c), with labels of the orientation at $Z = 7.1$nm (position i: bulk region), $Z = 2.9$nm (position ii: near the interface in the water side) and $Z = 2.3$nm (position iii: near the interface in the PVDF side). The value of $\langle\cos\phi\rangle$ at position i was almost zero, similar for position I in the crystal, showing that water molecules have random orientations in the bulk. A small peak was observed at position ii ($Z = 2.9$nm) which is located near the interface ($Z = 2.7$ nm) in the water side. The distribution of orientations at position ii shown by the black line in Figure 5(b), is similar to that of the bulk water region (position i), which indicates that the orientation of the dipole moment of water is almost random. At position iii, a large peak is observed and the averaged value of $\cos\phi$ shows that the orientation of the dipole moment of water is $98^\circ$. Furthermore, the distribution of the orientation of water dipole moments at position iii has large values in the region of $\cos\phi < 0$, as shown by the blue line in Figure 5(b). This implies that a lot of water molecules on the amorphous surface orient the dipole moment toward the PVDF side. A small peak located at $Z = 1.8$ nm is

also observed in Figure 4 (c), but this is thought to be noise coming from one water molecule that penetrates into the region.

Particular orientations of the dipole moment of water are also observed at the gas-liquid interface on both surfaces. We don't discuss this finding in detail since the gas-liquid interface is not the primary focus of this research, but several studies have reported such findings⁵⁹,⁶⁰ and our present result are consistent.

Based on the findings explained above, a schematic picture may be presented for the orientation of water molecules at the crystal and amorphous PVDF interface, shown on Figure 6.

## Electrostatic potential

As discussed above, the number density distribution of atoms and the orientation of water dipole moments at the interface are different between the crystal and amorphous surfaces. Molecules with a large dipole moment, such as water and PVDF, may produce strong electrostatic potential. The electrostatic potential $\psi$ can be estimated by doubly integrating the charge density distribution $\rho_e(Z)$ over the $Z$ coordinate as⁶⁰

$$
\Delta \psi=\psi\left(Z_{2}\right)-\psi\left(Z_{1}\right)=-\frac{1}{\varepsilon_{0}} \int_{Z_{1}}^{Z_{2}} \int_{Z_{1}}^{Z^{\prime}} \rho_{e}\left(Z^{\prime \prime}\right) d Z^{\prime \prime} d Z^{\prime} \tag{6}
$$

where $\Delta \psi$ is the electrostatic potential difference at $Z_2$ with respect to the reference position $Z_1$ and $\varepsilon_0$ is the dielectric constant of the vacuum. The value of $\Delta \psi$ can be obtained by direct numerical integration of the charge density distribution $\rho_e(Z)$. In the present study, the reference point $Z_1$ was chosen to be 18 nm, which represents a gas phase (vacuum) region. The calculated electrostatic potential on the crystal and amorphous surfaces is presented in Figure 7 and Figure 8, respectively.

Figure 7 shows that both PVDF and water have the characteristic charge density for the crystal PVDF. The PVDF has large oscillatory charge densities due to its crystal structure.

In contrast, water in the bulk region has almost zero charge density because of the random orientation in this region. However, water in the interface region has a high charge density due to the dipole orientation. The electrostatic potential produced by the charge density distribution was 0 V from the reference point ($Z =$18 nm) to around $Z =$12 nm, but suddenly changes to -0.56 V at the gas-liquid interface region around $Z =$11 nm. After that, it showed a nearly constant electrostatic potential up to the solid-liquid interface region, before decreasing again rapidly to -0.94 V at the solid-liquid interface, followed by an immediate rise to +0.81 V on the PVDF surface. A number of simulation results⁵⁹⁻⁶¹ for the electrostatic potential at the gas-liquid interface of water have been reported and our results at the gas-liquid interface corresponds well to these values. For example, values of -0.55 V and -0.50 V were reported for SPC/E⁶⁰ and TIP4P⁶¹ water-gas interfaces, respectively. An abrupt change of the electrostatic potential from -0.94 V to +0.81 V at the solid-liquid interface is due to the preferential orientations of water together with the crystal structure of PVDF. Since the crystal PVDF produces a large positive electrostatic potential, the negative side (O atom side) of the dipole moment of water is oriented toward the crystal surface. As a result, water contributes a large negative value to the electrostatic potential. This abrupt change of the electrostatic potential from negative to positive values is found clearly in the interface region.

As shown in Figure 8, the charge density distribution for the amorphous surface averages out to give a very smooth form compared with the crystal surface. This is due to the relatively random structure of PVDF and water in the amorphous surface region. The electrostatic potential in the gas phase was almost the same as the crystal surface. Tendency of the potential to change from almost zero to a negative value at the gas-liquid interface, as well as the change from a negative value to a positive one at the solid-liquid interface, was also qualitatively the same, though the change at the solid-liquid interface was small compared with the crystal surface. The charge density of amorphous PVDF resulted in a positive value of the electrostatic potential, which is similar to the crystal surface, though it was less than

1/4 of the crystal surface potential. We mentioned earlier that the dipole moment of water is oriented to the PVDF at the amorphous interface. Since the amorphous PVDF surface produces only small positive electrostatic potential, it is not necessary to preferentially orient the dipole moment of water to the bulk water side. Instead, more water molecules get closer with PVDF to interact with it directly, which gives an enthalpy gain at the interface.

# CONCLUSIONS

The effect of microscopic structure on the wettability of Poly(vinylidene fluoride) (PVDF) surface has been investigated using all-atom molecular dynamics (MD) simulations of water droplets in contact with both crystal and amorphous PVDF surfaces. For each surface, computations were performed for droplets with five different diameters, from which corresponding water droplet contact angles $\theta$ were obtained. Since the cosine of these contact angles are inversely proportional to the radius of the droplet contact surface $(r_{dr}(Z_0))$, the contact angle $\theta_\infty$ of the macroscopic water droplet was obtained by extrapolating $\cos\theta$ to $1/r_{dr}(Z_0)=0$. The estimated $\theta_\infty$ value on the crystal and amorphous surfaces were $96^\circ$ and $86^\circ$, respectively, showing that the amorphous surface is less hydrophobic than the crystal surface. Since the real PVDF is a semi-crystalline polymer, the contact angle of the crystal/amorphous mixed surface was estimated using the Cassie equation. The estimated value was $91^\circ$, assuming the crystalline/amorphous ratio on the PVDF film surface was 50% (the same as the crystallinity of the whole film obtained by experiments). This value agrees reasonably well with experimental measurements of the water contact angle on the PVDF film $(82^\circ$ - $90^\circ)$.

As stated above, the PVDF amorphous surface was less hydrophobic than the crystal surface. The microscopic origin of this difference was revealed by MD simulations of systems in which the PVDF film is fully covered by water molecules (crystal/water/vacuum and amorphous/water/vacuum slab). The interaction energy, the number density distribution,

the orientation of water dipole moment, and the electrostatic potential were analyzed based on the MD trajectory. The interaction analysis revealed that the amorphous surface interacts more favorably with water than the crystal surface. This interaction reduces the excess free energy (interfacial tension) at the PVDF and water interface and makes the amorphous surface less hydrophobic. The difference in the PVDF-water interactions between the crystal and amorphous systems may be attributed to their interface structures. In the amorphous system, the number density analysis clearly showed that water molecules and the PVDF molecules form a thick interfacial region. Furthermore, the dipole moment of water is oriented preferentially towards the PVDF side at the interface between the amorphous PVDF and water. Near this interface, more water molecules contact with the amorphous PVDF with strong interactions than at the crystal surface. Therefore, this amorphous interface structure makes water strongly interact with the PVDF.

# Acknowledgement

This paper is based on the research results from a project (P16010) commissioned by the New Energy and Industrial Technology Development Organization (NEDO). We thank Takeshi Aoyagi, National Institute of Advanced Industrial Science and Technology (AIST), and Takashi Honda, Research Association of High-Throughput Design and Development for Advanced Functional Materials (ADMAT), for the fruitful discussions.

# Supporting Information Available

Descriptions of the optimization process of the lattice constants of $\alpha$-crystal PVDF, preparation of PVDF amorphous surfaces, heating process of the droplet, and the change of droplet size with time are presented. Further information of the PVDF/water instantaneous interfaces is also included.

# AUTHOR INFORMATION

## Corresponding Author

*E-mail address: okazaki@chembio.nagoya-u.ac.jp.

## Notes

The authors declare no competing financial interests.

# References

(1) dong Kang, G.; ming Cao, Y. Application and modification of poly(vinylidene fluoride) (PVDF) membranes - A review. *Journal of Membrane Science* **2014**, *463*, 145–165.

(2) Lovinger, A. J. Ferroelectric Polymers. *Science* **1983**, *220*, 1115–1121.

(3) Atchariyawut, S.; Feng, C.; Wang, R.; Jiraratananon, R.; Liang, D. T. Effect of membrane structure on mass-transfer in the membrane gas-liquid contacting process using microporous PVDF hollow fibers. *Journal of Membrane Science* **2006**, *285*, 272–281.

(4) Wang, D.; Teo, W. K.; Li, K. Removal of H2S to ultra-low concentrations using an asymmetric hollow fibre membrane module. *Separation and Purification Technology* **2002**, *27*, 33–40.

(5) Ji, G. L.; Zhu, B. K.; Cui, Z. Y.; Zhang, C. F.; Xu, Y. Y. PVDF porous matrix with controlled microstructure prepared by TIPS process as polymer electrolyte for lithium ion battery. *Polymer* **2007**, *48*, 6415–6425.

(6) Li, N.; Xiao, C.; An, S.; Hu, X. Preparation and properties of PVDF/PVA hollow fiber membranes. *Desalination* **2010**, *250*, 530–537.

(7) Venault, A.; Liu, Y. H.; Wu, J. R.; Yang, H. S.; Chang, Y.; Lai, J. Y.; Aimar, P. Low-biofouling membranes prepared by liquid-induced phase separation of the PVDF/polystyrene-b-poly (ethylene glycol) methacrylate blend. *Journal of Membrane Science* **2014**, *450*, 340–350.

(8) Liu, J.; Shen, X.; Zhao, Y.; Chen, L. Acryloylmorpholine-grafted PVDF membrane with improved protein fouling resistance. *Industrial and Engineering Chemistry Research* **2013**, *52*, 18392–18400.

(9) Kuo, C. Y.; Lin, H. N.; Tsai, H. A.; Wang, D. M.; Lai, J. Y. Fabrication of a high hydrophobic PVDF membrane via nonsolvent induced phase separation. *Desalination* **2008**, *233*, 40–47.

(10) Teoh, M. M.; Chung, T. S. Membrane distillation with hydrophobic macrovoid-free PVDF-PTFE hollow fiber membranes. *Separation and Purification Technology* **2009**, *66*, 229–236.

(11) Lalia, B. S.; Guillen-Burrieza, E.; Arafat, H. A.; Hashaikeh, R. Fabrication and characterization of polyvinylidenefluoride-co-hexafluoropropylene (PVDF-HFP) electrospun membranes for direct contact membrane distillation. *Journal of Membrane Science* **2013**, *428*, 104–115.

(12) Cwikel, D.; Zhao, Q.; Liu, C.; Su, X.; Marmur, A. Comparing contact angle measurements and surface tension assessments of solid surfaces. *Langmuir* **2010**, *26*, 15289–15294.

(13) Hautman, J.; Klein, M. L. Microscopic wetting phenomena. *Physical Review Letters* **1991**, *67*, 1763–1766.

(14) Blake, T. D.; Clarke, A.; De Coninck, J.; de Ruijter, M. J. Contact Angle Relaxation during Droplet Spreading: Comparison between Molecular Kinetic Theory and Molecular Dynamics. *Langmuir* **1997**, *13*, 2164–2166.

(15) Ingebrigtsen, T.; Toxvaerd, S. Contact angles of Lennard-Jones liquids and droplets on planar surfaces. *Journal of Physical Chemistry C* **2007**, *111*, 8518–8523.

(16) Weijs, J. H.; Marchand, A.; Andreotti, B.; Lohse, D.; Snoeijer, J. H. Origin of line tension for a Lennard-Jones nanodroplet. *Physics of Fluids* **2011**, *23*, 1–13.

(17) Zhang, J.; Leroy, F.; Müller-Plathe, F. Influence of contact-line curvature on the evap- oration of nanodroplets from solid substrates. *Physical Review Letters* **2014**, *113*, 1–5.

(18) Surblys, D.; Yamaguchi, Y.; Kuroda, K.; Kagawa, M.; Nakajima, T.; Fujimura, H. Molecular dynamics analysis on wetting and interfacial properties of water-alcohol mix- ture droplets on a solid surface. *Journal of Chemical Physics* **2014**, *140*, 34505.

(19) Santiso, E. E.; Herdes, C.; Müller, E. A. On the calculation of solid-fluid contact angles from molecular dynamics. *Entropy* **2013**, *15*, 3734–3745.

(20) Hirvi, J. T.; Pakkanen, T. A. Molecular dynamics simulations of water droplets on polymer surfaces. *Journal of Chemical Physics* **2006**, *125*.

(21) Fan, C. F.; Cağın, T. Wetting of crystalline polymer surfaces: A molecular dynamics simulation. *The Journal of Chemical Physics* **1995**, *103*, 9053.

(22) Kumar, N.; Manik, G. Molecular dynamics simulations of polyvinyl acetate- perfluorooctane based anti-stain coatings. *Polymer* **2016**, *100*, 194–205.

(23) Darvishi, M.; Foroutan, M. Molecular investigation of oil-water separation using PVDF polymer by molecular dynamic simulation. *RSC Advances* **2016**, *6*, 74124–74134.

(24) Sresht, V.; Govind Rajan, A.; Bordes, E.; Strano, M. S.; Pádua, A. A.; Blankschtein, D. Quantitative Modeling of MoS₂–Solvent Interfaces: Predicting Contact Angles and Exfoliation Performance using Molecular Dynamics. *The Journal of Physical Chemistry C* **2017**, *121*, 9022–9031.

(25) Scocchi, G.; Sergi, D.; D'Angelo, C.; Ortona, A. Wetting and contact-line effects for spherical and cylindrical droplets on graphene layers: A comparative molecular- dynamics investigation. *Physical Review E* **2011**, *84*, 1-8.

(26) Pethica, B. A. The contact angle equilibrium. *Journal of Colloid And Interface Science* **1977**, *62*, 567-569.

(27) Schimmele, L.; Naplórkowski, M.; Dietrich, S. Conceptual aspects of line tensions. *Journal of Chemical Physics* **2007**, *127*, 164715.

(28) Lachet, V.; Teuler, J.; Rousseau, B. Classical Force Field for Hydrofluorocarbon Molec- ular Simulations . Application to the Study of Gas Solubility in Poly (vinylidene fluoride ). *Journal of Physical Chemistry A* **2015**, *119*, 140-151.

(29) Jorgensen, W. L.; Maxwell, D. S.; Tirado-Rives, J. Development and testing of the OPLS All-Atom force field on conformational energetics and properties of organic liq- uids. *Journal of the American Chemical Society* **1996**, *118*, 11225-11236.

(30) Abascal, J. L.; Vega, C. A general purpose model for the condensed phases of water: TIP4P/2005. *The Journal of chemical physics* **2005**, *123*, 234505.

(31) James, M.; Murtola, T.; Schulz, R.; Smith, J. C.; Hess, B.; Lindahl, E. ScienceDirect GROMACS : High performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX* **2015**, *1*, 19-25.

(32) Humphrey, W.; Dalke, A.; Schulten, K. VMD - Visual Molecular Dynamics. *Journal of Molecular Graphics* **1996**, *14*, 33-38.

(33) Hoover, W. G. Canonical dynamics: Equilibrium phase-space distributions. *Physical Review A* **1985**, *31*, 1695-1697.

(34) Abraham, M.; van der Spoel, D.; E. Lindahl, B. H.; the GROMACS development Team, *GROMACS User Manual version 5.1.4*; 2016.

(35) Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.; Pedersen, L. G. A smooth particle mesh Ewald method. *The Journal of Chemical Physics* **1995**, *103*, 8577–8593.

(36) Miyamoto, S.; Kollman, P. A. Settle: An analytical version of the SHAKE and RATTLE algorithm for rigid water models. *Journal of Computational Chemistry* **1992**, *13*, 952–962.

(37) Hess, B.; Bekker, H.; Berendsen, H. J.; Fraaije, J. G. LINCS: A Linear Constraint Solver for molecular simulations. *Journal of Computational Chemistry* **1997**, *18*, 1463–1472.

(38) Martins, P.; Lopes, A. C.; Lanceros-Mendez, S. Electroactive phases of poly(vinylidene fluoride): Determination, processing and applications. *Progress in Polymer Science* **2014**, *39*, 683–706.

(39) Lovinger, A. J.; Wang, T. Investigation of the properties of directionally solidified poly(vinylidene fluoride). *Polymer* **1979**, *20*, 725–732.

(40) Steinhart, M.; Göring, P.; Dernaika, H.; Prabhukaran, M.; Gösele, U.; Hempel, E.; Thurn-Albrecht, T. Coherent kinetic control over crystal orientation in macroscopic ensembles of polymer nanorods and nanotubes. *Physical Review Letters* **2006**, *97*, 1–4.

(41) Materials Studio 2017 R2. Dassault Systemes BIOVIA: San Diego 2017.

(42) Hasegawa, R.; Takahashi, Y.; Chatani, Y.; Tadokoro, H. Crystal Structures of Three Crystalline Forms of Poly(vinylidene fluoride). *Polymer Journal* **1971**, *3*, 600–610.

(43) Ray, S.; Easteal, A. J.; Cooney, R. P.; Edmonds, N. R. Structure and properties of melt-processed PVDF/PMMA/polyaniline blends. *Materials Chemistry and Physics* **2009**, *113*, 829–838.

(44) Mart, L.; Andrade, R.; Birgin, E. G.; Martínez, J. M. Packmol : A package for building

initial configurations for molecular dynamics simulations. *Journal of Computational Chemistry* **2009**, *30*, 2157–2164.

(45) Stillinger, F. H. Rigorous basis of the Frenkel-Band theory of association equilibrium. *The Journal of Chemical Physics* **1963**, *38*, 1486–1494.

(46) Pompe, T.; Herminghaus, S. Three-phase contact line energetics from nanoscale liquid surface topographies. *Physical Review Letters* **2000**, *85*, 1930–1933.

(47) Berg, J. K.; Weber, C. M.; Riegler, H. Impact of negative line tension on the shape of nanometer-size sessile droplets. *Physical Review Letters* **2010**, *105*, 1–4.

(48) Amirfazli, A.; Neumann, A. W. Status of the three-phase line tension: A review. 2004.

(49) Cassie, A. B. D. Contact angles. *Discussions of the Faraday Society* **1948**, *3*, 11.

(50) Wu, S. Calculation of interfacial tension in polymer systems. *Journal of Polymer Science Part C: Polymer Symposia* **1971**, *34*, 19–30.

(51) *Contact Angle, Wettability and Adhesion*, volume 3.; Mittal, KI. L. Ed.; CRC Press: Boca Raton, 2003.

(52) Vasile, C.; Baican, M. C.; Tibirna, C. M.; Tuchilus, C.; Debarnot, D.; Pslaru, E.; Poncin-Epaillard, F. Microwave plasma activation of a polyvinylidene fluoride surface for protein immobilization. *Journal of Physics D: Applied Physics* **2011**, *44*, 475303.

(53) Yakabe, H.; Tanaka, K.; Nagamura, T.; Sasaki, S.; Sakata, O.; Takahara, A.; Ka- jiyama, T. Grazing incidence X-ray diffraction study on surface crystal structure of polyethylene thin films. *Polymer Bulletin* **2005**, *53*, 213–222.

(54) Yakabe, H.; Sasaki, S.; Sakata, O.; Takahara, A.; Kajiyama, T. Paracrystalline lattice distortion in the near-surface region of melt-crystallized polyethylene films evaluated by synchrotron-sourced grazing-incidence X-ray diffraction. *Macromolecules* **2003**, *36*, 5905–5907.

(55) Sakai, A.; Tanaka, K.; Fujii, Y.; Nagamura, T.; Kajiyama, T. Structure and thermal molecular motion at surface of semi-crystalline isotactic polypropylene films. *Polymer* **2005**, *46*, 429–437.

(56) Vega, C.; De Miguel, E. Surface tension of the most popular models of water by using the test-area simulation method. *Journal of Chemical Physics* **2007**, *126*, 154707.

(57) Connolly, M. L. Analytical molecular surface calculation. *Journal of Applied Crystal- lography* **1983**, *16*, 548–558.

(58) Bekele, S.; Tsige, M. Effect of Polymer/Solid and Polymer/Vapor Instantaneous Inter- faces on the Interfacial Structure and Dynamics of Polymer Melt Systems. *Langmuir* **2016**, *32*, 7151–7158.

(59) Wilson, M. A.; Pohorille, A.; Pratt, L. R. Molecular dynamics of the water liquid-vapor interface. *Journal of Physical Chemistry* **1987**, *91*, 4873–4878.

(60) Sokhan, V. P.; Tildesley, D. J. The free surface of water: Molecular orientation, surface potential and nonlinear susceptibility. *Molecular Physics* **1997**, *92*, 625–640.

(61) Dang, L. X.; Chang, T. M. Molecular mechanism of ion binding to the liquid/vapor interface of water. *Journal of Physical Chemistry B* **2002**, *106*, 235–238.

Table 1: Number of water molecules contained in a water droplet and unit cell length adopted for contact angle calculations.

<table>
  <thead>
    <tr>
      <th>$D$ (nm)</th>
      <th>number of water molecules</th>
      <th colspan="3">crystal PVDF system</th>
      <th colspan="3">amorphous PVDF system</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>X cell length (nm)</th>
      <th>Y cell length (nm)</th>
      <th>Z cell length (nm)</th>
      <th>X cell length (nm)</th>
      <th>Y cell length (nm)</th>
      <th>Z cell length (nm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>4</td>
      <td>1128</td>
      <td>16.9</td>
      <td>17.4</td>
      <td>22.8</td>
      <td>18.0</td>
      <td>18.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <td>5.5</td>
      <td>2912</td>
      <td>16.9</td>
      <td>17.4</td>
      <td>22.8</td>
      <td>18.0</td>
      <td>18.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>5990</td>
      <td>16.9</td>
      <td>17.4</td>
      <td>22.8</td>
      <td>18.0</td>
      <td>18.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <td>10</td>
      <td>17503</td>
      <td>16.9</td>
      <td>17.4</td>
      <td>22.8</td>
      <td>18.0</td>
      <td>18.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <td>13</td>
      <td>38454</td>
      <td>21.7</td>
      <td>21.9</td>
      <td>30.4</td>
      <td>24.0</td>
      <td>24.0</td>
      <td>33.5</td>
    </tr>
  </tbody>
</table>

Table 2: Number of water molecules and unit cell length in crystal and amorphous PVDF/water/vacuum slab systems.

<table>
  <thead>
    <tr>
      <th></th>
      <th>number of water molecules</th>
      <th>X cell length (nm)</th>
      <th>Y cell length (nm)</th>
      <th>Z cell length (nm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>crystal PVDF system</td>
      <td>6425</td>
      <td>4.82</td>
      <td>4.99</td>
      <td>22.0</td>
    </tr>
    <tr>
      <td>amorphous PVDF system</td>
      <td>9654</td>
      <td>6.01</td>
      <td>6.01</td>
      <td>22.0</td>
    </tr>
  </tbody>
</table>

Table 3: Interaction energy of the whole system (total) and interaction energy between PVDF and water (PVDF-water) in crystal and amorphous PVDF/water/vacuum slab systems.

<table>
  <thead>
    <tr>
      <th rowspan="2">System</th>
      <th colspan="3">total interaction energy / volume<br>($\text{kJ mol}^{-1}\ \text{nm}^{-3}$)</th>
      <th colspan="3">PVDF-water interaction energy / area<br>($\text{kJ mol}^{-1}\ \text{nm}^{-2}$)</th>
    </tr>
    <tr>
      <th>LJ</th>
      <th>Coul</th>
      <th>LJ + Coul</th>
      <th>LJ</th>
      <th>Coul</th>
      <th>LJ + Coul</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>crystal</td>
      <td>71±1</td>
      <td>-881±2</td>
      <td>-810±2</td>
      <td>-45±1</td>
      <td>-28±4</td>
      <td>-73±5</td>
    </tr>
    <tr>
      <td>amorphous</td>
      <td>84±1</td>
      <td>-834±2</td>
      <td>-750±2</td>
      <td>-47±1</td>
      <td>-85±6</td>
      <td>-132±6</td>
    </tr>
  </tbody>
</table>

![](./images/812998106718142464_3.jpg)

Figure 1: An example initial configuration used for contact angle calculation (water droplet with diameter $D = 7$ nm on PVDF crystal surface)

![](./images/812998106718142464_4.jpg)

Figure 2: Droplet size dependence of contact angle of water droplet on PVDF surfaces. The water droplets on the PVDF crystal surface are shown by open diamonds and the water droplets on the PVDF amorphous surface are shown by solid diamonds. Error (standard deviation) of the contact angle was about $2^\circ$ or less on the crystal surface and about $4^\circ$ or less on the amorphous surface. (a) The calculated contact angle $\theta$ as a function of $r_{dr}(Z_0)$. (b) The calculated $\cos\theta$ as a function of $1/r_{dr}(Z_0)$. The broken line is the regression line of $\cos\theta$. (c) A snapshot of the final structure of a $D=13$ nm water droplet on the PVDF crystal surface. (d) A snapshot of the final structure of a $D=13$ nm water droplet on the PVDF amorphous surface.

![](./images/812998106718142464_5.jpg)

Figure 3: Structural analysis for the planar interface between PVDF crystal surface and water. (a) A snapshot of the final structure and (b) number density distribution of atoms. F atom of PVDF: black line, H atom of PVDF: red line, O atom of water: blue line, and H atom of water: green line. (c) Ensemble average of the orientation of water dipole moment $\langle\cos\phi\rangle$ as a function of $Z$, where $\phi$ is defined as the angle formed by the water dipole moment and Z-axis. Positions I and II are at $Z=7.1$ nm (bulk) and $2.9$ nm (interface).

![](./images/812998106718142464_6.jpg)

Figure 4: Structural analysis for the planar interface between a PVDF amorphous surface and water. (a) A snapshot of the final structure and (b) number density distribution of atoms. F atom of PVDF: black line, H atom of PVDF: red line, O atom of water: blue line and H atom of water: green line. (c) Ensemble average of the orientation of water dipole moment $\langle\cos\phi\rangle$ as a function of $Z$, where $\phi$ is defined by the angle formed by the water dipole moment and $Z$-axis. Positions i, ii and iii are at $Z=7.1$ nm (bulk), 2.9 nm (near the interface in the water side) and 2.3 nm (near the interface in the PVDF side).

![](./images/812998106718142464_7.jpg)

Figure 5: The calculated probability distribution of $\cos\phi$ on (a) PVDF crystal surface, red line: $Z=7.1$ nm (position I in Figure 3 (c)), black line: $Z=2.9$ nm (position II in Figure 3 (c)), and on (b) PVDF amorphous surface, red line: $Z=7.1$ nm (position i in Figure 4 (c)), black line: $Z=2.9$ nm (position ii in Figure 4 (c)) and blue line: $Z=2.3$ nm (position iii in Figure 4 (c)).

![](./images/812998106718142464_8.jpg)

Figure 6: Schematic diagram of the orientation of water dipole moments at the PVDF/water interface, (a) crystal PVDF/water interface and (b) amorphous PVDF/water interface.

![](./images/812998106718142464_9.jpg)

Figure 7: (a) The calculated charge density distribution and (b) electrostatic potential distribution for the PVDF crystal surface. Solid black line: total, red dashed line: contribution from PVDF, and green dashed line: contribution from water.

![](./images/812998106718142464_10.jpg)

Figure 8: (a) The calculated charge density distribution and (b) electrostatic potential distribution for the PVDF amorphous surface. Solid black line: total, red dashed line: contribution from PVDF, and green dashed line: contribution from water.

# Graphical TOC Entry

![](./images/812998106718142464_11.jpg)