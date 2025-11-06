# RNA-Seq Data Analysis
# Aim: To find differentially expressed genes and analyze expression levels between two samples.

# Step 1: Create sample RNA-Seq data (gene expression counts)
# Each gene has expression values for two different samples
data = {
    "Gene1": [50, 120],
    "Gene2": [200, 180],
    "Gene3": [90, 95],
    "Gene4": [300, 100],
    "Gene5": [40, 42]
}

# Step 2: Define a threshold for considering a gene as "differentially expressed"
threshold = 20  # if difference > 20, it is considered significant

# Step 3: Create an empty list to store differentially expressed genes
diff_genes = []

# Step 4: Loop through all genes and find the expression difference
for gene, values in data.items():
    diff = abs(values[0] - values[1])  # absolute difference between two samples
    if diff > threshold:               # check if the difference is big
        diff_genes.append(gene)        # add gene to the list

# Step 5: Print all RNA-Seq data clearly
print("=== RNA-Seq Data (Gene Expression Values) ===")
for gene, values in data.items():
    avg = (values[0] + values[1]) / 2  # calculate average expression
    print(f"{gene}: Sample1 = {values[0]}, Sample2 = {values[1]}, Average = {avg}")

# Step 6: Print all differentially expressed genes
print("\n=== Differentially Expressed Genes (difference > 20) ===")
if diff_genes:
    for g in diff_genes:
        print(g)
else:
    print("No genes show significant expression difference.")

# Step 7: Summary and conclusion
print("\n=== Summary ===")
print(f"Total genes analyzed: {len(data)}")
print(f"Genes with significant difference: {len(diff_genes)}")
print("\nConclusion: The above genes show large expression differences between two samples.")
