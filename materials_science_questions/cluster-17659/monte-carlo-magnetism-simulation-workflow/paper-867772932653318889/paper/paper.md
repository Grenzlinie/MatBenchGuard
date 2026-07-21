
# Comprehensive study of the critical behavior in the diluted antiferromagnet in a field

L. A. Fernandez, V. Martin-Mayor, and D. Yllanes

Departamento de Física Teórica I, Universidad Complutense, 28040 Madrid, Spain. and Instituto de Biocomputación y Física de Sistemas Complejos (BIFI), 50018 Zaragoza, Spain.

We study the critical behavior of the Diluted Antiferromagnet in a Field with the Tethered Monte Carlo formalism. We compute the critical exponents (including the elusive hyperscaling violations exponent  \( \theta \) ). Our results provide a comprehensive description of the phase transition and clarify the inconsistencies between previous experimental and theoretical work. To do so, our method addresses the usual problems of numerical work (large tunneling barriers and self-averaging violations).

PACS numbers: 75.50.Lk, 75.50.Mg, 75.10.Nr, 05.10.Ln

Understanding collective behavior in the presence of quenched disorder has long been one of the most challenging and interesting problems in statistical mechanics. One of its simplest representatives is the random field Ising model (RFIM), which has been extensively studied both theoretically and experimentally. \( ^{1} \)  The RFIM is physically realized by a diluted antiferromagnet in an applied magnetic field (DAFF).

It is known that the D = 3 DAFF/RFIM undergoes a phase transition, but the details remain controversial, with severe inconsistencies between analytical, experimental and numerical work. A scaling theory is generally accepted, where the dimension D of the system is replaced by  \( D - \theta \)  in the hyperscaling relation. This third independent critical exponent, believed to be  \( \theta \approx 1.5 \) , is inaccessible both to a direct experimental measurement and to traditional Monte Carlo methods.

The values of the remaining critical exponents, seemingly more straightforward, are also controversial. On the experimental front, different ansätze for the scattering line shape yield mutually incompatible estimates of the thermal critical exponent, namely  \( \nu = 0.87(7) \)  (Ref. 2), or  \( \nu = 1.20(5) \)  (Ref. 3). Furthermore, the experimental estimate of the anomalous dimension,  \( \eta = 0.16(6) \)  (Ref. 2), violates hyperscaling bounds, if one is to believe the experimental claims of a diverging specific heat  \( (\alpha \geq 0) \) . \( ^{4} \) 

On the other hand, the numerical determination of  \( \nu \)  has steadily shifted, the most precise estimate being 1.37(9) (Ref. 5), inconsistent with the experimental values and barely compatible with  \( \alpha\approx0 \) . The value of  \( \alpha \)  itself is very hard to measure in a numerical simulation. \( ^{6} \) 

More fundamentally, the smallness of the magnetic exponent  \( \beta \) , combined with the numerical observation of metastability, \( ^{7} \)  has led some authors to suggest that the transition in the DAFF may be of first order.

Ultimately, the physical reasons for this confusion be\-tray the fact that the traditional tools of statistical me\-chanics are ill-suited to systems with rugged free-energy landscapes. Both experimentally and numerically, the system gets trapped in local minima, with escape times that grow as  \( \log \tau \sim \xi^{\theta} \)  ( \( \xi \)  is the correlation length). This not only makes it exceedingly hard to thermalize the sys\-tem, but also generates a rare-events statistics, causing
self-averaging violations. \( ^{8} \) 
In this letter we study the DAFF with the Tethered Monte Carlo (TMC) formalism. \( ^{9} \)  Our approach restores self-averaging and is able to negotiate the free-energy barriers of the DAFF to equilibrate large systems safely. It also provides direct access to the key parameter  \( \theta \) . We thus obtain a comprehensive picture of the phase transition, consistent both with analytical results for the RFIM and with experiments on the DAFF, and shed light on the reasons behind the previous discrepancies.

In the following we provide a brief outline of the tethered formalism applied to the DAFF (see Refs. 9 and 10 for details). We note, however, that we give most of our physical results translated into the familiar canonical language. In a tethered computation, we run simulations where one (or more) order parameters of the system are (almost) constrained. In this way, we eliminate the need for exponentially slow tunneling caused by the free-energy barriers associated to these parameters. From these tethered simulations the Helmholtz effective potential is accurately reconstructed with a fluctuation-dissipation formalism.

