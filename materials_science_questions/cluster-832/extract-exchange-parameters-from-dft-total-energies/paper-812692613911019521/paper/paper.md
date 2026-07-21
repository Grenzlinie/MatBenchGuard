The spin-wave contribution to the specific heat of $\text{MnF}_2$, $\text{FeF}_2$, $\text{CoF}_2$ and $\text{NiF}_2$

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1969 J. Phys. C: Solid State Phys. 2 2329

(http://iopscience.iop.org/0022-3719/2/12/317)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 132.239.1.231
This content was downloaded on 21/08/2015 at 19:58

Please note that terms and conditions apply.

# The spin-wave contribution to the specific heat of MnF₂, FeF₂, CoF₂ and NiF₂

N. A. BEGUM, A. P. CRACKNELL, S. J. JOSHUA and J. A. REISSLAND

Department of Physics, University of Essex, Wivenhoe Park, Colchester, Essex

MS. received 7th May 1969, in revised form 28th July 1969

Abstract. By making use of the recently measured spin-wave dispersion relations we have calculated the spin-wave contributions to the low-temperature specific heats of antiferromagnetic MnF₂, FeF₂, CoF₂ and NiF₂ from 0 to 50 °K (0 to 35 °K for CoF₂) using two different numerical methods. The results are compared with the experimental measurements of Stout and Catalano for temperatures of 15 °K and above; it is suggested that further experimental measurements below 15 °K would be worth while.

## 1. Introduction

The use of the measured or calculated phonon dispersion relations in calculating the lattice contribution to the specific heat of a solid is now well established. In a similar way the measured or calculated magnon dispersion relations can be used to calculate the spin-wave contribution to the specific heat of a magnetic solid; this has been done for UO₂ (De Batist et al. 1967) and in a preliminary calculation for NiF₂ (Joshua and Cracknell 1969 a). Experimental measurements of the magnon dispersion relations of MnF₂, FeF₂, CoF₂ and NiF₂ have recently become available so that it is now possible to calculate the spin-wave contribution to the specific heat of these materials for comparison with the experimental measurements of Stout and Catalano (1955).

## 2. Spin-wave contribution to the specific heat of an antiferromagnet

We assume that for any given antiferromagnetic crystal the spin-wave dispersion relations, ν(k) as a function of k, are known analytically. The magnon density of states g(ν) dν can then be calculated and the total energy U_M of those spin waves which are actually excited, at temperature T, is given by

$$
U_{\mathrm{M}}=\int_{0}^{\infty} \frac{h \nu g(\nu) \mathrm{d} \nu}{\exp (h \nu / k T)-1}. \tag{1}
$$

The contribution C_M(T) to the specific heat of the crystal, at a given temperature T, due to the excitation of spin waves is therefore given by ∂U_M/∂T so that

$$
C_{\mathrm{M}}(T)=R \int_{0}^{\infty} \frac{x^{2} \mathrm{e}^{x} g(\nu) \mathrm{d} \nu}{\left(\mathrm{e}^{x}-1\right)^{2}} \tag{2}
$$

where $x=h \nu / k T$.

It is possible to use the magnon dispersion relations to calculate g(ν), the density of states, and then to evaluate C_M(T) by use of equation (2). However, this involves two separate numerical integrations and as an alternative procedure we could avoid the necessity of evaluating ν(k) at a large number of points to obtain g(ν) by making use of the symmetry properties of the Brillouin zone. If we know the value of a function along a given direction we can find its value elsewhere by expanding about the known line in terms of functions which have the same symmetry as the required function. In this way we can evaluate a function of frequency (in this case a contribution to the specific heat) along given lines and then interpolate between the lines. Such a procedure has been developed for lattice vibrations by Houston (1948), Horton and Schiff (1959), Betts et al. (1956) and Horton and Leech (1963). These authors were dealing with full cubic symmetry. For our case we require functions with full tetragonal symmetry.

2330
N. A. Begum, A. P. Cracknell, S. J. Joshua and J. A. Reissland

Considering explicitly a six-direction method we have used the orthogonal functions given by Bell (1954):

$$
\left.
\begin{aligned}
\chi_{1} &=1 \\
\chi_{2} &=x^{4}+y^{4}+z^{4}-3 / 5 \\
\chi_{3} &=x^{2} y^{2} z^{2}+\chi_{2} / 22-1 / 105 \\
\chi_{4} &=2 z^{2}-x^{2}-y^{2} \\
\chi_{5} &=2 z^{4}-x^{4}-y^{4}-6 \chi_{4} / 7 \\
\chi_{6} &=2 z^{6}-x^{6}-y^{6}-15 \chi_{5} / 11-5 \chi_{4} / 7
\end{aligned}
\right\} \quad (3)
$$

