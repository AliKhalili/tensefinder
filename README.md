Tense Finder
====
Python library for finding English tense in sentences
+ find simple tenses
+ find passive tenses
+ find all sentences in text and all tense for each sentence

Installation
===
`python setup.py`

Usage
====
```python
from TenseFinder.TenseParser import TenseParser
tense_parser = TenseParser()
tense_parser.find_tense_simple_form_str("How do you think children should spend their free time?")
```



