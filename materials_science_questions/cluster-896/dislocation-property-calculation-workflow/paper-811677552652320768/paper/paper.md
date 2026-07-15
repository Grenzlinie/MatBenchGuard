# ATOMIC STRUCTURE OF A $60^{\circ}$ DISLOCATION IN BULK SILICON AND GERMANIUM, AND AT Ge/SI INTERFACE.

A. S. NANDEDKAR AND J. NARAYAN

Department of Materials Science and Engineering
North Carolina State University
Raleigh, NC 27695-7916

## ABSTRACT

Atomic structures of $60^{\circ}$ dislocations were calculated in bulk Si and Ge ,and at Ge/Si interfaces, using energy minimization techniques. An empirical three body potential developed by Stillinger-Weber was used for Si ,and the same potential with modified parameters was used for Ge. Two different configurations of a $60^{\circ}$ dislocation (shuffle and glide) were compared. Energetics of a $60^{\circ}$ dislocation in shuffle configuration in bulk Si and Ge , and at Ge/Si interfaces are discussed.

## INTRODUCTION

Atomic structures of dislocations in semiconductors are of great significance while studying electronic characteristics of devices. Atomic arrangements of a core of a dislocation determine its electronic properties. In this paper, we have determined atomic structures of $60^{\circ}$ dislocations in bulk Si and Ge, and Ge/Si interface. Both shuffle and glide configurations of $60^{\circ}$ dislocations are studied, and their geometries and self energies are compared. A $90^{\circ}$ glide partial is also simulated in bulk Si and Ge in an effort to study the dissociation of a $60^{\circ}$ dislocation in a glide set of $\{111\}$ planes. Finally, we have compared an undissociated $60^{\circ}$ dislocation in shuffle configuration at Ge/Si interface [1] with atomic structures of dislocations in bulk Si and Ge. The dislocation configurations were simulated with the help of a computer program using energy minimization techniques [1]. We have used Stillinger-Weber potential [2,3] to calculate energies of the different dislocation configurations.

## METHOD

In the calculations presented here, the Burgers vector of a $60^{\circ}$ dislocation was

Mat. Res. Soc. Symp. Proc. Vol. 141. *1989 Materials Research Society

