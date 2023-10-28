import argparse

from src.video import VideoReader
from src.statistics import cluster_by_level, cluster_by_pos

def parse_args():

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Script for translating pot files to po files')

    parser.add_argument("--video-path", required=True,
                        metavar="INPUT",
                        help="video folder")

    parser.add_argument('-l', action='store_true',help="level of phrases")
    parser.add_argument('-p', action='store_true',help="part of speech of words")


    args = parser.parse_args()

    return args.video_path , args.l, args.p


video_path , level_of_phrases , pos_of_words = parse_args()

video_reader = VideoReader()

video = video_reader.read(video_path)
print(video)

if level_of_phrases:
    levels = cluster_by_level(video)
    print("---","Phrases by level","---")
    for k in sorted(levels.keys()):
        print(k,len(levels[k]))
if pos_of_words:
    pos = cluster_by_pos(video)
    print("---","Words by part of Speech","---")
    for k in sorted(pos.keys()):
        print(k,len(pos[k]))