which belong to the totally symmetrical representation, $\Gamma_{1}{ }^{+}$, of the holosymmetric tetragonal point group $4 / m m m\left(\mathrm{D}_{4 h}\right)$. If $f(\boldsymbol{k})$ is the function we require to integrate we can write

$$
f(\boldsymbol{k})=\sum_{i=1}^{6} C_{i} \chi_{i}(\boldsymbol{k}) \tag{4}
$$

and therefore

$$
\begin{aligned}
F &=\int_{0}^{\pi} \int_{0}^{2 \pi} f(\boldsymbol{k}) \sin \theta \mathrm{d} \theta \mathrm{d} \phi \\
&=4 \pi C_{1}
\end{aligned} \tag{5}
$$

since the $\chi_{i}$ are mutually orthogonal and in particular they are all orthogonal to $\chi_{1}=1$. Hence, from the value of $f(\boldsymbol{k})$ along $\boldsymbol{k}$, we can find $F$ from the coefficient of $\chi_{1}$ in the expansion.

Generalizing this, we can write

$$
F=\sum_{\boldsymbol{k}} C(\boldsymbol{k}) f(\boldsymbol{k}) \tag{6}
$$

and hence six simultaneous equations

$$
\left.
\begin{aligned}
\sum_{[\boldsymbol{k}]} C(\boldsymbol{k}) &=1 \\
\sum_{[\boldsymbol{k}]} C(\boldsymbol{k}) \chi_{i}(\boldsymbol{k}) &=0, \quad i=2, \ldots, 6
\end{aligned}
\right\} \tag{7}
$$

where $\Sigma_{[\boldsymbol{k}]}$ is a sum over the six directions. Using the functions (3) in equation (7) we can solve for the six values of $C(\boldsymbol{k})$, i.e. a constant for each direction. For the six directions chosen for this calculation the weighting factors were found to be

$$
\left.
\begin{aligned}
C([001]) &= & -0 \cdot 00153 \\
C([011]) &= & 4 \cdot 6590 \\
C([111]) &= & 5 \cdot 7837 \\
C([012]) &= & -16 \cdot 5425 \\
C([112]) &= & 24 \cdot 7412 \\
C([122]) &= & -17 \cdot 6399 .
\end{aligned}
\right\} \tag{8}
$$

Thus, using these values of $C(\boldsymbol{k})$ we can apply equation (6) to obtain the volume integral $F$ of any function with full tetragonal symmetry. $f(\boldsymbol{k})$, the line integral of the required function along a given direction, may be evaluated by any suitable numerical method. We found Simpson's rule to be satisfactory.

In applying this method to the calculation of $C_{\mathrm{M}}(T)$, the spin-wave contribution to the specific heat, we can easily show that $C_{\mathrm{M}}(T)$ is given by $F$ in equation (6) if

$$
f(\boldsymbol{k})=R^{\prime} \int_{0}^{k_{\max }} \frac{x^{2} \mathrm{e}^{x}|\boldsymbol{k}|^{2} \mathrm{~d}|\boldsymbol{k}|}{\left(\mathrm{e}^{x}-1\right)^{2}}
\tag{9}
$$

where $x=h \nu / k T$ and $R'$ is some constant.

