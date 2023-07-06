# DamnVulnerableLLMProject

This project is designed for Security Researchers to enhance their LLM hacking skills and for LLM Companies to secure their AI model and System against attackers

# Set Up

1. Get your OpenAI API key and add it **Secrets** as `OPENAI_API_KEY`
2. Make up and `API_KEY` for the JSON API, this can just be something like a password if you'd like
3. Fill the `training/facts` folder with as many `text` documents as you can containing information about anything including dummy credentials etc
4. Edit the `master.txt` file to represent who you want the bot to pretend to be
5. Click **Run**, select option `1`
6. To chat with the bot, once you've one the training, select option `2`

# OWASP top 10 LLM Vulnerabilities in this application

1. Prompt injection
2. Sensitive Data Disclosure on LLM
3. Unauthorised code injection on LLM
4. improper access control on LLM APIs
5. LLM Model poisoning (Undocumented in the writeup for a reason so find it on your own)  

# Writeup for Reference 

https://medium.com/@harishhacker3010/art-of-hacking-llm-apps-a22cf60a523b

# Credit

All based on the [Amjad Masad Chat bot](https://ai.repl.page) by IronCladDev on Replit
For more information on how this works, check out [Zahid Khawaja's Tutorial](https://replit.com/@zahidkhawaja/Replit-Assistant?v=1).
