from fastapi import FastAPI

app = FastAPI()
is_ready = False

model = None
model = Pororo(task="sentiment", model="brainbert.base.ko.shopping", lang="ko")

if model:
	if is_ready = True