## 3. Calculation of the specific heat of $\mathrm{NiF}_{2}$

In an earlier preliminary communication (Joshua and Cracknell 1969 a) the spin-wave contribution to the specific heat of $\mathrm{NiF}_{2}$ was calculated using the magnon dispersion relations given by Moriya (1966) together with various experimental determinations of the parameters. At that stage although $\phi$, the canting angle, and $J_{1}$, the nearest-neighbour exchange constant, were known quite accurately from experiment, there remained some uncertainty about $J_{2}$ and $J_{3}$ (Joshua and Cracknell 1969 b). This uncertainty only affected those magnons that have relatively high energies and consequently had very little effect on the specific heat curve. Subsequently some more experimental results have become available, in particular the one-magnon and two-magnon Raman-scattering experiments of Fleury (1969) and the neutron scattering experiments of Hutchings *et al.* (1969). In the light of these results it should now be possible to determine realistic values of $J_{2}$ and $J_{3}$.

Fleury (1969) observed one-magnon and two-magnon Raman scattering of light by a single crystal of $\mathrm{NiF}_{2}$ between $1 \cdot 8{ }^{\circ} \mathrm{K}$ and $300{ }^{\circ} \mathrm{K}$. The one-magnon absorption which involves the creation of a single magnon at $\boldsymbol{k}=0$ occurs at a frequency that is in agreement with the infra-red work of Richards (1965) and yields no new information. The two-magnon absorption which involves the creation of a pair of magnons (at $\boldsymbol{k}$ and $-\boldsymbol{k}$ to conserve momentum) occurs at twice the frequency of the individual zone-boundary magnon at $\boldsymbol{k}$ or $-\boldsymbol{k}$. It is possible to use the appropriate space-group selection rules to determine which of the special points on the Brillouin zone boundary are able to participate in this second-order Raman scattering. Such selection rules have been given previously for $\mathrm{MnF}_{2}$ by Fleury and Loudon (1968) and Cracknell (1969); we have applied the same theory to the space group $P n n^{\prime} m^{\prime}$ of antiferromagnetic $\mathrm{NiF}_{2}$. It is possible to show that the points $\mathrm{U}, \mathrm{R}$ and $\mathrm{M}$ can participate in the two-magnon Raman scattering whereas $\mathrm{X}, \mathrm{Y}, \mathrm{Z}$ and $\mathrm{A}$ cannot, where we use the labels of Joshua and Cracknell (1969 b) for the points of symmetry in the Brillouin zone of antiferromagnetic $\mathrm{NiF}_{2}$. The absorption observed by Fleury (1969) will therefore occur at twice the frequency of a magnon at $\mathrm{U}, \mathrm{R}$ or $\mathrm{M}$. From the appearance of the results of Fleury it would seem that these energies are all close together which suggests (see table 8 of Joshua and Cracknell 1969 b), that $J_{2} / J_{3} \sim 1$ and therefore $J_{2}=J_{3} \simeq 4 \cdot 8 \mathrm{~cm}^{-1}$. That the values of $\nu_{ \pm}(\boldsymbol{k})$ at $\mathrm{U}, \mathrm{R}$ and $\mathrm{M}$ were found by Fleury to be slightly in excess of $100 \mathrm{~cm}^{-1}$ further suggests that the above values of $J_{2}$ and $J_{3}$ are slightly too large, since they lead to $\nu_{ \pm}(\boldsymbol{k})=88 \cdot 8 \mathrm{~cm}^{-1}$.

More accurate values of $J_{2}$ and $J_{3}$ than we have estimated above may be obtained by using the results of the neutron diffraction data of Hutchings *et al.* (1969). Their final results are not yet available to us but preliminary values for the frequencies $\nu_{ \pm}(\boldsymbol{k})$ at three points of symmetry were kindly supplied to us in the summer of 1968. Using these three frequencies we have estimated values of $J_{2}$ and $J_{3}$ in Moriya's theory using

