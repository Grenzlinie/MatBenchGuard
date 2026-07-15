# A Model of Secondary Emission From Dust Grains and Its Comparison With an Experiment

Ivana Richterová, Zdeněk Němeček, Jana Šafránková, and Jiří Pavlů

**Abstract**—Secondary emission from metal surfaces is well described by the theory of Sternglass. His theory and resulting "universal" curve can be applied for planar uncharged surfaces in an energy range from tens of electronvolts to several kiloelectronvolts. However, space dust is composed of silicates, ice, and graphite, i.e., nonconducting materials. Their surfaces are highly curved, and they are usually charged to nonnegligible potentials. Since previous attempts to describe the size effect on emission properties of the dust succeeded only partly, we have used the original Sternglass approach and developed a computer model of secondary emission from small bodies. The model follows individual trajectories of primary electrons inside the grain and, based on simple assumptions consistent with the Sternglass theory, calculates a probability of escaping of the excited electrons. The model provides measurable quantities (the yield of secondary emission, the charge accumulated in the grain, or the surface potential) but it can illustrate processes which are not accessible by direct measurements. Free parameters of the model depend on the grain material and can be determined by a fit of model results to the experimental data. The paper presents model assumptions and results of calculations for spheres of different diameters and two insulating materials. The theoretical results are compared with the laboratory experiment when the grains with approximately 1, 2, 5, and 10 $\mu$m of diameter were charged by an electron beam in a range 300 eV–10 keV. The comparison shows a good agreement of the experiment and theory. Moreover, the reversal of the sign of the grain charge in a certain range of beam energies and grain diameters predicted by the model was confirmed by the experiment.

**Index Terms**—Dust, dust charging, model of secondary emission, secondary emission.

## I. INTRODUCTION

DUSTY PLASMA can be found nearly everywhere in space as well as in many industrial applications. The presence of the dust strongly affects plasma parameters because dust grains provide a large surface for recombination and chemical reactions and accumulate a nonnegligible charge by a variety of processes. It is usually expected that dominant processes charging the dust in plasma are electron and ion attachments. However, as Chakraborty *et al.* [2] have shown, in a nonequilibrium plasma, secondary emission can play a prominent role in an establishment of the grain charge. This process is important when a portion of the energetic (>10 eV) electrons is present in the medium surrounding the grain.

Secondary emission has been treated theoretically for many years. One of the first theories was published by Sternglass [1]. This theory describes well the experimental data from planar metal surfaces in a range from hundreds of electronvolts to several kiloelectronvolts, and thus we will repeat the basic assumptions here.

A primary electron penetrates into a solid and undergoes both elastic and inelastic collisions with lattice atoms. Although concentrating on metals, he assumes that the inelastic collisions are most important for secondary emission. Such collisions lead to excitation of electrons from inner shells. Accordingly, the energy losses of primary electrons during collisions are rather high (50–70 eV). A random scattering of primary electrons results in the fact that the energy of primaries is deposited in a thin layer near the surface. Thus, a depth of the maximum energy loss of primaries scales with their energy as $\sqrt{E}$. The electrons excited during collisions can reach the surface and become secondary electrons with a probability exponentially decreasing along their path to the surface. Theoretical treatments lead to the Sternglass [1] universal curve which can be written as

$$
\frac{\delta}{\delta_{\text{max}}} = \frac{E}{E_{\text{max}}} \cdot \exp \left( 2 - 2\sqrt{\frac{E}{E_{\text{max}}}} \right)
$$

where $\delta$ is the yield of secondary emission, $E$ is the energy of primary electrons, $E_{\text{max}}$ is a position of the peak of secondary emission, and $\delta_{\text{max}}$ is its height.

Dionne [3] analyzed the one-dimensional constant-loss theory of secondary electron emission and his results provide simple relations between the secondary-emission yield-curve parameters and variables which describe some of the electronic and chemical properties of a particular material.

The mentioned (and many others) models or theories cannot be used for description of charging of very small bodies with dimensions comparable to the penetration depth of primary electrons. A model of the secondary emission from submicrometer oil drops was developed by Ziemann *et al.* [4]. However, they achieved a good matching with their experiment up to 250 eV of the primary energy, which is below the lower limit of our energy range. Svestka *et al.* [5] have shown that the potential of the small grain follows roughly a curve of the secondary emission yield exhibiting a maximum at about 1 keV of a primary energy. When the primary energy increases, the potential decreases. However, above a certain limit ($\sim$10 keV in their case), the potential increases again. At the same time, Chow *et al.* [6] developed a model of secondary emission from spherical bodies. They assume that the primary electron current density

