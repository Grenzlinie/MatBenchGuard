
# Optical response of a nematic liquid crystal cell at splay–bend transition: model and dynamic simulation

Peizhi Xu, \( ^{1,*} \)  Vladimir Chigrinov, \( ^{1,\dagger} \)  and Alexei D. Kiselev \( ^{2,\ddagger} \) 

 \( ^{1} \) Hong Kong University of Science and Technology,

Clear Water Bay, Kowloon, Hong Kong

 \( ^{2} \) Chernigov State Technological University,

Shevchenko Street 95, 14027 Chernigov, Ukraine

(Dated: July 20, 2018)

## Abstract

We study dynamical optical response of a nematic liquid crystal (NLC) cell that undergoes the splay-bend transition after applying the voltage across the cell. We formulate a simplified model that takes into account both the flexoelectric coupling and the surface rotational viscosity. The dynamic equations of the model were solved numerically to describe temporal evolution of the director profile and the transmittance. We evaluate the response time as a function of a number of parameters characterising dielectric and elastic anisotropies, asymmetry of the surface pretilt angles, anchoring energy, surface rotational viscosity and flexoelectricity.

PACS numbers: 61.30.Gd, 78.66.Qn, 42.70.Gi

Keywords: bistability; splay-bend transition; anchoring energy; flexoelectricity; surface rotational viscosity

## I. INTRODUCTION

As it was originally shown by Berreman and Heffner in 1981  \( [1] \) , a nematic liquid crystal (NLC) cell can be prepared to have two metastable states that can be switched either way by applying an electric field. This general idea underlies the mode of operation of bistable liquid crystal devices that have been attracted considerable attention over the past few decades.

The approach pioneered in  \( [1] \)  is based on using bistable twisted NLC cells that have two metastable twist states produced as a result of a mismatch between the NLC pitch and the twist imposed by the boundary conditions at the substrates. This approach has been extensively studied and is found to have difficulties caused by fast relaxation of the metastable states to the intermediate stable configuration  \( [2, 3, 4, 5, 6] \) .
An alternative approach is to use the so-called optically compensated bend NLC cells also known as  \( \pi \)  cells [7, 8, 9, 10, 11]. Boundary surfaces of such cells both favour a uniformly tilted alignment and the pretilt angles at the substrates are equal in magnitude but opposite in sign. For sufficiently large surface pretilt angles, the equilibrium orientational structures are non-twisted [7, 8, 12, 13] and there are two director configurations that under certain conditions are degenerate in energy: the splay (horizontal) state and the bend (vertical) state.

By contrast to the bistable twisted cells, these bistable states are topologically distinct and separated by an energy barrier. So, the splay and bend states are both long-term stable. Applying the voltage across the cell it can be switched from the splay state to the bend state.

This splay-bend transition will be of our primary concern. We are aimed to study the dynamics of a NLC cell that undergoes the splay-bend transition induced by an external electric field.
 

The dynamical theory of NLC systems — the so-called nematohydrodynamics — is very complicated and dynamical properties of bistable liquid crystal cells have not received a fair amount of attention yet. In recent theoretical studies the dynamics of  \( \pi \)  cells [14], zonithally bistable [15] and super-twisted [16] NLC devices was investigated using different simplified models.

In this paper we concentrate on optical response of the NLC cell after switching on the voltage. The corresponding response time will be studied depending on a number of factors such as dielectric and elastic anisotropies, asymmetry of the surface pretilt angles, anchoring strengths, surface rotational viscosity and flexoelectricity.

The paper is organised as follows.

In Sec. II we formulate our model and derive a set of dynamic equations. The numerical results are presented in Sec. III. Concluding remarks are given in Sec. IV.

## II. MODEL

In this section we describe our model and derive a set of dynamic equations. Subsequently, these equations will be used to simulate the orientational dynamics of a NLC layer of the thickness d that undergoes the splay-bend transition under the action of an electric field.

## A. Free energy