$$
\nu_{ \pm}(\boldsymbol{k})=125 \cdot 0\left[\left\{1 \cdot 01569-\frac{\left(1-\gamma_{2 k}\right) J_{2}}{62 \cdot 2}-\frac{\left(1-\gamma_{3 k}\right) J_{3}}{31 \cdot 1}\right\}^{2}-\left\{\gamma_{1 k} \pm 0 \cdot 01534\right\}^{2}\right]^{1 / 2}
\tag{10}
$$

(Joshua and Cracknell 1969 b); we find the values of $J_{2}$ and $J_{3}$ given in table 1 and our calculated values of $\nu_{ \pm}(\boldsymbol{k})$ at the points of symmetry are given in table 2. Although the final values of $J_{2}$ and $J_{3}$ produced by Hutchings *et al.* may be slightly different from those in table 1, the corresponding effect on the spin-wave specific heat of $\mathrm{NiF}_{2}$ would be very small since the main contribution comes from spin waves near $\boldsymbol{k}=0$ where $J_{2}$ and $J_{3}$ are not important.

### Table 1. Parameters used in dispersion relations

| $\text{MnF}_2$ | $\text{FeF}_2$ | $\text{CoF}_2$ | $\text{NiF}_2$ |
|----------------|----------------|----------------|----------------|
| $J_1 = 0.236\ \text{cm}^{-1}$<br>$J_2 = 1.209\ \text{cm}^{-1}$<br>$J_3 = 0.034\ \text{cm}^{-1}$<br>$g\beta H_{\text{A}} = 0.730\ \text{cm}^{-1}$<br>$S = \frac{5}{2}$ | $J_1 = 0.024\ \text{cm}^{-1}$<br>$J_2 = 1.84\ \text{cm}^{-1}$<br>$J_3 = 0.097\ \text{cm}^{-1}$<br>$g\beta H_{\text{A}} = 19.93\ \text{cm}^{-1}$<br>$S = 2$ | $P = 0.99$<br>$Q = 2.38$<br>$R = 1.42$<br>$T = 0.38$<br>$S = \frac{1}{2}$<br>$p = z_2J_2'-z_1J_1'$<br>$J_1' = -0.617\ \text{cm}^{-1}$<br>$J_2' = 3.362\ \text{cm}^{-1}$ | $J_2 = 3.952\ \text{cm}^{-1}$<br>$J_3 = 3.118\ \text{cm}^{-1}$<br>see also equations (7) and<br>(8) of Joshua and Cracknell<br>(1969 b) |

### Table 2. Magnon frequencies at points of symmetry

|  | $\text{MnF}_2$<br>($\text{cm}^{-1}$) | $\text{FeF}_2$<br>($\text{cm}^{-1}$) | $\text{CoF}_2$<br>($\text{cm}^{-1}$) | $\text{NiF}_2$<br>($\text{cm}^{-1}$) |  |
|-----|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|-----|
| $\Gamma(0,0,0)$ | $8.431$ | $52.38$ | $37.83$ | $3.3$ | $31.1$ |
| $\text{Y}(\frac{1}{2},0,0)$ | $49.80$ | $80.36$ | $58.64$ | $114.4$ | $114.4$ |
| $\text{U}(\frac{1}{2},0,\frac{1}{2})$ | $54.53$ | $80.75$ | $64.44$ | $98.5$ | $98.5$ |
| $\text{M}(\frac{1}{2},\frac{1}{2},0)$ | $50.49$ | $81.91$ | $58.64$ | $101.9$ | $101.9$ |
| $\text{X}(0,\frac{1}{2},0)$ | $49.80$ | $80.36$ | $58.64$ | $114.4$ | $114.4$ |
| $\text{Z}(0,0,\frac{1}{2})$ | $53.83$ | $79.19$ | $64.44$ | $111.1$ | $111.1$ |
| $\text{R}(0,\frac{1}{2},\frac{1}{2})$ | $54.53$ | $80.75$ | $64.44$ | $98.5$ | $98.5$ |
| $\text{A}(\frac{1}{2},\frac{1}{2},\frac{1}{2})$ | $55.22$ | $82.30$ | $64.44$ | $86.0$ | $86.0$ |

