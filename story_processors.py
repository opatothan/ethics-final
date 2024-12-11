import json

class Event():
    def __init__(self, text):
        self.text = text
        self.choices = []
    
    def display(self):
        if isinstance(self.text, list):
            for line in self.text:
                print(line)
        else:
            print(self.text)
        print()
        for i, choice in enumerate(self.choices):
            print(f"[{i+1}]: {choice.text}")
    
    def select_choice(self, num):
        return self.choices[num].score, self.choices[num].next_event, self.choices[num].income

    def get_num_choices(self):
        return len(self.choices)
    
class Choice():
    def __init__(self, text, score, next_event, income = 0):
        self.id = id
        self.text = text
        self.score = score
        self.next_event = next_event
        self.income = income

"""
builds story from filename, returns first event
"""
def build_story(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        events = {}
        for index, event in data.items():
            events[index] = Event(event["event_text"])
        
        for index, event in data.items():
            choices = []
            for choice_data in event['choices']:
                income = 0 if "income" not in choice_data else choice_data["income"]
                choices.append(Choice(choice_data["text"], choice_data["score"], events[choice_data["next"]], income))
            events[index].choices = choices
    
    return events["0"]
            
            


