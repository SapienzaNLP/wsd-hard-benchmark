from argparse import ArgumentParser
from typing import Dict

from xml.etree import ElementTree as ET

from nltk.corpus import wordnet as wn

def read_data(data_path: str):
    pos_tag = {
        'NOUN': 'n',
        'ADJ': 'a',
        'ADV': 'r',
        'VERB': 'v'
    }
    data = {}
    tree: ET.ElementTree = ET.parse(data_path)
    root: ET.Element = tree.getroot()

    for sentence in root.iter('sentence'):

        for token in sentence:
            if token.tag == 'instance':
                data[token.attrib['id']] = {
                    'word': token.text,
                    'lemma': token.attrib['lemma'],
                    'pos': pos_tag[token.attrib['pos']],
                }
    
    return data

def read_synsets(synset_path: str):
    instances = {}

    with open(synset_path) as f:

        for line in f:
            line = line.strip()
            if not line:
                continue

            instance_id, *synsets = line.split()
            assert len(synsets) == 1
            instances[instance_id] = synsets[0]
    
    return instances

def convert(data: Dict[str, Dict], instances: Dict[str, str], sense_path: str):
    sense_instances = {}

    for instance_id, synset in instances.items():
        instance_lemma = data[instance_id]['lemma']
        instance_pos = data[instance_id]['pos']
        synset = wn.synset_from_pos_and_offset(synset[-1], int(synset[3:-1]))
        predicted_sense_keys = [l.key() for l in synset.lemmas() if instance_lemma.lower().replace(' ', '_') == l.key().lower().split('%')[0]]
        if len(predicted_sense_keys) != 1:
            print(instance_lemma, instance_pos)
            print(predicted_sense_keys)
            print()
        predicted_sense_key = predicted_sense_keys[0]
        sense_instances[instance_id] = predicted_sense_key
    
    with open(sense_path, 'w') as f:
        sorted_instance_ids = sorted(list(sense_instances.keys()))
        for instance_id in sorted_instance_ids:
            sense_key = sense_instances[instance_id]
            f.write(f'{instance_id} {sense_key}\n')


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(
        '--data_path',
        type=str,
        required=True,
        help='Path with the original data.'
    )
    parser.add_argument(
        '--synset_path',
        type=str,
        required=True,
        help='Path to the original predictions with synsets.'
    )
    parser.add_argument(
        '--sense_path',
        type=str,
        required=True,
        help='Output path for the predictions converted to keys.'
    )

    args = parser.parse_args()
    data_path: str = args.data_path
    synset_path: str = args.synset_path
    sense_path: str = args.sense_path

    data = read_data(data_path)
    instances = read_synsets(synset_path)
    convert(data, instances, sense_path)