We have used the values of $J_2$ and $J_3$ given in table 1 in the expression for $\nu_{\pm}(k)$ in equation (10) to determine the spin-wave contribution to the specific heat by calculating the density of states $g(\nu)$ from $\nu_{\pm}(k)$, using 167 304 wave vectors in the Brillouin zone. The result for $g(\nu)$ was then substituted into equation (2) and the results are given in table 3 where they are compared with the experimental values of $C_{\text{M}}(T)$ obtained by Stout and Catalano (1955).

### Table 3. Comparison of the calculated spin-wave specific heats of $\text{MnF}_2$, $\text{FeF}_2$, $\text{CoF}_2$ and $\text{NiF}_2$ with the experimental results of Stout and Catalano (1955) in units of $\text{J deg K}^{-1}\text{ mole}^{-1}$

| $T$<br>($^\circ\text{K}$) | $\text{MnF}_2$ | | $\text{FeF}_2$ | | $\text{CoF}_2$ | | $\text{NiF}_2$ | |
|---------------------------|----------------|---|----------------|---|----------------|---|----------------|---|
| | calc. | expt. | calc. | expt. | calc. | expt. | calc. | expt. |
| $0.36$ | — | — | — | — | — | — | $7.4\times10^{-10}$ | — |
| $2.5$ | $2.6\times10^{-12}$ | — | $2.6\times10^{-12}$ | — | $1.2\times10^{-7}$ | — | $1.4\times10^{-4}$ | — |
| $5.0$ | $0.029$ | — | $7.4\times10^{-6}$ | — | $0.0001$ | — | $0.0013$ | — |
| $7.5$ | $0.158$ | — | $0.0014$ | — | $0.010$ | — | $0.0052$ | — |
| $10.0$ | $0.509$ | — | $0.020$ | — | $0.097$ | — | $0.017$ | — |
| $12.5$ | $1.088$ | — | $0.100$ | — | $0.350$ | — | $0.049$ | — |
| $15.0$ | $1.785$ | $2.218$ | $0.281$ | $0.314$ | $0.785$ | $0.963$ | $0.123$ | $0.184$ |
| $20.0$ | $3.158$ | $3.767$ | $0.941$ | $1.097$ | $1.96$ | $2.428$ | $0.479$ | $0.431$ |
| $25.0$ | $4.248$ | $5.274$ | $1.800$ | $2.218$ | $3.15$ | $4.311$ | $1.102$ | $0.917$ |
| $30.0$ | $5.043$ | $6.697$ | $2.650$ | $3.474$ | $4.15$ | $6.655$ | $1.808$ | $1.632$ |
| $35.0$ | $5.614$ | $7.952$ | $3.394$ | $4.939$ | $4.94$ | $10.296$ | $2.645$ | $2.553$ |
| $40.0$ | $6.029$ | $9.124$ | $4.011$ | $6.320$ | — | — | $3.320$ | $3.599$ |
| $45.0$ | $6.337$ | $10.42$ | $4.513$ | $7.869$ | — | — | $3.975$ | $4.813$ |
| $50.0$ | $6.569$ | $11.89$ | $4.919$ | $9.543$ | — | — | $4.527$ | $6.194$ |

### 4. Calculation of the spin-wave contributions to the specific heats of $\text{MnF}_2$, $\text{FeF}_2$ and $\text{CoF}_2$

As a further comparison with the experimental results of Stout and Catalano (1955) we have evaluated the magnetic properties of $\text{MnF}_2$, $\text{FeF}_2$ and, in a more limited sense, $\text{CoF}_2$.

The magnetic excitations of antiferromagnetic $\text{MnF}_2$ have been discussed in some detail by many authors. We have used the dispersion relations given by Loudon (1968) to obtain the magnon energies

