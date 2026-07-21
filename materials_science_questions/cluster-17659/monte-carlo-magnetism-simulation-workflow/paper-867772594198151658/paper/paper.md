
# Islands of equilibrium in a dynamical world

David Saad and Alexander Mozeika

The Non-linearity and Complexity Research Group, Aston University, Birmingham B4 7ET, UK. (Dated: October 31, 2018)

Many natural, technological and social systems are inherently not in equilibrium. We show, by detailed analysis of exemplar models, the emergence of equilibrium-like behavior in localized or non-localized domains within non-equilibrium systems as conjectured in some real systems. Equilibrium domains are shown to emerge either abruptly or gradually depending on the system parameters and disappear, becoming indistinguishable from the remainder of the system for other parameter values. The models studied, defined on densely and sparsely connected networks, provide a useful representation of many real systems.

PACS numbers: 05.70.Ln, 64.60.aq, 05.40.-a, 05.45.-a

Equilibrium is a fundamental concept in statistical physics  \( [1] \) ; it assumes that while the system dynamics is governed by microscopic interactions, some systems eventually reach a state where macroscopic observables remain unchanged. The evolution of such systems is driven by the corresponding Hamiltonian energy function and their states converge to the equilibrium distribution which is a function of energy only; all macroscopic properties of the system then follow from this distribution.

The dynamics of a non-equilibrium system, on the other hand, is typically not governed by a process derived from a Hamiltonian and such systems do not converge to an equilibrium state  \( [2, 3] \) . This is assumed to be true for many real systems, for instance in the financial, social and biological areas. However, constituents of some of these systems exhibit equilibrium-like behavior in emerging localized or non-localized domains; notable examples of this behavior are the emergence of equilibrium-like structures in functional brain networks  \( [4] \) , neuronal dynamics  \( [5] \)  and the theory of markets  \( [6] \) . Consequently, such domains may exist under some conditions within many other non-equilibrium systems but are difficult to identify.

Most systems in statistical physics fall into one of these two categories  \( [7] \) ; the evolution of both equilibrium and non-equilibrium systems (in discrete time steps) is characterized by a trajectory  \( \mathbf{s}(0)\to\cdots\to\mathbf{s}(t) \) , where  \( \mathbf{s}(t) \)  is a microscopic state of the system (microstate) at time t. For Markovian processes this probability can be decomposed to a chain of transition probabilities from one time step to the next resulting in the joint probability

 \[ \begin{aligned}\mathrm{P}[\mathbf{s}(0)\rightarrow\cdots\rightarrow\mathbf{s}(t)]=\\ \mathrm{W}[\mathbf{s}(t)|\mathbf{s}(t-1)]\times\cdots\times\mathrm{W}[\mathbf{s}(1)|\mathbf{s}(0)]\mathrm{P}(\mathbf{s}(0)),\end{aligned} \quad (1) \] 

with initial  \( \mathrm{P}(\mathbf{s}(0)) \)  and transition  \( \mathrm{W}[\mathbf{s}(t)|\mathbf{s}(t-1)] \)  probability distributions. Expectation value of any macroscopic observable  \( M(\mathbf{s}(t)) \) , i.e., a function of microstates defining a macrostate, can be computed from the probability distribution (1). Unfortunately, even for highly stylized models of statistical physics this procedure is non-trivial [8]. In equilibrium systems, one assumes that the probability of any microscopic trajectory is invariant under time-reversal; this leads to a property termed detailed balance for the stationary distribution  \( \mathrm{P}_{\infty}(\mathbf{s}) \)  of process (1), where transitions from state s to  \( \hat{s} \)  are balanced by transitions in the opposite direction  \( \mathrm{W}[\hat{\mathbf{s}}|\mathbf{s}]\mathrm{P}_{\infty}(\mathbf{s})=\mathrm{W}[\mathbf{s}|\hat{\mathbf{s}}]\mathrm{P}_{\infty}(\hat{\mathbf{s}}) \) . For thermodynamic systems, this gives rise to the Gibbs-Boltzmann distribution  \( \mathrm{P}_{\infty}(\mathbf{s})\propto\mathrm{e}^{-\frac{1}{k_{B}T}E(\mathbf{s})} \) , with temperature T, Boltzmann constant  \( k_{B} \)  (we set  \( k_{B}=1 \)  for convenience) and Hamiltonian (or energy) function  \( E(\mathbf{s}) \) , which usually follows from the transition probability  \( \mathrm{W}[\mathbf{s}|\hat{\mathbf{s}}] \)  [9]. The stationary distributions in systems without detailed balance (when such distributions do exist) are generally much more complicated and difficult to analyze [2, 3].

In the absence of explicit time dependence, equilibrium systems therefore admit a reduced representation with respect to non-equilibrium ones, via the macrostates of the relevant (energy) functions. Some non-equilibrium physical systems show a local equilibrium-like behavior (e.g., having a slowly changing temperature) that allows for a similar reduced representation  \( [7] \) ; however, this requires full knowledge of the corresponding Hamiltonian, which is completely unknown in many systems, especially in biological, financial and technological systems.

In past studies equilibrium and non-equilibrium systems analyses were typically well separated. In this Letter we show that in a large class of non-equilibrium systems, without detailed balance, one can still find domains that exhibit equilibrium-like  \( [22] \)  behavior; these may be of a non-localised nature and may emerge and disappear depending on external conditions. In order to demonstrate this we study two exemplar models where one may intuitively anticipate this type of behavior to occur, and equally importantly, can quantitatively analyse it.

The two models considered here are Ising-like systems comprising N spins  \( s_{i} \in \{-1,1\} \) ,  \( i \in \{1,\ldots,N\} \) , representing variables (degrees of freedom) interacting on sparsely and densely connected networks. This type of system is commonly used in statistical physics as a prototype and a first approximation in modelling complex phenomena in many-body systems [10]. In the densely connected model each variable interacts with a very large (order of the system size) number of variables whereas in the sparse model the number of interactions is much smaller than that of the system size. Furthermore, both
 

models have bipartite topologies where one part of the network serves as a non-equilibrium “environment” while the other is designed to be in equilibrium when considered on its own.

Densely connected model: This model, described schematically in Figure 1(a), is governed by the process (1) where the microstate  \( \mathbf{s}(t) = (\sigma_{1}(t), \ldots, \sigma_{N^{\sigma}}(t), \tau_{1}(t), \ldots, \tau_{N^{\tau}}(t)) \)  is represented for clarity by two components consisting of  \( N^{\sigma} \)  and  \( N^{\tau} \)  extensive degrees of freedom, respectively, such that  \( N^{\sigma} + N^{\tau} = N \) ; the distinction between the two subsystems is not obvious through interaction strengths. The  \( \tau \) -component of the system ( \( \tau \) -system), drives the  \( \sigma \) -component ( \( \sigma \) -system) via stochastic alignment of spins  \( \{\sigma_{i}\} \)  to the corresponding local fields  \( h_{i}(\sigma, \tau) = \sum_{j \neq i}^{N^{\sigma}} J_{ij}^{\sigma} \sigma_{j} + \sum_{j}^{N^{\tau}} J_{ij}^{\sigma} \tau_{j} + \theta_{i}^{\sigma} \)  and is itself governed by the stochastic alignment of  \( \{\tau_{i}\} \)  to the local fields  \( g_{i}(\sigma, \tau) = \sum_{j}^{N^{\sigma}} J_{ij}^{\tau} \sigma_{j} + \sum_{j \neq i}^{N^{\tau}} J_{ij}^{\tau} \tau_{j} + \theta_{i}^{\tau} \) , where the variables  \( \{J_{ij}^{\sigma}, J_{ij}^{\tau}, J_{ij}^{\sigma}, \tau_{j}^{\tau}\} \)  prescribe the strengths of the various interactions and  \( \{\theta_{i}^{\sigma}, \theta_{i}^{\tau}\} \)  are external fields which may depend on time. Each site in the  \( \sigma \) -system ( \( \tau \) -system) is updated in a stochastic manner with the probabilities  \( \mathrm{P}[\sigma_{i}(t+1)] \propto \exp[\beta \sigma_{i}(t+1) h_{i}(\sigma(t), \tau(t))] \)  and  \( \mathrm{P}[\tau_{i}(t+1)] \propto \exp[\beta \tau_{i}(t+1) g_{i}(\sigma(t), \tau(t))] \) , respectively, which are controlled by the noise parameter  \( \beta \)  (that defines the temperature  \( T = 1/\beta \) ); the dynamics is completely deterministic when  \( \beta \to \infty \)  and is completely random when  \( \beta = 0 \) . All sites are updated independently of each other, which leads to the Markov process (1).

It is clear from the definitions of the fields that the two systems evolve independently and separately when all cross-component interactions  \( J_{ij}^{\sigma\tau} = J_{ij}^{\tau\sigma} = 0 \) . If in addition all  \( J_{ij}^{\sigma\tau} \)  are symmetric, i.e.  \( J_{ij}^{\sigma\tau} = J_{ji}^{\sigma} \) , and all external fields  \( \theta_{i}^{\sigma}(t) \)  do not depend on time, then the  \( \sigma \) -system is governed by the equilibrium distribution  \( \mathrm{P}_{\infty}(\sigma) \propto \mathrm{e}^{-\beta E_{\beta}(\sigma)} \)  with Peretto's [9] pseudo-Hamiltonian

 \[ E_{\beta}(\sigma)=-\frac{1}{\beta}\sum_{i=1}^{N^{\sigma}}\log2\cosh[\beta h_{i}(\sigma,0)]-\sum_{i=1}^{N^{\sigma}}\theta_{i}^{\sigma}\sigma_{i}. \quad (2) \] 

