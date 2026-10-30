# Contributing

Small, evidence-backed improvements are welcome: parsing fixes, anonymized regression fixtures, clearer skill boundaries, and documented host compatibility.

1. Open an issue describing the user-visible problem for substantial changes.
2. Keep the runtime standard-library-only and preserve Python 3.10 compatibility.
3. Add a regression test for changed calculations or parsers.
4. Run `python -m unittest discover -s tests -v`.
5. Update examples and documentation when behavior changes.
6. Submit a focused pull request describing the behavior, validation and limitations.

Use synthetic or anonymized examples. Never submit account tokens, private analytics, unpublished film assets, or personal information. Preserve license notices. Do not turn editorial preferences into universal performance claims, promise virality, or add automatic external posting.
