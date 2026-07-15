# Graded-index structures for high-efficiency solar thermophotovoltaic emitting surfaces

Craig Ungaro,¹ Stephen K. Gray,² and Mool C. Gupta¹,∗

¹Department of Electrical & Computer Engineering, University of Virginia, Charlottesville, Virginia 22901, USA
²Center for Nanoscale Materials, Argonne National Laboratory, 9700 South Cass Avenue, Argonne, Illinois 60439, USA
∗Corresponding author: mgupta@virginia.edu

Received February 20, 2014; revised April 6, 2014; accepted May 4, 2014;
posted July 31, 2014 (Doc. ID 206836); published September 3, 2014

This Letter presents a highly efficient emitter structure for solar thermophotovoltaic systems. The structure consists of a graded index on tungsten, shows a spectral efficiency of 59%, or 70% with the use of a back reflector, and is compared to other state-of-the-art emitter structures. The effects of different structures and periodicities on the efficiency of the emitter are explored, as well as the effect of a protective oxide coating. The causes of the antireflection properties of these structures are also explored. © 2014 Optical Society of America

OCIS codes: (160.4760) Optical properties; (350.6050) Solar energy.
http://dx.doi.org/10.1364/OL.39.005259

Solar thermophotovoltaic (STPV) systems provide increased efficiency for solar power conversion by using an intermediary material to absorb incoming sunlight, convert it to heat, and then re-emit it in a narrow band as thermal radiation, where it is absorbed by a photovoltaic (PV) cell. This is shown in Fig. 1. This increases efficiency, since the narrowband emission is better matched to a PV cell [1]. Spectral matching allows STPV systems to bypass the Shockley–Queisser limit and reach extremely high theoretical efficiencies of 85.4% [2].

Previous work by the authors has focused on efficient solar absorbing surfaces for STPV systems [3]. This work focuses on a separate component of the STPV system that emits the absorbed solar energy as thermal radiation. These absorbing and emitting surfaces play a critical role in the efficiency of STPV systems, and the combination of the two surfaces presented in this and the previous work will result in a highly efficient STPV system.

In order to improve spectral matching between thermally emitted radiation and the PV cell bandgap, the spectrum of the emitted radiation must be narrowed. Narrowing of the emitted radiation spectrum can cause a large increase in efficiency [4]. This can be accomplished by using a selective emitter or by placing a filter in front of the PV cell; however, filters placed in front of the PV cell can reduce efficiency and must operate on a diverging beam in high temperatures [5]. Sub-bandgap photons that transmit through the PV cell can also be reflected back to the emitter by a mirror placed behind the cell, called a back reflector [4]. This work combines the use of graded-index-type selective emitter structures with a back reflector to create a highly efficient STPV system.

There are a variety of selective emitters that have been studied for use in STPV systems, such as microcavities in tungsten, NiO-doped MgO films, titania nanofibers, rare-earth emitters, and photonic crystals [6–10]. While photonic crystals can provide a high-efficiency selective emitter, they are high cost and difficult to manufacture. Many photonic-crystal-based selective emitters also utilize materials such as Si and MgF₂ that have melting points in the range of STPV operating temperatures, as well as nanometer-scale geometry that has problems related to long-term stability at high operating temperatures [8,11].

Square gratings have also been explored in past work but suffer from relatively low absorption in the near-IR region due to their sudden change in index of refraction [12,13]. The absorption spectrum can be broadened via combining multiple periods of gratings; however, these structures still lack broadband absorption in the visible and near-IR region [14]. Blazed gratings can show higher absorption due to their graded-index-type behavior at certain wavelengths [15]. Pyramidal and cone-type structures also show similar high absorption due to graded index behavior.

This work presents a periodic microtexture on a tungsten surface that can provide selective emission with the use of only a protective coating. This coating is a single layer, and varied layer thickness can be tolerated. The elimination of multilayer coatings is advantageous for high-temperature operation and long-term stability [16]. The protective material can be chosen to have a high melting point to protect the tungsten surface from oxidation. The optical properties of the system are controlled by the textured tungsten and not by the oxide layer. This is achieved via the use of a blazed grating on tungsten with a thin layer for protection. This Letter also investi-gates the use of pyramid- and cone-type graded-index structures. These structures have lower maximum efficiencies than blazed gratings within the parameters of this work; however, they can tolerate larger feature sizes and may be simpler to manufacture.

![](./images/814703273394044928_1.jpg)

Fig. 1. Diagram of a STPV system with a solar absorber and thermal emitter.

