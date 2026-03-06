#!/usr/bin/env python3
import json

with open('01_Basic/L11_Prompt_Engineering_101.ipynb', 'r') as f:
    nb = json.load(f)

cells = nb["cells"]

# Add all remaining parts
final_cells = [
    # Part 4 markdown
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "## Part 4: Few-Shot Prompting\n\n**Few-shot prompting** provides examples to demonstrate the desired behavior.\n\n### When to Use Few-Shot:\n\n- Complex or ambiguous tasks\n- Specific output format needed\n- Consistent style required\n- Zero-shot performance is poor\n\n### Few-Shot Structure:\n\n```\n[Instruction]\n\nExample 1:\nInput: [example input 1]\nOutput: [example output 1]\n\nExample 2:\nInput: [example input 2]\nOutput: [example output 2]\n\nNow your turn:\nInput: [actual input]\nOutput:\n```\n\n### Example Selection Tips:\n\n1. **Diverse examples** - Cover different cases\n2. **Clear patterns** - Make the task obvious\n3. **Consistent format** - Same structure for all\n4. **Quality over quantity** - 2-5 good examples usually enough\n\n---"
    },
    # Step 6 code
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# Step 6: Few-Shot Prompting Examples\n\nprint(\"Few-Shot Prompting\\n\")\nprint(\"=\" * 60)\n\n# Task 1: Custom classification\nprint(\"\\n1. CUSTOM CLASSIFICATION (Product Categories)\")\nprint(\"-\" * 60)\nfew_shot_classify = \"\"\"Classify products into categories: Electronics, Clothing, or Food.\n\nExample 1:\nProduct: Laptop computer\nCategory: Electronics\n\nExample 2:\nProduct: Cotton t-shirt\nCategory: Clothing\n\nExample 3:\nProduct: Organic apples\nCategory: Food\n\nNow classify:\nProduct: Wireless mouse\nCategory:\"\"\"\nprint(f\"Prompt: {few_shot_classify}\\n\")\nresult = generate_text(few_shot_classify, max_length=120, temperature=0.3)\nprint(f\"Output: {result}\")\nprint()\n\n# Task 2: Format conversion\nprint(\"\\n2. FORMAT CONVERSION\")\nprint(\"-\" * 60)\nfew_shot_format = \"\"\"Convert casual messages to professional emails.\n\nExample 1:\nCasual: Hey, meeting at 3?\nProfessional: Dear colleague, shall we schedule our meeting for 3 PM?\n\nExample 2:\nCasual: Got the files, thx!\nProfessional: Thank you for sending the files. I have received them.\n\nNow convert:\nCasual: Can u review my doc?\nProfessional:\"\"\"\nprint(f\"Prompt: {few_shot_format}\\n\")\nresult = generate_text(few_shot_format, max_length=100, temperature=0.5)\nprint(f\"Output: {result}\")\nprint()\n\n# Task 3: Pattern completion\nprint(\"\\n3. PATTERN COMPLETION\")\nprint(\"-\" * 60)\nfew_shot_pattern = \"\"\"Generate creative product names following the pattern.\n\nExample 1:\nProduct: Coffee maker\nName: BrewMaster Pro\n\nExample 2:\nProduct: Running shoes\nName: SprintForce Elite\n\nExample 3:\nProduct: Desk lamp\nName: LumiDesk Plus\n\nNow create:\nProduct: Water bottle\nName:\"\"\"\nprint(f\"Prompt: {few_shot_pattern}\\n\")\nresult = generate_text(few_shot_pattern, max_length=100, temperature=0.7)\nprint(f\"Output: {result}\")\nprint()\n\nprint(\"=\" * 60)\nprint(\"\\nFew-shot examples teach the model your specific requirements!\")"
    },
    # Part 5 markdown
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "## Part 5: Chain-of-Thought Prompting\n\n**Chain-of-Thought (CoT)** prompting encourages the model to show its reasoning process.\n\n### Why Chain-of-Thought Works:\n\n- Breaks complex problems into steps\n- Reduces reasoning errors\n- Makes outputs more interpretable\n- Improves accuracy on multi-step tasks\n\n### CoT Patterns:\n\n**Pattern 1: Explicit Steps**\n```\nLet's solve this step by step:\n1. [First step]\n2. [Second step]\n3. [Conclusion]\n```\n\n**Pattern 2: Think Aloud**\n```\nLet's think through this carefully:\n[Reasoning process]\nTherefore, [answer]\n```\n\n**Pattern 3: Few-Shot CoT**\n```\nExample with reasoning:\nQuestion: [Q]\nThinking: [reasoning]\nAnswer: [A]\n```\n\n---"
    },
    # Step 7 code
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": "# Step 7: Chain-of-Thought Prompting\n\nprint(\"Chain-of-Thought Prompting\\n\")\nprint(\"=\" * 60)\n\n# Without CoT (baseline)\nprint(\"\\n1. WITHOUT CHAIN-OF-THOUGHT (Baseline)\")\nprint(\"-\" * 60)\nno_cot = \"\"\"Question: If a store has 15 apples and sells 7, then receives 12 more, how many apples does it have?\n\nAnswer:\"\"\"\nprint(f\"Prompt: {no_cot}\\n\")\nresult = generate_text(no_cot, max_length=80, temperature=0.3)\nprint(f\"Output: {result}\")\nprint()\n\n# With explicit CoT\nprint(\"\\n2. WITH CHAIN-OF-THOUGHT\")\nprint(\"-\" * 60)\nwith_cot = \"\"\"Question: If a store has 15 apples and sells 7, then receives 12 more, how many apples does it have?\n\nLet's solve this step by step:\n1. Starting apples: 15\n2. After selling 7: 15 - 7 = 8\n3. After receiving 12 more: 8 + 12 = 20\n\nAnswer:\"\"\"\nprint(f\"Prompt: {with_cot}\\n\")\nresult = generate_text(with_cot, max_length=100, temperature=0.3)\nprint(f\"Output: {result}\")\nprint()\n\n# Few-shot CoT\nprint(\"\\n3. FEW-SHOT CHAIN-OF-THOUGHT\")\nprint(\"-\" * 60)\nfew_shot_cot = \"\"\"Solve word problems by showing your reasoning.\n\nExample:\nQuestion: A book costs 12 dollars. If you buy 3 books, how much do you spend?\nThinking: Each book is 12 dollars. For 3 books, I multiply: 3 × 12 = 36 dollars.\nAnswer: 36 dollars\n\nNow solve:\nQuestion: A pizza has 8 slices. If 3 people each eat 2 slices, how many slices remain?\nThinking:\"\"\"\nprint(f\"Prompt: {few_shot_cot}\\n\")\nresult = generate_text(few_shot_cot, max_length=120, temperature=0.5)\nprint(f\"Output: {result}\")\nprint()\n\nprint(\"=\" * 60)\nprint(\"\\nChain-of-thought improves reasoning and accuracy!\")"
    }
]

cells.extend(final_cells)
print(f"Added Parts 4-5, total cells: {len(cells)}")

nb["cells"] = cells
with open('01_Basic/L11_Prompt_Engineering_101.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)

print("Saved Parts 4-5")
