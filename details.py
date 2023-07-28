import pandas as pd
import csv

Hchain={}
Lchain={}
model={}
antigen_type={}
antigen_het_name={}
antigen_name={}
short_header={}	
date={}	
compound={}
organism={}
heavy_species={}
light_species={}
antigen_species={}	
authors={}
resolution={}
method={}	
r_free={}	
r_factor={}	
scfv={}	
engineered={}	
heavy_subclass={}	
light_subclass={}	
light_ctype={}
affinity={}
delta_g={}
affinity_method={}
temperature={}
pmid={}


def add_details_dict(list, antigen):
    Hchain[antigen]=list[1]
    Lchain[antigen]=list[2]
    model[antigen]=list[3]
    antigen_type[antigen]=list[5]
    antigen_het_name[antigen]=list[6]
    antigen_name[antigen]=list[7]
    short_header[antigen]=list[8]
    date[antigen]=list[9]	
    compound[antigen]=list[10]
    organism[antigen]=list[11]
    heavy_species[antigen]=list[12]
    light_species[antigen]=list[13]
    antigen_species[antigen]=list[14]	
    authors[antigen]=list[15]
    resolution[antigen]=list[16]
    method[antigen]=list[17]	
    r_free[antigen]=list[18]	
    r_factor[antigen]=list[19]	
    scfv[antigen]=list[20]	
    engineered[antigen]=list[21]	
    heavy_subclass[antigen]=list[22]	
    light_subclass[antigen]=list[23]	
    light_ctype[antigen]=list[24]
    affinity[antigen]=list[25]
    delta_g[antigen]=list[26]
    affinity_method[antigen]=list[27]
    temperature[antigen]=list[28]
    pmid[antigen]=list[29]

# Open bsa.xlsx file and generate a list of all complexes
df = pd.read_excel('/Users/gracewang/Documents/wilson_lab/summary_files/bsa.xlsx')
complexes = df['Antibody'].tolist()

# Get list with file names
file_list = [item[:-2]+".tsv" for item in complexes]
# print(file_list)


# Open each file and turn tsv into a list
for file in file_list:
    details_list = []
    with open(file, "r", newline="") as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter="\t")
        for row in tsv_reader:
            details_list.append(row)
    for list in details_list[1:]:
        antigen = list[0]+"_chothia_"+list[4]
        Hchain[antigen]=list[1]
        Lchain[antigen]=list[2]
        model[antigen]=list[3]
        antigen_type[antigen]=list[5]
        antigen_het_name[antigen]=list[6]
        antigen_name[antigen]=list[7]
        short_header[antigen]=list[8]
        date[antigen]=list[9]	
        compound[antigen]=list[10]
        organism[antigen]=list[11]
        heavy_species[antigen]=list[12]
        light_species[antigen]=list[13]
        antigen_species[antigen]=list[14]	
        authors[antigen]=list[15]
        resolution[antigen]=list[16]
        method[antigen]=list[17]	
        r_free[antigen]=list[18]	
        r_factor[antigen]=list[19]	
        scfv[antigen]=list[20]	
        engineered[antigen]=list[21]	
        heavy_subclass[antigen]=list[22]	
        light_subclass[antigen]=list[23]	
        light_ctype[antigen]=list[24]
        affinity[antigen]=list[25]
        delta_g[antigen]=list[26]
        affinity_method[antigen]=list[27]
        temperature[antigen]=list[28]
        pmid[antigen]=list[29]

    #    if "|" in i[4]:
    #        chain = i[4].split(" | ")
    #        for letter in chain:
    #            add_details_dict(details_list, i[0]+"_chothia_"+chain)
    #    else:
    #        add_details_dict(details_list,i[0]+"_chothia_"+i[4])
    # print(file + " added")
    #     #     antigen.split(" | ")
    #     # antigen = i[0]+"_chothia_"+i[4]
    #     # if "|" in antigen:
    #     #     antigen.split(" | ")



# Add each complex and detail into dictionary

# Map

# Replace 'input_file.xlsx' with the path to your Excel file
# df = pd.read_excel('/Users/gracewang/Documents/wilson_lab/summary_files/bsa.xlsx')

# print(df.head())

# antibodies = df['Antibody'].tolist()
# print(antibodies)


### Gets contents of files
# for file_name in file_list:
#     # Open the file and read its content
#     with open(file_name, 'r') as file:
#         content = file.read()
        
#         # Perform any desired operations with the file content
#         print(f"Content of {file_name}:")
#         print(content)



# Replace 'your_file.tsv' with the path to your TSV file
# By default, the separator for read_csv is a comma (','), so we need to specify the separator as '\t' for TSV files.


# Now you can work with the DataFrame 'df' containing the data from the TSV file
# print(df_5)

# tsv_list = []


# for i in tsv_list[1:]:
#     antigen = i[0]+"_chothia_"+i[4]
#     Hchain[antigen]=i[1]
#     Lchain[antigen]=i[2]
#     model[antigen]=i[3]
#     antigen_type[antigen]=i[5]
#     antigen_het_name[antigen]=i[6]
#     antigen_name[antigen]=i[7]
#     short_header[antigen]=i[8]
#     date[antigen]=i[9]	
#     compound[antigen]=i[10]
#     organism[antigen]=i[11]
#     heavy_species[antigen]=i[12]
#     light_species[antigen]=i[13]
#     antigen_species[antigen]=i[14]	
#     authors[antigen]=i[15]
#     resolution[antigen]=i[16]
#     method[antigen]=i[17]	
#     r_free[antigen]=i[18]	
#     r_factor[antigen]=i[19]	
#     scfv[antigen]=i[20]	
#     engineered[antigen]=i[21]	
#     heavy_subclass[antigen]=i[22]	
#     light_subclass[antigen]=i[23]	
#     light_ctype[antigen]=i[24]
#     affinity[antigen]=i[25]
#     delta_g[antigen]=i[26]
#     affinity_method[antigen]=i[27]
#     temperature[antigen]=i[28]
#     pmid[antigen]=i[29]




