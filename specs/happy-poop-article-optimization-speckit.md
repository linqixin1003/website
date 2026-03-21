# Speckit Specification: Happy Poop Articles Overhaul

**Date:** 2026-02-04
**Project:** Happy Poop App (Web Version)
**Scope:** Content Enrichment & UI/UX Redesign for 30 Health Articles
**Stakeholders:** Global Top UI Master, Global Top Science Writer

---

## 1. Executive Summary
The goal is to transform 30 existing basic health tips into premium, medical-grade, visually stunning interactive articles. The content must bridge the gap between "medical textbook accuracy" and "friendly, accessible advice," while the UI must reflect a "modern digital health magazine" aesthetic.

## 2. Design Specifications (The "UI Master" Vision)

### 2.1 Visual Language: "Soft Clinical"
- **Color Palette:**
  - **Base:** Clean White (`#FFFFFF`) & Soft Gray (`#F9FAFB`) background.
  - **Typography:** Deep Charcoal (`#1F2937`) for readability, not pure black.
  - **Accents:** Category-specific branding (Purple/Bowel, Blue/Urinary, Pink/Menstrual, Teal/Hydration, Red/Fitness, Green/Nutrition).
- **Typography:**
  - **Headings:** `Inter` or `SF Pro Display`, bold, tight tracking. High contrast.
  - **Body:** `Merriweather` or `Georgia` (serif) for long-form reading comfort, or a high x-height sans-serif like `Lato`. 18px base size.
  - **Line Height:** 1.6 to 1.8 for optimal readability.

### 2.2 Layout & Components
- **Hero Section:**
  - Dynamic gradient background matching the category.
  - Custom generated SVG Hero Illustration (abstract but contextual).
  - "Quick Summary" card (TL;DR) at the top with glassmorphism effect.
- **Content Blocks:**
  - **"Medical Insight" Box:** Blue background, icon-driven, for deep science.
  - **"Red Flag" Alert:** Red/Rose background, distinct styling for "When to see a doctor".
  - **"Myth vs. Fact" Toggle:** Interactive or distinct visual comparison.
  - **Action Checklist:** Checkbox style for actionable advice.
- **Visual Breaks:**
  - Custom SVG dividers (waves, curves) between sections.
  - Inline SVG illustrations for key concepts (e.g., hydration levels, stool types).

### 2.3 Interaction
- Sticky Table of Contents for easy navigation.
- Progress bar at the top.
- Micro-interactions on buttons/links.

---

## 3. Content Specifications (The "Science Writer" Vision)

### 3.1 Content Structure (Target: 800-1200 words)
1.  **The Hook:** Relatable scenario or surprising fact.
2.  **The Science (How it Works):** simplified physiology (e.g., "How peristalsis works" for bowel health).
3.  **The Signals (Self-Check):** Detailed interpretation of body signals (Color, Shape, Frequency).
4.  **The Strategy (Actionable):** Diet, exercise, lifestyle changes.
5.  **The "Red Flags" (Warning):** Clear distinction between normal and emergency.
6.  **Expert FAQ:** Answering common but embarrassing questions.

### 3.2 Tone & Voice
- **Authoritative:** Citing general medical consensus.
- **Empathetic:** Understanding the anxiety around health issues.
- **Direct:** No fluff, specifically for embarrassing topics (poop, periods).

### 3.3 Persona Alignment
- **Bowel (1-6):** Colorectal Specialist (Focus: Gut motility, microbiome).
- **Urinary (7-10):** Urologist (Focus: Kidney function, hydration).
- **Menstrual (11-15):** Gynecologist (Focus: Hormonal cycles, reproductive health).
- **Hydration/Nutrition (16-30):** Clinical Nutritionist & Sports Scientist.

---

## 4. Technical Implementation Plan

### 4.1 Automation Pipeline
1.  **Content Expansion:** Use LLM with "Expert Persona" prompts to rewrite existing `zh` content.
2.  **SVG Generation:** Programmatically generate SVG strings based on keywords (e.g., "Stomach", "Water Drop", "Warning") to embed directly in HTML.
3.  **Template Injection:** Create a robust HTML5 template containing the new CSS/JS and inject the generated content.

### 4.2 File Structure Update
- Overwrite `zh/still-alive-tips/*.html` (Source of Truth).
- (Subsequent Task) Re-translate to other languages.

---

## 5. Acceptance Criteria
- [ ] **Visuals:** Every article has a unique Hero SVG and at least 2 inline illustrations.
- [ ] **Length:** Word count increased by >200%.
- [ ] **UI:** Implements "Happy Poop" branding (no "Still Alive" remnants), responsive design, and high accessibility.
- [ ] **Content:** Includes "Red Flags" section and "Quick Summary" in every article.
