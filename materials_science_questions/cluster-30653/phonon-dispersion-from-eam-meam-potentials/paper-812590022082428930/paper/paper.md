# Cu(111) and Ag(111) surface-phonon spectrum: The importance of avoided crossings
J. S. Nelson, M. S. Daw, and Erik C. Sowa*
Sandia National Laboratories, Livermore, California 94550-5800
(Received 13 March 1989)

Embedded-atom method (EAM) calculations of the phonon energies, polarizations, and first- and second-neighbor interatomic-force-constant tensors of the clean Cu(111) and Ag(111) surfaces are presented. Using embedded-atom parameters fit to bulk properties, we find that the EAM provides an accurate and detailed description of the lattice dynamics of these surfaces, in good agreement with the measured surface vibrational spectra. We find only modest 10-15 % changes in the sur- face force constants for both Cu and Ag from their bulk values. Our calculations also suggest an ex- planation for the anomalous softening of the longitudinal resonance mode along the $\Gamma M$ symmetry line in terms of an avoided crossing of first- and second-layer sagittal-plane modes.

## I. INTRODUCTION

Over the past several years the charge redistributions and force-constant changes at fcc noble-metal (111) sur- faces have received considerable attention. Information regarding these modifications can be obtained from an analysis of the surface-phonon dispersion curves provided by helium time-of-flight $^{1}$ (TOF) and electron-energy-loss spectroscopy $^{2}$ (EELS) experiments. The changes in fre quency of the surface-related vibrational modes from their bulk values are directly related to these force- constant modifications. A general agreement between researchers in this field on the magnitude of these changes has not yet been achieved.

Helium TOF measurements have been obtained for all the noble-metal (111) surfaces, $^{3-5}$ and EELS measure ments are available for the $Cu(111)$ surface. $^{6}$ The surface-phonon spectra for both the He TOF and the EELS measurements are in good agreement at low fre- quency. The EELS measurements also find additional high-frequency modes not seen in the He-scattering ex- periments. The existence of these high-frequency modes has raised some important questions relating to the ear- lier theoretical analysis of the He-scattering experi- ments. $^{7-9}$ Hall et al. $^{10}$ have discussed these questions in great detail. The main point of controversy is the amount of softening of the intralayer force constants necessary to account for the observed position of the longitudinal-resonance (LR) mode. Values of the soften- ing which range from $15 \%$ to $70 \%$ have been proposed.In their study of the $Ag(111)$ surface, Bortolani et al. $^{7}$  used a force-constant model with central and angular in- teractions including up to second neighbors. The surface force constants were determined by fitting the measured inelastic He-scattering cross sections. This procedure produced a $48 \%$ softening of the surface nearest-neighbor radial intralayer force constant for $Ag$ and $Cu$ , and a much larger value for $Au$ of $70 \%$ . On the other hand, us ing a much simpler nearest-neighbor central-potential(NNCP) model, Hall et al. $^{10}$ reproduced the observed Cu(111) surface-phonon spectrum and the inelastic-electron-scattering intensities with only a $15 \%$ reduction: this is a value similar to the one we have found on the $Cu(111)$ surface. $^{11}$ Jayanthi et al., $^{12}$ using a many-body description of the surface lattice dynamics, found approx- imately a $30 \%$ reduction in the intralayer radial force constant.

The purpose of this paper is to present a detailedtheory of the lattice dynamics of the $Cu(111)$ and $Ag(111)$  surfaces, and to provide an explanation for the controver- sy that has existed for these surfaces. We will see that the avoided crossing of surface modes, which has previously been observed on other transition and noble-metal sur- faces, $^{13}$ plays a critical role in the lattice dynamics of the(111) $Cu$ and $Ag$ surfaces. We will see that modes along IM can be explained in terms of an avoided crossing, without the need for a large softening of the surface in- tralayer force constant.

Our calculations are performed using the embedded- atom method (EAM), $^{14}$ which incorporates many-body interactions into the expression for the total energy. The EAM is computationally no more expensive to use than pair potentials, and has been shown to provide a good description of bulk phonons, $^{15}$ surfaces, $^{16}$ defects, $^{17}$ and liquids. $^{18}$ Within this method, the relaxations and changes in surface force constants are predicted in one consistent framework. Recently, the EAM has been used to calculate a $Cu(100)$ surface-phonon spectrum $^{11}$ which is in excellent agreement with experiment. On this sur- face, we calculated a change in the surface force con- stants of approximately $15 \%$ . The rest of the paper is or ganized as follows. In Sec. II we give a discussion of the our method, in Sec. III our results are presented, and in Sec. IV a summary is provided.

## II. METHOD

In the EAM (Ref. 14) the total energy of an arbitrary arrangement of atoms is given by
$$E_{\text {tot }}=\sum_{i} F_{i}\left(\rho_{i}\right)+\frac{1}{2} \sum_{i, j}^{(i \neq j)} \phi_{i j}\left(R_{i j}\right).\qquad(1)$$

In this expression, $\rho_{i}$ is the electron density at atom $i$ due to the remaining atoms of the system, $F_{i}(\rho)$ is the energy

to embed atom $i$ into the background electron density $\rho$, and $\phi_{i j}(R_{i j})$ is a short-ranged electrostatic repulsion between atoms $i$ and $j$ separated by a distance $R_{i j}$. The embedding energy represents the interaction of an atom with the local electron gas provided by all other atoms and thereby accounts for the cohesive energy of the solid. To make Eq. (1) of practical use, an approximation for the electron density $\rho_{i}$ at atom $i$ is provided by a linear superposition of atomic electron densities

$$
\rho_{i}=\sum_{j(\neq i)} \rho_{j}^{a}\left(R_{i j}\right), \quad(2)
$$

where $\rho_{j}^{a}(R_{i j})$ is the atomic electron density at atom $i$ due to atom $j$. The functions in Eq. (1) were determined in previous work by fitting to the following bulk properties: equilibrium lattice constants, sublimation energies, elastic constants, vacancy-formation energies, and binary alloy heats of formation. $^{17}$ They are used in this work without modification.

The force $\mathbf{F}_{i}$ exerted on atom $i$ when atom $j$ is moved by $d \mathbf{R}_{j}$ is given by the force-constant $\mathrm{K}_{i j}$, which can be obtained in a straightforward way from Eqs. (1) and (2). The result is

