import pickle

input_path = "/content/gdrive/MyDrive/Datathon2022/datathon.pkl"

infile = open(input_path, 'rb')
test_model = pickle.load(infile)

infile.close()

forecast = test_model.predict(10)
print(forecast)