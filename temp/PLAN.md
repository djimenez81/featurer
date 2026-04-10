# Initial Implementation Plan for `featurer` Package

This could be consider an initial _planning board_ for the implementation of
this small package.

The `featurer` package wants to be a library of functions that allows to
compute or specify featural systems for phonetic inventories, and some related
functionalities.

At this point, everything (names, formats, order, etc) is developing and
evolving. Things could significantly change quickly.

## The Main Plan

This section is at the top of the file as it most likely be my main reference.
Nevertheless, it makes reference to concepts defined or described in _The
Overall Idea_ section.

1. Compile necessary data.
2. Define the formats. At first most likely will be only **IPA** and
**X-SAMPA**, but other formats could be considered.
3. Implement the `convert` method (not because it is the most relevant, but
because at this point is probably the simpler to implement).
4. Implement the (_non prioritized_) `feature_selector` function.
5. Implement the `parser` function.
6. Implement the `inventory_computation` function.
7. Consider variants for the `feature_selector`, like prioritization of
features by the user, randomization of selection, different sets for vowels and
consonants, etc.


## The Overall Idea

This package is implemented with the overall idea to provide the functionality
to compute a _Minimal Featural System_ for a given _Phonetic Inventory_ within
_Articulatory Phonetics_. Therefore, the functionalities that it should provide
are:

1. **Computation of the Featural System**: The main method of the project, it
intends to provide the user with a set of features that already exists in the
literature, for the user-provided phonetic inventory. At a later point, we plan
to include capabilities for the user to provide some criteria to prioritize
which features are more desirable to consider within the system.
2. **Computation of the Phonetic Inventory from a Corpus**: Relevant for a
project that requires the computation detailed in the previous point is the
definition of the phonetic inventory used by a given corpus. This would be a
simple method that goes through a _corpus_ (list of words) phonetically
transcribed on a supported format, parses each string (word), and then returns
the list of all the phones that appears at least once in the corpus.
3. **Parser**: Given that, for the previous function defined, the need will
arise to implement a method that parses the given corpus, we consider that the
parsing functionality could be useful to the final user, and thus, it should be
public to them.
4. **Format Converter**: It is likely that the final user may be working with
data from different sources, phonetic transcriptions encoded in different
formats (_e.g.:_ **IPA**, **X-SAMPA**, etc), that the need to convert such
corpus to a uniform format arises.


### Potential Future Features

- Given that the user might want to compare corpora with overlapping but not
identical phonetic inventories or featural systems, we may consider to provide
a functionality to combine them. 


### The Definitions:

This final section is included to provide the reader with an informal
definition of the terms used through the document.

- _Phonetic Inventory_: Set of _phones_ (symbols) to be considered.
- _Feature_: Binary criteria over the phonetical inventory. That is, a function
from the set of _phones_ to the set {0,1} (or {+,-}, or {`True`, `False`}).
- _Featural System_: Set of features over the inventory that _distinguishes_
the phonetic inventory. This means, given any two phones in the phonetical
inventory, they differ in at least one feature.
- _Minimal Featural System_: A featural system that additionally satisfies
that any proper subset of features does not fully distinguishes the inventory.
