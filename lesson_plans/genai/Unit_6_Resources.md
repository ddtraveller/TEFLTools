# ## Learning Unit 6

## Learning Unit 6: Prompt Engineering and Effective Use of LLMs
- Objectives:
  * Learn techniques for effective prompt engineering
  * Understand how to leverage LLMs for various tasks
- Topics:
  * Principles of prompt engineering
  * In-context learning and few-shot learning
  * Best practices for interacting with LLMs
- Activities:
  * Hands-on workshop on prompt engineering
  * Competition: Create the most effective prompts for specific tasks relevant to Timor-Leste

## Unit Resources

Here are detailed resources for Learning Unit 6: Prompt Engineering and Effective Use of LLMs, formatted in Markdown:

# Resources for Learning Unit 6

## 1. Lecture Notes

### Principles of Prompt Engineering

#### Introduction
- Prompt engineering is the art and science of crafting effective inputs for large language models (LLMs)
- Goal: Elicit accurate, relevant, and useful responses from the AI

#### Key Principles
1. Clarity and Specificity
   - Be clear about what you want the AI to do
   - Use specific language and avoid ambiguity
   - Example: "List 5 tourist attractions in Dili, Timor-Leste" instead of "Tell me about tourism in Timor-Leste"

2. Provide Context
   - Give background information relevant to the task
   - Help the AI understand the perspective or role it should adopt
   - Example: "You are a cultural expert on Timor-Leste. Explain the significance of tais in Timorese culture."

3. Use Examples (Few-shot learning)
   - Provide examples of desired input-output pairs
   - Helps the AI understand the expected format and style
   - Example:
     ```
     Translate the following English phrases to Tetum:
     English: Hello
     Tetum: Bondia
     English: Thank you
     Tetum: Obrigadu
     English: How are you?
     Tetum: [AI should complete this]
     ```

4. Specify Output Format
   - Clearly state how you want the information presented
   - Use structural cues like bullet points, numbered lists, or tables
   - Example: "Present the information in a table with columns for Name, Location, and Brief Description"

5. Break Complex Tasks into Steps
   - For multi-step tasks, guide the AI through each step
   - Use numbered instructions or separate prompts for each stage
   - Example:
     ```
     1. List 3 traditional Timorese dishes
     2. For each dish, provide its main ingredients
     3. Explain the cultural significance of each dish in 1-2 sentences
     ```

6. Iterative Refinement
   - Start with a basic prompt and refine based on the output
   - Adjust specificity, add constraints, or provide additional context as needed
   - Example: If the initial response is too broad, add "Focus specifically on eco-tourism opportunities"

### In-context Learning and Few-shot Learning

#### In-context Learning
- Definition: The AI's ability to adapt its behavior based on information provided within the prompt
- Allows for task-specific guidance without fine-tuning the model
- Useful for customizing responses to specific contexts or domains

#### Few-shot Learning
- Definition: Providing a few examples of the desired task within the prompt
- Helps the AI understand the expected pattern or format
- Particularly useful for specialized tasks or domain-specific knowledge

#### Techniques
1. Task Description + Examples
   ```
   Classify the sentiment of the following Tetum phrases as Positive, Negative, or Neutral:

   Example 1:
   Phrase: "Hau kontente los ho ita nia vizita."
   Sentiment: Positive

   Example 2:
   Phrase: "Tempu oras ne'e manas demais."
   Sentiment: Negative

   Now classify this:
   Phrase: "Orsamentu estadu tinan ida ne'e hanesan tinan kotuk."
   Sentiment:
   ```

2. Analogical Reasoning
   ```
   Complete the analogy:
   Dili is to Timor-Leste as Jakarta is to Indonesia.
   Tetum is to Timor-Leste as ___ is to Malaysia.
   ```

3. Format Mimicking
   ```
   Create a short news headline about a recent event in Timor-Leste, following this format:
   "[Location]: [Brief description of event]"

   Example:
   "Dili: New solar power plant inaugurated, boosting clean energy capacity"

   Your headline:
   ```

### Best Practices for Interacting with LLMs

1. Start Broad, Then Narrow
   - Begin with a general prompt and refine based on the response
   - Allows for exploration of the AI's knowledge before focusing

2. Use Clear Instruction Words
   - "Explain", "List", "Summarize", "Compare", "Analyze", etc.
   - Helps direct the AI's response more effectively

3. Specify the Audience
   - Indicate the intended reader's background or expertise level
   - Helps tailor the complexity and tone of the response

4. Set Constraints
   - Limit word count, specify language level, or set other parameters
   - Helps control the scope and format of the output

5. Request Multiple Perspectives
   - Ask for pros and cons, or different viewpoints on a topic
   - Encourages more balanced and comprehensive responses

6. Use Role-Playing
   - Ask the AI to adopt a specific persona or expertise
   - Useful for generating specialized or creative content

7. Fact-Check and Verify
   - Always verify important information from authoritative sources
   - Be aware of the AI's limitations and potential for errors

8. Iterate and Refine
   - Use follow-up prompts to clarify or expand on initial responses
   - Treat the interaction as a dialogue to achieve the best results

## 2. Discussion Questions

