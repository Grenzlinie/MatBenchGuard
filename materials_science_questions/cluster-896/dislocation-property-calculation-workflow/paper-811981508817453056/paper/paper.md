![](./images/811981508817453056_1.jpg)

Philosophical Magazine A

ISSN: 0141-8610 (Print) 1460-6992 (Online) Journal homepage: http://www.tandfonline.com/loi/tpha20

# On the structure and energy of dissociated dislocations in F.C.C. metals

F. Gao & D. J. Bacon

To cite this article: F. Gao & D. J. Bacon (1992) On the structure and energy of dissociated dislocations in F.C.C. metals, Philosophical Magazine A, 66:5, 839-847, DOI: 10.1080/01418619208201593

To link to this article: http://dx.doi.org/10.1080/01418619208201593

![](./images/811981508817453056_2.jpg)
Published online: 13 Sep 2006.

![](./images/811981508817453056_3.jpg)
Submit your article to this journal ![](./images/811981508817453056_4.jpg)

![](./images/811981508817453056_5.jpg)
Article views: 22

![](./images/811981508817453056_6.jpg)
View related articles ![](./images/811981508817453056_7.jpg)

![](./images/811981508817453056_8.jpg)
Citing articles: 8 View citing articles ![](./images/811981508817453056_9.jpg)

Full Terms & Conditions of access and use can be found at
http://www.tandfonline.com/action/journalInformation?journalCode=tpha20

Download by: [University of California, San Diego]
Date: 29 June 2016, At: 13:55

PHILOSOPHICAL MAGAZINE A, 1992, VOL. 66, No. 5, 839-847

# On the structure and energy of dissociated dislocations in f.c.c. metals

By F. GAO† and D. J. BACON

Department of Materials Science and Engineering, The University,
P.O. Box 147, Liverpool L69 3BX, England

[Received 24 February 1992 and accepted 2 March 1992]

## ABSTRACT
Atomic-scale computer simulations using many-body interatomic potentials have been carried out to investigate the energy changes and equilibrium configur- ations associated with the dissociation of perfect and Lomer dislocations in copper and silver. The state of minimum energy is close in both cases to that given by the use of linear elasticity theory, and the Lomer dislocation adopts the asymmetric Lomer-Cottrell arrangement predicted by the same approach. The absolute energy values obtained from elasticity for the equilibrium dissociated configurations agree well with those found by computer simulation, but the elastic model does not accurately describe the energy *changes* associated with dissociation of the Lomer dislocation, thus confirming the conclusions drawn recently by Saada and Douin.

## § 1. INTRODUCTION
It is well known that dissociated dislocations play important roles in the plastic deformation of metals. Two Shockley partials separated by a ribbon of stacking fault have been observed in a variety of metals and, by using linear elasticity theory to relate the partial spacing $d$ to the stacking-fault energy $\gamma$, these observations have provided a means of measuring $\gamma$. Composite arrangements of dislocations are also of significance, for they can form barriers to glide processes or can provide routes for dislocation glide on non-conventional slip systems. The Lomer (L) dislocation with Burgers vector $\mathbf{b}=\frac{1}{2}\langle 110\rangle$ on a $\{001\}$ plane is the best known of these, for it can dissociate into the Lomer-Cottrell (LC) configuration of two Shockley partials and one stair-rod partial (all in a pure edge orientation), linked by two intrinsic faults on inclined $\{111\}$ planes.
An example of such a dissociation is

$$\frac{1}{2}[110]=\frac{1}{6}[11 \overline{2}]+\frac{1}{6}[110]+\frac{1}{6}[112]. \tag{1}$$

A similar arrangement can be achieved by the favourable interaction of dissociated $\frac{1}{2}[10 \overline{1}]$ and $\frac{1}{2}[011]$ dislocations on the $(111)$ and $(11 \overline{1})$ planes respectively. Although LC dislocations have been identified in deformed f.c.c. metals, there is apparently only one reported observation of the dissociated state in a pure metal, namely that of Korner and Karnthaler (1981) in silver. This raises the question as to what is the stable arrangement of the LC dislocation. From an analysis of the anisotropic elastic interaction energy, Korner, Schmid and Prinz (1979) showed that the configuration of lowest energy is asymmetric in which the spacings $d_1$ and $d_2$ of the Shockleys from the

† Permanent address: Department of Materials Science, Lanzhou University, Lanzhou, Gansu, P.R. China.

0141-8610/92 $3.00 © 1992 Taylor & Francis Ltd.

