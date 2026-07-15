# Contributions to the Theory of Specific Heat. IV. On the Calculation of the Specific Heat of Crystals from Elastic Data

M. Blackman

*Proc. R. Soc. Lond. A* 1935 **149**, 126-130
doi: 10.1098/rspa.1935.0052

## Email alerting service
Receive free email alerts when new articles cite this article - sign up in the box at the top right-hand corner of the article or click [here]

To subscribe to *Proc. R. Soc. Lond. A* go to:
http://rspa.royalsocietypublishing.org/subscriptions

This journal is © 1935 The Royal Society

# Contributions to the Theory of Specific Heat
## IV—On the Calculation of the Specific Heat of Crystals from Elastic Data

By M. BLACKMAN, Beit Scientific Research Fellow, Imperial College, South Kensington

(Communicated by S. Chapman, F.R.S.—Received November 1, 1934)

This paper contains a development of a method of calculating $\theta_{\mathrm{D}}$ values from elastic data (at low temperatures) originally given in Part II.*

1—The general problem is that one is given the equation of motion of a continuum, and hence the velocity of the elastic waves as a function of the direction of the waves in a crystal and of the elastic constants; for specific heat purposes it is necessary to obtain from this equation the mean value of the velocity, and this is correlated fairly easily with the Debye $\theta_{\mathrm{D}}$ value.

The strict solution of this problem in its general form seems extremely difficult; the methods given are all interpolation methods, due to Hopf and Lechner$\dagger$ and to Försterling$\ddagger$, following the earlier work of Born and v. Kármán,$§$ who gave a method applicable in the case of a nearly isotropic crystal. Debye had solved the problem for an isotropic medium, but this is hardly applicable to the ordinary crystal which is definitely anisotropic.

The advantage of the method developed here is that simple formulæ are obtained, and that a geometrical method is used which gives greater insight into the problem. The method is developed for regular crystals only.

2—The new idea which is introduced into this treatment, as compared with the older investigations, is that we can take advantage of the fact that we are really dealing with a crystal, and not an elastic continuum.

The crystal is built up of a large number of like cells. If we choose the basis to be a cube containing $s$ particles, we can build up a crystal out of

* ‘Proc. Roy. Soc.,’ A, vol. 148, p. 384 (1935).
$\dagger$ ‘Verh. deuts. Phys. Ges.,’ vol. 16, p. 643 (1914).
$\ddagger$ ‘Z. Physik,’ vol. 3, p. 9 (1920).
$\S$ ‘Phys. Z.,’ vol. 14, p. 15 (1913).

![](./images/812033204566360066_1.jpg)

# Theory of Specific Heat of Crystals

$n^3$ such cells; the crystal is a cube having a length of side $na$, where $a$ is the side of the elementary cube. The total number of particles is $\mathrm{N}s = n^3s$, and the number of normal vibrations $3\mathrm{N}s$.

If we consider the vibration of such a crystal we may assume solutions of the form*
$$
u_{l_1l_2l_3} = u' \, e^{i\left(2\pi vt+l_1\phi_1+l_2\phi_2+l_3\phi_3\right)}, \text{ etc.,} \tag{1}
$$
where
$$
\phi_1 = \frac{2\pi a_1}{n}, \quad \phi_2 = \frac{2\pi a_2}{n}, \quad \phi_3 = \frac{2\pi a_3}{n},
$$
and $a_1, a_2, a_3$ vary from 1 to $n$.

We have here $\mathrm{N} = n^3$ vibrations, and since there are three directions of motion for each particle, and $s$ particles in the unit cell, we have $3s\mathrm{N}$ vibrations in all which is the correct number.

This solution satisfies the condition of periodicity which is substituted for boundary conditions.

We have of course in the general case a determinant giving the frequency $v$ as a function of $\phi_1, \phi_2, \phi_3$. Here we will deal only with the region of small frequencies where we have only the three acoustical branches.

In this region the crystal behaves like an elastic continuum and we may describe any wave in a continuum in the form
$$
u = u' \, e^{2\pi i\left(\frac{t}{\mathrm{T}}+\frac{px+qy+rz}{\lambda}\right)}. \tag{2}
$$

The equation of motion of the regular crystal in this region is given by
$$
\begin{vmatrix}
c_{11}p^2 + c_{44}q^2 + c_{44}r^2 - \rho c^2 & (c_{12}+c_{44})pq & (c_{12}+c_{44})pr \\
(c_{12}+c_{44})qp & c_{11}q^2 + c_{44}r^2 + c_{44}p^2 - \rho c^2 & (c_{12}+c_{44})qr \\
(c_{12}+c_{44})rp & (c_{12}+c_{44})rq & c_{11}r^2 + c_{44}p^2 + c_{44}q^2 - \rho c^2
\end{vmatrix} = 0. \tag{3}
$$

