LSTM_PATH = 'pseudo-lstm'
#LSTM_PATH = 'bilstm'

SVRS = ['487A-optuna_pse-svr_eval_sudachi-fullA3','487A-optuna_pse-svr_eval_sudachi-fullC3',"487A-optuna_pse-svr_eval_sudachiA3",'487A-optuna_pse-svr_eval_sudachiC3','491A-optuna_pse-svr_eval_sudachiA3','491C-optuna_pse-svr_eval_sudachiC3','optuna_pse-svr_eval_sudachi-fullC-2','optuna_pse-svr_eval_sudachi-fullC']
LSTM = '522'
score = []
i = 1
print(LSTM)
for SVR in SVRS:
  with open('../../pseudo/svr/' + SVR + '.txt') as f1,open('../../pseudo/' + LSTM_PATH +'/'+ LSTM + '.txt') as f2:
    for s1,s2 in zip(f1,f2):
      avg = round((int(s1) + int(s2)) / 2 )
      score.append(avg)

  with open('../../pseudo/ensemble/sudachi/ensemble'+str(i)+'.txt','w') as fw:
    for s in score:
      s = int(s)
      fw.write(str(s) + '\n')
  score = []
  i += 1