stair rod are not equal. Their results for three pure metals and three Cu-Al alloys all give $d_{1}/d_{2}=3.82\pm0.2$. More recently, Bonneville and Douin (1990) have used isotropic elastic interaction energies between the partials to show that $d_{1}/d_{2}=3.82$, independent of $\gamma$ and the (isotropic) elastic constants.

The purpose of the work reported in the present paper was to use computer simulation of the atomic structure of the LC dislocation to see whether the general value of $d_{1}/d_{2}$ predicted by elasticity theory applies on the atomic scale. Furthermore, we wished to investigate a point raised by Bonneville and Douin and discussed in more detail recently by Saada and Douin (1991), that, when the total energy of the L and LC dislocations is considered, the LC state may not represent a reduction. Bonneville and Douin reported that the observed projected width of 0.7 nm of the L dislocation in copper was much less than that of 1.65 nm expected for the LC arrangement. Saada and Douin argue that uncertainties arising from the use of linear elasticity are such that even the sign of the energy change between the L and LC dislocations is unpredictable for partial spacings less than $20a/2^{1/2}$, where $a$ is the f.c.c. lattice parameter. Also they deduce that similar uncertainty applies to the dissociation of a perfect dislocation into two Shockleys for $d<6a/2^{1/2}$. We consider these points in more detail below.

## §2. COMPUTATIONAL METHOD

The XLITE suite of static relaxation programs, developed by Bacon and Martin (1981) from the DEVIL package written by M. J. Norgett at Harwell, were used for the simulations. The computational cell with $x,y,z$ axes $[11\overline{2}]$, [111] and $[1\overline{1}0]$ was generated with periodic boundary conditions along $[1\overline{1}0]$, the dislocation line direction. Fixed boundaries were used for the other two directions, with an outer region of sufficient thickness to contain a full set of neighbours for all inner-region atoms. The cell was two atomic planes thick in the $z$ direction, and approximately square in $x$-$y$ section. The number of relaxable atoms was 4600. For a particular dislocation configuration, all atoms (inner and outer) were initially displaced according to the linear isotropic elastic solution for the displacement field of (perfect or partial) dislocations at chosen origins, as defined in more detail below. The inner atomic positions were then relaxed to minimize the potential energy by the method of conjugate gradients.

The interatomic energy and forces were calculated by use of the $n$-body potentials of Finnis-Sinclair form for Cu and Ag developed by Ackland, Tichy, Vitek and Finnis (1987). These potentials fit the lattice parameter, elastic constants, cohesive energy and vacancy formation energy of each metal and give $\gamma$ values consistent with the range of experimental estimates, namely $36\,\text{mJ}\,\text{m}^{-2}$ for Cu and $23\,\text{mJ}\,\text{m}^{-2}$ for Ag. As noted above, experimental observation of dissociated L dislocations has only been reported for Ag.

## §3. RESULTS

Consider first the dissociation of a perfect $60^{\circ}$ dislocation lying along $[1\overline{1}0]$ with $\mathbf{b}_{\mathbf{p}}=\frac{1}{2}[10\overline{1}]$. It can dissociate into the edge and $30^{\circ}$ Shockley partials with $\mathbf{b}_{\mathbf{S}}$ equal to $\frac{1}{6}[11\overline{2}]$ and $\frac{1}{6}[2\overline{1}\overline{1}]$ and spacing $d$. Minimization of the combined stacking-fault and linear elastic interaction energies predicts $d=3.63\,\text{nm}$ for Cu and $4.73\,\text{nm}$ for Ag, corresponding to $10.0a$ and $11.6a$ respectively. The actual relaxed atomic configuration of lowest energy in Cu for an inner region of 4600 atoms is plotted in $[1\overline{1}0]$ projection in fig. 1(a). The edge partial is on the right, and the arrows display the relative displacement $\Delta u_{x}$ of atoms in the edge direction $[11\overline{2}]$, normalized to $\pm$ half the

Fig. 1

![](./images/811981508817453056_10.jpg)

![](./images/811981508817453056_11.jpg)

$[1\overline{1}0]$ projections of the relaxed configuration of minimum energy for (a) the dissociated perfect
$60^{\circ}$ dislocation and (b) the LC dislocation in copper.