1. How might effective prompt engineering be used to preserve and promote Timorese languages and cultural heritage?

2. Discuss the potential benefits and challenges of using LLMs for educational purposes in Timor-Leste, considering factors such as language barriers and access to technology.

3. How could prompt engineering techniques be applied to create a virtual assistant for Timorese government services? What ethical considerations should be taken into account?

4. Compare the potential impacts of zero-shot, few-shot, and fine-tuned models for specific applications in Timor-Leste's context. Which approach might be most appropriate for different scenarios?

5. How can we ensure that prompts and AI-generated content are culturally sensitive and appropriate for Timorese users? What strategies can be employed to mitigate potential biases?

6. Discuss the role of prompt engineering in developing AI applications for Timor-Leste's key industries (e.g., agriculture, tourism, oil and gas). How might these techniques be used to address industry-specific challenges?

7. How can prompt engineering be used to generate content in Tetum or other local languages, given that most LLMs are primarily trained on English and other major world languages?

8. What are the potential risks of over-reliance on AI-generated content in a developing country context? How can these risks be mitigated through effective prompt engineering and user education?

## 3. Writing Exercise Instructions

### Exercise 1: Cultural Preservation Prompt Design

1. Choose a specific aspect of Timorese culture (e.g., traditional music, folklore, crafts).
2. Design a series of prompts that could be used to generate educational content about this cultural element.
3. Your prompts should aim to:
   - Provide accurate information
   - Engage the reader (consider using storytelling techniques)
   - Be appropriate for a specific age group (specify your target audience)
4. Write at least 3 different prompts, each using a different prompt engineering technique discussed in the lecture.
5. For each prompt, explain your reasoning behind the design choices.

### Exercise 2: Multilingual Prompt Refinement

1. Start with the following basic prompt:
   "Translate the phrase 'Welcome to Timor-Leste' into Tetum."
2. Refine this prompt through at least 3 iterations, each time adding elements to improve its effectiveness. Consider:
   - Adding context
   - Specifying formality level
   - Requesting multiple variations
   - Asking for pronunciation guidance
3. For each iteration, provide the refined prompt and explain how and why you modified it.
4. Discuss how your final prompt might be more effective in producing a useful and culturally appropriate translation.

## 4. Assignment Details

### Prompt Engineering Project: Timor-Leste Tourism Chatbot

#### Objective
Design a set of prompts that could be used to create a simple AI-powered chatbot for tourists visiting Timor-Leste.

#### Requirements
1. Create at least 10 prompts covering different aspects of tourism in Timor-Leste, such as:
   - General information about the country
   - Popular destinations
   - Cultural etiquette
   - Transportation options
   - Local cuisine
   - Accommodation recommendations
   - Safety tips
   - Language assistance

2. For each prompt, include:
   - The prompt itself
   - An explanation of the prompt engineering techniques used
   - The intended purpose of the prompt within the chatbot's functionality

3. Design at least 3 prompts that utilize few-shot learning to handle potential user queries.

4. Include at least 2 prompts that demonstrate how the chatbot could provide information in both English and Tetum.

5. Write a brief reflection (500-750 words) discussing:
   - The challenges you encountered in designing prompts for this specific use case
   - How you addressed potential cultural sensitivities or biases
   - The potential benefits and limitations of using an AI chatbot for tourism in Timor-Leste

#### Submission Guidelines
- Submit your prompts in a clearly formatted document (Markdown preferred)
- Include your reflection at the end of the document
- Be prepared to demonstrate and discuss your prompts in class

## 5. Additional Materials and Examples

### Example: Iterative Prompt Refinement

Initial Prompt:
"Tell me about coffee production in Timor-Leste."

Refined Prompt 1:
"Provide an overview of coffee production in Timor-Leste, including key growing regions and typical flavor profiles."

Refined Prompt 2:
"As an agricultural expert, describe coffee production in Timor-Leste. Include:
1. Main coffee-growing regions
2. Typical varieties grown
3. Flavor profiles of Timorese coffee
4. Challenges faced by local coffee farmers
5. Recent initiatives to support the coffee industry

Limit your response to 250-300 words and use bullet points where appropriate."

### Example: Few-shot Learning for Local Language Generation

Prompt:
```
Translate the following phrases from English to Tetum, maintaining the same style and formality:

English: "Good morning, how can I assist you today?"
Tetum: "Bondia, oinsá ha'u bele ajuda ita ohin?"

English: "Please follow me to your table."
Tetum: "Favór ida tuir ha'u ba ita-nia meza."

English: "Would you like to try our local specialty dish?"
Tetum: [AI should complete this translation]

English: "Thank you for visiting our restaurant. Have a great day!"
Tetum: [AI should complete this translation]
```

### Resource: Prompt Engineering Checklist

When designing prompts, consider the following:

- [ ] Is the instruction clear and specific?
- [ ] Have I provided necessary context?
- [ ] Would examples (few-shot learning) improve the output?
- [ ] Is the desired output format clearly specified?
- [ ] For complex tasks, have I broken them into steps?
- [ ] Have I considered the intended audience?
- [ ] Are there any potential biases or cultural sensitivities to address?
- [ ] Can the prompt be refined or iterated upon based on initial outputs?