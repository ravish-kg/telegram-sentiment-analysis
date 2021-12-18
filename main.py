import datetime
from datetime import date, timedelta
from tqdm import tqdm
import nltk
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import plotly.graph_objects as go
import pandas as pd

nltk.download('vader_lexicon')


def filter_all_messages(filters):
    filtered_data = []
    f = open('result.json', "r")
    json_data = json.load(f)
    messages = json_data['messages']

    for index in tqdm(range(0, len(messages))):
        text = messages[index]['text']
        msg = messages[index]

        if text:
            is_present = any(([True if subStr in text else False for subStr in filters]))
            if is_present:
                filtered_data.append(msg)

    f.close()

    with open("filtered.json", "w") as outfile:
        json.dump(filtered_data, outfile, indent=4)

    return filtered_data


def calculate_sentiment_score(messages):
    analyser = SentimentIntensityAnalyzer()
    sentiment_scores = []

    for index in tqdm(range(0, len(messages))):
        polarity_scores = analyser.polarity_scores(messages[index]['text'])
        sentiment_scores.append((messages[index]['date'], messages[index]['text'], polarity_scores['compound']))
        
    return sentiment_scores


def find_avg_per_day(scored_messages):
    start_date = date(2021, 5, 1)
    end_date = date(2021, 5, 15)
    delta = timedelta(days=1)
    chart_data = []

    while start_date <= end_date:
        messages_per_day = list(
            filter(lambda x: datetime.datetime.fromisoformat(x[0]).date() == start_date, scored_messages))
        sum_per_day = 0

        for i in range(len(messages_per_day)):
            sum_per_day += messages_per_day[i][2]

        num_of_msgs = len(messages_per_day)

        if num_of_msgs > 0:
            avg = sum_per_day / num_of_msgs
            chart_data.append((start_date, num_of_msgs, avg))
        else:
            chart_data.append((start_date, num_of_msgs, 0))

        start_date += delta

    return chart_data


def plot(data):
    data_frame = pd.DataFrame(data)
    fig = go.Figure([go.Scatter(x=data_frame[0], y=data_frame[2])])
    fig.show()


if __name__ == '__main__':
    cleaned_data = filter_all_messages(['DOGE', 'SHIB', 'shib', 'doge'])

    computed_data = calculate_sentiment_score(cleaned_data)

    chart_data = find_avg_per_day(computed_data)
    plot(chart_data)