The layer is sandwiched between two parallel plates, z = 0 (lower substrate) and z = d (upper substrate), and we assume that both the electric field, E, and the z-axis are normal to the plane of the substrates. In addition, similar to [14, 15, 17], we shall restrict our consideration to the case in which the splay-bend transition does not involve twisted states.

In this case, the NLC director field, n, is constrained to lie in the x-z plane:

 \[ \mathbf{n}=\cos\theta(z)\mathbf{e}_{x}+\sin\theta(z)\mathbf{e}{}_{z}, \quad (1) \] 

where  \( \theta \)  is the tilt angle defined as the angle between the plane of the boundary surfaces and the director;  \( e_{x} \)  and  \( e_{z} \)  are the unit vectors parallel to the x-axis and the z-axis, respectively.

The vectors of easy orientation at the lower and the upper substrates are similarly characterised by the tilt angles  \( \theta_{L} \)  and  \( -\theta_{U} \) , respectively. So, the anchoring energy per unit area taken in the Rapini-Papoular form [18] is

 \[ f_{\mathrm{a n c h}}=\frac{W_{L}}{2}\sin^{2}(\theta_{0}-\theta_{L})+\frac{W_{U}}{2}\sin^{2}(\theta_{1}+\theta_{U}), \quad (2) \] 

where  \( \theta_{0,1} = \theta\big|_{z=0,d} \)  and  \( W_{L} \)  ( \( W_{U} \) ) is the strength of anchoring at the lower (upper) substrate.

We shall also need to write the bulk part of the free energy per unit area

 \[ F_{b}[\mathbf{n},\mathbf{E}]=F_{e l}[\mathbf{n}]+F_{E}[\mathbf{n},\mathbf{E}] \quad (3) \] 

which is a sum of the Frank elastic energy,  \( F_{el}[n] \) , and the energy of interaction between NLC molecules and the electric field,  \( F_{E}[n, E] \) .

For the director distribution (1), using the standard expression for the Frank elastic energy [19] gives the following result:

 \[ F_{e l}[\theta]=\frac{1}{2}\int_{0}^{d}K_{e l}(\theta)\dot{\theta}^{2}\mathrm{d}z, \quad (4) \] 

where dot stands for the derivative with respect to z and  \( K_{el}(\theta) = K_{11} \cos^{2} \theta + K_{33} \sin^{2} \theta \)  is the effective angle-dependent elastic coefficient;  \( K_{11} \)  and  \( K_{33} \)  are the splay and the bend elastic constants. Similarly, the director field (1) can be used to derive the expression for the electrostatic energy  \( F_{E}[n, E] \)  that depends on the electric field:  \( E = E_{z} e_{z} \) .

Assuming that the NLC Debye screening length is larger than the layer thickness, the
 

NLC material can be regarded as an insulator. So, we can neglect the effects caused by the presence of ionic charges.

But, the flexoelectric coupling between NLC and the applied field cannot be generally disregarded. This coupling is known to be caused by splay and bend director distortions that give rise to an average flexoelectric polarisation

 \[ \mathbf{P}_{f}=e_{11}\mathbf{n}(\nabla\cdot\mathbf{n})+e_{33}(\mathbf{n}\cdot\nabla)\mathbf{n}, \quad (5) \] 

characterised by the splay and bend flexoelectric coefficients,  \( e_{11} \)  and  \( e_{33} \) .

This is the well-known flexoelectric effect, first described by Meyer in 1969 [20], which has been extensively studied over recent years. Flexoelectricity appears to be a very important property of NLCs which must be taken into account in all experiments that deal with inhomogeneous director orientation.

In our case, it is not difficult (4) to obtain the z-component of the flexoelectric polarisation (5) in the following form:

 \[ P_{z}=g(\theta)\dot{\theta},\quad g(\theta)=e_{f}\sin\theta\cos\theta, \quad (6) \] 

where  \( e_{f}=e_{11}+e_{33} \)  is the flexoelectric coefficient. So, the final result for the electrostatic energy is

 \[ \begin{align*}F_{E}[\theta,E_{z}]=&-\int_{0}^{d}\big[\epsilon_{zz}E_{z}^{2}/2+P_{z}E_{z}\big]\mathrm{d}z,\\ \epsilon_{zz}(\theta)=\epsilon_{\perp}(1+u\sin^{2}\theta),\end{align*} \quad (7) \] 

