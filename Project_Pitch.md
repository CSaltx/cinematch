## Project Name:  CineMatch

### Project Overview:
For our final project we are proposing an application that helps users decide what to what watch. Users will discuss their television preferences will a chatbot, which will then recommend a TV show or movie depending on the user's input. The idea will be to finetune or use a prexisting Large Language Model (LLM) to essentailly "preload" an LLM (most likely wizard or [q]LLora) with data that will hold information regarding reviews of movies. This could help our chatbot develop the connections between movies and provide somewhat accurate responses based on the current chat. The data set used could be one of many existing datasets that hold reviews via IMDb and similar platforms.

### Feature Specification:  <1-2 pages>
- Mobile/Web Application (Choice IP)
- Frontend Options
  - React Native
  - ReactJS
  - NextJS
  - Vue
  - Angular
- Backend Options
  - Javascript
  - Python
    - Flask
    - Django
  - Go
  - Java
    - Spring
-  Functionality Options
  - Implement with pre-existing LLM
  - Finetune pre-existing LLM
    - Wizard
    - LLora
    - qLLora
    - LLama
  - Create own LLM
    - Barriers
      - Time-intensive
      - Complex
      - Probably difficult to achieve in the timeframe specified
      - Computationally intensive such that we would probably have to rent a superpod or more to train
  - Do a chatbot using an API or similar
    - Functionality could be less than intended
    - Could give poor answers or limited in scope
    - Good for timeframe as it could be completed in the 2 months specified
- UI/UX Design
  - ReactNative CSS or Tailwind for ReactJS
  - Figma for collaborative design
  - Maybe something else for experimentation
- Datasets
  - IMDB Reviews has a dataset that is good for sentiment analysis so could work well
  - IMDB Film Reviews is another one that could work especially for binary sentiment analysis
  - MovieLens has a 25M dataset that is collected from their website and propogated with 25 million reviews
  - OMDB API is another one that is crowdsourced and has content and images for various films (280k+)
  - UCI has a dataset for this too as well as 10's of others to choose from
  - Deciding on the above could be challenging but most likely any would work well for the task

### Technical Specification <1-2 sentences; optional>
The project could be a mobile or web app that implements a chatbot using either a frontend of [ReactNative/ReactJS] and a backend of a framework of our choosing. The idea would be to either have a server-based finetuned LLM to inteface with end users or to have a hardcoded chatbot that based on prefaces returns suggestions using an API of our choosing.
