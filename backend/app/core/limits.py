from threading import Semaphore

AI_SEMAPHORE = Semaphore(2)

with AI_SEMAPHORE:
    response = call_llm(prompt)