where  \( \epsilon_{ij} = \epsilon_{\perp}\delta_{ij} + (\epsilon_{\parallel} - \epsilon_{\perp})n_{i}n_{j} \)  is the dielectric tensor and  \( u = (\epsilon_{\parallel} - \epsilon_{\perp})/\epsilon_{\perp} \)  is the dielectric anisotropy parameter.

The Maxwell equation  \( \nabla \times E = 0 \)  implies that the electric field  \( \mathbf{E} = E_{z}(z)\mathbf{e}_{z} \)  can be expressed in terms of the scalar potential,  \( V: E_{z} = -\dot{V} \) . Variation of the electrostatic energy functional (7) with respect to V gives the well-known electrostatic constitutive relation

 \[ -\frac{\delta F_{E}}{\delta E_{z}}=\epsilon_{z z}E_{z}+P_{z}=D_{z}, \quad (9) \] 

where  \( D_{z} \)  is the z-component of the electric displacement field that, in contrast to  \( E_{z} \) , does not depend on z.

From the relation (9) the displacement  \( D_{z} \)  can be expressed in terms of the voltage  \( U = \int_{0}^{d} E_{z} \, dz = V(0) - V(d) \)  as follows

 \[ D_{z}=\frac{U+\psi(\theta_{1})-\psi(\theta_{0})}{\int_{0}^{d}\epsilon_{z z}^{-1}(\theta)\mathrm{d}z}, \quad (10) \] 

where

 \[ \begin{align*}\psi(\theta)&=\int g(\theta)\epsilon_{zz}^{-1}(\theta)\mathrm{d}\theta\\&=\frac{e_{f}\ln(1+u\sin^{2}\theta)}{2u\epsilon_{\perp}}.\end{align*} \quad (11) \] 

The expression on the right hand side of Eq. (10) clearly indicates the flexoelectricity-induced voltage shift. The effects of this shift in optical response of hybrid aligned liquid crystal cells were recently studied in [21].

Since the displacement  \( D_{z} \)  does not vary across the layer, it is convenient to have the displacement  \( D_{z} \)  as an independent field and use the free energy  \( G[\theta, D_{z}] \)  which is related to the energy  \( F[\theta, E_{z}] \)  via the Legendre transformation [22, 23]

 \[ G[\theta,D_{z}]=F[\theta,E_{z}]+E_{z}D_{z}, \quad (12) \] 

where  \( E_{z} = (D_{z} - P_{z})/\epsilon_{zz} \) 

We can now combine Eqs. (2)–(4) and Eq. (7) to derive the free energy  \( G[\theta, D_{z}] \)  in the following form:

 \[ G[\theta,D_{z}]=\int_{0}^{d}f_{b}\mathrm{d}z+f_{s}, \quad (13) \] 

 \[ f_{b}=K(\theta)\dot{\theta}^{2}+\frac{D_{z}^{2}}{\epsilon_{z z}(\theta)}, \quad (14) \] 

 \[ f_{s}=f_{\mathrm{a n c h}}+D_{z}(\psi(\theta_{0})-\psi(\theta_{1})), \quad (15) \] 

where  \( K(\theta) = K_{el}(\theta) + g^{2}(\theta)/\epsilon_{zz}(\theta) \)  is the effective elastic coefficient renormalised by the flexoelectricity.

As it can be seen from Eqs. (13)–(15), the bulk elastic coefficient and the anchoring energy are both renormalised by the flexoelectricity:  \( K_{el} \rightarrow K \)  and  \( f_{anch} \rightarrow f_{s} \) . Static
 

properties of NLC layers submitted to an electric field are known to be affected by this renormalisation [24, 25, 26, 27, 28].

## B. Dynamic equations

