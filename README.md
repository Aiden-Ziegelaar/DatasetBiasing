# Dataset Selection Demo

This repo is a super quick demo on how a dataset can be rebiased to
accentuate features of interest. 

In the notebook two datasets are compared, one containing the original 
dataset with a 16% attrition rate, and a model that randomly selects an
amount of non-attrited customers equal to the attrited customers. By 
doing this we decrease the overall accuracy of our model down 
(from 85.3% to 80.0%) to provide a massive increase in the correctly identified
attrited customers (from 3.1% to 64.2%) on the same data.

This is just a quick and simple demo with no optimisation performed to 
demonstrate how important building your dataset correctly is before you 
even get to model construction.

Cheers for reading!