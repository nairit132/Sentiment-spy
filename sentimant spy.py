import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.CYAN} 🐍 Welcome to senimant spy!!🐍 {Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mytery Agent"
conversation_history = []
print(f"{Fore.CYAN}Hello, Agent {user_name}!")
print("Type a Sentence and i will analyze your sentence with TextBlob ans show you the sentiment.")
print(f" Type {Fore.YELLOW}reset{Fore.CYAN} to quit {Style.RESET_ALL}\n")
while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE} EXITING SENIMENT SPY. Farewell Agent{user_name} ")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"\n{Fore.CYAN} All converation history cleared, Agent{user_name} {Style.RESET_ALL} ")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"\n{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL} ")
        else:
            print(f"{Fore.CYAN} Converation History: {Style.RESET_ALL}")
            for idx, (text, polarity, sentimant_type) in enumerate(conversation_history, start=1):
                if sentimant_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentimant_type == "Negitive":
                    color = Fore.RED
                    emoji = "☹️"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(f"{idx}. {color}{emoji} {text} "
                    f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
        continue

    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😭"

    # Store in history
    conversation_history.append((user_input, polarity, sentiment_type))

    # Print result with color, emojis, and polarity
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
        f"Polarity: {polarity:.2f}")