Low-frequency dynamical properties of NLCs are generally characterised by orientational relaxation as well as by shear and compressional flow. A full set of dynamic equations governing nematohydrodynamics is known as the Ericksen-Leslie equations and describes temporal evolution of the fluid velocity and the director field.

When the characteristic time scale of the velocity field is much shorter than the typical time of director reorientation, the flow velocity can be adiabatically eliminated from the dynamics of NLC. In this approximation, the orientational dynamics is purely relaxational and can be formulated as a time-dependent Ginzburg-Landau model  \( [29, 30] \) .

We shall apply this model to obtain the dynamic equation governing the orientational relaxation of the tilt angle in the bulk. Using the free energy (13) gives the following result

 \[ \begin{aligned}\gamma_{b}\frac{\partial\theta}{\partial t}&=-\frac{\delta G}{\delta\theta}=K(\theta)\ddot{\theta}+\frac{1}{2}\left[K^{\prime}(\theta)\dot{\theta}^{2}\right.\\&+\left.[D_{z}/\epsilon_{zz}(\theta)]^{2}\epsilon_{zz}^{\prime}(\theta)\right],\end{aligned} \quad (16) \] 

where  \( \gamma_{b} \)  is the bulk rotational viscosity and prime stands for derivatives with respect to  \( \theta \) .

It should be stressed that under certain circumstances the backflow effect caused by the coupling between the fluid flow and the director may considerably affect dynamical characteristics of NLC cells. Specifically, the so-called “optical bounce” in twisted cells manifests itself as a dip in transmission of normally incident light after the electric field is turned off  \( [31, 32, 33] \) . But in cases where the twisted states are of minor importance backflow is found to induce only quantitative changes in the dynamics  \( [14, 33] \) .
By analogy with Eq. (16) we can write the dynamic equations for the tilt angles,  \( \theta_{0} \)  and  \( \theta_{1} \) , at the lower and upper substrates as follows [15, 34, 35, 36]

 \[ \gamma_{s}\frac{\partial\theta_{i}}{\partial t}=(-1)^{i}K(\theta_{i})\dot{\theta}_{i}-\frac{\partial f_{s}}{\partial\theta_{i}},i=0,1, \quad (17) \] 

where  \( \gamma_{s} \)  is the surface rotational viscosity, which is defined as the ratio of the torque needed to change the director orientation at the surface for a certain angle and the corresponding relaxation velocity [37, 38].

<table><tr><td>K_{11} (N)</td><td>6.6\times10^{-12}</td><td>e_{11} (C/m)</td><td>-0.95\times10^{-11}</td></tr><tr><td>K_{33}/K_{11}</td><td>3.0</td><td>e_{33} (C/m)</td><td>-1.35\times10^{-11}</td></tr><tr><td>d (\mu m)</td><td>2.5</td><td>\epsilon_{\perp}</td><td>6.3</td></tr><tr><td>W (J/m^{2})</td><td>4.0\times10^{-4}</td><td>\epsilon_{\parallel}</td><td>12.6</td></tr><tr><td>\theta_{L} (deg)</td><td>46.0</td><td>U (V)</td><td>20.0</td></tr><tr><td>\theta_{U} (deg)</td><td>44.0</td><td>n_{o}</td><td>1.5</td></tr><tr><td>\gamma_{b} (N s/m^{2})</td><td>0.1</td><td>n_{e}</td><td>1.6</td></tr><tr><td>\gamma_{s} (N s/m)</td><td>3.0\times10^{-6}</td><td>\lambda (\mu m)</td><td>0.55</td></tr></table>

TABLE I: Parameters of the model employed in the calculations.

## III. SIMULATION RESULTS

In this section we present our numerical results obtained by solving the dynamic equations (16) and (17) numerically. Dependencies of the tilt angle on z at specified points in time were computed using the finite difference time domain method. The parameters used in our calculations are listed in Table I.

In order to study the dynamics of optical response of the layer, the data representing temporal evolution of the director profile, which is the tilt angle as a function of z,  \( \theta(z,t) \) , were used as an input for computing the transmittance of light through the layer placed between two crossed polarisers.

