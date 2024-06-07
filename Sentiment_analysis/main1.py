import string
from collections import Counter
import matplotlib.pyplot as plt
from speech import transcribe_audio_to_text


filename = r"C:\Users\hp\OneDrive\Desktop\Final Year Project\Sentiment_analysis\WhatsApp Audio 2024-05-25 at 12.30.05_9c7aea89.waptt.wav"
text = transcribe_audio_to_text(filename)
print("Transcribed Text: ", text)  # Debugging


lower_case = text.lower()
print("Lowercase Text: ", lower_case)  # Debugging

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
print("Cleaned Text: ", cleaned_text)  # Debugging


tokenized_words = cleaned_text.split()
print("Tokenized Words: ", tokenized_words)  # Debugging

# List of stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
final_words = [word for word in tokenized_words if word not in stop_words]
print("Final Words: ", final_words)  # Debugging

# NLP Emotion Algorithm
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        if ':' in clear_line:  # Ensure line contains a colon to split
            word, emotion = clear_line.split(':')
            if word in final_words:
                emotion_list.append(emotion)

print("Emotion List: ", emotion_list)  # Debugging

# Count each emotion in the emotion list
w = Counter(emotion_list)
print("Emotion Counts: ", w)  # Debugging

# Ensure there is data to plot
if not w:
    print("No emotions found to plot.")
else:
    # Plotting the emotions on the graph
    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    plt.show()
