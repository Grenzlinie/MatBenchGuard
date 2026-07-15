# Quantum Mode Phonon Forces between Chainmolecules

JAKOB BOHR
Department of Physics, The Technical University of Denmark, DK-2800 Lyngby, Denmark

Received 4 September 2000; revised 24 January 2001; accepted 20 February 2001

**ABSTRACT:** A phenomenological description of the contributions of phonons to molecular force is developed. It uses an approximation to consider macromolecules as solid continua. The molecular modes of a molecule can then be characterized by a Debye-like description of the partition function. The resulting bimolecular interaction is a truly many-body force that is temperature dependent and can be of the order of 1 eV. These phonon forces depend on molecular shape, composition, and density. They may therefore also be important for large molecular conformational changes, including the unfolding of chain molecules. For the later case, a significant change in zero-point energy is found. This may be the underlying cause for cold denaturation of proteins. © 2001 John Wiley & Sons, Inc. Int J Quantum Chem 84: 249–252, 2001

**Key words:** cold denaturation; forces; modes; zero-point energy; phonons

---

## Introduction

The most significant molecular forces originate from interactions involving charges, the motion of charges, spins, and entropy. The result is a large variety of phenomena, and chemical binding is often classified accordingly, e.g., van der Waals forces, London forces, covalent bonds, hydrogen bonds, electrostatic forces, entropic forces, hydrophobic forces, zero-point forces, etc. [1, 2]. In many cases it is sufficient to describe the interactions classically, e.g., van der Waals interactions. In other cases quantum mechanical considerations are necessary, e.g., covalent bonds [3]. Different approximations and methods such as Hartree–Fock methods, density functional theory [4], etc., are used for computational work involving larger molecules. In computational biochemistry molecular recognition is frequently modeled by the use of an approximate force field [5], e.g., AMBER [6] and CHARMM [7]. For unimolecular reactions ($A \rightarrow B$, e.g., $\text{CH}_3\text{NC} \rightarrow \text{CH}_3\text{CN}$) of relatively small molecules the quantization of modes is important [8, 9] as was early recognized by Slater, Rice, Ramsperger, Kassel, and Marcus [10–13].

The difference in zero-point energy between two molecules $A$ and $B$, and their molecular assembly $AB$ can be found by subtraction. Let the frequencies of their modes be $\omega_i^A$ and $\omega_j^B$, and $\omega_k^{AB}$, respectively, then

$$
\Delta U_{\text{Zero}} = \frac{1}{2}\left(\sum_{k} \omega_k^{AB}\hbar - \sum_{i} \omega_i^A\hbar - \sum_{j} \omega_j^B\hbar\right),
$$

Correspondence to: J. Bohr; e-mail: jakob.bohr@fysik.dtu.dk

International Journal of Quantum Chemistry, Vol. 84, 249–252 (2001)
© 2001 John Wiley & Sons, Inc.

BOHR

where the sums over $k$, $i$, and $j$ are over all modes. The number of modes is equal to $3N - 6$ as six degrees of freedom are translational and rotational. Therefore, the bonded molecule $AB$ has six intrinsic modes more than $A$ and $B$ together.

At $T$=0 K the contribution to the binding between two molecules $A$ and $B$ from zero-point motion is calculated as above. The force can be attractive, or repulsive, depending in details on how the mode spectra change when $A + B \to AB$. If the $AB$ is "more stiff" than $A$ and $B$, then $\Delta U_{\text{Zero}}$ is positive, and there will be a net repulsion between $A$ and $B$. This is a realistic conjecture for some flexible chain molecules. However, $\Delta U_{\text{Zero}}$ can be both positive and negative depending on geometry, atomic composition and density.

For small molecules the frequencies of bond vibration modes are typically $7 \times 10^{13}$ Hz giving a $\hbar\omega$ of about 0.3 eV. Therefore, at room temperature ($k_BT = 0.025$ eV) excited quantum states are hardly present. However, for larger molecules some of the modes will be sufficiently soft to have contributions from excited quantum states. For very large molecules, such as long one-dimensional chains, or large three-dimensional structures, modes that contribute with higher quantum states will be more densely distributed, thereby allowing their contribution to the binding energy to depend more strongly on temperature. An estimate of the quantum mode contribution to the binding energy of two large molecules will be obtained by considering a phenomenological Debye-like description that integrates over the participation of the modes. The fundamental approximation done is to describe a molecule as an isotropic solid continum. At a given temperature the Debye contribution to the intrinsic energy in a molecule can be estimated as:

$$
U_{\text{Debye}} = 3 \int_{\omega_L}^{\omega_U} \frac{V\omega^2}{2\pi^2 v^3} \frac{\hbar\omega}{e^{\hbar\omega/k_B T} - 1} d\omega,
$$

