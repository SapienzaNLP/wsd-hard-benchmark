<div align="center">    
 
# Nibbling at the Hard Core of Word Sense Disambiguation

[![Paper](http://img.shields.io/badge/paper-ACL--anthology-B31B1B.svg)]()
[![Conference](http://img.shields.io/badge/conference-ACL--2022-4b44ce.svg)](https://www.2022.aclweb.org/)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

</div>

## Cite this work
If you use any part of this work, please consider citing the paper as follows:

```
@inproceedings{maru-etal-2022-nibbling,
    title      = "Nibbling at the Hard Core of {W}ord {S}ense {D}isambiguation",
    author     = "Maru, Marco and Conia, Simone and Bevilacqua, Michele and Navigli, Roberto",
    booktitle  = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL 2022)",
    month      = may,
    year       = "2022",
    address    = "Dublin, Ireland",
    publisher  = "Association for Computational Linguistics"
}
```

## Description
This is the repository for the paper [*Nibbling at the Hard Core of Word Sense Disambiguation*](),
to be presented at ACL 2022 by [Marco Maru](https://it.linkedin.com/in/marcomaru),
[Simone Conia](https://c-simone.github.io),
[Michele Bevilacqua](https://mbevila.github.io/) and
[Roberto Navigli](http://wwwusers.di.uniroma1.it/~navigli/).


## Abstract
> With state-of-the-art systems having finally attained estimated human performance,
  Word Sense Disambiguation (WSD) has now joined the array of Natural Language Processing tasks
  that have seemingly been solved, thanks to the vast amounts of knowledge encoded into
  Transformer-based pre-trained language models. And yet, if we look below the surface of raw figures,
  it is easy to realize that current approaches still make trivial mistakes that a human would never make.
  In this work, we provide evidence showing why the F1 score metric should not simply be taken at face value
  and present an exhaustive analysis of the errors that seven of the most representative
  state-of-the-art systems for English all-words WSD make on traditional evaluation benchmarks.
  In addition, we produce and release a collection of test sets featuring (a)
  an amended version of the standard evaluation benchmark that fixes its lexical and semantic inaccuracies,
  (b) 42D, a challenge set devised to assess the resilience of systems with respect
  to least frequent word senses and senses not seen at training time, and (c) hardEN,
  a challenge set made up solely of instances which none of
  the investigated state-of-the-art systems can solve. We make all of the test sets and model predictions
  available to the research community at https://github.com/SapienzaNLP/wsd-hard-benchmark.


## Download
You can download a copy of all the files in this repository by cloning the
[git](https://git-scm.com/) repository:

    git clone https://github.com/SapienzaNLP/wsd-hard-benchmark.git

or [download a zip archive](https://github.com/SapienzaNLP/wsd-hard-benchmark/archive/main.zip).

## How to run
We recommend a working Python environment to run the code.
The recommended way to set up your environment is through the
[Anaconda Python distribution](https://www.anaconda.com/download/) which
provides the `conda` package manager.
Anaconda can be installed in your user directory and does not interfere with
the system Python installation.

We use `conda` virtual environments to manage the project dependencies in
isolation.
Thus, you can install our dependencies without causing conflicts with your
setup (even with different Python versions).


Run the following command and follow the steps to create a separate environment:
```bash
# Make sure you have installed conda.
> ./setup.sh
> Enter environment name (recommended: wsd-hard-benchmark): wsd-hard-benchmark
> Enter python version (recommended: 3.8): 3.8
```
