from data.model import Model

basic_model = Model('basic_rnn.mag', 'basic_rnn')
lookback_model = Model('lookback_rnn.mag', 'lookback_rnn')
attention_model = Model('attention_rnn.mag', 'attention_rnn')

pretrained_models_list = [basic_model, lookback_model, attention_model]