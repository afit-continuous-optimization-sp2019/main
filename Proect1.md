# Lifting / robust optimization
[This paper](https://hal.archives-ouvertes.fr/hal-01718012/document) looks very interesting to me.  Robust cost functions are often used in navigation and other places where outliers (e.g., faulty sensor measurements) may be present.  This paper claims that by using "lifting" they get much more accurate and better convergence properties.  Is this true for cases that we are interested in?  What is the cost computationally?  Are there ways we can speed it up?

* For an introduction to lifting, [this paper](ftp://ftp.esat.kuleuven.be/pub/SISTA/ida/reports/10-45.pdf) looks good.
* The paper that started this author's thoughts is [here](https://link.springer.com/chapter/10.1007%2F978-3-319-10602-1_50).  This may be the best paper to focus on.
* [A survey of robust cost techniques](http://openaccess.thecvf.com/content_ECCV_2018/papers/Christopher_Zach_Descending_lifting_or_ECCV_2018_paper.pdf), by the same author.
* [This paper](http://bmvc2018.org/contents/papers/0791.pdf) may be this author's most advanced technique.

Other robust optimization approaches include:
* [Switchable constraints](https://scholar.google.com/scholar_url?url=https://www.researchgate.net/profile/Niko_Suenderhauf/publication/261353750_Switchable_constraints_for_robust_pose_graph_SLAM/links/5641b16108ae24cd3e42560c.pdf&hl=en&sa=T&oi=gsb-gga&ct=res&cd=0&d=16404594540061172908&ei=HBulXInNHIKHygSUh7b4Cg&scisig=AAGBfm0KcrxqgfunfpgEVY9Nc6vD1kH-0g)
* [Max-mixtures](https://scholar.google.com/scholar_url?url=http://april.eecs.umich.edu/pdfs/olson2013ijrr_AP.pdf&hl=en&sa=T&oi=gsb-gga&ct=res&cd=0&d=661224392318639401&ei=VRulXP7nGIa8ygSn2InwBA&scisig=AAGBfm2wG3YFm5wAM-l5tCu3_D9AUQxPmw)
* [Dynamic Covariance Scaling](https://scholar.google.com/scholar_url?url=http://www.lifelong-navigation.eu/files/agarwal13_icra_ws.pdf&hl=en&sa=T&oi=gsb-gga&ct=res&cd=0&d=15927959963410715082&ei=cBulXIvDF8H9yQSBpKO4CQ&scisig=AAGBfm1-SICzNlW9dbAZ9GhwmiQXt3b5fQ)
* [Convex Relaxations](https://arxiv.org/pdf/1801.02112.pdf)

# Distributed optimization
Several techniques lately have introduced distributed optimization techniques using "Alternating Direction Method of Multipliers".
* An introductory paper is [here](http://users.eecs.northwestern.edu/~erminwei/DistributedADMMCDC-v7.pdf)
* Using ADMM to solve SLAM [here](https://www.cc.gatech.edu/~dellaert/pubs/Choudhary15iros.pdf)

It also sounds like some of the older techniques generally preferred a conjugate gradient method.  Why is one method better than the other?  In which cases are they better?


# Certifiably Correct SLAM
When running a large optimization procedure, it would be nice to know if you have converged to a local or global optimum.  [This paper](https://dspace.mit.edu/handle/1721.1/107296) claims to do that for the SLAM problem

# Variational Inference
When performing machine learning, one common task is to take a set of samples and create a parametric distribution that is "close" to those samples in some way.  Typically, the Kullback-Leibler divergence is the metric that is minimized.  In Christopher Bishop's book "Pattern Recognition and Machine Learning", and expectation maxmimization (EM) procedure is described to find the best mixture of Gaussians to represent a set of samples.  The problem is that EM can take a long time to converge.  [This paper](https://www.cs.cmu.edu/~rsalakhu/papers/emecg.pdf) claims to have a much quicker way to run EM.  (Basically, it claims that EM is similar to gradient descent, while other Newton-type methods can converge quicker).

Some other papers that may be of interest in this problem include:
* [A paper](https://arxiv.org/ftp/arxiv/papers/1206/1206.6427.pdf) saying it can converge more quickly for certain types of Gaussian Mixture models
* [This paper](https://link.springer.com/content/pdf/10.1007/BF01589116.pdf) talks about a "limited memory BFGS" approach that should do operate more quickly than EM approaches
* [This paper](https://www-sciencedirect-com.afit.idm.oclc.org/science/article/pii/S0031320312002117) modifies a cost function with an "entropy" term to try and more quickly solve the general EM problem

# Quadratic Programming
Chapter 16 of the book introduces a method for solving a least squares type problem, but with multiple constraints imposed on that problem.  I am interested in knowing if this could be used for loop-closure with SLAM in two scenarios.  One, where the IMU data is the quadratic expression to be minimized, but with loop-closing constraints.  The second, more challenging, would be minimum distances apart for some nodes in a SLAM framework.