We consider a system with  \( N = L^{D} \)  spins,  \( s_{x} = \pm 1 \) , on the nodes of a cubic lattice with periodic boundary conditions and interacting through the Hamiltonian

 \[ H=\sum_{\langle\boldsymbol{x},\boldsymbol{y}\rangle}\epsilon_{\boldsymbol{x}}s_{\boldsymbol{x}}\epsilon_{\boldsymbol{y}}s_{\boldsymbol{y}}-h M-h_{\mathrm{s}}M_{\mathrm{s}}=U-h M-h_{\mathrm{s}M_{\mathrm{s}}}. \quad (1) \] 

Here h and  \( h_{s} \)  are the applied fields, coupled to the magnetization and staggered magnetization,

 \[ M=N m=\sum_{\boldsymbol{x}}\epsilon_{\boldsymbol{x}}s_{\boldsymbol{x}},\quad M_{\mathrm{s}}=\sum_{\boldsymbol{x}}\epsilon_{\boldsymbol{x}}s_{\boldsymbol{x}}\mathrm{e}^{\mathrm{i}\pi\sum_{\mu=1}^{D}x_{\mu}}. \quad (2) \] 

We are ultimately interested in  \( h_{s}=0 \) , but we will find this parameter useful. The quenched occupation variables  \( \epsilon_{x} \)  are 1 with probability p=0.7 and zero otherwise (this value is chosen to be far both from the percolation threshold and from the pure system). For D=3, the system undergoes a paramagnetic-antiferromagnetic phase transition, where  \( m_{s} \)  is the order parameter.

Let us consider a single sample of the system (i.e., a fixed  \( \{\epsilon_{x}\} \) ). In our tethered computation, we define smooth magnetizations  \( \hat{m} \)  and  \( \hat{m}_{s} \)  by coupling m and  \( m_{s} \) .
 

to Gaussian baths and work in a statistical ensemble for fixed  \( (\hat{m},\hat{m}_{\mathrm{s}}) \)  with weight \( ^{9} \) 

 \[ \omega(\hat{m},\hat{m}_{\mathrm{s}};\{s_{\mathbf{x}}\})\propto\mathrm{e}^{-\beta U}\gamma(\hat{m},m)\gamma(\hat{m}_{\mathrm{s}},m_{\mathrm{s}}), \quad (3) \] 

where  \( \gamma(\hat{x},x)=\mathrm{e}^{N(x-\hat{x})}(\hat{x}-x)^{(N-2)/2}\Theta(\hat{x}-x) \) , and  \( \Theta(\hat{x}-{x}) \)  is the step function. The smoothing procedure shifts the mean value of the parameters, so  \( \hat{x}\simeq x+1/2 \) . This ensemble is related to the canonical one through a Legendre transformation. For instance, the partition function of the system is

 \[ \begin{align*}Z&=\int\mathrm{d}\hat{m}\mathrm{d}\hat{m}_{\mathrm{s}}\sum_{\{s_{\mathbf{x}}\}}\omega(\hat{m},\hat{m}_{\mathrm{s}};\{s_{\mathbf{x}}\})\mathrm{e}^{\beta N(h\hat{m}+h_{\mathrm{s}}\hat{m}_{\mathrm{s}})}\\&=\int\mathrm{d}\hat{m}\mathrm{d}\hat{m}_{\mathrm{s}}\mathrm{e}^{-N[\Omega_{N}(\hat{m},\hat{m}_{\mathrm{s}})-\beta h\hat{m}-\beta h_{\mathrm{s}}\hat{m}_{\mathrm{s}}]},\end{align*} \quad (4) \] 

where  \( \Omega_{N}(\hat{m},\hat{m}_{\mathrm{s}}) \)  is the Helmholtz effective potential.

