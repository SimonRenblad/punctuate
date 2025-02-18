# punctuate

`punctuate.py` is a simple python script to randomly punctuate and capitalize words, inspired by the features of a *certain* popular online typing test website. 

## Install

`punctuate` is available as a Nix flake:

```bash
nix shell github:SimonRenblad/punctuate             # try it out
nix profile install github:SimonRenblad/punctuate   # install to profiles
```

Or just run `python punctuate.py` / do what you want with it. `punctuate` does not depend on any additional python packages.

## Example

```bash
> cat example.txt
roud
pointfully
scutibranchian
acantha
deferrized
internecive
alliterating
propjet
thrusher
genny
```
```bash
> punctuate example.txt
'roud'
Pointfully/
scutibranchian
acantha
Deferrized
internecive
Alliterating
Propjet
thrusher
Genny
```

## Usage

`punctuate` takes a newline separated list of words as input. It is primarily designed to be used with pipes:

```bash
cat word_list.txt | punctuate -
```

Originally, I wrote `punctuate` in order to randomize inputs to CLI type testers like [tt](https://github.com/lemnos/tt) and [ttyper](https://github.com/max-niederman/ttyper). The example below samples 30 words from a word list, randomly capitalizes, and punctuates them before displaying as a typing test:

```bash
shuf -n 30 word_list.txt | punctuate - | ttyper -
```

You can also adjust the likelihood that `punctuate` will alter a word. The example below will capitalize a word 50% of the time, punctuate it at the end 20% of the time and never surround it with brackets or quotes.

```bash
punctuate word_list.txt -c 50 -p 20 -d 0
```
