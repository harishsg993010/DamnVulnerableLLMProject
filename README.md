# Turn Yourself into a GPT3 AI Chat Bot

_Everyone needs someone to talk to - even if it is just your chat-bot clone_

# Set Up

1. Get your OpenAI API key and add it **Secrets** as `OPENAI_API_KEY`
2. Make up and `API_KEY` for the JSON API, this can just be something like a password if you'd like
3. Fill the `training/facts` folder with as many `text` documents as you can containing information about the person you're training it on. Top tips would be blog posts, transcripts of interviews, diary entries or anything written by the person.
4. Edit the `master.txt` file to represent who you want the bot to pretend to be
5. Click **Run**, select option `1`
6. To chat with the bot, once you've one the training, select option `2`

## JSON API (Advanced Users)
Option 3, or stating automatically after five seconds on the menu, is the JSON API. You can use POST requests to this Repl's `repl.co` address to take the chat to a different location or app.

Here's a quick guide to dealing with the API part in Python

`import requests`

### data to be sent to the server
`data = {'key': 'YOUR API KEY', 'question': 'Your question', 'history': 'previous questioning history'}`

### sending post request and saving response as response object 
`r = requests.post(url = URL, data = data) `
  
### extracting response json 
`response_data = r.json() `
  
### printing response 
`print(response_data)`

# Credit

All based on the [Amjad Masad Chat bot](https://ai.repl.page) by IronCladDev on Replit
For more information on how this works, check out [Zahid Khawaja's Tutorial](https://replit.com/@zahidkhawaja/Replit-Assistant?v=1).
