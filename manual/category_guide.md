# How measures are sorted into categories

Every measure in `categories.csv` was placed by reading its full text (heading and everything under it; for a measure that
appears only in a cost table, the table's one-line description). The rules below are applied in order, and the reason for
each decision is in the file's `reason` column.

## Rules, in order

1. **Indigenous first.** A measure aimed only at First Nations, Inuit or Métis goes to Indigenous, whatever it is about
   (housing, water, health, policing, languages, claims, business).
2. **What it is for, not how it is delivered.** A tax cut, credit, rebate, loan, grant or regulation goes where its purpose
   is: the GST break for first-time buyers to Housing, research tax credits to Research, the clean-technology investment
   tax credits to Clean energy & climate, the Productivity Super-Deduction (2025) and Mega Deduction (2026) to Trade,
   industry & competitiveness, the Middle-Class Tax Cut to Affordability & social support.
3. **Taxation and Government hold only the tax system and the running of government**, and the money they raise or save
   (tax fairness and anti-avoidance, tax administration, spending reviews, the public service).
4. **Other only when nothing fits** (mainly foreign aid).

A measure that reverses an earlier policy is flagged in the `reverses` column with the category of the policy it undoes
(the consumer carbon price cancellation, 2025: filed under Affordability & social support, reverses Clean energy & climate).

## What each category holds

| Category | Holds |
|---|---|
| Housing | Building and financing homes, rental and co-op housing, home buyers (savings accounts, GST relief, mortgage rules), homelessness, infrastructure built to enable housing, federal land for homes |
| Affordability & social support | Income support and benefits for households (children, seniors, disability, low-wage workers), cost-of-living relief (rebates, broad household tax cuts, fuel tax relief), consumer prices and fees (junk fees, bank fees, groceries), child care, school food and food security |
| Health care | Health systems and transfers, long-term and home care, mental health, dental care, pharmacare, public health and pandemic health measures, substance use, the health workforce, health-motivated taxes (tobacco, vaping) |
| Trade, industry & competitiveness | Business support and small business, sectors (agriculture, fisheries, forestry, tourism, autos, steel), trade policy and export support, responses to tariffs, competition policy, the financial system and capital markets, critical minerals and mining, regional development, business investment incentives, major-project approvals, pandemic support for businesses |
| Jobs, skills & immigration | Training, apprenticeships and trades, students (grants and loans), youth employment, Employment Insurance and pandemic income support for workers, the wage subsidy, workers' rights and labour standards, foreign credentials, immigration levels and programs, the asylum system, settlement, citizenship |
| Infrastructure | Public transit, roads, bridges, rail, airports, ferries, broadband and mobile coverage, water and wastewater, municipal infrastructure funds, the Canada Infrastructure Bank |
| Research, AI & technology | Research funding and the granting councils, science facilities, AI, quantum, genomics, space, innovation programs, research tax credits, intellectual property, the digital economy |
| Culture & communities | Arts, heritage, museums, festivals, media and journalism, CBC/Radio-Canada, film and music, official languages, sport, community centres, equality and inclusion (gender, 2SLGBTQI+, anti-racism, Black Canadians, antisemitism and Islamophobia), gender-based violence programs, accessibility, charities and non-profits |
| Nature & environment | Parks and protected areas, oceans and coasts, fresh water, species at risk, plastics and waste, chemicals and pollution, the weather service, nature-based climate solutions |
| Clean energy & climate | Clean electricity and nuclear power, hydrogen, carbon capture, clean-technology tax credits, electric vehicles and charging, cutting emissions, carbon pricing, energy-efficiency retrofits, climate adaptation, sustainable finance |
| Taxation | Tax fairness and anti-avoidance, corporate and international tax (global minimum tax, digital services tax), capital gains and minimum tax, excise duties with no other purpose, tax administration and compliance, GST/HST technical changes |
| Government | The public service, spending reviews and savings, government operations, procurement and property, service delivery and digital government, statistics and the census, Parliament and democratic institutions, Crown corporations such as Canada Post |
| Defence & security | The armed forces and their equipment, NATO and NORAD, military aid (including to Ukraine), veterans, intelligence and cyber security, foreign interference, border security, policing, firearms, organized and financial crime, courts, legal aid and corrections, emergency management and disasters, the Coast Guard, Arctic sovereignty |
| Indigenous | Anything aimed only at First Nations, Inuit or Métis |
| Other | Foreign aid and development, humanitarian assistance (including to Ukraine), international financial institutions, and anything else that fits nowhere |