The expression for the transmittance can be derived by using the Jones matrix method [39]. When the director of LC cell
 
![](./images/867773697744700302_1.jpg)

FIG. 1: The director configuration through the cell at different points in time after applying the voltage. The anchoring strengths at the substrates are assumed to be equal,  \( W_{L} = W_{U} \equiv W \) , and the list of the parameters are given in Table I.

is at 45 degrees to the input polariser, the transmittance, T, is given by [40, 41]

 \[ T=\sin^{2}(\Delta\phi/2), \quad (18) \] 

 \[ \Delta\phi=\frac{2\pi}{\lambda}\int_{0}^{d}(n_{\mathrm{e f f}}-n_{o})\mathrm{d}z, \quad (19) \] 

 \[ \frac{1}{n_{\mathrm{eff}}^{2}}=\frac{\sin^{2}\theta}{n_{o}^{2}}+\frac{\cos^{2}\theta}{{n_{e}^{2}}}, \quad (20) \] 

where  \( \Delta\phi \)  is the phase difference between the ordinary and extraordinary ray;  \( \lambda \)  is the wavelength of the incident light and  \( n_{o} \)  ( \( n_{e} \) ) is the ordinary (extraordinary) refractive index.

Thus, we describe the dynamics of optical response by computing temporal change in the transmittance (18). An important parameter characterising the rate of change of the transmittance is the response time which is the time it takes for the transmittance to increase from 10% to 90%.
We begin with the case in which the flexoelectric effect is neglected and  \( e_{f}=0 \) . Fig. 1 shows how the director profile evolves in time after applying the voltage across the NLC cell. Asymmetric pretilt angles and symmetric surface anchoring energy are used in this calculation. As is illustrated in Fig. 1, the initial director configuration corresponds to the splay state which gradually transforms into the bend state under the action of the electric field.

Now we pass on to discussing the effects related to the dielectric and elastic anisotropies. The results for various values of the dielectric anisotropy parameter,  \( u = (\epsilon_{\parallel} - \epsilon_{\perp})/\epsilon_{\perp} \) , and the elastic ratio,  \( K_{33}/K_{11} \) , are shown in Figs. 2 and 3, respectively.

Fig. 2(b) indicates that the response time is a non-monotonic function of the dielectric anisotropy parameter and goes through a
 
![](./images/867773697744700302_2.jpg)

(a)

![](./images/867773697744700302_3.jpg)

(b)

FIG. 2: (a) Transmittance as a function of time at various values of the dielectric anisotropy parameter,  \(  u = (\epsilon_{\parallel} - \epsilon_{\perp}) / \epsilon_{\perp}  \) . (b) Response time as a function of u.

minimum in the vicinity of u = 0.8. By contrast, as is shown in Fig. 3(b), the response time monotonically declines as the ratio of  \( K_{33} \)  and  \( K_{11} \)  increases. So, large values of the elastic ratio facilitate the splay-bend transition.

The surface pretilt angles,  \( \theta_{L} \)  and  \( \theta_{U} \) , are known to play an important part in the splay-bend transition [8]. These are among the parameters that affect the dynamics of optical response through the boundary conditions at the substrates (17).

The first parameter we consider is the difference between the pretilt angles:  \( \Delta\theta_{s} = \theta_{L} - \theta_{U} \) . Fig. 4(a) shows the curves for the transmittance varying in time at various values of the pretilt angle difference. As is evident from Fig. 4(a), the curves are getting steeper as  \( \Delta\theta_{s} \)  increases and the response time, shown in Fig. 4(b), is a decreasing function of  \( \Delta\theta_{s} \) .

The anchoring energy dependence of the
 
![](./images/867773697744700302_4.jpg)

(a)

![](./images/867773697744700302_5.jpg)

(b)

FIG. 3: (a) Transmittance as a function of time at various values of the elastic ratio  \( K_{33}/K_{11} \) ,  \( \left(=\left(\theta_{L}-\theta_{U}\right)\right) \) . (b) Response time as a function of the elastic ratio  \( K_{33}/K_{11} \) .