Manuscript received August 14, 2003; revised October 16, 2003. This work was supported in part by Research Project MSM 113200004 and by the Charles University Grant Agency under Contract 176/01.

The authors are with the Faculty of Mathematics and Physics, Charles University, Prague, Czech Republic.

Digital Object Identifier 10.1109/TPS.2004.826111

is conserved inside the grain, the production rate of secondaries is proportional to the energy loss of primaries, and the escaping probability of secondary electrons decreases exponentially with a distance to the surface. They add the Whiddington law for energy losses along their path in the grain and computed the yield of secondary emission. We would like to note that their assumptions are similar to those in [3].

The Chow *et al.* [6] computation, in fact, assumes that the primary electrons move along straight lines inside the grain, but the secondaries can proceed toward the surface in any direction. Since this model did not reproduce the Svestka *et al.* [5] data, Chow *et al.* [7] published an improved model. The new model provides the curve of the yield of secondary emission with several maxima. Varying the constants of the model, the authors were able to fit the data but they should use different sets of constants for low- and high-energy portions.

The motivation of the present work is to investigate the effect of the grain size on its charging properties. We use micron-sized spherical dust grains from nonconducting materials. Since we were not able to interpret our experimental results using previous models, we have developed a new model of secondary emission. Finally, we discuss a difference between the model and experiment.

## II. MODEL OF SECONDARY EMISSION

Experimental investigations of dust grains affected by the monoenergetic electron beam reveal several regimes of the grain charging. At a low energy range, the grain potential exhibits a characteristic local maximum corresponding to the maximum of secondary emission yield. It means that the grain behaves as a large body.

At middle energies, grains with the diameter above a certain limit gain a negative potential determined by the beam energy and/or other processes than secondary emission. At a high energy range, the grain potential increases with the beam energy. Even if the grain was charged negatively by a certain beam energy, the increase of this energy can switch the sign of the grain potential to positive values.

All above cases were observed in our experiment and will be shown in Section II. Since our attempts to explain the observations in terms of present models were unsuccessful, we have developed our own model.

### A. Model Assumptions

Since the theory of Sternglass [1] achieved a great success in the description of the secondary emission from planar surfaces, we followed the basic assumptions of this theory in our model.

1) Primary beam electrons penetrate into a grain and undergo collisions with grain atoms. A direction of the primary electron motion changes during collisions in a random way.
2) The primary electron loses a constant energy $\Delta E$ during each collision and excites one secondary electron.
3) The length of the primary electron path between two consecutive collisions is proportional to its current energy $\lambda = \lambda_0 \cdot (E/\Delta E)$ ($\lambda_0$ is hereafter called the elementary mean-free path).
4) A probability $P = A \cdot \exp(-\alpha x)$ that the excited secondary electron reaches a grain surface decreases exponentially with a distance from the surface $x$. In this equation, $\alpha$ is the absorption constant (or an inverse of the absorption length $\Lambda$). Constant $A$ normalizes the integral probability to be equal to 1/2 when the electron is on the surface of a grain with the infinite diameter.
5) Secondary electrons reach the grain surface with a Maxwellian energy distribution. The influence of their temperature on model results will be discussed later.

In order to simplify a computation of the spatial distribution of energy losses, we apply the Monte Carlo method for a description of a primary electron motion inside the grain. On the other hand, a probability that the excited electron reaches the surface is obtained by the integration of the probability function around $4\pi$ of a spatial angle. The secondary emission yield $\delta$ is thus considered as a sum of all probabilities divided by a number of launched primary electrons. Since we follow trajectories of all primary electrons inside the grain, we can simply determine the reflection coefficient $\eta$ as a ratio of numbers of primary electrons falling on the grain and escaping from the grain. This is very important for the calculations of a total charge accumulated in the grain because primary electrons remaining in a grain deposit their charges there, whereas those escaping do not.

### B. Model Testing

