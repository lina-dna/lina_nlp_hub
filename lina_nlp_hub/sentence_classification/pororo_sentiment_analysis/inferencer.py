from fastapi import FastAPI
from pororo import Pororo

app = FastAPI()
is_ready = False

model = None
model = Pororo(task="sentiment", model="brainbert.base.ko.shopping", lang="ko")

if model:
	is_ready = True

#endpoints
@app.get("/")
async def health():
	if is_ready:
		output = {'code': 200}
	else:
		output - {'code': 500}

@app.post("/predict")
async def predict_sentiment(text: str):
	#return format example -> {'negative': 0.7525266408920288, 'positive': 0.2474733293056488}
	return model(text, show_probs=True)