Now since (1) and (2) are perfectly equivalent methods of describing a wave in a crystal we have the relations
$$
\phi_1 = \frac{2\pi}{\lambda} ap, \quad \phi_2 = \frac{2\pi}{\lambda} aq, \quad \phi_3 = \frac{2\pi}{\lambda} ar. \tag{4}
$$

$(x = l_1a,\ y = l_2a,\ z = l_3a)$.

The main point is now to substitute these relations back in (3) and

*Cf. Born and v. Kármán, ‘Phys. Z.,’ vol. 13, p. 297 (1912), where this method was first introduced.

128
M. Blackman

obtain a new equation in which we have the frequency $v$ as a function of $\phi_1, \phi_2, \phi_3$.

$$
\begin{vmatrix}
- v^2 + \frac{c_{11} \phi_1^2}{4\pi^2 a^2 \rho} + \frac{c_{44} \phi_2^2}{4\pi^2 a^2 \rho} + \frac{c_{44} \phi_3^2}{4\pi^2 a^2 \rho} & \frac{(c_{12} + c_{44}) \phi_1 \phi_2}{4\pi^2 a^2 \rho} & \frac{(c_{12} + c_{44}) \phi_1 \phi_3}{4\pi^2 a^2 \rho} \\
\frac{(c_{12} + c_{44}) \phi_2 \phi_1}{4\pi^2 a^2 \rho} & - v^2 + \frac{c_{11} \phi_2^2}{4\pi^2 a^2 \rho} + \frac{c_{44} \phi_3^2}{4\pi^2 a^2 \rho} + \frac{c_{44} \phi_2^2}{4\pi^2 a^2 \rho} & \frac{(c_{12} + c_{44}) \phi_2 \phi_3}{4\pi^2 a^2 \rho} \\
\frac{(c_{12} + c_{44}) \phi_3 \phi_1}{4\pi^2 a^2 \rho} & \frac{(c_{12} + c_{44}) \phi_3 \phi_2}{4\pi^2 a^2 \rho} & - v^2 + \frac{c_{11} \phi_3^2}{4\pi^2 a^2 \rho} + \frac{c_{44} \phi_1^2}{4\pi^2 a^2 \rho} + \frac{c_{44} \phi_2^2}{4\pi^2 a^2 \rho}
\end{vmatrix} = 0. \tag{5}
$$

This is a form which permits us to take advantage of the fact that we are dealing with a crystal.

3—In the region of low frequencies we know that the density of the vibrations is proportional to $v^2$. If we count the number of vibrations $(n_1)$ between $v = 0$ and $v = v_1$, we can obtain an expression for the Debye maximum frequency $v_D$ in the form

$$
v_D^3 = v_1^3 \frac{n_0}{n_1}, \tag{6}
$$

where $n_0 =$ total number of the vibrations $= 3s\text{N}$.

The advantage of using (5) is that we can evaluate $n_0$ and $n_1$ fairly simply on the same scale, in certain cases.

The method now followed is essentially that adopted in Part II. The justification of the method adopted is given there. The advance made here is that we do not need to refer our considerations to a model as done there, and hence we have a greater generality.

For small values of $c_{12} + c_{44}/c_{11}$ (about $\frac{1}{5}$) we may neglect the non-diagonal terms and obtain for the surfaces of constant frequency three ellipsoids* of the form

$$
1 = \frac{\phi_1^2}{\frac{4\pi^2 a^2 \rho}{c_{11}}} + \frac{\phi_2^2}{\frac{4\pi^2 a^2 \rho}{c_{44}}} + \frac{\phi_3^2}{\frac{4\pi^2 a^2 \rho}{c_{44}}}. \tag{7}
$$

The volume of the ellipsoids lying between $v = 0$ and $v = v_1$ is proportional to the number of vibrations lying between $v = 0$ and $v = v_1$. Using the range $0 \leqq \phi \leqq \pi$ in each case, the total number of vibrations is proportional to $3sn^3$.

* Cf. Part II.

### Theory of Specific Heat of Crystals

The value of $v_D$ obtained is given by*

$$
v_D{}^3 = \frac{3}{4\pi} \frac{s}{a^3 \rho^{\frac{2}{3}}} \sqrt{c_{11} c_{44}{}^2}. \tag{8}
$$

