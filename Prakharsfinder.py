print("hello welcome to Prakhars finder")
print("Im here at youre sevrice and im here to help you find yourself")
districts = {
    1: {
        "counties": ["Atlantic", "Cape May", "Cumberland"],
        "municipalities": [
            "Avalon", "Bridgeton", "Cape May", "Cape May Point", "Commercial", "Corbin City", "Dennis", "Downe", 
            "Estell Manor", "Fairfield (Cumberland)", "Lawrence (Cumberland)", "Lower", "Maurice River", "Middle", 
            "Millville", "North Wildwood", "Ocean City", "Sea Isle City", "Stone Harbor", "Upper", "Vineland", 
            "West Cape May", "West Wildwood", "Weymouth", "Wildwood", "Wildwood Crest", "Woodbine"
        ]
    },
    2: {
        "counties": ["Atlantic"],
        "municipalities": [
            "Absecon", "Atlantic City", "Brigantine", "Egg Harbor Township", "Galloway", "Hamilton (Atlantic)", 
            "Linwood", "Longport", "Margate City", "Northfield", "Pleasantville", "Port Republic", "Somers Point", "Ventnor City"
        ]
    },
    3: {
        "counties": ["Cumberland", "Gloucester", "Salem"],
        "municipalities": [
            "Alloway", "Carneys Point", "Clayton", "Deerfield", "East Greenwich", "Elk", "Elmer", "Elsinboro", 
            "Glassboro", "Greenwich (Cumberland)", "Greenwich (Gloucester)", "Harrison (Gloucester)", "Hopewell (Cumberland)", 
            "Logan", "Lower Alloways Creek", "Mannington", "Mantua", "National Park", "Oldmans", "Paulsboro", "Penns Grove", 
            "Pennsville", "Pilesgrove", "Pitman", "Pittsgrove", "Quinton", "Salem", "Shiloh", "South Harrison", "Stow Creek", 
            "Swedesboro", "Upper Deerfield", "Upper Pittsgrove", "Wenonah", "West Deptford", "Westville", "Woodstown", "Woolwich"
        ]
    },
    4: {
        "counties": ["Atlantic", "Camden", "Gloucester"],
        "municipalities": ["Buena", "Buena Vista", "Chesilhurst", "Franklin (Gloucester)", "Gloucester Township", "Monroe (Gloucester)", "Newfield", "Washington (Gloucester)", "Waterford", "Winslow"]
    },
    5: {
        "counties": ["Camden", "Gloucester"],
        "municipalities": ["Audubon", "Barrington", "Bellmawr", "Brooklawn", "Camden", "Collingswood", "Deptford", "Gloucester City", "Haddon Heights", "Merchantville", "Mount Ephraim", "Pennsauken", "Runnemede", "Woodbury", "Woodbury Heights", "Woodlynne"]
    }}
choice = input("do you want to use a county or munucipality? ")
if choice == "municipality":
    search_municipality = input("enter the name of your municipality, make sure to capatilize the first letter ")

    for district, details in districts.items():
        if search_municipality in details["municipalities"]:
            print(f"{search_municipality} is in District {district}.")
            break
else:
    search_county = input("whats the name of your county? and make sure the first letter of your county is capitalized ")

    for district, details in districts.items():
        if search_county in details["counties"]:
            print(f"{search_county} County is in District {district}.")
            break  

shelter_links ={

"Atlantic City": "https://acrescuemission.org/",
    "Family Promise CMC": "https://familypromisecmc.org/",
    "Cumberland": "https://www.cumberlandcountynj.gov/filestorage/22641/22643/22917/22937/Homeless_Referral_Flow_Chart_Family_2024.pdf",
    "Avalon": "https://www.homelessshelterdirectory.org/city/nj-avalon",
    "Bridgeton": "https://homelesssolutions.org/",
    "Cape May Point": "https://www.capeatlanticresourcenet.org/search/family-promise-of-cape-may-county/#:~:text=(609)%20846%2D7862&text=Family%20Promise%20of%20Cape%20May%20County%20is%20a%20program%20designed,only%20accepts%20families%20with%20children.",
    "Commercial": "https://www.homelessshelterdirectory.org/city/nj-commercial_township",
    "Cumberland Family Shelter": "https://cumberlandfamilyshelter.com/about/",
    "Dennis Township": "https://www.homelessshelterdirectory.org/city/nj-dennis_township",
    "Estell Manor": "https://www.findhelp.org/housing/temporary-shelter--estell-manor-nj?postal=08319&cursor=10&limit=10",
    "Fairfield": "https://www.findhelp.org/housing/temporary-shelter--fairfield-nj",
    "Lawrenceville": "https://www.findhelp.org/housing/temporary-shelter--lawrence-township-nj",
    "Lower": "https://www.homelessshelterdirectory.org/city/nj-lower_township",
    "Maurice River": "https://www.homelessshelterdirectory.org/city/nj-maurice_river_township",
    "Middle Township": "https://www.homelessshelterdirectory.org/city/nj-middle_township",
    "Millville": "https://www.findhelp.org/housing/temporary-shelter--millville-nj",
    "North Wildwood": "https://www.findhelp.org/housing/temporary-shelter--wildwood-nj",
    "Ocean City": "https://www.findhelp.org/housing/temporary-shelter--ocean-city-nj",
    "Sea Isle City": "https://www.homelessshelterdirectory.org/city/nj-sea_isle_city",
    "Stone Harbor": "https://www.homelessshelterdirectory.org/city/nj-stone_harbor",
    "Vineland": "https://www.findhelp.org/housing/temporary-shelter--vineland-nj",
    "West Cape May": "https://www.findhelp.org/housing/temporary-shelter--cape-may-nj",
    "West Wildwood": "https://www.findhelp.org/housing/temporary-shelter--wildwood-nj",
    "Weymouth": "https://www.homelessshelterdirectory.org/city/nj-weymouth_township",
    "Wildwood Crest": "https://www.theextendedhandministry.org/about_us",
    "Woodbine": "https://www.findhelp.org/housing/temporary-shelter--woodbine-nj",
    "Absecon": "https://www.findhelp.org/housing/temporary-shelter--absecon-nj",
    "Brigantine": "https://www.findhelp.org/housing/temporary-shelter--brigantine-nj",
    "Egg Harbor Township": "https://www.findhelp.org/housing/temporary-shelter--egg-harbor-township-nj",
    "Galloway Township": "https://www.homelessshelterdirectory.org/city/nj-galloway_township",
    "Hamilton": "https://www.homelessshelterdirectory.org/city/nj-hamilton_township",
    "Linwood": "https://www.shelterlist.com/city/nj-linwood",
    "Longport": "https://www.homelessshelterdirectory.org/city/nj-longport"
}
place = input("Please enter the name of the place you're searching for a homeless shelter link (e.g., Atlantic City): ")

# Check if the place exists in the dictionary
if place in shelter_links:
    print(f"The homeless shelter link for {place} is: {shelter_links[place]},if you need any help or need someone to talk to please call 988")
else:
    print(f"Sorry, we don't have a shelter link for {place}. Please try another location.")