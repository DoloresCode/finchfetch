from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Microorganism:
    def __init__(self, name, image, characteristics, description, manifestation, laboratory_diagnosis):
        self.name = name
        self.image = image
        self.characteristics = characteristics
        self.description = description
        self.manifestation = manifestation
        self.laboratory_diagnosis = laboratory_diagnosis

microorganisms = [
    Microorganism("Staphylococcus aureus", "https://i.pinimg.com/564x/42/11/f5/4211f594b5c1fda6797ebfc0c614fcc9.jpg", "1/ Gram stain: Staphylococci appear as Gram-positive cocci that occur singly and in pairs, tetrads, short chains, and irregular grape-like clusters, 2/ Catalase Test: Positive, 3/ Coagulase Test:  Positive, 4/ Non-motile, 5/ Non-sporing, 6/ Often unencapsulated or have a limited capsule, 7/ Facultative anaerobes.", "Staphylococcus aureus is a Gram-positive, round bacterium found in clusters. It's a common source of post-injury or surgical infections, affecting approximately 500,000 patients in American hospitals annually. This bacterium is present in all mammalian species and can transmit between species. Around 30 pourcent of healthy humans carry S. aureus in their nose, throat, and skin. Though S. aureus is carried by one-third of healthy individuals, it generally doesn't cause disease unless there's a break in the skin or other entry sites. It's considered an opportunistic bacterium, causing infections when the opportunity arises, particularly in immunocompromised or immunodeficient individuals. S. aureus can cause a variety of conditions, from minor skin infections to life-threatening diseases such as pneumonia, meningitis, osteomyelitis, endocarditis, toxic shock syndrome, bacteremia, and sepsis. Diagnosis can be challenging due to the bacteria's prevalence on the skin, nose, and throat of humans and animals. However, it can be identified via culture of suspicious lesions, presenting as characteristic yellow to white colonies on blood agar.", "Staphylococcus aureus, often shortened to S. aureus, can lead to a number of health problems. These include: 1/ Skin Infections & Surgical wound infections, 2/ Osteomyelitis, 3/ Food poisoning/gastroenteritis, 4/ Toxic shock syndrome, 5/ Pneumonia (mainly hospital-acquired), 6/ Acute endocarditis, 7/ Infective arthritis, 8/ Necrotizing fasciitis, 9/ Sepsis and Staphylococcal scalded skin syndrome (SSSS)", "The laboratory diagnosis of a Staphylococcus aureus infection includes: 1/ Gram staining: Gram-positive cocci in clusters, cocci may appear singly in pairs or in short chains. 2/ Sample Collection: Depending on the suspected infection site, a sample (like a swab or blood) is collected. 3/ Culture and Identification: - Blood Agar: The sample is cultured on blood agar. After incubation for 18 to 24 hours, S. aureus typically forms round, golden-yellow colonies with or without beta hemolysis. - Mannitol Salt Agar (MSA): This selective medium is also used for isolation of S. aureus. After inoculation, MSA plates are incubated at 35°C for 24 to 48 hours. S. aureus, being a mannitol fermenting bacterium, forms yellow or gold colonies on MSA.4/ Gram Stain and Catalase Test: S. aureus is Gram-positive (stains purple) and catalase-positive (produces bubbles when mixed with hydrogen peroxide). 5/ Coagulase Test: S. aureus produces an enzyme called coagulase that causes blood plasma to clot. 6/ Antibiotic Susceptibility Testing: This test identifies which antibiotics the bacteria are sensitive to, guiding treatment. 7/ Molecular Testing: Techniques like PCR may be used for further identification or to detect virulence factors or antibiotic resistance genes."),
]

class MicroorganismIndex(TemplateView):
    template_name = "microorganism_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["microorganisms"] = microorganisms
        return context