To obtain the result in Part II (i.e., an orthocubic lattice with particles of one type only) we put
$$
s = 1,\quad \rho = \frac{m}{a^3},\quad c_{11} = \frac{\alpha + 4\gamma}{a},\quad c_{12} = c_{44} = \frac{2\gamma}{a},
$$
where $\alpha$ and $\gamma$ are the binding forces defined in Part II.† This gives
$$
v_J{}^3 = \frac{3}{4\pi} \sqrt{\frac{4\gamma^2 (\alpha + 4\gamma)}{m^3}},
$$
which we obtained in Part II, and which follows as a special case of the more general theory.

In the case where $c_{12} + c_{44}/c_{11}$ is larger than assumed here the surfaces become very complicated, and explicit formulæ can be obtained only in one special case, where the wave surfaces become spherical. We assume the Cauchy Relation $c_{12} = c_{44}$ for simplicity and then find
$$
v_D{}^3 = \frac{3s}{3 \cdot 57 \sqrt{3}\pi} \frac{1}{a^3 \rho^{\frac{2}{3}}} \sqrt{c_{11} c_{44}{}^2} \quad \left(c_{44} = \frac{1}{3}c_{11}\right). \tag{9}
$$

This equation is so written in order to illustrate the fact that it is really the constant of the equation which has been changed, and that this is about $50\%$ smaller.

Now the equation (1) with its constant $3/4\pi$ will hold for $c_{44}/c_{11} \leqq \frac{1}{10}$ as is evidenced by the comparison of the value for KCl with the accurate calculations of Hopf and Lechner (see Table I below). Now it will be assumed that the change in the constant is linear between $c_{44}/c_{11}$ values of $\frac{1}{10}$ and $\frac{1}{3}$; this is perhaps not strictly justified, but it will suffice if we desire results of a few per cent. accuracy, as will be shown in Table I.

For values of $c_{44}/c_{11}$ between $\frac{1}{10}$ and $\frac{1}{3}$ we use this method of finding the constant, and also the value of $\frac{1}{2}(c_{12} + c_{44})$ instead of $c_{12}$ and $c_{44}$ in the case where these are found not to be quite equal. In the case of formula (8) the $c_{44}$ values only are used.

* It is interesting that Hopf and Lechner found extremely complicated integrals in this case so that a direct computation was not possible. This illustrates the superiority of the geometrical consideration.
† *Cf.* also Born and v. Kármán, *loc. cit.*

VOL. CXLIX.—A
K

130
# Theory of Specific Heat of Crystals

4—The following table shows a comparison of the results obtained here with Hopf and Lechner's results, also the data relevant to the calculation. The elastic data used were those due to Voigt and are the same as those used by Hopf and Lechner.

<table>
  <thead>
    <tr>
      <th rowspan="2">Substance</th>
      <th rowspan="2">$s$</th>
      <th rowspan="2">$a$</th>
      <th rowspan="2">$\rho$</th>
      <th colspan="3">TABLE I</th>
    </tr>
    <tr>
      <th>$\theta_{\text{D}}$ (calculated)</th>
      <th>$\theta_{\text{D}}$ (Hopf and Lechner)</th>
      <th>$\theta_{\text{D}}$ (Born and v. Kármán)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>KCl</td>
      <td>1</td>
      <td>3⋅14</td>
      <td>1⋅987</td>
      <td>227</td>
      <td>230</td>
      <td>—</td>
    </tr>
    <tr>
      <td>NaCl</td>
      <td>1</td>
      <td>2⋅81</td>
      <td>2⋅161</td>
      <td>282</td>
      <td>296</td>
      <td>302</td>
    </tr>
    <tr>
      <td>$\text{CaF}_2$</td>
      <td>12</td>
      <td>5⋅45</td>
      <td>3⋅11</td>
      <td>496</td>
      <td>499</td>
      <td>—</td>
    </tr>
    <tr>
      <td>$\text{FeS}_2$</td>
      <td>12</td>
      <td>5⋅38</td>
      <td>5⋅03</td>
      <td>662</td>
      <td>682</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

The method can be made more accurate by the use of Born and v. Kármán's method in conjunction with formula (8). It may also be pointed out that a similar analysis holds for any type of crystal; an investigation shows, however, that the large number of elastic constants render the treatment rather complicated, and it has been thought better to confine this paper to essentially simple crystals.

## SUMMARY

A new method is deduced by which $\theta_{\text{D}}$ values can be calculated from elastic data; this is based on considerations of lattice theory as well as on the geometrical form of the wave surfaces.

The numerical results in particular cases are compared with those due to other investigators.
