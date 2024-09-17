import csv
# List of basic phrases and their translations
phrases = [
    # Greetings & Introductions
    ("こんにちは", "Konnichiwa", "Hello / Good afternoon"),
    ("おはようございます", "Ohayou gozaimasu", "Good morning"),
    ("こんばんは", "Konbanwa", "Good evening"),
    ("さようなら", "Sayounara", "Goodbye"),
    ("お元気ですか？", "Ogenki desu ka?", "How are you?"),
    ("はじめまして", "Hajimemashite", "Nice to meet you"),
    ("わたしの名前は___です", "Watashi no namae wa ___ desu", "My name is ___"),
    ("よろしくお願いします", "Yoroshiku onegaishimasu", "Please treat me well / Nice to meet you"),
    
    # Politeness & Responses
    ("ありがとうございます", "Arigatou gozaimasu", "Thank you (polite)"),
    ("どういたしまして", "Dou itashimashite", "You're welcome"),
    ("すみません", "Sumimasen", "Excuse me / Sorry"),
    ("はい", "Hai", "Yes"),
    ("いいえ", "Iie", "No"),
    ("わかりません", "Wakarimasen", "I don’t understand"),
    ("もう一度お願いします", "Mou ichido onegaishimasu", "Please say that again"),
    
    # Common Daily Phrases
    ("これ/それ/あれは何ですか？", "Kore / Sore / Are wa nan desu ka?", "What is this/that?"),
    ("いくらですか？", "Ikura desu ka?", "How much is this?"),
    ("トイレはどこですか？", "Toire wa doko desu ka?", "Where is the bathroom?"),
    ("助けてください", "Tasukete kudasai", "Please help me"),
    ("ちょっと待ってください", "Chotto matte kudasai", "Please wait a moment"),
    
    # Numbers & Shopping
    ("一", "Ichi", "One"),
    ("二", "Ni", "Two"),
    ("三", "San", "Three"),
    ("百", "Hyaku", "Hundred"),
    ("これをください", "Kore o kudasai", "I’ll take this, please"),
    ("すごい！", "Sugoi!", "Amazing!")
]

# Filepath to save the CSV
csv_file_path = 'japanese_basic_conversation_anki.csv'

# Writing to CSV file in Anki-compatible format (Japanese word, pronunciation, meaning)
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Japanese", "Pronunciation", "Meaning"])  # Header row
    writer.writerows(phrases)

print(f"Japanese Basic Conversation Anki CSV created: {csv_file_path}")
