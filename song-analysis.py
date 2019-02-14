#Create a bar chart histogram of song lyrics
import plotly
from plotly import offline
from plotly.offline import iplot, init_notebook_mode
from plotly import tools
import plotly.graph_objs as go
offline.init_notebook_mode()

lyrics = "Ah, Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann Oh Barbara Ann Take My Hand Barbara Ann You Got Me Rockin' And A-Rollin' Rockin' And A-Reelin' Barbara Ann Ba Ba Ba Barbara Ann ...More Lyrics... Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann"
list_of_lyrics = lyrics.split(' ')

unique_words = set(list_of_lyrics)

word_histogram = dict.fromkeys(unique_words, 0)
for word in list_of_lyrics:
    word_histogram[word] = word_histogram[word]+ 1

trace = {'type': 'bar', 'x': list(unique_words), 'y': list(word_histogram.values())}

plotly.offline.iplot({'data': [trace]})
