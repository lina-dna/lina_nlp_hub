from pororo import Pororo

import streamlit as st

st.title('Pororo sentiment analysis engine')

#load model
@st.cache(allow_output_mutation=True)
def load_model():
	with st.spinner('Loading pororo sentiment analysis model ...'):
		model = Pororo(task="sentiment", model="brainbert.base.ko.shopping", lang="ko")

		return model

if __name__ == '__main__':
	st.subheader('pororo sentiment_analysis')
	model = load_model()

	sentiment_input = st.text_input('query: ')
	if sentiment_input != '':
		with st.spinner('Predicting ...'):
			st.json(model(sentiment_input, show_probs=True))


