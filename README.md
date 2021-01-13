# Dataset Selection Demo

## DNN

This repo is a super quick demo on how a dataset can be rebiased or pruned to
accentuate features of interest. 

In the notebook two datasets are compared, one containing the original 
dataset with a 16% attrition rate, and a model that randomly selects an
amount of non-attrited customers equal to 0.8 * the attrited customers. By 
doing this we decrease the overall accuracy of our model
(down from 83.6% to 80.6%) to provide a massive increase in the correctly identified
attrited customers (up from 2.8% to 66.2%) on the same data.

## Random Forest

This demo was mostly just about pruning datasets to enhance features on DNNs.
The random forest implementation compared to this (pretty basic) DNN was both faster 
and more accurate. Goes to show that when all you have is a hammer everything
looks like a nail.

Cheers for reading!