chosen to be $a/2[01\overline{1}]$ with a dislocation line along the [110] direction in the $(\overline{1}11)$ plane. A block of two consecutive (220) planes is periodic along [110] with a repeat distance of $a/\sqrt{2}$. A total of 1250 atoms from these two planes was used as a computational cell for a simulation of a dislocation. In order to simulate a dislocation in the middle of this computational cell, the atomic sites are shifted in accordance with standard dislocation displacements using isotropic elasticity theory [4]. It is assumed that the isotropic-elasticity theory predicts the displacements of the atoms outside the computational cell. Therefore, several layers of atoms on the boundary of the cell were not relaxed during energy minimization. Thus, the computational cell is assumed to be embedded in the elastic continuum. Atomic structure obtained from this method contained some bonds with lengths varying from 70% to 130% of their ideal value and considerable angular distortions from the ideal bond angle (109° 47'). This structure was then relaxed to the minimum self energy configuration using Stillinger-Weber atomic potential [2,3]. This potential involves a combination of a two body and three body empirical potential energy functions. The two-body potential represents chemical bonding between two atoms and the three-body potential accounts for angles between two bonds made by the same atom. The Stillinger-Weber potential can account for physical properties involving small (elastic constants and phonon spectra) as well as large atomic displacements (properties of liquid and point defects in Si [5]). For bulk Ge, the Stillinger-Weber potential was used with parameters obtained by Ding and Andersen [3].

The computer program that minimizes energy of a dislocation configuration, mainly consists of two subroutines, e.g. ENERGY and LENGTH. The ENERGY subroutine tested different positions around each atom within a specified area (0.0016 Å2) and displaced the atom to the position of minimum energy. The LENGTH subroutine adjusted the bond lengths to within the specified range without calculating the energy of the configuration. A combination of ENERGY and LENGTH subroutines effectively minimized energy of a dislocation configuration.

# RESULTS AND DISCUSSION

Table 1 shows the energies of 60° dislocations in shuffle and glide configurations in

bulk Ge. The calculated atomic structures corresponding to these minimized energies are shown in Figures 1-a and 2-a respectively.

TABLE I
Energies of dislocations in eV/Å

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">60° Dislocation (Shuffle)<br>a/2 &lt;110&gt; {111} | &lt;110&gt;</th>
      <th colspan="2">60° Dislocation (Glide)<br>a/2&lt;110&gt;{111} | &lt;110&gt;</th>
      <th colspan="2">90 ° Glide Partial<br>a/6&lt;112&gt;{111} | &lt;110&gt;</th>
    </tr>
    <tr>
      <th></th>
      <th>Core (5 Å)</th>
      <th>Total, R= 28Å</th>
      <th>Core (5 Å )</th>
      <th>Total, R=28 Å</th>
      <th>Core (5 Å )</th>
      <th>Total, R=28 Å</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Si</td>
      <td>0.98</td>
      <td>2.1</td>
      <td></td>
      <td></td>
      <td>0.55</td>
      <td>0.9</td>
    </tr>
    <tr>
      <td>Ge</td>
      <td>1.05</td>
      <td>2.13</td>
      <td>0.93</td>
      <td>4.62</td>
      <td>0.95</td>
      <td>1.36</td>
    </tr>
    <tr>
      <td>Ge/Si</td>
      <td>1.13</td>
      <td>5.74</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

Figure 1-a depicts a $60^\circ$ dislocation in bulk Ge in shuffle configuration. The core of this dislocation contains an octaring of atoms whereas the elastic region of the dislocation contains hexarings. In Figure 1-b, energy of the dislocation in Figure 1-a is plotted as a function of $\ln(R)$.

![](./images/811677552652320768_1.jpg)

Atomic structure of a $60^\circ$ dislocation
(shuffle) in bulk Ge.
a

![](./images/811677552652320768_2.jpg)

E vs. $\ln(R)$ plot
b

Figure 1

![](./images/811677552652320768_3.jpg)

Atomic structure of a $60^{\circ}$ dislocation (glide) in bulk Ge.

a

![](./images/811677552652320768_4.jpg)

E vs. $\ln(R)$ plot

b

Figure 2

According to continuum elasticity theory and superposition principle, the self energy of a mixed dislocation is the sum of self energies of a screw dislocation ($b_S = b \cos \beta$) and an edge dislocation ($b_e = b \sin \beta$). $\beta$ is the angle between the sense vector and the Burgers vector of the dislocation and is $60^{\circ}$ for a mixed $60^{\circ}$ dislocation. The energy per unit length of a dislocation line within a cylinder of radius R is given by
$$E_{total} = (\mu b^2/4\pi) [\cos^2 \beta + \sin^2 \beta/(1-v)] \ln(R/r_C) + E_C,$$
where $\mu$ is the shear modulus, b the Burgers vector, v the Poisson's ratio, $\beta = 60^{\circ}$, $r_C$ the core radius and $E_C$ the core energy. Thus total energy varies linearly with $\ln(R)$ in the elastic region of the dislocation. This relation is shown in Figure 1-b for a $60^{\circ}$ dislocation in shuffle configuration in bulk Ge. Using the above continuum expression, the slope of this line is determined to be 0.604 eV/Å (Si) and 0.533 eV/Å (Ge) . From our calculations slope of this line is 0.609 eV/Å for Ge showing a reasonably good agreement. In Figure 2-b, energy of a $60^{\circ}$ dislocation in glide configuration is plotted against $\ln(R)$. In Figures 1-b and 2-b, the point at which the plot of E Vs $\ln(R)$ deviates from linearity, is the point that gives the core radius of the dislocation. From our calculations, the core radii of all dislocations are found to be approximately $5Å$.

A calculated structure of a $90^\circ$ glide partial dislocation in bulk Ge is shown in Figure 3-a. The core contains a pentaring and a septaring. The arrangement of atoms near the glide plane on the right side of the dislocation contains a stacking fault. The plot of E Vs ln(R) (Figure 3-b) was plotted and a slope of $0.224\ \text{eV}/\text{\AA}$ was obtained for Ge.

Using the continuum expression, we obtain values of slope to be $0.213\ \text{eV}/\text{\AA}$ for Si or $0.187\ \text{eV}/\text{\AA}$ for Ge.

![](./images/811677552652320768_5.jpg)
Atomic configuration of a $90^\circ$ glide partial dislocation in bulk Ge.
a

![](./images/811677552652320768_6.jpg)
E vs. ln(R) plot
b

Figure 3

Our calculations show that it is energetically favorable for a $60^\circ$ dislocation to exist in undissociated form in a shuffle configuration, and in dissociated form in a glide configuration.

We have included, in Table I, the energy of a $60^\circ$ (shuffle) dislocation simulated at Ge/Si interface [1]. This energy is higher than the energy of the same dislocation in bulk Si or Ge, although the geometrical arrangement of atoms is identical for both bulk Si and Ge, and Ge/Si interface. This is because of the residual coherent strain in the film. The coherent strain results from the $4\%$ mismatch between the lattice constants of Si and Ge. One dislocation does not relieve entire coherent strain in the film. A crossgrid of dislocations at a spacing of $48\ \text{\AA}$ is necessary to relieve the coherent strain completely [1].

The core of a $60^\circ$ dislocation in shuffle configuration has an unsatisfied or dangling

bond. Despite its presence, the total energy of this dislocation is about 50% of the total energy of a $60^\circ$ dislocation in glide configuration. All atomic structures of dislocations calculated here have bond lengths within -3% to +3% of the ideal value. Thus for a $60^\circ$ dislocation in glide configuration, the energy contribution due to bending of bonds is about three times higher than the energy contribution due to stretching of bonds.

## ACKNOWLEDGMENT

Part of this work was supported by National Science Foundation - Engineering Research Center Grant CDR - 8721505 on Advanced Materials Processing.

## SUMMARY

We have determined the atomic structures of $60^\circ$ dislocations in shuffle and glide configurations in bulk Si and Ge, and compared it with a shuffle dislocation configuration at Ge/Si interface. When the self energies of shuffle and glide configurations are compared with a $90^\circ$ glide partial in bulk Ge and Si, it is found that an undissociated $60^\circ$ dislocation is likely to exist in shuffle configuration, while it will dissociate in a glide configuration.

## REFERENCES

1. A. S. Nandedkar and J. Narayan, Phil. Mag.A , 56 (5), 625 , (1987) ; to be presented at the Aug. 1989 conference at University of Virginia, Charlottesville.

2. F.H.Stillinger and T.A.Weber, Phys.Rev.B, 31 (8), 5262, (1985).

3. K.Ding and H.C.Andersen, Phys. Rev. B, 34 (10), 6987, (1986).

4. J.P.Hirth and J.Lothe, Theory of Dislocations, (Mcgraw-Hill Book Company,New York, 1968).

5. B.W.Dodson, Phys. Rev. B 33 (10), 7361, (1986).