A test of the model can be done by a comparison of results computed for the sphere of an infinite diameter with the Sternglass universal curve [1]. These results are shown in Fig. 1 where the normalized yield of secondary emission is plotted as a function of the normalized energy of primary electrons. We can note that the Sternglass curve (full line) does not differ substantially from those obtained by our calculations using different forms of random distribution. Surprisingly, the model results are not sensitive to a particular form of this distribution. We are presenting calculations for random distribution (thin line) and random distribution weighted by cosine of the angle between the velocities before and after the collision (dashed line). For comparison, the dotted line shows the results computed under assumption that primary electrons move along a straight line. This assumption is used in other calculations, e.g., Chow *et al.* [7], but it can be seen that the results differ significantly from the generally accepted universal curve.

However, Monte Carlo calculations are time consuming, and thus it is desirable to use only one distribution of velocities. The secondary emission yield does not allow us to decide, but the calculations of a number of reflected electrons (not presented) show that the random distribution leads to an excess of these electrons in comparison with published data [8]. We think that the primary electron does not lose completely the information about its motion before collision, and thus the cosine distribution provides better results. All calculations presented hereafter use this distribution.

### C. Model Results—Yield of Secondary Emission

Fig. 2 shows the calculated yield of secondary emission as a function of the primary electron energy for four different grain

![](./images/812345424705748994_1.jpg)

Fig. 1. Comparison of normalized secondary emission yields computed for different velocity distributions of primary electrons with Sternglass universal curve.

radii. The plot is given in normalized units, the energy in a number of elementary losses and grain radii in units of the elementary mean-free path $\lambda_0$. We can see from the figure that the yield of secondary emission depends on the grain diameter only slightly and that there are no secondary maxima in the whole range of energies. Since different materials exhibit the same de- pendence of the secondary emission yield if plotted in normal- ized coordinates $\delta/\delta_{\text{max}}$, $E/E_{\text{max}}$[1], we have plotted $\delta_{\text{max}}$ and $E_{\text{max}}$ as a function of a grain radius $R$ and material constant $\alpha$, in Fig. 3. As can be seen from the figure, both $\delta_{\text{max}}$ and $E_{\text{max}}$ are nearly independent on the grain diameter and both are roughly inversely proportional to a logarithm of the material constant, $\alpha$. Note that $R$ is here and in all other figures given in units of the elementary mean-free path $\lambda_0$. A small rise of $\delta_{\text{max}}$ below $R = 10^3$ is thus out of our range of grain sizes. It is clear from these plots that a behavior of the grain potential mentioned in previous sections cannot be explained by a variation of the secondary emission yield with a grain size.

### D. Model Results-Surface Potential of the Grain
The quantities like secondary emission yield are not measurable, but the proposed model can provide a value of the grain charge which can be simply converted into a potential. Model results for four different grain diameters are plotted in Fig. 4, again as a function of the primary beam energy. We can identify four types of dependencies. The potential rises with the energy of primary electrons for very small grains. Larger grains exhibit a clear local minimum which becomes deeper with an increasing grain size. If the grain is large enough, the potential changes its sign and becomes negative in a range of energies (dotted and dashed-dotted lines in Fig. 4). We should point out that our model cannot reproduce negative potentials, and thus the potential is set to zero in such cases. The potential of the grains of an intermediate size (dotted line) changes its sign again for a high energies of primary electrons, whereas it remains negative in a modeled range of energies for very large grains. We would like to note that the values of computed potentials depend on the temperature of an energy distribution of secondary electrons. Calculations presented in Fig. 4 expect the temperature of 1.2 eV; however, an advantage of the Maxwellian distribution is that the computed potential is directly proportional to the temperature, and thus the model data can be simply scaled to the experiment.

We suggest that the potential behavior is given by a balance of secondary electrons leaving the grain and primary electrons remaining in the grain. The former is proportional to the yield of secondary emission $\delta$, whereas the latter is proportional to

![](./images/812345424705748994_2.jpg)

Fig. 2. Computed yield of secondary emission as a function of the primary energy and grain sizes.

![](./images/812345424705748994_3.jpg)

Fig. 3. Energy corresponding to(a) maximum of secondary emission yield and (b) maximum of the yield as a function of the grain size and material constant.

![](./images/812345424705748994_4.jpg)

Fig. 4. Computed potentials of dust grains of different sizes as a function of the beam energy.

![](./images/812345424705748994_5.jpg)

Fig. 5. Secondary emission yield and a number of primary electrons remaining in the grain as a function of the beam energy.

