import json
from colorama import init, Fore, Style

# Initialize colorama
init()

# Define colors
PROMPT_COLOR = Fore.YELLOW
INPUT_COLOR = Fore.CYAN

inp_arr = []
dic={}
print(PROMPT_COLOR + 'Please enter your input to the model to predict the chances of having brain stroke' + Style.RESET_ALL)
gender=input(INPUT_COLOR + "What is your gender? (M/F): " + Style.RESET_ALL)
dic['gender']=1 if gender=='F' or gender=='f' else 0
inp_arr.append(dic['gender'])

dic['age']=int(input(INPUT_COLOR + 'How old are you?: ' + Style.RESET_ALL))
inp_arr.append(dic['age'])

hypertension=input(INPUT_COLOR + "Do you have hypertension? (Y/N): " + Style.RESET_ALL)
dic['hypertension']= 1 if hypertension=='Y' or hypertension=='y' else 0
inp_arr.append(dic['hypertension'])

heart_disease=input(INPUT_COLOR + "Do you have any heart disease?(Y/N): " + Style.RESET_ALL)
dic['heart_disease']= 1 if heart_disease=='Y' or heart_disease=='y' else 0
inp_arr.append(dic['heart_disease'])

married=input(INPUT_COLOR + "Have you ever been married? (Y/N): " + Style.RESET_ALL)
dic['ever_married']= 1 if married=='Y' or married=='y' else 0
inp_arr.append(dic['ever_married'])

worked=input(INPUT_COLOR + "What is your work type (Govt job/ private job/ self employed/ children): " + Style.RESET_ALL)
dic['worked_type']=0 if worked=='Govt job' else 1 if worked=='private job' else 2 if worked=='self employed' else 3
inp_arr.append(dic['worked_type'])

residence_type=input(INPUT_COLOR + "What is your residence type? (rural/urban): " + Style.RESET_ALL)
dic['Residence_type']= 0 if residence_type=='rural' else 1
inp_arr.append(dic['Residence_type'])

dic['avg_glucose_level']=int(input(INPUT_COLOR + "What is your average glucose level? " + Style.RESET_ALL))
inp_arr.append(dic['avg_glucose_level'])

dic['bmi']=float(input(INPUT_COLOR + "What is your BMI: " + Style.RESET_ALL))
inp_arr.append(dic['bmi'])

smoke=input(INPUT_COLOR + "Do you Smoke? (prefer not to say/ formerly/ never/ smokes): " + Style.RESET_ALL)
dic['smoking_status']=0 if smoke=='prefer not to say' else 1 if smoke=='formerly' else 2 if smoke=='never' else 3
inp_arr.append(dic['smoking_status'])

# Convert dictionary to JSON string
json_data = json.dumps(inp_arr)

# Save JSON data to file
with open("user_input.json", "w") as file:
    json.dump(json_data, file)
    