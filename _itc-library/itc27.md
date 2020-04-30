---
title: ITC27
year: 2015
---

Becker, N. and Fidler, M.<br/>
**A Non-stationary Service Curve Model for Performance Analysis of Transient Phases**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277434'))
[\[Abstract\]](javascript:toggleVis('abstract_7277434'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277434.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/80d7b462a7d1a45cd420be31fa903535/itc)

<div id="7277434" style="display: none;" class="bibtex">@inproceedings{7277434,
    title         = { A Non-stationary Service Curve Model for Performance Analysis of Transient Phases },
    year          = { 2015 },
    author        = { Becker, N. and Fidler, M. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 116-124 },
    misc          = {   doi = 10.1109/ITC.2015.21 }
}</div>
<div id="abstract_7277434" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Steady-state solutions for a variety of relevant queueing systems are known today, e.g., from queueing theory, effective bandwidths, and network calculus. The behavior during transient phases, on the other hand, is understood to a much lesser extent as its analysis poses significant challenges. Considering the majority of short-lived flows, transient effects that have diverse causes, such as TCP slow start, sleep scheduling in wireless networks, or signalling in cellular networks, are, however, predominant. This paper contributes a general model of regenerative service processes to characterize the transient behavior of systems. The model leads to a notion of non-stationary service curves that can be conveniently integrated into the framework of the stochastic network calculus. We derive respective models of sleep scheduling and show the significant impact of transient phases on backlogs and delays. We also consider measurement methods that estimate the service of an unknown system from observations of selected probe traffic. We find that the prevailing rate scanning method does not recover the service during transient phases well. This limitation is fundamental as it is explained by the non-convexity of nonstationary service curves. A second key difficulty is proven to be due to the super-additivity of network service processes. We devise a novel two-phase probing technique that first determines a minimal pattern of probe traffic. This probe is used to obtain an accurate estimate of the unknown transient service.
</div>

Metzger, F. and Steindl, C. and Hossfeld, T.<br/>
**A Simulation Framework for Evaluating the QoS and QoE of TCP-based Streaming in an LTE Network**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277440'))
[\[Abstract\]](javascript:toggleVis('abstract_7277440'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277440.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/97e2a28ff90e63b7d722ce1283fb7bc3/itc)

<div id="7277440" style="display: none;" class="bibtex">@inproceedings{7277440,
    title         = { A Simulation Framework for Evaluating the QoS and QoE of TCP-based Streaming in an LTE Network },
    year          = { 2015 },
    author        = { Metzger, F. and Steindl, C. and Hossfeld, T. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 168-176 },
    misc          = {   doi = 10.1109/ITC.2015.27 }
}</div>
<div id="abstract_7277440" style="display: none;" class="abstract">
    <strong>Abstract:</strong> TCP-based streaming has garnered much research interest in the past few years. Yet it still remains difficult to evaluate the performance of such streaming approaches in mobile networks. In the past, this could be be partly attributed to the scarce availability of mobile network simulators but this circumstance has changed. Nevertheless, there are many open issues and challenges in video delivery over mobile networks.Inspired by the lack of tools for assessing video streaming QoS and QoE, we provide a streaming framework on top of one of the existing mobile network simulators. The framework is configurable and extensible enough to be able to be employed for many mobile and other network scenarios. The provided scenarios and example playback strategies are put to the test in some initial experiments. In these, a negative impact of mobility on the playback of a streaming video could already be revealed.
</div>

Hours, H. and Biersack, E. and Loiseau, P. and Finamore, A. and Mellia, M.<br/>
**A Study of the Impact of DNS Resolvers on Performance Using a Causal Approach**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277422'))
[\[Abstract\]](javascript:toggleVis('abstract_7277422'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277422.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/cf58811882d71cd246b555730e4c5cdb/itc)

<div id="7277422" style="display: none;" class="bibtex">@inproceedings{7277422,
    title         = { A Study of the Impact of DNS Resolvers on Performance Using a Causal Approach },
    year          = { 2015 },
    author        = { Hours, H. and Biersack, E. and Loiseau, P. and Finamore, A. and Mellia, M. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 10-18 },
    misc          = {   doi = 10.1109/ITC.2015.9 }
}</div>
<div id="abstract_7277422" style="display: none;" class="abstract">
    <strong>Abstract:</strong> For a user to access any resource on the Internet, it is necessary to first locate a server hosting the requested resource. The Domain Name System service (DNS) represents the first step in this process, translating a human readable name, the resource host name, into an IP address. With the expansion of Content Distribution Networks (CDNs), the DNS service has seen its importance increase. In a CDN, objects are replicated on different servers to decrease the distance from the client to a server hosting the object that needs to be accessed. The DNS service should improve user experience by directing its demand to the optimal CDN server. While most of the Internet Service Providers (ISPs) offer a DNS service to their customers, it is now common to see clients using a public DNS service instead. This choice may have an impact on Web browsing performance. In this paper we study the impact of choosing one DNS service instead of another and we compare the performance of a large European ISP DNS service with the one of a public DNS service, Google DNS. We propose a causal approach to expose the structural dependencies of the different parameters impacted by the DNS service used and we show how to model these dependencies with a Bayesian network. This model allows us to explain and quantify the benefits obtained by clients using their ISP DNS service and to propose a solution to further improve their performance.
</div>

Vitale, C. and Rizzo, G. and Rengarajan, B. and Mancuso, V.<br/>
**An Analytical Approach to Performance Analysis of Coupled Processor Systems**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277431'))
[\[Abstract\]](javascript:toggleVis('abstract_7277431'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277431.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/7404b66f1e06d94960ab9ceb1693b43a/itc)

<div id="7277431" style="display: none;" class="bibtex">@inproceedings{7277431,
    title         = { An Analytical Approach to Performance Analysis of Coupled Processor Systems },
    year          = { 2015 },
    author        = { Vitale, C. and Rizzo, G. and Rengarajan, B. and Mancuso, V. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 89-97 },
    misc          = {   doi = 10.1109/ITC.2015.18 }
}</div>
<div id="abstract_7277431" style="display: none;" class="abstract">
    <strong>Abstract:</strong> We consider a queuing system with coupled processors (CPS), in which the service rate at each queue varies over time in function of the set of active queues in the system. Performance analysis of CPS has so far been based on simulations or on complex Markov chains under restricting assumptions on input traffic statistics. In contrast, we propose a fully analytical approach to CPS, based on a worst case analysis of system dynamics, and applicable to a large family of traffic characterizations. We derive sufficient conditions for stability for traffic characterized stochastically as well as for traffic constrained by arrival curves, and we show how to compute bounds on backlog and delay. We illustrate our approach and assess our results by means of an example of coupling of wireless transmissions.
</div>

Wang, Shuo and Zhang, Xing and Zhang, Jiaxin and Feng, Jian and Wang, Wenbo and Xin, Ke<br/>
**An Approach for Spatial-Temporal Traffic Modeling in Mobile Cellular Networks**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277444'))
[\[Abstract\]](javascript:toggleVis('abstract_7277444'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277444.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/7223e2e78eaf95214447a937368908f0/itc)

<div id="7277444" style="display: none;" class="bibtex">@inproceedings{7277444,
    title         = { An Approach for Spatial-Temporal Traffic Modeling in Mobile Cellular Networks },
    year          = { 2015 },
    author        = { Wang, Shuo and Zhang, Xing and Zhang, Jiaxin and Feng, Jian and Wang, Wenbo and Xin, Ke },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 203-209 },
    misc          = {   doi = 10.1109/ITC.2015.31 }
}</div>
<div id="abstract_7277444" style="display: none;" class="abstract">
    <strong>Abstract:</strong> The volume and types of traffic data in mobile cellular networks have been increasing continuously. Meanwhile, traffic data change dynamically in several dimensions such as time and space. Thus, traffic modeling is essential for theoretical analysis and energy efficient design of future ultra-dense cellular networks. In this paper, the authors try to build a tractable and accurate model to describe the traffic variation pattern for a single base station in real cellular networks. Firstly a sinusoid superposition model is proposed for describing the temporal traffic variation of multiple base stations based on real data in a current cellular network. It shows that the mean traffic volume of many base stations in an area changes periodically and has three main frequency components. Then, lognormal distribution is verified for spatial modeling of real traffic data. The spatial traffic distributions at both spare time and busy time are analyzed. Moreover, the parameters of the model are presented in three typical regions: park, campus and central business district. Finally, an approach for combined spatial-temporal traffic modeling of single base station is proposed based on the temporal and spatial traffic distribution of multiple base stations. All the three models are evaluated through comparison with real data in current cellular networks. The results show that these models can accurately describe the variation pattern of real traffic data in cellular networks.
</div>

Ramakrishnan, A. and Westphal, C. and Markopoulou, A.<br/>
**An Efficient Delivery Scheme for Coded Caching**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277426'))
[\[Abstract\]](javascript:toggleVis('abstract_7277426'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277426.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/b47645b1a4047e1b3a34b9abc775a10e/itc)

<div id="7277426" style="display: none;" class="bibtex">@inproceedings{7277426,
    title         = { An Efficient Delivery Scheme for Coded Caching },
    year          = { 2015 },
    author        = { Ramakrishnan, A. and Westphal, C. and Markopoulou, A. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 46-54 },
    misc          = {   doi = 10.1109/ITC.2015.13 }
}</div>
<div id="abstract_7277426" style="display: none;" class="abstract">
    <strong>Abstract:</strong> We consider a network with several users trying to access a database of files stored at a server through a shared link. Each user is equipped with a cache, where files can be prefetched according to a caching policy which is mainly based on the popularities of the files. Coded caching tries to exploit coding opportunities created by cooperative caching and has been shown to significantly reduce the load on the shared link. Most of the prior works focused on optimizing the caching policy so as to minimize this expected load. Given the caching policy and the user demands, the problem of minimizing the load over the shared link is essentially an index coding problem. In this paper, we design a novel delivery scheme that builds on a prior scheme for the uniform demand case, but performs better in the non-uniform demand case. We also evaluate this delivery scheme for different caching policies.
</div>

Wu, Huaming and Knottenbelt, W. and Wolter, K.<br/>
**Analysis of the Energy-Response Time Tradeoff for Mobile Cloud Offloading Using Combined Metrics**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277436'))
[\[Abstract\]](javascript:toggleVis('abstract_7277436'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277436.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/e1084143d4c16781328ee253408d9f34/itc)

<div id="7277436" style="display: none;" class="bibtex">@inproceedings{7277436,
    title         = { Analysis of the Energy-Response Time Tradeoff for Mobile Cloud Offloading Using Combined Metrics },
    year          = { 2015 },
    author        = { Wu, Huaming and Knottenbelt, W. and Wolter, K. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 134-142 },
    misc          = {   doi = 10.1109/ITC.2015.23 }
}</div>
<div id="abstract_7277436" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Mobile offloading migrates heavy computation from mobile devices to cloud servers using one or more communication network channels. Communication interfaces vary in speed, energy consumption and degree of availability. We assume two interfaces: WiFi, which is fast with low energy demand but not always present and cellular, which is slightly slower has higher energy consumption but is present at all times. We study two different communication strategies: one that selects the best available interface for each transmitted packet and the other multiplexes data across available communication channels. Since the latter may experience interrupts in the WiFi connection packets can be delayed. We call it interrupted strategy as opposed to the uninterrupted strategy that transmits packets only over currently available networks. Two key concerns of mobile offloading are the energy use of the mobile terminal and the response time experienced by the user of the mobile device. In this context, we investigate three different metrics that express the energy-performance tradeoff, the known Energy-Response time Weighted Sum (EWRS), the Energy-Response time Product (ERP) and the Energy-Response time Weighted Product (ERWP) metric. We apply the metrics to the two different offloading strategies and find that the conclusions drawn from the analysis depend on the considered metric. In particular, while an additive metric is not normalised, which implies that the term using smaller scale is always favoured, the ERWP metric, which is new in this paper, allows to assign importance to both aspects without being misled by different scales. It combines the advantages of an additive metric and a product. The interrupted strategy can save energy especially if the focus in the tradeoff metric lies on the energy aspect. In general one can say that the uninterrupted strategy is faster, while the interrupted strategy uses less energy. A fast connection improves the response time much more than the - ast repair of a failed connection. In conclusion, a short down-time of the transmission channel can mostly be tolerated.
</div>

Akin, S. and Fidler, M.<br/>
**Backlog and Delay Reasoning in HARQ System**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277442'))
[\[Abstract\]](javascript:toggleVis('abstract_7277442'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277442.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/009f6cfbfdf5ef876bc01c5f1013d2e4/itc)

<div id="7277442" style="display: none;" class="bibtex">@inproceedings{7277442,
    title         = { Backlog and Delay Reasoning in HARQ System },
    year          = { 2015 },
    author        = { Akin, S. and Fidler, M. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 185-193 },
    misc          = {   doi = 10.1109/ITC.2015.29 }
}</div>
<div id="abstract_7277442" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Recently, hybrid-automatic-repeat-request (HARQ) systems have been favored in particular state-of-the-art communications systems since they provide the practicality of error detections and corrections aligned with repeat-requests when needed at receivers. The queueing characteristics of these systems have taken considerable focus since the current technology demands data transmissions with a minimum delay provisioning. In this paper, we investigate the effects of physical layer characteristics on data link layer performance in a general class of HARQ systems. Constructing a state transition model that combines queue activity at a transmitter and decoding efficiency at a receiver, we identify the probability of clearing the queue at the transmitter and the packet-loss probability at the receiver. We determine the effective capacity that yields the maximum feasible data arrival rate at the queue under quality-ofservice constraints. In addition, we put forward non-asymptotic backlog and delay bounds. Finally, regarding three different HARQ protocols, namely Type-I HARQ, HARQ-chase combining (HARQ-CC) and HARQ-incremental redundancy (HARQ-IR), we show the superiority of HARQ-IR in delay robustness over the others. However, we further observe that the performance gap between HARQ-CC and HARQ-IR is quite negligible in certain cases. The novelty of our paper is a general cross-layer analysis of these systems, considering encoding/decoding in the physical layer and delay aspects in the data-link layer.
</div>

Guillemin, F. and Elayoubi, S.E. and Robert, P. and Fricker, C. and Sericola, B.<br/>
**Controlling Impatience in Cellular Networks Using QoE-aware Radio Resource Allocation**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277439'))
[\[Abstract\]](javascript:toggleVis('abstract_7277439'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277439.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/f13687fadfa1183828dac9b9774ea8b8/itc)

<div id="7277439" style="display: none;" class="bibtex">@inproceedings{7277439,
    title         = { Controlling Impatience in Cellular Networks Using QoE-aware Radio Resource Allocation },
    year          = { 2015 },
    author        = { Guillemin, F. and Elayoubi, S.E. and Robert, P. and Fricker, C. and Sericola, B. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 159-167 },
    misc          = {   doi = 10.1109/ITC.2015.26 }
}</div>
<div id="abstract_7277439" style="display: none;" class="abstract">
    <strong>Abstract:</strong> We consider in this paper an important Quality of Experience (QoE) indicator in cellular networks that is reneging of users due to impatience. We specifically consider a cell under heavy load conditions, modeled as a multiclass Processor Sharing system, and compute the reneging probability by using a fluid limit analysis. In order to enhance the user QoE, we propose a radio resource allocation control scheme that minimizes the global reneging rates. This control scheme is based on the a-fair scheduling framework and adapts the scheduler parameter depending on the traffic load. While the proposed scheme is simple, our results show that it achieves important performance gains.
</div>

Leconte, M. and Lelarge, M. and Massoulie, L.<br/>
**Designing Adaptive Replication Schemes in Distributed Content Delivery Networks**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277424'))
[\[Abstract\]](javascript:toggleVis('abstract_7277424'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277424.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/d7278ce867cefd72c2f3bc4889b07cb7/itc)

<div id="7277424" style="display: none;" class="bibtex">@inproceedings{7277424,
    title         = { Designing Adaptive Replication Schemes in Distributed Content Delivery Networks },
    year          = { 2015 },
    author        = { Leconte, M. and Lelarge, M. and Massoulie, L. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 28-36 },
    misc          = {   doi = 10.1109/ITC.2015.11 }
}</div>
<div id="abstract_7277424" style="display: none;" class="abstract">
    <strong>Abstract:</strong> We address the problem of content replication in large distributed content delivery networks, composed of a data center assisted by many small servers with limited capabilities and located at the edge of the network. We aim at optimizing the placement of contents on the servers to offload the data center as much as possible. We model the sub-system constituted by the small servers as a loss network, each loss corresponding to a request to the data center. Based on large system / storage behavior, we obtain an asymptotic formula for the optimal replication of contents and propose adaptive schemes to attain it by reacting to losses, as well as faster algorithms which can react before losses occur. We show through simulations that our adaptive schemes outperform significantly standard replication strategies both in terms of loss rates and adaptation speed.
</div>

Larranaga, M. and Boxma, O.J. and Nunez-Queija, R. and Squillante, M.S.<br/>
**Efficient Content Delivery in the Presence of Impatient Jobs**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277429'))
[\[Abstract\]](javascript:toggleVis('abstract_7277429'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277429.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/bdacf59f8158460b8d583d17ced40fbc/itc)

<div id="7277429" style="display: none;" class="bibtex">@inproceedings{7277429,
    title         = { Efficient Content Delivery in the Presence of Impatient Jobs },
    year          = { 2015 },
    author        = { Larranaga, M. and Boxma, O.J. and Nunez-Queija, R. and Squillante, M.S. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 73-81 },
    misc          = {   doi = 10.1109/ITC.2015.16 }
}</div>
<div id="abstract_7277429" style="display: none;" class="abstract">
    <strong>Abstract:</strong> We consider a content delivery problem in which jobs are processed in batches and may abandon before their service has been initiated. We model the problem as a Markovian single-server queue and analyze two different settings: (1) the system is cleared as soon as the server is activated, i.e., service rate μ = ∞, and (2) the service speed is exponentially distributed with rate μ <; ∞. The objective is to determine the optimal clearing strategy that minimizes the average cost incurred by holding jobs in the queue, having jobs renege, and performing setups. This last cost is incurred upon activation of the server in the case μ = ∞, and per unit of time the server is active otherwise. Our first contribution is to prove that policies of threshold type are optimal in both frameworks. In order to do so we have used the Smoothed Rate Truncation method which overcomes the problem arising from unbounded transition rates. For our second contribution, we derive the steady-state job-length distribution under threshold policies. The latter yields a characterization of the optimal threshold strategy, which can be easily implemented. Finally, we present numerical results for our solution across a wide range of parameters. We show that the performance of nonoptimal threshold policies can be very poor, which highlights the importance of computing the optimal threshold.
</div>

Hyytia, E. and Righter, R.<br/>
**Fairness through Linearly Increasing Holding Costs in Systems of Parallel Servers with Setup Delays**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277437'))
[\[Abstract\]](javascript:toggleVis('abstract_7277437'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277437.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/6ec0ba0a2dc4c61557fd3e9fac4d19fd/itc)

<div id="7277437" style="display: none;" class="bibtex">@inproceedings{7277437,
    title         = { Fairness through Linearly Increasing Holding Costs in Systems of Parallel Servers with Setup Delays },
    year          = { 2015 },
    author        = { Hyytia, E. and Righter, R. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 143-151 },
    misc          = {   doi = 10.1109/ITC.2015.24 }
}</div>
<div id="abstract_7277437" style="display: none;" class="abstract">
    <strong>Abstract:</strong> We consider a system of parallel servers, where arriving jobs are routed to one of the servers upon arrival. The standard objective of minimizing the mean sojourn time (delay) does not enforce any kind of fairness in the system and it is acceptable, e.g., to delay one job a lot if it reduces the sojourn time of some other jobs. We take fairness into account by defining a linearly increasing instantaneous holding cost rate by two job-specific non-negative random variables, (ai; ßi), that can depend on the service time. We focus on first-come-first-served (FCFS) and preemptive last-come-first-served (LCFS) scheduling, and derive the so-called value functions for the corresponding M/G/1 queues. Then we apply these results and obtain cost aware dispatching policies by means of policy improvement and lookahead. The policies are finally evaluated numerically.
</div>

Van Hautegem, K. and Rogiest, W. and Bruneel, H.<br/>
**Fill the Void: Improved Scheduling for Optical Switching**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277430'))
[\[Abstract\]](javascript:toggleVis('abstract_7277430'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277430.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/2018974a11813befc3ad7f33ac955c5b/itc)

<div id="7277430" style="display: none;" class="bibtex">@inproceedings{7277430,
    title         = { Fill the Void: Improved Scheduling for Optical Switching },
    year          = { 2015 },
    author        = { Van Hautegem, K. and Rogiest, W. and Bruneel, H. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 82-88 },
    misc          = {   doi = 10.1109/ITC.2015.17 }
}</div>
<div id="abstract_7277430" style="display: none;" class="abstract">
    <strong>Abstract:</strong> With ever-increasing demand for bandwidth, optical packet/burst switching is proposed to utilize more of the available capacity of optical networks in the future. In these packet-based switching techniques, packet contention on a single wavelength is resolved effectively by means of Fiber Delay Lines. The involved scheduling algorithms are typically designed to minimize packet loss and/or packet delay. By filling so-called voids, void-filling algorithms are known to outperform their non-void-filling counterparts. This however comes at a large computational cost as the void-filling algorithms have to keep track of beginnings and endings of all voids. This is opposed to the non-void-filling algorithms which only have to keep track of a single system state variable. We therefore propose a new type of algorithm that selectively creates voids that are larger than strictly needed, only when these will likely be filled. Results obtained by Monte Carlo simulation show that selective void creation can jointly reduce packet loss by 50% and packet delay by 18%, without imposing a high computational cost.
</div>

Kleinrouweler, J.W. and Cabrero, S. and van der Mei, R. and Cesar, P.<br/>
**Modeling Stability and Bitrate of Network-Assisted HTTP Adaptive Streaming Players**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277441'))
[\[Abstract\]](javascript:toggleVis('abstract_7277441'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277441.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/a9412ad01595b340d7eb931c37781c4f/itc)

<div id="7277441" style="display: none;" class="bibtex">@inproceedings{7277441,
    title         = { Modeling Stability and Bitrate of Network-Assisted HTTP Adaptive Streaming Players },
    year          = { 2015 },
    author        = { Kleinrouweler, J.W. and Cabrero, S. and van der Mei, R. and Cesar, P. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 177-184 },
    misc          = {   doi = 10.1109/ITC.2015.28 }
}</div>
<div id="abstract_7277441" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Viewers using HTTP Adaptive Streaming (HAS) without sufficient bandwidth undergo frequent quality switches that hinder their watching experience. This situation, known as instability, is produced when HAS players are unable to accurately estimate the available bandwidth. Moreover, when several players stream over a bottleneck link, their individual adaptation techniques may result in an unfair share of the channel. These are two detrimental issues in HAS technology, which is otherwise very attractive. To overcome them, a group of solutions are proposed in the literature that can be classified as network-assisted HAS. Solving stability and fairness only in the player is difficult, because a player has a limited view of the network. Using information from network devices can help players in making better adaptation decisions. The contribution of this paper is three-fold. First, we describe our implementation in the form of an HTTP proxy server, and show that both stability and fairness are strongly improved. Second, we present an analytical model that allows to compute the number of changes in video quality and the bitrate of a video stream. Third, we validate the accuracy of the model by comparing the model-based estimations for the number of changes in video quality and for the mean bitrate of a video stream, with results in a real implementation of our HAS assistant. The results show that the model-based results are highly accurate. As such, this model is useful in practice for planning video delivery networks that use in-network HAS assistants, and enables us to analyze the stability and the mean bitrate of HAS streams prior to real deployment.
</div>

Maccio, V.J. and Down, D.G.<br/>
**On Optimal Control for Energy-Aware Queueing Systems**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277432'))
[\[Abstract\]](javascript:toggleVis('abstract_7277432'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277432.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/4984daa995ed7790aa04d95d42dcc035/itc)

<div id="7277432" style="display: none;" class="bibtex">@inproceedings{7277432,
    title         = { On Optimal Control for Energy-Aware Queueing Systems },
    year          = { 2015 },
    author        = { Maccio, V.J. and Down, D.G. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 98-106 },
    misc          = {   doi = 10.1109/ITC.2015.19 }
}</div>
<div id="abstract_7277432" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Over the past few years, energy provisioning in server farms and data-centres has become an active area of research. As such, many models have been proposed where an individual server has setup times and can switch between two different energy states (on and off). To make such models tractable, assumptions are usually made on the type of policies the system can implement. However, it is often not known if such assumptions allow for the model to capture the optimal policy, or if such a model will be strictly suboptimal. In this work we model such systems using Markov Decision Processes (MDPs) and derive several structural properties which (partially) describe the optimal policy. These properties reduce the set of feasible policies significantly, allowing one to describe the optimal policy by a set of thresholds which have considerable structure. In addition to the analysis, we discuss the current literature in the context of our results.
</div>

Kamiyama, N. and Takahashi, Y. and Ishibashi, K. and Shiomoto, K. and Otoshi, T. and Ohsita, Y. and Murata, M.<br/>
**Optimizing Cache Location and Route on CDN Using Model Predictive Control**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277425'))
[\[Abstract\]](javascript:toggleVis('abstract_7277425'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277425.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/3e23fb38472dabef6afd70d824be925f/itc)

<div id="7277425" style="display: none;" class="bibtex">@inproceedings{7277425,
    title         = { Optimizing Cache Location and Route on CDN Using Model Predictive Control },
    year          = { 2015 },
    author        = { Kamiyama, N. and Takahashi, Y. and Ishibashi, K. and Shiomoto, K. and Otoshi, T. and Ohsita, Y. and Murata, M. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 37-45 },
    misc          = {   doi = 10.1109/ITC.2015.12 }
}</div>
<div id="abstract_7277425" style="display: none;" class="abstract">
    <strong>Abstract:</strong> In content delivery services, cache-server selection and route control are independently operated by content delivery network (CDN) providers and Internet service providers (ISPs), respectively. However, the number of ISPs providing CDN service has been increasing, and they can optimize the cache-server and delivery-route selection simultaneously. In this paper, we investigate the effect of jointly controlling these two operations. To continuously maintain a desirable state over a long time span in an environment in which estimating future demand is not easy, we should use an optimization method with which we can repeat the optimization procedure continuously. Therefore, we propose a method of optimizing the cache-server selection using the model predictive control (MPC), which has been widely used in system control. We also propose a method of simultaneously optimizing both the cache-server and delivery-route selection using the MPC. Through numerical evaluation using two actual network topologies of Tier-1 ISPs and the access log data of VoD services, we confirm that we can achieve almost the same effect by optimizing only cache-server selection using the MPC compared with optimizing both operations simultaneously. We also confirm that the number of failed requests that are not accommodated in the system can be reduced by about 1/30 with the proposed methods using the MPC.
</div>

Elayoubi, S.E. and Roberts, J.<br/>
**Performance Evaluation of Video Transcoding and Caching Solutions in Mobile Networks**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277427'))
[\[Abstract\]](javascript:toggleVis('abstract_7277427'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277427.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/7945b57ab5b0b61b920d1f14e78dc399/itc)

<div id="7277427" style="display: none;" class="bibtex">@inproceedings{7277427,
    title         = { Performance Evaluation of Video Transcoding and Caching Solutions in Mobile Networks },
    year          = { 2015 },
    author        = { Elayoubi, S.E. and Roberts, J. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 55-63 },
    misc          = {   doi = 10.1109/ITC.2015.14 }
}</div>
<div id="abstract_7277427" style="display: none;" class="abstract">
    <strong>Abstract:</strong> The rapid growth in demand for video streaming applications is stressing the performance of wireless access networks. To alleviate congestion, vendors currently propose devices to be placed in the operator's network that transcode videos to a lower rate in order to reduce traffic volume in case of congestion. The devices are also able to cache popular videos, both to reduce the burden of transcoding and to alleviate backhaul load. The paper proposes a model of this augmented radio access network enabling an evaluation of the performance benefits for given transcoding and caching capacities. Our results show that a gain in cell capacity of 15% can be realized with moderate transcoding and cache capacities.
</div>

Fiadino, P. and D'Alconzo, A. and Schiavone, M. and Casas, P.<br/>
**RCATool - A Framework for Detecting and Diagnosing Anomalies in Cellular Networks**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277443'))
[\[Abstract\]](javascript:toggleVis('abstract_7277443'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277443.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/6c854e1ea689b666dba85fe2f01638f4/itc)

<div id="7277443" style="display: none;" class="bibtex">@inproceedings{7277443,
    title         = { RCATool - A Framework for Detecting and Diagnosing Anomalies in Cellular Networks },
    year          = { 2015 },
    author        = { Fiadino, P. and D'Alconzo, A. and Schiavone, M. and Casas, P. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 194-202 },
    misc          = {   doi = 10.1109/ITC.2015.30 }
}</div>
<div id="abstract_7277443" style="display: none;" class="abstract">
    <strong>Abstract:</strong> The DNS protocol has proved to be a valuable means for identifying and dissecting large-scale anomalies in omnipresent Over The Top (OTT) Internet services. In this paper, we present and evaluate a framework for detecting and diagnosing traffic anomalies via DNS traffic analysis. Detection of such anomalies is achieved by monitoring different DNS-related symptomatic features, flagging a warning as soon as one or more of them show a significant change. The investigation of the root causes for such deviations is done by looking at significant changes in a number of diagnostic features (i.e., device manufacturer and OS, requested host name, error codes, etc.), which convey information directly linked to the potential origins of the detected anomalies. For the purpose of detecting significant changes in the time-series of diagnostic features, we propose two different schemes: the first is based of change point detection applied to the entropy of the considered features, the second considers the full statistical distribution of the traffic features. The proposed solutions are tested and compared using both real and synthetic data from a nationwide mobile ISP, the latter generated from real traffic statistics to resemble the real mobile network traffic. To show the operational value of the proposed framework, we report the results of the diagnosis in two prototypical cases.
</div>

Bosman, J. and van den Berg, H. and van der Mei, R.<br/>
**Real-Time QoS Control for Service Orchestration**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277438'))
[\[Abstract\]](javascript:toggleVis('abstract_7277438'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277438.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/4797fa874ae4059079adaf0b2e0a31b3/itc)

<div id="7277438" style="display: none;" class="bibtex">@inproceedings{7277438,
    title         = { Real-Time QoS Control for Service Orchestration },
    year          = { 2015 },
    author        = { Bosman, J. and van den Berg, H. and van der Mei, R. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 152-158 },
    misc          = {   doi = 10.1109/ITC.2015.25 }
}</div>
<div id="abstract_7277438" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Service orchestration has become the predominant paradigm that enables businesses to combine and integrate services offered by third parties. For the commercial viability of orchestrated services, it is crucial that they are offered at sharp price-quality ratios. A complicating factor is that many attractive third-party services often show highly variable service quality. This raises the need for mechanisms that promptly adapt the orchestration to changes in the quality delivered by third party services. In this paper, we propose a real-time QoS control mechanism that dynamically optimizes service orchestration in real time by learning and adapting to changes in third party service response time behaviors. Our approach combines the power of learning and adaptation with the power of dynamic programming. The re¬sults show that real-time service re-compositions lead to dramatic savings of cost, while meeting the service quality requirements of the end-users. The challenge here is to respond to signi?cant response-time changes in a timely manner, while not wasting CPU cycles on unnecessary orchestration updates. Experimental results performed in a test-lab environment demonstrate that a few orchestration updates are suf?cient to achieve this.
</div>

De Vleeschauwer, D. and Feyaerts, B. and Bruneel, H. and Wittevrongel, S.<br/>
**Scheduling Announced Requests for Streamed Information**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277428'))
[\[Abstract\]](javascript:toggleVis('abstract_7277428'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277428.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/ecf505fc4d2ee7d7e82d57b744866d12/itc)

<div id="7277428" style="display: none;" class="bibtex">@inproceedings{7277428,
    title         = { Scheduling Announced Requests for Streamed Information },
    year          = { 2015 },
    author        = { De Vleeschauwer, D. and Feyaerts, B. and Bruneel, H. and Wittevrongel, S. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 64-72 },
    misc          = {   doi = 10.1109/ITC.2015.15 }
}</div>
<div id="abstract_7277428" style="display: none;" class="abstract">
    <strong>Abstract:</strong> We analyse a scheduling system in which users announce requests for information from a server some time before they actually need this information. Each constituent of the requested information has its own specific deadline, which is characteristic for applications that gradually consume a stream of information (e.g., video). For that purpose, a request fully specifies when the requesting user needs each constituent of this information. Since each user device is equipped with a buffer, the server can exploit this detailed timing information to deliver parts of the requested information upfront. The more the requests are announced in advance, the better the ability of the server to avoid deadline violations. We investigate for a given server capacity via semi-analytical techniques complemented with simulations how much the requests need to be announced in advance to essentially avoid violating all deadlines.
</div>

Boussard, M. and Bui, Dinh Thai and Ciavaglia, L. and Douville, R. and Le Pallec, M. and Le Sauze, N. and Noirie, L. and Papillon, S. and Peloso, P. and Santoro, F.<br/>
**Software-Defined LANs for Interconnected Smart Environment**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277446'))
[\[Abstract\]](javascript:toggleVis('abstract_7277446'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277446.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/49aa2412c1a0ffc412ac04719da2beda/itc)

<div id="7277446" style="display: none;" class="bibtex">@inproceedings{7277446,
    title         = { Software-Defined LANs for Interconnected Smart Environment },
    year          = { 2015 },
    author        = { Boussard, M. and Bui, Dinh Thai and Ciavaglia, L. and Douville, R. and Le Pallec, M. and Le Sauze, N. and Noirie, L. and Papillon, S. and Peloso, P. and Santoro, F. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 219-227 },
    misc          = {   doi = 10.1109/ITC.2015.33 }
}</div>
<div id="abstract_7277446" style="display: none;" class="abstract">
    <strong>Abstract:</strong> In this paper, we propose a solution to delegate the control and the management of the network connecting the many devices of a smart environment to a software entity, while keeping end-users in control of what is happening in their networks. For this, we rely on the logical manipulation of all connected devices through device abstraction and network programmability. Applying Software Defined Networking (SDN) principles, we propose a software-based solution that we call Software-Defined LANs in order to interconnect devices of smart environments according to the services the users are requesting or expecting.We define the adequate virtualization framework based on Virtual Objects and Communities of Virtual Objects. Using these virtual entities, we apply the SDN architectural principles to define a generic architecture that can be applied to any smart environment. Then we describe a prototype implementing these concepts in the home networking context, through a scenario in which users of two different homes can easily interconnect two private but shareable DLNA devices in a dedicated video-delivery SD-LAN. Finally we provide a discussion of the benefits and challenges of our approach regarding the generalization of SDN principles, autonomic features, Internet of Things scalability, security and privacy aspects enabled by SD-LANs intrinsic properties.
</div>

Lange, S. and Gebert, S. and Spoerhase, J. and Rygielski, P. and Zinner, T. and Kounev, S. and Tran-Gia, Phuoc<br/>
**Specialized Heuristics for the Controller Placement Problem in Large Scale SDN Networks**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277445'))
[\[Abstract\]](javascript:toggleVis('abstract_7277445'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277445.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/cb9cd46c02540d355a9c67a225e3e69f/itc)

<div id="7277445" style="display: none;" class="bibtex">@inproceedings{7277445,
    title         = { Specialized Heuristics for the Controller Placement Problem in Large Scale SDN Networks },
    year          = { 2015 },
    author        = { Lange, S. and Gebert, S. and Spoerhase, J. and Rygielski, P. and Zinner, T. and Kounev, S. and Tran-Gia, Phuoc },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 210-218 },
    misc          = {   doi = 10.1109/ITC.2015.32 }
}</div>
<div id="abstract_7277445" style="display: none;" class="abstract">
    <strong>Abstract:</strong> The Software Defined Networking (SDN) concept introduces a paradigm shift in the networking world towards an externalized control plane which is logically centralized. When designing an SDN-based WAN architecture, it is of vital importance to find a feasible solution to the controller placement problem, i.e., to decide where to position a limited amount of resources within the network. In addition to time-independent constraints regarding aspects like scalability, resilience, and control plane communication delays, dynamically changing network conditions like traffic patterns or bandwidth demands need to be considered as well. Consequently, such dynamic environments call for a regular and fast recalculation of placements in order to adapt to the current situation in a timely manner. While an exhaustive evaluation of all possible solutions can be performed within a practically feasible time frame for small and medium-sized networks, such an approach is out of scope for large problem instances which have significantly higher time and memory requirements. Therefore, this work investigates a specialized heuristic, which takes into account a particular set of optimization objectives and returns solutions representing the possible trade-offs between them. Due to its low computation time and acceptable margin of error, this heuristic can be employed by automatic decision systems operating in dynamic environments.
</div>

Mukhopadhyay, A. and Mazumdar, R.R. and Guillemin, F.<br/>
**The Power of Randomized Routing in Heterogeneous Loss Systems**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277435'))
[\[Abstract\]](javascript:toggleVis('abstract_7277435'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277435.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/f14a910b73f11972315727f295a80132/itc)

<div id="7277435" style="display: none;" class="bibtex">@inproceedings{7277435,
    title         = { The Power of Randomized Routing in Heterogeneous Loss Systems },
    year          = { 2015 },
    author        = { Mukhopadhyay, A. and Mazumdar, R.R. and Guillemin, F. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 125-133 },
    misc          = {   doi = 10.1109/ITC.2015.22 }
}</div>
<div id="abstract_7277435" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Motivated by cloud computing applications, we consider a multi-server system, consisting of a large number of parallel servers, where jobs arrive according to a Poisson process and are assigned to the servers for processing. Each server has the capacity to process only a finite number of jobs simultaneously and different servers have different capacities. A job is accepted for processing only if there is a vacancy available at the server to which it is assigned. Otherwise, the job is discarded or blocked. We consider randomized schemes to assign jobs to servers with the aim of reducing the average blocking probability of jobs in the system. In particular, we consider a scheme that assigns an incoming job to the server having maximum available vacancy among d randomly sampled servers. We consider the system in the limit where both the number of servers and the arrival rate of jobs are scaled by a large factor. This gives rise to a mean field analysis. We show that in the limiting system servers behave independently. Stationary tail probabilities of server occupancies are obtained from the stationary solution of the mean field which is shown to be unique and globally attractive. We further characterize the rate of decay of the stationary tail probabilities. Numerical results suggest that the proposed scheme significantly reduces the average blocking probability of jobs compared to static schemes that probabilistically route jobs to servers independently of their states.
</div>

Ravaioli, R. and Urvoy-Keller, G. and Barakat, C.<br/>
**Towards a General Solution for Detecting Traffic Differentiation at the Internet Access**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277421'))
[\[Abstract\]](javascript:toggleVis('abstract_7277421'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277421.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/92c348b525b80de5af383e84094f3544/itc)

<div id="7277421" style="display: none;" class="bibtex">@inproceedings{7277421,
    title         = { Towards a General Solution for Detecting Traffic Differentiation at the Internet Access },
    year          = { 2015 },
    author        = { Ravaioli, R. and Urvoy-Keller, G. and Barakat, C. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 1-9 },
    misc          = {   doi = 10.1109/ITC.2015.8 }
}</div>
<div id="abstract_7277421" style="display: none;" class="abstract">
    <strong>Abstract:</strong> In recent years network neutrality has been widely debated from both technical and economic points of view. Various cases of traffic differentiation at the Internet access have been reported throughout the last decade, in particular aimed at bandwidth consuming traffic flows. In this paper we present a novel application-agnostic method for the detection of traffic differentiation, through which we are able to correctly identify where a shaper is located with respect to the user and evaluate whether it affected delays, packet losses or both. The tool we propose, ChkDiff, replays the user's own traffic in order to target routers at the first few hops from the user. By comparing the resulting flow delays and losses to the same router against one other, and analyzing the behaviour on the immediate router topology spawning from the user end-point, ChkDiff manages to detect instances of traffic shaping. We provide a detailed description of the design of the tool for the case of upstream traffic, the technical issues it overcomes and a validation in controlled scenarios.
</div>

Bonald, T.<br/>
**Traffic Models for User-Level Performance Evaluation in Data Networks**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277433'))
[\[Abstract\]](javascript:toggleVis('abstract_7277433'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277433.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/a2cd249261e071b13ca1dfda20dcb577/itc)

<div id="7277433" style="display: none;" class="bibtex">@inproceedings{7277433,
    title         = { Traffic Models for User-Level Performance Evaluation in Data Networks },
    year          = { 2015 },
    author        = { Bonald, T. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 107-115 },
    misc          = {   doi = 10.1109/ITC.2015.20 }
}</div>
<div id="abstract_7277433" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Traffic modeling is key to the capacity planning of data networks. Usual models rely on the implicit assumption that each user generates data flows in series, one after the other, the ongoing flows sharing equitably the considered backhaul link. We relax this assumption and consider the more realistic case where users may generate several data flows in parallel, these flows having to share the user's access line as well. We derive explicit user-level performance metrics like mean throughput and congestion rate in this context, assuming balanced fair sharing between ongoing flows. These results generalize existing ones in that both match in the limit of an infinite number of access lines.
</div>

Giordano, D. and Traverso, S. and Grimaudo, L. and Mellia, M. and Baralis, E. and Tongaonkar, A. and Saha, S.<br/>
**YouLighter: An Unsupervised Methodology to Unveil YouTube CDN Changes**<br/>
In *Teletraffic Congress (ITC 27), 2015 27th International*.  2015<br/>
[\[BibTeX\]](javascript:toggleVis('7277423'))
[\[Abstract\]](javascript:toggleVis('abstract_7277423'))
[\[Download\]](https://gitlab2.informatik.uni-wuerzburg.de/itc-conference/itc-conference-public/-/raw/master/itc27/7277423.pdf?inline=true)
[\[BibSonomy\]](https://www.bibsonomy.org/bibtex/3b75b7fc9c6656219b8870cda07b9894/itc)

<div id="7277423" style="display: none;" class="bibtex">@inproceedings{7277423,
    title         = { YouLighter: An Unsupervised Methodology to Unveil YouTube CDN Changes },
    year          = { 2015 },
    author        = { Giordano, D. and Traverso, S. and Grimaudo, L. and Mellia, M. and Baralis, E. and Tongaonkar, A. and Saha, S. },
    booktitle     = { Teletraffic Congress (ITC 27), 2015 27th International },
    month         = { Sept },
    pages         = { 19-27 },
    misc          = {   doi = 10.1109/ITC.2015.10 }
}</div>
<div id="abstract_7277423" style="display: none;" class="abstract">
    <strong>Abstract:</strong> YouTube relies on a massively distributed Content Delivery Network (CDN) to stream the billions of videos in its catalogue. Unfortunately, very little information about the design of such CDN is available. This, combined with the pervasiveness of YouTube, poses a big challenge for Internet Service Providers (ISPs), which are compelled to optimize end-users' Quality of Experience (QoE) while having no control on the CDN decisions.This paper presents YouLighter, an unsupervised technique to identify changes in the YouTube CDN. YouLighter leverages only passive measurements to cluster co-located identical caches into edge-nodes. This automatically unveils the structure of YouTube's CDN. Further, we propose a new metric, called Pattern Dissimilarity, that compares the clustering obtained from two different time snapshots, to pinpoint sudden changes. While several approaches allows us to compare the clustering results from the same dataset, no technique measures the similarity of clusters from different datasets. Hence, we develop a novel methodology, based on the Pattern Dissimilarity, to solve this problem.By running YouLighter over 10-month long traces obtained from ISPs, we pinpoint both sudden changes in edge-node allocation, and modifications to the cache allocation policy which actually impair the QoE that the end-users perceive.
</div>