$(1 - \eta)$. Fig. 5 presents these two quantities for a grain which changes twice the potential sign in the considered energy range (dotted line in Fig. 4). Comparing Figs. 4 and 5, we can see that $\phi = 0$ when $1 - \eta = \delta$ ($\sim$160 and 260 units of the energy) and $\phi$ is positive, if $1 - \eta < \delta$. A value of the surface potential is then determined by the energy distribution of secondary electrons. On the other hand, if $1 - \eta > \delta$, the potential is negative and determined by the beam energy and other processes, as is shown in Pavlu *et al.* [9].

Contrary to our suggestions, it is generally expected (see, e.g., [5]–[7]) that a rise of the grain potential at a high energy range is caused by secondary electrons emitted from the back side of a grain when the penetration depth of primary electrons becomes comparable with the grain size. To check this hypothesis, we have divided the grain into slices of equal surface along the primary beam direction and plotted a number of secondary and scattered primary electrons as a function of the beam energy and slice position $D$, in Fig. 6. We can see that a number of primary electrons escaping from the back side ($D < 0.5$) increases with the energy and becomes dominant for energies exceeding 10 keV, as one would expect. (The calculations were done for a 1-$\mu$m grain.) On the other hand, the number of secondary electrons emitted from the back side increases only slightly with the beam energy [Fig. 6(b)].

## III. COMPARISON OF THE MODEL WITH EXPERIMENTAL RESULTS

In the previous section, we have shown that the model qualitatively reproduces the experimental data. However, the model has several free parameters ($\Delta E, \lambda_0, \alpha$) which can be determined by a comparison of model and experimental results, only. For this reason, we have used the experimental setup described in [10] and measured the grain potential as a function of the electron beam energy. We have used spheres from melamine formaldehyde resin with 2.35, 4.97, and 9.78 $\mu$m of diameter. (The sphericity and diameters of grains were checked by the electron microscope.)

![](./images/812345424705748994_6.jpg)

Fig. 6. Number of (a) scattered primaries and (b) emitted secondaries as a function of the beam energy and locations on the grain surface.

Measured values of grain potentials are shown in Fig. 7 by different symbols. We can note that the measured potential does not depend substantially on the grain size up to 4 keV of primary energy and the same shows the computed potential plotted by the lines. The model predicts well the maximum at $\sim$350 eV and the decreasing of the potential up to 1 keV of primary energy. Above this value, the model suggests a further steep decreasing,

![](./images/812345424705748994_7.jpg)

Fig. 7. Comparison of the measured (points) and computed (lines) potentials for MF spheres of different diameters. Parameters of the model are $\Delta E = 37$ eV, $\lambda_0 = 0.21$ nm, $\alpha = 0.03$, $T_{SE} = 3$ eV.

whereas measured potential decreases more gradually. This dis- agreement is caused by the energy distribution of secondary electrons. As we noted above, we use the Maxwellian distri- bution in our calculations because it allows a simple scaling. A difference between the model and experiment suggests that a distribution with an enhanced tail would be more appropriate. This conclusion is consistent with a fact that, in order to fit the maximum of the potential, we should use 4.4 eV of the sec- ondary electron temperature.

An increase of the potential measured for the 2.35-$\mu$m grain in the range 9–10 keV is well predicted by the model. Model potentials were obtained for the following values of constants: $\Delta E = 37$ eV, $\lambda_0 \approx 0.21$ nm, $\Lambda = 7$ nm, $T_{SE} = 3$ eV. The values are in a very good agreement with expectations. $\Delta E$ is very similar to that suggested by Sternglass [1], the value of $\lambda_0$ suggests that the mean-free path of low-energy primary elec- trons is of the order of interatom distances, and $\Lambda$ is in the range of the absorption length measured by other methods [7]. How- ever, all grains shown in Fig. 7 exhibit negative potentials. Our model predicts that the negative potentials disappear for smaller grains. Unfortunately, we do not have 1-$\mu$m grains from the same material at our disposal and thus we used 1.2-$\mu$m spheres from SiO₂. The comparison of model and experimental results for this case is shown in Fig. 8. The fit was obtained with fol- lowing constants: $\Delta E = 34$ eV, $\lambda_0 \approx 0.12$ nm, $\Lambda = 7$ nm, $T_{SE} = 2.2$ eV. We should note that the only notably changed constant is the elementary mean-free path of primary electrons. It shows that penetration depth of primary electrons in SiO₂ is shorter than that in MF resin. Such a result could be expected if one takes into account the different structures of these materials.

