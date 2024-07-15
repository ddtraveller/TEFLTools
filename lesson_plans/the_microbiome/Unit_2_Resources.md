# ## Learning Unit 2

## Learning Unit 2: Microbiome Research Techniques
- Objectives:
  * Understand common methods for studying the microbiome
  * Interpret basic microbiome data
- Topics:
  * 16S rRNA gene sequencing
  * Whole-genome shotgun metagenomic sequencing
  * Bioinformatics tools for microbiome analysis
- Activities:
  * Analyze sample microbiome datasets
  * Design a hypothetical microbiome study relevant to Timor-Leste

## Unit Resources

# Lecture Notes

## 16S rRNA Gene Sequencing

### Introduction
- 16S rRNA gene: Highly conserved gene present in all bacteria
- Used for taxonomic classification and phylogenetic studies
- Approximately 1,500 base pairs long

### Sequencing Process
1. DNA extraction from sample
2. PCR amplification of 16S rRNA gene
3. Sequencing of amplified products
4. Bioinformatic analysis of sequences

### Advantages
- Cost-effective for large-scale studies
- Well-established databases for comparison
- Suitable for identifying bacterial composition

### Limitations
- Limited resolution (genus or species level)
- Cannot provide functional information
- Potential PCR bias

## Whole-Genome Shotgun Metagenomic Sequencing

### Principles
- Sequences all genetic material in a sample
- Provides both taxonomic and functional information

### Process
1. DNA extraction from sample
2. Fragmentation of DNA
3. Sequencing of all fragments
4. Assembly and annotation of sequences

### Comparison with 16S rRNA Sequencing
- Higher resolution (strain-level identification possible)
- Provides functional information
- More expensive and computationally intensive

### Applications
- Identifying novel genes and pathways
- Understanding community functions
- Studying microbial interactions

## Bioinformatics Tools for Microbiome Analysis

### Common Software Packages
- QIIME (Quantitative Insights Into Microbial Ecology)
- mothur
- DADA2 (Divisive Amplicon Denoising Algorithm)

### Basic Analysis Steps
1. Quality control and preprocessing
2. OTU clustering or ASV (Amplicon Sequence Variant) generation
3. Taxonomic assignment
4. Diversity analysis (alpha and beta diversity)
5. Statistical analysis and visualization

### Visualization Tools
- Krona (interactive pie charts)
- PhyloSeq (R package for microbiome analysis)
- MicrobiomeAnalyst (web-based tool)

# Discussion Questions

1. How might the choice between 16S rRNA sequencing and metagenomic sequencing affect our understanding of the microbiome in Timor-Leste?

2. What are some potential challenges in implementing microbiome research techniques in a resource-limited setting like Timor-Leste? How might these be overcome?

3. How could microbiome research techniques be applied to study traditional Timorese practices and their impact on gut health?

4. Discuss the ethical considerations of collecting and analyzing microbiome samples from communities in Timor-Leste. How can researchers ensure responsible and respectful practices?

5. How might bioinformatics tools need to be adapted or developed to better suit the specific needs and contexts of microbiome research in Timor-Leste?

# Writing Exercise Instructions

Write a 500-word essay comparing and contrasting 16S rRNA gene sequencing and whole-genome shotgun metagenomic sequencing. Include the following points:

1. Basic principles of each technique
2. Advantages and limitations of each method
3. Suitable applications for each technique
4. Considerations for choosing between the two methods in a resource-limited setting like Timor-Leste

Use clear, concise language and provide specific examples where possible. Cite at least two scientific sources to support your points.

# Assignment Details

## Microbiome Study Design Project

### Objective
Design a hypothetical microbiome study relevant to a health issue in Timor-Leste.

### Requirements
1. Choose a specific health issue relevant to Timor-Leste (e.g., malnutrition, infectious disease, maternal health)
2. Formulate a clear research question
3. Select an appropriate sequencing method (16S rRNA or metagenomic) and justify your choice
4. Outline the basic study design, including:
   - Sample collection method
   - Sample size and population
   - Control group (if applicable)
   - Key variables to measure
5. Describe the planned analysis approach, including bioinformatics tools
6. Discuss potential challenges and limitations of the study
7. Explain the potential impact of the study on public health in Timor-Leste

### Format
- 3-4 pages, double-spaced
- Include a title page and references (not counted in page limit)
- Use APA format for citations and references

### Grading Criteria
- Relevance to Timor-Leste context (20%)
- Appropriateness of research design (30%)
- Justification of methods chosen (20%)
- Consideration of practical and ethical issues (15%)
- Clarity and organization of writing (15%)

# Additional Materials

## Sample 16S rRNA Dataset

```
Sample_ID,Bacteroides,Prevotella,Faecalibacterium,Escherichia,Bifidobacterium
TL001,45.2,12.3,8.7,2.1,5.6
TL002,38.9,15.7,10.2,1.8,4.9
TL003,42.1,13.5,9.5,2.3,6.1
TL004,40.5,14.1,9.8,2.0,5.3
TL005,43.7,13.9,9.1,1.9,5.8
```

## Metagenomic Functional Analysis Chart

![Metagenomic Functional Analysis](https://example.com/metagenomic_chart.png)

(Note: This is a placeholder. In a real lesson, you would include an actual image of a metagenomic functional analysis chart.)

## Key Bioinformatics Tools Handout

1. QIIME2
   - Purpose: Comprehensive microbiome analysis pipeline
   - Key features: Quality filtering, OTU clustering, diversity analysis
   - Website: https://qiime2.org/

2. mothur
   - Purpose: Microbial community analysis software
   - Key features: Sequence alignment, classification, population statistics
   - Website: https://mothur.org/

3. DADA2
   - Purpose: High-resolution sample inference from amplicon data
   - Key features: Error correction, exact sequence variants
   - R package: https://benjjneb.github.io/dada2/

4. Kraken2
   - Purpose: Taxonomic classification of metagenomic DNA sequences
   - Key features: Fast, accurate classification using k-mer matches
   - GitHub: https://github.com/DerrickWood/kraken2

5. MetaPhlAn
   - Purpose: Profiling composition of microbial communities
   - Key features: Species-level resolution, estimation of relative abundances
   - Website: https://huttenhower.sph.harvard.edu/metaphlan/