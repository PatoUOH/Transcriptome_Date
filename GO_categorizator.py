import pandas as pd

input_file = "go_list_biological_process.txt"

def read_go_file(path):
    rows = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or not line.startswith("GO:"):
                continue
            if "\t" in line:
                go_id, term = line.split("\t", 1)
            else:
                parts = line.split(None, 1)
                go_id = parts[0]
                term = parts[1] if len(parts) > 1 else ""
            if term == "0":
                term = ""
            rows.append({"id": go_id, "term": term})
    return rows

def classify_go_term(label):
    text = label.lower()

    # Angiogenesis
    if any(w in text for w in [
        "angiogenesis", "vasculogenesis", "blood vessel", "endothelial tube",
        "vessel morphogenesis", "sprouting"
    ]):
        return "Angiogenesis"

    # White cell trafficking
    if any(w in text for w in [
        "leukocyte", "neutrophil", "monocyte", "macrophage", "lymphocyte",
        "t cell", "b cell", "myeloid", "chemotaxis", "degranulation"
    ]):
        return "White cell trafficking"

    # Platelet activation
    if "platelet" in text or "thrombocyte" in text:
        return "Platelet activation"

    # Thrombosis
    if any(w in text for w in [
        "blood coagulation", "coagulation", "clot", "thrombus", "hemostasis"
    ]):
        return "Thrombosis"

    # Fibrinolysis
    if any(w in text for w in ["fibrinolysis", "plasminogen", "plasmin"]):
        return "Fibrinolysis"

    # VMSC proliferation
    if any(w in text for w in [
        "smooth muscle cell proliferation", "vascular smooth muscle cell", "vsmc"
    ]):
        return "VMSC proliferation"

    # Inflammation
    if any(w in text for w in [
        "inflammation", "inflammatory", "cytokine", "interleukin",
        "tumor necrosis factor", "tnf", "interferon",
        "immune response", "defense response", "innate immune"
    ]):
        return "Inflammation"

    # Vascular tone
    if any(w in text for w in [
        "vasodilation", "vasoconstriction", "vascular tone",
        "blood pressure", "nitric oxide", "smooth muscle contraction",
        "smooth muscle relaxation"
    ]):
        return "Vascular tone"

    # Vascular permeability
    if any(w in text for w in [
        "permeability", "barrier", "endothelial barrier",
        "tight junction", "cell-cell junction", "cell junction",
        "extracellular matrix", "basement membrane", "adhesion",
        "endothelial cell-cell adhesion", "paracellular"
    ]):
        return "Vascular permeability"

    # Metabolism
    if any(w in text for w in [
        "metabolic process", "metabolism", "biosynthetic process",
        "catabolic process", "glycolysis", "oxidative phosphorylation",
        "atp metabolic", "amino acid metabolic", "lipid metabolic",
        "fatty acid metabolic", "nucleotide metabolic"
    ]):
        return "Metabolism"

    return "UNASSIGNED"

go_rows = read_go_file(input_file)

for r in go_rows:
    r["high_level_function"] = classify_go_term(r["term"])
    
df = pd.DataFrame(go_rows)
df.to_csv("go_categorizations_biological_process.csv", index=False)
print(df.head()) 