An overall agreement of the experiment and model is very good except the region of lowest potentials. This region is again affected by the shape of the energy distribution as discussed in a previous case.

### IV. DISCUSSION

We have presented a simple model of secondary emission from small spherical grains. The model describes well obser- vational results measured on insulating grains of different di- ameters in the energy range 0.3–10 keV. The model is based on assumptions originally formulated and successfully used by Sternglass [1]. The success of our model in the description of experimental observations shows that the principal process to be taken into account is the random scattering of primary elec- trons inside the solid.

![](./images/812345424705748994_8.jpg)

Fig. 8. Best fit of the potential measured on a 1.2-$\mu$m SiO₂ sphere (measured in dots, model in solid line). Parameters of the model are $\Delta E = 34$ eV, $\lambda_0 = 0.12$ nm, $\alpha = 0.016$, $T_{SE} = 2.2$ eV.

However, an important difference between processes in metals described by Sternglass [1] and our modeling of in- sulators reveals a relatively low value of elementary energy loss $\Delta E$ that we have found. Sternglass expected that the principal process leading to creation of secondary electrons is collision of primaries with atoms of the solid lattice, not with the free electrons in the conducting band. However, there are no electrons in the conducting band in insulators, and thus the interaction with lattice atoms can excite the electrons from the valence band. This probably leads to a lower excitation energy $\Delta E$, as observed.

In spite of a good agreement with experimental data, the model has several limitations. We suppose that all energy of primary electrons is lost by collisions and we do not treat the rest of the energy. This can cause a negligible error only if the initial energy is large enough, and thus the model cannot give realistic results for energies up to several hundreds of electronvolts.

Primary electrons can interact with lattice atoms in a different way when their energy is very high (tens of kiloelectronvolts or more). In such a case, secondary electrons can be excited from inner shells and the corresponding energy losses would be higher. Moreover, the probability that a primary electron excites more than one secondary electron during one collision would increase with the energy. These facts limit the validity range of our model to about 20 keV.

The model uses the Maxwellian energy distribution of sec- ondary electrons but the process of a diffusion of the excited electrons from different locations inside the grain does not nec- essarily provide such distribution, and the model potentials are rather sensitive to content of high energy electrons in the distri- bution.

Velyhan et al. [11] studied secondary emission from different metals and compared the results with an analytical model of Žilavý et al. [10] which uses the energy distribution of sec-

ondary electrons as an input parameter. The authors have shown that the distribution suggested by Draine and Salpeter [12] fits the experimental data significantly better than the Maxwellian distribution. Moreover, many astrophysical plasmas are seen to have non-Maxwellian, high-energy tails (e.g., Summers and Thorne [13]) which can be well represented by generalized Lorentzian ($\kappa$) distributions (e.g., Gosling *et al.* [14], Christon *et al.* [15]), and thus we would like to continue in this direction in the future.

### V. CONCLUSION

The theoretical and experimental studies of secondary emission from insulating dust grains reveal that:
- the potential of the grain can be enhanced in a range of primary energies and grain sizes (if the grain size is comparable with a penetration depth of primary electrons);
- contrary to previous expectations, the enhancement is caused by the increasing number of scattered primary electrons, not by an enhanced true secondary emission yield;
- the true secondary emission yield is a function of the grain size in a nanometer range only;
- a more exact modeling of grain potentials requires the knowledge of the secondary electron energy distribution.

We would like to point out that although the presented model was intended to explain the emission from insulators, it can be used for metals and semiconductors because it is based on assumptions already suggested for metals. However, it is also clear that further model improvements are necessary in order to have a full theory, in particular to describe larger grain sizes which exhibit negative surface potentials in the intermediate energy range.

## REFERENCES

[1] E. J. Sternglass, "Theory of secondary electron emission under electron bombardment," in *Westinghouse Res. Lab.*, Pittsburgh, PA, Jul. 1957, Scientific Paper 6-94 410-2-P9.

[2] M. Chakraborty, S. S. Kausik, B. K. Saikia, M. Kakati, and S. Bujarbarua, "The effect of the ambient plasma conditions on the variation of charge on dust grains," *Phys. Plasmas*, vol. 10, pp. 554-557, Feb. 2003.

