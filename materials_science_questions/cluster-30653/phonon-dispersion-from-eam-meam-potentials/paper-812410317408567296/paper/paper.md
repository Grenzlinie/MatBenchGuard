![](./images/812410317408567296_1.jpg)
Solid State Communications, Vol. 75, No. 11, pp. 877-880, 1990.
Printed in Great Britain.
0038-1098/90$3.00+.00
Pergamon Press plc

# EMBEDDED ATOM METHOD FOR PHONON FREQUENCIES IN TRANSITION METALS

Luo Ningsheng, Xu Wenlan and S.C.Shen

Laboratory for Infrared Physics, Shanghai Institute of Technical Physics,
Academia Sinica; 420 Zhong Shan Bei Yi Road, Shanghai, P.R.China.

(Received 28 February 1990 by A.A.Maradudin)

The Embedded Atom Method (EAM) has been applied to calculate the phonon frequencies of transition metals Ni, Pd, and Cu. It is found that the EAM with the first neighbor potential can not assure to reproduce the phonon frequencies at zone boundary. To reproduce the measured phonon frequencies accurately, we provide a modification with the force field of the third neighbor potential interactions in the EAM by considering somewhat non-uniform distribution of electron densities in real transition metals, except for Cu in which the non-nearest potential interactions can be neglected.

The Daw and Baskes [1] developed a new technique, called the Embedded Atom Method (EAM), for the approximate description of the interatomic interactions in a metallic system, based on the results from the density functional theory. The method can quickly give the total energy of an arbitrary arrangement of atoms in a metallic system through a semiempirical procedure which obtains the empirical functions by fitting the fundamental properties of the system, for example, lattice constants, elastic constants, cohesive energy, vacancy-formation energy, the state equation of metal, and so on. Luo Ningsheng, Xu Wenlan and S.C.Shen [2,3] have applied the EAM to the calculations of Cu bulk phonon frequencies in the symmetry and off-symmetry directions without any adjustable parameter, the calculated result is in excellent agreement with experimental data, the maximum deviation is 5.6%. For Ni and Pd, Daw and Hatcher [4] have calculated their bulk phonon frequencies, but the calculated results are only in good agreement with experimental data in the low frequency zone, the deviations of phonon frequencies at the zone boundaries are about 15.2% for Ni and 12.3% for Pd. In this work we apply the embedded atom method to the phonon frequencies in Ni and Pd, with a modi- fication of the third neighbor poten- tial interactions, we can reproduce the experimental phonon dispersion data with very small deviations. We find that the low frequency phonons are more correlated with the distant neighbor interatomic interactions than the high frequency phonons. We show that the EAM can give better agreements of phonon frequencies with experimental data in the whole phonon frequency zone while the distant neighbor potential interactions are included.

Within the framework of density functional theory, the total electronic energy for an arbitrary arrangement of nuclei can be written as a unique functional of the total electron density. From this point of view, Daw and Baskes[1] have introduced the embedded atom method where the total electron density of a metal is reasonable approximated by the linear superposition of contributions from the individual atoms. In addition, there is an electrostatic energy contribution due to core-core overlap. Thus the EAM is uniquely capable of quick calculations of the total energy. The total energy of a homonuclear solid in an arbitrary arrangement is given as a simple function of the positions of the atoms:

$$
E_{\text {tot }}=\sum_{i} F\left(\rho_{h, i}\right)+(1 / 2) \sum_{\substack{i, j \\(i \neq j)}} \phi\left(R_{i j}\right) \quad(1)
$$

where $F(\rho_{h, i})$ is the energy to embed atom i into the background host electron density $\rho_{h, i}$ due to the remaining atoms of the system. $\phi(R_{i j})$ is a short-range core-core repulsion

between atoms i and j, and the sums are over lattice atoms. The host electron density $\rho_{h,i}$ at atom i is:

$$
\rho_{h,i} = \sum_{j(\neq i)} \rho^a(R_{ij}) \tag{2}
$$

where $\rho^a(R_{ij})$ is the atomic electron density. The pairwise term takes the form:

$$
\phi(R_{ij}) = z^2(R_{ij})/R_{ij} \tag{3}
$$

where the effective charge $Z(R_{ij})$ is the function of the atomic species and interatomic distance $R_{ij}$.

In the low frequency vibrational zone, the crystal can be approximated as an elastic medium. For a fcc structural crystal, the frequencies of three elastic waves can be obtained from its elastic constants[5]:
K-[100]
$$
w_1=q(C_{11}/D)^{1/2} \quad V-[100] \tag{4a}
$$
$$
w_2=q(C_{44}/D)^{1/2} \quad V-[010] \tag{4b}
$$
$$
w_3=q(C_{44}/D)^{1/2} \quad V-[001] \tag{4c}
$$
K-[110]
$$
w_1=q[(C_{11}+C_{12}+2C_{44})/(2D)]^{1/2} \quad V-[110] \tag{5a}
$$
$$
w_2=q(C_{44}/D)^{1/2} \quad V-[001] \tag{5b}
$$
$$
w_3=q[(C_{11}+C_{12})/(2D)]^{1/2} \quad V-[1\overline{1}0] \tag{5c}
$$
K-[111]
$$
w_1=q[(C_{11}+2C_{12}+4C_{44})/(3D)]^{1/2} \quad V-[111] \tag{6a}
$$
$$
w_2=w_3=q[(C_{11}-C_{12}+C_{44})/(3D)]^{1/2} \quad V\text{-normal to [111]} \tag{6b}
$$

