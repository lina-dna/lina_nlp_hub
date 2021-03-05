from pororo import Pororo

#sentence_classification
natural_language_inference = Pororo(task="nli", lang="ko")
paraphrase_identification = Pororo(task="para", lang="ko")
review_scoring = Pororo(task="review", lang="ko")
semantic_textual_similarity = Pororo(task="similarity", lang="ko")
sentence_embedding = Pororo(task="sentence_embedding", lang="ko")
sentiment_analysis = Pororo(task="seniment", model="brainbert.base.ko.shopping", lang="ko")
topic_classification = Pororo(task="zero-topic", lang="ko")

#sequential_labeling
contextualized_embedding = Pororo(task="cse", lang="ko")
dependency_parsing = Pororo(task="dep_parse", lang="ko")
fill_in_blank = Pororo(task="fib", lang="ko")
machine_reading_comprehension = Pororo(task="mrc", lang="ko")
named_entity_recognition = Pororo(task="ner", lang="ko")
part_of_speech_tagging = Pororo(task="pos", lang="ko")
semantic_role_labeling = Pororo(task="srl", lang="ko")

#seq2seq
constituency_parsing = Pororo(task="const", lang="ko")
grammatical_error_correction = Pororo(task="gec", lang="ko")
grapheme_to_phoneme = Pororo(task="g2p", lang="ko")
paraphrase_generation = Pororo(task="pg", lang="ko")
question_generation = Pororo(task="qg", lang="ko")
text_summarization = Pororo(task="summarization", model="extractive", lang="ko")
word_send_disambiguation = Pororo(task="wsd", lang="ko")