We can reconstruct  \( \Omega_{N} \)  from computations at fixed  \( (\hat{m},\hat{m}_{\mathrm{s}}) \)  via the so-called tethered field  \( (\hat{b},\hat{b}_{\mathrm{s}}) \) 

 \[ \hat{b}=1-\frac{1/2-1/N}{\hat{m}-m},\qquad\hat{b}_{\mathrm{s}}=1-\frac{1/2-1/N}{\hat{m}_{\mathrm{s}}-m_{\mathrm{s}}}. \quad (5) \] 

In particular, the gradient  \( \nabla\Omega_{N} \)  is

 \[ \left(\partial\Omega_{N}/\partial\hat{m},\partial\Omega_{N}/\hat{m}_{\mathrm{s}}\right)=\left(\langle\hat{b}\rangle_{\hat{m},\hat{m}_{\mathrm{s}}},\langle\hat{b}_{\mathrm{s}}\rangle_{\hat{m},\hat{m}_{\mathrm{s}}}\right). \quad (6) \] 

The notation  \( \langle\cdots\rangle_{\hat{m},\hat{m}_{\mathrm{s}}} \)  denotes tethered expectation values, computed with weight (3).

A TMC computation consists in a set of independent Monte Carlo simulations at fixed  \( (\hat{m},\hat{m}_{\mathrm{s}}) \)  that are then combined to reconstruct  \( \Omega_{N} \) . Note that the effective potential (as a function of the magnetizations) has all the information about the system in the tethered ensemble, just as the free energy (as a function of the applied fields) has all the information in the canonical ensemble.

The canonical averages at fixed  \( (h, h_{\mathrm{s}}) \)  can be recovered with Eq. (4). Note that, according to (6), this integral is dominated by saddle points  \( (\hat{m}, \hat{m}_{\mathrm{s}}) \)  such that

 \[ \langle\hat{b}\rangle_{\hat{m},\hat{m}_{\mathrm{s}}}=\beta h,\quad\langle\hat{b}_{\mathrm{s}}\rangle_{\hat{m},\hat{m}_{\mathrm{s}}}=\beta h_{\mathrm{s}}. \quad (7) \] 

We can determine the relative weights of different saddle points by line-integrating the tethered field along any connecting path. We are interested in the case  \( h_{s}=0 \) .

So far we have summarized the application of TMC for a single sample. Since it consists of simulations at fixed  \( (\hat{m},\hat{m}_{\mathrm{s}}) \) , it eliminates the need to tunnel between coexisting phases and, hence, equilibrates the system much faster than a canonical simulation. However, we still face the serious problem of self-averaging violations. In principle, the definition of quenched disorder implies reconstructing the free energy with (4) before computing the disorder average. In this work, however, we sample average the Helmholtz potential rather than the free energy (a similar approach was taken in Ref. 11).

In order to motivate this approach, let us consider Figure 1—Top. We compare the tethered average  \( \langle\hat{b}_{s}\rangle_{\hat{m},\hat{m}_{s}} \) 

![](./images/867772932653318889_1.jpg)

FIG. 1. (color online) Top: Tethered field  \( \langle\hat{b}_{s}\rangle_{\hat{m},\hat{m}_{s}} \) , Eq. (5), at T = 1.6 and  \( \hat{m} = 0.11 \) , for two individual samples of an L = 24 system ( \( \square \)  and  \( \blacksquare \) ) and for the sample average ( \( \bullet \) ) as a function of  \( \hat{m}_{s} \) . The field is self-averaging in the region outside the two external zeros. The errors cannot be seen at this scale. Bottom: Effective potential  \( \widehat{\Omega}_{N}(\hat{m} = 0.11, \hat{m}_{s}) \)  obtained by integrating the averaged tethered field of the top panel. The two antiferromagnetic minima are separated by a very large barrier (the escape time is  \( \tau \sim \exp[N\Delta\widehat{\Omega}] \) ), and there is no paramagnetic minimum.

for two individual samples with the disorder average over 1000 samples. The zeros of this latter curve separate an internal gap with chaotic fluctuations, where the field vanishes in the thermodynamical limit, from an external region where the field is actually self-averaging.

