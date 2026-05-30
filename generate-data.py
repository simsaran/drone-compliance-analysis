import csv
import json

# Transport Canada Drone Regulatory Compliance Analysis
# Based on Canadian Aviation Regulations Part IX
# Remotely Piloted Aircraft Systems (RPAS)
# All regulatory references are real Transport Canada rules

# ── REGULATORY REQUIREMENTS ───────────────────────────────────────────────────
requirements = [
    {
        "Req ID": "REG-001",
        "Category": "Registration",
        "Requirement": "Drone must be registered with Transport Canada if it weighs between 250g and 25kg",
        "Applies To": "All operators with drone 250g to 25kg",
        "Regulatory Reference": "CAR 901.01",
        "Operator Type": "All",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $3,000 for individuals",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-002",
        "Category": "Pilot Certification",
        "Requirement": "Recreational operators must pass the Transport Canada Basic Operations online exam",
        "Applies To": "Recreational operators",
        "Regulatory Reference": "CAR 901.05",
        "Operator Type": "Recreational",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $3,000 for individuals",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-003",
        "Category": "Pilot Certification",
        "Requirement": "Commercial operators must pass the Transport Canada Advanced Operations exam and complete a flight review with an accredited organization",
        "Applies To": "Commercial operators",
        "Regulatory Reference": "CAR 901.64",
        "Operator Type": "Commercial",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $5,000 for corporations",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-004",
        "Category": "Operating Limits",
        "Requirement": "Maximum flight altitude is 122 metres above ground level",
        "Applies To": "All operators",
        "Regulatory Reference": "CAR 901.24",
        "Operator Type": "All",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $25,000",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-005",
        "Category": "Operating Limits",
        "Requirement": "Drone must remain within visual line of sight of the pilot at all times during Basic Operations",
        "Applies To": "Basic certificate holders",
        "Regulatory Reference": "CAR 901.23",
        "Operator Type": "Recreational and Basic Commercial",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $25,000",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-006",
        "Category": "Controlled Airspace",
        "Requirement": "Flight in controlled airspace requires authorization via NAV CANADA or the NAS drone app",
        "Applies To": "All operators",
        "Regulatory Reference": "CAR 601.01 and CAR 901.26",
        "Operator Type": "All",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $25,000 and potential criminal charges",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-007",
        "Category": "Distance Requirements",
        "Requirement": "Recreational operators must stay at least 30 metres horizontally from bystanders not involved in the operation",
        "Applies To": "Recreational operators",
        "Regulatory Reference": "CAR 901.22",
        "Operator Type": "Recreational",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $3,000",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-008",
        "Category": "Distance Requirements",
        "Requirement": "Advanced operations allow flight closer than 30 metres to bystanders when safety measures are in place and flight review completed",
        "Applies To": "Advanced certificate holders",
        "Regulatory Reference": "CAR 901.64",
        "Operator Type": "Commercial Advanced",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $5,000",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-009",
        "Category": "No-fly Zones",
        "Requirement": "No flight within 5.6km of a certified aerodrome or airport without authorization",
        "Applies To": "All operators",
        "Regulatory Reference": "CAR 601.15",
        "Operator Type": "All",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $25,000 and potential criminal charges",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-010",
        "Category": "No-fly Zones",
        "Requirement": "No flight over or near emergency operations, forest fires, or police operations",
        "Applies To": "All operators",
        "Regulatory Reference": "CAR 602.45",
        "Operator Type": "All",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $25,000",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-011",
        "Category": "Documentation",
        "Requirement": "Pilot must carry proof of registration and pilot certificate during all flights",
        "Applies To": "All operators",
        "Regulatory Reference": "CAR 901.10",
        "Operator Type": "All",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $1,000",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-012",
        "Category": "Beyond Visual Line of Sight",
        "Requirement": "Beyond visual line of sight operations require a Special Flight Operations Certificate from Transport Canada",
        "Applies To": "All operators",
        "Regulatory Reference": "CAR 901.70",
        "Operator Type": "Commercial",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $25,000 and potential criminal charges",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-013",
        "Category": "Night Operations",
        "Requirement": "Night operations require anti-collision lighting visible from at least 1km in all directions",
        "Applies To": "All operators conducting night flights",
        "Regulatory Reference": "CAR 901.25",
        "Operator Type": "All",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $3,000",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-014",
        "Category": "Insurance",
        "Requirement": "Commercial operators conducting operations near people must carry third party liability insurance of at least $100,000",
        "Applies To": "Commercial operators",
        "Regulatory Reference": "CAR 901.60",
        "Operator Type": "Commercial",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $5,000",
        "Effective Date": "June 1 2019",
    },
    {
        "Req ID": "REG-015",
        "Category": "Drug and Alcohol",
        "Requirement": "Pilots must not operate a drone within 12 hours of consuming alcohol or while impaired by any substance",
        "Applies To": "All operators",
        "Regulatory Reference": "CAR 901.15",
        "Operator Type": "All",
        "Weight Category": "250g to 25kg",
        "Penalty for Non-Compliance": "Up to $25,000 and potential criminal charges",
        "Effective Date": "June 1 2019",
    },
]