To describe the relative performance of various types of selective emitters, Eq. (1) (below) was used to calculate the spectral efficiency. This equation takes into account only the effect of the emitting surface and does not represent an overall efficiency. The microtextures proposed in this Letter are analyzed along with structures from other papers in the STPV field to demonstrate the viability of this texture for STPV applications.

The spectral efficiency consists of the fraction of the absorbed energy emitted by the selective emitter that the PV cell is able to use. The total available emitted spectral energy is found by multiplying the emittance of an emitter by the blackbody thermal radiation spectrum. This assumes that the STPV system temperature is at 1750 K. The actual absorption of solar energy is not considered here, because this Letter focuses on the emitting surface only, and the absorbing and emitting surfaces are in different locations. The amount of energy available for solar power conversion is then found by multiplying the number of photons available, as determined by the cell's bandgap energy. A bandgap energy of $E_{\text{bg}} = 0.726$ eV (corresponding to a wavelength of $\lambda_{\text{bg}} = 1707$ nm) was used, since GaSb is a commonly used PV cell in STPV applications [4]. Emitter temperature ranges from 1700 to 2200 K are common in STPV systems; however, a temperature of 1750 K is used in this simulation due to its prevalence [5,8]. Temperatures in this range have been used previously under experimental conditions [4].

The spectral efficiency is given by

$$
\text{Eff} = \frac{\int_{0}^{\lambda_{\text{bg}}} \frac{E_{\text{bg}}}{E_{\text{photon}}(\lambda)} B(\lambda, T)\epsilon_{s}(\lambda)\text{d}\lambda}{\int_{0}^{\infty} B(\lambda, T)\epsilon_{s}(\lambda)\text{d}\lambda}, \tag{1}
$$

where $B(\lambda, T)$ is Planck's law for the spectral radiance of a blackbody at temperature $T$, $\epsilon_{s}(\lambda)$ is the emittance of the emitter, which is equal to absorbance or 1—reflectance, $E_{\text{photon}}(\lambda)$ is the energy of a photon of wavelength $\lambda$, $E_{\text{bg}}$ is the bandgap energy of the PV cell used, and $\lambda_{\text{bg}}$ is the wavelength of a photon with the bandgap energy.

To maximize conversion efficiency, the emitter must minimize emitted radiation with energy below and far above the bandgap. The focus of this Letter is to illustrate that the performance of existing emitter structures can be enhanced with a simple graded-index structure on tungsten.

Bare tungsten has a very high (greater than 90%) reflection in the 2–10 μm wavelength range, and a lower (40%–90%) reflection in the visible to 2 μm wavelength range [17]. This reflection spectrum, combined with its high melting point of 3695 K, makes tungsten a good candidate for an emitter material for a STPV system.

This work uses finite-difference time domain (FDTD) modeling to examine the effect of various microtextures on the reflectance spectrum of tungsten, with the goal of finding an easy-to-manufacture texture that can increase the spectral efficiency of tungsten for STPV applications [18]. An open-source implementation of the FDTD algorithm, MIT electromagnetic equation propagation (MEEP), was used for the simulations performed in this work [19]. In an FDTD simulation, a solution is found by iteratively solving Maxwell's equations on a grid.

A Gaussian source was used to excite electrical and magnetic fields, and structures were specified via the dielectric constants of the grid at each location. Perfectly matched layer boundary conditions were used in the direction of the light propagation, while Bloch periodic boundary conditions were used in the lateral directions. This allows an infinitely large surface to be simulated. The surfaces described in this Letter were modeled with a 1 μm thick tungsten substrate beneath the graded structures. Transmission was recorded to be less than 0.01%. An accurate Drude plus multiple Lorentzian model for tungsten was used to describe its dielectric constant in the simulated wavelength range [20]. While room temperature optical constants were used, the expected change in the emissivity of tungsten from room temperature to 1900 K is only 3.3% [21]. This simulation approximated an unpolarized light source by using the average reflectance of a P-polarized and S-polarized incident wave.

The structure used to control the emission spectrum is a blazed grating. When the grating period is smaller than the wavelength of incoming radiation, the grating will operate as a subwavelength grating. Subwavelength gratings do not have any propagating diffractive modes (only zero-order modes are allowed in this condition), and they demonstrate broadband antireflection properties at wavelengths larger than the first order of diffraction due to their graded index characteristics [22,23]. Blazed gratings in particular provide a more gradual index gradient when compared to square gratings, increasing their antireflection properties [15].

Figure 2(a) shows the blazed grating on a tungsten surface that was found to have the highest spectral efficiency. It has a height of 285 nm and a period of 200 nm. First-order diffraction will occur at a wavelength of 188 nm for this grating according to the grating equation. For wavelengths longer than 188 nm, this grating will act as a zero-order grating.