length of the perfect Burgers vector $\mathbf{b}_\mathrm{p}$, that is $a/2 \times 2^{1/2}$. The equivalent plot for Ag is similar, but the core is slightly wider. From a graph of $\Delta u_x$ against $x$, the spacing between the partials may be taken as the distance between the points where $\Delta u_x$ equals $\mathbf{b}_\mathrm{p}/6$ and $2\mathbf{b}_\mathrm{p}/3$. This gives $d$ equal to $11.9a$ for Cu and $14.3a$ for Ag, that is slightly wider than the estimates based on elasticity theory. The dependence of the relaxed energy on partial spacing is shown by the data for the two metals in fig. 2(a), where the potential energy of the computational cell (of length $a/2^{1/2}$ in the line direction) minus the energy of the perfect undislocated crystal is plotted agains $d$ (in units of $a$). These data were obtained by starting from unrelaxed states corresponding to different values of the

Fig. 2

![](./images/811981508817453056_12.jpg)

![](./images/811981508817453056_13.jpg)

(a) Dislocation energy against relaxed partial spacing for the dissociated perfect $60^\circ$ dislocation in Cu and Ag. The variation in the dislocation energy with unrelaxed $d_2$ value for several values of $d_1$ for the LC dislocation is plotted in (b) and (c) for Cu and Ag respectively.

spacing of the origins of the elastic displacement solutions for the two partials and then measuring $d$ (as defined above) in each block after relaxation. The initial unrelaxed spacing and energy are shown against each relaxed data point. It can be seen that an initially perfect dislocation relaxes to $d$ values of about $6a$ and $5a$ in Cu and Ag respectively, and that the lowest-energy state is not achieved because of the influence of the outer region atoms which are held rigidly at their initial elastic coordinates. In fact, the relaxed $d$ values are larger than their unrelaxed counterparts for spacings less than about $10a$ in Cu and $11a$ in Ag, and this relationship is reversed for spacings greater than about $12a$ in Cu and $15a$ in Ag. between these limits, the unrelaxed and relaxed spacings are in approximate agreement and the dislocation energy is a minimum. The reduction in energy during relaxation in fig. 2 (a) varies between about 22 and $45\%$ and, although there is occasional discrepancy between the trends in the unrelaxed and relaxed energy with $d$, this probably only reflects the sensitivity of the unrelaxed value to the precise location of the origins for the elastic displacements.

The variation in the energy and form of the L and LC dislocations has been investigated in one of two ways. First, the spacings $d_1$ and $d_2$ between the two Shockley partials and the stair-rod dislocation were set equal in the initial unrelaxed state, and the relaxed energy was then computed as a function of the $d_1=d_2$ value. However, the elastic analysis predicts an asymmetric arrangement with $d_1 \neq d_2$ (see $\S 1$), and the undissociated L dislocation with $d_1=d_2=0$ was indeed found to relax to an asymmetric LC. We therefore carried out simulations in which $d_1$ was fixed initially at one of several values close to that calculated by elasticity theory (Korner et al. 1979, Bonneville and Douin 1990) and studied the relaxed values of energy and $d_2$ for each $d_1$. The results of these investigations are summarized by the data in figs. 2 (b) and (c) for Cu and Ag respectively, where the relaxed dislocation energy is plotted against $d_2$, and the

unrelaxed energy is given against each data point. The $d_1$ and $d_2$ values given in these figures are for the unrelaxed state but, in the vicinity of the minima on the plots, the relaxed and unrelaxed spacings are close in value.

It can be seen that the symmetric LC dislocation is not the dislocation of lowest energy, and that the spacing of unstable equilibrium given by elasticity (of approxi- mately $4a$ for Cu and $6.5a$ for Ag) is very close to the atomistic result. The stable LC dislocation of lowest energy is clearly seen to be asymmetric, with $d_1$ and $d_2$ values of approximately $8.2a$ and $2.4a$ respectively for Cu and $10.7a$ and $3.0a$ respectively for Ag. These values compare reasonably well with predictions from elasticity of $6.3a$ and $1.6a$ respectively for Cu and $10.3a$ and $2.7a$ respectively for Ag. Furthermore, the ratio $d_1/d_2$ is $3.4$ for Cu and $3.6$ for Ag, compared with a value of $3.8$ for both in the elastic model. There is rather more discrepancy in figs. $2(b)$ and $(c)$ between the trends in the unrelaxed and relaxed energies than was seen in fig. $2(a)$, but again it probably arises because of sensitivity to the precise position in which the three origins for the elastic displacements were placed.

An atomic projection of the lowest energy configuration for the LC dislocation in the relaxed Cu crystal is plotted in fig. $1(b)$