[3] G. F. Dionne, "Origin of secondary-electron-emission yield-curve parameters," *J. Appl. Phys.*, vol. 46, pp. 3347-3351, Aug. 1975.

[4] P. J. Ziemann, P. Liu, D. B. Kittelson, and P. H. McMurry, "Electron-impact charging properties of size-selected, submicrometer organic particles," *J. Phys. Chem.*, vol. 99, pp. 5126-5138, Apr. 1995.

[5] J. Švestka, I Čermák, and E. Grün, "Electric charging and electrostatic fragmentation of dust particle in laboratory," *Adv. Space Res.*, vol. 13, pp. (10)199-(10)202, Oct. 1993.

[6] V. W. Chow, D. A. Mendis, and M. Rosenberg, "Role of grain size and particle velocity distribution in secondary electron emission in space plasmas," *J. Geophys. Res.*, vol. 98, no. A11, pp. 19065-19076, Nov. 1993.

[7] ——, "Secondary emission from small dust grains at high electron energies," *IEEE Trans. Plasma Sci.*, vol. 22, pp. 179-186, Apr. 1994.

[8] I. M. Bronshtein and B. S. Frajman, *Secondary Electron Emission*. Moscow, Russia: Nauka, 1969.

[9] J. Pavlů, Z. Němeček, J. Šafránková, and I. Čermák, *Emission From Non-Conducting Negatively Charged Dust Grains*.

[10] P. Žilavý, Z. Sternovský, I. Čermák, Z. Němeček, and J. Šafránková, "Surface potential of small particles charged by the medium-energy electron beam," *Vacuum*, vol. 50, no. 1-2, pp. 139-142, June 1998.

[11] A. Velyhan, Z. Němeček, and J. Šafránková, "Secondary electron emission from small metallic grains," *WDS'01 Proc. Contributed Papers*, pp. 267-272, 2001.

[12] B. T. Draine and E. E. Salpeter, "On the physics of dust grains in hot gas," *Astrophys. J.*, vol. 231, pp. 77-94, July 1979.

[13] D. Summers and R. M. Thorne, "The modified plasma dispersion function," *Phys. Fluids*, vol. 83, pp. 1835-1847, Aug. 1991.

[14] J. T. Gosling *et al.*, "Interplanetary ions during an energetic storm particle event: The distribution function from solar wind thermal energies to 1.6 MeV," *J. Geophys. Res.*, vol. 86, pp. 547-554, 1981.

[15] S. P. Christon *et al.*, "Energy spectra of plasma sheet ions and electrons from 50 eV/e to 1 Mev/e during plasma temperature transitions," *J. Geophys. Res.*, vol. 93, pp. 2562-2572, Apr. 1988.

![](./images/812345424705748994_9.jpg)
Ivana Richterová was born in 1979 in Český Brod, Czech Republic. She is working toward the M.S. degree at Charles University, Prague, Czech Republic.

![](./images/812345424705748994_10.jpg)
Zdeněk Němeček was born in 1947 in Prague, Czech Republic. He received the M.S., Ph.D., and Dr.Sc. degrees from Charles University, Prague, Czech Republic, in 1971, 1982, and 1996, respectively.

Since 1971, he has held several positions in the Faculty of Mathematics and Physics, Charles University, where he is currently Vice Dean of the Faculty. His research interests include dealing with the solar wind interaction with the Earth's magnetosphere and the laboratory simulation of plasma processes.

![](./images/812345424705748994_11.jpg)
Jana Šafránková was born in Teplice, Czech Republic, in 1947. She received the M.S., Ph.D., and Dr.Sc. degrees from Charles University, Prague, Czech Republic, in 1972, 1982, and 1996, respectively.

Since 1971, she has held several positions in the Faculty of Mathematics and Physics, Charles University, where she is currently Deputy Director of the Department of Electronics and Vacuum Physics and the Head of Space Physics Laboratory. Her recent research interests include the magnetospheric physics and laboratory simulation of elementary processes in dusty plasmas.

![](./images/812345424705748994_12.jpg)
Jiří Pavlů was born in 1977 in Pardubice, Czech Republic. He received the M.S. degree from Charles University, Prague, Czech Republic, in 2001, and is currently working toward the Ph.D. degree there.

At present, he works in the Space Physics Laboratory, Department of Electronics and Vacuum Physics, Faculty of Mathematics and Physics, Charles University. His research interests include the laboratory investigation of elementary charging processes on dust grains.