from django.shortcuts import render
from django.views import View
from .models import Microorganism
from django.http import HttpResponse 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

# class Microorganism:
#     def __init__(self, name, image, characteristics, description, manifestations, laboratory_diagnosis):
#         self.name = name
#         self.image = image
#         self.characteristics = characteristics
#         self.description = description
#         self.manifestations = manifestations
#         self.laboratory_diagnosis = laboratory_diagnosis

# microorganisms = [
#     Microorganism("Staphylococcus aureus", "https://i.pinimg.com/564x/42/11/f5/4211f594b5c1fda6797ebfc0c614fcc9.jpg", "Characteristics: 1/ Gram stain: Staphylococci appear as Gram-positive cocci that occur singly and in pairs, tetrads, short chains, and irregular grape-like clusters, 2/ Catalase Test: Positive, 3/ Coagulase Test:  Positive, 4/ Non-motile, 5/ Non-sporing, 6/ Often unencapsulated or have a limited capsule, 7/ Facultative anaerobes.", "Description: Staphylococcus aureus is a Gram-positive, round bacterium found in clusters. It's a common source of post-injury or surgical infections, affecting approximately 500,000 patients in American hospitals annually. This bacterium is present in all mammalian species and can transmit between species. Around 30 pourcent of healthy humans carry S. aureus in their nose, throat, and skin. Though S. aureus is carried by one-third of healthy individuals, it generally doesn't cause disease unless there's a break in the skin or other entry sites. It's considered an opportunistic bacterium, causing infections when the opportunity arises, particularly in immunocompromised or immunodeficient individuals. S. aureus can cause a variety of conditions, from minor skin infections to life-threatening diseases such as pneumonia, meningitis, osteomyelitis, endocarditis, toxic shock syndrome, bacteremia, and sepsis. Diagnosis can be challenging due to the bacteria's prevalence on the skin, nose, and throat of humans and animals. However, it can be identified via culture of suspicious lesions, presenting as characteristic yellow to white colonies on blood agar.", "Manifestations: Staphylococcus aureus, often shortened to S. aureus, can lead to a number of health problems. These include: 1/ Skin Infections & Surgical wound infections, 2/ Osteomyelitis, 3/ Food poisoning/gastroenteritis, 4/ Toxic shock syndrome, 5/ Pneumonia (mainly hospital-acquired), 6/ Acute endocarditis, 7/ Infective arthritis, 8/ Necrotizing fasciitis, 9/ Sepsis and Staphylococcal scalded skin syndrome (SSSS)", "Laboratory_diagnosis: The laboratory diagnosis of a Staphylococcus aureus infection includes: 1/ Gram staining: Gram-positive cocci in clusters, cocci may appear singly in pairs or in short chains. 2/ Sample Collection: Depending on the suspected infection site, a sample (like a swab or blood) is collected. 3/ Culture and Identification: - Blood Agar: The sample is cultured on blood agar. After incubation for 18 to 24 hours, S. aureus typically forms round, golden-yellow colonies with or without beta hemolysis. - Mannitol Salt Agar (MSA): This selective medium is also used for isolation of S. aureus. After inoculation, MSA plates are incubated at 35°C for 24 to 48 hours. S. aureus, being a mannitol fermenting bacterium, forms yellow or gold colonies on MSA.4/ Gram Stain and Catalase Test: S. aureus is Gram-positive (stains purple) and catalase-positive (produces bubbles when mixed with hydrogen peroxide). 5/ Coagulase Test: S. aureus produces an enzyme called coagulase that causes blood plasma to clot. 6/ Antibiotic Susceptibility Testing: This test identifies which antibiotics the bacteria are sensitive to, guiding treatment. 7/ Molecular Testing: Techniques like PCR may be used for further identification or to detect virulence factors or antibiotic resistance genes."),
#     Microorganism("Enterococcus faecalis", "https://microbe-canvas.com/uploads/image/bacterien/enterococcus-faecalis/enterococcus-faecalis_bk_gram-2_f-350x220.jpg", "Characteristics: 1/ Gram-positive, 2/ cocci, 3/ diplococci, 4/ growth both-aerobic-and-anaerobic, 5/ catalase-negative, 6/ oxidase-negative, 7/ phrase-positive, 8/ vancomycin-susceptible, 9/ penicillin-resistant, 10/ esculin-positive, 11/ bile-tolerance, 12/ NaCl 6.5%-tolerance", "Description: Enterococci, including species such as Enterococcus faecalis and Enterococcus faecium, are gram-positive bacteria commonly found in soil, food, water, and as part of the normal flora in animals and humans. They are particularly prevalent in the human gastrointestinal and female genitourinary tracts. Enterococci can cause infections when they gain access to sterile sites in the body, often during gastrointestinal or genitourinary procedures. They are especially significant in hospital settings, where they can be transmitted person-to-person or via contaminated medical equipment. Enterococcus faecalis is a notable cause of hospital-acquired urinary tract infections and endocarditis.These bacteria have a variety of virulence factors, such as cytolysin/hemolysin, which can lyse red blood cells, and aggregation substances that promote clumping of cells and facilitate the transfer of drug resistance.Treatment of enterococcal infections usually involves a combination of penicillin or ampicillin and an aminoglycoside such as gentamicin. This regimen is typically effective due to their synergistic effect, as penicillin or vancomycin can weaken the bacterial cell wall, allowing the aminoglycoside to penetrate. In cases of resistance, vancomycin is used, and linezolid is an option for treating vancomycin-resistant enterococci (VRE). Preventive measures include administering penicillin and gentamicin to patients with damaged heart valves prior to certain procedures. As of now, there is no vaccine available for enterococci.", "Manifestations: Enterococci, due to their intrinsic and increased drug resistance, are primarily responsible for hospital-acquired (nosocomial) infections. They can cause a variety of conditions including urinary tract infections (such as cystitis, urethritis, pyelonephritis, and prostatitis), blood infections (bacteremia), and life-threatening heart infections (mitral valve endocarditis). They may also lead to intra-abdominal, pelvic, and soft tissue infections, eye infections, and rarely, meningitis and respiratory tract infections.", "Laboratory Diagnosis: In the laboratory, E. faecalis is typically isolated from samples such as urine or pus from infected sites. Identification relies on cultural characteristics, microscopic observation, and biochemical tests. For precise identification and genetic characterization, molecular diagnosis is also used. There is no special requirement for sample collection, transportation, or processing. I - Macroscopy and Culture: Enterococci can be identified through the following features: 1/ They are gram-positive bacteria, appearing as oval shapes organized in pairs with a distinctive angle between them, resembling a 'spectacle-eyed' look. 2/ When cultured on blood agar, they yield smooth, gray, and typically non-hemolytic translucent colonies. However, α or β hemolysis can sometimes occur. 3/ On MacConkey agar, they generate minute magenta pink colonies. 4/ They show poor growth on nutrient agar. 5/ Enterococci can thrive under extreme conditions, including high salt concentrations (6.5% NaCl), high bile content (40%), high pH levels (9.6), and a wide range of temperatures (10°C to 45°C). 6/ They exhibit heat resistance, surviving temperatures of 60°C for up to 30 minutes. 7/ Enterococci are categorized into five groups (I to V) based on mannitol fermentation and arginine hydrolysis characteristics. E.faecalis and E. faecium are part of group II and can be further differentiated by additional biochemical traits. II - Biochemical tests:  They are important for the differentiation and identification of Enterococcus faecalis. To conclusively identify the bacteria as E. faecalis, once it's established as Gram-positive cocci, a sequence of biochemical analyses is performed. Regularly utilized tests include the catalase test, oxidase test, LAP test, and PYR test. The Bile Esculin test, examination of growth in 6.5% NaCl, arginine dihydrolase test, and tests for carbohydrate fermentation (including pyruvate, mannitol, and raffinose) are also commonly employed. Several biochemical tests help differentiate and identify Enterococcus faecalis: 1/ Catalase Test: E. faecalis tests negative, assisting in differentiating it from staphylococci. 2/ Hemolysis: E. faecalis is typically non-hemolytic. 3/ Motility Test: E. faecalis is non-motile. This distinguishes it from E. gallinarum and E. casseliflavus, which are motile. 4/ Pyrrolidonyl-β-naphthylamide (PYR) Test: E. faecalis tests positive, enabling presumptive identification of group A beta-hemolytic streptococci and enterococci. 5/ Esculin and Bile-Esculin Test: E. faecalis tests positive (with growth and black precipitate), helping differentiate enterococci from non-enterococcus group D streptococci. 6/ Bile Solubility Test: E. faecalis is insoluble in bile, unlike S. pneumoniae, which is bile soluble. 7/ LAP Test: E. faecalis tests positive, used for identifying catalase-negative, gram-positive cocci. 8/ Pyruvate Broth: E. faecalis tests positive, aiding in differentiating it from E. faecium, which tests negative. 9/ Salt Tolerance Test: E. faecalis tests positive, allowing differentiation between enterococci and non-enterococci. There are also specific features to differentiate between E. faecalis and E. faecium: 1/ Arabinose: E. faecalis does not ferment arabinose, while E. faecium does. 2/ Sorbitol: E. faecalis ferments sorbitol, whereas E. faecium does not. 3/ Pyruvate: E. faecalis ferments pyruvate, unlike E. faecium. III - Molecular Diagnosis: For a quicker and more precise identification, molecular diagnostic techniques such as PCR and sequencing, rRNA sequencing, and Matrix-Assisted Laser Desorption/Ionization Time-of-Flight Mass Spectrometry (MALDI-TOF MS) are favored. Nonetheless, these methods are rarely utilized in clinical diagnosis."),
#     Microorganism("Escherichia coli", "https://img.freepik.com/premium-photo/microscopic-view-gram-stain-showing-rod-shape-escherichia-coli-e-coli-bacteria_581734-82.jpg?w=360", "Characteristics: ", "Description: ", "Manifestations: ", "Laboratory Diagnosis: "),
#     Microorganism("Candida albicans", "https://www.researchgate.net/profile/Anna-Biedunkiewicz/publication/284139043/figure/fig2/AS:391460177367042@1470342787093/Candida-krusei-microculture-on-the-Nickerson-agar_Q320.jpg", "Characteristics: ", "Description: ", "Manifestations: ", "Laboratory Diagnosis: "),    
#     Microorganism("Mycobacterium tuberculosis", "https://histopath.files.wordpress.com/2014/04/afb.jpg", "Characteristics: ", "Description: ", "Manifestations: ", "Laboratory Diagnosis: "), 
#     Microorganism("Treponema pallidum", "https://cwoer.ccbcmd.edu/science/microbiology/Lab%20Manual/lab1/images/Tpallidum03_scale.jpg", "Characteristics: ", "Description: ", "Manifestations: ", "Laboratory Diagnosis: "),            
# ]