We exploit the situation by considering a small, but finite, value of  \( h_{s} \) . The saddle point defined by this field will be in the self-averaging region. We can therefore solve the saddle-point equations (7) on average, rather than sample by sample. Only afterwards do we make  \( h_{s} \rightarrow 0 \)  in the solution (this is analogous to the mathematical definition of spontaneous symmetry breaking). The limit  \( h_{s} = 0^{+} \)  is essentially equivalent to considering a 'smeared' saddle point and averaging over all  \( \hat{m}_{s} \) .

 \[ \overline{\langle O\rangle}_{\hat{m}}=\int\mathrm{d}\hat{m}_{\mathrm{s}}\overline{\langle O\rangle}_{\hat{m},\hat{m}_{\mathrm{s}}}\mathrm{e}^{-N[\widehat{\Omega}_{N}(\hat{m},\hat{m}_{\mathrm{s}})-\Omega_{0}]}. \quad (8) \] 

 \( \Omega_{0} \)  is a normalization constant. Since we work at fixed  \( \hat{m} \) ,  \( \widehat{\Omega}_{N} \)  is just the one-dimensional integral of  \( \langle\hat{b}_{s}\rangle_{\hat{m},\hat{m}_{s}} \) .

The other saddle-point equation,  \( \langle\hat{b}\rangle_{\hat{m}}=\beta h \) , defines a one-to-one relation  \( \hat{m}(h) \)  so that  \( \langle\widehat{O}\rangle_{\hat{m}(h)} \)  and the canonical  \( \overline{\langle O\rangle}(h) \)  both tend to the same thermodynamical limit (ensemble equivalence). Furthermore, for finite lattices  \( \langle\widehat{O}\rangle_{\hat{m}} \)  is better behaved statistically and arguably more faithful to the physics of an experimental sample. Therefore, we shall identify  \( \overline{\langle O\rangle}(h)=\overline{\langle O\rangle}_{\hat{m}(h)} \)  and use the more familiar canonical notation. See Refs. 9 and 10 for a more detailed study of this ensemble equivalence.

We have used the above outlined procedure to thermalize the DAFF for temperatures down to \(T=1.6\) and
 
![](./images/867772932653318889_2.jpg)

![](./images/867772932653318889_3.jpg)

FIG. 2. (color online) Top: Correlation length  \( \xi/L \)  as a function of the applied magnetic field h for T = 1.6. The curves intersect, marking a second-order phase transition. Bottom: Scaling plot of  \( \xi \)  as a function of T for h = -2.13, showing large corrections to leading scaling (we use  \( \nu = 1.05 \) ).

sizes up to L = 32 (1000 samples for L = 8, 12, 16, 24 and 700 samples for L = 32). For each size we simulate a grid of  \( \approx 150 \)  points in the  \( (\hat{m}, \hat{m}_{\mathrm{s}}) \)  plane (5 values of  \( \hat{m} \) , and  \( \approx 30 \)  values of  \( \hat{m}_{s} \)  on each). We also use temperature parallel tempering. This is only necessary to thermalize  \( L \geq 24 \) , but it is convenient for smaller lattices because we are also interested in the T dependence. Thermalization is ensured using the methods described in Ref. 12. We provide more technical details in Ref. 10.

The first interesting physical result is the effective potential itself. Some authors have found metastable behavior in the DAFF, interpreted as a sign of a first-order transition. \( ^{7} \)  This should manifest as the coexistence of antiferromagnetic and paramagnetic minima in  \( \Omega \) . However, see Figure 1—Bottom, our results exhibit only two antiferromagnetic minima, separated by a very large free-energy barrier. In a canonical simulation, the system tunnels back and forth between the two, with an escape time  \( \tau \sim \exp[N\Delta\Omega] \) . This explains the metastable behavior observed in previous work (and the difficulty to thermalize large samples with canonical methods), but is inconsistent with a first-order scenario.

Of course, we could be looking at a value of  \( \hat{m} \)  (equivalently, of h) far from the critical point. In order to find the phase transition, we compute the usual second-moment correlation length  \( \xi \) . \( ^{13} \)  We use the propagator  \( F_{h}(\boldsymbol{k}) = N\langle\phi(\boldsymbol{k})\phi(-\boldsymbol{k})\rangle(h) \) , where  \( \phi \)  is the staggered Fourier transform of the spin field.

