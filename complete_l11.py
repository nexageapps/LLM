#!/usr/bin/env python3
import json

# Load notebook
with open('01_Basic/L11_Prompt_Engineering_101.ipynb', 'r') as f:
    nb = json.load(f)

cells = nb["cells"]

# Add Part 2 through Part 9, Exercises, Key Takeaways, and Resources
additional_cells = [
    # Part 2 markdown
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "## Part 2: Instruction Formatting Techniques\n\n**Instruction formatting** helps models understand exactly what you want.\n\n### Key Formatting Principles:\n\n1. **Use Clear Delimiters**\n   - Separate instruction from input\n   - Use markers like ###, ---, or labels\n\n2. **Structure with Labels**\n   - Instruction:\n   - Input:\n   - Output:\n\n3. **Numbered Steps**\n   - Break complex tasks into steps\n   - Guide the model's reasoning\n\n4. **Explicit Constraints**\n   - Specify length, tone, format\n   - Define what to include/exclude\n\n### Good vs Bad Formatting:\n\n**Bad:**\n```\nTranslate this to French hello how are you\n```\n\n**Good:**\n```\nInstruction: Translate the following English text to French.\nInput: Hello, how are you?\nOutput:\n```\n\n---"
    },
    # Step 4 code
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# Step 4: Instruction Formatting Examples\n\nprint(\"Instruction Formatting Techniques\\n\")\nprint(\"=\" * 60)\n\n# Example 1: Poor formatting\nprint(\"\\n1. POOR FORMATTING\")\nprint(\"-\" * 60)\npoor_prompt = \"summarize this text Machine learning is a subset of AI\"\nprint(f\"Prompt: {poor_prompt}\\n\")\nresult = generate_text(poor_prompt, max_length=60)\nprint(f\"Output: {result}\")\nprint()\n\n# Example 2: Clear delimiters\nprint(\"\\n2. CLEAR DELIMITERS\")\nprint(\"-\" * 60)\ndelimited_prompt = \"\"\"Task: Summarize the following text in one sentence.\n\n###\nMachine learning is a subset of artificial intelligence that enables computers to learn from data without being explicitly programmed. It uses algorithms to identify patterns and make predictions.\n###\n\nSummary:\"\"\"\nprint(f\"Prompt: {delimited_prompt}\\n\")\nresult = generate_text(delimited_prompt, max_length=100)\nprint(f\"Output: {result}\")\nprint()\n\n# Example 3: Structured labels\nprint(\"\\n3. STRUCTURED LABELS\")\nprint(\"-\" * 60)\nlabeled_prompt = \"\"\"Instruction: Extract the key information from the text.\nInput: Python was created by Guido van Rossum in 1991.\nOutput format: Creator, Year, Language\nOutput:\"\"\"\nprint(f\"Prompt: {labeled_prompt}\\n\")\nresult = generate_text(labeled_prompt, max_length=80)\nprint(f\"Output: {result}\")\nprint()\n\n# Example 4: Explicit constraints\nprint(\"\\n4. EXPLICIT CONSTRAINTS\")\nprint(\"-\" * 60)\nconstrained_prompt = \"\"\"Write a product description with these requirements:\n- Length: Exactly 2 sentences\n- Tone: Professional\n- Product: Wireless headphones\n- Include: Battery life and comfort\n\nDescription:\"\"\"\nprint(f\"Prompt: {constrained_prompt}\\n\")\nresult = generate_text(constrained_prompt, max_length=100)\nprint(f\"Output: {result}\")\nprint()\n\nprint(\"=\" * 60)\nprint(\"\\nClear formatting leads to better, more predictable outputs!\")"
    }
]

cells.extend(additional_cells)
print(f"Added Part 2, total cells: {len(cells)}")

# Save
nb["cells"] = cells
with open('01_Basic/L11_Prompt_Engineering_101.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)

print("Saved Part 2")