For asymmetric cross-component interactions  \( J_{ij}^{\sigma\tau} \neq 0 \)  or  \( J_{ij}^{\tau\sigma} \neq 0 \)  the complete system is not in equilibrium. However, this does not prevent the  \( \sigma \) -system from exhibiting equilibrium-like behavior. To see this we consider the simplest case of  \( J_{ij}^{\sigma} = J_{ij}^{\sigma\tau} = 1 \)  and  \( J_{ij}^{\tau} \neq J_{ji}^{\tau} \) , where both interaction variables  \( J_{ij}^{\tau} \)  and  \( J_{ij}^{{\tau}\sigma} \)  are independent random variables and are assigned values of  \( \pm 1 \)  with equal probability; to simplify the example we will also choose  \( N^{\sigma} = N^{\tau} = N/2 \)  [23].

We employ the method of generating functional analysis to obtain expectation values of various macroscopic quantities, averaged over the quenched disordered induced by the randomly assigned values of  \( J_{ij}^{\tau} \)  and  \( J_{ij}^{{\tau}\sigma} \) . It turns out that in this case the complete system admits a macroscopic description via the magnetizations  \( m^{\sigma}(\sigma(t)) = \frac{1}{N^{\sigma}} \sum_{i=1}^{N^{\sigma}} \sigma_{i}(t) \)  and  \( m^{\tau}(\tau(t)) = \frac{1}{N^{\tau}} \sum_{i=1}^{N^{\tau}} \tau_{i}(t) \) . In particular, for the magnetizations averaged over the process,  \( m^{\sigma}(t) = \langle m^{\sigma}(\sigma(t))\rangle \) ,  \( m^{\tau}(t) = \langle m^{\tau}(\tau(t))\rangle \) , and in the thermodynamic limit  \( N \to \infty \) , one obtains

 \[ \begin{aligned}&m^{\sigma}(t+1)=\tanh\beta[m^{\sigma}(t)+m^{\tau}(t)+\theta^{\sigma}(t)]\\&m^{\tau}(t+1)=0\\ \end{aligned} \quad (3) \] 

with initial conditions given by  \( m^{\sigma}(0) \)  and  \( m^{\tau}(0) \) . For  \( \theta^{\sigma}(t)=\theta^{\sigma} \)  and  \( \theta^{\tau}=0 \)  this equation admits a stationary solution  \( m^{\sigma}(\infty)=\tanh[\beta(m^{\sigma}(\infty)+\theta^{\sigma})] \)  which is exactly the same as one finds in equilibrium [11] governed by (2). Similar argument also holds for the average density  \( -\frac{1}{N^{\sigma}}\frac{1}{\beta}\sum_{i=1}^{N^{\sigma}}\log2\cosh[\beta h_{i}(\sigma,\tau)]-\theta^{\sigma}\frac{1}{N^{\sigma}}\sum_{i=1}^{N^{\sigma}}\sigma_{i} \) , which approaches the equilibrium energy (2) and is a function of the magnetization only. Furthermore, for  \( \theta^{\sigma}=0 \)  the stationary solution  \( m^{\sigma}(\infty)=0 \)  (disordered phase) is stable when  \( \beta<1 \)  but bifurcates into two solutions  \( |m^{\sigma}(\infty)|\neq0 \)  (ordered phase) at  \( \beta=1 \) . Thus both parts of the system are indistinguishable when  \( \beta<1 \) .

While we deliberately focussed on a particularly simple and tractable model, more complex systems of similar characteristics could be constructed to demonstrate the existence of equilibrium-like domains in a non-equilibrium environment.

Sparsely connected model: The model considered here is a sparsely connected Ising ferromagnetic system defined on an N-node random regular graph where each node is randomly connected to exactly  \( k \in O(N^{0}) \)  other nodes. The system evolves by selecting a node i with probability 1/N at each time step and aligning its state  \( \sigma_{i} \)  to the local field  \( h_{i}(\sigma) = J \sum_{j \in \partial i} \sigma_{j} \)  with probability proportional to  \( \mathrm{e}^{\beta \sigma_{i} h_{i}(\sigma)} \) , where  \( \partial i \)  is a set ( \( |\partial i| = k \) ) of sites directly connected to site i. This leads to a Markovian process in continuous time (see Appendix). Furthermore, a fraction p of (randomly selected) spins in this system are driven by the random time-dependent external fields  \( \theta_{i}(t) \in \{-1, 1\} \) , where  \( \mathrm{P}(\theta_{i}(t) = \pm 1) = 1/2 \) , i.e., in these sites the field  \( h_{i}(\sigma) \)  is effectively changed to  \( h_{i} (\sigma) + \theta_{i}(t) \) .

Without external fields and after long time  \( (t \to \infty) \)  the system is in thermal equilibrium and the spins are governed by the Gibbs-Boltzmann distribution with the Hamiltonian  \( E(\sigma) = -J \sum_{\langle ij \rangle} \sigma_i \sigma_j \) . In the equilibrium the average energy and magnetization are given respectively by the equations

 \[ \begin{align*}E~&=~-\frac{1}{2}k\frac{\tanh(\beta J)+\tanh(\beta h)^{2}}{1+\tanh(\beta J)\tanh(\beta h)^{2}}\\m~&=~\tanh\{\tanh^{-1}[\tanh(\beta J)\tanh(\beta h)]k\}~,\end{align*} \] 

respectively, where h is a solution of  \(  h = \frac{1}{\beta}(k - 1)\tanh^{-1}[\tanh(\beta J)\tanh(\beta h)]  \)  [12]. The system is in an ordered (disordered) state if  \( T < T_{c} \)  ( \( T > T_{c} \) ), with  \( T_{c} = J/\tanh^{-1}\frac{1}{k-1} \)  being the critical temperature of the system. In the presence of time-dependent external fields convergence to thermal equilibrium is no longer guaranteed, but part of the system, which is not directly affected by the external fields, can exhibit equilibrium-like behavior as can be seen in Figure 1(b). This phenomena,
 
![](./images/867772594198151658_1.jpg)

(b)

![](./images/867772594198151658_2.jpg)

![](./images/867772594198151658_3.jpg)

![](./images/867772594198151658_4.jpg)

FIG. 1: (a) Densely connected system composed of equilibrium ( \( \sigma \) -system, blue nodes) and non-equilibrium ( \( \tau \) -system, red nodes) components. Blue and red edges represent positive and negative interactions, respectively. Interaction directions are not shown. (b) Properties of sparse systems exhibiting equilibrium-like behavior. The degrees of freedom (blue nodes) are interacting on graphs with locally tree-like topology. A fraction of these nodes (red) are exposed to the changing environment (perturbations). Macroscopic observables of the un-perturbed nodes suggest they are in thermal equilibrium at low temperature as the influence of perturbations on the macroscopic observables is negligible (left - E panel); as one approaches a critical temperature, the system becomes very sensitive, develops long-range order and exhibits significant deviations from the equilibrium values of these observables (middle - NE panel). The transition point is determined by the point where deviation from the equilibrium values exceeds thermal fluctuations and represents an estimate. The perturbations become negligible again at the high temperature region as one moves away from the critical temperature  \( T_{c} \)  (right - E panel). This qualitative explanation is supported by comparing the equilibrium energy E (dashed line) and magnetization m (solid line) with the average energy  \( E(\sigma) = -\frac{1}{N} \sum_{\langle ij \rangle} \sigma_{i} \sigma_{j} \)  and magnetization densities  \( m(\sigma) = \frac{1}{N} \sum_{i=1}^{N} \sigma_{i} \)  measured in Monte Carlo simulations (symbols) of a ferromagnetic Ising spin system, defined on a random regular graph of size  \( N = 10^{6} \)  with k = 3, where a fraction p = 0.05 of sites are subject to the external time-dependent random binary fields  \( \theta_{i}(t) \in \{-1, 1\} \) , with  \( \mathrm{P}(\theta_{i}(t) = \pm 1) = 1/2 \) ; all Monte Carlo simulations results reported here have been carried out for a similar system size and connectivity degree. The measurements are taken only on sites not influenced by  \( \theta_{i}(t) \) . (c) Deviations from equilibrium, shown in NE panel of (b), are much larger than one usually finds due to thermal fluctuations alone in equilibrium. We compare thermal fluctuations of the equilibrium energy E (dashed line) and magnetization m (solid line) with those measured in Monte Carlo simulations (represented by symbols with error bars, much smaller than the symbol size, on the solid lines). The non-equilibrium simulation measurements (symbols with error bars) are taken only at sites not influenced by  \( \theta_{i}(t) \)  and show clear deviation from the equilibrium values. (d) Comparing the magnetization m (solid lines) calculated theoretically with values (symbols) measured in the Monte Carlo simulations of ferromagnetic Ising spin system defined on an asymmetric (an incoming edge with probability 1/2) random regular graph show good agreement between the two.

vanishes when the temperature T in the system is close to  \( T_{c} \) . The presence of this phase transition seems to magnify the non-equilibrium effect of an external driving field which is much larger than one usually finds due to the thermal fluctuations alone, in equilibrium, as can be seen in Figure 1(c). We note that similar behavior also occurs in a system defined on a Cayley tree where boundary sites are subject to the same external fields [13].

Alternatively, the  \( \theta_{i} \)  can be viewed as a field induced by a non-equilibrium part of the system. In the long time limit  \( t \to \infty \) , this system is equivalent to the setup where one part of the system (asymmetric) drives the other (symmetric). The sites affected by the asymmetric part are described by the set  \( \{m_{i}(t)\} \)  of local magnetizations  \( m_{i}(t) = \sum_{\sigma} \mathrm{P}_{i}(\sigma) \sigma_{i} \) . Furthermore, if the stationary point of these local magnetizations is exactly  \( m_{i}(t) = 0 \) , the asymptotic behavior of the system is equivalent to that of the system depicted in Figure 1(b).
 