We have plotted  \( \xi(h)/L \)  at T = 1.6 as a function of the applied field h in Figure 2—Top. The curves for different L show very clear intersections, marking the onset of a second-order phase transition. In order to estimate the critical exponents, we apply the quotients method. \( ^{13} \)  We consider the ratios of physical observables for system

<table><tr><td>L</td><td>\( h^{*}(L) \)</td><td>\( \beta/\nu_{h} \)</td><td>\( \nu_{h} \)</td><td>&lt;fcel&gt;</td><td>\( \nu_{T} \)</td></tr><tr><td>8</td><td>-2.178(4)</td><td>0.0125(7)</td><td>0.887(5)</td><td>0.0765(25)</td><td>1.07(9)</td></tr><tr><td>12</td><td>-2.140(5)</td><td>0.0104(5)</td><td>7.090(9)</td><td>0.0781(27)</td><td>1.01(4)</td></tr><tr><td>16</td><td>-2.123(3)</td><td>0.0119(4)</td><td>0.742(7)</td><td>0.224(4)</td><td>1.10(15)</td></tr></table>

TABLE I. Computation of the critical exponents using the quotients method. We extract our estimates from ratios of physical observables for sizes  \( (L, 2L) \) , computed at the intersection point of  \( \xi/L \) . The first four columns give results for fixed T = 1.6 and the last one at fixed h = -2.13.

<table><tr><td>L</td><td>\( \Delta F/N \)</td><td>Fit range</td><td>\( \theta \)</td><td>\( \chi^{2}/\mathrm{d.o.f.} \)</td></tr><tr><td>8</td><td>0.03382(29)</td><td>\( L \geq 8 \)</td><td>1.448(9)</td><td>5.56/3</td></tr><tr><td>12</td><td>0.01756(15)</td><td>\( L \geq 12 \)</td><td>1.469(13)</td><td>0.44/2</td></tr><tr><td>16</td><td>0.01138(9)</td><td>\( L \geq 16 \)</td><td>1.461(20)</td><td>0.16/1</td></tr><tr><td>24</td><td>0.00608(5)</td><td></td><td></td><td></td></tr><tr><td>32</td><td>0.00392(5)</td><td></td><td></td><td></td></tr></table>

TABLE II. Computation of the hyperscaling violations exponent  \( \theta \)  from the free-energy barriers  \( \Delta F \) . We report fits to  \( \Delta F = AL^{\theta} \) , for different ranges, giving the  \( \chi^{2} \)  and the degrees of freedom of each fit. Our preferred final estimate is  \( \theta = 1.469(20) \) , taking the central value of the fit for  \( L \geq 12 \)  and the more conservative error of the fit for  \( L \geq 16 \) .

sizes  \( (L,2L) \) , computed at the intersection point  \( h^{*}(L) \)  of their respective  \( \xi(h)/L \) . We have applied this method to  \( \partial_{h}\xi\sim L^{1+1/\nu_{h}} \)  and  \( \overline{\langle m_{s}^{2}\rangle}(h)\sim L^{2\beta/\nu_{h}-3} \)  in Table I. Note that our estimate for  \( \beta \)  is very low, in accordance with previous numerical and experimental work.

We can also estimate  \( \nu \)  from the temperature dependence of  \( \xi \)  at fixed h, obtaining a second estimate  \( \nu_{T} \)  (Table I). Both determinations of  \( \nu \)  should coincide, but we obtain  \( \nu_{h} \approx 0.75 \)  and  \( \nu_{T} \approx 1.05 \) . We can see in Figure 2—Bottom that this discrepancy is due to strong scaling corrections. If one attempts a collapse of the curves, focusing on different ranges for  \( \xi/L \) , the corresponding values of  \( \nu \)  vary from  \( \nu \approx 0.75 \)  to  \( \nu > 2 \) , which explains the wide range of variation in previous numerical estimates of  \( \nu \) . By safely locating the critical point and using the quotients method, we have minimized the scaling corrections, but not eliminated them completely.

