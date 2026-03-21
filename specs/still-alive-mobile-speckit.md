# SPECKIT SPECIFICATION

## Feature
Add a mobile-style tips page for the Still Alive app and populate it with multiple safety articles.

## Goals
- Provide a mobile-first UI that matches the provided screenshots (header, chips, cards, FAB, bottom nav).
- Include multiple safety-related articles with brief summaries and external references.
- Link the new page from `still-alive.html` for discoverability.

## Non-Goals
- Build a CMS or dynamic backend.
- Implement authenticated user accounts.
- Replace existing Still Alive marketing content.

## User Stories
- As a visitor, I can browse a mobile-style safety tips feed that looks like an app screen.
- As a visitor, I can filter tips by category.
- As a visitor, I can open trusted resources for deeper reading.

## Functional Requirements
- Create `still-alive-mobile.html` with a responsive, mobile-style layout.
- Add category chips with filtering behavior (All, Preparedness, Check-In, Home Safety, Wellness, Science).
- Provide five tip cards per category (25 total), each with title, short summary, read time, and internal article links.
- Create dedicated article pages under `still-alive-tips/` with source references.
- Add a floating action button and fixed bottom navigation for visual parity.
- Add a new section and nav anchor in `still-alive.html` that links to the mobile page.
- Update `sitemap.xml` to include the new page and article pages.

## Content Requirements
Article list, internal pages, and references:
- Emergency Kit Essentials -> `still-alive-tips/01-emergency-kit-essentials.html` (https://www.ready.gov/kit)
- Personal Check-In Plan -> `still-alive-tips/02-personal-check-in-plan.html` (https://www.ready.gov/plan)
- Prevent Falls at Home -> `still-alive-tips/03-prevent-falls-at-home.html` (https://www.cdc.gov/falls/)
- Power Outage Readiness -> `still-alive-tips/04-power-outage-readiness.html` (https://www.ready.gov/power-outages)
- Home Fire Escape Basics -> `still-alive-tips/05-home-fire-escape-basics.html` (https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/fire.html)
- Emergency Prep for Older Adults -> `still-alive-tips/06-emergency-prep-older-adults.html` (https://www.nia.nih.gov/health/emergency-preparedness)
- Fall Risk Facts -> `still-alive-tips/07-fall-risk-facts.html` (https://www.who.int/news-room/fact-sheets/detail/falls)
- Evacuation Ready Checklist -> `still-alive-tips/08-evacuation-ready-checklist.html` (https://www.ready.gov/evacuation)
- Water Storage Basics -> `still-alive-tips/09-water-storage-basics.html` (https://www.ready.gov/water)
- Shelter-in-Place Planning -> `still-alive-tips/10-shelter-in-place-planning.html` (https://www.ready.gov/shelter)
- Build a Trusted Contacts List -> `still-alive-tips/11-trusted-contacts-list.html` (https://www.redcross.org/get-help/how-to-prepare-for-emergencies/make-a-plan.html)
- Missed Check-In Escalation Steps -> `still-alive-tips/12-missed-check-in-steps.html` (https://www.ready.gov/plan)
- Travel Check-In Routine -> `still-alive-tips/13-travel-check-in-routine.html` (https://travel.state.gov/content/travel/en/international-travel/before-you-go/step.html)
- Share Medical Notes Safely -> `still-alive-tips/14-share-medical-notes.html` (https://www.nia.nih.gov/health/keeping-track-your-medicines)
- Smoke Alarm Maintenance -> `still-alive-tips/15-smoke-alarm-maintenance.html` (https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/fire.html)
- Carbon Monoxide Safety -> `still-alive-tips/16-carbon-monoxide-safety.html` (https://www.cdc.gov/co/)
- Safer Bathroom Setup -> `still-alive-tips/17-safer-bathroom-setup.html` (https://www.nia.nih.gov/health/prevent-falls-and-fractures)
- Heat Safety for Daily Routines -> `still-alive-tips/18-heat-safety-routine.html` (https://www.cdc.gov/disasters/extremeheat/)
- Cold Weather Readiness -> `still-alive-tips/19-cold-weather-readiness.html` (https://www.cdc.gov/disasters/winter/)
- Medication Organization for Emergencies -> `still-alive-tips/20-medication-organization.html` (https://www.cdc.gov/medicationsafety/)
- Stress Reset After an Emergency -> `still-alive-tips/21-stress-reset-after-emergency.html` (https://www.cdc.gov/mentalhealth/stress-coping/cope-with-stress/index.html)
- How Emergency Alerts Work -> `still-alive-tips/22-emergency-alerts-wea.html` (https://www.fcc.gov/consumers/guides/wireless-emergency-alerts-wea)
- Watches vs Warnings -> `still-alive-tips/23-weather-watches-warnings.html` (https://www.weather.gov/safety)
- Hydration Basics Under Stress -> `still-alive-tips/24-hydration-basics.html` (https://www.cdc.gov/healthywater/drinking/)
- Social Connection and Safety -> `still-alive-tips/25-social-connection-safety.html` (https://www.cdc.gov/aging/publications/features/lonely-older-adults.html)

## UI Notes
- Soft pastel card colors with rounded corners and drop shadows.
- Compact header with subtitle, category chips, and stacked cards.
- Fixed bottom navigation with an active "Tips" state.

## Acceptance Criteria
- Mobile tips page renders correctly at 360-420px width with no horizontal scroll.
- Each category shows five article cards.
- Category chips filter the article cards.
- Each card links to a local article page.
- Each article page includes a source link to the external reference.
- Still Alive page includes a "Mobile Safety Tips Preview" section linking to the new page.
