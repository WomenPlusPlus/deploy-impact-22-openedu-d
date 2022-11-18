# How to run the model | keybert and zeroshot classification

## Table of Content

- [Used Technology  Stack](#used-technology-stack)
- [KeyBERT](#keybert)
- [Assumptions](#assumptions)
- [To run code](#to-run-code)

## Used Technology  Stack

- Python version used: 3.9
- Libraries needed:
  - Pandas
  - re

## KeyBERT

```
import KeyBERT from keybert
import pipeline from transformers
```

## Assumptions

- Data file is in xlsx version
- Data is with description of the upload in english language
- Data labels:
  - 'topic' for level-1 classification
  - 'excerpt' for description

## To run code

- Step 6 should be run for each topic.
- Topic to run currently needs to be specified in this line after `== {Robotics = data.loc[data['topic'] == 'Robotics']}`
list of labels to allocate sub-topics is to be passed under `candidate_label`.
- After allocation of sub-topics, two files, one in excel and one in csv format are exported to the location of the code.