where $w_1$, $w_2$ and $w_3$ are the frequencies of vibrations, K is the direction of wave vector, V is the direction of vibration, q is the value of wave vector, $C_{11}$, $C_{12}$ and $C_{44}$ are the elastic constants, D is the mass density of crystal. Thus it is known obviously without any calculation done by Daw and Hatcher [4] that the embedded atom method can reproduce measured phonon frequencies in the low frequency zone, because it gives good fitting to the elastic constants. we now discuss why the EAM can not assure to reproduce measured phonon frequencies near the zone boundaries.

In a crystal, the dispersions of the vibrations along the high symmetrical directions, for example, [100], [110], and [111], are similar to a one-dimensional infinitive atomic chain whose force constants are taken as the interplanar force constants [6]. The dispersion relation can be written as

$$
w^2=(2/M) \sum_{n>0} C_n(1-\cos(nqa)) \tag{7}
$$

where w is the phonon frequency, $C_n$, the nth neighbor force constant, q, the value of wave vector, a, the distance between the nearest neighbor atoms, M, the mass of an atom, and in the summation n runs over positive integers. But in the real theoretical calculation, one always takes finite neighbor interactions. For example, here we take only the nearest neighbor interaction force constants. In the low frequency zone, the nearest neighbor force constant is $C_1$, at the zone boundary, is $C_b$. From Eq.(7), nearby q=0, there is the low frequency zone, and $q=\pi/a$ is the point of zone boundary. To reproduce the phonon frequencies of a infinitive force constant model by the use of a nearest neighbor force constant model, we derive different relations of force constants in different zones. Thus we have approximately

$$
C_1=C_1+4C_2+9C_3+16C_4+............ \tag{8}
$$

$$
C_b=C_1+C_3+C_5+C_7+............ \tag{9}
$$

Therefore, it is impossible to reproduce the whole phonon frequencies of a infinitive force constant model by the use of the same nearest force constant model unless the non-nearest interaction force constants can be neglected. In the EAM [1], the cutoff distance of potential was the shortest possible, between first and second neighbors, thus the potential interactions beyond the first neighbor were neglected, this is the reason why the EAM with good fitting to elastic constants or low frequencies of vibrations can not assure to reproduce the frequencies of vibrations near zone boundary, it was shown in the calculations for the bulk phonon dispersions in Ni and Pd by Daw and Hatcher[4] where the neglecting of non-nearest neighbor potential resulted in the larger derivations of phonon frequencies near the zone boundaries, except for Cu by Luo Ningsheng, Xu Wenlan and S.C.Shen [2,3] where the non-nearest neighbor potential can be neglected.

To reproduce the measured phonon frequencies accurately, we consider more neighbors for the potential

interactions in the EAM. It is known from above calculations that the contribution of the potential interaction to total energy is only about 10%, and we expect that in the energy contributed from the potentials, the nearest neighbor is dominant by comparing with that from the non-nearest neighbors. Thus to permit a reasonable fit, we assume that the contribution of energy from the non-nearest potential interactions can be neglected. In addition, due to the symmetry of atoms in fcc crystal, the potentials of the second neighbors give no contributions to elastic constants $C_{12}$ and $C_{44}$, and to the phonon frequencies at zone boundaries. The atoms of the second neighbors are at the high symmetry points in fcc crystal, they have more screen effect for their potential interactions than the atoms at the low symmetry points by considering somewhat non-uniform distribution of electron densities in real transition metal. Thus we can also neglect the force field of the second neighbors, and expect that the third neighbors give the contributions to force field of crystal to modify the deviation of phonon frequencies at zone boundary by a permitted fitting procedure. In this way we introduce two parameters $\phi_{3}'$ and $\phi_{3}''$ in fitting, $\phi_{3}'$ and $\phi_{3}''$ are the first derivation and the second derivation of the third neighbor potential respectively. By fitting lattice constant, elastic constants, cohesive energy, vacancy-formation energy, and phonon frequencies at zone boundaries, we can

