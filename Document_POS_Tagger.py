#Code written by Shimon Johnson,Khalid Alnajjar
#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pathlib import Path
from stanfordcorenlp import StanfordCoreNLP
import logging
import json
import pprint
import glob

class StanfordNLP:
    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    def pos(self, sentence):
        return self.nlp.pos_tag(sentence)

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def dependency_parse(self, sentence):
        return self.nlp.dependency_parse(sentence)

    def annotate(self, sentence):
        return json.loads(self.nlp.annotate(sentence, properties=self.props))

    @staticmethod
    def tokens_to_dict(_tokens):
        tokens = defaultdict(dict)
        for token in _tokens:
            tokens[int(token['index'])] = {
                'word': token['word'],
                'lemma': token['lemma'],
                'pos': token['pos'],
                'ner': token['ner']
            }
        return tokens

Path("./POS_output").mkdir(parents=True, exist_ok=True)
if __name__ == '__main__':
    sNLP = StanfordNLP()


files = glob.glob("Input_files/*.txt")
files.sort()
lists = []
i = 1
for file in files:
    with open(file) as f:
        txt_file_as_string = f.read()
        tagged_docs = sNLP.pos(str(txt_file_as_string))
        lists.append(tagged_docs)
        output_s = pprint.pformat(tagged_docs)

    with open("POS_output/Taggedfile{}.txt".format(i), 'w') as output:
        output.write(str(output_s))

    i += 1

ob = StanfordNLP()
