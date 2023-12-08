from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for lines in story:
    line_words = lines.decode('utf8').split()
    print(line_words)
    for words in line_words:
        story_words.append(words)

story.close()
print(story_words)