response time is plotted in Fig. 5 for the symmetric case with  \( W_{L} = W_{U} \equiv W \) . The curve is depicted in logarithmic scale and clearly indicates the transition between two regimes of anchoring: the weak anchoring regime and the strong anchoring regime. In the regime of weak anchoring, the extrapolation length is larger than the cell thickness, d, and the response time is small. As is seen from Fig. 5, the response time increases with the anchoring energy and saturates on reaching the strong anchoring regime where the extrapolation length is much smaller than d.

Influence of asymmetry in the anchoring energy strengths on the response time is illustrated in Fig. 6 where the anchoring strength at the upper substrate is kept constant at the value listed in Table I,  \( W_{U} = W \) . It is shown that the response time varies slowly and reaches its maximum at  \( W_{L}/W_{U} \approx 4.0 \) .

The surface rotational viscosity,  \( \gamma_{s} \) , can be conveniently characterised by the ratio of  \( \gamma_{s} \)  and the bulk viscosity which has the dimension of length. There are, however, only few
 
![](./images/867773697744700302_6.jpg)

(a)

![](./images/867773697744700302_7.jpg)

(b)

FIG. 4: (a) Transmittance as a function of time at various values of  \( \Delta\theta_{s}, (=\theta_{L}-\theta_{U}) \) . (b) Response time as a function of  \( \Delta\theta_{s} \) .

measurements of this length that, according to [34, 35, 42], can be of the order tens and hundreds nanometers. Our numerical results on the surface viscosity dependence of the response time are presented in Fig. 7. It is seen that variations of the surface viscosity over a wide range of values have almost no effect on the response time.

So far we have limited our discussion to the case in which the flexoelectric coefficient  \( e_{f} \)  vanishes and thus the flexoelectric effect appears to be eliminated from the consideration. There are some measurements of the flexoelectric coefficient in a variety of liquid crystals [43, 44, 45, 46, 47, 48]. It was found that the value of  \( |e_{f}| \)  typically falls in the range between  \( 5 \times 10^{-12} \)  C/m and  \( 9 \times 10^{-11} \)  C/m. But reliable and accurate experimental estimates of  \( e_{f} \)  are still missing. For example, the reported values of  \( e_{f} \)  for MBBA turned out to differ in both magnitude and sign depending on theoretical approach used for pro-
 
![](./images/867773697744700302_8.jpg)

FIG. 5: Response time as a function of the anchoring strength,  \( W = W_{L} = W_{U} \) 

cessing experimental data [21, 26, 43, 45].

Numerical results related to the effect of flexoelectricity on the dynamics of NLC cell are presented in Figs. 8–10. The curves shown in Fig. 8 indicate that the dielectric anisotropy dependence of the response time turns out to be strongly affected by the flexoelectric effect. In the presence of flexoelectricity the curve has a pronounced maximum peaked at  \( u \approx 0.5 \)  which follows a minimum reached at  \( u \approx 0.35 \) .

By contrast to the dielectric anisotropy dependence, the dependencies of the response time on the pretilt angle difference,  \( \Delta\theta_{s} \) , depicted in Fig. 9, do not differ significantly. For  \( \Delta\theta_{s} \)  larger than 10 deg, referring to Fig. 9, the curve with non-zero flexoelectric coefficient is approximately shifted upward by 5 ms with respect to the curve computed at vanishing  \( e_{f} \) .

Finally, we comment on the dependencies displayed in Fig. 10. The curves plotted in Fig. 10(a) represent temporal evolution of the transmittance at different values of the flexoelectric coefficient. The response time in relation to the flexoelectric coefficient obtained from these curves is shown in Fig. 10(b). It can be seen that the response time steeply declines after reaching a maximum at  \( e_{f} \approx -1.15 \times 10^{-11} C/m \) .

## IV. CONCLUSION

In this paper we used a simplified approach to study the dynamics of optical response at the splay-bend transition that occurs after applying the voltage across the NLC cell. It is assumed that the coupling between the director and the flow velocity can be eliminated from consideration.

