import os
import json

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "lexicon.json")

def parse_bib_file(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    concepts = {}
    duplicates = []

    idx = 0
    while True:
        idx = text.find("@concept{", idx)
        if idx == -1:
            break

        # find concept key
        start_key = idx + len("@concept{")
        end_key = text.find(",", start_key)
        key = text[start_key:end_key].strip()

        # find block contents using brace counting
        brace_level = 1
        i = end_key + 1
        while i < len(text) and brace_level > 0:
            if text[i] == "{":
                brace_level += 1
            elif text[i] == "}":
                brace_level -= 1
            i += 1
        block = text[end_key + 1:i - 1].strip()

        if key in concepts:
            duplicates.append(key)
            idx = i
            continue

        # parse fields
        concept_data = {}
        lines = block.splitlines()
        field_name = None
        field_value_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if "=" in line and line.endswith("},"):
                # single-line field
                name, value = line.split("=", 1)
                concept_data[name.strip()] = value.strip()[1:-2].strip()
            elif "=" in line:
                # multi-line start
                name, value = line.split("=", 1)
                field_name = name.strip()
                field_value_lines = [value.strip()[1:]]  # remove opening brace
            elif field_name:
                # accumulating multi-line field
                field_value_lines.append(line)
                if line.endswith("},"):
                    # end of multi-line field
                    full_value = " ".join(field_value_lines)
                    concept_data[field_name] = full_value[:-2].strip()  # remove closing },
                    field_name = None
                    field_value_lines = []

        concepts[key] = concept_data
        idx = i

    if duplicates:
        print("Warning: duplicate keys found:", duplicates)

    return concepts

# Loop over all .bib files
all_concepts = {}
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".bib"):
        path = os.path.join(DATA_DIR, filename)
        concepts = parse_bib_file(path)
        all_concepts.update(concepts)

# Optional: only 'ready'
# all_concepts = {k: v for k, v in all_concepts.items() if v.get("status") == "ready"}

# sort
sorted_concepts = dict(sorted(all_concepts.items()))

# save JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(sorted_concepts, f, ensure_ascii=False, indent=2)

print(f"JSON written to {OUTPUT_FILE} ({len(sorted_concepts)} concepts)")