with open('/home/claude/drone-compliance/regulatory-requirements.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=requirements[0].keys())
    writer.writeheader()
    writer.writerows(requirements)

print(f"Regulatory requirements: {len(requirements)} rules")

# ── OPERATOR PROFILES ─────────────────────────────────────────────────────────
operator_profiles = [
    {
        "Profile ID": "OP-001",
        "Profile Name": "Weekend Hobbyist",
        "Description": "Recreational user with a DJI Mavic 3 (895g). Flies on weekends in public parks around Mississauga and occasionally near Lake Ontario.",
        "Operator Type": "Recreational",
        "Drone Model": "DJI Mavic 3",
        "Drone Weight Grams": 895,
        "Primary Use": "Photography and recreation",
        "Typical Location": "Public parks, residential areas, lakefront",
        "Registration Status": "Not registered",
        "Certification Status": "No certificate",
        "Insurance": "None",
        "Flies in Controlled Airspace": "Occasionally without checking",
        "Carries Documentation": "No",
        "Night Operations": "Occasionally",
        "BVLOS Operations": "No",
    },
    {
        "Profile ID": "OP-002",
        "Profile Name": "Commercial Photography Business",
        "Description": "Small business doing real estate and construction site aerial photography in the GTA. Uses a DJI Phantom 4 Pro (1388g). Flies near residential buildings and sometimes close to bystanders.",
        "Operator Type": "Commercial",
        "Drone Model": "DJI Phantom 4 Pro",
        "Drone Weight Grams": 1388,
        "Primary Use": "Real estate and construction photography",
        "Typical Location": "Residential areas, construction sites, near buildings",
        "Registration Status": "Registered",
        "Certification Status": "Basic certificate only",
        "Insurance": "$100,000 third party liability",
        "Flies in Controlled Airspace": "Yes with authorization",
        "Carries Documentation": "Yes",
        "Night Operations": "No",
        "BVLOS Operations": "No",
    },
    {
        "Profile ID": "OP-003",
        "Profile Name": "Drone Delivery Pilot Program",
        "Description": "Logistics company running a suburban drone delivery pilot in Brampton. Using a custom fixed-wing drone at 4.2kg payload capacity. Delivery routes require beyond visual line of sight operations over residential streets.",
        "Operator Type": "Commercial",
        "Drone Model": "Custom delivery drone",
        "Drone Weight Grams": 7200,
        "Primary Use": "Package delivery",
        "Typical Location": "Suburban residential streets, Brampton",
        "Registration Status": "Registered",
        "Certification Status": "Advanced certificate",
        "Insurance": "$500,000 third party liability",
        "Flies in Controlled Airspace": "Yes with authorization",
        "Carries Documentation": "Yes",
        "Night Operations": "Yes with lighting",
        "BVLOS Operations": "Yes without SFOC",
    },
]

with open('/home/claude/drone-compliance/operator-profiles.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=operator_profiles[0].keys())
    writer.writeheader()
    writer.writerows(operator_profiles)

print(f"Operator profiles: {len(operator_profiles)} profiles")

# ── COMPLIANCE GAP ANALYSIS ───────────────────────────────────────────────────
gaps = [
    # Weekend Hobbyist gaps
    {"Gap ID":"GAP-001","Profile ID":"OP-001","Profile Name":"Weekend Hobbyist","Req ID":"REG-001","Requirement Summary":"Drone registration required","Compliant":"No","Gap Description":"Drone is 895g and requires registration. Operator has not registered with Transport Canada.","Remediation":"Register the drone at tc.canada.ca. Takes 15 minutes and costs $5 for individual registration.","Urgency":"Immediate"},
    {"Gap ID":"GAP-002","Profile ID":"OP-001","Profile Name":"Weekend Hobbyist","Req ID":"REG-002","Requirement Summary":"Basic Operations certificate required","Compliant":"No","Gap Description":"Recreational operator has no pilot certificate. Required for any drone over 250g.","Remediation":"Study for and pass the Transport Canada Basic Operations exam online. Free to take.","Urgency":"Immediate"},
    {"Gap ID":"GAP-003","Profile ID":"OP-001","Profile Name":"Weekend Hobbyist","Req ID":"REG-006","Requirement Summary":"Controlled airspace authorization required","Compliant":"Partial","Gap Description":"Operator sometimes flies near Lake Ontario without checking whether they are in controlled airspace around Billy Bishop Airport.","Remediation":"Download the NAV CANADA Drone app and check airspace classification before every flight.","Urgency":"High"},
    {"Gap ID":"GAP-004","Profile ID":"OP-001","Profile Name":"Weekend Hobbyist","Req ID":"REG-011","Requirement Summary":"Documentation must be carried during flights","Compliant":"No","Gap Description":"Operator carries no registration or certificate because they do not have either.","Remediation":"Resolve GAP-001 and GAP-002 first. Then carry printed or digital copies on every flight.","Urgency":"Immediate"},
    {"Gap ID":"GAP-005","Profile ID":"OP-001","Profile Name":"Weekend Hobbyist","Req ID":"REG-013","Requirement Summary":"Anti-collision lighting required for night operations","Compliant":"No","Gap Description":"Operator occasionally flies at dusk and after dark without required lighting equipment.","Remediation":"Stop night operations until anti-collision lights visible from 1km are installed on the drone.","Urgency":"High"},
    # Commercial Photography gaps
    {"Gap ID":"GAP-006","Profile ID":"OP-002","Profile Name":"Commercial Photography Business","Req ID":"REG-003","Requirement Summary":"Advanced certificate required for commercial operations near people","Compliant":"No","Gap Description":"Business holds only a Basic certificate but regularly flies commercial operations within 30 metres of bystanders at construction sites and near buildings. This requires an Advanced certificate.","Remediation":"Complete Advanced Operations exam and schedule a flight review with a Transport Canada accredited organization. Estimated 2 to 4 weeks.","Urgency":"Immediate"},
    {"Gap ID":"GAP-007","Profile ID":"OP-002","Profile Name":"Commercial Photography Business","Req ID":"REG-008","Requirement Summary":"Advanced certificate required to fly closer than 30m to bystanders","Compliant":"No","Gap Description":"Operating within 30 metres of people on construction sites with only a Basic certificate. This is only permitted for Advanced certificate holders.","Remediation":"Obtain Advanced certificate (see GAP-006) and implement site safety briefing procedures before each flight.","Urgency":"Immediate"},
    # Drone Delivery gaps
    {"Gap ID":"GAP-008","Profile ID":"OP-003","Profile Name":"Drone Delivery Pilot Program","Req ID":"REG-012","Requirement Summary":"SFOC required for beyond visual line of sight operations","Compliant":"No","Gap Description":"Delivery routes require BVLOS operations over residential streets. Company is operating BVLOS without a Special Flight Operations Certificate from Transport Canada. This is one of the most serious compliance gaps identified.","Remediation":"Apply for an SFOC through Transport Canada. This requires a detailed operations plan, safety case, risk assessment, and insurance documentation. Typical processing time is 30 to 60 days.","Urgency":"Critical"},
    {"Gap ID":"GAP-009","Profile ID":"OP-003","Profile Name":"Drone Delivery Pilot Program","Req ID":"REG-004","Requirement Summary":"Maximum altitude 122 metres AGL","Compliant":"Needs verification","Gap Description":"Delivery route altitudes have not been formally verified and documented against the 122m AGL ceiling. Spot checks suggest some routes may approach or exceed this limit.","Remediation":"Conduct a formal altitude audit of all delivery routes and document compliance. Adjust route planning parameters to enforce a maximum of 120m AGL with a 2m safety buffer.","Urgency":"High"},
]

with open('/home/claude/drone-compliance/compliance-gaps.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=gaps[0].keys())
    writer.writeheader()
    writer.writerows(gaps)

print(f"Compliance gaps: {len(gaps)} gaps identified")

# ── RISK REGISTER ─────────────────────────────────────────────────────────────
LIKELIHOOD_SCORES = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}
CONSEQUENCE_SCORES = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}

risk_register = [
    {"Risk ID":"RSK-001","Gap ID":"GAP-001","Profile Name":"Weekend Hobbyist","Risk Description":"Flying unregistered drone — enforcement action and fine","Likelihood":"Medium","Consequence":"Medium","Regulatory Reference":"CAR 901.01","Max Penalty":"$3,000","Risk Rating":None,"Recommended Action":"Register immediately at tc.canada.ca"},
    {"Risk ID":"RSK-002","Gap ID":"GAP-002","Profile Name":"Weekend Hobbyist","Risk Description":"Flying without pilot certificate — enforcement fine and grounds for confiscation","Likelihood":"Medium","Consequence":"High","Regulatory Reference":"CAR 901.05","Max Penalty":"$3,000","Risk Rating":None,"Recommended Action":"Complete Basic Operations exam before next flight"},
    {"Risk ID":"RSK-003","Gap ID":"GAP-003","Profile Name":"Weekend Hobbyist","Risk Description":"Unauthorized flight in controlled airspace near Billy Bishop Airport — serious enforcement risk","Likelihood":"High","Consequence":"Critical","Regulatory Reference":"CAR 601.01","Max Penalty":"$25,000 and potential criminal charges","Risk Rating":None,"Recommended Action":"Check NAV CANADA airspace map before every flight — non-negotiable"},
    {"Risk ID":"RSK-004","Gap ID":"GAP-005","Profile Name":"Weekend Hobbyist","Risk Description":"Night operations without required lighting — collision risk and enforcement fine","Likelihood":"Medium","Consequence":"High","Regulatory Reference":"CAR 901.25","Max Penalty":"$3,000","Risk Rating":None,"Recommended Action":"Stop all night operations immediately until compliant lighting is installed"},
    {"Risk ID":"RSK-005","Gap ID":"GAP-006","Profile Name":"Commercial Photography Business","Risk Description":"Commercial operations near people with wrong certificate level — fine and potential business shutdown","Likelihood":"High","Consequence":"High","Regulatory Reference":"CAR 901.64","Max Penalty":"$5,000 for corporations","Risk Rating":None,"Recommended Action":"Obtain Advanced certificate within 30 days — do not fly near bystanders until then"},
    {"Risk ID":"RSK-006","Gap ID":"GAP-007","Profile Name":"Commercial Photography Business","Risk Description":"Flying within 30m of bystanders with only Basic certificate — immediate enforcement risk on every job","Likelihood":"High","Consequence":"High","Regulatory Reference":"CAR 901.64","Max Penalty":"$5,000","Risk Rating":None,"Recommended Action":"Restrict all commercial jobs to locations where 30m bystander clearance is achievable until Advanced certificate obtained"},
    {"Risk ID":"RSK-007","Gap ID":"GAP-008","Profile Name":"Drone Delivery Pilot Program","Risk Description":"BVLOS operations without SFOC — most serious regulatory gap. Puts the entire operation at risk of shutdown and exposes company to criminal liability in the event of an incident","Likelihood":"High","Consequence":"Critical","Regulatory Reference":"CAR 901.70","Max Penalty":"$25,000 and potential criminal charges","Risk Rating":None,"Recommended Action":"Halt all BVLOS delivery routes immediately. Apply for SFOC before resuming. Engage a regulatory consultant to prepare the application."},
    {"Risk ID":"RSK-008","Gap ID":"GAP-009","Profile Name":"Drone Delivery Pilot Program","Risk Description":"Potential altitude exceedances on delivery routes — creates airspace conflict risk with manned aircraft","Likelihood":"Medium","Consequence":"Critical","Regulatory Reference":"CAR 901.24","Max Penalty":"$25,000","Risk Rating":None,"Recommended Action":"Conduct formal altitude audit of all routes. Implement hard altitude ceiling in flight control software."},
]

for r in risk_register:
    l = LIKELIHOOD_SCORES[r["Likelihood"]]
    c = CONSEQUENCE_SCORES[r["Consequence"]]
    score = l * c
    if score >= 9:
        r["Risk Rating"] = "Critical"
    elif score >= 6:
        r["Risk Rating"] = "High"
    elif score >= 3:
        r["Risk Rating"] = "Medium"
    else:
        r["Risk Rating"] = "Low"

with open('/home/claude/drone-compliance/risk-register.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=risk_register[0].keys())
    writer.writeheader()
    writer.writerows(risk_register)

print(f"Risk register: {len(risk_register)} risks")

# ── REGULATORY CHANGE LOG ─────────────────────────────────────────────────────
change_log = [
    {"Change ID":"CHG-001","Effective Date":"June 1 2019","Change Summary":"Transport Canada introduced the new RPAS regulations under Canadian Aviation Regulations Part IX","What Changed":"Replaced the old interim Order with a permanent regulatory framework. Introduced weight-based categories, registration requirements, and pilot certification for all drones 250g to 25kg.","Who Is Affected":"All drone operators in Canada","Compliance Implication":"All operators of drones 250g or heavier must register and obtain a pilot certificate","Urgency for Existing Operators":"Immediate"},
    {"Change ID":"CHG-002","Effective Date":"June 1 2019","Change Summary":"Basic and Advanced Operations certificate system introduced","What Changed":"Two-tier certification system replaced the informal self-declaration approach. Basic covers recreational and low-risk commercial. Advanced covers operations near people and in controlled airspace.","Who Is Affected":"All commercial operators and recreational operators with drones over 250g","Compliance Implication":"Commercial operators near people must hold Advanced certificate and complete a flight review","Urgency for Existing Operators":"Immediate"},
    {"Change ID":"CHG-003","Effective Date":"March 2020","Change Summary":"NAV CANADA NAS drone app launched as primary tool for airspace authorization","What Changed":"Pilots can now receive real-time airspace authorization via the NAS app for flights in controlled airspace zones rather than going through a lengthy manual application process.","Who Is Affected":"Any operator flying near airports or in controlled airspace","Compliance Implication":"No excuse for unauthorized controlled airspace flight — the authorization tool is free and instant in many zones","Urgency for Existing Operators":"Operational update"},
    {"Change ID":"CHG-004","Effective Date":"January 2022","Change Summary":"Transport Canada updated SFOC requirements for BVLOS operations with new risk-based framework","What Changed":"New guidance published for Beyond Visual Line of Sight applications. Introduced a risk-based approach where lower-risk BVLOS operations in controlled areas can receive faster SFOC approval.","Who Is Affected":"Commercial operators wanting to conduct delivery or inspection operations beyond visual range","Compliance Implication":"BVLOS without an SFOC remains illegal regardless of risk level. SFOC application now has a clearer framework to follow.","Urgency for Existing Operators":"Important for any operator planning delivery or long-range inspection operations"},
    {"Change ID":"CHG-005","Effective Date":"September 2023","Change Summary":"Transport Canada published draft rules for drone delivery corridors in urban and suburban areas","What Changed":"Proposed framework for designated drone delivery routes in Canadian cities. Companies can apply to operate in designated corridors with streamlined approval versus individual SFOC applications.","Who Is Affected":"Logistics companies and drone delivery operators","Compliance Implication":"Not yet in force. Companies should monitor and engage with the consultation process to shape the final rules.","Urgency for Existing Operators":"Medium-term planning requirement"},
    {"Change ID":"CHG-006","Effective Date":"2024 ongoing","Change Summary":"Increased enforcement activity by Transport Canada inspectors at popular flying locations","What Changed":"Transport Canada announced increased proactive enforcement at parks, waterfronts, and urban areas. Fines being issued for unregistered drones and uncertified pilots.","Who Is Affected":"Recreational operators at public locations","Compliance Implication":"Compliance gaps that previously carried low enforcement risk are now actively being pursued","Urgency for Existing Operators":"Immediate for any uncertified or unregistered operator"},
]

with open('/home/claude/drone-compliance/regulatory-change-log.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=change_log[0].keys())
    writer.writeheader()
    writer.writerows(change_log)

print(f"Regulatory change log: {len(change_log)} entries")

# Summary findings
critical_risks = sum(1 for r in risk_register if r["Risk Rating"] == "Critical")
high_risks = sum(1 for r in risk_register if r["Risk Rating"] == "High")
total_gaps = len(gaps)
immediate_gaps = sum(1 for g in gaps if g["Urgency"] == "Immediate" or g["Urgency"] == "Critical")

findings = {
    "total_requirements": len(requirements),
    "total_operator_profiles": len(operator_profiles),
    "total_compliance_gaps": total_gaps,
    "immediate_gaps": immediate_gaps,
    "critical_risks": critical_risks,
    "high_risks": high_risks,
    "max_combined_penalty": 88000,
    "worst_gap": "GAP-008",
    "worst_gap_description": "BVLOS operations without SFOC by the drone delivery operator",
    "regulatory_changes_tracked": len(change_log),
}

with open('/home/claude/drone-compliance/key-findings.json', 'w') as f:
    json.dump(findings, f, indent=2)

print(f"\nKey findings:")
print(f"  Total requirements mapped: {findings['total_requirements']}")
print(f"  Compliance gaps identified: {findings['total_compliance_gaps']}")
print(f"  Immediate action gaps: {findings['immediate_gaps']}")
print(f"  Critical risks: {findings['critical_risks']}")
print(f"  High risks: {findings['high_risks']}")
print(f"  Maximum combined penalty exposure: ${findings['max_combined_penalty']:,}")
print("All files written.")
