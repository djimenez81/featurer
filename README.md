# Featurer

**WARNING:** At the present moment this package is at the very early stages of
implementation, therefore it is not yet functional.

Featurer is a small library with the following (presently intended)
functionalities:

1. Given a _phonetical inventory_ (any subset of phones with at least
two elements), it provides a _minimal featural system_. This means, it provides
a set of binary criteria, or _features_, that each phone either fulfills or not
(that is, each phone has either a value of `+` or `-` associated with that
_feature_), and any two phones differ in at least a feature. Furthermore, the
_featural system_ is _minimal_, in the sense that any proper subset of
features of the system does not completely differentiate the inventory. At a
later stage, it is planned to allow a priorization of features provided by the
user.

2. Given a phonetically transcribed _corpus_ (a non-empty list of _words_
transcribed phonetically **in the supported formats**), it computes the
phonetical inventory containing all phones used in the provided corpus.

3. It provides the functionality to _parse_ a phonetically transcribed _word_
(**in the supported formats**), into its component phones.

4. It provides the functionality to _convert_ a phonetically transcribed _word_
**in any of the supported formats** to **any other supported format**.

At this moment, `featurer` supports (or at least it is planned to support):

- IPA. 
- X-SAMPA.