class MicroorganismCreate(CreateView):
    model = Microorganism
    fields = ['name', 'img', 'characteristics', 'description', 'manifestation', 'laboratory_diagnosis', 'verified_microorganism']
    template_name = "microorganism_create.html"
    success_url = "/microorganisms/"

class MicroorganismIndex(TemplateView):
    template_name = "microorganism_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # This is essentially a query built into Django that's saying SELECT * FROM main_app_microorganism
        # self.request.GET is a dictionary just like in express we have req.query
        # print(self.request.GET)
        name = self.request.GET.get('name')
        if name != None:
            # This is essentially a regex matcher that's built in for us.
            context["microorganisms"] = Microorganism.objects.filter(name__icontains=name)
        else:
            context["microorganisms"] = Microorganism.objects.all()
        return context
    
class MicroorganismDetail(DetailView):
    model = Microorganism
    template_name = "microorganism_detail.html"

class MicroorganismUpdate(UpdateView):
    model = Microorganism
    fields = ['name', 'img', 'characteristics', 'description', 'manifestation', 'laboratory_diagnosis', 'verified_microorganism']
    template_name = "microorganism_update.html"
    success_url = "/microorganisms/"

class MicroorganismDelete(DeleteView):
    model = Microorganism
    template_name = "microorganism_delete_confirmation.html"
    success_url = "/microorganisms/"