$$
\begin{aligned}
\mathrm{K}_{i j}= & \frac{\partial^{2} E_{\mathrm{tot}}}{\partial \mathbf{R}_{i} \partial \mathbf{R}_{j}} \\
= & -\mathrm{A}_{i j}+F_{i}^{\prime \prime} \rho_{j}^{a \prime}\left(R_{i j}\right) \hat{\mathbf{r}}_{j i} \mathbf{g}_{i}+F_{j}^{\prime \prime} \mathbf{g}_{j} \rho_{i}^{a \prime}\left(R_{i j}\right) \hat{\mathbf{r}}_{i j} \\
& +\sum_{k(\neq i, j)} F_{k}^{\prime \prime} \rho_{j}^{a \prime}\left(R_{j k}\right) \rho_{i}^{a \prime}\left(R_{i k}\right) \hat{\mathbf{r}}_{j k} \hat{\mathbf{r}}_{i k},
\end{aligned}
$$

where
$$
\begin{aligned}
& \mathrm{A}_{i j}=\psi_{i j}^{\prime \prime} \hat{\mathbf{r}}_{i j} \hat{\mathbf{r}}_{i j}+\psi_{i j}^{\prime}\left(\mathbb{1}-\hat{\mathbf{r}}_{i j} \hat{\mathbf{r}}_{i j}\right) / R_{i j}, \\
& \psi_{i j}\left(R_{i j}\right)=F_{i}^{\prime}\left(\rho_{i}\right) \rho_{j}^{a}\left(R_{i j}\right)+F_{j}^{\prime}\left(\rho_{j}\right) \rho_{i}^{a}\left(R_{i j}\right)+\phi_{i j}\left(R_{i j}\right), \quad(3 \mathrm{~b}) \\
& \mathbf{g}_{i}=\sum_{j(\neq i)} \rho_{j}^{a \prime}\left(R_{i j}\right) \hat{\mathbf{r}}_{i j}.
\end{aligned}
$$

Here the unit vector $\hat{\mathbf{r}}_{i j}=\left(\mathbf{R}_{i}-\mathbf{R}_{j}\right) / R_{i j}$ points from atom $j$ to atom $i$, and the prime denotes differentiation with respect to the argument. The dynamical matrix $^{19}$ for the system, which yields the squared phonon frequencies and polarization, can be constructed using Eq. (3).

The tensor $\mathrm{A}_{i j}$ represents the contribution to $\mathrm{K}_{i j}$ from the environment-dependent effective pair potential $\psi_{i j}$. The other terms in $\mathrm{K}_{i j}$ include environment-dependent many-body contributions. $^{14,16}$ The environmental dependence of $\psi_{i j}$ is contained in the first derivatives of the embedding functions, $F_{i}^{\prime}$ and $F_{j}^{\prime}$, which are evaluated at the charge density at atoms $i$ and $j$. The environmental dependence of the many-body terms comes from the gradients of the charge densities at atoms $i$ and $j$ as measured by the quantities $\mathbf{g}_{i}$ and $\mathbf{g}_{j}$. The background charge density and its gradient will necessarily be different at the surface than in the bulk, thereby modifying the force constants and leading to shorter bond lengths and deeper potential wells at the surface. This can be more clearly seen by a comparison of the bulk and surface $\psi_{i j}$ for $\mathrm{Cu}$ and $\mathrm{Ag}$ shown in Figs. 1(a) and 1(b), respectively. The surface $\psi_{i j}$ has a minimum which is deeper and closer in. This is consistent with the general trend that lower coordination leads to stronger, shorter bonds. The interlayer relaxations and force-constant changes are thus obtained in one consistent calculation. Foiles $^{16}$ has discussed the changes in the effective pair and three-body terms for the fcc metals in some detail.

The surface vibrational spectrum is calculated using a 63-layer slab, which is thick enough so that the two surfaces do not interact. The positions for the relaxed surface slab were determined by minimizing the energy. A detailed comparison of the calculated surface structure with low-energy electron-diffraction (LEED) experiments

### (a) Effective Pair Potential of Cu
![](./images/812590022082428930_1.jpg)

### (b) Effective Pair Potential of Ag
![](./images/812590022082428930_2.jpg)

FIG. 1. Bulk and surface effective pair potentials $\psi_{i j}$ for $\mathrm{Cu}$ and $\mathrm{Ag}$. The surface $\psi_{i j}$ has a minimum which is deeper and closer in. This is consistent with the general trend that lower coordination leads to stronger shorter bonds.

is given in Ref. 17; the calculated values are within a few percent of the experiment. The real- and reciprocal-space unit cells of the (111) surface are shown in Fig. 2. The surface point group is $C_{3v}$. The $x$ direction is taken along the $[\overline{1}10]$, the $y$ direction along $[11\overline{2}]$, and the $z$ direction along [111]. Along $\Gamma M$, which has mirror-plane symmetry, the sagittal plane is defined by vibrational modes with $z$ and $y$ polarization (even modes), which do not couple to shear-horizontal modes with $x$ polarization (odd modes). Along $\Gamma K$, since there is no mirror plane, the vibrational modes cannot be decoupled into even and odd modes; consequently, all polarizations will mix. As will be seen below, the mixing of the modes along $\Gamma K$ is an important part of the explanation of the observed He-scattering data. $^{3}$

Once the vibrational spectrum has been calculated, the surface and resonance states can be identified by constructing the surface-vibrational local density of states (VLDOS). The amplitude for a selected degree of freedom, $|e_{i}^{n}|^{2}$ (where $i$ labels the Cartesian coordinate and $n$ identifies the layer), is plotted as the third coordinate of a three dimensional (3D) plot. $^{20}$ A vibrational mode which is fully localized on a single atom with purely longitudinal or transverse character should have a VLDOS equal to two (we have two surfaces in the slab calculation); the amount of localization is proportional to the height of the peaks seen in the VLDOS plots.

![](./images/812590022082428930_3.jpg)

Fig. 2. (a) Real and (b) reciprocal-space unit cells of the fcc (111) surface. The $z$ direction is along [111], the $x$ direction along $[\overline{1}10]$, and the $y$ direction along $[11\overline{2}]$. The large solid circles are the first-layer atoms, open circles represent second-layer atoms, and the hatched circles are third-layer atoms. The thick lines define the $(1\times 1)$ unit cell and the thin lines define the unit cell used to calculate the interatomic force-constant tensors. The surface atoms labeled 1, 2, and 4 and the second-layer atom labeled 3 will be used later for the force-constant-tensor evaluation (see Sec. III G).

## III. RESULTS

The results will be presented in the following order. Section III A, bulk-phonon spectrum; Sec. III B, general features of the Cu(111) and Ag(111) surface-phonon spectrum; Sec. III C, Cu(111) along $\Gamma M$; Sec. III D, Ag(111) along $\Gamma M$; Sec. III E, Cu(111) along $\Gamma K$; and Sec. III F, Ag(111) along $\Gamma K$. In Sec. III G the force-constant tensors predicted by the EAM are compared to those from the NNCP model.

### A. Bulk-phonon spectrum

