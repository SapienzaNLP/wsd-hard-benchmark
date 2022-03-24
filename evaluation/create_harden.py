from argparse import ArgumentParser
from typing import Dict, List
from xml.dom import minidom
from xml.etree import ElementTree as ET


def read_intersection_ids(paths: List[str]) -> List[str]:
    ids: List[str] = []

    for path in paths:
        with open(path) as f:
            for line in f:
                instance_id = line.strip()
                if not instance_id:
                    continue

                ids.append(instance_id)

    return ids


def read_keys(intersection_instance_ids: List[str], paths: List[str]) -> Dict[str, List[str]]:
    keys: Dict[str, List[str]] = {}
    
    for path in paths:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                instance_id, *sense_keys = line.split()
                if instance_id in intersection_instance_ids:
                    keys[instance_id] = sense_keys
        
    return keys


def read_data(intersection_instance_ids: List[str], data_paths: List[str]) -> Dict[str, Dict[str, Dict]]:
    data = {}

    for data_path in data_paths:
        tree: ET.ElementTree = ET.parse(data_path)
        root: ET.Element = tree.getroot()

        for document in root.iter('text'):
            document_data = {}

            for sentence in document.iter('sentence'):
                sentence_data = {
                    'tokens': [],
                    'lemmas': [],
                    'pos_tags': [],
                    'instances': [],
                }

                sentence_id: str = sentence.attrib['id']
                
                for token in sentence:
                    sentence_data['tokens'].append(token.text)
                    sentence_data['lemmas'].append(token.attrib['lemma'])
                    sentence_data['pos_tags'].append(token.attrib['pos'])
                    if token.tag == 'instance':
                        instance_id = token.attrib['id']
                        if instance_id in intersection_instance_ids:
                            sentence_data['instances'].append(instance_id)
                        else:
                            sentence_data['instances'].append('_')
                    else:
                        sentence_data['instances'].append('_')
                
                document_data[sentence_id] = sentence_data

            data[document.attrib['id']] = document_data
    
    return data


def create_hardEN(all_data, all_keys, data_output_path, keys_output_path) -> None:
    root = ET.Element('corpus')
    root.attrib['language'] = 'en'
    root.attrib['source'] = 'hardEN'

    sorted_document_ids = sorted(list(all_data.keys()))

    for document_id in sorted_document_ids:
        document_root = ET.SubElement(root, 'text')
        document_root.attrib['id'] = document_id
        document_data = all_data[document_id]
        sorted_sentence_ids = sorted(list(document_data.keys()))

        for sentence_id in sorted_sentence_ids:
            sentence_root = ET.SubElement(document_root, 'sentence')
            sentence_root.attrib['id'] = sentence_id
            sentence_data = document_data[sentence_id]

            for token, lemma, pos, instance_id in zip(sentence_data['tokens'], sentence_data['lemmas'], sentence_data['pos_tags'], sentence_data['instances']):
                if instance_id != '_':
                    token_root = ET.SubElement(sentence_root, 'instance')
                    token_root.attrib['id'] = instance_id
                else:
                    token_root = ET.SubElement(sentence_root, 'wf')
                token_root.attrib['lemma'] = lemma
                token_root.attrib['pos'] = pos
                token_root.text = token
    
    tree_string = ET.tostring(root, encoding='utf-8')
    reparsed = minidom.parseString(tree_string)
    pretty_xml = reparsed.toprettyxml(indent='  ')
    with open(data_output_path, 'w') as f:
        f.write(pretty_xml)

    sorted_keys = sorted(list(all_keys.keys()))

    with open(keys_output_path, 'w') as f:
        for key in sorted_keys:
            senses = all_keys[key]
            senses = ' '.join(senses)
            line = f'{key} {senses}\n'
            f.write(line)
    

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(
        '--ALLamended_data_path',
        type=str,
        required=True,
        help='Path to the original data for ALL amended.'
    )
    parser.add_argument(
        '--ALLamended_gold_path',
        type=str,
        required=True,
        help='Path to the original gold keys for ALL amended.'
    )
    parser.add_argument(
        '--fortitude_data_path',
        type=str,
        required=True,
        help='Path to the original data for 42D.'
    )
    parser.add_argument(
        '--fortitude_gold_path',
        type=str,
        required=True,
        help='Path to the original gold keys for 42D.'
    )
    parser.add_argument(
        '--ALLamended_intersection_path',
        type=str,
        required=True,
        help='Path to the instance ids predicted wrong by all the systems in ALL.'
    )
    parser.add_argument(
        '--SE10_intersection_path',
        type=str,
        required=True,
        help='Path to the instance ids predicted wrong by all the systems in SemEval-2010.'
    )
    parser.add_argument(
        '--fortitude_intersection_path',
        type=str,
        required=True,
        help='Path to the instance ids predicted wrong by all the systems in 42D.'
    )
    parser.add_argument(
        '--data_output_path',
        type=str,
        required=True,
        help='Path to hardEN data (xml).'
    )
    parser.add_argument(
        '--gold_output_path',
        type=str,
        required=True,
        help='Path to hardEN keys (txt).'
    )

    args = parser.parse_args()

    ALLamended_data_path: str = args.ALLamended_data_path
    ALLamended_gold_path: str = args.ALLamended_gold_path
    fortitude_data_path: str = args.fortitude_data_path
    fortitude_gold_path: str = args.fortitude_gold_path
    ALLamended_intersection_path: str = args.ALLamended_intersection_path
    SE10_intersection_path: str = args.SE10_intersection_path
    fortitude_intersection_path: str = args.fortitude_intersection_path
    data_output_path: str = args.data_output_path
    gold_output_path: str = args.gold_output_path

    intersection_paths: List[str] = [
        ALLamended_intersection_path,
        SE10_intersection_path,
        fortitude_intersection_path
    ]

    data_paths: List[str] = [
        ALLamended_data_path,
        fortitude_data_path
    ]

    gold_paths: List[str] = [
        ALLamended_gold_path,
        fortitude_gold_path
    ]

    intersection_instance_ids: List[str] = read_intersection_ids(intersection_paths)
    all_data: Dict[str, Dict[str, Dict]] = read_data(intersection_instance_ids, data_paths)
    all_keys: Dict[str, List[str]] = read_keys(intersection_instance_ids, gold_paths)

    create_hardEN(
        all_data,
        all_keys,
        data_output_path,
        gold_output_path,
    )