where $\omega_L = (\pi/2)v(4\pi/3V)^{1/3}$ is a lower cutoff frequency that is introduced to describe the finite size of the system. The molecule is taken to be spherical and the longest half wavelength to be equal to the diameter of the molecule. The upper frequency, $\omega_U = v[2\pi^2(3N - 6 + \pi^2/12)/V]^{1/3}$, is estimated by requiring the total number of modes to be equal to $3N - 6$. The material properties are assumed to be isotropic, and no distinction is made between longitudinal and transverse modes, $v$ is the velocity of sound. $N$ is the number of atoms and $V = (4/3)\pi[(3N/4\pi)^{1/3} - 1/2]^3a$ is the volume spanned by the atomic coordinates; $a$ is a typical atomic distance.

For infinite, or very large systems, $\omega_L$ becomes zero and $\omega_U$ the usual Debye frequency [14]. Similar to the estimate of the Debye energy, we can estimate the zero-point energy of a large molecule by

$$
U_{\text{Zero}} = 3 \int_{\omega_L}^{\omega_U} \frac{V\omega^2}{2\pi^2 v^3} \frac{\hbar\omega}{2} d\omega = \frac{3}{16} \frac{Vh}{\pi^2 v^3}(\omega_U^4 - \omega_L^4).
$$

Likewise, the difference in zero-point energy between two identical molecules and their fused molecule, *the dimer*, can be estimated to:

$$
\Delta U_{\text{Zero}} = \frac{3}{8} \frac{Vh}{\pi^2 v^3}[\omega_{U,d}^4 + \omega_{L,m}^4 - \omega_{U,m}^4 - \omega_{L,d}^4],
$$

where the indexes $m$ and $d$ are for monomer and dimer, respectively.

Consider approximate numerical values that are typical for some biomolecules. For example, consider molecules with about 500 atoms, with a typical interatomic distance of $a = 1.5 \times 10^{-10}$ m. The velocity of sound, $v$, is set to 2500 m/s, a value typical for polymers. Then one gets $\omega_U = 7.22 \times 10^{13}$ s$^{-1}$ and $\omega_L = 5.92 \times 10^{12}$ s$^{-1}$. The zero-point energy and the difference in zero-point energies become $U_{\text{Zero}} = 26.6$ eV and $\Delta U_{\text{Zero}} = -1.1$ eV, respectively. It is necessary to include the temperature contribution, i.e., the Debye energy $U_{\text{Debye}}$:

$$
\Delta U = U_{\text{Debye},d} - 2U_{\text{Debye},m} + \Delta U_{\text{Zero}}
$$

or

$$
\begin{aligned}
\Delta U &= \frac{3V_d(k_b T)^4}{2\pi^2 v^3 \hbar^3} \int_{\hbar\omega_{L,d}/k_B T}^{\hbar\omega_{U,d}/k_B T} \frac{x^3}{e^x - 1} dx \\
&\quad - 2\frac{3V_m(k_b T)^4}{2\pi^2 v^3 \hbar^3} \int_{\hbar\omega_{L,m}/k_B T}^{\hbar\omega_{U,m}/k_B T} \frac{x^3}{e^x - 1} dx + \Delta U_{\text{Zero}}.
\end{aligned}
$$

Figure 1 shows the internal energy constituting the zero-point energy and the Debye energy as a function of temperature. The molecule is spherical and contain 500 atoms. The straight line is the classical energy $(3N - 6)k_BT$. As a curiosity, it is worthwhile to notice that if the exponential function in the Debye model is series expanded to second order, then the asymptotical result becomes $(3N - 6)k_BT - U_{\text{Zero}}$. Historically, the existence of zero-point energy was suggested in 1911 at the first Solvay Conference by Max Plank, using an argument that built on obtaining classical equipatition in the high-temperature limit [15].

Figure 2 shows the change in the internal energy, $\Delta U$, obtained by dimerization, as a function of temperature. At constant pressure the change in

QUANTUM MODE PHONON FORCES

![](./images/812463840187908097_1.jpg)

FIGURE 1. Internal energy, $U$, constituting the zero-point energy and the Debye energy as a function of temperature for a molecule with 500 atoms. The straight line is the classical result $(3N-6)k_BT$.

enthalpy (heat of reaction) is determined as $\Delta H = \Delta U + P\Delta V$. In the simplified continuum model described, no volume change shall be assumed to be associated with dimerization. As can be seen, the dimerization energies are not insignificant at temperatures typical for biological activities. The change in the Helmholtz free energy $\Delta F$ is shown in Figure 3. The Helmholtz free energy, $H=-k_BT\ln Z$, is calculated from the partition function, $Z$,

$$
\ln Z=-\int_{\omega_L}^{\omega_U} g(\omega)\left\{\frac{\hbar\omega}{2k_BT}+\ln\left[1-\exp\left(-\frac{\hbar\omega}{k_BT}\right)\right]\right\}d\omega,
$$

where $g(\omega)$ is the density of states

$$
g(\omega)=\frac{3V\omega^2}{2\pi^2v^3}.
$$

![](./images/812463840187908097_2.jpg)

FIGURE 2. Change in internal energy upon dimerization, $\Delta U$, as a function of temperature, for two identical monomers with 500 atoms each. The straight line is the classical result $6k_BT$. Depending on the dispersion of these six modes, they may still take part, in which case the dimerization energy becomes the difference between the two curves.

![](./images/812463840187908097_3.jpg)