### §4. Discussion
The most noticeable feature of the results presented above is the basically good agreement between the equilibrium configuration predicted simply on the basis of linear elasticity and that revealed by computer simulation. Both the spacing of the two Shockley partials in a dissociated perfect dislocation and the separation of the two Shockleys from the stair-rod partial in a dissociated L dislocation are close at equilibrium to the values given by the elastic analysis. Furthermore, the LC dislocation has been clearly seen to adopt an asymmetric form in good correspondence to that suggested by the elastic model. Some caution is required when computer simulation is used to estimate the spacing of dislocations, because not only is there an uncertainty in defining the centre of the core in an atomic structure but also the relaxed energy is not a sensitive function of partial spacing near the equilibrium state. Both these points are obvious from figs. 1 and 2. Any discrepancies between the results of atomistic and elastic modelling can easily be accounted for by the uncertainties that these features introduce.

The actual energy computed here is more difficult to assess in quantitative terms because the absolute value depends on the size of the computational block and the unrelaxed value varies even when the line position is moved by only small amounts compared with $a$. Also, it is not very meaningful to compare relaxed with unrelaxed energies, since the former vary from about 50 to $80\%$ of the latter, depending on the initial configuration. Nevertheless, it is worthwhile considering the trends and the magnitude of changes in the energy with changes in the dislocation structure because, as pointed out by Saada and Douin (1991), it may not be possible to estimate these changes reliably from elasticity theory alone, in view of the uncertainties in the core radius and core energy parameters which occur in that approach.

First, with regard to the dissociation of a perfect dislocation, we see that the unrelaxed energy exhibits a large reduction of $23\%$ in Cu and $33\%$ in Ag between $d=0$ and the equilibrium value. However, the equivalent change for the relaxed atomic state, which is of more interest for theories involving dislocation splitting and constriction, cannot be estimated because the relaxed energy for the unstable undissociated perfect dislocation is unknown. To obtain this change, we have to reassess the elastic model.

Following the notation of Saada and Douin (1991) we write the energy per unit length of a straight dislocation in the usual form

$$
E=K \ln \left(\frac{R}{\lambda r}\right), \tag{2}
$$

where $K$ is the energy factor, $R$ is the outer radius of the elastic cylinder, $r$ is the core cut-off radius and $\lambda$ is a parameter chosen so that $E$ includes the nonlinear core energy. We may reasonably assume that $r$ scales with $b$ for each dislocation and, since $\lambda$ is as yet undetermined, replace $r$ by $b$. Thus, using isotropic elasticity theory for the perfect and dissociated $60^{\circ}$ dislocations considered here, we find the following:

$$
E_{\mathrm{P}}=K_{\mathrm{P}} \ln \left(\frac{R}{\lambda_{\mathrm{P}} b_{\mathrm{P}}}\right), \tag{3}
$$

where

$$
K_{\mathrm{P}}=\frac{\mu a^{2}(4-v)}{32 \pi(1-v)} ; \tag{4}
$$

$$
E_{\mathrm{D}}=K_{\mathrm{P}} \ln \left(\frac{R}{\lambda_{\mathrm{S}} b_{\mathrm{S}}}\right)-K_{\mathrm{I}} \ln \left(\frac{d}{e \lambda_{\mathrm{S}} b_{\mathrm{S}}}\right), \tag{5}
$$

where

$$
K_{\mathrm{I}}=\frac{\mu a^{2}}{24 \pi(1-v)} ; \tag{6}
$$

$$
E_{\mathrm{P}}-E_{\mathrm{D}}=K_{\mathrm{I}} \ln \left(\frac{d}{\rho_{\mathrm{D}}}\right), \tag{7}
$$

where

$$
\rho_{\mathrm{D}}=e \lambda_{\mathrm{S}} b_{\mathrm{S}}\left(\frac{\lambda_{\mathrm{P}} b_{\mathrm{P}}}{\lambda_{\mathrm{S}} b_{S}}\right)^{K_{\mathrm{P}} / K_{\mathrm{I}}}. \tag{8}
$$

Here, $\mu$ is the shear modulus, $v$ is Poisson's ratio and the subscripts P, D and S denote perfect, dissociated and Shockley respectively. Equations (3), (5), (7) and (8) apply for any line orientation, but $K_{\mathrm{P}}$ and $K_{\mathrm{I}}$ are specifically for the $60^{\circ}$ case. Saada and Douin argue that the uncertainties in $\rho_{\mathrm{D}}$ are such that even the sign of $E_{\mathrm{P}}-E_{\mathrm{D}}$ in eqn. (7) may not be positive unless $\gamma$ is sufficiently small for $d$ to be larger than about $10 b_{\mathrm{p}}$.

