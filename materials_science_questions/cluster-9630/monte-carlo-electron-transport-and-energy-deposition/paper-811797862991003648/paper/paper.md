Monte Carlo simulation of focused helium ion beam induced deposition

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2010 Nanotechnology 21 175302

(http://iopscience.iop.org/0957-4484/21/17/175302)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 129.2.19.100
This content was downloaded on 06/02/2015 at 10:32

Please note that terms and conditions apply.

# Monte Carlo simulation of focused helium ion beam induced deposition

Daryl A Smith, David C Joy and Philip D Rack¹

Department of Material Science and Engineering, University of Tennessee, Knoxville, USA

E-mail: prack@utk.edu

Received 22 January 2010, in final form 12 March 2010
Published 1 April 2010
Online at stacks.iop.org/Nano/21/175302

## Abstract
The details of a Monte Carlo helium ion beam induced deposition simulation are introduced and initial results for reaction rate and mass transport limited growth regimes are presented.
Reaction rate limited growth leads to fast vertical growth from incident primary ions and minimal lateral broadening, whereas mass transport limited growth has lower vertical growth velocity and exhibits broadening due to scattered ions and secondary electrons. The results are compared to recent experiments and previous electron beam induced deposition simulations.

(Some figures in this article are in colour only in the electronic version)

The recent advances in the helium gas source ion beam has enabled the development of a new focused ion beam imaging tool which has garnered much interest for its high-brightness, nanoscale imaging resolution, and multiple imaging modes. Several groups have recently reported on various imaging resolution and contrast mechanisms as well as various scanning and transmission imaging modes [1–3]. Beyond imaging applications, the ability of the helium ion beam to induce nanoscale localized deposition [4], etching [5], and nanoscale lithography [6] has also been recently been demonstrated. Interesting advantages can be imagined as the helium ion beam conveniently straddles characteristics between the gallium focused ion beam and focused electron beams. For instance, deleterious implantation damage and staining associated with the heavy gallium focused ion beam can be somewhat mitigated with helium ions [7].

The focus of this paper is to introduce a Monte Carlo simulation based on ion–solid and secondary electron algorithms from the recently described IONiSE simulation [8] and gas handling algorithms based on an electron beam induced deposition simulation [9–12]. After a basic description of the simulation (so-called EnvisION) we present helium ion beam induced deposition results assuming a 1.5 nm FWHM Gaussian beam comparing the growth of tungsten nanopillars via a WF₆ precursor in two growth modes: (1) reaction rate limited regime in which the flux of precursor atoms is 1000× the flux of He ions, and (2) the mass transport limited regime in which the flux of helium ions is 1000× the flux of precursor atoms.

As mentioned, the single scattering helium ion beam Monte Carlo simulation is based on the IONiSE simulation (with roots to the original SRIM ion beam simulation [13]) where the two-dimensional algorithms have been extended to three dimensions (see Ramachandra *et al* [8] for ion–solid and Monte Carlo and secondary electron generation details). Briefly, successive ion trajectories/scattering steps proceed by: (1) knowing the initial energy, $x$–$y$–$z$ coordinates, and trajectory of the helium ion; (2) based on this information and the relevant solid parameters, the step length, energy loss, and scattering angle ($\theta$) is determined and a random $2\pi$ azimuthal angle ($\phi$) chosen for the first scattering step; the ion energy for the subsequent step is reduced by the calculated energy loss and the new $x$–$y$–$z$ coordinate based on the step length and trajectory is determined. The process continues until either the ion leaves the solid or the ion energy is below a threshold value (250 eV for the present study). Modifications to the standard ion–solid Monte Carlo simulations were made for the present simulation to account for forward scattered and backscattered ions which traverse the solid–vacuum boundary, but have a trajectory that intersects the substrate or the growing nanostructure. In this case when it is determined that the new coordinate is in vacuum, the fractional step length is determined and the fractional energy loss is applied to the ion and the ion trajectory is preserved when re-entering the solid. A new scattering step is determined upon re-entry and the simulation continues.

Several modifications to the secondary electron generation algorithms were made as necessary to spatially represent the SE trajectories as well as handle secondary electron generation

¹ Author to whom any correspondence should be addressed.

in features shorter than the ion step length of the Monte Carlo. First of all, SEs are treated as binary-collision-approximation events whereby the electronic and nuclear stopping powers are handled separately. To approximate the generation of SEs the number of SEs generated at each scattering step is calculated using Bethe's stopping power equation. Consistent with the IONiSE simulation only the electronic energy loss component of the ion is used to generate the SEs:

$$
\delta_{\mathrm{SE}}=-\left(\frac{1}{\varepsilon}\right)\left(\frac{\mathrm{d} E}{\mathrm{~d} s}\right)_{\text {electronic }}.
$$

The scaling constant, $\varepsilon$, is related to the energy required to generate a secondary electron and is a tunable parameter used to determine the correct SE coefficient relative to experimental values. The number of SEs generated at each scattering step (equal to the rounded product of $\delta_{\mathrm{SE}}$ and the step length) are assigned random trajectories and traced until they intersect the solid-vacuum interface. The probability of escape ($p$) is determined via a modified Salow's diffusion/escape probability escape equation [14]:

$$
p(z)=A \exp \left(-\frac{z_{\text {eff }}}{\lambda_{\text {mfp }}}\right),
$$

such that '$z_{\text {eff}}$' is the total distance traveled by the SE to the solid-vacuum interface, rather than simply the depth beneath the surface. The constant 'A' is set equal to 1/2 if the SEs are generated beneath the substrate surface, and the random SE trajectory is generated in $2\pi$ space (toward the substrate-vacuum interface). If the SE is generated in the IBID deposit 'A' is set equal to 1 and the random SE trajectory is selected over $4\pi$ space.

For the original IONiSE simulation, there are two fitting parameters $\lambda_{\text {mfp }}$ and $\varepsilon$, which for tungsten they were determined to be 0.75 nm and 78 eV, respectively. It is important to note that in the IONiSE simulation $\lambda_{\text {mfp }}$ is calculated from the $z$-position for the coordinates of the scattering step from which it is created (which effectively assumes all secondary electrons generated have trajectories that are normal to the surface). To account for the angular distribution of the secondary electron trajectories we have modified the secondary electron algorithm. First the mean free path used here is assumed to be the inelastic MFP along a straight line approximation trajectory. The functionality of the inelastic mean free path is taken from [15] and is described in our previous EBID SE generation description [9]. To determine the mean free path, an energy value is assigned based on conservation of momentum and energy arguments as described in Kotera [16]. Note that this model is based on electron-electron generation, but it has been pointed out that this method of handling SE generation from ions is reasonable for a first order approximation [17]. Secondly, as noted above, the SE trajectory has a $2\pi$ or $4\pi$ angular distribution and thus the average distance the secondary electrons travel to reach the surface are larger than the $z$-position where they are generated (i.e. $z_{\text {eff }}=z / \cos (\theta)$).

Table 1 describes the initial set of parameters that have been used to test the EnvisION simulation which is comparable to published results from our EBID simulation. The gas dynamics assumed for this simulation includes: the surface diffusion is zero; the precursor residence time is long relative to the simulation time; and a Langmuir isotherm is assumed so only a single monolayer can accumulate on the surface. Initially a 'tuning' algorithm was run to determine the $\varepsilon$ value (78 eV) which would yield an SE coefficient of 2.25 for 25 keV helium ions for a flat tungsten substrate to be consistent with measured secondary electron values [18]. The average $\lambda_{\text {mfp }}$ based on the TPP2M model [15] was calculated which is a function of the secondary electron energy. The average inelastic mean free path generated was 2.9 nm, which is reasonably larger than the 0.75 nm value which neglects the angular distribution. The ratio of the two mean free paths (2.9/0.75) is close to the average value of $(1 / \cos (\theta))$ from $0^{\circ}$ to $89^{\circ}$ (average taken to $89^{\circ}$ because the secant function approaches infinity at $90^{\circ}$). Secondary electrons generated after the 5th scattering step are designated SE-II electrons which resulted in an SE-I coefficient of 0.95 and an SE-II coefficient of 1.3 for the flat tungsten substrate. Figure 1 shows (a) a cross-section and (b) a plane view of 10 000 ion trajectories and figure 1(c) shows the histogram of the final $z$-position in the substrate. The backscattered ion coefficient for the flat tungsten substrate was simulated to be 0.32. The peak implant range ($R_{\mathrm{p}}$) and 90% ion range (R90%) approximated by $R_{\mathrm{p}}(\mathrm{nm})=80(E 0.73 / \rho)$ and $R 90 \%(\mathrm{~nm})=$ $56.5(E 0.84-0.002 E / \rho)$, respectively; where $\rho$ is density of target $(\mathrm{g} \mathrm{cm}^{-3})$ and $E$ is the beam energy (keV) was calculated to be $R_{\mathrm{p}}=44 \mathrm{~nm}$ and $R 90 \%=118 \mathrm{~nm}$ [8]. This is in good agreement with the simulated $R_{\mathrm{p}}(44 \mathrm{~nm})$ and R90 (98 nm) of $10000 \mathrm{He}^{+}$ions in tungsten. The electron dissociation cross-section used for the secondary electrons is the same as that described in Livengood et al [7]. While some literature data for gallium ion beam cross-sections have been estimated [19-21], the specific contribution of the ion and SE contribution is not clear. Because of the lack of available helium ion beam induced dissociation cross-section data, for illustrative

<table>
<caption>Table 1. Summary of inputs and outputs for reaction rate limited and mass transport limited regimes.</caption>
<tbody>
<tr>
<td>Inputs</td>
<td>Reaction rate limited</td>
<td>Mass transport limited</td>
</tr>
<tr>
<td>Energy</td>
<td>25 keV</td>
<td>25 keV</td>
</tr>
<tr>
<td>Beam current</td>
<td>9 fA</td>
<td>9 pA</td>
</tr>
<tr>
<td>Beam radius, profile</td>
<td>1.5 nm, Gaussian-like</td>
<td>1.5 nm, Gaussian-like</td>
</tr>
<tr>
<td>Localized pressure</td>
<td>7 Torr</td>
<td>7 mTorr</td>
</tr>
<tr>
<td>SE yield, cumulative</td>
<td>2.25</td>
<td>2.25</td>
</tr>
<tr>
<td>Number of electrons</td>
<td>1 million</td>
<td>30 million</td>
</tr>
<tr>
<td>Outputs</td>
<td>Reaction rate limited</td>
<td>Mass transport limited</td>
</tr>
<tr>
<td>PI atoms deposited</td>
<td>42k</td>
<td>83k</td>
</tr>
<tr>
<td>FSI atoms deposited</td>
<td>151k</td>
<td>1400k</td>
</tr>
<tr>
<td>BSI atoms deposited</td>
<td>6k</td>
<td>212k</td>
</tr>
<tr>
<td>SE(I) atoms deposited</td>
<td>139k</td>
<td>379k</td>
</tr>
<tr>
<td>SE(II) atoms deposited</td>
<td>64k</td>
<td>1288k</td>
</tr>
<tr>
<td>Deposit efficiency (atoms/ion)</td>
<td>40%</td>
<td>11%</td>
</tr>
<tr>
<td>Height</td>
<td>160 nm</td>
<td>148 nm</td>
</tr>
<tr>
<td>Width</td>
<td>8 nm</td>
<td>21 nm</td>
</tr>
</tbody>
</table>

![](./images/811797862991003648_1.jpg)

Figure 1. (a) Cross-section and (b) plain view of $10\,000$ $25$ keV ${\rm He}^{+}$ ions trajectories in a flat tungsten substrate. Figure (c) is a histogram of the final depth of the helium ion (note the backscattered ion coefficient is approximately $32\%$).

purposes, the helium ion beam induced dissociation cross-section was assumed to have similar functionality and a $10\times$ larger magnitude relative to the electron beam dissociation cross-section. The validity of this assumption needs to be explored in the future and better quantitative data for the energy dependent ${\rm He}^{+}$ ion beam-precursor dissociation cross-section will be critical to using the EnvisION simulation to understand experimental results. Thus the value of the results presented here are mainly for illustrative purposes which show some of the relevant ion beam induced deposition phenomena.

Figure 2(a) shows 50 primary ion trajectories in a $10\,\text{nm} \times 10\,\text{nm} \times 20\,\text{nm}$ solid tungsten nanostructure on a tungsten substrate which illustrates some of the details of the simulation. The inset of figure 2(a) is a magnified view of the nanostructure illustrating 10 ion trajectories and the subsequent deposition events generated by the ion (for illustrative purposes the precursor coverage and dissociation probability were set to unity). Note the forward scattered ions can cause deposition leaving the nanostructure and re-entering the substrate surface. Figure 2(b) shows one primary ion trajectory and the all the generated SE electrons and their subsequent trajectories (whether they escape or not). The inset of figure 2(b) illustrates the trajectories of only the SEs which escape and also demonstrates the subsequent deposition (again precursor coverage and dissociation probability were set to unity). For secondary electrons generated above the substrate (i.e. in the grown structure), the electron trajectories are generated in a random position between scattering steps to help randomize where they are generated to compensate for the fact that we are mimicking a continuous process with discrete scattering steps. While secondary electrons are generated for every scattering step, if its $z$-position is more than $10\times\lambda_{\text{imfp}}$ from the surface, its trajectory is not determined to save computational time; the probability of escape for a trajectory normal to the surface is $\sim5\times10^{-5}$.

Figure 3 show a compilation of results for the reaction rate limited parameter set run for 1 million primary ions. Figure 3(a) is a three-dimensional rendering of the deposited tungsten structure and figure 3(b) is an expanded cross-section slice of the top of the deposited structure. The simulation tracks the type of species which is responsible for its dissociation and deposition and the color-coded atoms represent tungsten atoms deposited by: red-primary ions (PI), blue-backscattered ions (BSI), green-forward scattered ions (FSI), yellow-SE-I electrons, and cyan-SE-II electrons. Figure 3(c) shows the sampled deposition efficiency (atoms deposited per ion) for the different types of deposited species as a function of the number of ions (i.e. time). (d) shows the temporal evolution (per ion)

![](./images/811797862991003648_2.jpg)

Figure 2. Simulated 25 keV He⁺ ion trajectories in a
10 nm × 10 nm × 20 nm tungsten nanostructure on a tungsten
substrate. Figure (a) shows the trajectories of 50 ions and the inset is
a magnified view of 10 simulated ions demonstrating the ion
trajectories and ion induced deposition events (for illustrative
purposes the probability and precursor coverage both set to unity).
Figure (b) illustrates a single ion trajectory and all the subsequent
secondary electrons (I and II) generated along the scattering steps
within $10×\lambda_{imfm}$. Inset illustrates an expanded view of five ion
trajectories which illustrate only secondary electron trajectories that
escape and induce deposition (coverage and deposition probability
set to unity).

of the SE-I and SE-II secondary electron coefficients as well as
the combined FSI and BSI coefficient. As demonstrated in the
figure 3(b), a nanopillar geometry with a diameter on the order
of 7–8 nm is realized which is comprised of atoms deposited
by primary He ions and SE-I electrons in the central core of
the pillar and from forward scattered ions and SE-II electrons
at the nanopillar outer shell region. The overall deposition
efficiency (atoms deposited/incident helium ion) is $\sim$40% and
the vertical growth rate is $\sim1.6 × 10^{-4}$ nm/ion.

![](./images/811797862991003648_3.jpg)

Figure 3. Simulation output of 1 million simulated 25 keV He⁺ ions
grown in reaction rate limited regime. Figure (a) illustrates the
resultant nanopillar, and (b) is a cross-section slice through the
middle of the top of the nanopillar (color code of deposited atoms:
red—primary ions (PI), blue—backscattered ions (BSI),
green—forward scattered ions (FSI), yellow—SE-I electrons, and
cyan—SE-II electrons). Figure (c) is the sampled deposition
efficiency (atoms deposited per ion) for the different types of
deposited species as a function of the number of ions (i.e. time).
Figure (d) is the sampled ion and secondary electron coefficients as a
function of the number of ions (i.e. time).

Figure 3(d) shows the electron and ion coefficients (averaged every 40 000 ions) versus the cumulative number of ions (for example the time axis). Figure 3(d) shows during the initial nanopillar growth (up to ~200k ions) the secondary electron yields (SE-I and SE-II) increase up to a combined value of approximately 11 and then decreases to approximately 9. The $\sim 4\times$ increase in the total SE coefficient is reasonable and compares favorably to recent 30 keV helium line edge simulations which showed a $\sim 3\times$ increase in the SE yield [22]. As demonstrated in figure 3(d), the decrease in the total SE yield is due to the slight decrease in the SE-II coefficient which is a simulation artifact attributed to the way we handle trajectories that leave the simulated growth area. Specifically, for this simulation, the simulated $x$–$y$ coordinate area was a 40 nm $\times$ 40 nm area and whose height increases with the pillar growth the save on computational time. When an ion leaves the simulated $x$–$y$ growth area, the secondary electron yield is estimated by the ion energy and a secant function with the angle relative to the substrate normal. At 200k ions the pillar height (32 nm) is at the cross-over point in which many of the forward scattered ions start to leave the 40 nm $\times$ 40 nm grid and apparently the secant function slightly underestimates the Monte Carlo algorithm. The combined FSI and BSI yield approaches unity at this point which suggests that virtually all the impinging ions scatter out of the nanopillar due to the nanoscale radial dimension.

Figure 3(c) shows that the deposition efficiencies for the secondary electrons basically follow the yield data which is reasonable for a reaction rate limited regime. The primary helium ion deposition is constant, as expected, and the forward scattered ion deposition increases as the nanoscale topology develops and eventually saturates. The saturation is related to the effective interaction volume of the helium ion beam in the pseudo-one-dimensional nanostructure. The cone height at the top of the nanopillar is $\sim 20$ nm which transitions to a cylindrical shape. This cone height is equivalent to the effective beam interaction region of the ion in the pseudo-one-dimensional nanopillar and is consistent with the height at which the FSI, SE (I and II) and BSI yields all have an inflection point. The continued slight increase beyond this saturation region is due to re-entry of the ions into the 40 nm $\times$ 40 nm area until $\sim 32$ nm tall pillars scatter beyond the simulation growth region.

Figures 4(a)–(d) shows a similar compilation of results for the mass transport limited parameter set run for 30 million primary ions. Noticeably, the nanopillar is wider ($\sim 22$ nm diameter) with again the central core region dominated by primary ions and SE-I electron induced deposition and the outer shell region is dominated by forward scattered ions and SE-II electrons. The inner core dimension is comparable for both the mass transport and reaction rate limited growth regimes with a $\sim 6$ nm diameter. The outer shell thickness is much wider for the mass transport limited regime which is due to additional lateral growth caused by the slow vertical growth. The vertical growth rate is $\sim 30$ times slower ($\sim 4.9 \times 10^{-6}$ nm/ion). The trends in the backscattered and forward scattered ion and secondary electron yields as well as the deposited species are slightly different for the mass transport

![](./images/811797862991003648_4.jpg)

Figure 4. Simulation output of 30 million simulated 25 keV ${\rm He}^{+}$ ions grown in mass transport limited regime. Figure (a) illustrates the resultant nanopillar, and (b) is a cross-section slice through the middle of the top of the nanopillar (color code of deposited atoms: red—primary ions (PI), blue—backscattered ions (BSI), green—forward scattered ions (FSI), yellow—SE-I electrons, and cyan—SE-II electrons). Figure (c) is the sampled deposition efficiency (atoms deposited per ion) for the different types of deposited species as a function of the number of ions (i.e. time). Figure (d) is the sampled ion and secondary electron coefficients as a function of the number of ions (i.e. time).

![](./images/811797862991003648_5.jpg)

![](./images/811797862991003648_6.jpg)

Figure 5. Schematic illustrating the precursor gas coverage (purple spheres) on the nanopillars for the (a) reaction rate limited growth and (b) the mass transport limited growth at the end of the simulated growth. Figure (c) is a plot of the incremental coverage (every 1 nm) as a function of the $z$-position on the nanopillar which demonstrates the unity coverage for the reaction rate limited growth and the gradient in the coverage over the beam interaction region.

limited regime. For instance, the secondary electron yields saturate at slightly lower values and the SE-II contribution is greater than the SE-I. This is due to the increased radial dimension and the convention that the SE-I cutoff was five scattering events. The wider pillar decreases the escape probability of the electrons and the primary ion travels further in the solid thus the transition to a higher SE-II coefficient.

As for the deposition efficiencies, first of all, in the mass transport limited regime simulated here, the deposition efficiencies are all lower than the reaction rate limited simulations because the precursor occupied surface site density in the beam interaction region ranges from approximately 15 to 90%, as compared to effectively 100% for the reaction rate limited regime. The SE-II deposition efficiency is much higher than the SE-I deposition efficiency which is partly due to the increase in the SE-II coefficient and partly due to the increased site occupancy farther from the pillar apex where the SE-II are preferably generated and escape. Figure 5 shows a snapshot of the (a) reaction rate and (b) mass transport pillar with occupied gas sites plotted at the end of the simulation, which demonstrates the occupied site density variation in the beam interaction region. Figure 5(c) shows the precursor surface coverage as a function of nanopillar height (measured in one nanometer increments as the number of gas sites occupied divided by the number of gas sites available). Clearly reaction rate limited pillar is fully covered and the mass transport pillar coverage varies from ~15% coverage near the apex to 100% coverage below the beam interaction region. The primary helium ion deposition is again constant, and the forward scattered ion deposition increases as the nanoscale topology develops and eventually saturates as the effective beam interaction region (~45 nm) is developed. The ~45 nm cone dimension at the top of the nanopillar is consistent with the saturation in the forward scattered ion and SE-I and II deposition efficiency which occurs at ~10 million ions at a nanopillar height of ~50 nm. The BSI deposition efficiency behaves similar to the RRL regime; namely it increases slightly during the initial pillar deposition and then decreases rather than saturates due to the finite extent of the simulation area.

Interestingly the vertical deposition rate is much smaller in the MTL pillar relative to the overall change in the deposition efficiency. As noted, this is what is responsible for the pillar broadening as the vertical growth rate is significantly decreased which allows the lateral growth in the beam interaction region to broaden the pillar.

The $He^+$ IBID simulation parameters were deliberately similar to previous electron beam induced deposition simulations (the same beam profile, localized precursor flux and currents, precursor, etc) so comparisons could be made [9, 10]. The main difference in comparing these simulations is that our EBID simulations have been performed for electron beam energies at low beam energies (1 and 5 keV) due to limitations of the plural scattering electron-solid Monte Carlo. Conveniently however, as pointed out by Livengood and Thomson [7, 23], when comparing the beam interaction of a $He^+$ ion to an electron it is convenient to compare velocities rather than energies. Because of the mass difference (and ignoring relativistic effects appropriate at low energy), the helium ion velocity is about 1.2% of that of an electron. Thus the 25 keV $He^+$ ion beam has a velocity similar to an approximately 300 eV electron beam which is close to our previous 1 keV simulations.

Interestingly, the simulated reaction rate limited pillar diameters for 1 keV electrons (~5–6 nm) and 25 keV $He^+$ ions (7–8 nm) are similar and the overall deposition efficiency per incident particle is high (~25% for 1 keV electrons and 40% for 25 keV $He^+$ ions) [8]. Coincidentally the primary

$He^{+}$ ion at 25 keV and the electron at 1 keV have similar cross-sections and thus the deposited species per ion are similar ($\sim$4% for 25 keV $He^{+}$ ion and $\sim$4.5% for 1 keV electron). The slightly higher growth efficiencies for the helium ion are due to the higher SE-I, SE-II, and forward scattered ion efficiencies. Surprisingly, the vertical growth rate is slightly higher for the 1 keV electrons ($2.24 \times 10^{-4}$ nm/electron) and appears to be due to a small contribution from backscattered electrons. Thus the slight broadening in the 25 keV $He^{+}$ ion beam growth relative to the 1 keV electron beam growth is due to a combination of competing effects. The slightly slower growth rate and higher SE-II and forward scattered ion deposition efficiencies both contribute to the lateral broadening.

The mass transport limited growth of the 25 keV $He^{+}$ ions relative to the 1 keV electrons is also an interesting comparison. First of all, the 25 keV helium ion beam is about twice the diameter of the 1 keV electron beam (22 nm versus 10.75 nm). The overall growth efficiencies per incident particle are much lower for the 1 keV electron beam (2.9%) relative to the 25 keV $He^{+}$ ion beam (11%). Importantly, even though the overall growth efficiency is almost $4\times$ greater for the 25 keV He ion, the vertical growth rate is slightly greater for the 1 keV electron beam ($5.7 \times 10^{-6}$ nm/electron [10]), which is again likely due to the backscattered electrons which contribute to the vertical growth and not because the primary particle efficiency (primary electron $=0.15\%$, primary ion $=0.27\%$). The observed broadening in the $He^{+}$ ion beam is due to several important factors. First of all, the total secondary electron coefficient is $5\times$ greater for the 25 keV ion beam ($\sim$8.5) relative to the 1 keV electron beam (1.7) which translates into $\sim$$5\times$ increase in the SE (I + II) deposition efficiency. Additionally, the total forward plus backscattered ion yield is approximately 1, whereas the 1 keV electron beam is $\sim$0.8; furthermore the ratio of the forward scattered to backscattered deposition yield for the ion beam (10/1) is much higher than for the electron beam (3/1). Finally, the forward scattered ion deposition efficiency is much larger for the 25 keV $He^{+}$ ion (5%) relative to the forward scattered electron (1%). The increased efficiency is due to a combination of effects including: (1) there are more FSIs than FSEs; (2) the cross-section for the ions is slightly higher cross-section over the relevant energy ranges; and (3) higher occupied gas density in the cumulative beam interaction region (see Smith, *et al* [11] for more details).

Finally, we attempt to make a quantitative comparison of our simulated results to experimental $He^{+}$ IBID data. Due to the relative infancy of the focused ion beam instrument, to our knowledge, Sanford *et al* [4] is the first report on focused $He^{+}$ IBID. Thus we do a brief comparison of our simulated results to their work. In this paper, the Sanford *et al* compare the deposited volumes and deposit composition to various scanning parameters. Unfortunately, this study focused on area scans so no comparison to the pillar morphology could be made. Based on their analysis and a brief review of their conditions, their growth appears to be in a mass transport limited regime. Namely, the volumetric growth efficiency (volume/dose) increases with decreasing current. Thus we compare our effective growth efficiency of tungsten with the $WF_{6}$ precursor to the Pt–C deposition using the $C_{9}H_{16}Pt$ precursor. For our comparison, we have calculated an effective growth efficiency (precursor atoms/electron) based on their maximum volumetric growth efficiency ($0.6\ \mu\mathrm{m}\ \mathrm{nC}^{-1}$ for 1 pA current). To reduce the volume to the number of precursor atoms dissociated, we use the precursor diameter of 0.356 nm, which is upper estimate since the precursor is fragmented and the resultant deposit is smaller. To compensate for the upper estimate, a packing factor of 100% was assumed. Based on these assumptions, the effective deposited efficiency (precursor atoms deposited/$He^{+}$) is $\sim$18%. While only an estimate, one which can vary significantly depending on the mass transport properties, the value is in reasonable agreement with the mass transport limited tungsten deposit efficiency which was determined to be 11%.

In summary, we report for the first time results from a Monte Carlo $He^{+}$ ion beam induced deposition simulation. The details of the simulation are briefly reviewed and the two growth regimes are compared; namely the reaction rate and mass transport limited growth of tungsten nanopillars from a $WF_{6}$ precursor. The reaction rate limited growth results in fast vertical growth and consequently smaller diameter (7–8 nm) nanopillars. Mass transport limited growth, conversely, has slower vertical growth and subsequently more lateral growth leading to wider ($\sim$22 nm) nanopillars. The resultant nanopillar growth morphologies are correlated to the relevant primary ion and subsequent secondary electron trajectories in the solid. Finally, the 25 keV $He^{+}$ ion beam induced deposition results were compared to previous electron beam induced deposition simulations of 1 keV electrons and recent $He^{+}$ ion beam induced deposition experiments. Future work will include trying to extract relevant helium ion beam induced dissociation cross-sections similar to our recent attempts at extracting EBID parameters [24]. Additionally we will compare different beam energy, materials, as well as surface diffusion effects which are expected to be different than comparable electron beam induced processing because of the secondary electron magnitude as well as the differences stopping power functionality.

## Acknowledgments

The authors would like to acknowledge support of the Semiconductor Research Corporation (Dan Herr program manager). PDR also acknowledges that a portion of this research was conducted at the Center for Nanophase Materials Sciences, which is sponsored at Oak Ridge National Laboratory by the Division of Scientific User Facilities, US Department of Energy.

## References

[1] Postek M T and Vladar A E 2008 *Scanning* **30** 457
[2] Bell D C 2009 *Microsc. Microanal.* **15** 147
[3] Scipioni L *et al* 2009 *J. Vac. Sci. Technol. B* **27** 3250
[4] Sanford C A *et al* 2009 *J. Vac. Sci. Technol. B* **27** 2660
[5] Bell D C *et al* 2009 *Nanotechnology* **20** 455301
[6] Winston D *et al* 2009 *J. Vac. Sci. Technol. B* **27** 2702
[7] Livengood R H *et al* 2007 *J. Vac. Sci. Technol. B* **27** 2547

[8] Ramachandra R, Griffin B and Joy D 2009 *Ultramicroscopy* **109** 748

[9] Smith D A, Fowlkes J D and Rack P D 2007 *Nanotechnology* **18** 265308

[10] Smith D A, Fowlkes J D and Rack P D 2008 *Nanotechnology* **19** 415704

[11] Smith D A, Fowlkes J D and Rack P D 2008 *Small* **9** 1382

[12] Fowlkes J D, Randolph S J and Rack P D 2005 *J. Vac. Sci. Technol. B* **23** 2825

[13] Ziegler J F, Biersack J P and Littmark U 1985 *The Stopping and Range of Ions in Solids* vol 1 (New York: Pergamon)

[14] Salow H 1940 *Phys. Z.* **41** 434

[15] Tanuma S *et al* 2005 *Surf. Interface Anal.* **37** 833

[16] Kotera M 1989 *J. Appl. Phys.* **65** 3991

[17] Scheinfein M R, Drucker J and Weiss J K 1993 *Phys. Rev. B* **47** 4068

[18] Large L N 1963 *Proc. Phys. Soc.* **81** 1101–3

[19] Petzold H C and Heard P J 1991 *J. Vac. Sci. Technol. B* **9** 2664

[20] Friedli V *et al* 2007 *Appl. Phys. Lett.* **90** 053106

[21] Chen P, Salemink H W M and Alkemadeohya P F A 2009 *J. Vac. Sci. Technol. B* **27** 2718

[22] Ohya K *et al* 2009 *Nucl. Instrum. Methods Phys. Res. B* **267** 584

[23] Thomson J J 1912 *Phil. Mag.* **24** 209

[24] Fowlkes J D and Rack P D 2010 *ACS Nano* **4** 1619