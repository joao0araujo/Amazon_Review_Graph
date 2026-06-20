import gzip, json

with gzip.open("Video_Games.jsonl.gz", "rt") as f:
    for i, line in enumerate(f):
        print(json.loads(line))
        if i == 2:1
        break