We need an additional critical exponent in order fully to characterize the critical behavior of the DAFF. This is the hyperscaling violations exponent  \( \theta \) , which can be related to the free-energy barrier between the ordered and the disordered phase:  \( \Delta F \propto L^{\theta} \) . \( ^{14} \)  The computation of these barriers is very difficult with traditional methods, but straightforward with TMC. Indeed, we can identify  \( \Delta F \)  with the  \( \Delta \Omega_{N} \)  between the two saddle points (disordered and antiferromagnetic) defined by the critical  \( h_{c} \) .

We can compute this barrier simply by evaluating the line integral of  \( \left(\langle\hat{b}\rangle_{\hat{m},\hat{m}_{\mathrm{s}}}-\beta h_{\mathrm{c}},\langle\hat{b}_{\mathrm{s}}\rangle_{\hat{m},\hat{m}_{\mathrm{s}}}\right) \)  along a path joining the two saddle points. We know that one of them will lie on the line  \( \hat{m}_{s}=0.5 \)  ( \( m_{s}\approx0 \) ). Therefore, we first integrate from the antiferromagnetic saddle point to
 

 \( \hat{m}_{s}=0.5 \)  at fixed  \( \hat{m} \) . We then integrate at fixed  \( \tilde{m}_{s}=0.5 \)  until we reach the disordered saddle point. We give the resulting values of  \( \Delta\varOmega_{N}=\Delta F/N \)  in Table II. Our final estimate is  \( \theta=1.469(20) \) , incompatible with the  \( \theta=D-1 \)  of a first-order phase transition.

Notice that the hyperscaling relation  \( 2-\alpha=\nu(D-\theta) \) , coupled with our values for  \( \nu \)  and  \( \theta \) , predicts not only a divergence of the specific heat, as observed in experiments, but also a positive  \( \alpha \) . We could test this result directly by computing  \( C=\partial_{h}\overline{\langle m\rangle} \) . Unfortunately, the quotients method is ill-suited to this quantity, whose scaling is more aptly described as  \( C\simeq A+BL^{\alpha/\nu} \) . Therefore, one needs extremely large values of L to reach the asymptotic regime  \( C\sim L^{\alpha/\nu} \) . The behavior of the quotients in Table I is consistent with this expectation.

It has been proposed that  \( \theta \)  is not independent, but given by  \( \theta = D/2 - \beta/\nu \) . \( ^{16} \)  Combining Tables I and II we see that our numerical results are indeed compatible with this two-exponent scenario.

We can use our results to comment on the experimental situation. In an experimental study, the critical exponents are computed from fits to the scattering line shape  \( S(k) = S_{\mathrm{d}}(k) + S_{\mathrm{c}}(k) \) , where the two terms distinguish connected and disconnected contributions. In the two-exponent scenario, strongly supported by our data, the most singular term in  \( S_{d} \)  is the square of  \( S_{c} \) . This Ansatz was applied in Ref. 2, yielding  \( \nu = 0.87(7) \)  and  \( \eta = 0.16(6) \) . Since  \( \eta = \theta - 1 + 2\beta/\nu \) , however, this last value violates hyperscaling bounds and is also incompatible with our results. Perhaps taking  \( S_{\mathrm{d}} = (S_{\mathrm{c}})^{2} \)  for the whole function, not just its singularity, is an excessive simplification. Clearly a better theoretical determination of  \( S(k) \)  is needed. Our methods are well suited to a direct numerical approach to this question.

We have used the tethered formalism to obtain a comprehensive picture of the critical behavior of the DAFF, resolving the inconsistencies in previous work. This method restores self-averaging to the problem and is capable of handling rugged free-energy landscapes to equilibrate much larger systems than canonical parallel tempering. Our simulations show clear signs of a second-order phase transition and are consistent both with experiments on the DAFF and with analytical results for the RFIM. The critical exponents  \( \theta \)  and  \( \beta/\nu \)  (equivalently,  \( \eta \)  and  \( \bar{\eta} \) ) are computed with a high precision, although our simulations were not optimized for the computation of  \( \nu \)  (equivalently, of  \( \alpha \) ). We obtain  \( \nu = 0.90(15) \) , consistent with a positive  \( \alpha \) .