Figure 2(b) uses a FDTD model to compare the reflections of square and blazed gratings with a 600 nm period and a height of 450 nm. While the square grating provides an intermediary change in the effective index of refraction between the metal and air, this is less effective than

![](./images/814703273394044928_2.jpg)

Fig. 2. (a) Surface of a blazed grating with a periodicity of 200 nm and a blaze angle of 55 deg, (b) FDTD calculation of the reflectance of square and blazed gratings, both with a 600 nm periodicity, and an optimized structure with a 200 nm periodicity.

the gradual index change provided by a blazed grating. Surface plasmons and the microcavity effect cause absorption peaks in the case of the square grating; however, these peaks are narrow and do not provide broad absorption of solar radiation [24]. The blazed grating shows a broader band of low reflection than the square grating in the visible region while maintaining a high reflectance in the IR region. This results in higher efficiency due to enhanced solar absorption.

At the zero-order condition, gratings exhibit specular reflection properties and no diffraction [25]. The emission of light at wavelengths longer than 188 nm is not expected to have an angular dependency beyond that of Lambert's cosine law. FDTD simulations show a change in spectral efficiency from 0.59 to 0.58 when Eq. (1) is integrated from $-85^\circ$ to $85^\circ$. Equation (1) is used without angular dependence due to a lack of data in many references.

The height and periodicity of this grating were varied, and the spectral efficiency was calculated at each point, as shown in Fig. 3. While decreasing the periodicity further below 200 nm resulted in a small ($<$1%) increase in efficiency, these data were not included in this Letter due to concerns about the viability of manufacturing such a structure. While the maximum spectral efficiency of 0.59 can be seen at a period of 200 nm and blaze angle of $55^\circ$, other periods and angles show promise as well. At a period of 600 nm and a blaze angle of $35^\circ$, the spectral efficiency is 0.57. Cone- or pyramid-type structures also maintain high spectral efficiencies of over 0.56 at a 900 nm periodicity and an angle of $25^\circ$ and can be fabricated using standard optical lithography [26]. Larger feature sizes may be desirable due to increased manufacturability and thermal stability.

Figure 4 shows the thermal emission of a blazed grating on tungsten with a period of 200 nm and a blaze angle of $55^\circ$ as compared to the blackbody spectrum at a temperature of 1750 K. The blazed grating results in a much larger portion of the emitted radiation occurring at wavelengths that are usable by a GaSb PV cell. The spectral efficiency of a blackbody radiator is only 0.23, while it is 0.59 for a blazed grating, making the surface structure presented in this Letter highly efficient in comparison.

The effect of a protective oxide film on the spectral efficiency was also examined. A protective oxide will allow the textured tungsten to operate at high temperatures without oxidation on the surface [27]. An oxide of $\mathrm{Al_2O_3}$ was chosen for simulation in this work due to its high temperature stability and melting point of 2345 K. It was found that there is a small (less than 1%) loss in spectral efficiency at an oxide thickness of up to 100 nm. This allows the use of a protective oxide layer on the emitter while maintaining high spectral efficiency.

![](./images/814703273394044928_3.jpg)

Fig. 3. Spectral efficiency versus periodicity and angle of blazed grating on tungsten. The angle is the angle of the blazing, with $0^\circ$ meaning a flat surface.

![](./images/814703273394044928_4.jpg)

Fig. 4. Thermal emission of a blackbody and blazed grating on a tungsten substrate with a periodicity of 200 nm and an angle of $55^\circ$. The vertical line is the absorption edge of a GaSb PV cell.

<table>
<caption>Table 1. Spectral Efficiency Calculations</caption>
<thead>
<tr>
<th>Emitter Type</th>
<th>Spectral Efficiency</th>
</tr>
</thead>
<tbody>
<tr>
<td>Blazed grating on tungsten</td>
<td>0.59 (this work)</td>
</tr>
<tr>
<td>Microcavity in tungsten</td>
<td>0.49 [6]</td>
</tr>
<tr>
<td>NiO-doped MgO films</td>
<td>0.61 [9]</td>
</tr>
<tr>
<td>Titania nanofibers</td>
<td>0.49 [6]</td>
</tr>
<tr>
<td>Rare earth ($\mathrm{Yb_2O_3}$)</td>
<td>0.54 [6]</td>
</tr>
<tr>
<td>Photonic crystals on tungsten</td>
<td>0.63 [8]</td>
</tr>
<tr>
<td>Complex square grating on tungsten</td>
<td>0.53 [14]</td>
</tr>
</tbody>
</table>