$$\{\hbar\omega(\boldsymbol{k})\}^2 = \{E_0+V_1(\boldsymbol{k})\}^2-V_2(\boldsymbol{k})^2 \tag{11}$$

where

$$V_1(\boldsymbol{k})=2V_1\cos ck_z + 2V_3(\cos ak_x+\cos ak_y)$$

$$V_2(\boldsymbol{k})=8V_2\cos\frac{1}{2}ak_x\cos\frac{1}{2}ak_y\cos\frac{1}{2}ck_z$$

and $V_1\equiv -2J_1S$, $V_2\equiv +2J_2S$ and $V_3\equiv -2J_3S$. This expression was used for a direct computation of the density of magnon states for use in equation (2) in order to obtain the spin-wave contribution to the specific heat at low temperatures. The salient features of the dispersion are shown in table 2 and the specific heat in table 3. A programme for the six-line-integral interpolation formula in equation (6) to find $C_{\text{M}}(T)$ was also tested for $\text{MnF}_2$; good agreement between the two methods was obtained.

Using equation (11) for $\text{FeF}_2$ and the parameters required to fit the experimental work of Guggenheim *et al.* (1968) we present the corresponding results for $\text{FeF}_2$ in tables 2 and 3. The parameters are given in table 1.

Lines (1965) discussed the magnetic properties of $\text{CoF}_2$ which also has the rutile structure but the properties arising from $\text{Co}^{2+}$ are fundamentally different from those arising from $\text{Mn}^{2+}$. In the latter, the crystal field may be neglected and the $\text{Mn}^{2+}$ treated as a pure spin. The ground state of an isolated $\text{Co}^{2+}$ ion is a degenerate F state. The degeneracy is lifted by the interaction terms present when the ion is in a crystal and hence the energy states involve crystal field terms and spin-orbit terms as well as exchange interactions. Lines' spin-wave treatment yields an expression for the dispersion of a magnetic excitation involving the lowest two energy levels:

$$(\hbar\omega)^2 = S\{a(\xi_z)b(\xi_z)-c^2(\xi)\} \tag{12}$$

where

$$a(\xi_z)=Rp(R+T/S)+J_1'z_1P^2\cos2\pi\xi_z$$

$$b(\xi_z)=Rp(R+T/S)+J_1'z_1Q^2\cos2\pi\xi_z$$

$$c(\xi)=J_2'z_2PQ\cos\pi\xi_x\cos\pi\xi_y\cos\pi\xi_z$$

and values for the parameters are given in table 1. The effects of the next two levels were included in the molecular field determination of the levels to be included in the spin-wave analysis. Lines found this approach to be satisfactory up to $\frac{2}{5}T_{\text{N}}$. Following this method, and thus including contributions from just the lowest branch of the magnon energies for which Martel *et al.* (1968)$\dagger$ have found values of the parameters which satisfactorily reproduce neutron scattering measurements, we are able to find a density of states and hence evaluate the specific heat contribution. In fact we have used the six-line-integral interpolation formula of equation (6). The results are given in tables 2 and 3.

The numerical integration of equation (2) which we have used for calculating $C_{\text{M}}(T)$ for these difluorides has been carried out by three methods: trapezoidal rule, Simpson's rule and by curve fitting. The agreement among these methods was considerably better than the experimental error in the data employed, so we are satisfied that no additional error of any significance arises from our numerical procedure.

### 5. Conclusion

For $\text{MnF}_2$, $\text{FeF}_2$ and $\text{CoF}_2$ the calculations consistently give lower results than the experiments of Stout and Catalano, whereas in the case of $\text{NiF}_2$ the theoretical results are too high except for the lowest temperature at which experimental data are given.

$\dagger$ The formula quoted in this reference is in error and should read as in our equation (12).