In Fig. 3 we show the calculated and measured bulk phonons of fcc Cu (Ref. 21) and Ag (Ref. 22) along several symmetry lines. Good agreement between theory and experiment is found throughout the Brillouin zone for both Cu and Ag. Because the semiempirical EAM

![](./images/812590022082428930_4.jpg)

FIG. 3. Comparison of the experimental (points) and calculated (solid lines) bulk-phonon spectra for Cu and Ag along several symmetry directions. The experimental points for Cu (Ag) are from Ref. 23 (24). Good agreement between experiment and theory can be seen throughout the Brillouin zone. Note that the EAM functions are fitted to the elastic constants, assuring a reasonable fit at small wave vector.

functions were fitted to the experimental elastic con- stants, we are assured of a good fit for small wave vector $q$. Small discrepancies $(\sim 0.3$ THz) at the zone boun daries are observed for the several of the phonon modes, which is reasonable given the fact that no fitting to the zone-edge phonons has been done. The bulk zone-edge frequencies need not be fitted exactly to give a good description of the changes in the vibrational modes at the surface. Because we have not exactly reproduced the bulk-phonon spectrum, the most important quantity we will compare is the shift of the surface frequency from the bulk bands.

### B. (111) surface-phonon spectrum
The calculated vibrational spectra for the 63-layer Cu and Ag slabs are compared with He-scattering measure- ments $^{4}$ in Figs. 4(a) and 4(b), respectively. The EELS measurements of Mohamed et al. $^{6}$ along the $\Gamma M$ symmetry line of Cu are also shown in Fig. 4(a). Note the simi- larities between the vibrational spectrum of Cu and Ag, indicating that the calculated changes in force constants at the surfaces of these metals are very similar. There are several modes which appear to be split off from, or in the gaps of, the bulk vibrational spectrum. These modes are labeled $S_{1}, S_{2}$ , and $S_{3}$ .

![](./images/812590022082428930_5.jpg)

FIG. 4. Surface-phonon spectrum for 63-layer (a) Cu(111) slabs and (b) Ag(111) slabs. The experimental points are from Refs. 5 (He scattering). Along $\Gamma M$ of $Cu$ , the EELS measure ments (Ref. 6) are plotted instead of the He-scattering points. The He-scattering and EELS data are in good agreement. The modes which are split off from the bulk modes have been la- beled $S_{1}, S_{2}$ , and $S_{3}$ .

