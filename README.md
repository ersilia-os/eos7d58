# ADMET properties prediction

ADMET AI is a framework for carrying out fast batch predictions for ADMET properties. It is based on ensemble of five Chemprop-RDKit models and has been trained on 41 tasks from the ADMET group in Therapeutics Data Commons (v0.4.1). Out of these 41 tasks, there are 31 classification tasks and 10 regression tasks. In addition to that output also contains 8 physicochemical properties, namely, molecular weight, logP, hydrogen bond acceptors, hydrogen bond doners, Lipinskis Rule of 5, QED, stereo centers, and topological polar surface area. Furthermore, each of these outcomes is contextualized through a computation of its percentile in reference to DrugBank approved drugs.

This model was incorporated on 2024-02-07.

## Information
### Identifiers
- **Ersilia Identifier:** `eos7d58`
- **Slug:** `admet-ai-prediction`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `ADME`, `Toxicity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `98`
- **Output Consistency:** `Fixed`
- **Interpretation:** ADMET outcomes, including physicochemical properties and classification tasks, as well as percentile normalizations based on the DrugBank chemical space.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| molecular_weight | float | high | Physicochemical property for molecular weight |
| logp | float | low | Physicochemical property for logarithm of partition coefficient (logP) |
| hydrogen_bond_acceptors | integer | high | Physicochemical property for the number of hydrogen bond acceptors |
| hydrogen_bond_donors | integer | high | Physicochemical property for the number of hydrogen bond donors |
| lipinski | integer | high | Compliance with Lipinski's rule of five (out of 4) |
| qed | float | high | Quantitative estimate of drug-likeness (0-1) |
| stereo_centers | integer | high | Physicochemical property for the number of stereocenters |
| tpsa | float | high | Physicochemical property for topological polar surface area (TPSA) in squared Angstroms |
| ames | float | high | Predicted probability of Ames mutagenicity |
| bbb_martins | float | high | Predicted probability of blood-brain barrier penetration |

_10 of 98 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos7d58](https://hub.docker.com/r/ersiliaos/eos7d58)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7d58.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7d58.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `6062`
- **Image Size (Mb):** `5940.22`

**Computational Performance (seconds):**
- 10 inputs: `41.01`
- 100 inputs: `40.51`
- 10000 inputs: `1268.82`

### References
- **Source Code**: [https://github.com/swansonk14/admet_ai](https://github.com/swansonk14/admet_ai)
- **Publication**: [https://academic.oup.com/bioinformatics/article/40/7/btae416/7698030](https://academic.oup.com/bioinformatics/article/40/7/btae416/7698030)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2024`
- **Ersilia Contributor:** [DhanshreeA](https://github.com/DhanshreeA)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos7d58
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos7d58
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
