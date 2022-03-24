from argparse import ArgumentParser

from nltk.corpus import wordnet as wn


def load_keys(path):
    keys = {}

    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            instance_id, *sense_keys = line.split()
            if not sense_keys:
                continue
            assert instance_id not in keys
            keys[instance_id] = set(sense_keys)
    
    return keys


def evaluate(gold, pred, eval_keys=None):
    tp, fp, fn = 0, 0, 0

    for instance_id in gold:
        if eval_keys and instance_id not in eval_keys:
            continue

        if instance_id in pred:
            correct = False

            for key in pred[instance_id]:
                if key in gold[instance_id]:
                    correct = True
            
            if correct:
                tp += 1
            else:
                for key in pred[instance_id]:
                    fp += 1
                fn += 1
        else:
            fn += 1
    
    precision = tp / (tp + fp) if tp + fp != 0 else 0
    recall = tp / (tp + fn) if tp + fn != 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if precision + recall != 0 else 0

    print('Precision   =', '{:0.2f} [{}/{}]'.format(100 * precision, tp, tp + fp))
    print('Recall      =', '{:0.2f} [{}/{}]'.format(100 * recall, tp, tp + fn))
    print('F1 score    =', '{:0.2f}'.format(100 * f1))


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(
        '--gold_path',
        type=str,
        required=True,
        help='Path to the gold keys.'
    )
    parser.add_argument(
        '--pred_path',
        type=str,
        required=True,
        help='Path to the predicted keys.'
    )
    parser.add_argument(
        '--key_subset_path',
        type=str,
        required=False,
        help='Path to a regular key file.\n The evaluation script will consider only those keys appearing in this file.'
    )

    args = parser.parse_args()
    gold_path: str = args.gold_path
    pred_path: str = args.pred_path
    key_subset_path: str = args.key_subset_path

    gold_keys = load_keys(gold_path)
    pred_keys = load_keys(pred_path)

    if not key_subset_path:
        evaluate(gold_keys, pred_keys)
    else:
        eval_keys = load_keys(key_subset_path)
        evaluate(gold_keys, pred_keys, eval_keys=eval_keys)
