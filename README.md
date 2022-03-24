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

## The WSD hard benchmark

### Overview
Our revised and amended evaluation benchmark for WSD includes the following datasets:
```
wsd_hard_benchmark/
├── 42D
│   ├── 42D.data.xml
│   └── 42D.gold.key.txt
├── ALLamended
│   ├── ALLamended.data.xml
│   └── ALLamended.gold.key.txt
├── hardEN
│   ├── hardEN.data.xml
│   └── hardEN.gold.key.txt
├── S07amended
│   ├── S07amended.data.xml
│   └── S07amended.gold.key.txt
├── S10amended
│   ├── S10amended.data.xml
│   └── S10amended.gold.key.txt
└── softEN
    ├── softEN.data.xml
    └── softEN.gold.key.txt
```

### Data format
We follow the format proposed in [Word Sense Disambiguation: A Unified Evaluation Framework and Empirical Comparison (Raganato et al., 2017)](https://aclanthology.org/E17-1010/).
In particular, each dataset `dataset_name` is divided into two files:
* `dataset_name.data.xml`: An XML file that contains the test sentences, meta-data and the target words the system has to disambiguate.
* `dataset_name.gold.key.txt`: A text file which contains the ground truth for the target words in `dataset_name.data.xml`.

#### `dataset_name.data.xml`
Here is a sample from `ALLamended.data.xml`:
* The root element is `corpus`.
* Each sentence is wrapped within `<sentence> ... </sentence>` tags.
* Each non-target word is wrapped within `<wf> ... </wf>` tags.
* Each **target** word, i.e., word to disambiguate is wrapped within `<instance> ... </instance>` tags. The `id` of an instance is used in the `dataset_name.gold.key.txt` file to indicate the corresponding gold sense(s).
* Both `wf` and `instance` elements are provided with their corresponding lemmas and part-of-speech (pos) tags.
```xml
<?xml version="1.0"?>
<corpus lang="en" source="senseval2-senseval3-semeval2013-semeval2015">
  <text id="senseval2.d000">
    <sentence id="senseval2.d000.s000">
      <wf lemma="the" pos="DET">The</wf>
      <instance id="senseval2.d000.s000.t000" lemma="art" pos="NOUN">art</instance>
      <wf lemma="of" pos="ADP">of</wf>
      <wf lemma="change_ringing" pos="NOUN">change-ringing</wf>
      <wf lemma="be" pos="VERB">is</wf>
      <instance id="senseval2.d000.s000.t002" lemma="peculiar" pos="ADJ">peculiar</instance>
      <wf lemma="to" pos="PRT">to</wf>
      <wf lemma="the" pos="DET">the</wf>
      <instance id="senseval2.d000.s000.t003" lemma="english" pos="NOUN">English</instance>
      <wf lemma="," pos=".">,</wf>
      <wf lemma="and" pos="CONJ">and</wf>
      <wf lemma="," pos=".">,</wf>
      <wf lemma="like" pos="ADP">like</wf>
      <instance id="senseval2.d000.s000.t004" lemma="most" pos="ADJ">most</instance>
      <instance id="senseval2.d000.s000.t005" lemma="english" pos="ADJ">English</instance>
      <instance id="senseval2.d000.s000.t006" lemma="peculiarity" pos="NOUN">peculiarities</instance>
      <wf lemma="," pos=".">,</wf>
      <instance id="senseval2.d000.s000.t007" lemma="unintelligible" pos="ADJ">unintelligible</instance>
      <wf lemma="to" pos="PRT">to</wf>
      <wf lemma="the" pos="DET">the</wf>
      <instance id="senseval2.d000.s000.t008" lemma="rest" pos="NOUN">rest</instance>
      <wf lemma="of" pos="ADP">of</wf>
      <wf lemma="the" pos="DET">the</wf>
      <instance id="senseval2.d000.s000.t009" lemma="world" pos="NOUN">world</instance>
      <wf lemma="." pos=".">.</wf>
    </sentence>
   ...
  </text>
 ...
</corpus>
```

#### `dataset_name.gold.key.txt`
Here is a sample from `ALLamended.gold.key.txt`:
* Each line refers to an instance.
* The first element of each line is the `id` of the instance (see `dataset_name.data.xml` above).
* The other elements of the line are the gold senses expressed as WordNet sense keys.
* In case of multiple gold senses, they are all equally valid (according to expert annotators). 
```
senseval2.d000.s000.t000 art%1:09:00::
senseval2.d000.s000.t002 peculiar%5:00:00:characteristic:00 peculiar%5:00:00:specific:00
senseval2.d000.s000.t003 english%1:18:00::
senseval2.d000.s000.t004 most%3:00:02::
senseval2.d000.s000.t005 english%3:01:00::
senseval2.d000.s000.t006 peculiarity%1:07:02:: peculiarity%1:09:00::
senseval2.d000.s000.t007 unintelligible%5:00:00:incomprehensible:00
senseval2.d000.s000.t008 rest%1:24:00::
senseval2.d000.s000.t009 world%1:14:02::
```

### Datasets
* **ALLamended:** A revised and amended version of the widely used ALL dataset proposed by Raganato et al. (2017).
It is constructed by concatenating Senseval2, Senseval3, SemEval-2013, and SemEval-2015. **NOTE:** Differently from the original ALL,
this dataset does not contain SemEval-2007 which is often used in the literature as the development/validation set.
* **SemEval-2010 (S10amended):** A revised and amended version of SemEval-2010.
* **42D:** A novel challenge set for WSD, comprising difficult and out-of-domain words/senses.
* **hardEN:** A "hard" dataset built by including all the instances of ALLamended, SemEval-2010 and 42D that are disambiguated incorrectly by several state-of-the-art systems.
* **softEN:** This dataset includes all the instances of ALLamended, SemEval-2010 and 42D that are not included in hardEN.

### Evaluation
We provide two scripts to compute the micro-averaged F1 score and the macro-averaged F1 score (we refer to the paper for further details).

#### Micro F1
You can compute the micro F1 score of your system using the following command:
```bash
python evaluation/evaluate_micro_F1.py \
    --gold_path <path/to/gold/keys.txt> \
    --pred_path <path/to/pred/keys.txt>
```
Optionally, you can specify another keys file which will be used to filter instances,
i.e., the evaluation script will only consider those instances appearing in this third file.
```bash
# Evaluates the score of ESC on the instances of ALL by only considering
# those instances that appear in ALLamended.
python evaluation/evaluate_micro_F1.py \
    --gold_path ALL.gold.key.txt \
    --pred_path esc-predictions.key.txt \
    --key_subset_path ALLamended.gold.key.txt
```


#### Macro F1
You can compute the macro F1 score of your system using the following command:
```bash
python evaluation/evaluate_macro_F1.py \
    --gold_path <path/to/gold/keys.txt> \
    --pred_path <path/to/pred/keys.txt>
```
Similarly to the micro F1 scoring script, you can also specify another keys file which will be used to filter instances,
i.e., the evaluation script will only consider those instances appearing in this third file.
```bash
# Evaluates the score of ESC on the instances of ALL by only considering
# those instances that appear in ALLamended.
python evaluation/evaluate_macro_F1.py \
    --gold_path ALL.gold.key.txt \
    --pred_path esc-predictions.key.txt \
    --key_subset_path ALLamended.gold.key.txt
```

The macro F1 scoring script has also a "strict" mode, which you can enable by using the `--strict` flag as follows:
```bash
python evaluation/evaluate_macro_F1.py \
    --gold_path <path/to/gold/keys.txt> \
    --pred_path <path/to/pred/keys.txt> \
    --strict
```

## Acknowledgments

The authors gratefully acknowledge the support of the [ERC Consolidator Grant MOUSSE No. 726487](http://mousse-project.org/) and the [European Language Grid
project No. 825627 (Universal Semantic Annotator, USeA)](https://live.european-language-grid.eu/catalogue/project/5334/) under the European Union’s Horizon 2020 research and innovation programme.

This work was supported in part by the MIUR under grant “Dipartimenti di eccellenza 2018-2022” of the Department of Computer Science of the Sapienza University of Rome.


## License
This work is under the Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license.
