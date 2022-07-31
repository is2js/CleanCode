import json
import pickle


class Serializer:
    def to_json(self):
        print(f"저는 self.__class__.__name__: {self.__class__.__name__}의 self.__dict__: {self.__dict__}입니다.")
        return json.dumps(self.__dict__)

    def to_pickle(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, path)