It should be noticed that the spin-wave approximation is not valid at high temperatures approaching the Néel temperature; therefore, our calculations should not be used in this region. In particular this is true for $CoF_{2}$ which has a Néel temperature about half of those of the other three difluorides discussed. Also we have only considered the lowest magnon branch and if Lines' (1965) estimate of validity (below $\frac{2}{5}T_{\mathrm{N}}$) is true we would not expect any of Stout and Catalano's measurements to compare well since their lowest temperature corresponds to the upper temperature limit of the dispersion relations employed. The inclusion of the higher branches of the spin-wave dispersion relations, which we have neglected, would raise the theoretical values of $C_{\mathrm{M}}(T)$ of each of these difluorides by only a very small amount.

It should also be noted that part of the discrepancy is probably due to the fact that Stout and Catalano have obtained $C_{\mathrm{M}}(T)$ by subtracting from the total specific heat of the appropriate magnetic difluoride the total specific heat of (non-magnetic) $ZnF_{2}$, weighted suitably for the differences in mass and lattice spacing. While this is clearly a good first approximation, it is reasonable to expect that if the proper lattice specific heat, calculated from the phonon dispersion relations, had been used, the agreement between the experi- mental and theoretical spin-wave contributions to the specific heat would be improved. On the basis of mass and crystal dimensions, $CoF_{2}$ and $NiF_{2}$ bear the closest similarity to $ZnF_{2}$ and hence we might expect their vibrational properties to be more accurately described by an interpolation based on a law of corresponding states than those of $MnF_{2}$ and $FeF_{2}$. There is some evidence for this in table 3 in that $NiF_{2}$ shows better agreement than $MnF_{2}$ or $FeF_{2}$ between our calculations and the measurements of Stout and Catalano. We cannot comment on this for $CoF_{2}$ because of its low Néel temperature.

Some new experimental determinations of the spin-wave contributions to the specific heat of these four difluorides in the range $0-15$ $^{\circ}\mathrm{K}$ would provide a valuable test of our calculated specific heats below $15$ $^{\circ}\mathrm{K}$.

## References

BELL, D. G., 1954, *Rev. Mod. Phys.*, **26**, 311-20.
BETTS, D. D., BHATIA, A. B., and WYMAN, M., 1956, *Phys. Rev.*, **104**, 37-42.
CRACKNELL, A. P., 1969, *J. Phys. C (Solid St. Phys.)*, [2], **2**, 500-11.
DE BATIST, R., GEVERS, R., and VERSCHUEREN, M., 1967, *Phys. Stat. Sol.*, **19**, 77-88.
FLEURY, P. A., 1969, *Phys. Rev.*, **180**, 591-3.
FLEURY, P. A., and LOUDON, R., 1968, *Phys. Rev.*, **166**, 514-30.
GUGGENHEIM, H. J., HUTCHINGS, M. T., and RAINFORD, B. D., 1968, *J. Appl. Phys.*, **39**, 1120-1.
HORTON, G. K., and LEECH, J. W., 1963, *Proc. Phys. Soc.*, **82**, 816-54.
HORTON, G. K., and SCHIFF, H., 1959, *Proc. R. Soc. A*, **250**, 248-65.
HOUSTON, W. V., 1948, *Rev. Mod. Phys.*, **20**, 161-5.
HUTCHINGS, M. T., *et al.*, 1969, *J. Phys. C (Solid St. Phys.)* to be submitted.
JOSHUA, S. J., and CRACKNELL, A. P., 1969 a, *Phys. Lett.*, **28A**, 562-3.
—— 1969 b, *J. Phys. C (Solid St. Phys.)*, [2], **2**, 24-36.
LINES, M. E., 1965, *Phys. Rev.*, **137**, A982-93.
LOUDON, R., 1968, *Adv. Phys.*, **17**, 243-80.
MARTEL, P., COWLEY, R. A., and STEVENSON, R. W. H., 1968, *Can. J. Phys.*, **46**, 1355-70.
MORIYA, T., 1966, *J. Phys. Soc. Japan*, **21**, 926-32.
RICHARDS, P. L., 1965, *Phys. Rev.*, **138**, A1769-75.
STOUT, J. W., and CATALANO, E., 1955, *J. Chem. Phys.*, **23**, 2013-22.