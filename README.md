# Am I Even Allowed to Fly This Thing?
### Transport Canada Drone Regulatory Compliance Analysis

I have been studying for my Transport Canada drone pilot certificate. The further I got into it the more I realized the rules are actually pretty complex. It is not just where you can fly. There are weight limits, certification levels, airspace categories, distance rules from people, and a whole separate set of rules if you want to fly beyond what you can see. I started mapping it all out to make sense of it. That turned into a full compliance analysis across three different types of drone operators.

---

## What this is

A regulatory affairs and compliance analysis project covering Transport Canada's drone regulations under the Canadian Aviation Regulations Part IX. Fifteen requirements mapped. Three realistic Canadian operator profiles assessed. Nine compliance gaps identified with risk ratings, penalty exposure, and plain English remediation steps for each one. An interactive Streamlit compliance checker that any drone operator can use to assess their own situation.

---

## Live app

[Launch the Compliance Checker and Analysis Dashboard](your-streamlit-link-here)

---

## What the analysis found

The three operator profiles tell three different stories.

The Weekend Hobbyist has four immediate compliance gaps. Unregistered drone. No pilot certificate. Occasionally flies near Billy Bishop Airport without checking airspace. Sometimes flies at dusk without proper lighting. Maximum combined penalty exposure across those gaps is $34,000.

The Commercial Photography Business looks compliant at first glance. Registered, insured, and has a certificate. But they hold only a Basic certificate and regularly work within 30 metres of bystanders at construction sites. Commercial operations near people require an Advanced certificate. Every job they take at a busy site is a compliance violation they do not know they are committing.

The Drone Delivery Operator is the most serious case. Registered, Advanced certified, properly insured. But delivery routes require the drone to travel beyond the pilot's visual line of sight and they are doing this without a Special Flight Operations Certificate. This is illegal under CAR 901.70 and creates potential criminal liability in the event of any incident during delivery operations.

| Profile | Gaps | Immediate | Critical Risks | Max Penalty |
|---------|------|-----------|---------------|------------|
| Weekend Hobbyist | 4 | 4 | 1 | $34,000 |
| Commercial Photography | 2 | 2 | 0 | $10,000 |
| Drone Delivery Operator | 3 | 2 | 2 | $50,000 |

---

## What the five tabs cover

The Compliance Overview tab shows the full picture across all three profiles — gaps by urgency, risk rating distribution, and requirements broken down by category.

The Operator Profiles tab lets you select any of the three profiles and see every compliance gap for that operator with the remediation step for each one.

The Risk Register tab shows the full risk matrix with likelihood and consequence scores, risk ratings, and the recommended action for each risk.

The Regulatory Changes tab walks through every significant Transport Canada drone rule update since 2019 including the 2024 increase in enforcement activity.

The Compliance Checker tab is an interactive tool where any drone operator can answer six questions about their drone and how they fly it and get back an instant plain English compliance assessment.

---

## Files in this repo

| File | What it is |
|------|-----------|
| app.py | Streamlit compliance checker and analysis dashboard |
| regulatory-requirements.csv | 15 Transport Canada requirements with regulatory references and penalties |
| operator-profiles.csv | Three operator profiles with registration, certification, and operating details |
| compliance-gaps.csv | 9 compliance gaps with descriptions, urgency ratings, and remediation steps |
| risk-register.csv | Risk register with likelihood, consequence, and risk ratings for all gaps |
| regulatory-change-log.csv | 6 Transport Canada regulatory updates tracked since 2019 |
| key-findings.json | Summary statistics and headline findings |
| compliance-report.pdf | Full regulatory compliance assessment report |
| generate-data.py | Python script that built all the structured data files |
| requirements.txt | Package dependencies |

---

## Skills this project demonstrates

Regulatory requirement mapping and interpretation. Compliance gap analysis across multiple operator profiles. Risk register development with likelihood and consequence scoring. Regulatory change tracking and impact assessment. Plain English communication of complex regulatory obligations. Interactive compliance tool design. Regulatory affairs knowledge in the Canadian transport and aviation context.

---

## About this project

Part of a portfolio series built while job searching in Canada after graduating from the University of Waterloo.

Prepared by Simran Saran. Targeting regulatory affairs, compliance, and business analyst roles in transport, aerospace, and logistics across Canada.

All regulatory references are based on Transport Canada Canadian Aviation Regulations Part IX as published at tc.canada.ca. Rules change regularly. Always verify current requirements directly with Transport Canada.