Table 1 shows the spectral efficiency of the blazed grating on tungsten compared to other emitters found in the literature. The results shown in Table 1 were obtained by applying Eq. (1) to the emission spectra presented in each reference.

This work presents a solution for a high-efficiency, temperature-stable, and manufacturable graded-index emitter for use in STPV systems. It also investigates structures that allow for larger periods while maintaining a high spectral efficiency. The availability of such a structure combined with the absorbing structure for high-temperature STPV systems presented in the authors' previous work could have a large impact on the STPV field [3].

We thank the NASA Langley Professor and NSF IUCRC Programs for their support of this project. This work was performed, in part, at the Center for Nanoscale Materials, a U.S. Department of Energy, Office of Science, Office of Basic Energy Sciences User Facility, under Contract No. DE-AC02-06CH11357.

### References

1. R. M. Swanson, Proc. IEEE **67**, 446 (1979).
2. P. A. Davies and A. Luque, Sol. Energy Mater. Sol. Cells **33**, 11 (1994).
3. C. Ungaro, S. K. Gray, and M. C. Gupta, Appl. Phys. Lett. **103**, 071105 (2013).
4. V. M. Andreev, V. P. Khvostikov, O. A. Khvostikova, A. S. Vlasov, P. Y. Gazaryan, N. A. Sadchikov, and V. D. Rumyantsev, *IEEE Photovoltaic Specialists Conference* (2005), pp. 671–674.

5. H. Hofler, H. J. Paul, W. Ruppel, and P. Wurfel, Solar Cells **10**, 273 (1983).

6. Y. Xuan, X. Chen, and Y. Han, Renew. Energy **36**, 374 (2011).

7. B. Bitnar, W. Durisch, J. C. Mayor, H. Sigg, and H. R. Tschudi, Sol. Energy Mater. Sol. Cells **73**, 221 (2002).

8. E. Rephaeli and S. Fan, Opt. Express **17**, 15145 (2009).

9. L. G. Ferguson and F. Dogan, Mater. Sci. Eng. B **83**, 35 (2001).

10. S.-Y. Lin, J. Moreno, and J. G. Fleming, Appl. Phys. Lett **83**, 380 (2003).

11. N. P. Sergeant, O. Pincon, M. Agrawal, and P. Peumans, Opt. Express **17**, 22800 (2009).

12. H. Sai and H. Yugami, Appl. Phys. Lett. **85**, 3399 (2004).

13. H. Sai, Y. Kanamori, K. Hane, H. Yugami, and M. Yamaguchi, *Photovoltaic Specialists Conference* (2005), pp. 762–765.

14. Y. B. Chen and Z. M. Zhang, Opt. Commun. **269**, 411 (2007).

15. E. B. Grann and M. G. Moharam, J. Opt. Soc. Am. A **13**, 988 (1996).

16. V. Rinnerbauer, S. Ndao, Y. X. Yeng, W. R. Chan, J. J. Senkevich, J. D. Joannopoulos, M. Soljacic, and I. Celanovic, Energy Environ. Sci. **5**, 8815 (2012).

17. E. D. Palik, *Handbook of Optical Constants of Solids* (Academic, 1985).

18. A. Taflove and S. C. Hagness, *Computational Electrody- namics: the Finite-Difference Time-Domain Method*, 3rd ed. (Artech House, 2005).

19. A. F. Oskooi, D. Roundy, M. Ibanescu, P. Bermel, J. D. Joannopoulos, and S. G. Johnson, Comput. Phys. Commun. **181**, 687 (2010).

20. H. P. Chiang, P. T. Leung, and W. S. Tse, J. Chem. Phys. **108**, 2659 (1998).

21. A. G. Worthing, J. Opt. Soc. Am. Rev. Sci. Instr. **13**, 635 (1926).

22. W. Stork, N. Streibl, H. Haidner, and P. Kipfer, Opt. Lett **16**, 1921 (1991).

23. K.-H. Kim and Q.-H. Park, Sci. Rep. **3** (2013).

24. H. Sai, Y. Kanamori, K. Hane, and H. Yugami, J. Opt. Soc. Am. A **22**, 1805 (2005).

25. C. Palmer, *Diffraction Grating Handbook* (Newport Corporation, 2005).

26. G. Owen, R. Pease, D. Markle, A. Grenville, R. Hsieh, R. von Bunau, and N. Maluf, J. Vac. Sci. Technol. B **10**, 3032 (1992).

27. K. A. Arpin, M. D. Losego, and P. V. Braun, Chem. Mater. **23**, 4783 (2011).