To test this, consider the absolute energy values given in fig. 2 (a). They correspond to a block of $N=4600$ atoms, and we may take the area per atom $a^{2} / 2 \times 2^{1 / 2}$ in the [$\overline{1} 10$] projection of fig. 1 to be equal to $\pi R^{2} / N$. Furthermore, it is reasonable to assume $\lambda_{\mathrm{P}}=\lambda_{\mathrm{S}}=\lambda$. Hirth and Lothe (1982) suggest, from a variety of evidence, that $\lambda$ may be about $\frac{1}{4}$. With this value, and using the appropriate 'effective' isotropic $\mu$ and $v$ values for $\mathrm{Cu}$ and $\mathrm{Ag}$ tabulated by Bacon (1985), we find that $E_{\mathrm{D}}$ given by eqn. (5) for a straight line of length $a / 2^{1 / 2}$ is $2 \cdot 25 \mathrm{eV}$ for $\mathrm{Cu}$ and $2.07 \mathrm{eV}$ for $\mathrm{Ag}$. Remarkably, these values are within $5 \%$ of the energy at the minima in the curves in fig. 2 (a). On the basis of this satisfactory agreement, we find by taking $\lambda=\frac{1}{4}$ in eqn. (7) for the dissociation of a line of length $a / 2^{1 / 2}$ that $E_{\mathrm{P}}-E_{\mathrm{D}}$ is $0.48 \mathrm{eV}$ for $\mathrm{Cu}$ and $0.49 \mathrm{eV}$ for $\mathrm{Ag}$, that is about $18 \%$ of the total energy $E_{\mathrm{P}}$. It would appear that the choice of $\lambda=\frac{1}{4}$ gives considerably smaller values of $\rho_{\mathrm{D}}$ (about $1 \cdot 2 a$ in $\mathrm{Cu}$ and $\mathrm{Ag}$ ) than anticipated by Saada and Douin for dissociation of the screw dislocation. By varying the size of the atomic block between

3600 and 5600 atoms, we actually find that $\lambda=0 \cdot 2$ gives an excellent fit to the computed $E_{\mathrm{D}}$ values, but, in view of the uncertainties inherent in the approximation of isotropic elasticity, we did not consider it worthwhile to pursue this point further.

Saada and Douin also considered the change in energy between the L and LC dislocations using isotropic elasticity and found that the latter is only expected to have a lower energy than the former if $d$, as defined for the equilibrium spacing of two Shockley partials, is greater than about $20 b_{\mathrm{p}}$, that is about $14 a$. This large value leads to doubt as to whether the LC configuration is actually stable with respect to the L state in pure f.c.c. metals. We have reconsidered this in the light of the preceding discussion. Using the energy form of eqn. (2), with $r=b$ for each dislocation, and the total interaction energy for the LC dislocation given by Bonneville and Douin, we find that $\dagger$

$$
E_{\mathrm{L}}-E_{\mathrm{LC}}=\frac{2}{9} K_{\mathrm{L}} \ln \left(\frac{\bar{d}}{\rho_{\mathrm{LC}}}\right), \tag{9}
$$

where

$$
\bar{d}=\frac{1}{2}\left(d_{1}+d_{2}\right) \tag{10}
$$

and

$$
\rho_{\mathrm{LC}}=13 \cdot 5 \lambda b_{\mathrm{L}}\left(\frac{b_{\mathrm{L}}}{b_{\mathrm{SR}}}\right)^{1 / 2}\left(\frac{b_{\mathrm{L}}}{b_{\mathrm{S}}}\right)^{3}. \tag{11}
$$

Here, the subscript SR denotes stair-rod. Also, we have assumed that $\lambda_{\mathrm{L}}=\lambda_{\mathrm{S}}=\lambda_{\mathrm{SR}}=\lambda$, as above. Since $b_{\mathrm{L}}=b_{\mathrm{p}}=a / 2^{1 / 2}$, eqn. (11) reduces to $\rho_{\mathrm{LC}} \approx 21 a$ if $\lambda=\frac{1}{4}$, which is of the order of the estimate derived by Saada and Douin. In a similar fashion, the total energy of the LC dislocation in a cylindrical medium of radius $R$ is

$$
E_{\mathrm{LC}}=K_{\mathrm{L}}\left[\ln \left(\frac{R}{\lambda a}\right)-\frac{2}{9} \ln \left(\frac{\bar{d}}{410 \lambda a}\right)\right]. \tag{12}
$$

