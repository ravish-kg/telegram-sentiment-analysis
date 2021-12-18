# telegram-sentiment-analysis

# How to run the code
1. Installing packages included in packages.txt
2. python main.py

# Summary
1. Extracted text messages from crypto telegram group (May 1st to May 15th).
2. Filtered messages that included "DOGE", "SHIB" words.
3. After extraction, messages are pre-processed and kept only messages that mentioned either "SHIB" or "DOGE".
4. Used NLTK library (VADER) to calculate positive, negative and compound scores.
5. Graph is plotted taking x-axis as date and y-axis as avg compound score (total compound score per day / number of messages).

# Graph

1. Y-Axis represents (total compound score / number of messages per day)
2. X-Axis represents Date.

![image](https://user-images.githubusercontent.com/87482237/146627825-2e012298-1d78-4cf1-a4b7-827b7acbd265.png)
