from drafter import *
from dataclasses import dataclass


set_website_title("Where in the Bay?")
set_site_information(
    author="Linnea Hain",
    description="Find the location of your sample!",
    sources="https://eyesonthebay.dnr.maryland.gov/",
    planning=["plan.pdf", "design.pdf"],
    links=["https://github.com/your-username/your-repository"]
)
hide_debug_information()
set_website_framed(False)

@dataclass
class State:
    temperature: str
    pH: str
    salinity: str

@dataclass
class Location:
    name: str
    temperature: float
    pH: float
    salinity: float

all_locations = [Location("Still Pond", 37.90, 7.80, 3.00),
                Location("Turkey Point", 38.10, 8.20, 0.20),
                Location("Swan Point", 38.50, 8.00, 11.40),
                Location("Bay Bridge(N)", 39.00, 8.20, 13.20),
                Location("Kent Point(SW)", 39.20, 8.20, 15.10),
                Location("MD Mid Bay", 39.20, 8.20, 16.40),
                Location("Choptank River", 39.60, 8.20, 17.50),
                Location("Cove Point", 40.30, 8.30, 16.80),
                Location("Point No Point", 40.50, 8.20, 19.30),
                Location("Smith Point", 41.00, 8.20, 19.80) 
                 ]

@route
def index(state: State)-> Page:
    return Page(state, [
                        Header("Where in the Bay?"),
                        LineBreak(),
                        
                        Text("Where in the bay is your sample from?"),
                        LineBreak(),
                        Text("Input your information below regarding a sample from January of 2026 to generate possible locations!"),
                        LineBreak(),
                        LineBreak(),
                        
                        Text("Enter Temperature in Farhenheit"),
                        TextBox("temperature"),
                        LineBreak(),
                        
                        Text("Enter pH"),
                        TextBox("pH"),
                        LineBreak(),
                        
                        Text("Enter Salinity in ppt"),
                        TextBox("salinity"),
                        LineBreak(),
                    
                        Button("Submit", submit)
                        
                        ])
@route
def submit(state: State)-> Page:

    return Page(state, [
                        Text("All values:"),
                        LineBreak(),
                        
                        Text("Temperature:"+ state.temperature),
                        LineBreak(),
                        
                        Text("pH:" + state.pH),
                        LineBreak(),
                        
                        Text("Salinity:" + state.salinity),
                        LineBreak()
                        
                        ])
@route
def submit(state: State, temperature: str, pH: str, salinity: str) -> Page:

    temperature = float(temperature)
    pH = float(pH)
    salinity = float(salinity)

    matches = []

    for location in all_locations:
        if (abs(location.temperature - temperature) <= 2 and
            abs(location.pH - pH) <= 0.2 and
            abs(location.salinity - salinity) <= 3):

            matches.append(location.name)

    if len(matches) > 0:
        return Page(state, [
            Header("Possible Matches"),
            Text(", ".join(matches))
        ])
    else:
        return Page(state, [
            Text("No matching locations found.")
        ])

start_server(State("","",""))
                        

