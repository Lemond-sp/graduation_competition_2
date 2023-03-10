'''
BiLSTM SVR との平均
'''

LSTM_PATH = 'pseudo-lstm'
LSTM = ''
MLP  = 'mlp'
score = []

with open('../../pseudo/mlp/' + MLP + '.txt') as f1,open('../../pseudo/' + LSTM_PATH +'/'+ LSTM + '.txt') as f2:
  for s1,s2 in zip(f1,f2):
    avg = round((int(s1) + int(s2)) / 2 )
    score.append(avg)

with open('../../pseudo/ensemble/ensemble'+str(i)+'.txt','w') as fw:
  for s in score:
    s = int(s)
    fw.write(str(s) + '\n')