As can been seen in Figs. 4(a) and 4(b), the Rayleigh waves (RW's), $S_{1}$ , along $\Gamma M$ and $\Gamma K$ , are in good agree ment with the He-scattering data $^{4}$ for both $Cu$ and $Ag$ . Better agreement is found for Cu than for Ag since the bulk modes are more accurately represented in this case. For both $Cu$ and $Ag$ , the calculated split off of the RW's from the bulk is in good agreement with the experimental value. Recall that no fitting of the surface modes to ex- periment has been done.

For $Cu$ , the EELS data $^{6}$ show two features in the gap near the $M$ point. Our calculations exhibit only one mode in the gap identified with the lower branch of the experimental gap modes. The position of the $S_{2}$ gap mode at $M$ is in reasonable agreement with the EELS measurements; $^{6}$ the calculated modes are about $0.4 THz$  higher in energy, which can be traced to a similar discrepancy in the $L$ mode along $\Gamma X$ in the bulk [see Fig.3(a)]. As will be seen below, second-layer vertical and longitudinal modes above the $S_{2}$ gap can account for the higher branch of the experimental gap modes near the $M$ point. High-frequency modes corresponding to $S_{2}$ were not seen in the He-scattering experiments. $^{4}$

At $K$ , the $S_{3}$ mode has not been experimentally identified for either $Cu$ or $Ag$ .

Both the He-scattering $^{4}$ and the EELS (Ref. 6) experi ments observe modes that are resonant with the bulk vi- brational spectrum: the LR mode along $\Gamma M$ and $\Gamma K$ , and the higher-frequency modes along $\Gamma M$ of $Cu$ . Several interesting questions are suggested by the follow- ing experiments.

(1) Why does the surface LR mode have a value of 5.0 $THz$ at $M$ , while the bulk longitudinal edge is $7.8 THz$ ?
(2) Why does the He data $^{4}$ appear to follow the "odd" mode along $\Gamma K$ (assuming the He atom only interacts with the surface atom, the odd mode should not be ob- servable due to mirror-plane symmetry)?
(3) What vibrational excitations do the high-frequency EELS modes correspond to?

These questions can best be answered by considering in detail the surface VLDOS. Since we have not fitted to ex- periment, our results for the character of these modes will not be prejudiced by a fitting procedure; this is one of the attractive features of the EAM calculations of the surface phonon spectrum.

### C. $Cu(111)$ along $\Gamma M$
Let us examine the VLDOS of $Cu(111)$ along $\Gamma M$ , shown in detail in Fig. 5. Along $\Gamma M$ , the even modes have $y$ (longitudinal) and $z$ (transverse) polarizations; the odd vibrational modes have $x$ (shear-horizontal) polariza tion. The $e_{z}^{1}$ mode (first layer with $z$ polarization) plotted

in Fig. 5(a) exhibits only a weak localization at small wave vector, growing to about 50% at the zone boundary. Referring back to Fig. 4(a), the $S_1$ mode along $\Gamma M$ is split off from the bulk edge by a small amount, consistent with partial localization. The experimental $S_1$ is in nearly perfect agreement with this mode. Note also that the $e_z^1$ shows a small, almost constant disturbance at about 7 THz along $\Gamma M$, and from 0 to 5 THz at small wave vector. These regions correspond to bulk vibrations with some amplitude on the first-layer atom.

In Fig. 5(b) the amplitude for longitudinal polarization, $e_y^1$, exhibits a broad feature. This is a clear illustration of its resonant character. At $\Gamma$ the disturbance ranges from 0 to about 3.2 THz, and shows very little mixing with the $S_1$ mode. One very interesting feature can be seen in Fig. 5(b). At about $0.6k_{\Gamma M}$ the $e_y^1$ mode splits into two

![](./images/812590022082428930_6.jpg)

FIG. 5. Vibrational local density of states (VLDOS) of Cu along $\Gamma M$ for modes with (a) $z$ polarization and (b) $y$ polarization on the first-layer atom, $e_z^1$ and $e_y^1$, respectively. The small circles represent the He-scattering results of Ref. 5. The low-frequency disturbance in (a) is the $S_1$ Rayleigh wave seen in Fig. 4(a). The resonant character of the $e_y^1$ mode is clearly illustrated in (b). The large peak at the $M$ point in (b) corresponds to the $S_2$ gap mode in Fig. 4(a). The splitting of the $e_y^1$ mode at $0.6k_{\Gamma M}$ is due to the avoided crossings.

branches, one that continues up in energy to become the $S_2$ gap mode and another that flattens out at about 5.0 THz at large wave vector. From these results, we can clearly see that the $S_2$ gap mode is equivalent to the upper branch of the $e_y^1$ mode. The $S_2$ gap mode is, in the physical picture of Allen et al.,$^{23}$ the surface-related longitudinal mode peeling off from the bulk longitudinal edge into the gap. The question we must answer is why does the $e_y^1$ mode split into two distinct branches? The answer to this question is obtained by examining the longitudinal and transverse vibrations on the second-layer atoms, $e_z^2$ and $e_y^2$.

The VLDOS of the $e_z^2$ and $e_y^2$ modes are shown in Figs. 6(a) and 6(b), respectively. The mixing of $e_z^2$ with $e_z^1$ can be seen by the low-frequency mode in Fig. 6(a). Two other regions with significant $e_z^2$ amplitude can be seen in

![](./images/812590022082428930_7.jpg)

FIG. 6. VLDOS of Cu along $\Gamma M$ for modes with (a) $z$ polarization and (b) $y$ polarization on the second-layer atom, $e_z^2$ and $e_y^2$, respectively. The small circles represent the EELS scattering results of Ref. 6. The low-frequency feature in (a) is due to the decay of the Rayleigh wave into the bulk, while the high-frequency disturbance with a small amount of dispersion is a true $e_z^2$ mode. This mode interacts with the $e_y^1$ mode in Fig. 5(b), to produce the large feature at the $M$ point at about 5 THz.

Fig. 6(a): (1) a ridge at about 7 THz with very little dispersion, corresponding to some of the high-frequency EELS data, $^{6}$ and (2) a region that starts out at $0.6 k_{\Gamma M}$ and increases in amplitude towards point $M$. Note that this is in the same region where the $e_{y}^{1}$ mode splits into two branches. At $\Gamma$ the calculated $e_{y}^{2}$ mode is about 1THz higher in frequency than the experimental mode; part of this discrepancy is related to not reproducing the bulk modes exactly. Figure 6(b) shows many interesting features related to the $e_{y}^{2}$ mode: (1) significant mixing with $e_{y}^{1}$ , and (2) a very strong localization of this mode that starts at 3.2 THz and then proceeds to run along the back of the $e_{y}^{1}$ mode, ending at the $M$ point in the regionof the high-frequency EELS data. $^{6}$

A schematic representation of the modes involved in the avoided crossing is presented in Fig. 7. The first- and second-layer modes are indicated by solid and dashed lines, respectively. If we now follow $e_{y}^{1}, e_{z}^{2}$ , and $e_{y}^{2}$ to wards the $M$ point, we can see that they approach each other at about $0.6 k_{\Gamma M}$ . Since all these modes are of even symmetry (vibrations in the sagittal plane), they will have matrix elements coupling them, and consequently will avoid each other. This is the avoided crossing of themodes. The high-frequency $e_{z}^{2}$ mode interacts with the $e_{y}^{1}$  mode at $0.6 k_{\Gamma M}$ , resulting in the splitting of the $e_{y}^{1}$ mode seen in Fig. 5(b). The $e_{z}^{2}$ and $e_{y}^{2}$ modes also avoid each other. The first-layer $e_{y}^{1}$ mode accounts for the $S_{2}$ gap mode, and the second-layer $e_{y}^{2}$ mode can account for the second higher-frequency mode at the $M$ point seen in the EELS experiments. $^{6}$ If the $e_{z}^{2}$ mode [Fig. 6(a)] could be shifted down in frequency by 1 THz, bringing this mode into better agreement with experiment, then this would increase the interaction with the $e_{y}^{1}$ mode, shifting it to lower frequency, in better agreement with experiment.

A comparison of our results and that of Hall et al. $^{10}$  for the first- and second-layer amplitudes of vibrations at the $M$ point shows that both calculations find (1) that the S, gap mode is almost entirely related to the first-layer longitudinal vibrations $(e_{y}^{1})$ , and (2) the LR mode at the $M$ point is related to the second-layer vertical $(e_{z}^{2})$ and first-layer longitudinal $(e_{y}^{1})$ vibrations. The characters of the modes are in good agreement, with some small discrepancies in the actual frequencies. This level of discrepancy is reasonable given the very different force- constant models used in the calculations. Although the nearest-neighbor central-potential model used by Hall et al. $^{10}$ does not represent an accurate description of the long-wavelength vibrations, it does provide a reasonably good fit to the zone-edge vibrations, which are important for understanding the character of the LR and $S_{2}$ gap modes. The new feature that our results have provided isthe avoided crossing of the surface modes. Hall et al. $^{10}$  explained the LR mode and the $S_{2}$ gap mode as two dis tinct modes, whereas we can see from our results that they are actual intimately connected through the avoided crossing.

Bortolani et al. $^{7,8}$ and Jayanthi et al. $^{12}$ have also calcu lated the surface-vibrational modes of Cu(111) along $\Gamma M$ . Both of these calculations explain the position of the LR mode in terms of a large softening of the intralayer force constants, rather than an avoided crossing of sagital- plane modes as we have done.

### D. Ag(111) along $\Gamma M$
The sagittal-plane VLDOS of the first-layer atom, $e_{z}^{1}$  and $e_{y}^{1}$ , is compared to the He-scattering experiments inFig. 8. In this plot we have combined the VLDOS of $e_{z}^{1}$  and $e_{y}^{1}$ for convenience. Two main features can be seen inFig. 8: (1) a low-frequency peak corresponding to the $e_{z}^{1}$  mode, in good agreement with the lower experimental mode, and (2) a higher-energy structure corresponding to the $e_{y}^{1}$ mode. The second experimental mode follows the $e_{y}^{1}$ branch until about $0.3 k_{\Gamma M}$ and then flattens out to wards the zone boundary. In comparison with Cu [Fig.5(b)], the second experimental mode seems to deviatemore quickly from the $e_{y}^{1}$ branch. Similar to the Cu(111) $\Gamma M$ direction [Fig. 5(b)], the $e_{y}^{1}$ mode splits into two branches at $0.6 k_{\Gamma M}$ , with the lower branch having a somewhat smaller amplitude than in the Cu case. Note the large peak in the upper branch of the $e_{y}^{1}$ mode, corre sponding to the $S_{2}$ gap mode of Ag.

Second-layer-atom sagittal-plane VLDOS's, $(e_{z}^{2}+e_{y}^{2})$  are depicted in Fig. 9. These modes show many features similar to the Cu VLDOS [Figs. 6(a) and 6(b)]. The lowest two features are related to the decay of the $e_{z}^{1}$ and e, modes, respectively. The distinct second-layer vibra- tional modes are labeled in Fig. 9. Note the interaction of the $e_{z}^{2}$ with the $e_{y}^{2}$ mode at $0.6 k_{\Gamma M}$ ; these two modes will also interact and avoid the $e_{y}^{1}$ mode shown in Fig. 8. The solid line in Fig. 9 connects the $e_{y}^{1}$ and the $e_{z}^{2}$ modes. From our analysis of Cu, this mode should correspond to the second experimental mode. The agreement for Ag is not as good as Cu, although the experimental points show a large amount of scatter for a given wave vector(~0.3-0.5 THz). A better fit to the bulk modes and a lowering of the $e_{z}^{2}$ mode would bring the calculated sur

![](./images/812590022082428930_8.jpg)

FIG. 7. Schematic illustration of the avoided crossings of the sagittal plane modes along $\Gamma M$ direction for Cu(111). A similar picture can be applied to the sagittal-plane modes along $\Gamma M$ of Ag(111). The solid lines indicate first-layer modes and the dashed lines indicate second-layer modes. The avoided crossing of the modes at about $0.6 k_{\Gamma M}$ is clearly evident.

![](./images/812590022082428930_9.jpg)

FIG. 8. VLDOS of the first-layer sagittal-plane modes, $e_{z}^{1}+e_{y}^{1}$, for $\mathrm{Ag}$ along $\Gamma M$. The small circles represent the He-scattering results of Ref. 5. The two large features at point $M$ are the $S_{1}$ Rayleigh wave and the $S_{2}$ gap mode [see Fig. 4(b)]. Similar to the $\mathrm{Cu}$ case, the $S_{2}$ gap mode is almost entirely related to the first-layer longitudinal mode, $e_{y}^{1}$. A branching of the $e_{y}^{1}$ mode is also visible for $\mathrm{Ag}$ at about $0.6 k_{\Gamma M}$.

face modes into better agreement with experiment. The EAM functions we are using do not seem to be able to account for the position of the $e_{z}^{2}$ mode.

### E. Cu(111) along $\Gamma K$
The vibrational spectrum along $\Gamma K$ is more complicated than that along $\Gamma M$ due to a coupling of the sagittal-plane vibrational modes and the shear-horizontal modes. The lack of a mirror plane along $\Gamma K$ results in a mixing of these modes. A He-atom beam with wave vector along $\Gamma K$ should couple most strongly to modes with $e_{z}^{1}$ (transverse) and $e_{x}^{1}$ (longitudinal) amplitudes. The He-scattering experiments have observed two modes for both $\mathrm{Cu}$ and $\mathrm{Ag}$ along the $\Gamma K$ direction. One would expect

![](./images/812590022082428930_10.jpg)

FIG. 9. VLDOS of the second-layer sagittal plane modes, $e_{z}^{2}+e_{y}^{2}$, for $\mathrm{Ag}$ along $\Gamma M$. The small circles represent the He-scattering results of Ref. 5. The solid line is a guide to the eye to mark the position of the longitudinal-resonance mode made up of $e_{y}^{1}$ (wave vector less than $\sim 0.6 k_{\Gamma M}$ ) and $e_{z}^{2}$ (wave vector greater than $\sim 0.6 k_{\Gamma M}$ ) polarizations.

that these modes would correspond to $e_{z}^{1}$ and $e_{x}^{1}$ modes.
To see if this is indeed the case, we show the VLDOS of
the $e_{z}^{1}$ and $e_{x}^{1}$ polarizations in Figs. 10(a) and 10(b), re-
spectively. The dominant branch of the $e_{z}^{1}$ mode is in ex-
cellent agreement with the lowest experimental mode.
Near the $\Gamma$ point, the $e_{x}^{1}$ mode appears to follow the
second experimental mode, but deviates significantly after
about $0.1k_{\Gamma K}$. At the $K$ point the $e_{x}^{1}$ mode shows two
structures of approximately equal intensity; the lower
structure is due to coupling with the $e_{y}^{1}$ mode (a conse-
quence of the missing mirror plane). Near the $K$ point
the second experimental mode seems to correspond more
closely with the high-frequency branch of the $e_{z}^{1}$ mode,
which is a consequence of the mixing with the first-layer
sagittal-plane modes with the $e_{y}^{1}$, $e_{z}^{2}$, $e_{x}^{2}$, and $e_{y}^{2}$ modes.
All five of these modes have appreciable amplitude in this
region and can account for the second experimental
mode. The higher-frequency branch of the $e_{z}^{1}$ mode has

![](./images/812590022082428930_11.jpg)

FIG. 10. VLDOS of Cu along $\Gamma K$ for modes with (a) $z$ polarization and (b) $x$ polarization on the first-layer atom, $e_{z}^{1}$ and $e_{x}^{1}$, respec
tively. The small circles represent the He-scattering results of Ref. 5. In (a) two structures related to $e_{z}^{1}$ are clearly visible. The
lowest (highest) modes are the Rayleigh wave (pseudo-Rayleigh wave), respectively. Both modes in (a) are in good agreement with
the He-scattering experiments. In (b) the main disturbance is the sagittal-plane longitudinal mode, $e_{x}^{1}$. At point $K$, two features of
equal amplitude can been seen: (1) the lowest feature is a result of mixing with the first-layer shear mode $e_{y}^{1}$ [see Fig. 9(a)], and (2) the
higher-energy feature is the zone-edge amplitude of the $e_{x}^{1}$ mode.

been labeled by Bortolani et al. $^{7,8}$ as the "pseudo Rayleigh wave" (PRW); we shall adopt this labeling in the rest of the paper. In contrast to the suggestion of Bortolani et al., $^{7,8}$ we find that the PRW explains the second experimental mode, rather than the lowest experimental mode.

The VLDOS of the $e_{y}^{1}$, $e_{z}^{2}$, $e_{x}^{2}$, and $e_{y}^{2}$ modes are shown in Figs. 11(a)-11(d), respectively. Note the splitting of $e_{y}^{1}$ mode into two branches along $\Gamma K$ [Fig. 11(a)], as a result of an avoided crossing with the $e_{z}^{2}$ mode. The $e_{z}^{2}$ mode [Fig. 11(b)] exhibits a high-frequency disturbance, which interacts with and contributes to the lower branch of the $e_{y}^{1}$ mode. This is very similar to the avoided crossing of the $e_{y}^{1}$ and $e_{z}^{2}$ modes along $\Gamma M$. The two low-frequency disturbances in the $e_{z}^{2}$ VLDOS [Fig. 11(b)] are related to the decay of the $e_{z}^{1}$ branch into the bulk. Second-layer longitudinal $(e_{x}^{2})$ and horizontal $(e_{y}^{2})$ [Figs. 11(c) and 11(d)] vibrational modes exhibit similar features to the corresponding modes along $\Gamma M$. The main features of the first-layer modes, $e_{z}^{1}$, $e_{x}^{1}$, and $e_{y}^{1}$, are illustrated schematically in Fig. 11(e).

![](./images/812590022082428930_12.jpg)

FIG. 11. VLDOS's of $e_{y}^{1}$, $e_{z}^{2}$, $e_{x}^{2}$, and $e_{y}^{2}$ are given in (a)-(d), respectively. The small circles represent the He-scattering results of Ref. 5. All four of these modes have appreciable amplitude in the region of the second higher-frequency mode as a result of the mixing of the sagittal-plane and shear modes. The main features of the first-layer sagittal-plane modes are illustrated in (e).

![](./images/812590022082428930_13.jpg)

![](./images/812590022082428930_14.jpg)

![](./images/812590022082428930_15.jpg)

FIG. 11. (Continued).

### F. Ag(111) along $\Gamma K$

The VLDOS of first- and second-layer sagittal-plane vibrational modes $(e_z^1+e_x^1, e_z^2+e_x^2)$ are shown in Figs. 12(a) and 12(b). Similar to the Cu VLDOS along $\Gamma K$, we see that the second experimental mode follows the PRW (higher branch of the $e_z^1$ mode) rather than the longitudinally polarized mode $e_x^1$. Both the RW and the PRW are in good agreement with experiment. This also gives us confidence that the nature and position of the modes along $\Gamma M$ are well characterized. Note the coupling of the sagittal-plane longitudinal mode $e_x^1$ with the shear-horizontal mode at the $K$ point. In addition, the PRW exhibits predominantly $e_z^2$ character at point $K$. In Fig. 13 the combined VLDOS of the shear and vertically polarized modes $(e_y^1+e_z^1, e_y^2+e_z^2)$ is given. These modes, like those of Cu, show a variety of structures and avoided crossings. One interesting feature is the splitting of the $e_y^1$ mode: one branch follows the PRW, and the other exhibits a large feature at the $K$ point, which is related to the coupling of the shear and sagittal-plane modes.

Along $\Gamma K$ of Ag, Bortolani $et$ $al.^7$ calculated three modes which are split off from the lower transverse edge, while the calculations of Jayanthi $et$ $al.^{12}$ showed two

![](./images/812590022082428930_16.jpg)

FIG. 12. VLDOS's of the (a) first-layer, $e_z^1+e_x^1$, and (b) second-layer, $e_z^2+e_x^2$, sagittal-plane modes for Ag along $\Gamma K$. The small circles represent the He-scattering results of Ref. 5.

modes. Our vibrational spectrum for Ag is considerably different from these calculations, showing only one mode splitting off from the lower transverse edge. The large number of modes found by Bortolani et al. $^{7}$ is presum ably due to large changes in intralayer central and angu- lar interactions used in the calculation.

### G. Interlayer and intralayer force-constant tensor: comparison of EAM and NNCP

The modifications of the force constants at the surface can be viewed in a two-step process. First, the bulk is truncated to create the *ideal* surface; one would expect that the intralayer force constants would be most sensi- tive to this process. In the second step the *ideal* bulk ter- minated surface is allowed to relax; the dominant effect of this step is a stiffening of the interlayer force constants. From Eqs. (3a) and (3b) we can calculate these changes and relate them to the relative importance of the two- and three-body contributions to the force-constant ten- sor, $K_{ij}$.

In Fig. 2 the surface unit-cell geometry and positions of the atoms used to evaluate the relevant interatomic force-constant tensor are given. [111] is taken along the $z$ axis, $[\overline{1}10]$ is along the $x$ axis, and $[11\overline{2}]$ along the $y$ axis.

![](./images/812590022082428930_17.jpg)

FIG. 13. VLDOS's of the first- and second-layer shear modes, (a) $e_{z}^{1}+e_{y}^{1}$ and (b) $e_{z}^{2}+e_{y}^{2}$, for Ag along $\Gamma K$. The small circles represent the He-scattering results of Ref. 5.

**TABLE I.** Force-constant tensors for the nearest-neighbor intralayer and interlayer interactions and second-neighbor intralayer interactions. The labeling and positions of the atoms are given in Fig. 2. Values are given for both the bulk, ideal surface, and re- laxed (111) surfaces of Cu and Ag. Atom 1 is taken as a reference. Therefore $\mathbf{K}_{12}$ is the nearest-neighbor intralayer force-constant tensor, $\mathbf{K}_{13}$ is the nearest-neighbor interlayer force-constant tensor, and $\mathbf{K}_{14}$ is the second-neighbor intralayer force-constant tensor. $\phi_{\text{bulk}}$ (1.685 eV/Å) (Ref. 10), $\phi_{\text{is}}$ (1.432 eV/Å) (Ref. 10), and $\phi_{\text{rs}}$ are the nearest-neighbor NNCP force-constants in the bulk, the ideal surface, and the relaxed surface, respectively. Note also we have allowed the intralayer $\phi_{\text{rs}}$ and the interlayer $\phi_{\text{rs}}'$ to be different. The values of the force-constants are in (eV/Å $^{2}$). The first, second, and third columns of each $\text{K}_{ij}$ tensor corresponds to the $x$, $y$, and $z$ components.

### Bulk EAM (Cu)
$$
\mathrm{K}_{12}=\begin{array}{rrr}
-1.978 & 0.000 & 0.000 \\
0.000 & 0.090 & -0.008 \\
0.000 & -0.008 & 0.093
\end{array},
\quad
\mathrm{K}_{13}=\begin{array}{rrr}
0.088 & 0.000 & 0.000 \\
0.000 & -0.589 & -0.981 \\
0.000 & -0.981 & -1.284
\end{array},
\quad
\mathrm{K}_{14}=\begin{array}{rrr}
0.009 & 0.000 & 0.000 \\
0.000 & 0.002 & -0.001 \\
0.000 & -0.001 & -0.001
\end{array}
$$

### Bulk EAM (Ag)
$$
\mathrm{K}_{12}=\begin{array}{rrr}
-1.534 & 0.000 & 0.000 \\
0.000 & 0.059 & -0.010 \\
0.000 & -0.010 & 0.052
\end{array},
\quad
\mathrm{K}_{13}=\begin{array}{rrr}
0.045 & 0.000 & 0.000 \\
0.000 & -0.467 & -0.754 \\
0.000 & -0.754 & -1.000
\end{array},
\quad
\mathrm{K}_{14}=\begin{array}{rrr}
0.012 & 0.000 & 0.000 \\
0.000 & -0.027 & 0.000 \\
0.000 & 0.000 & 0.001
\end{array}
$$

### Bulk NNCP
$$
\mathrm{K}_{12}=\begin{array}{rrr}
-\phi_{\text{bulk}} & 0.000 & 0.000 \\
0.000 & 0.000 & 0.000 \\
0.000 & 0.000 & 0.000
\end{array},
\quad
\mathrm{K}_{13}=\begin{array}{rrr}
0.000 & 0.000 & 0.000 \\
0.000 & -\phi_{\text{bulk}} & -\phi_{\text{bulk}} \\
0.000 & -\phi_{\text{bulk}} & -\phi_{\text{bulk}}
\end{array},
\quad
\mathrm{K}_{14}=\begin{array}{rrr}
0.000 & 0.000 & 0.000 \\
0.000 & 0.000 & 0.000 \\
0.000 & 0.000 & 0.000
\end{array}
$$

### Ideal-surface EAM (Cu)
$$
\mathrm{K}_{12}=\begin{array}{rrr}
-1.767 & -0.003 & 0.141 \\
0.003 & 0.080 & -0.004 \\
-0.141 & -0.004 & 0.025
\end{array},
\quad
\mathrm{K}_{13}=\begin{array}{rrr}
0.078 & 0.000 & 0.000 \\
0.000 & -0.558 & -0.948 \\
0.000 & -0.994 & -1.324
\end{array},
\quad
\mathrm{K}_{14}=\begin{array}{rrr}
0.019 & 0.000 & 0.000 \\
0.000 & -0.002 & -0.005 \\
0.000 & 0.004 & -0.003
\end{array}
$$

### Ideal-surface EAM (Ag)
$$
\mathrm{K}_{12}=\begin{array}{rrr}
-1.336 & -0.003 & 0.131 \\
0.003 & 0.058 & -0.005 \\
-0.141 & -0.005 & 0.002
\end{array},
\quad
\mathrm{K}_{13}=\begin{array}{rrr}
0.042 & 0.000 & 0.000 \\
0.000 & -0.433 & -0.729 \\
0.000 & -0.768 & -1.036
\end{array},
\quad
\mathrm{K}_{14}=\begin{array}{rrr}
0.023 & 0.000 & 0.000 \\
0.000 & -0.058 & -0.002 \\
0.000 & 0.001 & 0.000
\end{array}
$$

### Ideal-surface NNCP
$$
\mathrm{K}_{12}=\begin{array}{rrr}
-\phi_{\text{is}} & 0.000 & 0.000 \\
0.000 & 0.000 & 0.000 \\
0.000 & 0.000 & 0.000
\end{array},
\quad
\mathrm{K}_{13}=\begin{array}{rrr}
0.000 & 0.000 & 0.000 \\
0.000 & -\phi_{\text{is}} & -\phi_{\text{is}} \\
0.000 & -\phi_{\text{is}} & -\phi_{\text{is}}
\end{array},
\quad
\mathrm{K}_{14}=\begin{array}{rrr}
0.000 & 0.000 & 0.000 \\
0.000 & 0.000 & 0.000 \\
0.000 & 0.000 & 0.000
\end{array}
$$

### Relaxed-surface EAM (Cu)
$$
\mathrm{K}_{12}=\begin{array}{rrr}
0.029 & -0.143 & -0.004 \\
0.003 & 0.081 & -0.004 \\
-0.143 & -0.004 & 0.029
\end{array},
\quad
\mathrm{K}_{13}=\begin{array}{rrr}
0.095 & 0.000 & 0.000 \\
0.000 & -0.619 & -1.048 \\
0.000 & -1.096 & -1.437
\end{array},
\quad
\mathrm{K}_{14}=\begin{array}{rrr}
0.018 & 0.000 & 0.000 \\
0.000 & -0.022 & -0.005 \\
0.000 & 0.004 & -0.003
\end{array}
$$

### Relaxed-surface EAM (Ag)
$$
\mathrm{K}_{12}=\begin{array}{rrr}
-1.352 & -0.003 & 0.133 \\
0.003 & 0.058 & -0.005 \\
-0.133 & -0.005 & 0.006
\end{array},
\quad
\mathrm{K}_{13}=\begin{array}{rrr}
0.058 & 0.000 & 0.000 \\
0.000 & -0.503 & -0.844 \\
0.000 & -0.886 & -1.173
\end{array},
\quad
\mathrm{K}_{14}=\begin{array}{rrr}
0.022 & 0.000 & 0.000 \\
0.000 & -0.055 & -0.001 \\
0.000 & -0.001 & 0.000
\end{array}
$$

### Relaxed-surface NNCP
$$
\mathrm{K}_{12}=\begin{array}{rrr}
-\phi_{\mathrm{rs}} & 0.000 & 0.000 \\
0.000 & 0.000 & 0.000 \\
0.000 & 0.000 & 0.000
\end{array},
\quad
\mathrm{K}_{13}=\begin{array}{rrr}
0.000 & 0.000 & 0.000 \\
0.000 & -\phi_{\mathrm{rs}}^{\prime} & -\phi_{\mathrm{rs}}^{\prime} \\
0.000 & -\phi_{\mathrm{rs}}^{\prime} & -\phi_{\mathrm{rs}}^{\prime}
\end{array},
\quad
\mathrm{K}_{14}=\begin{array}{rrr}
0.000 & 0.000 & 0.000 \\
0.000 & 0.000 & 0.000 \\
0.000 & 0.000 & 0.000
\end{array}
$$


Therefore, according to our notation, $K_{12}(x,x)$ would be equivalent to the nearest-neighbor intralayer force constant within the NNCP model. Table I compares the nearest-neighbor intralayer and interlayer and second- neighbor intralayer force-constant tensors, $K_{ij}$'s, calculated with the EAM and the NNCP model for Cu and Ag. For the bulk crystals, the EAM and NNCP $K_{ij}$ are very similar. The EAM $K_{ij}$ have small contributions not contained in the NNCP model which are related to three- body interactions and first derivatives of the effective pair potential $\psi_{ij}$. Note that the second-nearest-neighbor intralayer force-constant tensor, $K_{14}$, is more than 2 orders of magnitude smaller than the nearest-neighbor intralayer force-constant tensor, $K_{12}$. This gives a justification for the use of the NNCP for Cu by Hall et al. $^{10}$ Our calculated value for the nearest-neighbor bulk force constant, $1.978\ \text{eV}/\mathring{\text{A}}^2$, compares favorably with the value of $1.685\ \text{eV}/\mathring{\text{A}}$ used by Hall et al. $^{10}$

The dominant changes in the $K_{ij}$'s from their bulk values for both the Cu and Ag *ideal* surfaces are

$$[\mathsf{K}_{12}(x,x)]_{\text{surf}}=0.89[\mathsf{K}_{12}(x,x)]_{\text{bulk}} \text{ for Cu},$$

$$[\mathsf{K}_{12}(x,x)]_{\text{surf}}=0.87[\mathsf{K}_{12}(x,x)]_{\text{bulk}} \text{ for Ag},$$

$$[\mathsf{K}_{12}(x,z)]_{\text{surf}}=-[\mathsf{K}_{12}(z,x)]_{\text{surf}}=0.141$$
$$\text{where } [\mathsf{K}_{12}(x,z)]_{\text{bulk}}=0.000 \text{ for Cu},$$

$$[\mathsf{K}_{12}(x,z)]_{\text{surf}}=-[\mathsf{K}_{12}(z,x)]_{\text{surf}}=0.131$$
$$\text{where } [\mathsf{K}_{12}(x,z)]_{\text{bulk}}=0.000 \text{ for Ag},$$

$$[\mathsf{K}_{13}(i,j)]_{\text{surf}}=(1\pm 0.02)[\mathsf{K}_{13}(i,j)]_{\text{bulk}} \text{ for Cu and Ag}.$$

Some of these changes can be related to changes in both the effective pair potential shown in Fig. 1 and the three- body contributions given by the fourth term in Eq. (3a). Other modifications $([K_{12}(x,z)]_{\text{surf}})$ can be directly related to three-body contributions at the surface due to the charge-density-gradient terms $\mathbf{g}_{i}$ appearing in Eqs. (3a) and (3b). Although the EAM does not contain explicit angular interactions, the nonzero values of $[K_{12}(x,z)]_{\text{surf}}$ would occur for angle-dependent terms. In the NNCP model the ideal surface force constant $\phi_{\text{is}}$ is changed from $\phi_{\text{bulk}}$ to fit the measured surface modes. Using this procedure, Hall et al. $^{10}$ found a value of $\phi_{\text{is}}$ equal to 0.85 $\phi_{\text{bulk}}$ for Cu, in good agreement with our value of $11\%$ softening of the intralayer nearest-neighbor force constant. Since the EAM does not allow for explicit charge relaxation at the surface, these values may be slightly different from the real force-constant modifications. Nevertheless, we feel that our values are very reasonable given the good agreement we have found with most of the experimental surface modes.

Relaxation of the ideal surfaces leaves the intralayer force-constant tensors, $K_{12}$ and $K_{14}$, essentially unchanged, and increases the interlayer force-constant tensor, $K_{13}$, by about $10-15\%$ for Cu and Ag. Within the NNCP, interlayer relaxation can be taken into account by allowing the intralayer and interlayer nearest-neighbor force constants to be different.

### IV. CONCLUSIONS

We have shown that the EAM is able to provide an accurate and detailed description of the lattice dynamics of the Cu(111) and Ag(111) surfaces. Our calculations suggest that the modifications of the surface interatomic force constants from their bulk values are not that large for these surfaces; similar results have been found for other surfaces of Cu and Ag, and also with other $3d$ transition metals. The avoided crossings of surface modes are an integral part of the surface-phonon spectrum, and may lead to confusion when the experimental results are analyzed within a particular model.

### ACKNOWLEDGMENTS

We would like to thank Professor D. L. Mills, Professor J. P. Toennies, Professor H. Ibach, and Professor F. Wuttig for useful discussions. This work was support by the U.S. Department of Energy (Division of Materials Sciences of the Office of Basic Energy Sciences).

---

*Present address: Lawrence Livermore National Laboratory,(L-356), Livermore, CA 94550.
$^{1}$J. P. Toennies, J. Vac. Sci. Technol. **A** 2, 1055 (1984).
$^{2}$H. Ibach and D. L. Mills, *Electron Energy Loss Spectroscopy and Surface Vibrations* (Academic, New York, 1982).
$^{3}$M. Cates and D. R. Miller, Phys. Rev. **B** 28, 3615 (1983).
$^{4}$R. B. Doak, U. Harten, and J. P. Toennies, Phys. Rev. Lett. **51**,578 (1983).
$^{5}$U. Harten, J. P. Toennies, and Ch. Woll, Faraday Discuss.Chem. Soc. **80**, 137 (1985).
$^{6}$M. H. Mohamed, L. L. Kesmodel, B. M. Hall, and D. L. Mills,Phys. Rev. **B** 37, 2763 (1988).
$^{7}$V. Bortolani, A. Franchini, F. Nizzoli, and G. Santoro, Phys.Rev. Lett. **52**, 429 (1984).
$^{8}$V. Bortolani, G. Santoro, U. Harten, and J. P. Toennies, Surf.Sci. **148**, 82 (1984); see also V. Bortolani, A. Franchini, F.Nizzoli, and G. Santoro, *ibid*. **152**, 811 (1985).
$^{9}$G. Santoro, A. Franchini, V. Bortolani, U. Harten, J. P. Toennies, and Ch. Woll, Surf. Sci. **183**, 180 (1987).
$^{10}$B. M. Hall, D. L. Mills, M. H. Mohamed, and L. L. Kesmodel, Phys. Rev. **B** 39, 1988).
$^{11}$J. S. Nelson, E. C. Sowa, and M. S. Daw, Phys. Rev. Lett. **61**,1977 (1988); see also L. Ningsheng, X. Wenlan, and S. C.Shen, Solid State Commun. **67**, 837 (1988).
$^{12}$C. S. Jayanthi, H. Bilz, W. Kress, and G. Benedek, Phys. Rev.Lett. **59**, 795 (1987).
$^{13}$G. Bracco, R. Tatarek, R. Tommasini, U. Linke, and M.Persson, Phys. Rev. **B** 36, 2928 (1987); see also P. Zeppenfeld,K. Kern, R. David, K. Kuhnke, G. Comsa, *ibid*. **38**, 12 329(1988).

$^{14}$M. S. Daw and M. I. Baskes, Phys. Rev. B 29, 6443 (1984).

$^{15}$M. S. Daw and R. D. Hatcher, Solid State Commun. 56, 697 (1985).

$^{16}$S. M. Foiles, Surf. Sci. 191, L779 (1987).

$^{17}$S. M. Foiles, M. I. Baskes, and M. S. Daw, Phys. Rev. B 33, 7983 (1986).

$^{18}$S. M. Foiles, Phys. Rev. B 32, 3409 (1985).

$^{19}$A. A. Maradudin, E. W. Montroll, and G. H. Weiss, *Theory of Lattice Dynamics in the Harmonic Approximation* (Academic, New York, 1963).

$^{20}$E. C. Sowa, M. S. Daw, and J. S. Nelson (unpublished).

$^{21}$E. C. Svensson, B. N. Brockhouse, and J. M. Rowe, Phys. Rev. 155, 619 (1967).

$^{22}$W. A. Kamitakahara and B. N. Brockhouse, Phys. Lett. 29A, 639 (1969).

$^{23}$R. E. Allen, G. P. Alldredge, and F. W. de Wette, Phys. Rev. B 4, 1661 (1987).