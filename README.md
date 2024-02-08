# ADMET properties prediction

A framework based on ensemble of five Chemprop-RDKit models, for fast batch prediction of ADMET properties of small molecules. The framework exists as a CLI tool, a Python API, and a web server. We incorporate it using the API.

## Identifiers

* EOS model ID: `eos7d58`
* Slug: `admet-ai-prediction`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification, Regression`
* Output: `Probability, Score`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: ADMET AI is a framework for carrying out fast batch predictions for ADMET properties. It is based on ensemble of five Chemprop-RDKit models and has been trained on 41 tasks from the ADMET group in Therapeutics Data Commons (v0.4.1). Out of these 41 tasks, there are 31 classification tasks and 10 regression tasks. In addition to that output also contains 8 physicochemical properties, namely, molecular weight, logP, hydrogen bond acceptors, hydrogen bond doners, Lipinski's Rule of 5, QED, stereo centers, and topological polar surface area. Furthermore, each of these outcomes is contextualized through a computation of its percentile in reference to DrugBank approved drugs. According to the authors, the framework can generate predicitons for a million compounds in approximately 3 hours on a single GPU or 32 CPU machine.

## References

* [Publication](https://www.biorxiv.org/content/10.1101/2023.12.28.573531v1)
* [Source Code](https://github.com/swansonk14/admet_ai)
* Ersilia contributor: [DhanshreeA](https://github.com/DhanshreeA)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos7d58)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7d58.zip)

## Citation

If you use this model, please cite the [original authors](https://www.biorxiv.org/content/10.1101/2023.12.28.573531v1) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!