Similar approach was recently applied to formulate the model of switching in
 
![](./images/867773697744700302_9.jpg)

FIG. 6: Response time as a function of the anchoring strength ratio,  \( W_{L}/W_{U} \) , at  \( W_{U} = W = 4.0 \times 10^{-4} J/m^{2} \) .

a zonitally bistable device [15]. In our case, however, not only the boundary conditions (17) are different, but also inhomogeneity of the electric field is taken into account using the constitutive relation (9).

The simulation results for the transmittance were obtained by solving the dynamic equations of the model numerically. The response time characterising the rate of change of the transmittance was evaluated to study how the parameters of the cell influence the dynamics of optical response.

Dependencies of the response time on the dielectric anisotropy parameter and on the flexoelectric coefficient are found to be strongly non-monotonic. It was shown that the response time declines as the elastic ratio  \( K_{33}/K_{11} \)  or the pretilt angle difference  \( \Delta\theta_{s} \)  increases. From the other hand, the response time appears to be relatively insensitive to anchoring strength asymmetry and to changes in the surface viscosity.

## Acknowledgments

This research was partially supported by RGC Grants HKUST6004/01E and HKUST6102/03E.

[1] D. W. Berreman and W. R. Heffner, J. Appl. Phys. 52, 3032 (1981).

[2] Z. L. Xie and H. S. Kwok, J. Appl. Phys.

84, 77 (1998).

[3] Z. Zhuang, Y. J. Kim, and J. S. Patel, Appl. Phys. Lett. 75, 3008 (1999).
 
![](./images/867773697744700302_10.jpg)

FIG. 7: Response time as a function of the rotational surface viscosity.

[4] Z. L. Xie, Y. M. Dong, S. Y. Xu, H. J. Gao, and H. S. Kwok, J. Appl. Phys. 87, 2673 (2000).

[5] Z. L. Xie, C. Y. Zheng, S. Y. Xu, H. J. Gao, and H. S. Kwok, J. Appl. Phys. 88, 1722 (2000).

[6] J. X. Guo, Z. G. Meng, M. Wong, and H. S. Kwok, Appl. Phys. Lett. 77, 3716 (2000).

[7] J. Cheng, R. N. Thurston, and D. W. Berreman, J. Appl. Phys. 52, 2756 (1981).

[8] E. J. Acosta, M. J. Towler, and H. G. Walton, Liq. Cryst. 27, 977 (2000).

[9] H. Nakamura and M. Noguchi, Jpn. J. Appl. Phys. 39, 6368 (2000).

[10] S. H. Lee, T. J. Kim, G. D. Lee, T. H. Yoon, and J. C. Kim, Jpn. J. Appl. Phys. 42, L1148 (2003).

[11] I. Inoue, T. Miyashita, T. Uchida, Y. Yamada, and Y. Ishii, Journal of the SID 11/3, 571 (2003).

[12] G. Porte and J. P. Jadot, J. Phys. (Paris) 39, 213 (1978).

[13] L. Komitov, G. Hauck, and H. D. Koswig, Phys. Stat. Sol. 97, 645 (1986).

[14] H. Cheng and H. Gao, Liq. Cryst. 28, 1337 (2001).

[15] A. J. Davidson and N. J. Mottram, Phys. Rev. E 65, 051710 (2002).

[16] H. Cheng and H. Gao, Liq. Cryst. 30, 839 (2003).

[17] V. I. Tsoy, Techn. Phys. 47, 34 (2002).

[18] A. Rapini and M. Papoular, J. Phys. (Paris) Colloq. C4 30, 54 (1969).

[19] P. G. de Gennes and J. Prost, The Physics of Liquid Crystals (Clarendon Press, Oxford, 1993).

[20] R. B. Meyer, Phys. Rev. Lett. 22, 918 (1969).

[21] N. T. Kirkman, T. Stirner, and W. E. Hagston, Liq. Cryst. 30, 1115 (2003).
 
![](./images/867773697744700302_11.jpg)

(a)

![](./images/867773697744700302_12.jpg)

(b)

