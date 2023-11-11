import os
import hashlib

from .video import VideoReader
from .statistics import get_max_level


class VideoRepository:

    def __init__(self,folder):


        video_reader = VideoReader()

        self.videos = []
        for video_folder in os.listdir(folder):
            path = os.path.join(folder,video_folder)
            if not os.path.isdir(path):
                continue
            video = video_reader.read(path)
            self.videos.append(video)

    def get_metadata_list(self):

        metadata = []

        for video in self.videos:
            metadata.append({
                "id" : video.id,
                "title" : video.metadata['title']
            })

        return metadata

    def get_vocabulary(self,video_id,language):

        vocabulary = []

        for video in self.videos:

            if video.id != video_id:
                continue

            for phrase in video.dataset:

                #TODO check parameters and existence of translation
                translation = video.translation[language][phrase['text']]

                level = get_max_level(phrase)


                vocabulary.append({
                    "id" : hashlib.md5(phrase['text'].encode('utf-8')).hexdigest(),
                    "text" : phrase['text'],
                    "translation" : translation,
                    "level" : level,
                    "token" : phrase['words']
                })
         
        return vocabulary
