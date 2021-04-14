from torch.utils.data import Dataset

import os, sys
import dask.dataframe as dd


class ContextDataset(Dataset):
    """Custom Data loader for dialog dataframe set

    file_path_regex : file path regex to load dataframe files(csv format)
    sort_column_list : sort dialog session by provided columns
    session_column : grouping dialog seesion by provided column name(assert it in sort_column_list)
    turn_column : column name which distinguish user or system turn
    user_turn_value : value of turn column about user utterance
    system_turn_value : value of turn column about system utterance(inference this turn tokens in model)
    text_column : utterance contained column name
    tokenizer : tokenizer instance based on huggingface tokenizers
    min_context_length : min turn of context
    max_context_length : max turn of context
    max_token_length : max utterance token length
    """

    def __init__(
        self,
        file_path_regex: str,
        sort_column_list,
        session_column: str,
        turn_column: str,
        user_turn_value: str,
        system_turn_value: str,
        text_column: str,
        tokenizer,
        min_context_length=4,
        max_context_length=16,
        max_token_length=32,
    ):
        assert session_column in sort_column_list

        self.min_context_length = min_context_length
        self.max_context_length = max_context_length
        self.max_token_length = max_token_length

        self.contexts = []
        self.responses = []

        print("Loading data ...")
        df = dd.read_csv(file_path_regex).set_index(session_column).compute()

        print("Sorting by session & seq ...")
        df.sort_values(sort_column_list)

        print("Filtering valid dialogs ...")
        for session_key, group in df.groupby(session_column):
            if len(group) - 1 < self.min_context_length:  # -1 for response utterance
                continue

            while len(group) - 1 >= self.min_context_length:
                group = group.iloc[: -self.max_context_length]
                if group.iloc[-1][turn_column] != system_turn_value:
                    group = group.iloc[:-1]

            if self.min_context_length <= len(group) - 1 <= self.max_context_length:
                current_context = []
                # padding context & response tokens
                for row_index, row in group.iterrows():
                    if row_index < len(group) - 1:
                        tokens = self.tokenizer.encode(row[text_column])[:self.max_token_length-1] + [self.tokenizer.sep_token_id]
                        if len(tokens) < self.max_token_length:
                            tokens += [(self.max_token_length - len(tokens)) * self.tokenizer.pad_token_id]
                        current_context.append(tokens)
                    else:
                        tokens = self.tokenizer.encode(row[text_column])[:self.max_token_length-1] + [self.tokenizer.sep_token_id]
                        if len(tokens) < self.max_token_length:
                            tokens += [(self.max_token_length - len(tokens)) * self.tokenizer.pad_token_id]
                        self.responses.append(tokens)
 
                # padding context dialogs
                if len(current_context) < self.max_context_length:
                    for i in range(self.max_context_length - len(current_context)):
                        current_context.append([[self.tokenizer.pad_token_id] * self.max_token_length])


    def __getitem__(self, offset):
        # padding context & response
        current_context = self.contexts[offset]
        current_response = self.responses[offset]

    def __len__(self):
        return len(self.context)