The tethered approach demonstrated in this paper has a very broad scope and we believe it can be fruitfully applied to many systems featuring large free-energy barriers. Indeed, it has already been successfully implemented for hard-spheres crystallization. \( ^{17} \)  Other promising avenues are the study of Goldstone bosons and the equation of state for the D = 3 spin glass, \( ^{18} \)  or equilibrium and aging relaxation in a metastable phase (e.g., to prevent crystallization of supercooled liquids, see Ref. 19).

We thank N.G. Fytas for his comments on our manuscript. Our simulations were performed on the Red Española de Supercomputación and at BIFI (Terminus and Piregrid). We acknowledge partial financial support from MICINN, Spain, (contract no FIS2009-12648-C03) and from UCM-Banco de Santander (GR32/10-A/910383). DY was supported by the FPU program (Spain).

 \( ^{1} \)  T. Nattermann, in Spin glasses and random fields, edited by A. P. Young (World Scientific, Singapore, 1998); D. P. Belanger, ibid.

 \( ^{2} \)  Z. Slanic, D. P. Belanger, and J. A. Fernandez-Baca, Phys. Rev. Lett. 82, 426 (1999).

 \( ^{5} \)  F. Ye, et al., J. Magn. & Magn. Mater. 272, 1298 (2004).

 \( ^{4} \)  D. P. Belanger, A. R. King, V. Jaccarino, and J. L. Cardy, Phys. Rev. B 28, 2522 (1983); D. P. Belanger and Z. Slanic, J. Magn. and Magn. Mat. 186, 65 (1998).

 \( ^{5} \)  A. A. Middleton and D. S. Fisher, Phys. Rev. B 65, 134411 (2002).

 \( ^{6} \)  A. K. Hartmann and A. P. Young, Phys. Rev. B 64, 214419 (2001); A. Malakis and N. G. Fytas, Phys. Rev. E 73, 016109 (2006).

 \( ^{7} \)  N. Sourlas, Comp. Phys. Comm. 121, 183 (1999); Y. Wu and J. Machta, Phys. Rev. B 74, 064418 (2006); A. Maiorano, V. Martin-Mayor, J. J. Ruiz-Lorenzo, and A. Tarançon, ibid. 76, 064435 (2007).

 \( ^{8} \)  G. Parisi and N. Sourlas, Phys. Rev. Lett. 89, 257204 (2002); N. G. Fytas and A. Malakis, Eur. Phys. J. B 79, 13 (2011).

 \( ^{9} \)  L. A. Fernandez, V. Martin-Mayor, and D. Yllanes, Nucl.

Phys. B 807, 424 (2009).

 \( ^{10} \)  V. Martin-Mayor, B. Seoane, and D. Yllanes, J. Stat. Phys. 144, 554 (2011).

 \( ^{11} \)  L. A. Fernandez, A. Gordillo-Guerrero, V. Martin-Mayor, and J. J. Ruiz-Lorenzo, Phys. Rev. Lett. 100, 057201 (2008).

 \( ^{12} \)  R. A. Baños, et al., J. Stat. Mech., P06026 (2010).

 \( ^{13} \)  H. G. Ballesteros, L. A. Fernandez, V. Martin-Mayor, and A. Muñoz Sudupe, Phys. Lett. B 378, 207 (1996).

 \( ^{14} \)  R. L. C. Vink, T. Fischer, and K. Binder, Phys. Rev. E 82, 051134 (2010); T. Fischer and R. L. C. Vink, J. Phys. Condens. Matt. 23, 234117 (2011).

 \( ^{15} \)  H. G. Ballesteros, et al., Phys. Rev. B 58, 2740 (1998).

 \( ^{16} \)  M. Schwartz and A. Soffer, Phys. Rev. Lett. 55, 2499 (1985); Phys. Rev. B 33, 2059 (1986).

 \( ^{17} \)  L. Fernández, V. Martin-Mayor, B. Seoane, and P. Verrocchio, (2011), arXiv:1103.2599.

 \( ^{18} \)  R. A. Baños, et al., Phys. Rev. Lett. 105, 177202 (2010).

 \( ^{19} \)  L. A. Fernandez, V. Martin-Mayor, and P. Verrocchio, Phys. Rev. E 73, 020501 (2006).
 
