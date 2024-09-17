import csv
# List of Katakana characters and their pronunciations
katakana = [
    ("ア", "a"), ("イ", "i"), ("ウ", "u"), ("エ", "e"), ("オ", "o"),
    ("カ", "ka"), ("キ", "ki"), ("ク", "ku"), ("ケ", "ke"), ("コ", "ko"),
    ("サ", "sa"), ("シ", "shi"), ("ス", "su"), ("セ", "se"), ("ソ", "so"),
    ("タ", "ta"), ("チ", "chi"), ("ツ", "tsu"), ("テ", "te"), ("ト", "to"),
    ("ナ", "na"), ("ニ", "ni"), ("ヌ", "nu"), ("ネ", "ne"), ("ノ", "no"),
    ("ハ", "ha"), ("ヒ", "hi"), ("フ", "fu"), ("ヘ", "he"), ("ホ", "ho"),
    ("マ", "ma"), ("ミ", "mi"), ("ム", "mu"), ("メ", "me"), ("モ", "mo"),
    ("ヤ", "ya"), ("ユ", "yu"), ("ヨ", "yo"),
    ("ラ", "ra"), ("リ", "ri"), ("ル", "ru"), ("レ", "re"), ("ロ", "ro"),
    ("ワ", "wa"), ("ヲ", "wo"), ("ン", "n")
]
# List of Hiragana characters and their pronunciations
hiragana = [
    ("あ", "a"), ("い", "i"), ("う", "u"), ("え", "e"), ("お", "o"),
    ("か", "ka"), ("き", "ki"), ("く", "ku"), ("け", "ke"), ("こ", "ko"),
    ("さ", "sa"), ("し", "shi"), ("す", "su"), ("せ", "se"), ("そ", "so"),
    ("た", "ta"), ("ち", "chi"), ("つ", "tsu"), ("て", "te"), ("と", "to"),
    ("な", "na"), ("に", "ni"), ("ぬ", "nu"), ("ね", "ne"), ("の", "no"),
    ("は", "ha"), ("ひ", "hi"), ("ふ", "fu"), ("へ", "he"), ("ほ", "ho"),
    ("ま", "ma"), ("み", "mi"), ("む", "mu"), ("め", "me"), ("も", "mo"),
    ("や", "ya"), ("ゆ", "yu"), ("よ", "yo"),
    ("ら", "ra"), ("り", "ri"), ("る", "ru"), ("れ", "re"), ("ろ", "ro"),
    ("わ", "wa"), ("を", "wo"), ("ん", "n")
]
# List of basic Kanji characters with their pronunciations and meanings
kanji = [
    ("日", "nichi", "Day/Sun"),
    ("本", "hon", "Book"),
    ("人", "jin", "Person"),
    ("月", "getsu", "Month/Moon"),
    ("火", "ka", "Fire"),
    ("水", "sui", "Water"),
    ("木", "moku", "Tree"),
    ("金", "kin", "Gold/Money"),
    ("土", "do", "Earth"),
    ("何", "nani", "What"),
    ("大", "dai", "Big"),
    ("小", "shou", "Small"),
    ("中", "chuu", "Middle"),
    ("上", "ue", "Up"),
    ("下", "shita", "Down"),
]

# List of advanced sounds including Dakuten, Handakuten, and Combo (Yōon) sounds
advanced_sounds = [
    # Dakuten (゛) - Voiced versions of regular syllables
    ("が", "ga"), ("ぎ", "gi"), ("ぐ", "gu"), ("げ", "ge"), ("ご", "go"),
    ("ざ", "za"), ("じ", "ji"), ("ず", "zu"), ("ぜ", "ze"), ("ぞ", "zo"),
    ("だ", "da"), ("ぢ", "ji"), ("づ", "zu"), ("で", "de"), ("ど", "do"),
    ("ば", "ba"), ("び", "bi"), ("ぶ", "bu"), ("べ", "be"), ("ぼ", "bo"),

    # Handakuten (゜) - "P" sounds
    ("ぱ", "pa"), ("ぴ", "pi"), ("ぷ", "pu"), ("ぺ", "pe"), ("ぽ", "po"),

    # Combo (Yōon) - Small ゃ, ゅ, ょ with different consonants
    ("きゃ", "kya"), ("きゅ", "kyu"), ("きょ", "kyo"),
    ("しゃ", "sha"), ("しゅ", "shu"), ("しょ", "sho"),
    ("ちゃ", "cha"), ("ちゅ", "chu"), ("ちょ", "cho"),
    ("にゃ", "nya"), ("にゅ", "nyu"), ("にょ", "nyo"),
    ("ひゃ", "hya"), ("ひゅ", "hyu"), ("ひょ", "hyo"),
    ("みゃ", "mya"), ("みゅ", "myu"), ("みょ", "myo"),
    ("りゃ", "rya"), ("りゅ", "ryu"), ("りょ", "ryo"),

    # Long vowels (おう, えい) and double consonants (っ)
    ("こう", "kou"), ("とう", "tou"), ("えい", "ei"),
    ("まっすぐ", "massugu"), ("がっこう", "gakkou")
]
# Filepath to save the Katakana CSV
katakana_csv_path = 'katakana_anki.csv'
# Filepath to save the Hiragana CSV
hiragana_csv_path = 'hiragana_anki.csv'
# Filepath to save the Kanji CSV
kanji_csv_path = 'kanji_anki.csv'

# Filepath to save the advanced sounds CSV
advanced_sounds_csv_path = 'advanced_japanese_sounds_anki.csv'


# Writing Katakana to CSV file
with open(katakana_csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Katakana", "Pronunciation"])  # Header row
    writer.writerows(katakana)

print(f"Katakana CSV created: {katakana_csv_path}")

# Writing Kanji to CSV file
with open(kanji_csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Kanji", "Pronunciation", "Meaning"])  # Header row
    writer.writerows(kanji)

print(f"Kanji CSV created: {kanji_csv_path}")

# Writing Hiragana to CSV file
with open(hiragana_csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Hiragana", "Pronunciation"])  # Header row
    writer.writerows(hiragana)

print(f"Hiragana CSV created: {hiragana_csv_path}")

# Writing advanced sounds to CSV file
with open(advanced_sounds_csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Japanese", "Pronunciation"])  # Header row
    writer.writerows(advanced_sounds)

print(f"Advanced Sounds CSV created: {advanced_sounds_csv_path}")
