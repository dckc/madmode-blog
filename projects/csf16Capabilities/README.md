# A study of CSF'16 paper by Rezk et. al.

  - V. Rajani, Garg, D., and Rezk, T., [On Access Control,
    Capabilities, Their Equivalence, and Confused Deputy Attacks][1], in
    Proceedings of the 29th IEEE Computer Security Foundations
    Symposium (CSF), 2016.

## Abstract

Motivated by the problem of understanding the difference between
practical access control and capability systems formally, we distill
the essence of both in a language- based setting. We first prove that
access control systems and (object) capabilities are fundamentally
different. We further study capabilities as an enforcement mechanism
for confused deputy attacks (CDAs), since CDAs may have been the
primary motivation for the invention of capabilities. To do this, we
develop the first formal characterization of CDA-freedom in a
language-based setting and describe its relation to standard
information flow integrity. We show that, perhaps suprisingly,
capabilities cannot prevent all CDAs. Next, we stipulate re-
strictions on programs under which capabilities ensure CDA- freedom
and prove that the restrictions are sufficient. To relax those
restrictions, we examine provenance semantics as sound CDA-freedom
enforcement mechanisms.

[1]: https://www-sop.inria.fr/lemme/Tamara.Rezk/publication/csf16Capabilities.pdf

## Design Notes

I'm rendering the formal parts of the paper in idris. WIP.
