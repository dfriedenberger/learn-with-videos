import os
import json
import polib


class Video:

    def __init__(self,id):
        self.id = id
        self.dataset = None
        self.metadata = None
        self.translation = {}

    def __repr__(self):
        return f'Video({self.metadata["title"]}, {len(self.dataset)}, {self.translation.keys()})'


class VideoReader:


    def read(self,folder):

        id = os.path.basename(folder.strip("/"))

        video = Video(id)

        metadata_file = os.path.join(folder,"metadata.json")
        with open(metadata_file,encoding="UTF-8") as f:
            video.metadata = json.load(f)

        # read phrases
        with open(os.path.join(folder,"phrases.json"),encoding="UTF-8") as f:
            video.dataset = json.load(f)

        # read translations
        for lang in ["de","en","es"]:
            po_file = os.path.join(folder,f"{lang}.po")
            if not os.path.isfile(po_file):
                continue

            language_dict = dict()
            po = polib.pofile(po_file)
            for entry in po:
                language_dict[entry.msgid] = entry.msgstr

            video.translation[lang] = language_dict

        return video