With $\bar{d}=5 \cdot 3 a$ for $\mathrm{Cu}$ and $6 \cdot 5 a$ for $\mathrm{Ag}$, as revealed by our simulations, and the same values for $R$ and $\lambda$ as used above, we find that for a line length $a / 2^{1 / 2}, E_{\mathrm{LC}}$ is $3 \cdot 23 \mathrm{eV}$ for $\mathrm{Cu}$ and $3.02 \mathrm{eV}$ for $\mathrm{Ag}$. These values compare with $3 \cdot 45$ and $3 \cdot 26 \mathrm{eV}$ respectively for the stable LC configurations found in our computational blocks (see fig. $2(b)$ ). Again the two sets of energies are surprisingly close, for they agree to within $8 \%$. However, because $\bar{d}$ for the LC dislocation in both $\mathrm{Cu}$ and $\mathrm{Au}$ is less than the estimate $\rho_{\mathrm{LC}} \approx 21 a$ derived above, the difference $E_{\mathrm{L}}-E_{\mathrm{LC}}$ given by eqn (9) is negative. Thus the elastic approximation can provide a good estimate for $E_{\mathrm{LC}}$ but not for the energy reduction which, from our atomistic modelling, is associated with dissociation of the $\mathrm{L}$ dislocation. This suggests that the change is, at best, small and confirms the view of Saada and Douin that it cannot be analysed in a sensible way by elasticity theory for pure metals.

We may therefore draw the following conclusions.

(1) From atomic-scale simulations using the best available many-body potentials for $\mathrm{Cu}$ and $\mathrm{Ag}$, it has been found that the dissociated state of minimum energy for perfect and L dislocations is very close in terms of partial spacing to that

---
$\dagger$ The general equation for the interaction energy given by Bonneville and Douin (1990), their eqn. (1), is correct, but the formula without a number which follows it is in error. The additional term $\ln \left(3^{1 / 2} / 2\right)-2$ should be inserted in the expression in squared brackets.

calculated on the basis of elasticity theory. Furthermore, the latter dislocation adopts an asymmetric LC arrangement, as first predicted from the elasticity model by Korner *et al.* (1979).

(2) The energy per unit length of line for the stable dissociated dislocations is strikingly close to the elasticity estimates when the latter employ the energy form of eqn. (2) with $r=b$ and $\lambda \approx 0.25$. Because of the uncertainties in this analysis, and errors introduced by the approximation of isotropic elasticity, we did not investigate how $\lambda$ might vary with line type and orientation.

(3) The elastic approach predicts that $E_{\mathbf{P}}-E_{\mathbf{D}}$ is positive for smaller values of $d$, that is for larger values of $\gamma$, than suggested by Saada and Douin (1991). The same approach for $E_{\mathbf{L}}$ and $E_{\mathbf{L C}}$ gives a sign for the change $E_{\mathbf{L}}-E_{\mathbf{L C}}$ which is not consistent with the results of the atomistic simulations. The variations found in the latter were small, however, and close to thermal values, and this may well lie at the heart of the observation of Saada and Douin that LC dislocations have not been observed in pure f.c.c. metals.

## ACKNOWLEDGMENTS
We acknowledge very helpful comments on an early version of this paper from Dr Saada and Dr Douin, and the Chinese Government and the British Council for an award to Gao Fei under the Sino-British Friendship Scholarship Scheme.

## REFERENCES
ACKLAND, G. J., TICHY, G., VITEK, V., and FINNIS, M. W., 1987, *Phil. Mag. A*, **56**, 735.
BACON, D. J., 1985, *Fundamentals of Deformation and Fracture*, edited by B. A. Bilby, K. J. Miller and J. R. Willis (Cambridge University Press), p. 401.
BACON, D. J., and MARTIN, J. W., 1981, *Phil. Mag. A*, **43**, 883.
BONNEVILLE, J., and DOUIN, J., 1990, *Phil. Mag. A*, **62**, 247.
HIRTH, J. P., and LOTHE, J., 1982, *Theory of Dislocations*, second edition (New York: Wiley), p. 231.
KORNER, A., and KARNTHALER, H. P., 1981, *Phil. Mag. A*, **44**, 275.
KORNER, A., SCHMID, H., and PRINZ, F., 1979, *Phys. Stat. sol. (a)*, **51**, 613.
SAADA, G., and DOUIN, J., 1991, *Phil. Mag. Lett.*, **64**, 67.