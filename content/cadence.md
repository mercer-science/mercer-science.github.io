---
title: Cadence, a Spaced-Repetition App
roles: [design, coding, wildcard]
tabs: [other-ui-projects, software-projects]
status: Ongoing, early MVP
dates: 2026 to present
images:
  - id: home
    src: assets/img/cadence-home.jpg
    alt: The Cadence home screen, showing a Your Decks list with a starter deck card, the number of cards due, and a Study Now button.
    caption: The deck list. How many cards are ready, and one button into the session.
  - id: deck
    src: assets/img/cadence-deck.jpg
    alt: A Cadence deck view listing each card's question and answer, with Add Card and Study Now actions.
    caption: Inside a deck. Every card at a glance, with add and study one tap away.
  - id: study-question
    src: assets/img/cadence-study-question.jpg
    alt: The Cadence study screen showing a card's question, a progress count of cards left, and a Show Answer button.
    caption: Studying. One card, one decision, and the count of what is left.
  - id: study-answer
    src: assets/img/cadence-study-answer.jpg
    alt: The Cadence answer screen with the card revealed and Again, Hard, Good, and Easy grading buttons, each labeled with its next interval and one marked Suggested.
    caption: The answer, with each grade's next interval and the FSRS-suggested choice marked.
  - id: settings
    src: assets/img/cadence-settings.jpg
    alt: The Cadence settings screen for connecting an AI provider (Claude, ChatGPT, or Gemini) with your own API key, and a Gentle Rephrasing toggle.
    caption: AI settings. Bring your own provider key; Gentle Rephrasing reshapes a card to test the idea, not the wording.
---

Anki is widely used by medical students, but its interface has accumulated years of features and settings that can make daily studying feel more complicated than it needs to be. Its underlying spaced-repetition scheduling is valuable; the challenge is making the study experience simpler and more manageable, especially when users face hundreds of due cards.

I am building Cadence as a streamlined alternative using React, TypeScript, and the FSRS scheduling algorithm, which models memory to determine when cards should be reviewed. The design focuses on reducing friction: making each card easy to review, showing users how much time their queue will take before they begin, and keeping frequently used settings accessible without overwhelming the interface.

[figure: home, deck]

[figure: study-question, study-answer]

In addition, the app will include LLM incorporation, altering each card to enhance the learning process.

[figure: settings]

The project is an ongoing early-stage. The source repository is private, so screenshots currently provide the best view of the application.
