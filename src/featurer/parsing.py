"""Contains methods to parse phonetic transcriptions on supported formats.

This module contains all the parsing related functions and classes
(with the exception of constants) to parse strings containing phonetic
trasncriptions written in the supported formats. The current version
supports:

  - IPA
  - X-SAMPA

MAIN METHODS
------------
  -
"""


__author__  = "David Jiménez"
__email__   = "david.jimenezlopez@ucr.ac.cr"
__status__  = "Initial implementation"
__version__ = "0.1.0"


# Strandard library imports


# Third party imports


# Local imports


# Functions 
def parse_xsampa(transcription: str) -> list[str]:
    """Parses an X-SAMPA transcription into its individual phones.
    """
    pass


def parse_ipa(transcription: str) -> list[str]:
    """Parses an IPA transcription into its individual phones.
    """
    pass


def convert_ipa_xsampa(ipa: str) -> str:
    """Converts an IPA phone to the corresponding X-SAMPA representation.
    """
    pass


def convert_xsampa_ipa(ipa: str) -> str:
    """Converts an IPA phone to the corresponding X-SAMPA representation.
    """
    pass