FIG. 8: (a) Transmittance as a function of time for various values of the dielectric anisotropy parameter at non-vanishing flexoelectric coefficient  \( e_{f} \) . (b) Response time as a function of u at  \( e_{f} = 0.0 \, C/m \)  (squares) and  \( e_{f} = -2.3 \times 10^{-12} \, C/m \)  (circles).

[22] R. N. Thurston and D. W. Berreman, J. Appl. Phys. 52, 508 (1981).

[23] J. F. Palierne, Phys. Rev. Lett. 56, 1160 (1986).

[24] G. Barbero and G. Durand, Phys. Rev. A 35, 1294 (1987).

[25] G. Barbero and G. Durand, J. Appl. Phys. 68, 5549 (1990).

[26] S. Ponti, P. Ziherl, C. Ferrero, and S. Žumer, Liq. Cryst. 26, 1171 (1999).

[27] C. V. Brown and N. J. Mottram, Phys. Rev. E 68, 031702 (2003).

[28] M. Felczak and G. Derfel, Liq. Cryst. 30, 739 (2003).

[29] P. C. Hohenberg and B. I. Halperin, Rev. Mod. Phys 49, 435 (1977).

[30] P. M. Chaikin and T. C. Lubensky, Principles of Condensed Matter Physics (Cambridge University Press, Cambridge, 1995).

[31] P. Pieransky, F. Brochard, and E. Guyon,
 
![](./images/867773697744700302_13.jpg)

FIG. 9: Response time as a function of the pretilt angle difference at  \( e_{f}=0.0\ C/m \)  (squares) and  \( e_{f}=-2.3\times10^{-12}\ C/m \)  (circles).

J. Phys. (Paris) 34, 35 (1973).

[32] D. W. Berreman, J. Appl. Phys. 46, 3746 (1975).

[33] S. M. Chen and T. C. Hsieh, Phys. Rev. A 43, 2848 (1991).

[34] A. Merteli and M. Čopič, Phys. Rev. E 61, 1622 (2000).

[35] M. Vilfan, I. D. Olenik, A. Mertelj, and M. Čopič, Phys. Rev. E 63, 061709 (2001).

[36] P. Ziherl and S. Žumer, Phys. Rev. E 54, 1592 (1996).

[37] A. M. Sonnet, E. G. Virga, and G. Durand, Phys. Rev. E 62, 3694 (2000).

[38] G. Durand and E. G. Virga, Phys. Rev. E 59, 4137 (1999).

[39] C. R. Jones, J. Opt. Soc. Am. 32, 486 (1942).

[40] L. M. Blinov and V. G. Chigrinov, Electrooptic effects in liquid crystal materials (Springer-Verlag, Berlin, 1994).

[41] H. S. Kwok, J. Appl. Phys. 80, 3687 (1996).

[42] A. G. Petrov, A. T. Ionescu, C. Versace, and M. Scaramuzza, Liq. Cryst. 19, 169 (1995).

[43] N. V. Madhusudana and G. Durand, J. Phys. (Paris) Lett. 46, L195 (1985).

[44] S. R. Warrier and N. V. Madhusudana, J. Phys. II 7, 1789 (1997).

[45] T. Takahashi, S. Hashidate, H. Nishijou, M. Usui, M. Kimura, and T. Akahane, Jpn. J. Appl. Phys. 37, 1865 (1998).

[46] L. M. Blinov, M. I. Barnik, H. Ohoka, M. Ozaki, and K. Yoshino, Phys. Rev. E 64, 031707 (2001).

[47] A. Mazzulla, F. Ciuchi, and J. R. Sambles, Phys. Rev. E 64, 021708 (2001).

[48] S. A. Jewel and J. R. Sambles, J. Appl. Phys. 92, 19 (2002).
 
![](./images/867773697744700302_14.jpg)

(a)

![](./images/867773697744700302_15.jpg)

(b)

FIG. 10: (a) Transmittance as a function of time at various values of the flexoelectric coefficient  \( e_{f} \) . (b) Response time as a function of the flexoelectric coefficient.
 