Table.1. Parameters used to define the functions $F(\rho)$ and $Z(r)$ for $Ni$ and $Pd$.
The positions of the spline knots and the values at the knots are given. Distances are in $\AA$, densities are in $\AA^{-3}$, charge in a.u., energy in ev, $\phi_{3}'$ in $ev/\AA$, and $\phi_{3}''$ in $ev/\AA^{2}$. The lattice constants $a_{0}$ are $3.52\AA$ and $3.89\AA$ for $Ni$ and $Pd$ respectively. The equilibrium densities $\bar{\rho}=0.02855\AA^{-3}$ for $Ni$, $\bar{\rho}=0.01518\AA^{-3}$ for $Pd$.

<table>
  <tr>
    <td>$r$</td>
    <td>$Z_{Ni}(r)$</td>
    <td>$Z'_{Ni}(r)$</td>
    <td>$Z_{Pd}(r)$</td>
    <td>$Z'_{Pd}(r)$</td>
  </tr>
  <tr>
    <td>0.0</td>
    <td>28.0</td>
    <td>0.0</td>
    <td>46.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td>$0.43a_{o}$</td>
    <td>5.1282</td>
    <td></td>
    <td>10.4536</td>
    <td></td>
  </tr>
  <tr>
    <td>$0.65a_{o}$</td>
    <td>0.2890</td>
    <td></td>
    <td>0.3728</td>
    <td></td>
  </tr>
  <tr>
    <td>$0.71a_{o}$</td>
    <td>0.1386</td>
    <td></td>
    <td>0.0907</td>
    <td></td>
  </tr>
  <tr>
    <td>$0.85a_{o}$</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td>$\phi_{3}'$</td>
    <td colspan="2">-0.0099</td>
    <td colspan="2">-0.0592</td>
  </tr>
  <tr>
    <td>$\phi_{3}''$</td>
    <td colspan="2">0.1227</td>
    <td colspan="2">-0.1093</td>
  </tr>
  <tr>
    <td>$\rho$</td>
    <td>$F_{Ni}(\rho)$</td>
    <td>$F''_{Ni}(\rho)$</td>
    <td>$F_{Pd}(\rho)$</td>
    <td>$F''_{Pd}(\rho)$</td>
  </tr>
  <tr>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td>$0.5\bar{\rho}$</td>
    <td>-3.6065</td>
    <td></td>
    <td>-2.8623</td>
    <td></td>
  </tr>
  <tr>
    <td>$1.0\bar{\rho}$</td>
    <td>-5.1593</td>
    <td></td>
    <td>-4.1842</td>
    <td></td>
  </tr>
  <tr>
    <td>$2.0\bar{\rho}$</td>
    <td>-3.3902</td>
    <td></td>
    <td>-2.5571</td>
    <td></td>
  </tr>
  <tr>
    <td>$2.3\bar{\rho}$</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.0</td>
  </tr>
</table>

obtain the embedded energy function $F(\rho)$, the effect charge function of the first neighbors $Z(r)$, and two parameters for force field contributions of the third neighbor potentials $\phi_{3}'$ and $\phi_{3}''$. The parameters and values of spline knots are given in Table 1, the phonon dispersion curves are shown in Fig.1 and Fig.2 with solid

PHONON DISPERSION IN Ni

![](./images/812410317408567296_2.jpg)

Fig.1. Calculated phonon dispersion curves (solid lines) for Ni.The experimental data ( ● )are from Ref.7.

PHONON DISPERSION IN Pd

![](./images/812410317408567296_3.jpg)

Fig.2. Calculated phonon dispersion curves (solid lines) for Pd.The experimental data ( ● )are from Ref.8.

lines. It is obvious that the EAM reproduces the measured phonon frequencies better by the modification of force fields of the third neighbor potentials.

In summary, in this work we have tested the EAM in the application to phonon frequencies of fcc transition metals Ni, Pd and Cu. It is found that the EAM with the first neighbor potential can not assure to reproduce the phonon frequencies at zone boundaries. To reproduce the measured phonon frequencies accurately, we provide a method with the modification of the force fields of the third neighbor potentials by considering somewhat non-uniform distribution of electron densities in real transition metals. The work to study the phonon frequencies for bcc and hcp transition metals, and other fcc transition metals is in progress.

## REFERENCES

1. M.S.Daw and M.I.Baskes,Phys.Rev.B29, 6443(1984).

2. Luo Ningsheng, Xu Wenlan & S.C.Shen, Phys.Stat.Sol.(b)147, 511(1988).

3. Luo Ningsheng, Xu Wenlan & S.C.Shen, Solid State Commun.69, 155(1989).

4. M.S.Daw and R.D.Hatcher, Solid State Commun.56, 697(1985).

5. L.D.Landau and E.M.Lifshiz, Theory of Elasticity (Translated from the Russian), Chapt.1, Pergamon Press, 1960.

6. C.Kittel,Introduction to Solid State Physics, 5th Ed., New York 1976.

7. R.J.Birgeneau, J.Cordes, G.Dolling, and A.D.B.Woods, Phys.Rev.A136, 1359(1964).

8. A.P.Muller and B.N.Brockhouse, Can.J.Phys.49, 704(1971).