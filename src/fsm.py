from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_searched_term(self, event):
        print("go to searched_term")

    def is_going_to_suggest_term(self, event):
        print("go to suggest_term")
    
    def is_going_to_symptom_category(self, event):
        print("go to symptom_category")
    
    def is_going_to_nutrition_category(self, event):
        print("go to nutrition_category")
    
    def is_going_to_diet_category(self, event):
        print("go to diet_category")
    
    def is_going_to_sport_category(self, event):
        print("go to sport_category")
    
    def is_going_to_disease_category(self, event):
        print("go to disease_category")
    
    def is_going_to_disease_category2(self, event):
        print("go to disease_category2")
    
    def is_going_to_bone_disease(self, event):
        print("go to bone_disease")
    
    def is_going_to_cranial_disease(self, event):
        print("go to cranial_disease")
    
    def is_going_to_ear_disease(self, event):
        print("go to ear_disease")
    
    def is_going_to_eye_disease(self, event):
        print("go to eye_disease")
    
    def is_going_to_gynecology_disease(self, event):
        print("go to gynecology_disease")
    
    def is_going_to_kidney_disease(self, event):
        print("go to kidney_disease")
    
    def is_going_to_liver_disease(self, event):
        print("go to liver_disease")
    
    def is_going_to_lung_disease(self, event):
        print("go to lung_disease")
    
    def is_going_to_mind_disease(self, event):
        print("go to mind_disease")
    
    def is_going_to_skin_disease(self, event):
        print("go to skin_disease")
    
    def is_going_to_heart_disease(self, event):
        print("go to heart_disease")
    
    def is_going_to_stomach_disease(self, event):
        print("go to stomach_disease")
    
    def is_going_to_urinary_disease(self, event):
        print("go to urinary_disease")
    
    def is_going_to_male_symptom(self, event):
        print("go to male_symptom")
    
    def is_going_to_female_symptom(self, event):
        print("go to female_symptom")
    
    def is_going_to_elder_symptom(self, event):
        print("go to elder_symptom")
    
    def is_going_to_child_symptom(self, event):
        print("go to child_symptom")
    
    