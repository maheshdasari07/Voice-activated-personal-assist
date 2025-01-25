import speech_recognition as sr
import pyttsx3
import requests
import datetime

engine = pyttsx3.init()
engine.say("Hello! i'm here to help you with your tasks")
engine.runAndWait()

while True:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognozer.adjust_for_ambient_noise(source, duration= 2)
        print("Please say something:")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recogniozer.recognizer_google(audio, language = "en-US").lower()
            print("You: ", text)
        except sr.UnknownValueError:
            print("Assistent: Sorry, I didn't catch that")
            engine.say("Sorry, I didn't catch that")
        if "Weather" in text:
            city = "Hyderabad"
            api_key = "a8eb78858fba3146bcf8f45ecca9b0e475c6e1717ad82c19b6cfa6286425f0a0"
            base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(base_url)
            if response.satus_code == 200:
                data = response.json()
                weather = data["weather"][0]["description"]
                temp = data["main"]["temp"]
                print(f"Assistant: Weather in {city}: is {weather} and temperature is {temp} degree c")
                engine.say(f"Assistant: Weather in {city}: is {weather} and temperature is {temp} degree c")

            else:
                engine.say("Assistant: Unable to fetch weather data")
                print("Assistant: Unable to fetch weather data")
            engine.runAndWait()
        elif "news" in text:
            api_key_news = "0b659b425fb74b519e53eb32e7aaaf30"
            base_url_news = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key_news}"
            response_news = requests.get(base_url_news)
            if response_news.status_code == 200:
                articals = response.json().get("articals",[])
                headlines = [artical['title'] for article in articals[:5]]
                print("Assistant: Here are the top 5 news headlines")
                for i, headline in enumerate(headlines,1):
                    print(f"{i}. {headline}")
                engine.say("Here are the top 5 news headlines: " * ", ".join(headlines))
                engine.runAndWait()
        elif "time" in text:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"The current time is {time}.")
            engine.say(f"The current time is {time}.")
            engine.runAndWait()


        elif "exit" or "quit" in text:
            engine.say("Assistant: Goodbye!")
            break

        else:
            print("Assistant: I'm not sure how to help with that.")
            engine.say("Assistant: I'm not sure how to help with that.")
            engine.runAndWait()
    