FIGURE 3. Change in the Helmholtz free energy, $\Delta F$, upon dimerization. For the change in internal energy see Figure 2.

At constant pressure the change in the Gibbs free energy is $\Delta G=\Delta F+P\Delta V$. It is important to take notice that the above estimates depend strongly on the material parameters, such as the speed of sound, density, and volume for the molecules and the dimer. For example, if the effective speed of sound in the dimer is 5% higher than in the monomers, then the interaction between the monomers be- comes repulsive, see Figures 4 and 5. Such molecu- lar dependent factors will be more significant when binding is considered between two molecules that are not identical to each other. A phenomenologi- cal Debye description cannot be expected to provide accurate numerical estimates. More realistic calcula- tions could be based on an enumeration of the many individual modes.

Above it was found that the effect of the inter- nal mode spectrum in large molecules contribute to binding between two molecules, and that the strength of such forces can be comparable with

![](./images/812463840187908097_4.jpg)

FIGURE 4. Gain in internal energy, $\Delta U$, upon dimerization for the case where the speed of sound is 5% higher in the dimer than in the monomer. The straight line is the classical result $6k_BT$.

---
INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY

BOHR

![](./images/812463840187908097_5.jpg)

FIGURE 5. Change in the Helmholtz free energy, $\Delta F$, upon dimerization for the case where the speed of sound is 5% higher in the dimer than in the monomer. For the change in internal energy see Figure 4.

numbers typically given for van der Waals forces, hydrophobic forces, and hydrogen bonds. Such quantum mode (or phonon) forces are truly many-body forces that depend in details on geometry and atomic composition. The spherical geometry considered above corresponds to a "fusion model," which is not realistic for real systems that can devi- ate significantly from spherical symmetry. A small change in the velocity of sound between the com- pound molecule and its components can change the quantum mode energy by plus or minus sev- eral electron volts. The atomic composition and the chemical bonding pattern therefore plays a signif- icant role in determining whether quantum mode forces are attractive or repulsive.

The density of states, $g(\omega)$, is dependent on the molecular shape. The unfolding of a protein is an extreme case of shape change, and the density of states changes from being three dimensional in character to one dimensional in character. For a one- dimensional system the density of states becomes independent of $\omega$:
$$
g=\frac{3 V}{\pi a^{2} v},
$$
and hence the zero-point energy
$$
U_{\text {Zero }}=\int_{\omega_{L}}^{\omega_{U}} \frac{3 V}{\pi a^{2} v} \frac{\hbar \omega}{2} d \omega=\frac{3 V \hbar}{4 \pi v a^{2}}\left[\omega_{U}^{2}-\omega_{L}^{2}\right].
$$

For 500 atoms arranged as a long string the the lower cutoff frequency becomes $\omega_{L}=\pi v / N a$ and the upper cutoff frequency $\omega_{U}=\pi(3 N-$ 6)v/3Na. The result is a zero-point energy af 12.9 eV, which is only about half the number for the three- dimensional spherical arrangement of the atoms. Phonon forces will therefore favor the unfolded phase at low temperature. A proposition that is con- sistent with cold denaturation of proteins becomes exothermic.

## References

1. Schulz, G. E.; Schirmer, R. H. Principle of Protein Structure; Springer: New York, 1979.
2. Buckingham, A. D. In Buckingham, A. D.; Legon, A. C.; Roberts, S. M., Eds. Intermolecular Forces in Principles of Molecular Recognition; Blackie Academic & Professional: London, 1993.
3. Pauling, L. The Nature of the Chemical Bond, 3rd ed.; Cor- nell University Press: Ithaca, NY, 1960.
4. Kohn, W.; Sham, L. J. Phys Rev 1965, 140, A1133.
5. Keserü, G.; Kolossváry, I. Molecular Mechanics and Con-formational Analysis in Drug Design; Blackwell Science: Oxford, 1999.
6. Cornell, W. D.; Cieplak, P.; Bayly, C. I.; Gould, I. R.; Merz, K. M.; Fergusin, D. M.; Spellmeyer, D. C.; Fox, T.; Cald- well, J. W.; Kollman, P. A. J Am Chem Soc 1995, 117,5179.
7. Brooks, B. R.; Bruccoleri, R. E.; Olafson, B. D.; States, D. J.; Swaminathan, S.; Karplus, M. J Comput Chem 1983, 4,187.
8. Robinson, P. J.; Holbrook, K. A. Unimolecular Reactions; Wiley-Interscience: London, 1972.
9. Forst, W. Theroy of Unimolecular Reactions; Academic: New York, 1973.
10. Slater, N. B. Theory of Unimolecular Reaction; Cornell Uni- versity Press: Ithaca, NY, 1959.
11. Rice, O. K.; Ramsperger, H. C. J Am Chem Soc 1927, 49,1617.
12. Kassel, L. S. J Phys Chem 1928, 32, 225, 1065.
13. Marcus, R. A.; Rice, O. K. J Phys Coll Chem 1951, 55, 894.
14. Kittel, C. Introduction to Solid State Physics, 7th ed.; Wiley: New York, 1996.
15. Mehra, J.; Rechenberg, H. Foundations of Physics 1999, 29,91-132.
