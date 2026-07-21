The replica mean field theory for the glass matrix model

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2008 J. Phys. A: Math. Theor. 41 125002

(http://iopscience.iop.org/1751-8121/41/12/125002)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 130.237.29.138
This content was downloaded on 21/08/2015 at 18:33

Please note that terms and conditions apply.

# The replica mean field theory for the glass matrix model

Kazuo Nokura

Shonan Institute of Technology, Fujisawa 251-8511, Japan

Received 10 June 2007, in final form 27 December 2007
Published 10 March 2008
Online at stacks.iop.org/JPhysA/41/125002

## Abstract
We study the dynamical phase transition of the glass matrix model by using the replica method for deterministic models. In the glass matrix model, $N$ dynamical variables are defined by $P$ component vectors which make states of a particle. Each component of a vector is assumed to take $\pm 1$. To perform replica calculation, auxiliary variables are introduced to control the order of the sum of replicated partition function. These variables work like quenched random variables of the usual replica method. Using the approximation for small $P/N$ and assuming the homogeneity of the component space, we find that the replica theory is similar to that of the previously studied glassy spin models. We study the dynamical solution, which is defined by imposing the marginally stable condition for a one-step replica symmetry breaking ansatz. To find the marginally stable condition, we study the fluctuation modes in replica spaces and component space. The results of simulated annealing is presented to compare with the analytic result. The transition temperatures suggested by the two approaches are consistent. However, the agreement is modest in the sense that simulated annealing shows richer behavior than the replica results, mainly due to the lower energy states, which appear by the slow annealing schedule.

PACS numbers: 05.20.–y, 05.50.+q, 64.60C

## 1. Introduction
Glassy systems are characterized by the enormous number of metastable states at low temperature [1]. Because of these states, the dynamical property changes at glass transition temperature, which is called a dynamical phase transition. Below this temperature, very slow parts of correlation and response function arise and describe a long-time property such as ageing. This is a non-equilibrium phenomenon and transition temperature is not identified by a static approach such as the study of partition function. Although a dynamical method has been applied to some mean field models [2–4], direct study of dynamics is very difficult in many cases.

Recently, by the development of the replica theory of spin glass models [5], it has been suggested that glassy systems can be discussed by referring to the replica method [1,6]. Some authors pointed out that there is a close relation between the replica method and the dynamical approach [7]. Further, it was suggested that the replica mean field solution with marginal stability describes the dynamical phase transition and glassy states at low temperature [8,9]. This idea works well for random spin models and nonrandom frustrated spin models to study low-temperature phase, especially to identify the transition temperature [10-12]. It is highly desirable to extend the study to glassy particle systems.

Particle systems are characterized by the large space of states when compared with spin systems. Taking into account this feature, several authors suggested the mean field model of the deterministic glass model called the glass matrix model [13, 17]. In this model, the coordinates of the particle are represented by P-component vectors to model a large space of particle state, where P is of the same order of the number of particles N. Using the conventional terminology, we call the P-component vector a spin. Interactions are made of inner products of these spins. The simplest nontrivial energy function is given by

$$
H\left\{S_{i}^{a}\right\}=\frac{1}{4 N} \sum_{i \neq j}\left(\sum_{a} S_{i}^{a} S_{j}^{a}\right)^{2}-\frac{1}{4} P N. \tag{1}
$$

To be specific, we discuss the case where each component takes $\pm 1$. Thus for the N spin system, we have dynamical variables $S_{i}^{a}= \pm 1$ ($i=1,2, \ldots, N, a=1,2, \ldots, P$). The volume of particle states is $2^{P}$. Obviously, this energy function implies that the N vectors should be orthogonal to each other to give low-energy states. For general $S_{i}^{a}$, each inner product is of order $\sqrt{P}$, which gives the energy of order $PN$. This is comparable to the high-temperature entropy given by $PN \ln 2$. To have nontrivial dynamics, $P$ should be the same order of $N$, as we will see in the following section. We also note the duality between $i$ and $a$, that is, the energy function can be written by the inner products of $P$ vectors which have $N$ components.

The partition function of the glass matrix model was evaluated in the paramagnetic phase [13]. It was found that the entropy becomes zero at finite temperature, which implies that there is a phase transition above this temperature. By numerical simulations, it was shown that the glass-phase transition takes place at finite temperature. However, analytic study of transition temperature and low-temperature phase, even by some kind of approximation, seems to be absent more than 10 years after the suggestion.

The purpose of this paper is to apply the replica method to the glass matrix model and study the dynamical transition and low-temperature property. The replica method we adopt is based on a transformation of dynamical variables, which was applied for long-range anti- ferromagnets (LRAF) a few years ago [11, 12]. By this method, we can formulate the replica theory for the glass matrix model and discuss the glassy states by using the idea of marginal stability.

The plan of this paper is as follows. In the following section, we present the replica formulation for the glass matrix model. We find that the calculation becomes extremely simple if we restrict ourselves to small $\alpha=P / N$, where the similarity to the anti-Hebbian (AH) model [10] becomes apparent. We also show that the action becomes similar to the replica theory of the mean field spin models by introducing the assumption of homogeneity of the component space. In section 3, we discuss the one-step replica symmetry breaking (RSB) solution. In section 4, we discuss the fluctuation around the saddle point to find the marginally stable condition. In section 5, we present the results of simulation to compare with the analytic results. Section 6 is devoted to some discussion.

## 2. The replica method for the glass matrix model

The replica method was originally introduced to find quenched random averages of the free energy, i.e., the logarithm of the partition function, by using the relation $\ln Z = \lim_{n \to 0}(Z^n - 1)/n$. In the application to the mean field model, we obtain the effective action which is expressed by overlaps between metastable states. Apart from the study of the free energy average, the property of overlap order parameter gives deep information of the spin glass states. This suggests that if there are many pure states in the system, the replicated partition function can give a meaningful idea of the property of metastable states even if there is no randomness. This is the motivation for introducing the replica method for deterministic models.

In this section, we first discuss the high-temperature expansion of the glass matrix model for small $\alpha$ and then study the replica method. The study of high-temperature expansion is helpful in discussing the replica method.

### 2.1. High-temperature expansion

Let us discuss the high-temperature expansion for the glass matrix model for small $\alpha$. We find that the expression is very similar to that of the previously studied glassy spin models to the lowest order of $\alpha$.

The partition function for $H\{S_i^a\}$ is given by
$$
Z = \sum_{\{S_i^a\}} \exp \left(-\beta H\{S_i^a\}\right),
\tag{2}
$$
where $\beta = 1/T$ is an inverse temperature. Substituting the energy function into the partition function, we have
$$
Z = \sum_{\{S_i^a\}} \prod_{i<j,a<b} \exp \left(-\frac{\beta}{N} S_i^a S_i^b S_j^a S_j^b\right).
\tag{3}
$$

In the high-temperature expansion, the partition function is expanded in terms of $\beta/N$. The exact solution is given by the theory of the matrix model [13]. For small $\alpha$, the leading contribution comes from the products of the same component indices that make a loop. For these contributions, the products $S_i^a S_i^b$ work like a single variable. In this way, we obtain
$$
Z = \exp \left(-\frac{1}{4} P(P-1)(\ln(1+\beta)-\beta)+PN\ln 2\right)
\tag{4}
$$
for small $\alpha$. As expected, this expression is similar to that of the AH model. In appendix A, we present another derivation of this result. Then the free-energy density $f = -\ln Z/\beta PN$, entropy $s$ and energy $e$ are given by
$$
f = -\frac{1}{\beta} \ln 2 + \frac{1}{4} \alpha \left(\frac{1}{\beta} \ln(1+\beta)-1\right)
\tag{5}
$$

$$
s = \ln 2 + \frac{1}{4} \alpha \left(\frac{\beta}{1+\beta}-\ln(1+\beta)\right)
\tag{6}
$$

$$
e = \frac{1}{4} \frac{\alpha}{1+\beta} - \frac{1}{4} \alpha.
\tag{7}
$$

These expressions lead to an interesting insight into the low-temperature property. Entropy becomes zero at $T=T_s \sim \exp(-1-4\ln 2/\alpha)$, which implies that there should be some phase transition at finite temperature. A similar result is also found in spin models.

Simulated annealing shows that the temperature dependence of the energy does not obey the above equation below a certain temperature, signaling the existence of phase transition. In the following subsection, we discuss the replica theory by restricting ourselves to small $\alpha$.

### 2.2. The replica method
Now we discuss the replica method for the glass matrix model. This is based on a simple equation introduced as follows [11]. In the first step, we introduce $n$ replicas $S_{i}^{a\alpha}$ for each Ising variable and write

$$
Z^{n}=\sum_{\left\{S_{i}^{a \alpha}\right\}} \exp \left(-\beta \sum_{\alpha=1}^{n} H\left\{S_{i}^{a \alpha}\right\}\right).
\tag{8}
$$

For this expression, we want to perform partial statistical summation with fixed correlation among replicas. This is achieved by the transformation common to all replica defined by $S_{i}^{a \alpha} \rightarrow \eta_{i}^{a} S_{i}^{a \alpha}$, where auxiliary variables $\eta_{i}^{a}= \pm 1$. We note that $S_{i}^{a \alpha} S_{i}^{a \beta}$ are invariant for an arbitrary $\eta_{i}^{a}$ and $Z^{n}$ does not change, thanks to the summation over each replica. Thus by performing the sum over $\eta_{i}^{a}$, we obtain the expression

$$
Z^{n}=\frac{1}{2^{P N}} \sum_{\left\{\eta_{i}^{a}\right\}} \sum_{\left\{S_{i}^{a \alpha}\right\}} \exp \left(-\beta \sum_{\alpha=1}^{n} H\left\{\eta_{i}^{a} S_{i}^{a \alpha}\right\}\right).
\tag{9}
$$

With regards to the usual replica method, $\eta_{i}^{a}$ work like quenched randomness. This formula gives a highly nontrivial expression when we perform the $\eta_{i}^{a}$ sum first. This is feasible for small $\alpha$ in the same way as the high-temperature expansion.

The replicated and transformed energy function is given by

$$
\sum_{\alpha=1}^{n} H\left\{\eta_{i}^{a} S_{i}^{a \alpha}\right\}=\frac{1}{N} \sum_{i<j, a<b} \eta_{i}^{a} \eta_{i}^{b} \eta_{j}^{a} \eta_{j}^{b} \Omega_{i j}^{a b},
\tag{10}
$$

where

$$
\Omega_{i j}^{a b}=\sum_{\alpha=1}^{n} S_{i}^{a \alpha} S_{i}^{b \alpha} S_{j}^{a \alpha} S_{j}^{b \alpha}.
\tag{11}
$$

Although this expression looks rather complicated, we note that there is some analogy to the replica method for random spin models, such as the Hopfield model [14] and the AH model [10]. That is, each term in the energy function has the product of quenched variables with two-site indices. This implies that the sum over $\eta_{i}^{a}$ yields loop diagrams in terms of site. The apparent difference is that dynamical variables and quenched variables have common component indices $a, b$. This means that there can be order parameters which depend on component indices. For this reason, the matrix model is similar to the particle model rather than the spin model. In addition, due to four-body interaction among $\eta_{i}^{a}$, the sum over $\eta_{i}^{a}$ is much more complicated than the average over quenched randomness in spin models. However, when we restrict ourselves to the lowest nontrivial order of $\alpha$, we find the diagrams appearing in the expansion in terms of $\beta$ have the same structure as those of spin models, that is, one-loop diagrams made of $\Omega_{i j}^{a b}$. In the following study, we concentrate on the lowest order of $\alpha$.

After the summation over site indices, one-loop diagrams made of $\Omega_{i j}^{a b}$ can be expressed by the overlap defined by

$$
Q_{a b}^{\alpha \beta}=\frac{1}{N} \sum_{i} S_{i}^{a \alpha} S_{i}^{b \alpha} S_{i}^{a \beta} S_{i}^{b \beta}.
\tag{12}
$$


In this way, we obtain

$$
Z^{n}=\sum_{\left\{S_{i}^{a \alpha}\right\}} \exp \left(-\frac{1}{2} \sum_{a<b} \operatorname{Tr}\left\{\ln \left(1+\beta \mathbf{Q}_{a b}\right)-\beta\right\}\right)
\tag{13}
$$

to the lowest order of $\alpha$. Note in this expression, Tr works only on the replica indices and there is no coupling among a different pair $a b$. Note $Q_{a b}^{\alpha \alpha}=1$ is included in the trace. Another derivation of (13) is presented in appendix A.

For $Q_{a b}^{\alpha \beta}$ with $\alpha \neq \beta$ and $a \neq b$, we write

$$
\begin{aligned}
1=\prod_{a<b, \alpha<\beta} \iint & \frac{N}{P} \frac{\mathrm{d} \Lambda_{a b}^{\alpha \beta} \mathrm{d} Q_{a b}^{\alpha \beta}}{2 \pi \sqrt{-1}} \\
& \times \exp \left\{-\frac{N}{P} \Lambda_{a b}^{\alpha \beta}\left(Q_{a b}^{\alpha \beta}-\frac{1}{N} \sum_{i} S_{i}^{a \alpha} S_{i}^{b \alpha} S_{i}^{a \beta} S_{i}^{b \beta}\right)\right\}
\end{aligned}
$$

and obtain

$$
Z^{n}=\prod_{a<b, \alpha<\beta} \iint \frac{N}{P} \frac{\mathrm{d} \Lambda_{a b}^{\alpha \beta} \mathrm{d} Q_{a b}^{\alpha \beta}}{2 \pi \sqrt{-1}} \exp (-A\{Q, \Lambda\}),
\tag{14}
$$

where the action is given by

$$
A\{Q, \Lambda\}=G\{Q\}+K\{Q, \Lambda\}+F\{\Lambda\},
\tag{15}
$$

with

$$
G\{Q\}=\frac{1}{2} \sum_{a<b} \operatorname{Tr}\left\{\ln \left(1+\beta \mathbf{Q}_{a b}\right)-\beta\right\}
$$

$$
K\{Q, \Lambda\}=\frac{N}{P} \sum_{a<b, \alpha<\beta} \Lambda_{a b}^{\alpha \beta} Q_{a b}^{\alpha \beta}
$$

$$
F\{\Lambda\}=-N \ln Z_{P}^{n},
$$

where

$$
Z_{P}^{n}=\sum_{\{S\}} \exp \frac{1}{P} \sum_{a<b, \alpha<\beta} \Lambda_{a b}^{\alpha \beta} S^{a \alpha} S^{b \alpha} S^{a \beta} S^{b \beta}.
\tag{16}
$$

In $Z_{P}^{n}$, site indices $i$ in $S_{i}^{a \alpha}$ are dropped. To the lowest order of $\alpha$, this expression defines the one-site problem for the glass matrix model. Unlike the spin model, this one-site problem still contains a large number of spin components. Note that the factor $N / P$ is assigned for each $\Lambda_{a b}^{\alpha \beta}$ in (14) to have $F\{\Lambda\} / N$ free from $N$.

The expression (14) contains the $P(P-1)$ folded integral over $\Lambda_{a b}^{\alpha \beta}$ and $Q_{a b}^{\alpha \beta}$ for each replica pair. Thus we will have $P(P-1)$ folded integral around the saddle point even if it is found. In section 4 and appendix C, we discuss the fluctuation modes around mean field solution. The argument there implies that the contribution by these modes is of order $P$ instead of $P^{2}$. This justifies the saddle point approximation for glass matrix model.

In (16), couplings among different components can be treated by the mean field method if we assume the homogeneity in component space, that is, $\Lambda_{a b}^{\alpha \beta}=\Lambda^{\alpha \beta}$ and $Q_{a b}^{\alpha \beta}=Q^{\alpha \beta}$. By this approximation, the replica theory substantially reduces to that of the spin models. With mean fields $\Lambda^{\alpha \beta}$, we have

$$
Z_{P}^{n}=\sum_{\left\{S^{a \alpha}\right\}} \exp \frac{1}{2 P} \sum_{\alpha<\beta} \Lambda^{\alpha \beta}\left\{\left(\sum_{a} S^{a \alpha} S^{a \beta}\right)^{2}-P\right\}.
\tag{17}
$$


Introducing Gaussian variables $q^{\alpha\beta}$, we have

$$
\begin{aligned}
Z_{P}^{n}= & \int \prod_{\alpha<\beta} \frac{\sqrt{P \Lambda^{\alpha \beta}} \mathrm{d} q^{\alpha \beta}}{\sqrt{2 \pi}} \exp -\frac{1}{2} P \sum_{\alpha<\beta} \Lambda^{\alpha \beta}\left(q^{\alpha \beta}\right)^{2}-\frac{1}{2} \sum_{\alpha<\beta} \Lambda^{\alpha \beta} \\
& +P \ln \sum_{S^{\alpha}} \exp \sum_{\alpha<\beta} \Lambda^{\alpha \beta} q^{\alpha \beta} S^{\alpha} S^{\beta},
\end{aligned}
$$

where the component indices in $S^{\alpha \alpha}$ are dropped. This expression gives the one-site-one-component problem of the mean field theory for the glass matrix model. Note that there are terms of $\Lambda^{\alpha \beta}$ which are not proportional to $P$, which will be disregarded in the saddle point approximation.

To summarize this section, we write the full expression of action at the homogeneous saddle point

$$
\begin{aligned}
A\{Q, \Lambda\}= & \frac{1}{4} P(P-1) \operatorname{Tr}\{\ln (1+\beta \mathbf{Q})-\beta\} \\
& +\frac{1}{2} N(P-1) \sum_{\alpha<\beta} \Lambda^{\alpha \beta} Q^{\alpha \beta}+\frac{1}{2} N P \sum_{\alpha<\beta} \Lambda^{\alpha \beta}\left(q^{\alpha \beta}\right)^{2} \\
& -N P \ln \sum_{\{S\}} \exp \left(\sum_{\alpha<\beta} \Lambda^{\alpha \beta} q^{\alpha \beta} S^{\alpha} S^{\beta}\right).
\end{aligned}
$$

This action is appealing since it has a similar structure to the replica theory of infinite range spin glass models, although $\Lambda^{\alpha \beta}$ will depend on temperature. With this expression, it is easy to study several well-known ansatz of the replica solution. In the following section, we discuss the one-step RSB solution.

### 3. Replica symmetry breaking solutions

In this section, we study the one-step RSB solution for the action obtained in the previous section. We will study the fluctuation modes around the saddle point solution in the following section.

In the one-step RSB ansatz, the replica index is divided into $n/m$ groups, which implies $Q^{\alpha \beta}$ is divided into $(n/m) \times (n/m)$ blocks of size $m \times m$. We assume that, in the diagonal blocks, $Q^{\alpha \beta}=Q_{1}$ and in the off-diagonal blocks, $Q^{\alpha \beta}=Q_{0}$. Further, $\Lambda^{\alpha \beta}$ and $q^{\alpha \beta}$ are assumed to have the same structure with $\Lambda_{1}, \Lambda_{0}$ and $q_{1}, q_{0}$, respectively, because the correlation among replicas is controlled by the correlation among metastable states.

Using the assumption for order parameters, we evaluate the free energy in appendix B, and obtain $\beta f=-\lim _{n \rightarrow 0}\left(Z^{n}-1\right) / n P N$ as

$$
\begin{aligned}
\beta f=\frac{1}{4} \alpha & \left\{\frac{1}{m} \ln \left(1+\beta X_{m}\right)+\left(1-\frac{1}{m}\right) \ln \left(1+\beta X_{1}\right)+\frac{\beta Q_{0}}{1+\beta X_{m}}-\beta\right\} \\
& +\frac{1}{4}\left\{(m-1) \Lambda_{1} Q_{1}-m \Lambda_{0} Q_{0}\right\}+\frac{1}{4}\left\{(m-1) q_{1}^{2} \Lambda_{1}-m q_{0}^{2} \Lambda_{0}\right\} \\
& +\frac{1}{2} q_{1} \Lambda_{1}-\frac{1}{m} \int D x \ln \int D y(2 \cosh A)^{m},
\end{aligned}
$$

where $X_{1}=1-Q_{1}, X_{m}=1-Q_{1}+m\left(Q_{1}-Q_{0}\right), A=\sqrt{q_{0} \Lambda_{0}} x+\sqrt{q_{1} \Lambda_{1}-q_{0} \Lambda_{0}} y$ and $D x=\exp \left(-x^{2} / 2\right) \mathrm{d} x / \sqrt{2 \pi}$. The saddle point equations are given by

$$
\Lambda_{0}=\frac{\alpha \beta^{2} Q_{0}}{\left(1+\beta X_{m}\right)^{2}} \quad \Lambda_{1}=\frac{\alpha \beta}{m}\left(\frac{1}{1+\beta X_{1}}-\frac{1}{1+\beta X_{m}}\right)+\frac{\alpha \beta^{2} Q_{0}}{\left(1+\beta X_{m}\right)^{2}}
$$


$$
q_{0}=\int D x(\overline{\langle S\rangle})^{2} \quad q_{1}=\int D x \overline{\langle S\rangle^{2}},
$$

where $\langle S\rangle=\tanh A$,
$$
\overline{\cdots}=\frac{\int D y \cdots \cosh ^{m} A}{\int D y \cosh ^{m} A}
\tag{20}
$$
and $Q_{0}=q_{0}^{2}, Q_{1}=q_{1}^{2}$.

We need one additional equation to determine the solution. According to the suggestion [9], there are two kinds of RSB solution; one is static and other is dynamical, depending on the equation. The static solution is expected to describe the absolute minimum state of the system and dynamical solution is expected to describe the glassy states. In both cases, numerical studies reveal that $q_{0}=Q_{0}=\Lambda_{0}=0$. This implies that contributing states are not correlated each other.

The static solution is given by the extreme value of $f$ in terms of $m$, that is, by imposing $\partial f / \partial m=0$. According to the numerical study, this solution appears at the very low temperature which is very close to $T_{s}$ with $q_{1} \sim 1, q_{0}=0$, such that $\beta\left(1-q_{1}^{2}\right) \sim 0$. This implies $X_{1} \sim 0$ and $X_{m} \sim m$. After a short calculation presented in appendix B, we have
$$
f \sim \frac{1}{4} \alpha\left(\frac{1}{\beta m} \ln (1+\beta m)-1\right)-\frac{1}{\beta m} \ln 2.
\tag{21}
$$

This expression implies that $(\partial f / \partial m)_{m=1}=0$ equals $s=0$ approximately. This explains that $T_{s}$ is very close to the temperature $T_{\mathrm{RSB}}$, where the solution determined by $\partial f / \partial m=0$ appears. This aspect seems to be common in glassy models.

In the following section, we discuss the dynamical solution by imposing the marginally stable condition.

### 4. Fluctuation around the mean field solution

In this section, we discuss the fluctuation modes around the mean field solution. Although the fluctuation modes in replica space have been well studied [15,16], our model has fluctuations in component space which will require additional consideration. We are interested in the marginally stable condition, which determine the dynamical phase transition and low-temperature glassy states. The eigenmodes with the smallest eigenvalues with respect to all fluctuation can be marginally stable modes.

To study the fluctuation modes around the saddle point, we set $\Lambda_{a b}^{\alpha \beta}=\Lambda^{\alpha \beta}+\delta \Lambda_{a b}^{\alpha \beta}$ and $Q_{a b}^{\alpha \beta}=Q^{\alpha \beta}+\delta Q_{a b}^{\alpha \beta}$ in (15), where $\Lambda^{\alpha \beta}$ and $Q^{\alpha \beta}$ are one-step RSB solutions. In $G\{Q\}$ and $K\{Q, \Lambda\}$, there are no couplings among different pair $a b$ and it is enough to study the fluctuation only in the replica space. On the other hand, in $F\{\Lambda\}$, there are couplings among different component pairs.

Let us start with $F\{\Lambda\}$. The second-order terms in $F\{\Lambda+\delta \Lambda\}-F\{\Lambda\}$, denoted by $\delta^{2} F$, are given by
$$
\delta^{2} F\{\Lambda\}=\frac{N}{2 P^{2}}\left(\left\langle\Delta^{2}\right\rangle-\langle\Delta\rangle^{2}\right),
\tag{22}
$$
where
$$
\Delta=\sum_{a<b, \alpha<\beta} \delta \Lambda_{a b}^{\alpha \beta} S^{a \alpha} S^{b \alpha} S^{a \beta} S^{b \beta}
\tag{23}
$$
and $\langle\cdots\rangle$ means an average by the weight of one-site-one-component problem defined by (18). In this average, correlation among replicas of the same component variables remains.

Thus for example, $\langle S^{a\alpha} S^{b\gamma} S^{a\beta} S^{b\delta} \rangle = \langle S^{a\alpha} S^{a\beta} \rangle \langle S^{b\gamma} S^{b\delta} \rangle = q^{\alpha\beta} q^{\gamma\delta}$, where $q^{\alpha\beta} = \langle S^\alpha S^\beta \rangle$, etc.
Using this rule, we group the terms in $D = \langle \Delta^2 \rangle - \langle \Delta \rangle^2$ in terms of the number of different component indices and obtain

$$
D = \sum_{a<b} \sum_{(\alpha\beta),(\gamma\delta)} \delta \Lambda_{ab}^{\alpha\beta} \delta \Lambda_{ab}^{\gamma\delta} A_{(\alpha\beta)(\gamma\delta)} + \sum_{a\neq b\neq c} \sum_{(\alpha\beta),(\gamma\delta)} \delta \Lambda_{ab}^{\alpha\beta} \delta \Lambda_{ac}^{\gamma\delta} B_{(\alpha\beta)(\gamma\delta)},
\tag{24}
$$

where all component indices are different in the sum and
$$
A_{(\alpha\beta)(\gamma\delta)} = (q^{\alpha\beta\gamma\delta})^2 - (q^{\alpha\beta})^2 (q^{\gamma\delta})^2 \quad B_{(\alpha\beta)(\gamma\delta)} = q^{\alpha\beta\gamma\delta} q^{\alpha\beta} q^{\gamma\delta} - (q^{\alpha\beta})^2 (q^{\gamma\delta})^2,
$$
with $q^{\alpha\beta\gamma\delta} = \langle S^\alpha S^\beta S^\gamma S^\delta \rangle$. We should note that these matrix elements do not depend on component indices. We should also note that there is no restriction on replica indices at this stage except $\alpha < \beta$ and $\gamma < \delta$.

To diagonalize $D$ in component space, denoting eigen modes by $I$, we set $\delta \Lambda_{ab}^{\alpha\beta} = \sum_I \delta \Lambda_I^{\alpha\beta} \psi_{ab}^{(I)}$ and find the normalized vector $\psi_{ab}^{(I)}$ such that $\sum_{a<b} \psi_{ab}^{(I)} \psi_{ab}^{(I')} = \delta_{II'}$ and $\sum_{a,b\neq a,c\neq a} \psi_{ab}^{(I)} \psi_{ac}^{(I')} = \epsilon_I \delta_{II'}$. We discuss these vectors in appendix C. The largest $\epsilon_I$ is given by the homogeneous mode $\psi_{ab}^{(0)} = (P(P - 1)/2)^{-1/2}$, which gives $\epsilon_0 \sim 2P$ with degeneracy 1. The second largest eigenvalue is given by $\epsilon_1 \sim P$ with degeneracy $P - 1$. The smallest eigenvalue is given by $\epsilon_2 = 0$ with degeneracy $P(P - 3)/2$. As discussed in appendix C, the largest $\epsilon_1$ give the softest modes in the space made of $(\delta Q \delta \Lambda)$. Thus we can restrict ourselves to the homogeneous eigenmode to have marginal stability. These arguments also imply that the leading contribution comes from the second term in (24).

After finding contributing eigenmode in component space, the problem is reduced to the well-studied problem of finding the eigenmodes around RSB solution [15, 16]. We set $q^{\alpha\beta} = 0$ for $\alpha$ and $\beta$ belonging to different blocks, and $q^{\alpha\beta} = q_1$ for $\alpha$ and $\beta$ belonging to the same blocks. By the argument presented above, it is sufficient to study $B_{(\alpha\beta)(\gamma\delta)}$. For the replicas in the same block, elements of $B_{(\alpha\beta)(\gamma\delta)}$ is given by
$$
P_\Lambda = q_1^3 - q_1^4 \quad Q_\Lambda = q_1^3 - q_1^4 \quad R_\Lambda = q_1^2 \overline{\langle S \rangle^4} - q_1^4
$$
for the cases $(\alpha\beta) = (\gamma\delta)$, $\alpha = \gamma$ and $\beta \neq \delta$, and $(\alpha\beta) \neq (\gamma\delta)$, respectively, and zero for the case that $\alpha, \beta, \gamma, \delta$ belonging to different blocks. Then the eigenvalue of replicon modes is given by
$$
\begin{aligned}
\lambda_\Lambda &= P_\Lambda - 2 Q_\Lambda + R_\Lambda \\
&= q_1^2 \overline{(1 - \langle S \rangle^2)^2}
\end{aligned}.
$$

The study of the second-order terms of $G\{Q\}$ is the same as spin models since there is no coupling among different component pairs. Repeating the same procedure as for spin models, we obtain $\lambda_Q = \alpha \beta^2/(1 + \beta X_1)^2$ [9, 10]. In this way, we obtain the marginally stable condition given by

$$
1 - 2 \lambda_\Lambda \lambda_Q = 0.
\tag{25}
$$

Note that the factor 2 comes from the largest eigenvalue $\epsilon_0$ as discussed in appendix C.

The energy obtained by the dynamical one-step RSB solution are presented in figures for $\alpha = 0.3, 0.5$ as well as those obtained by high-temperature expansion and simulation results, which will be described in the following section. The behavior of dynamical RSB is similar to that of the spin models. The transition temperature $T_g$ is given by the temperature where the saddle point equations and (25) have the solution with $m = 1$. At this temperature, $q_1$ is very close to 1 and increases to 1 as the temperature decreases, while $m$ decreases to 0. The energy obtained by dynamical RSB does not change much below $T_g$ but starts to decrease at lower temperature.

![](./images/812711034237222912_1.jpg)

Figure 1. Temperature dependence of energy obtained by several methods for $\alpha = 0.3$. Full line shows the high-temperature expansion. Broken line shows the RSB with marginally stable condition, where $T_g$ is 0.0243 and $e$ at $T_g$ is $-0.0732$. Points with error bars are averages and standard deviations obtained by five runs of simulated annealing for $(P, N) = (30, 100)$. MC steps for each temperature is 100 and 1000 from top.

## 5. The results of simulated annealing

In the previous section, we found that the replica solution of the glass matrix model is quite similar to that of the glassy spin models, although we have introduced several approximations to obtain the results. Firstly, the calculation was performed to the lowest order of $\alpha$. Secondly, the saddle point variables are assumed to be independent of component indices. To see the validity of these approximations, the comparison with simulation results will be important.

This section is devoted to the presentation of simulation results. We are interested in the dynamical phase transition temperature $T_g$, which should be identified by the change of dynamical property and temperature dependence of energy. Spin variables are assumed to obey the Monte Carlo (MC) dynamics, where flips of components are performed sequentially according to the probabilities controlled by the change of energy $\Delta E$, that is, $\min[1, \exp(-\beta\Delta E)]$. To compare with the results of the replica study, we restrict ourselves to small $\alpha$.

In figures 1 and 2, the results obtained by simulated annealing are presented for $\alpha = 0.3$ and $0.5$. The energy obtained by high-temperature expansion varies from 0 to $-\alpha/4$ as temperature decreases. Note that the scale of energy and temperature is very small in these figures, implying that the transitions take place at rather low temperature. We note that the energy by high-temperature expansion looks rather good even for $\alpha = 0.5$. We can see that the next-order term of $\alpha$ is also higher order of $T$. Basically, the energy obtained by simulated annealing decreases as the temperature decreases in the high-temperature region according to the high-temperature energy and ceases to decrease around a certain temperature, which is much higher than $T_{\text{RSB}}$, but close to $T_g$. Around this temperature, the acceptance rate of spin flips decreases drastically. This means that the dynamical property changes drastically around this temperature. The resulting configurations seem to be random and uncorrelated. These aspects are common in glassy models such as the random orthogonal model [9], the AH model [10] and LRAF [11, 12].


![](./images/812711034237222912_2.jpg)

Figure 2. Same as figure 1 but $\alpha=0.5$, where $T_g$ is 0.0445 and $e$ at $T_g$ is $-0.1197$. Simulated annealing is performed for $(P,N)=(40,80)$.

In figures, two types of annealing schedule are presented to show that the resulting energies depend on the schedule. By increasing the number of MC steps at each temperature, the resulting energy decreases slightly at least for the studied MC steps. As in figure 1, we often observe that the energy starts to decrease rapidly slightly above $T_g$ and becomes rather low, much lower than the energy obtained by replica method for $T<T_g$. We suppose that, as discussed in [13], there are crystal-like configurations with rather low energy. We also note that there are an absolute minimum state and slightly disturbed states with very low energies, as expected by static RSB solution. These configurations may affect the simulated annealing for the studied system sizes. They will exist but will be difficult to be found by simulated annealing for larger systems.

To summarize, the dynamical transition temperature obtained by the replica method is consistent with the simulation results. However, the energies obtained by simulated annealing have some spectrum depending on the annealing schedule, implying rich low-temperature phase. The replica solution presented in this paper does not seem to cover these aspects.

## 6. Discussion

In this paper, we have studied the glass matrix model by the replica method, which is defined by using a transformations common to all replicas. The glass matrix model is defined by the inner products of $P$-component spin variables and is similar to the particle model in the sense that it has a high-dimensional one-particle state. We restricted ourselves to small $\alpha=P/N$, where the high-temperature expansion is given by one-loop diagrams, as in the spin models. The replica theory also becomes similar to that of the spin models if we assume the homogeneity of the component space. By studying the fluctuation modes around the saddle point, we found the marginality condition to identify the dynamical transition. The results of simulated annealing is consistent with the dynamical phase transition determined by the replica theory.

By comparing the replica result and simulation, we note that the simulation results seem much richer than the replica solution we presented in this paper. In the simulated annealing, the resulting energies depend on the annealing schedule at least in the studied MC steps. As

the decrease of temperature becomes slow, the states with lower energy appear. This aspect is quite natural as a glass model since the marginally stable condition simply gives a boundary of the region where pure states exist. Having some idea on the transition temperature, direct study of dynamics at low temperature will be a quite interesting subject.

The existence of a parameter $\alpha$ is an interesting aspect of LRAF and glass matrix model. Roughly speaking, $\alpha$ is a ratio between the number of constraint terms and the number of degrees of freedom. In these models, the one-loop contribution to free energy is proportional to $\alpha \ln \beta$. Consequently, $T_s$ is proportional to $\exp(-c/\alpha)$ for small $\alpha$. By disregarding the higher order terms of $\alpha$, the description by two-replica order parameter becomes possible as in the AH model. On the other hand, unlike the AH model, there are higher order terms of $\alpha$ for the studied deterministic models. These contributions induce order parameters with more than two replica indices. The study of the exact solution, including these contributions, will be an interesting problem.

The energy function we have studied may be the simplest one in the glass matrix model. Among some variations, the model with hard sphere particles and continuous dynamical variables sounds interesting in various aspects [17]. For continuous variables, we cannot use the argument of negative entropy to find phase transition. We also expect that the replica method in this paper should be modified to cope with the continuous variables. The study of these problems sounds quite challenging and will give a fruitful insight into glassy states.

## Acknowledgments
The author is grateful to referees for the variable comments.

## Appendix A
In this appendix, we present another derivation of the action (13). We first discuss the high-temperature expansion to the lowest order of $\alpha$. The energy function is written as

$$
H=\frac{1}{2} \sum_{a<b} g\left(\frac{1}{\sqrt{N}} \sum_{i=1}^{N} S_{i}^{a} S_{i}^{b}\right)-\frac{1}{4} P^{2} \tag{A.1}
$$

with $g(x)=x^{2}$. In the following, we omit the constant terms in $H$ for simplicity. Introducing $1=\int \mathrm{d} \phi \delta(\phi-x)$ and integral representation for the delta-function, the partition function is written as

$$
Z=\prod_{a<b} \int \frac{\mathrm{d} \bar{\phi}_{a b} \mathrm{~d} \phi_{a b}}{2 \pi \sqrt{-1}} \exp \left(-\frac{\beta}{2} \sum_{a<b} g\left(\phi_{a b}\right)\right) \exp \left(\sum_{a<b} \bar{\phi}_{a b} \phi_{a b}+\ln \Phi\right), \tag{A.2}
$$

where

$$
\Phi=\sum_{\{S\}} \prod_{i} \exp \left(-\frac{1}{\sqrt{N}} \sum_{a<b} \bar{\phi}_{a b} S_{i}^{a} S_{i}^{b}\right).
$$

Due to the factor $1 / \sqrt{N}, \Phi$ can be expanded in terms of $\alpha=P / N$. To the lowest order, we obtain

$$
\ln \Phi \sim \frac{1}{2} \sum_{a<b} \bar{\phi}_{a b}^{2}+P N \ln 2. \tag{A.3}
$$

Performing the Gaussian integral, we obtain

$$
\ln Z / P N \sim-\frac{1}{4} \alpha \ln (1+\beta)+\ln 2. \tag{A.4}
$$

Note that the higher order terms of $\bar{\phi}_{a b}$ in $\ln \Phi$ give the higher order terms of $\alpha$ in $\ln Z / P N$.

To obtain $Z^n$ given by (13), we introduce $n$ replicas for all integral variables and denote them by $\phi_{ab}^{\alpha}, \overline{\phi}_{ab}^{\alpha}$ and $S_i^{a\alpha}$. Then we perform the transformation $S_i^{a\alpha} \to \eta_i^a S_i^{a\alpha}$ in $\Phi^n$, followed by the sum over $\eta_i^a = \pm 1$. Then we have

$$
Z^n = \prod_{\alpha,a<b} \int \frac{\mathrm{d}\overline{\phi}_{ab}^{\alpha} \mathrm{d}\phi_{ab}^{\alpha}}{2\pi\sqrt{-1}} \exp\left(-\frac{\beta}{2} \sum_{a<b} g(\phi_{ab}^{\alpha})\right) \exp\left(\sum_{a<b} \overline{\phi}_{ab}^{\alpha}\phi_{ab}^{\alpha} + \ln \Phi^n\right), \tag{A.5}
$$

where

$$
\Phi^n = \frac{1}{2^{PN}} \sum_{\{\eta\}} \sum_{\{S^a\}} \prod_i \exp\left(-\frac{1}{\sqrt{N}} \sum_{a<b} \eta_i^a \eta_i^b K_{ab,i}\right)
$$

with

$$
K_{ab,i} = \sum_{\alpha=1}^n \overline{\phi}_{ab}^{\alpha} S_i^{a\alpha} S_i^{b\alpha}.
$$

To the lowest order of $\alpha$, we have

$$
\Phi^n \sim \sum_{\{S^a\}} \exp\left(\frac{1}{2} \sum_{a<b} \sum_{\alpha\beta} \overline{\phi}_{ab}^{\alpha} \overline{\phi}_{ab}^{\beta} Q_{ab}^{\alpha\beta}\right), \tag{A.6}
$$

where $Q_{ab}^{\alpha\beta}$ are defined by (12). Since $g(x) = x^2$, integrals over $\phi$ and $\overline{\phi}$ in $Z^n$ are Gaussian, and we obtain the expression (13). We should note that, in the higher order of $\alpha$, there arise couplings among different component pairs and more than two replica indices in (A.6).

## Appendix B

In this appendix, we describe the derivation of the one-step RSB free energy. In the one-step RSB ansatz, $Q^{\alpha\beta}$ has eigenvalues $X_n = 1 - Q_1 + m(Q_1 - Q_0) + nQ_0$, $X_m = 1 - Q_1 + m(Q_1 - Q_0)$ and $X_1 = 1 - Q_1$ with degeneracy $1, n/m - 1$ and $n - n/m$, respectively. Then using (14) and (18), we obtain

$$
\begin{aligned}
\ln Z^n =& -\frac{1}{4} P(P - 1) \left\{\ln(1 + \beta X_n) + \left(\frac{n}{m} - 1\right)\ln(1 + \beta X_m) + \left(n - \frac{n}{m}\right)\ln(1 + \beta X_1) - n\beta\right\} \\
& -\frac{1}{4} N(P - 1)\{n(n - m)\Lambda_0 Q_0 + n(m - 1)\Lambda_1 Q_1\} - F\{\Lambda\}, \tag{B.1}
\end{aligned}
$$

where

$$
\begin{aligned}
F\{\Lambda\} =& -\frac{1}{4} N P\left\{n(n - m)q_0^2 \Lambda_0 + n(m - 1)q_1^2 \Lambda_1\right\} \\
& -\frac{1}{2} n N P q_1 \Lambda_1 + N P \ln \int \left(\int (2\cosh A)^m D y\right)^{\frac{n}{m}} D x,
\end{aligned}
$$

where $A = \sqrt{q_0 \Lambda_0}x + \sqrt{q_1 \Lambda_1 - q_0 \Lambda_0}y$. By taking the limit $n \to 0$, we obtain (19).

Let us calculate the low-temperature expression of the last term in $\beta f$, which is given by

$$
\beta \Delta f = \frac{1}{m} \int D x \ln \int D y(2\cosh A)^m. \tag{B.2}
$$

For the simplicity, we assume $q_0 = 0$. For large $\beta$, $2\cosh A$ is approximated to be $\exp|A|$. Then the integral over $y$ is given by $2\exp(m^2 q_1 \Lambda_1 /2)$. Using this expression and setting $q_0 = 0, q_1 = 1$ in (19), we obtain the free energy (21).

### Appendix C

In this appendix, we study the fluctuation modes of the action. Setting $\Lambda_{ab}^{\alpha\beta} = \Lambda^{\alpha\beta} + \delta\Lambda_{ab}^{\alpha\beta}$ and $Q_{ab}^{\alpha\beta} = Q^{\alpha\beta} + \delta Q_{ab}^{\alpha\beta}$ and keeping the second-order terms in the exponent of (14), which is denoted by $\delta^2 A$, we have

$$
\begin{aligned}
\delta^2 A = \frac{1}{2} & \sum_{a<b,(\alpha\beta)(\gamma\delta)} G_{(\alpha\beta)(\gamma\delta)} \delta Q_{ab}^{\alpha\beta} \delta Q_{ab}^{\gamma\delta} + \frac{N}{P} \sum_{a<b} \sum_{(\alpha\beta)} \delta \Lambda_{ab}^{\alpha\beta} \delta Q_{ab}^{\alpha\beta} \\
& + \frac{N}{2P^2} \left( \sum_{a<b} \sum_{(\alpha\beta)(\gamma\delta)} \delta \Lambda_{ab}^{\alpha\beta} \delta \Lambda_{ab}^{\gamma\delta} \bar{A}_{(\alpha\beta)(\gamma\delta)} + \sum_{a,b\neq a,c\neq a} \sum_{(\alpha\beta)(\gamma\delta)} \delta \Lambda_{ab}^{\alpha\beta} \delta \Lambda_{ac}^{\gamma\delta} B_{(\alpha\beta)(\gamma\delta)} \right),
\end{aligned}
$$

where

$$
G_{(\alpha\beta)(\gamma\delta)} = \frac{\partial^2 G(Q)}{\partial Q_{ab}^{\alpha\beta} \partial Q_{ab}^{\gamma\delta}}, \tag{C.1}
$$

with $G(Q) = \sum_{a<b} \text{Tr}\ln(1+\beta \mathbf{Q}_{ab})/2$ and $\bar{A}_{(\alpha\beta)(\gamma\delta)} = A_{(\alpha\beta)(\gamma\delta)} - 2B_{(\alpha\beta)(\gamma\delta)}$.

First we discuss the component space. Let us set $\delta \Lambda_{ab}^{\alpha\beta} = \sum_I \delta \Lambda_I^{\alpha\beta} \psi_{ab}^{(I)}, \delta Q_{ab}^{\alpha\beta} = \sum_I \delta Q_I^{\alpha\beta} \psi_{ab}^{(I)}$ and find the normalized vectors such that $\sum_{a<b} \psi_{ab}^{(I)} \psi_{ab}^{(I')} = \delta_{I'}$ and $\sum_{a,b\neq a,c\neq a} \psi_{ab}^{(I)} \psi_{ac}^{(I')} = \epsilon_I \delta_{II'}$. The second equation is to diagonalize the matrix in the component space. The simplest mode is given by $\psi_{ab}^{(0)} = (P(P-1)/2)^{-1/2}$, i.e. homogeneous mode with degeneracy 1. This mode gives $\epsilon_0 \sim 2P$. There are two kinds of mode which are orthogonal to $\psi_{ab}^{(0)}$. One is defined by $\psi_{kb}^{(1)} = x, \psi_{ab}^{(1)} = y$ for arbitrary $k$ and $a, b \neq k$. We have $2x+(P-2)y=0, \sum_b \psi_{kb}^{(1)} = (P-1)x$ and $\sum_b \psi_{ab}^{(1)} = x+(P-2)y=-x$ for $a \neq k$. Using these relations, we have $\epsilon_1 \sim P$ with degeneracy $P-1$. Note that these modes are not orthogonal to each other. This will not matter in the following argument. The third modes are defined by $\sum_b \psi_{ab}^{(2)} = 0$ for all $a$. This mode gives $\epsilon_2=0$ with degeneracy $P(P-3)/2$. By using these eigenmodes, we write

$$
\delta^2 A / NP = \frac{1}{2} \sum_I \left( \delta Q_I \delta \Lambda_I \right) \begin{pmatrix} \alpha \mathbf{G} & 1 \\ 1 & \mathbf{K}_I \end{pmatrix} \begin{pmatrix} \delta Q_I \\ \delta \Lambda_I \end{pmatrix}, \tag{C.2}
$$

where $\mathbf{K}_I$ is given by $\bar{\mathbf{A}}/P$ for $I=2$ and $(\epsilon_I/P)\mathbf{B}$ for $I=0,1$. Then we can discuss the eigenmodes in the replica space for each $I$. The matrices $\mathbf{G}, \mathbf{A}$ and $\mathbf{B}$ are diagonalized by the eigenvectors which have the same structure in replica space. This problem was well studied in spin models [15, 16]. They are replaced by the eigenvalues for the corresponding eigenvectors. The eigenvectors of $\mathbf{G}$ and $(\epsilon_I/P)\mathbf{B}$(or $\bar{\mathbf{A}}/P$) are mixed by the off-diagonal terms in $(\delta Q, \delta \Lambda)$. Apparently, eigenmodes $I=2$ do not become marginally stable since $\bar{\mathbf{A}}/P \to 0$ for $P \to \infty$. Thus we restrict ourselves to $I=0,1$.

For the replicon modes, $\alpha \mathbf{G}$ is replaced by $\lambda_Q = \alpha \beta^2/(1+\beta X_1)^2$ [9, 10] and $\mathbf{B}$ is replaced by $\lambda_\Lambda = q_1^2 \overline{(1-\langle S\rangle^2)^2}$. By replacing $\delta \Lambda \to \sqrt{-1} \delta \Lambda$, we obtain the product of two eigenvalues $1-(\epsilon_I/P)\lambda_\Lambda \lambda_Q$ for replicon modes in $(\delta Q_I, \delta \Lambda_I)$. Since the second term in this expression is smaller than 1 in paramagnetic phase and increases as temperature decreases, the largest eigenvalue $\epsilon_0 \sim 2P$ should be chosen in front of $\lambda_\Lambda$ to give the marginally stable mode.

Let us remark on the contribution of Gaussian integrals of eigenmodes to the action. The number of the eigenmode $I=0$ is of order 1 and they do not modify the leading term of the action. The number of the eigenmodes $I=1$ is of order $P$ and they also do not modify the leading term of the action. The number of modes $I=2$ is the same order of action, $P^2$. However, they do not contribute to the leading term of action since these

eigenvalues have the form $1 - c/P$ with a constant $c$ of order 1 and the contribution is given by $P^2 \ln(1 - c/P) \sim cP$, which is the next order of $P$.

## References

[1] Barrat J L *et al* (ed) 2002 Slow Relaxation and non-equilibrium dynamics in condensed matter, Les Houches

[2] Sompolinsky H and Zippelius A 1982 *Phys. Rev.* B **25** 6860

[3] Horner H 1992 *Z. Phy.* B **86** 291

[4] Cugliandolo L F and Kurchan J 1993 *Phys. Rev. Lett.* **71** 173

[5] Mézard M, Parisi G and Virasoro M A 1987 *Spin Glass Theory and Beyond* (Singapore: World Scientific)

[6] Monasson R 1995 *Phys. Rev. Lett.* **75** 2847

[7] Franz S, Mézard M, Parisi G and Pliti L 1998 *Phys. Rev. Lett.* **81** 1758

[8] Marinari E, Parisi G and Ritort F 1994 *J. Phys. A: Math. Gen.* **27** 7615

[9] Marinari E, Parisi G and Ritort F 1994 *J. Phys. A: Math. Gen.* **27** 7647

[10] Nokura K 1998 *J. Phys. A: Math. Gen.* **31** 7447

[11] Nokura K 2002 *J. Phys. A: Math. Gen.* **35** 4973

[12] Nokura K 2002 *J. Phys. A: Math. Gen.* **35** 8013

[13] Cugliandolo L F, Kurchan J, Parisi G and Ritort F 1995 *Phy. Rev. Lett.* **74** 1012

[14] Amit D J, Gutfreund H and Sompolinsky H 1987 *Ann. Phys.* **173** 30

[15] Temesvari T, De Dominicis C and Kondor I 1994 *J. Phys. A: Math. Gen.* **27** 7569

[16] Brunetti R, Parisi G and Ritort F 1992 *Phys. Rev.* B **46** 5339

[17] Cugliandolo L F, Kurchan J, Monasson R and Parisi G 1996 *J. Phys. A: Math. Gen.* **29** 1347