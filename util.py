daily_dialog = [
    ['corpus/dailydialog/train/dialogues_train.txt', 'corpus/dailydialog/dialogues_train.txt'],
    ['corpus/dailydialog/test/dialogues_test.txt', 'corpus/dailydialog/dialogues_test.txt'],
    ['corpus/dailydialog/validation/dialogues_validation.txt', 'corpus/dailydialog/dialogues_validation.txt']
]


def process_daily_dialog(file_name: str, output_name: str):
    lines = []
    conversation_list = []
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        utterances = line[:-1].split('__eou__')
        conversation_list.append([u for u in utterances if u != ''])

    src_list = []
    tgt_list = []
    for conversation in conversation_list:
        if len(conversation) == 1:
            continue
        for i in range(len(conversation) - 1):
            src_list.append(conversation[i].strip(' ').rstrip(' '))
            tgt_list.append(conversation[i + 1].strip(' ').rstrip(' '))
    with open(output_name.split('.')[0] + '_src.txt', 'w', encoding='utf-8') as f:
        for src in src_list:
            f.write(src + '\n')
    with open(output_name.split('.')[0] + '_tgt.txt', 'w', encoding='utf-8') as f:
        for tgt in tgt_list:
            f.write(tgt + '\n')


if __name__ == '__main__':
    for f in daily_dialog:
        process_daily_dialog(f[0], f[1])
