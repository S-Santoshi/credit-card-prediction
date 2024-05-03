import pickle
from joblib import load

model = load('backend/model.joblib')
g=load('backend/gender.joblib')
# with open("backend/model.pkl", 'rb') as f:
#     model = pickle.load(f)
             

data={'gender': 'F', 'property': '1', 'car': '1', 'children': '3', 'income': '123456', 'emplymentStatus': 'Working', 'education': 'Secondary / secondary special', 'maritalStatus': 'Married', 'dwelling': 'With parents', 'age': '28', 'employmentDate': '2022-06-03', 'workPhone': '1', 'phone': '1', 'email': '1', 'jobTitle': 'IT staff', 'familyMemberCount': '3', 'accountAge': '10'}


def clean_data(data):

    columns_to_encode = ['gender', 'emplymentStatus', 'education', 'maritalStatus', 'dwelling']
    for column in columns_to_encode:
        # label_encoder = load(f'backend/{column}.joblib')
        g.fit_transform(data[column])
    print(data)
    del data['jobTitle']
    # for k,v in data.items():
        

def process_data(data):
    data=clean_data(data)
    pred=model.predict(data)

process_data(data)