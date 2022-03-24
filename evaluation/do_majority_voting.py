from argparse import ArgumentParser
from typing import Dict, List


def read_data(path: str):
    data: Dict[str, List[str]] = {}
    
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            instance_id, *sense_keys = line.split()
            data[instance_id] = sense_keys
    
    return data


def do_majority_voting(gold_data, system_data, system_ranking, use_system_ranking=False):
    keys = {}

    for gold_instance_id, gold_sense_keys in gold_data.items():
        answers = {}

        for system_name, system_predictions in system_data.items():
            if gold_instance_id not in system_predictions:
                continue

            system_sense_keys = system_predictions[gold_instance_id]
            for system_sense_key in system_sense_keys:
                if system_sense_key not in answers:
                    answers[system_sense_key] = 0
                
                if use_system_ranking:
                    answers[system_sense_key] += system_ranking[system_name]
                else:
                    answers[system_sense_key] += 1

            majority_key = max(answers, key=answers.get)
            keys[gold_instance_id] = majority_key
    
    return keys


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(
        '--gold_path',
        type=str,
        required=True,
        help='Path to the gold keys.'
    )
    parser.add_argument(
        '--ares_path',
        type=str,
        required=True,
        help='Path to the keys predicted by ARES.'
    )
    parser.add_argument(
        '--bem_path',
        type=str,
        required=True,
        help='Path to the keys predicted by BEM.'
    )
    parser.add_argument(
        '--esc_path',
        type=str,
        required=True,
        help='Path to the keys predicted by ESC.'
    )
    parser.add_argument(
        '--ewiser_path',
        type=str,
        required=True,
        help='Path to the keys predicted by EWISER.'
    )
    parser.add_argument(
        '--generationary_path',
        type=str,
        required=True,
        help='Path to the keys predicted by Generationary.'
    )
    parser.add_argument(
        '--glossbert_path',
        type=str,
        required=True,
        help='Path to the keys predicted by GlossBERT.'
    )
    parser.add_argument(
        '--syntagrank_path',
        type=str,
        required=True,
        help='Path to the keys predicted by SyntagRank.'
    )
    parser.add_argument(
        '--output_path',
        type=str,
        required=True,
        help='Path to the keys that were not predicted correctly by any system.'
    )
    parser.add_argument(
        '--use_system_ranking',
        action='store_true',
        help='Use this flag to perform a ranked ensemble.'
    )

    args = parser.parse_args()

    gold_path: str = args.gold_path
    ares_path: str = args.ares_path
    bem_path: str = args.bem_path
    esc_path: str = args.esc_path
    ewiser_path: str = args.ewiser_path
    generationary_path: str = args.generationary_path
    glossbert_path: str = args.glossbert_path
    syntagrank_path: str = args.syntagrank_path
    output_path: str = args.output_path
    use_system_ranking: bool = args.use_system_ranking

    gold_data: Dict[str, List[str]] = read_data(gold_path)
    system_data: Dict[str, Dict[str, List[str]]] = {
        'ares': read_data(ares_path),
        'bem': read_data(bem_path),
        'esc': read_data(esc_path),
        'ewiser': read_data(ewiser_path),
        'generationary': read_data(generationary_path),
        'glossbert': read_data(glossbert_path),
        'syntagrank': read_data(syntagrank_path),
    }
    system_ranking: Dict[str, int] = {
        'ares': 5,
        'bem': 6,
        'esc': 7,
        'ewiser': 4,
        'generationary': 2,
        'glossbert': 3,
        'syntagrank': 1,
    }

    keys = do_majority_voting(gold_data, system_data, system_ranking, use_system_ranking=use_system_ranking)

    sorted_instance_ids = sorted(list(keys.keys()))
    with open(output_path, 'w') as f:
        for instance_id in sorted_instance_ids:
            sense_key = keys[instance_id]
            f.write(f'{instance_id} {sense_key}\n')
