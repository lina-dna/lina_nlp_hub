from transformers import BertForPreTraining, BertModel, BertConfig, BertTokenizer, BertLMHeadModel
from tokenizers import BertWordPeiceTokenizer

from copy import deepcopy

import torch.nn as nn


class DialogBERTModel(nn.Module):
    def __iit(
        self,
        vocab_file_path,
        hidden_size=256,
        num_hidden_layers=6,
        num_attention_heads=2,
        intermediate_size=1024,
    ):
        super(DialogBERTModel, self).__init__()

        self.tokenizer = BertTokenizer(vocab_file=vocab_file_path)

        self.encoder_config = BertConfig(
            vocab_size=tokenizer.vocab_size,
            hidden_size=hidden_size,
            num_hidden_layers=num_hidden_layers,
            intermediate_size=intermedidate_size,
        )
        self.utterance_encoder = BertForPreTraining(self.encoder_config)
        self.context_encoder = BertModel(self.encoder_config)
        
        self.decoder_config = deepcopy(self.encoder_config)
        self.decoder_config.is_decoder = True
        self.decoder_config.add_cross_attention = True
        self.decoder = BertLMHeadModel(self.decoder_config)

    def forward(self, context, response):
        ## loss for response generation


        ## loss for dialog flow

        ## loss for context order prediction



