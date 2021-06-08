## Train
`onmt_train -config seq2seq.yaml -continue`
## Generate
`onmt_translate -model model/model_step_100000.pt -src corpus/dailydialog/dialogues_test_src.txt -output output/pred_100000.txt -verbose
`