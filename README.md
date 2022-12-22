# ChatGPT Voice Assistant

Not really a voice assistant, but rather ChatGPT without a keyboard.


## Usage
1.  `pip install -r requirements.txt`
2.  `python main.py`
3. You can now open and edit `settings/settings.json`
- **prefix:** is used to know where is the beginning of a sentence, it's like "Alexa" or "Ok google".
- **api-key:** The OpenAI API uses API keys for authentication. Visit your [API Keys](https://beta.openai.com/account/api-keys "here") page to retrieve the API key you'll use in your requests, 18$ of credits are free.
- **engine:** OpenIA API setting, the default one (`text-davinci-003`) is the best for ChatGPT-3, you can find the others engines [here](https://beta.openai.com/docs/models/gpt-3 "here").
- **max_tokens** OpenIA API setting which is used to put a limit on your request so as not to use too many tokens.
- **temperature:** Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer.
- **language:** .
- **voice selected  &  voices:** Change voice, documentation [here](https://support.microsoft.com/en-gb/topic/download-languages-and-voices-for-immersive-reader-read-mode-and-read-aloud-4c83a8d8-7486-42f7-8e46-2b0fdf753130: "here")
- **device selected  &  audio devices:** Select your microphone, make sure to select the first one with the name of your microphone, if the microphone does not work, try another one.