To verify this we assume that for asynchronous dynamics on an asymmetric regular graph the local magnetization  \( m_{i}(t) \)  is a function of the local magnetizations  \( m_{j}(t) \)  of its neighbors  \( j \in \partial i \)  only. For k = 3 this leads to the following set of equations

 \[ \frac{\mathrm{d}}{\mathrm{d}t}m_{i}+m_{i}=\left\{\begin{array}{ll}(A+7\Gamma)\sum_{j\in\partial i}m_{j}&if|\partial i|=3\\\quad+6\Gamma\prod_{j\in\partial i}m_{j}&\\\frac{1}{2}\tanh(2\beta)\sum_{j\in\partial i}m_{j}&if|\partial i|=2\\\tanh(\beta)\sum_{j\in\partial i}m_{j}&if|\partial i|=1\\0&if|\partial i|=0\end{array}\right. \] 

where  \( A=(27\tanh(\beta)-\tanh(3\beta))/24 \)  and  \( \Gamma=(\tanh(3\beta)-3\tanh(\beta))/24 \) , which is valid for single instances of asymmetric regular graphs as can be seen in Figure 1(d).

Recent studies of neural populations [14], flocks of birds [15], magnets [16] and of many other natural and technological systems, suggest the existence of equilibrium domains in non-equilibrium systems. However, to show the emergence of such domains in practice may prove difficult, especially if they are composed of non-localized degrees of freedom; for instance, a group of traders located in different stock markets and aiming to maximize their profits may (possibly inadvertently) constitute an equilibrium-like system. This Letter aims to change our viewpoint on the traditional separation between equilibrium and non-equilibrium systems in order to understand the emergence of equilibrium behaviors within non-equilibrium systems and possibly facilitate control of this phenomenon. The exemplar models systematically analyzed here represent the first step towards this goal; they demonstrate the emergence of such domains and their dependence on various system parameters as well as their dissipation close to criticality. In the real world such systems may emerge randomly or evolve in a structured manner through a selection process. The study opens up exciting opportunities for future work on the role and dynamics of equilibrium domains in systems with adiabatically changing interactions and parameters, such as coordinated global trade and social networks.

## Acknowledgments

We would like to thank David Sherrington, Marc Mézard, David Lowe and Riccardo Zecchina for very helpful comments on the manuscript. This work is supported by the EU FET project STAMINA (FP7-265496) and the Leverhulme trust grant F/00 250/H.

## Appendix A: Processes on graphs

We consider a system of N Ising spins,  \( \sigma_{i} \in \{-1, 1\} \) , which are placed on the vertices of a graph and interact only when they are connected. Their microscopic dynamics are governed by a Glauber type stochastic algorithm where a spin on site i is flipped with probability

 \[ \mathrm{P}(\sigma_{i}\rightarrow-\sigma_{i})=\frac{\mathrm{e}^{-\beta\sigma_{i}h_{i}(\sigma)}}{2\cosh(\beta h_{i}(\sigma))}, \quad (A1) \] 

where  \( h_{i}(\sigma) \)  is a local field defined as

 \[ h_{i}(\sigma)=\sum_{j\in\partial i}J_{i j}\sigma_{j}+\theta_{i}, \quad (A2) \] 

with  \( \partial i \)  being the set of sites connected to site i and where we have used the notation  \( \sigma = (\sigma_{1}, \ldots, \sigma_{N}) \) . The parameter  \( \beta \)  controls the level of noise in the system; the dynamics is completely random when  \( \beta \rightarrow 0 \)  and completely deterministic when  \( \beta  \rightarrow \infty \) . The parameter  \( \theta_{i} \)  defines an external field. The set of variables  \( \{J_{ij}\} \)  prescribes the strengths of interactions between the spins. Once chosen these variables are kept fixed for the duration of the process.

In order to complete the above algorithm we have to specify how we choose the sites for each update according to (A1). A simplest choice is to update all sites simultaneously which gives rise to the parallel dynamics governed by the Markov equation (this type of dynamics is popular in the modeling of neural networks [11])

 \[ \mathrm{P}_{t+1}(\sigma)=\sum_{\sigma^{\prime}}W[\sigma|\sigma^{\prime}]\mathrm{P}_{t}(\sigma^{\prime}) \quad (A3) \] 

with the transition probability

 \[ \mathrm{W}[\sigma|\sigma^{\prime}]=\prod_{i=1}^{N}\frac{\mathrm{e}^{\beta\sigma_{i}h_{i}(\sigma^{\prime})}}{2\cosh(\beta h_{i}(\sigma^{\′}))}. \quad (A4) \] 

For the symmetric interactions, i.e.  \( J_{ij} = J_{ji} \) , the detailed balance property  \( \mathrm{W}[\sigma'|\sigma] \mathrm{P}(\sigma) = \mathrm{W}[\sigma|\sigma'] \mathrm{P}(\sigma') \)  is always satisfied. If in addition the ergodic property  \( (\exists t' \)  such that for  \( \forall t \geq t' \) :  \( \mathrm{P}_t(\sigma) > 0) \)  is satisfied then the process (A3) converges [9] to the equilibrium distribution

 \[ \mathrm{P}_{\infty}(\sigma)\propto\mathrm{e}^{-\beta E_{\beta}(\sigma)}, \quad (A5) \] 

where  \( E_{\beta}(\sigma) \)  is the pseudo-Hamiltonian (this is not a proper Hamiltonian because of its explicit dependence on the noise parameter  \( \beta \) )

 \[ E_{\beta}(\sigma)=-\frac{1}{\beta}\sum_{i=1}^{N}\log2\cosh(\beta h_{i}(\sigma))-\sum_{i=1}^{N}\theta_{i}\sigma_{i}. \quad (A6) \] 

A slightly more complicated scenario is when the sites of a system are updated asynchronously in the following manner: at each iteration of the algorithm a site i is drawn randomly and independently from the set  \( \{1,\ldots,N\} \)  of all sites then the spin  \( \sigma_{i} \)  of this site is updated with the probability (A1) (this is one of the main algorithms used to study the dynamics of Ising-type magnetic systems [17]). This process naturally leads to the Markov equation [18] in continuous time

 \[ \begin{align*}\frac{\mathrm{d}}{\mathrm{d}t}\mathrm{P}_{t}(\sigma)=\sum_{i=1}^{N}\big[\mathrm{P}_{t}(\sigma_{1},\ldots,\sigma_{i},\ldots,\sigma_{N})\mathrm{P}(\sigma_{i}\to\sigma_{i})(A7)\\-\mathrm{P}_{t}(\sigma_{1},\ldots,\sigma_{N})\mathrm{P}(\sigma_{i}\to-\sigma_{i})\big].\end{align*} \quad (A7) \]
 

As in the case of synchronous dynamics (A3) the process (A7) satisfies detailed balance only for symmetric interactions and it evolves towards the equilibrium Gibbs-Boltzmann distribution  \( \mathrm{P}_{\infty}(\sigma) \propto \mathrm{e}^{-\beta E(\sigma)} \) , with the Hamiltonian (or energy) function

 \[ E(\sigma)=-\sum_{\langle i j\rangle}J_{i j}\sigma_{i}\sigma_{j}-\sum_{i=1}^{N}\theta_{i}\sigma_{i} \quad (A8) \] 

(the first sum is over all edges in the graph), which is a unique stationary solution when the process (A7) is

ergodic.

## Appendix B: Dynamics of a densely connected model

## 1. Generating functional

In this section we study dynamics of a densely connected Ising spin system governed by the Markov process with the transition probability given by

 \[ \mathrm{W}[\sigma(t+1),\tau(t+1)|\sigma(t),\tau(t)]=\prod_{i=1}^{N^{\sigma}}\frac{\mathrm{e}^{\beta\sigma_{i}(t+1)h_{i}(\sigma(t),\tau(t))}}{2\cosh[\beta h_{i}(\sigma(t),\tau(t))]}\prod_{\ell=1}^{N^{\tau}}\frac{\mathrm{e}^{\beta\tau_{\ell}(t+1)}g_{\ell}(\sigma(t),\tau(t))}{2\cosh[\beta g_{\ell}(\sigma(t),\tau(t))]}, \quad (B1) \] 

where  \( h_{i}(\sigma,\tau)=\sum_{j\neq i}^{N^{\sigma}}J_{ij}^{\sigma}\sigma_{j}+\sum_{j}^{N^{\tau}}J_{ij}^{\sigma\tau}\tau_{j}+\theta_{i}^{\sigma} \)  and  \( g_{i}(\sigma,\tau)=\sum_{j}^{N^{\sigma}}J_{ij}^{\tau\sigma}\sigma_{j}+\sum_{j\neq i}^{N^{\tau}}J_{ij}^{\tau}\tau_{j}+\theta_{i}^{\tau} \) . The averages of various macroscopic quantities in this system can be conveniently computed from the generating function

 \[ \Gamma[\psi^{\sigma},\psi^{\tau}]=\left\langle\exp\left[-\mathrm{i}\sum_{t=0}^{t_{\mathrm{m a x}}}\left\{\sum_{i=1}^{N^{\sigma}}\psi_{i}^{\sigma}(t)\sigma_{i}(t)+\sum_{\ell=1}^{N^{\tau}}\psi_{\ell}^{\tau}(t)\tau_{\ell}(t)\right\}\right]\right\rangle, \quad (B2) \] 

where the average  \( \langle\cdots\rangle \)  is taken over the microscopic trajectories  \( \sigma(0),\tau(0)\to\cdots\to\sigma(t_{\mathrm{max}}),\tau(t_{\mathrm{max}}) \)  occurring with probability

 \[ \mathrm{P}(\sigma(0))\mathrm{P}(\tau(0))\prod_{t=0}^{t_{\mathrm{m a x}}-1}\mathrm{W}[\sigma(t+1),\tau(t+1)|\sigma(t),\tau(t)]. \quad (B3) \] 

Inserting into the generating function (B2) the following integral representations of  \( \delta \) -functions for all times t and site indices i

 \[ \begin{aligned}&\int\frac{\mathrm{d}h_{i}(t)\mathrm{d}\hat{h}_{i}(t)}{2\pi}\mathrm{e}^{\mathrm{i}\hat{h}_{i}(t)[h_{i}(t)-h_{i}(\sigma(t),\tau(t))]}=1\\&\int\frac{\mathrm{d}g_{i}(t)\mathrm{d}\hat{g}_{i}(t)}{2\pi}\mathrm{e}^{\mathrm{i}\hat{g}_{i}(t)[g_{i}(t)-g_{i}(\sigma(t),\tau(t))]}=1\end{aligned} \quad (B4) \] 

we obtain

 \[ \begin{align*}\Gamma[\psi^{\sigma},\psi^{\tau}]~=&\int\{\mathrm{d}h\mathrm{~d}\hat{h}\mathrm{~d}g\mathrm{~d}\hat{g}\}\exp\left[\mathrm{i}\sum_{t=0}^{t_{\max}-1}\left\{\hat{h}(t)\cdot h(t)+\hat{g}(t)\cdot g(t)\right\}\right]\\&\times\sum_{\{\sigma_{i}(t),\tau_{i}(t)\}}\exp\left[-\mathrm{i}\sum_{t=0}^{t_{\max}-1}\left\{\hat{h}(t)\cdot h(\sigma(t),\tau(t))+\hat{g}(t)\cdot g(\sigma(t),\tau (t))\right\}\right]\\&\times\mathrm{P}\big[\sigma(t_{\max}),\tau(t_{\max})\leftarrow\cdots\leftarrow\sigma(1),\tau(1)\big.\\&\quad\left.\left|h(t_{\max}-1),g(t_{\max}-1),\cdots,h(0),g(0)\right]\mathrm{P}(\sigma(0))\mathrm{P}(\tau(0))\right.\\&\left.\times\exp\left[-\mathrm{i}\sum_{t=0}^{t_{\max}}\left\{\psi^{\sigma}(t)\cdot\sigma(t)+\psi^{\tau}(t)\cdot\tau(t)\right\}\right],\right.\end{align*} \quad (B5) \]
 

 \[ \int\{\mathrm{d}h\mathrm{d}\hat{h}\mathrm{d}g\mathrm{d}\hat{g}\}=\prod_{t=0}^{t_{\mathrm{m a x}}-1}\left\{\prod_{i=1}^{N^{\sigma}}\left\{\int\frac{\mathrm{d}h_{i}(t)\mathrm{d}\hat{h}_{i}(t)}{2\pi}\right\}\prod_{\ell=1}^{N^{\tau}}\left\{\int\frac{\mathrm{d}g_{\ell}(t)\mathrm{d}\hat{g}_{\ell}(t)}{2\pi}\right\}\right\}, \quad (B6) \] 

 \[ \begin{aligned}&\mathrm{P}\left[\sigma(t_{\max}),\tau(t_{\max})\leftarrow\cdots\leftarrow\sigma(1),\tau(1)|h(t_{\max}-1),g(t_{\max}-1),\cdots,h(0),g(0)\right]\right.\\ &=\left.\prod_{t=0}^{t_{\max}-1}\left\{\prod_{i=1}^{N^{\sigma}}\frac{\mathrm{e}^{\beta\sigma_{i}(t+1)h_{i}(t)}}{2\cosh[\beta h_{i}(t)]}\prod_{\ell=1}^{N^{\tau}}\frac{\mathrm{e}^{\beta\tau_{\ell}(t+1)g_{\ell}(t)}}{2\cosh[\beta g_{\ell}(t)]}\right\}\right.\\ \end{aligned} \quad (B7) \] 

and, to reduce notation, we used various variables in a vector form  \( (h(t) = (h_{1}(t), \ldots, h_{N}(t)) \) , etc.) wherever possible.
In order to proceed with the computation of (B5), we have to specify the interaction variables in the term

 \[ \begin{aligned}&\exp\left[-\mathrm{i}\sum_{t=0}^{t_{\max}-1}\left\{\hat{h}(t)\cdot h(\sigma(t),\tau(t))+\hat{g}(t)\cdot g(\sigma(t),\tau (t))\right\}\right]\\&=\prod_{t=0}^{t_{\max}-1}\exp\left[-\mathrm{i}\sum_{i=1}^{N^{\sigma}}\hat{h}_{i}(t)\left\{\sum_{j\neq i}^{N^{\sigma}}J_{ij}^{\sigma}\sigma_{j}(t)+\sum_{j\neq i}^{N^{\tau}}J_{ij}^{\sigma_{i}\leftarrow\tau}\tau_{j}(t)+\theta_{i}^{\sigma}(t)\right\}\right]\\&\times\exp\left[-\mathrm{i}\sum_{\ell=1}^{N^{\tau}}\hat{g}_{\ell}(t)\left\{\sum_{k\neq\ell}^{N^{\tau}}J_{\ell k}^{\tau}\tau_{k}(t)+\sum_{k\neq\ell}^{N^{\sigma}}J_{\ell k}^{\tau\leftarrow\sigma}\sigma_{k}(t)+\theta_{\ell}^{\tau}(t)\right\}\right]\end{aligned} \quad (B8) \] 

which contains all information about the structure of our model. For the sake of simplicity we take the interactions  \( J_{ij}^{\sigma} = \frac{J^{\sigma}}{N^{\sigma}} \) ,  \( J_{ij}^{\sigma \leftarrow \tau} = \frac{J^{\sigma \leftarrow \sigma}}{N^{\tau}} \)  and  \( J_{ij}^{\tau} \) ,  \( J_{ij}^{ \tau \leftarrow \sigma} \)  are random independent variables drawn from the distributions  \( \frac{1}{2} \delta (J_{ij}^{\tau} - \frac{J^{\tau}}{N^{\tau}}) + \frac{1}{2} \delta (J_{ij}^{\tau} + \frac{J^{\tau}}{N^{\tau}}) \)  and  \( \frac{1}{2} \delta (J_{ij}^{\tau \leftarrow \sigma} - \frac{J^{\tau \leftarrow \alpha}}{N^{\sigma}}) + \frac{1}{2} \delta (J_{ij}^{\tau \leftarrow \sigma} + \frac{J^{\tau \leftarrow \alpha}}{N^{\sigma}}) \)  respectively. The scaling of these interactions will allow us to take the thermodynamic limit later on. First, however, we have to deal with the disorder in interactions. Assuming that the system is self-averaging [19] (which is expected for a very large system) allows us to take disorder averages in (B8).

## 2. Disorder averages

Let us now take the averages in the disorder-dependent part of (B8)
 

(B9)

 \[ \begin{aligned}&\prod_{t=0}^{t_{\max}-1}\exp\left[-i\sum_{\ell=1}^{N^{\tau}}\hat{g}_{\ell}(t)\left\{\sum_{k\neq\ell}^{N^{\tau}}J_{\ell k}^{\tau}\tau_{k}(t)+\sum_{k\neq\ell}^{N^{\sigma}}J_{\ell k}^{\tau-\sigma}\sigma_{k}(t)\right\}\right]^{\{J_{\ell k}^{\tau},J_{\ell k}^{\prime\tau-\sigma}\}}\\ &=\prod_{\ell=1}^{N^{\tau}}\prod_{k\neq\ell}^{N^{\tau}}\exp\left[-i J_{\ell k}^{\tau}\sum_{t=0}^{t_{\max}-1}\hat{g}_{\ell}(t)\tau_{k}(t)\right]\prod_{k\neq\ell}^{N^{\sigma}}\exp\left[-i J_{\ell k}^{\tau-\sigma}\sum_{t=0}^{t_{\max}-1}\hat{g}_{\ell}(t)\sigma_{k}(t)\right]^{\{J_{\ell k}^{\tau-\sigma}\}}\\ &=\prod_{\ell=1}^{N^{\tau}}\prod_{k\neq\ell}^{N^{\tau}}\cos\left[\frac{J^{\tau}}{\sqrt{N^{\tau}}}\sum_{t=0}^{t_{\max}-1}\hat{g}_{\ell}(t)\tau_{k}(t)\right]\prod_{k\neq\ell}^{N^{\sigma}}\cos\left[\frac{J^{\tau-\sigma}}{\sqrt{N^{\sigma}}}\sum_{t=0}^{t_{\max}-1}\hat{g}_{\ell}(t)\sigma_{k}(t)\right]\\ &=\prod_{\ell=1}^{N^{\tau}}\exp\left[-\frac{1}{2N^{\tau}}\sum_{k\neq\ell}^{N^{\tau}}\left(J^{\tau}\sum_{t=0}^{t_{\max}-1}\hat{g}_{\ell}(t)\tau_{k}(t)\right)^{2}\right]\exp\left[-\frac{1}{2N^{\sigma}}\sum_{j\neq\ell}^{N^{\sigma}}\left(J^{\tau-\sigma}\sum_{t=0}^{t_{\max}-1}\hat{g}_{\ell}(t)\sigma_{j}(t)\right)^{2}+O(N^{0})\right]\\ &=\prod_{\ell=1}^{N^{\tau}}\exp\left[-\frac{(J^{\tau})^{2}}{2N^{\tau}}\sum_{k\neq\ell}^{N^{\tau}}\sum_{\tau,t^{\prime}}\hat{g}_{\ell}(t)\hat{g}_{\ell}({t^{\prime}})\tau_{k}(t)\tau_{k}({t^{\prime}})\right]\exp\left[-\frac{(J^{\tau-\sigma})^{2}}{2N^{\sigma}}\sum_{j\neq\ell}^{N^{\sigma}}\sum_{\tau,t^{\prime}}\hat{g}_{\ell}(t)\hat{g}_{\ell}({t^{\prime}})\sigma_{j}(t)\sigma_{j}({t^{\prime}})+O(N^{0})\right]\end{aligned} \] 

In the above we have used the asymptotic identity  \( \cos(x) = \exp(-\frac{x^{2}}{2} + O(x^{4})) \)  as  \( x \to 0 \)  to obtain the quadratic form in the last line of (B9). We note that for any interactions of the form  \( \frac{J}{\sqrt{N}} \)  with random J sampled from the (well behaved) distribution  \( \mathrm{P}(J) \) , with  \( \int dJ \mathrm{P}(J)\mathrm{J} = 0 \)  and  \( \int dJ \mathrm{P}(J)\mathrm{J}^{2} = 1 \) , the result of the disorder average (B9) remains the same.

## 3. Order parameters

Using the scaling of interactions from the section B1 and the results of disorder averages from the section B2 we obtain the disorder-averaged generating functional

 \[ \begin{align*}\overline{\Gamma}[\psi^{\sigma},\psi^{\overline{\tau}}]&=\int\{\mathrm{d}h\mathrm{~d}\hat{h}\mathrm{~d}g\mathrm{~d}\hat{g}\}\exp\left[\mathrm{i}\sum_{t=0}^{t_{\max}-1}\left\{\hat{h}(t)\cdot[h(t)-\theta^{\sigma}(t)]+\hat{g}(t)\cdot[g(t)-\theta^{\tau}(t)]\right\}\right]\\&\quad\times\sum_{\{\sigma_{i}(t),\tau_{i}(t)\}}\exp\left[-\mathrm{i}\sum_{i=1}^{N^{\sigma}}\sum_{t=0}^{t_{\max}-1}\hat{h}_{i}(t)\left\{\frac{J^{\sigma}}{N^{\sigma}}\sum_{j\neq i}^{N^{\sigma}}\sigma_{j}(t)+\frac{J^{\sigma-\tau}}{N^{\tau}}\sum_{k\neq i}^{N^{\tau}}\tau_{k}(t)\right\}\right]\\&\quad\times\prod_{\ell=1}^{N^{\tau}}\exp\left[-\frac{(J^{\tau})^{2}}{2N^{\tau}}\sum_{k\neq\ell}^{N^{\tau}}\sum_{\tau,t^{\prime}}\hat{g}_{\ell}(t)\hat{g}_{\ell}({t^{\prime}})\tau_{k}(t)\tau_{k}({t^{\prime}})\right]\exp\left[-\frac{(J^{\tau-\sigma})^{2}}{2N^{\sigma}}\sum_{j\neq\ell}^{N^{\sigma}}\sum_{\tau,t^{\prime}}\hat{g}_{\ell}(t)\hat{g}_{\ell}({t^{\prime}})\sigma_{j}(t)\sigma_{j}({t^{\prime}})+O(N^{0})\right]\\&\quad\times\mathrm{P}\big[\sigma(t_{\max}),\tau(t_{\max})\leftarrow\cdots\leftarrow\sigma(1),\tau(1)\big.\\&\quad\left.\left|h(t_{\max}-1),g(t_{\max}-1),\cdots,h(0),g(0)\right]\mathrm{P}(\sigma(0))\mathrm{P}(\tau(0))\exp\left[-\mathrm{i}\sum_{t=0}^{t_{\max}}\left\{\psi^{\sigma}(t)\cdot\sigma(t)+\psi^{\tau}(t)\cdot\tau(t)\right\}\right]\right.\end{align*} \quad (B10) \] 

Inserting into above the following representations of unity for all times t

 \[ \begin{aligned}&\int\frac{\mathrm{d}m^{\sigma}(t)\mathrm{d}\hat{m}^{\sigma}(t)}{2\pi/N^{\sigma}}\mathrm{e}^{\mathrm{i}N^{\sigma}\hat{m}^{\sigma}(t)[m^{\sigma}(t)-\frac{1}{N^{\sigma}}\sum_{i=1}^{N^{\sigma}}\sigma_{i}(t)]}=1\\&\int\frac{\mathrm{d}m^{\tau}(t)\mathrm{d}\hat{m}^{\tau}(t)}{2\pi/N^{\tau}}\mathrm{e}^{\mathrm{i}N^{\tau}\hat{m}^{\tau}(t)[m^{\tau}(t)-\frac{1}{N^{\tau}}\sum_{i=1}^{N^{\tau}}\tau_{i}(t)]}=1\end{aligned} \quad (B11) \]
 

 \[ \begin{align*}&\int\frac{\mathrm{d}q^{\sigma}(t,t^{\prime})}{\mathrm{d}\hat{q}^{\sigma}(t,t^{\rho})}\mathrm{e}^{\mathrm{i}N^{\sigma}\hat{q}^{\sigma}(t,t^{\prime})[q^{\sigma}(t,t^{\rho})-\frac{1}{N^{\sigma}}\sum_{i=1}^{N^{\sigma}}\sigma_{i}(t)\sigma_{i}(t^{\prime})]}=1\\&\int\frac{\mathrm{d}q^{\tau}(t,t^{\prime})}{\mathrm{d}\hat{q}^{\tau}(t,t^{\rho})}\mathrm{e}^{\mathrm{i}N^{\tau}\hat{q}^{\tau}(t,t^{\prime})[q^{\tau}(t,t^{\rho})-\frac{1}{N^{\tau}}\sum_{i=1}^{N^{\tau}}\tau_{i}(t)\tau_{i}(t^{\prime})]}=1\end{align*} \] 

and using that they are just integrals over the  \( \delta \) -functions in their Fourier representation, we obtain

(B12)

 \[ \begin{aligned}&\overline{\Gamma[\psi^{\sigma},\psi^{\tau}]}=\int\left\{\mathrm{d}m^{\sigma}\mathrm{d}\hat{m}^{\sigma}\mathrm{d}m^{\tau}\mathrm{d}\hat{n}^{\tau}\mathrm{d}q^{\sigma}\mathrm{d}\hat{q}^{\sigma}\mathrm{d}q^{T}\mathrm{d}\hat{{q}}^{T}\right\}\exp\left[\mathrm{i}N^{\sigma}\sum_{t}\hat{m}^{\sigma}(t)m^{\sigma}(t)+\mathrm{i}N^{\sigma}\sum_{t,t^{\prime}}\hat{q}^{\sigma}(t,t^{\prime})q^{\sigma}(t,t^{\rho})\right]\\&\times\exp\left[\mathrm{i}N^{\tau}\sum_{t}\hat{m}^{\tau}(t)m^{\tau}(t)+\mathrm{i}N^{\tau}\sum_{t,t^{\prime}}\hat{q}^{\tau}(t,t^{\rho})q^{\tau}(t,t^{\prime})\right]\\&\times\sum_{\{\sigma_{i}(t),\tau_{i}(t)\}}\prod_{t=0}^{t_{\max}-1}\prod_{i=1}^{N^{\sigma}}\left\{\int\mathrm{d}h_{i}(t)\delta\left(h_{i}(t)-J^{\sigma}m^{\sigma}(t)-J^{\bar{\sigma}\leftarrow\tau}m^{\tau}(t)-\theta_{i}^{\sigma}(t)+\Delta_{i}^{h}(\sigma,\tau)\right)\right\}\\&\times\int\{\mathrm{d}g\mathrm{d}\hat{g}\}\prod_{t=1}^{N^{\tau}}\exp\left[\mathrm{i}\sum_{t=0}^{t_{\max}-1}\hat{g}_{\ell}(t)\left[g_{\ell}(t)-\theta_{\ell}^{T}(t)\right]\right]\exp\left[-\frac{1}{2}(J^{\tau})^{2}\sum_{t,t^{\prime}}\hat{g}_{\ell}(t)\Lambda(t,t^{\prime})\hat{g}_{\ell}({t^{\prime}})+\Delta_{\ell}^{A}(\sigma,\tau)\right]\\&\times\prod_{i=1}^{N^{\sigma}}\exp\left[-\mathrm{i}\sum_{t}\hat{m}^{\sigma}(t)\sigma_{i}(t)-\mathrm{i}\sum_{t,t^{\prime}}\hat{q}^{\sigma}(t,t^{\rho})\sigma_{i}(t)\sigma_{i}(t^{\prime})\right]\prod_{i=1}^{N^{\tau}}\exp\left[-\mathrm{i}\sum_{t}\hat{m}^{\tau}(t)\tau_{i}(t)-\mathrm{i}\sum_{t,t^{\prime}}\hat{q}^{\tau}(t,t^{\rho})\tau_{i}(t)\tau_{i}(t^{\prime})\right]\\&\times\mathrm{P}\big[\sigma(t_{\max}),\tau(t_{\max})\leftarrow\cdots\leftarrow\sigma(1),\tau(1)\big.\\&\left.\left|h(t_{\max}-1),g(t_{\max}-1),\cdots,h(0),g(0)\right]\mathrm{P}(\sigma(0))\mathrm{P}(\tau(0))\right)\exp\left[-\mathrm{i}\sum_{t=0}^{t_{\max}}\left\{\psi^{\sigma}(t)\cdot\sigma(t)+\psi^{\tau}(t)\cdot\tau(t)\right\}+O(N^{0})\right],\end{aligned} \] 

where in the above we have used the following notations

(B14)

 \[ \begin{aligned}&\int\left\{\mathrm{d}m^{\sigma}\mathrm{d}\hat{m}^{\sigma}\mathrm{d}m^{\tau}\mathrm{d}\hat{n}^{\tau}\mathrm{d}q^{\sigma}\mathrm{d}\hat{q}^{\sigma}\mathrm{d}q^{T}\mathrm{d}\hat{{q}}^{T}\right\}\equiv\quad(\mathrm{B13})\\&\int\frac{\mathrm{d}m^{\sigma}(t)\mathrm{d}\hat{m}^{\sigma}(t)}{2\pi/N^{\sigma}}\int\frac{\mathrm{d}m^{\tau}(t)\mathrm{d}\hat{n}^{\tau}(t)}{2\pi/N^{\tau}}\\&\times\int\frac{\mathrm{d}q^{\sigma}(t,t^{\prime})\mathrm{d}\hat{q}^{\sigma}(t,t^{\rho})}{2\pi/N^{\sigma}}\int\frac{\mathrm{d}q^{\tau}(t,t^{\prime})\mathrm{d}\hat{q}^{\tau}(t,t^{\rho})}{2\pi/N^{\tau}}\\ \end{aligned} \] 

 \[ \mathrm{A}(t,t^{\prime})=q^{\tau}(t,t^{\prime})+\left[\frac{J^{\tau\leftarrow\sigma}}{J^{\tau}}\right]^{2}q^{\sigma}(t,t^{\prime}). \quad (B14) \] 

 \[ \mathrm{T h e~c o r r e c t i o n s~}\Delta_{i}^{h}(\sigma,\tau)=\frac{J^{\sigma}}{N^{\sigma}}\sigma_{i}(t)+\frac{J^{\sigma\leftarrow\tau}}{N^{\tau}}\tau_{i}(t)\mathrm{~a n d~} \] 

 \[ \Delta_{\ell}^{A}(\sigma,\tau)=\frac{1}{2}(J^{\tau})^{2}\sum_{t,t^{\prime}}\hat{g}_{\ell}(t)\Biggl\{\frac{1}{N^{\tau}}\tau_{\ell}(t)\tau_{\ell}(t^{\prime})+\frac{1}{N^{\sigma}}\left[\frac{J^{\tau\leftarrow\sigma}}{J^{\tau}}\right]^{2}\sigma_{\ell}(t)\sigma_{\ell}(t^{\prime})\Biggr\}\hat{g}_{\ell}(t^{\prime}) \] 

contribute to the  \( O(N^{0}) \)  term in the equation (B12).

Using the Gaussian integral identity
 

 \[ \exp\left[-\frac{1}{2}(J^{\tau})^{2}\sum_{t,t^{\prime}}\hat{g}(t)\mathrm{A}(t,t^{\prime})\hat{g}(t^{\prime})\right]=\sqrt{\frac{|A^{-1}|}{(2\pi)^{t_{\max}}}}\int\{\mathrm{d}\phi\}\exp\left[-\frac{1}{2}\sum_{t,t^{\prime}}\phi(t)\mathrm{A}^{-1}(t,t^{\prime})\phi(t^{\prime})-\mathrm{i}J^{\tau}\sum_{t}\phi(t)\hat{g}(t)\right] \quad (B15) \] 

allows us to linearise the quadratic form in the equation (B12). This with subsequent integration over the  \( \hat{g} \)  vari-
ables gives us

 \[ \begin{aligned}\overline{\Gamma}[\psi^{\sigma},\psi^{\tau}]&=\int\left\{\mathrm{d}m^{\sigma}\mathrm{d}\hat{m}^{\sigma}\mathrm{d}m^{\tau}\mathrm{d}\hat{\eta}^{\tau}\mathrm{d}q^{\sigma}\mathrm{d}\hat{q}^{\sigma}\mathrm{d}q^{7}\mathrm{d}\hat{{q}}^{7}\right\}\exp\left[\mathrm{i}N^{\sigma}\sum_{t}\hat{m}^{\sigma}(t)m^{\sigma}(t)+\mathrm{i}N^{\sigma}\sum_{t,t^{\prime}}\hat{q}^{\sigma}(t,t^{\prime})q^{\sigma}(t,t^{\nu})\right]\\&\quad\times\exp\left[+\mathrm{i}N^{\tau}\sum_{t}\hat{m}^{\tau}(t)m^{\tau}(t)+\mathrm{i}N^{\tau}\sum_{t,t^{\prime}}\hat{q}^{\tau}(t,t^{\prime})q^{\tau}(t,t^{\nu})\right]\\&\quad\times\sum_{\{\sigma_{i}(t),\tau_{i}(t)\}=0}^{t_{\max}-1}\prod_{i=1}^{N^{\sigma}}\int\mathrm{d}h_{i}(t)\delta\left(h_{i}(t)-J^{\sigma}m^{\sigma}(t)-J^{\tau\leftarrow\tau}m^{\tau}(t)-\theta_{i}^{\sigma}(t)\right)\Bigg\}\\&\quad\times\prod_{\ell=1}^{N^{\tau}}\left\{\sqrt{\frac{|A^{-1}|}{(2\pi)^{t_{\max}}}}\int\{\mathrm{d}\phi\}\exp\left[-\frac{1}{2}\sum_{t,t^{\nu}}\phi(t)\mathrm{A}^{-1}(t,t^{\nu})\phi(t^{\nu})\right]\prod_{t=0}^{t_{\max}-1}\int\mathrm{d}g_{\ell}(t)\delta\left(g_{\ell}(t)-J^{\tau}\phi(t)-\theta_{\ell}^{\tau}(t)\right)\right\}\\&\quad\times\prod_{i=1}^{N^{\sigma}}\exp\left[-\mathrm{i}\sum_{t}\hat{m}^{\sigma}(t)\sigma_{i}(t)-\mathrm{i}\sum_{t,t^{\nu}}\hat{q}^{\sigma}(t,t^{\nu})\sigma_{i}(t^{\nu})\right]\prod_{i=1}^{N^{\tau}}\exp\left[-\mathrm{i}\sum_{t}\hat{m}^{\tau}(t)\tau_{i}(t)-\mathrm{i}\sum_{t,t^{\nu}}\hat{q}^{\tau}(t,t^{\nu})\tau_{i}(t)\tau_{i}(t^{\nu})\right]\\&\quad\times\mathrm{P}\left[\sigma(t_{\max}),\tau(t_{\max})\leftarrow\cdots\leftarrow\sigma(1),\tau(1)|h(t_{\max}-1),g(t_{\max}-1),\cdots,h(0),g(0)\right]\mathrm{P}(\sigma(0))\mathrm{P}(\tau(0))\right.\\&\quad\times\exp\left[-\mathrm{i}\sum_{t=0}^{t_{\max}}\left\{\psi^{\sigma}(t)\cdot\sigma(t)+\psi^{\tau}(t)\cdot\tau(t)\right\}+O(N^{0})\right]\\&\quad=\int\left\{\mathrm{d}m^{\sigma}\mathrm{d}\hat{m}^{\sigma}\mathrm{d}m^{\tau}\mathrm{d}\hat{\eta}^{\tau}\mathrm{d}q^{\sigma}\mathrm{d}\hat{q}^{\sigma}\mathrm{d}q^{7}\mathrm{d}\hat{{q}}^{7}\right\}\exp\left[\mathrm{i}N^{\sigma}\sum_{t}\hat{m}^{\sigma}(t)m^{\sigma}(t)+\mathrm{i}N^{\sigma}\sum_{t,t^{\nu}}\hat{q}^{\sigma}(t,t^{\nu})q^{\sigma}(t,t^{\prime})\right]\\&\quad\times\exp\left[\mathrm{i}N^{\tau}\sum_{t}\hat{m}^{\tau}(t)m^{\tau}(t)+\mathrm{i}N^{\tau}\sum_{t,t^{\nu}}\hat{q}^{\tau}(t,t^{\nu})q^{\tau}(t,t^{\prime})\right]\\&\quad\times\sum_{\{\sigma_{i}(t),\tau_{i}(t)\}}\exp\left[O(N^{0})\right]\prod_{i=1}^{N^{\sigma}}\exp\left[-\mathrm{i}\sum_{t}\hat{m}^{\sigma}(t)\sigma_{i}(t)-\mathrm{i}\sum_{t,t^{\nu}}\hat{q}^{\sigma}(t,t^{\nu})\sigma_{i}(t^{\nu})\right]\exp\left[-\mathrm{i}\sum_{t=0}^{t_{\max}}\psi_{\ell}^{\sigma}(t)\sigma_{i}(t)\right]\\&\quad\times\prod_{i=1}^{N^{\sigma}}\left\{\prod_{t=0}^{t_{\max}-1}\frac{\mathrm{e}^{\beta\sigma_{i}(t+1)}\{J^{\sigma}m^{\sigma}(t)+J^{\sigma\leftarrow\tau}m^{\tau}(t)+\theta_{i}^{\sigma}(t)\}}{\mathrm{2}\cosh[\beta\left\{J^{\sigma}m^{\sigma}(t)+J^{\sigma\leftarrow\tau}m^{\tau}(t)+\theta_{i}^{\sigma}(t)\right\}]}\right\}\frac{1}{2}\left[1+m^{\sigma}(0)\sigma_{i}(0)\right]\\&\quad\times\prod_{\ell=1}^{N^{\tau}}\exp\left[-\mathrm{i}\sum_{t}\hat{m}^{\tau}(t)\tau_{\ell}(t)-\mathrm{i}\sum_{t,t^{\nu}}\hat{q}^{\tau}(t,t^{\nu})\tau_{\ell}(t)\tau_{\ell}(t^{\nu})\right]\exp\left[-\mathrm{i}\sum_{t=0}^{t_{\max}}\psi_{\ell}^{\tau}(t)\tau_{\ell}(t)\right]\\&\quad\times\prod_{\ell=1}^{N^{\tau}}\sqrt{\frac{|A^{-1}|}{(2\pi)^{t_{\max}}}}\int\{\mathrm{d}\phi\}\exp\left[-\frac{1}{2}\sum_{t,t^{\nu}}\phi(t)A^{-1}(t,t^{\nu})\phi(t^{\nu})\right]\\&\quad\times\left\{\prod_{t=0}^{t_{\max}-1}\frac{\mathrm{e}^{\beta\tau_{\ell}(t+1)}\{J^{\tau}\phi(t)+\theta_{\ell}^{\tau}(t)\}}{2\cosh[\beta\left\{J^{\tau}\phi(t)+\theta_{\ell}^{\tau}(t)\right\}]}\right\}\frac{1}{2}\left[1+m^{\tau}(0)\tau_{\ell}(0)\right]\end{aligned} \quad (B16) \]
 

Let us now define the two objects

 \[ \begin{align*}\mathsf{M}^{\sigma}\left[\left\{\sigma_{i}(t)\right\}\middle|\left\{\psi_{i}^{\sigma}(t)\right\}\right]&=\exp\left[-\mathrm{i}\sum_{t}\hat{m}^{\sigma}(t)\sigma_{i}(t)-\mathrm{i}\sum_{t,t^{\prime}}\hat{q}^{\sigma}(t,t^{\prime})\sigma_{i}(t)\sigma_{i}(t^{\prime})\right]\exp\left[-\mathrm{i}\sum_{t=0}^{t_{\max}}\psi_{i}^{\sigma}(t)\sigma_{i}(t)\right]\\\times\left\{\prod_{t=0}^{t_{\max}-1}\frac{\mathrm{e}^{\beta\sigma_{i}(t+1)}\{J^{\sigma}m^{\sigma}(t)+J^{\sigma\leftarrow\tau}m^{\tau}(t)+\theta_{\ell}^{\sigma}(t)\}}{2\cosh[\beta\left\{J^{\sigma}m^{\sigma}(t)+J^{\sigma\leftarrow\tau}m^{\tau}(t)+\theta_{\ell}^{\sigma}(t)\}\right\}}\right\}&\frac{1}{2}\left[1+m^{\sigma}(0)\sigma_{i}(0)\right]\end{align*} \quad (B17) \] 

 \[ \begin{align*}\mathsf{M}^{\tau}\left[\left\{\tau_{\ell}(t)\right\}\middle|\left\{\psi_{\ell}^{\tau}(t)\right\}\right]&=\exp\left[-\mathrm{i}\sum_{t}\hat{m}^{\tau}(t)\tau_{\ell}(t)-\mathrm{i}\sum_{t,t^{\prime}}\hat{q}^{\tau}(t,t^{\prime})\tau_{\ell}(t)\tau_{\ell}(t^{\prime})\right]\exp\left[-\mathrm{i}\sum_{t=0}^{t_{\max}}\psi_{\ell}^{\tau}(t)\tau_{\ell}(t)\right]\\\times&\sqrt{\frac{|A^{-1}|}{(2\pi)^{t_{\max}}}}\int\{\mathrm{d}\phi\}\exp\left[-\frac{1}{2}\sum_{t,t^{\prime}}\phi(t)\mathrm{A}^{-1}(t,t^{\prime})\phi(t^{\prime})\right]\left\{\prod_{t=0}^{t_{\max}-1}\frac{\mathrm{e}^{\beta\tau_{\ell}(t+1)}\{J^{\tau}\phi(t)+\theta_{\ell}^{\tau}(t)\}}{2\cosh[\beta\left\{J^{\tau}\phi(t)+\theta_{\ell}^{\tau}(t)\right\}]}\right\}\frac{1}{2}\left[1+m^{\tau}(0)\tau_{\ell}(0)\right].\end{align*} \quad (B18) \] 

Using above definitions in the final result of (B16), with  \( N^{\sigma} = \gamma N \)  and  \( N^{\tau} = (1 - \gamma)N \)  we are able to write the disorder-averaged generating functional (B16) in the form of an integral

 \[ \overline{{\Gamma[\psi^{\sigma},\psi^{\tau}]}}=\int\left\{\mathrm{d}m^{\sigma}\mathrm{d}\hat{m}^{\sigma}\mathrm{d}m^{\tau}\mathrm{d}\hat{n}^{\tau}\mathrm{d}q^{\sigma}\mathrm{d}\hat{q}^{\sigma}\mathrm{d}q^{r}\mathrm{d}\hat{\boldsymbol{q}}^{r}\right\}\mathrm{e}^{N\Psi[m^{\sigma},\hat{m}^{\sigma},m^{\tau},\hat{m}^{\tau},q^{\sigma},\hat{q}^{\sigma},q^{r},\hat{q}^{r},\psi^{\sigma},\psi^{\tau}]+O(N^{0})}, \quad (B19) \] 

where

 \[ \begin{align*}&\Psi[m^{\sigma},\hat{m}^{\sigma},m^{\tau},\hat{m}^{\tau},q^{\sigma},\hat{q}^{\sigma},q^{\tau},\hat{q}^{\tau},\psi^{\sigma},\psi^{\tau}]\\=&\mathrm{i}\gamma\sum_{t}\hat{m}^{\sigma}(t)m^{\sigma}(t)+\mathrm{i}\gamma\sum_{t,t^{\prime}}\hat{q}^{\sigma}(t,t^{\prime})q^{\sigma}(t,t^{\tau})+\mathrm{i}(1-\gamma)\sum_{t}\hat{m}^{\tau}(t)m^{\tau}(t)+\mathrm{i}(1-\gamma)\sum_{t,t^{\prime}}\hat{q}^{\tau}(t,t^{\prime})q^{\tau}(t,t^{\tau})\\&+\frac{1}{N}\sum_{i=1}^{N^{\sigma}}\log\left[\sum_{\{\sigma_{i}(t)\}}\mathsf{M}^{\sigma}\left[\{\sigma_{i}({t})\}\right]\left\{\psi_{i}^{\sigma}({t})\right\}\right]+\frac{1}{N}\sum_{i=1}^{N^{\tau}}\log\left[\sum_{\{\tau_{i}(t)\}}\mathsf{M}^{\tau}\left[\{\tau_{i}({t})\}\right]\left\{\psi_{i}^{\tau}({t})\right\}\right].\end{align*} \quad (B20) \] 

Now for  \( N \to \infty \)  we can use the saddle-point method to evaluate this integral.
which gives us

 \[ \begin{align*}m^{\sigma}(t)&=\langle\sigma(t)\rangle_{\mathrm{M}^{\sigma}}\\ \mathrm{i}\hat{m}^{\sigma}(t)&=\beta J^{\sigma}\Big(\langle\sigma(t+1)\rangle_{\mathrm{M}^{\sigma}}\\ &\quad-\tanh\left[\beta\left\{J^{\sigma}m^{\sigma}(t)+J^{\sigma\leftarrow\tau}m^{\tau}(t)+\theta^{\sigma}(t)\right\}\right]\\ m^{\tau}(t)&=\langle\tau(t)\rangle_{\mathrm{M}^{\tau}}\\ \mathrm{i}\hat{m}^{\tau}(t)&=\frac{\gamma}{1-\gamma}\beta J^{\sigma\leftarrow\tau}\Big(\langle\sigma(t+1)\rangle_{\mathrm{M}^{\sigma}}\\ &\quad-\tanh\left[\beta\left\{J^{\sigma}m^{\sigma}(t)+J^{\sigma\leftarrow\tau}m^{\tau}(t)\right\}\right]\Big)\\ q^{\sigma}(t,t^{\prime})&=\langle\sigma(t)\sigma(t^{\prime})\rangle_{\mathrm{M}^{\sigma}}\\ q^{\tau}(t,t^{\prime})&=\langle\tau(t)\tau(t^{\prime})\rangle_{\mathrm{M}^{\tau}}\\ \mathrm{i}\hat{q}^{\tau}(t,t^{\prime})&=\mathrm{i}\hat{q^{\sigma}}(t,t^{\prime})=0,\end{align*} \quad (B21) \] 

## 4. Saddle-point problem

The integral (B19) is dominated by the extrema of the function (B20). To obtain these we solve the equations  \( \frac{\partial\Psi}{\partial\Omega}=0 \) , where  \( \Omega\in\{m^{\sigma},\hat{m}^{\sigma},m^{\tau},\hat{m}^{\tau},q^{\sigma},\hat{q}^{\sigma},q^{\tau},\hat{q}^{\tau}\} \) , where the averages  \( \langle\cdots\rangle_{M^{\sigma}} \)  and  \( \langle\ldots\rangle_{M^{\tau}} \)  are generated by the (site independent) weight functions[24] (B17) and (B18) respectively.

In order to show that the equality  \( \mathrm{i}\hat{q}^{\tau}(t,t^{\prime})= \)
 

 \[ \begin{align*}\mathrm{M}^{\tau}\left[\left\{\tau_{\ell}(t)\right\}\middle|\left\{\psi_{\ell}^{\tau}(t)\right\}\right]&=\int\left\{\mathrm{d}g_{\ell}(t)\mathrm{d}\hat{g}_{\ell}(t)\right\}\mathrm{M}^{\tau}\left[\left\{\tau_{\ell}(t)\right\};\left\{g_{\ell}(t),\hat{g}_{\ell}(t)\right\}\middle|\left\{\psi_{\ell}^{\tau}(t)\right\}\right]\\&=\int\left\{\mathrm{d}g_{\ell}(t)\mathrm{d}\hat{g}_{\ell}(t)\right\}\exp\left[-\mathrm{i}\sum_{t}\hat{m}^{\tau}(t)\tau_{\ell}(t)-\mathrm{i}\sum_{t,t^{\prime}}\hat{q}^{\tau}(t,t^{\prime})\tau_{\ell}(t)\tau_{\ell}(t^{\prime})\right]\\&\times\exp\left[\mathrm{i}\sum_{t=0}^{t_{\max}-1}\hat{g}_{\ell}(t)\left[g_{\ell}(t)-\theta_{\ell}^{\tau}(t)\right]\right]\exp\left[-\frac{1}{2}(J^{\tau})^{2}\sum_{t,t^{\prime}}\hat{g}_{\ell}(t)\mathrm{A}(t,t^{\prime})\hat{g}_{\ell}( t^{\prime})\right]\\&\times\left\{\prod_{t=0}^{t_{\max}-1}\frac{\mathrm{e}^{\beta\tau_{\ell}(t+1)g_{\ell}(t)}}{2\cosh[\beta g_{\ell}(t)]}\right\}\frac{1}{2}\left[1+m^{\tau}(0)\tau_{\ell}(0)\right]\exp\left[-\mathrm{i}\sum_{t=0}^{t_{\max}}\psi_{\ell}^{\tau}(t)\tau_{\ell}(t)\right],\end{align*} \quad (B22) \] 

where  \( \mathrm{A}(t,t') = q^{\tau}(t,t') + \left[\frac{J^{\tau-t}g}{\bar{J}^{\tau}}\right]^{2} q^{\sigma}(t,t') \) .

From the above it is clear that

 \[ \frac{\partial}{\partial q(t,t^{\prime})}\log\left[\sum_{\{\tau_{\ell}(t)\}}\int\{\mathrm{d}g_{\ell}(t)\mathrm{d}\hat{g}_{\ell}(t)\}\mathrm{M}^{\tau}\left[\ldots\right]\right]=-\frac{1}{2}J^{2}\left\langle\hat{g}_{\ell}(t)\hat{g}_{\ell}(t^{\prime})\right\rangle_{\mathrm{M}^{\tau}}, \quad (B23) \] 

but also

 \[ -\frac{\partial^{2}}{\partial\theta_{\ell}^{\tau}(t)\partial\theta_{\ell}^{\sigma}(t^{\prime})}\log\left[\sum_{\{\tau_{\ell}(t)\}}\int\{\mathrm{d}g_{\ell}(t)\mathrm{d}\hat{g}_{\ell}(t)\}\mathrm{M}^{\tau}\left[\ldots\right]\right]=\left\langle\hat{g}_{\ell}(t)\hat{g}_{\ell}(t^{\prime})\right\rangle_{\mathrm{M}^{\tau}}. \quad (B24) \] 

Now using the above results and the identity  \( \frac{\partial^{2}}{\partial\theta_{\ell}^{\tau}(t)\partial\theta_{\ell}^{\sigma}(t^{\prime})}\Gamma[0,0]=0 \)  (since  \( \Gamma[0,0])=1 \) ), it is not difficult to show that the equality  \( \mathrm{i}\hat{q}^{\tau}(t,t^{\prime})=\mathrm{i}\hat{q}^{o}(t,t^{\prime})=0 \)  is true. Application of this equality in the equations (B21) leads to further simplifications after which we obtain the following four equations

 \[ m^{\sigma}(t+1)=\tanh\left[\beta\left\{J^{\sigma}m^{\sigma}(t)+J^{\sigma\leftarrow\tau}m^{\tau}(t)+\theta^{\sigma}(t)\right\}\right] \quad (B25) \] 

 \[ m^{\tau}(t+1)=\sqrt{\frac{|A^{-1}|}{(2\pi)^{t_{\max}}}}\int\{\mathrm{d}\phi\}\exp\left[-\frac{1}{2}\sum_{t,t^{\prime}}\phi(t)\mathrm{A}^{-1}(t,t^{\prime})\phi(t^{\prime})\right]\tanh\left[\beta J^{\tau}\phi(t)\right] \quad (B26) \] 

 \[ q^{\sigma}(t,t^{\prime})=\delta_{t,t^{\prime}}+(1-\delta_{t,t^{\ prime}})m^{\sigma}(t)m^{\sigma}(t^{\prime}) \quad (B27) \] 

 \[ q^{\tau}(t+1,t^{\prime}+1)=\sqrt{\frac{|A^{-1}|}{(2\pi)^{t_{\max}}}}\int\{\mathrm{d}\phi\}\exp\left[-\frac{1}{2}\sum_{t,t^{\prime}}\phi(t)\mathrm{A}^{-1}(t,t^{\prime})\phi(t^{\prime})\right]\tanh\left[\beta J^{\tau}\phi(t)\right]\tanh\left[{\beta J^{\tau}}\phi(t^{\prime})\right] \quad (B28) \] 

Now the multivariate Gaussian probability measure in the equation (B26) can be reduced to a Gaussian of one variable only (with zero mean) thereby leading us to the result (3).
 
![](./images/867772594198151658_5.jpg)

FIG. 2: Cayley tree with k = 3 and r = 4 generations (edges painted in blue) with the asymmetric boundary (edges painted in red).

## Appendix C: Dynamics of a sparse model: Cayley tree

In this section we study the dynamics of Ising spin system which is governed by the Markov process of Eq. (A7). This system has a Cayley tree topology of degree k with r generations; all edges in this tree are symmetric except the boundary edges which are asymmetric (see Figure 2). The sites on the boundary are subject to the random time-dependent fields  \( \theta_{i}(t) \in \{-1,1\} \) , where  \( \mathrm{P}(\theta_{i}(t) = \pm1) = 1/2 \) .

Without the contribution of asymmetric boundary the process (A7) is converging to the equilibrium Gibbs-Boltzmann distribution with Hamiltonian (A8). For the ferromagnetic system with  \( J_{ij} = J > 0 \)  and  \( \theta_i = 0 \)  the free energy per spin  \( f(\beta) = -\frac{1}{\beta} \log 2 \cosh(\beta J) \)  (that gives the average internal energy per spin  \( \langle E \rangle = \frac{\partial}{\partial \beta} \beta f(\beta) = -\tanh(\beta J) \) ) is an analytic function of the inverse temperature  \( \beta = \frac{1}{T} \) , which rules out a phase transition in this system for any T > 0 [20].

Adding an asymmetric boundary disturbs the detailed balance condition and there is no guarantee that the system will end up in a thermal equilibrium state asymptotically. Nevertheless, the symmetric part of the system (provided that it is at a sufficient distance from the asymmetric boundary) exhibits equilibrium like behavior as can be seen in Figure 3.

Results obtained in the Figure 3 are also valid if a

[1] L. D. Landau and E. M. Lifshitz, Statistical physics (Pergamon Press: Oxford, 1969).

Cayley tree is embedded in the following random graph topology. Suppose we generate a very large random regular graph of degree k (N being the number of nodes). The number of short loops (of a finite length) is vanishing

![](./images/867772594198151658_6.jpg)

FIG. 3: Comparing the equilibrium energy  \( E = -\tanh(J/T) \)  (solid line) with the energy measured  \( (E(\sigma) = -\frac{1}{N} \sum_{\langle ij \rangle} J_{ij} \sigma_i \sigma_j) \)  in Monte Carlo simulation (symbols) on the symmetric part of a Cayley tree (of degree k = 3 and of radius r = 19) with asymmetric boundary. For this system  \( T_c = 0 \) . The measurements are taken away from the asymmetric boundary (with incoming edges, pointing towards the center, denoted a.b. in the figure) on a sub-tree of radius  \( r = \{10, 12, 14, 16\} \) . For comparison, the value of  \( E(\sigma) \)  for the total system (symbols labeled by 'bulk') is included. The case of a boundary with incoming edges is also compared with that of a boundary with equal (on average) number of incoming and outgoing edges.

with increasing N and only long loops of order  \( O(\log N) \)  are present in this graph [21]. By following the neighbors of an arbitrary node in this network and its neighbors of neighbors, etc. we can form a Cayley tree of radius r.

Suppose we pick one of these Cayley trees and make all the edges belonging to it symmetric and the rest of the edges in the network asymmetric (incoming with probability 1/2). The dynamics of the Ising spin on a Cayley tree is dominated by the dynamics of its boundary which is described by the set  \( \{m_{i}(t)\} \)  of local magnetizations  \( m_{i}(t)=\sum_{\sigma}\mathrm{P}_{t}(\sigma)\sigma_{i} \) , which in a very large system  \( (N\to\infty \)  with  \( r=O(N^{0}) \) ) are dominated by the asymmetric part of this system. However, we have shown in the Letter that after long time these local magnetizations are vanishing and the results obtained for the original Cayley tree configuration hold also here.

[2] A. C. C. Coolen and D. Sherrington, Physica A 200, 602

[2] A. C. C. Coolen and D. Sherrington, Physica A 200, 602
 

(1993).

[3] R. Graham and T. Tél, Phys. Rev. Lett. 52, 9 (1984).

[4] D. Fraiman, P. Balenzuela, J. Foss, and D. R. Chialvo, Phys. Rev. E 79, 061922 (2009).

[5] G. Werner, Biosystems 90, 496 (2007).

[6] D. K. Foley, J. Econ. Theory 62, 321 (1994).

[7] R. Balescu, Equilibrium and nonequilibrium statistical mechanics (New York: Wiley, 1975).

[8] K. Mimura and A. C. Coolen, J. Phys. A: Math. Theor. 42, 415001 (2009).

[9] P. Peretto, Biol. Cybern. 50, 51 (1984).

[10] S. N. Dorogovtsev, A. V. Goltsev, and J. F. F. Mendes, Rev. Mod. Phys. 80, 1275 (2008).

[11] A. C. C. Coolen, R. Kühn, and P. Sollich, Theory of Neural Information Processing Systems (Oxford University Press, 2005).

[12] M. Mezard and G. Parisi, Eur. Phys. J. B 20, 217 (2001).

[13] See Supplemental Material at [URL will be inserted by publisher] for details.

[14] E. Schneidman, M. J. Berry, R. Segev, and W. Bialek, Nature 440, 1007 (2006).

[15] W. Bialek, A. Cavagna, I. Giardina, T. Mora, E. Silvestri, M. Viale, and A. M. Walczak, ArXiv e-prints (2011), 1107.0604.

[16] D. T. Robb, P. A. Rikvold, A. Berger, and M. A. Novotny, Phys. Rev. E. 76, 021124 (2007).

[17] H. Nishimori, Statistical Physics of Spin Glasses and Information Processing (Oxford University Press, Oxford, 2001).

[18] D. Bedeaux, K. Lakatos-Lindenberg, and K. E. Shuler, J. Math. Phys. 12, 2116 (1971).

[19] C. De Dominicis, Phys. Rev. B 18, 4913 (1978).

[20] T. P. Eggarter, Phys. Rev. B. 9, 2989 (1974).

[21] E. Marinari and R. Monasson, J. Stat. Mech. Theory Exp. 2004, P09004 (2004).

[22] The term equilibrium-like behavior refers to systems where the average values of macroscopic observables are equal to those of their equilibrium counterparts, assuming that in very large systems only a limited number of observables can be measured.

[23] As we focus on the thermodynamic limit, a more careful scaling of the interactions is required. See Appendix for a detailed derivation that also accommodates more general interaction strengths and interaction disorder.

[24] We have removed (set to zero) generating fields in the functional (B20), external fields in the  \( \tau \) -system and set  \( \theta_{i}^{\sigma}(t)=\theta^{\sigma}(t) \)  in the  \( \sigma \) -system.
 
