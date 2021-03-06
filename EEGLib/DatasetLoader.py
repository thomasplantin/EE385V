import os


class DatasetLoader:
    def __init__(self, root_folder):
        self.__root = root_folder
        self.__subject_dict = {}
        self.load_subjects()

    def load_subjects(self):
        data = {}
        folder = self.__root
        for subject in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, subject)):
                data[subject] = {}
                for trial in os.listdir(os.path.join(folder, subject)):
                    if os.path.isdir(os.path.join(folder, subject, trial)):
                        data[subject][trial] = []
                        for run in os.listdir(os.path.join(folder, subject, trial)):
                            if run.endswith('.gdf'):
                                data[subject][trial].append(run)
        self.__subject_dict = data
        return data

    def getOffline(self):
        data = self.__subject_dict
        offline = {}
        for subject in data.keys():
            offline[subject] = []
            for trials in data[subject].keys():
                if trials == 'Offline':
                    offline[subject] = data[subject][trials]
        return offline
