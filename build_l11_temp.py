import json

# Read current notebook
with open('01_Basic/L11_Prompt_Engineering_101.ipynb', 'r') as f:
    notebook = json.load(f)

# Define all remaining cells
remaining_cells = [
    # Part 1 intro
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": "## Part 1: Basic Prompt Design Patterns\n\n**Prompt design patterns** are proven structures that consistently produce good results.\n\n### Pattern 1: Direct Instruction\n\nSimply tell the model what to do.\n\n```\nInstruction: [Clear command]\nInput: [Data to process]\n```\n\n### Pattern 2: Role-Based Prompting\n\nAssign the model a specific role or persona.\n\n```\nYou are a [role]. [Task description]\n```\n\n### Pattern 3: Step-by-Step Reasoning\n\nAsk the model to think through the problem.\n\n```\nLet's solve this step by step:\n1. [First step]\n2. [Second step]\n...\n```\n\n### Pattern 4: Format Specification\n\nDefine exactly how the output should look.\n\n```\nProvide your answer in the following format:\n- Field 1: [value]\n- Field 2: [value]\n```\n\n---"
    }
]

print(f"Building notebook with {len(remaining_cells)} additional cells...")
