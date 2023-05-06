import keras
from voice_identification.Tools.Predictor import *
from voice_identification import Container


def create_model(n_features, n_classes):

    model = Sequential()

    model.add(Dense(n_features, input_shape=(n_features,), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Dense(2048, activation='relu'))
    model.add(Dropout(0.4))

    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.4))

    model.add(Dense(2048, activation='relu'))
    model.add(Dropout(0.5))

    model.add(Dense(n_classes, activation='softmax'))

    model.compile(loss='categorical_crossentropy', metrics=['accuracy'])

    return model


class word_model:

    def __init__(self, words, load=False, path=""):

        data = pd.DataFrame()

        for word in words:
            word_data = getDataFromDir(f'{Container.getWordPath()}\\{word}/')
            # print(word_data)
            data = data.append(word_data)

        train, val = train_test_split(data, test_size=0.25, stratify=data['speaker'])
        self.ss = StandardScaler()

        train_features = getFeatures(train['filepath'], self.ss)
        val_features = getFeatures(val['filepath'], self.ss)
        # print(val_features)
        # print("next")
        header = ''
        for i in range(1, 25):
             header += f' mfcc{i}'
        header = header.split()
        # print('CSV Header: ', header)
        csvFileName = "val_features.csv"
        file = open(csvFileName, 'w', newline='')
        #with file:
        writer = csv.writer(file)
        writer.writerow(header)
        rowEnter = ''
        for i in val_features:
            for j in i:
                rowEnter = rowEnter + " " + str(j)
            rowEnter = rowEnter.split()

            writefile = open(csvFileName, "a", newline='')
            writer = csv.writer(writefile)
            writer.writerow(rowEnter)
            # print(rowEnter)
            rowEnter = ''
        # print(train_features)
        # print("next1")

        self.train_labels = train['speaker'].tolist()

        self.train_labels_encoded = getEncodedLabels(train['speaker'])
        val_labels = getEncodedLabels(val['speaker'])


        if load:
            self.model = keras.models.load_model(path)
            self.accuracy = self.model.evaluate(val_features, val_labels)
        else:
            self.model = create_model( N_MFCCS, len(self.train_labels_encoded[0]))
            history = self.model.fit(train_features, self.train_labels_encoded, epochs=50, validation_data=(val_features, val_labels))

            self.accuracy = history.history['val_accuracy']
